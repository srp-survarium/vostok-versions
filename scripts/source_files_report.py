#!/usr/bin/env python3
"""Compare the source-file checksums recorded in the configured builds' PDBs.

Includes headers and every file-checksum record under each catalog source root.
Output contains complete per-build checksum tables, per-pair file lists, counts,
and input/tool provenance. PDB-only paths describe debug-record coverage, not
proof of source-tree addition/deletion. Missing/incomparable hashes are unknown.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as c  # noqa: E402

ALGORITHMS = {"md5": 32, "sha1": 40, "sha256": 64}
STATUSES = ("changed", "unchanged", "added", "removed", "unknown")


def parse_checksums(text: str) -> dict[str, dict]:
    records = {}
    for line_number, line in enumerate(text.splitlines(), 1):
        if not line:
            continue
        fields = line.split("\t")
        if len(fields) != 3:
            raise ValueError(f"invalid checksum row {line_number}")
        algorithm, digest, raw_path = fields
        algorithm, digest = algorithm.lower(), digest.lower()
        path = raw_path.replace("\\", "/").lower()
        if (not path or PurePosixPath(path).is_absolute() or ":" in path
                or any(part in ("", ".", "..") for part in path.split("/"))):
            raise ValueError(f"unsafe/non-relative source path: {raw_path!r}")
        if algorithm == "none":
            if digest:
                raise ValueError(f"unexpected digest for checksum kind none: {path}")
        elif algorithm not in ALGORITHMS or not re.fullmatch(
                "[0-9a-f]{" + str(ALGORITHMS[algorithm]) + "}", digest):
            raise ValueError(f"invalid {algorithm} checksum for {path}")
        record = {"algorithm": algorithm, "digest": digest}
        if path in records and records[path] != record:
            raise ValueError(f"conflicting checksum records for {path}")
        records[path] = record
    if not records:
        raise ValueError("no source checksum records; check the source prefix and tool")
    return dict(sorted(records.items()))


def file_kind(path: str) -> str:
    suffix = PurePosixPath(path).suffix
    if suffix in (".c", ".cc", ".cpp", ".cxx", ".c++"):
        return "source"
    if suffix in (".h", ".hh", ".hpp", ".hxx", ".inl", ".ipp", ".tpp"):
        return "header"
    return "other"


def compare(base: dict, target: dict) -> list[dict]:
    rows = []
    for path in sorted(base.keys() | target.keys()):
        before, after = base.get(path), target.get(path)
        reason = None
        if before is None:
            status = "added"
        elif after is None:
            status = "removed"
        elif "none" in (before["algorithm"], after["algorithm"]):
            status, reason = "unknown", "checksum not recorded on one or both sides"
        elif before["algorithm"] != after["algorithm"]:
            status, reason = "unknown", "checksum algorithms differ"
        else:
            status = "unchanged" if before["digest"] == after["digest"] else "changed"
        rows.append({"path": path, "status": status, "kind": file_kind(path),
                     "scope": "engine" if path.startswith("vostok/") else "third_party",
                     "base": before, "target": after, "reason": reason})
    return rows


def counts(rows: list[dict]) -> dict:
    counter = Counter(row["status"] for row in rows)
    return {status: counter[status] for status in STATUSES}


def expected_pdb_hash(entry: dict) -> str | None:
    return entry.get("pdb", {}).get("sha256")


def write_pair(output: Path, base: str, target: str, rows: list[dict]) -> dict:
    pair = f"{base}__{target}"
    directory = output / "pairs" / pair
    directory.mkdir(parents=True)
    engine = [r for r in rows if r["scope"] == "engine"]
    third_party = [r for r in rows if r["scope"] == "third_party"]
    summary = {"base": base, "target": target, "all": counts(rows),
               "engine": counts(engine), "third_party": counts(third_party),
               "engine_source": counts([r for r in engine if r["kind"] == "source"]),
               "engine_header": counts([r for r in engine if r["kind"] == "header"]),
               "engine_other": counts([r for r in engine if r["kind"] == "other"])}
    md = [f"# {base} → {target}: source-file checksums", "",
          "Changed/unchanged compare checksums at the same normalized path. "
          "Added/removed mean present in only one PDB's selected file records. "
          "They do not prove repository creation/deletion. "
          "Unknown means absent checksums or incompatible algorithms.", "",
          "Source contents are not embedded here; changed hashes cannot identify changed lines "
          "or distinguish comments/line endings from functional edits.", "",
          "| Scope | Changed | Unchanged | Added | Removed | Unknown |",
          "| --- | ---: | ---: | ---: | ---: | ---: |"]
    for scope in ("all", "engine", "engine_source", "engine_header", "engine_other", "third_party"):
        md.append(f"| {scope} | " + " | ".join(str(summary[scope][s]) for s in STATUSES) + " |")
    md += ["", "[Complete per-file records and both hashes](files.tsv). "
           "Each status also has an exhaustive plain-text path list in this directory."]
    for status in STATUSES:
        selected = [r for r in rows if r["status"] == status]
        (directory / f"{status}.txt").write_text("".join(r["path"] + "\n" for r in selected))
        # Changed paths are the main reading surface; include every one in Markdown.
        if status == "changed":
            md += ["", "## Changed engine files", ""]
            paths = [r["path"] for r in selected if r["scope"] == "engine"]
            md += [f"- `{p}`" for p in paths] or ["None."]
            md += ["", "## Changed third-party files", ""]
            paths = [r["path"] for r in selected if r["scope"] == "third_party"]
            md += [f"- `{p}`" for p in paths] or ["None."]
    table = ["status\tscope\tkind\tpath\tbase_algorithm\tbase_digest\ttarget_algorithm\ttarget_digest\treason"]
    for row in rows:
        before, after = row["base"] or {}, row["target"] or {}
        table.append("\t".join([row["status"], row["scope"], row["kind"], row["path"],
                                before.get("algorithm", ""), before.get("digest", ""),
                                after.get("algorithm", ""), after.get("digest", ""), row["reason"] or ""]))
    (directory / "files.tsv").write_text("\n".join(table) + "\n")
    (directory / "README.md").write_text("\n".join(md) + "\n")
    (directory / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdb", action="append", default=[], metavar="LABEL=PATH",
                        help="use this local PDB; other selected builds are fetched through Nix")
    parser.add_argument("--labels", nargs="+", help="explicit subset/order; default: full configured chain")
    parser.add_argument("--tool", default=os.environ.get("PDB_DIFF", "pdb_diff"),
                        help="pdb_diff with --all-files and --list-checksums support")
    parser.add_argument("--output", type=Path, default=c.REPORTS_DIR / "source-files",
                        help="new output directory; existing directories are never overwritten")
    parser.add_argument("--coverage-note", default="", help="record the reason for a limited run")
    args = parser.parse_args()
    configured = c.chain_versions()
    by_label = {v["label"]: v for v in configured}
    labels = args.labels or list(by_label)
    if len(labels) < 2 or len(set(labels)) != len(labels) or set(labels) - by_label.keys():
        parser.error("select at least two distinct labels from the configured chain")
    overrides = {}
    for value in args.pdb:
        label, separator, path = value.partition("=")
        if not separator or not path or label not in labels or label in overrides:
            parser.error(f"invalid or duplicate --pdb: {value}")
        overrides[label] = Path(path).resolve()
    if args.output.exists():
        parser.error(f"output already exists: {args.output}; choose a new --output")
    tool = c.tool_identity(args.tool)
    help_text = subprocess.run([args.tool, "--help"], capture_output=True, text=True, check=True).stdout
    if not all(flag in help_text for flag in ("--all-files", "--list-checksums")):
        parser.error("pdb_diff lacks --all-files/--list-checksums; use this repository's patched Nix package")
    output = args.output.resolve()
    (output / "builds").mkdir(parents=True)
    (output / "INCOMPLETE").write_text("Incomplete until the final manifest and index are written.\n")
    builds, checksums = {}, {}
    for label in labels:
        entry = by_label[label]
        pdb = overrides.get(label)
        if pdb is None:
            pdb = c.fetch_from_flake(label) / "survarium.pdb"
        digest = c.sha256_file(pdb)
        expected = expected_pdb_hash(entry)
        if expected and digest != expected:
            sys.exit(f"error: PDB hash does not match catalog metadata for {label}: {pdb}")
        prefix = entry["engine_path"]
        c.log("sources", f"reading every checksum under {prefix}: {label}")
        result = subprocess.run([args.tool, "--target-pdb", str(pdb), "--target-engine-path", prefix,
                                 "--all-files", "--list-checksums"],
                                capture_output=True, text=True, check=True)
        records = parse_checksums(result.stdout)
        checksums[label] = records
        table = "".join(f"{r['algorithm']}\t{r['digest']}\t{path}\n" for path, r in records.items())
        table_path = output / "builds" / f"{label}.tsv"
        table_path.write_text(table)
        builds[label] = {"pdb_path": str(pdb), "pdb_sha256": digest,
                         "matches_catalog_pdb": digest == expected if expected else None,
                         "catalog_entry": entry, "source_root": prefix,
                         "records": len(records), "algorithms": dict(Counter(r["algorithm"] for r in records.values())),
                         "engine_records": sum(p.startswith("vostok/") for p in records),
                         "table": table_path.relative_to(output).as_posix(),
                         "table_sha256": c.sha256_file(table_path), "tool_warnings": result.stderr}
    pairs = [write_pair(output, a, b, compare(checksums[a], checksums[b]))
             for a, b in zip(labels, labels[1:])]
    manifest = {"generated_at": c.now_iso(), "method": "PDB file checksums; all files including headers",
                "normalization": "Case-insensitive Windows paths, each catalog source root stripped, slash separators. No suffix/version/path-move inference.",
                "scope": "Files under each catalog source root; engine = vostok/, third_party = remaining paths. PDB-omitted files are outside coverage.",
                "configured_chain": list(by_label), "selected_chain": labels,
                "unselected_builds": [label for label in by_label if label not in labels],
                "coverage_note": args.coverage_note,
                "complete_chain": labels == list(by_label), "tool": tool,
                "script_sha256": c.sha256_file(Path(__file__)),
                "flake_lock_sha256": c.sha256_file(c.REPO_DIR / "flake.lock"),
                "flake_sha256": c.sha256_file(c.REPO_DIR / "flake.nix"),
                "tool_patch_sha256": c.sha256_file(c.REPO_DIR / "patches/pdb-diff-all-files.patch"),
                "builds": builds, "pairs": pairs}
    md = ["# Source-file checksum comparisons", "",
          f"Generated {manifest['generated_at']}. "
          f"{'Full configured chain' if manifest['complete_chain'] else 'Explicit subset of the configured chain'}: "
          f"{len(builds)} PDBs, {len(pairs)} comparison(s).", "",
          "Every checksum record under the catalog's source root is included, including headers. "
          "Paths are normalized across the 2013/2014 build-machine root change. "
          "Engine means `vostok/`; remaining paths are grouped as third-party. "
          "Files absent from debug records are outside this analysis.", "",
          "**Changed** means different hashes of the same algorithm at the same path. "
          "**Unchanged** means equal recorded hashes. **Added/removed** mean present only in the "
          "target/base PDB coverage. **Unknown** means no comparable checksum. "
          "These counts measure recorded source contents, independently of function/object changes. "
          "They cannot identify changed lines, establish behavior, or exclude comments/line-ending changes.", "",
          "## Engine files (sources and headers)", "",
          "| Comparison | Changed | Unchanged | Added | Removed | Unknown |",
          "| --- | ---: | ---: | ---: | ---: | ---: |"]
    if args.coverage_note:
        md[4:4] = [args.coverage_note, ""]
    for pair in pairs:
        name = f"{pair['base']}__{pair['target']}"
        md.append(f"| [{pair['base']} → {pair['target']}](pairs/{name}/README.md) | " +
                  " | ".join(str(pair["engine"][s]) for s in STATUSES) + " |")
    md += ["", "## Source-file versus header changes", "",
           "| Comparison | Changed source files | Changed headers/inlines | Changed other engine files | Changed third-party files |",
           "| --- | ---: | ---: | ---: | ---: |"]
    for pair in pairs:
        md.append(f"| {pair['base']} → {pair['target']} | " + " | ".join(
            str(pair[k]["changed"]) for k in ("engine_source", "engine_header", "engine_other", "third_party")) + " |")
    md += ["", "## Per-build checksum coverage", "",
          "| Build | All files | Engine files | Checksum kinds | Matches catalog PDB SHA-256 |",
           "| --- | ---: | ---: | --- | --- |"]
    for label, build in builds.items():
        verified = {True: "yes", False: "no", None: "no catalog reference"}[build["matches_catalog_pdb"]]
        md.append(f"| [{label}]({build['table']}) | {build['records']} | {build['engine_records']} | "
                  f"{', '.join(build['algorithms'])} | {verified} |")
    if manifest["unselected_builds"]:
        md += ["", "## Configured builds not analyzed in this run", "",
               *[f"- `{label}`" for label in manifest["unselected_builds"]], "",
               "The comparison above spans the explicitly selected endpoints. It does not "
               "replace the missing consecutive-build comparisons or localize changes to an intermediate release."]
    md += ["", "Each comparison directory includes complete `changed.txt`, `unchanged.txt`, "
           "`added.txt`, `removed.txt`, and `unknown.txt` lists. `files.tsv` records every path, "
           "status, scope, file kind, and both hashes. [manifest.json](manifest.json) records "
           "PDB SHA-256 identities, table hashes, selected coverage, tool and script identities, "
           "and all comparison counts."]
    (output / "README.md").write_text("\n".join(md) + "\n")
    manifest["files"] = {p.relative_to(output).as_posix(): c.sha256_file(p)
                         for p in sorted(output.rglob("*")) if p.is_file() and p.name != "INCOMPLETE"}
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    (output / "INCOMPLETE").unlink()
    c.log("sources", f"{len(builds)} PDBs, {len(pairs)} comparisons -> {output}")


if __name__ == "__main__":
    main()
