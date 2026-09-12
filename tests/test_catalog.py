import base64
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CatalogTests(unittest.TestCase):
    def test_binary_release_matches_catalog_and_preserved_inputs(self):
        versions = json.loads((ROOT / "catalog/versions.json").read_text())
        release = json.loads((ROOT / "catalog/binary-release.json").read_text())
        assets = {asset["label"]: asset for asset in release["assets"]}
        bundled = {v["label"]: v for v in versions if "bundle_url" in v}
        self.assertEqual(set(assets), set(bundled))

        preserved_names = {
            "v0.10b-build802": "v0.100b-build802",
        }
        for label, asset in assets.items():
            version = bundled[label]
            self.assertEqual(version["bundle_url"], asset["url"])
            self.assertEqual(version["bundle_sha256"], asset["nix_hash"])
            self.assertEqual(set(asset["contents"]), {"survarium.exe", "survarium.pdb"})
            self.assertGreater(asset["size"], 0)
            self.assertRegex(asset["sha256"], r"^[0-9a-f]{64}$")
            sri = "sha256-" + base64.b64encode(bytes.fromhex(asset["sha256"])).decode()
            self.assertEqual(asset["nix_hash"], sri)
            self.assertEqual(
                asset["url"],
                f"{release['release_url'].replace('/tag/', '/download/')}/"
                f"{asset['asset_name']}",
            )

            historical = preserved_names.get(label, label)
            meta = json.loads(
                (ROOT / f"reports/2026-06/versions/{historical}/meta.json").read_text()
            )
            for name, details in asset["contents"].items():
                key = name.removeprefix("survarium.")
                self.assertEqual(details["size"], meta[key]["size"])
                self.assertEqual(details["sha256"], meta[key]["sha256"])

    def test_documented_diff_counts_match_chain_report(self):
        text = (ROOT / "observations/2026-09-12-version-diff-explanations.md").read_text()
        chain = json.loads((ROOT / "reports/2026-06/CHAIN_REPORT.json").read_text())
        rows = re.findall(
            r"\| (\d+) -> (\d+) \| ([\d,]+) \| ([\d,]+) \| ([\d,]+) \| ([\d,]+) \|",
            text,
        )
        documented = {
            (int(base), int(target)): tuple(int(value.replace(",", "")) for value in counts)
            for base, target, *counts in rows
        }
        expected = {}
        for pair in chain["steps"]:
            base = int(pair["from"].rsplit("build", 1)[1])
            target = int(pair["to"].rsplit("build", 1)[1])
            expected[(base, target)] = (
                len(pair["added"]),
                len(pair["deleted"]),
                len(pair["changed"]),
                pair["identical"],
            )
        self.assertEqual(documented, expected)


if __name__ == "__main__":
    unittest.main()
