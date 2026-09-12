import base64
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CatalogTests(unittest.TestCase):
    def test_release_directories_and_builds_are_fully_accounted(self):
        releases = json.loads((ROOT / "catalog/releases.json").read_text())["versions"]
        versions = json.loads((ROOT / "catalog/versions.json").read_text())
        extra = json.loads((ROOT / "catalog/extra_builds.json").read_text())
        release_by_name = {item["version"]: item for item in releases}
        directories = {p.name for p in (ROOT / "versions").iterdir()
                       if p.is_dir() and p.name != "wiki"}
        self.assertEqual(directories, set(release_by_name))
        self.assertTrue(all((ROOT / "versions" / name / "README.md").is_file()
                            for name in directories))

        for build in versions + extra:
            release = build["release"]
            self.assertIn(build["label"], release_by_name[release]["builds"])
            build_dir = str(build["build"]) if build.get("build") is not None else "unknown"
            metadata = ROOT / "versions" / release / "builds" / build_dir / "metadata.json"
            self.assertTrue(metadata.is_file(), build["label"])
            stored = json.loads(metadata.read_text())
            self.assertEqual(stored["label"], build["label"])
            self.assertEqual(stored["release"], release)

    def test_binary_release_matches_catalog_and_version_metadata(self):
        versions = json.loads((ROOT / "catalog/versions.json").read_text())
        release = json.loads((ROOT / "catalog/binary-release.json").read_text())
        assets = {asset["label"]: asset for asset in release["assets"]}
        bundled = {v["label"]: v for v in versions if "bundle_url" in v}
        self.assertEqual(set(assets), set(bundled))

        for label, asset in assets.items():
            version = bundled[label]
            self.assertEqual(version["bundle_url"], asset["url"])
            self.assertEqual(version["bundle_sha256"], asset["nix_hash"])
            self.assertEqual(set(asset["contents"]), {"survarium.exe", "survarium.pdb"})
            sri = "sha256-" + base64.b64encode(bytes.fromhex(asset["sha256"])).decode()
            self.assertEqual(asset["nix_hash"], sri)
            self.assertEqual(
                asset["url"],
                f"{release['release_url'].replace('/tag/', '/download/')}/{asset['asset_name']}",
            )
            meta = json.loads((ROOT / "versions" / version["release"] / "builds" /
                               str(version["build"]) / "metadata.json").read_text())
            for filename, details in asset["contents"].items():
                key = filename.removeprefix("survarium.")
                self.assertEqual(details["size"], meta[key]["size"])
                self.assertEqual(details["sha256"], meta[key]["sha256"])
                self.assertEqual(details["size"], version[key]["size"])
                self.assertEqual(details["sha256"], version[key]["sha256"])

    def test_every_chain_transition_has_complete_canonical_evidence(self):
        labels = json.loads((ROOT / "catalog/chain.json").read_text())["versions"]
        catalog = {v["label"]: v for v in
                   json.loads((ROOT / "catalog/versions.json").read_text())}
        expected = []
        for base, target in zip(labels, labels[1:]):
            source = catalog[base]["release"]
            destination = catalog[target]["release"]
            directory = ROOT / "versions" / destination / "changes-from" / source
            expected.append(directory)
            for name in ("README.md", "functions.json", "object-summary.json",
                         "object-summary.md", "symbols-by-scope.md"):
                self.assertTrue((directory / name).is_file(), directory / name)
            functions = json.loads((directory / "functions.json").read_text())
            self.assertEqual(functions["base"]["label"], base)
            self.assertEqual(functions["target"]["label"], target)
            for status in ("added", "deleted", "changed"):
                self.assertEqual(functions["counts"][status], len(functions[status]))
            readme = (directory / "README.md").read_text()
            match = re.search(
                r"Function accounting: \*\*(\d+) added, (\d+) deleted, "
                r"(\d+) changed, and (\d+) identical\*\*",
                readme,
            )
            self.assertIsNotNone(match, directory)
            self.assertEqual(tuple(map(int, match.groups())), tuple(
                functions["counts"][key]
                for key in ("added", "deleted", "changed", "identical")
            ))

        actual = list((ROOT / "versions").glob("*/changes-from/*/functions.json"))
        self.assertEqual(len(actual), len(expected))


if __name__ == "__main__":
    unittest.main()
