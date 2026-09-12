#!/usr/bin/env python3
"""
add_version.py - ingest one Survarium build into the version database.

    python3 scripts/add_version.py <label> <source> [options]

<source> is either an InnoSetup installer (.exe) or a directory that already
contains survarium.exe + survarium.pdb. Steps:

  1. resolve source -> a dir holding survarium.{exe,pdb}
     (installer: innoextract into .generated/downloads/<label>/; directory: used as-is)
  2. vostok-delinker  -> .generated/builds/<label>/objects/   (per-function COFF .obj)
  3. pdb_parser       -> .generated/builds/<label>/structure/  (readable stubs; --no-structure to skip)
  4. write .generated/builds/<label>/meta.json (hashes, sizes, object count, ...)

The comparison chain is maintained in catalog/chain.json. Passing --base updates
its base label; ingestion does not append builds to the chain.

Folded-symbol naming: each version writes its own symbol map. For stable diffs
*against the base*, pass `--align-to <base-label>` so this build reuses the
base's folded-group names instead of choosing its own.

If <source> is omitted, the label is looked up in catalog/versions.json and the build is
fetched + extracted from archive.org via the flake (`nix build .#version-<label>`).

Run inside this repo's `nix develop` (provides the tools).
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as c  # noqa: E402


def resolve_source(label: str, source: Path, keep_cache: bool) -> tuple[Path, Path]:
    if source.is_dir():
        c.log("add", f"source is a directory: {source}")
        return c.find_exe_pdb(source)

    if not source.is_file():
        sys.exit(f"error: source {source} is neither a file nor a directory")

    # Installer: extract once into .generated/downloads/<label>/.
    c.require_tool(c.innoextract())
    dest = c.CACHE_DIR / label
    if dest.exists() and not keep_cache:
        shutil.rmtree(dest)
    dest.mkdir(parents=True, exist_ok=True)
    c.log("add", f"innoextract {source.name} -> {dest}")
    subprocess.run([c.innoextract(), "-d", str(dest), str(source)], check=True)
    return c.find_exe_pdb(dest)


def delink(label: str, exe: Path, pdb: Path, engine_path: str, align_to: str | None) -> tuple[Path, dict]:
    c.require_tool(c.delinker())
    out = c.VERSIONS_DIR / label / "objects"
    own_map = c.VERSIONS_DIR / label / "symbol-map.tsv"

    def run(flags: list[str]) -> None:
        own_map.unlink(missing_ok=True)
        if out.exists():
            shutil.rmtree(out)
        out.mkdir(parents=True, exist_ok=True)
        c.log("add", f"delinking {exe.name} -> {out}")
        subprocess.run(
            [c.delinker(),
             "--pdb-path", str(pdb),
             "--exe-path", str(exe),
             "--output-path", str(out),
             "--engine-path", engine_path,
             *flags],
            check=True,
        )

    write_own = ["--write-symbol-map", str(own_map)] if c.delinker_supports("--write-symbol-map") else []

    # Prefer aligning this build's folded-group names to the base's (stable diffs).
    aligned: list[str] = []
    alignment = {"requested": align_to, "actual": None, "status": "not-requested"}
    if align_to:
        base_map = c.VERSIONS_DIR / align_to / "symbol-map.tsv"
        if base_map.exists() and c.delinker_supports("--read-symbol-map"):
            aligned = ["--read-symbol-map", str(base_map)]
            alignment["map_sha256"] = c.sha256_file(base_map)
        else:
            alignment["status"] = "unavailable"
            c.log("add", f"--align-to {align_to!r}: base map or flag missing; writing own map")

    if aligned:
        c.log("add", f"aligning folded symbols to base {align_to!r}")
        try:
            run(aligned)
            alignment.update(actual=align_to, status="aligned")
            return out, alignment
        except subprocess.CalledProcessError as e:
            # Best-effort alignment: a bad cross-version map shouldn't block the
            # ingest - fall back to an unaligned delink that writes its own map.
            c.log("add", f"aligned delink failed (exit {e.returncode}); retrying unaligned")
            alignment.update(status="failed-fallback", exit_code=e.returncode)
    run(write_own)
    return out, alignment


def make_structure(label: str, pdb: Path, engine_path: str) -> str:
    if shutil.which(c.pdb_parser()) is None:
        c.log("add", "pdb_parser absent; skipping structure stubs")
        return "unavailable"
    out = c.VERSIONS_DIR / label / "structure"
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True, exist_ok=True)
    c.log("add", f"pdb_parser -> {out}")
    # Structure stubs are readability-only; the delinked objects (what we diff)
    # are already done. pdb_parser panics on some PDBs (e.g. "Enums cannot be of
    # different length"), so never let it sink the whole ingest.
    try:
        subprocess.run(
            [c.pdb_parser(),
             "--output-path", str(out),
             "--pdb-path", str(pdb),
             "--engine-path", engine_path],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        c.log("add", f"pdb_parser failed (exit {e.returncode}); skipping structure stubs")
        shutil.rmtree(out, ignore_errors=True)
        return "failed"
    return "generated"


def main() -> None:
    ap = argparse.ArgumentParser(description="Ingest one Survarium build into the version DB.")
    ap.add_argument("label", help="short version label, e.g. v0.10b-build802")
    ap.add_argument("source", type=Path, nargs="?",
                    help="installer .exe OR a dir with survarium.{exe,pdb}; "
                         "omit to fetch from versions.json via the flake")
    ap.add_argument("--engine-path", default=None,
                    help=f"PDB source-path prefix to strip (default: registry value or {c.ENGINE_PATH_DEFAULT})")
    ap.add_argument("--align-to", metavar="LABEL",
                    help="reuse this base version's folded-symbol map for stable diffs")
    ap.add_argument("--base", action="store_true", help="record this version as the matching base")
    ap.add_argument("--no-structure", action="store_true", help="skip pdb_parser structure stubs")
    ap.add_argument("--keep-cache", action="store_true",
                    help="reuse an existing .generated/downloads/<label> extract")
    ap.add_argument("--force", action="store_true", help="re-ingest even if meta.json already exists")
    args = ap.parse_args()
    if args.align_to == args.label:
        ap.error("--align-to must name a different build")

    entry = c.registry_entry(args.label) or {}
    if not entry.get("symbols", True):
        sys.exit(f"error: {args.label} has no PDB; use deps_report.py")
    engine_path = args.engine_path or entry.get("engine_path") or c.ENGINE_PATH_DEFAULT

    meta_path = c.VERSIONS_DIR / args.label / "meta.json"
    objects_path = meta_path.parent / "objects"
    if meta_path.exists() and any(objects_path.rglob("*.obj")) and not args.force:
        c.log("add", f"{args.label} already ingested; --force to redo with new inputs/options")
        cfg = c.load_config()
        if args.base:
            cfg["base"] = args.label
            c.save_config(cfg)
        return

    if args.source is not None:
        exe, pdb = resolve_source(args.label, args.source, args.keep_cache)
    elif entry:
        c.log("add", f"fetching {args.label!r} through the flake")
        src_dir = c.fetch_from_flake(args.label)
        exe, pdb = c.find_exe_pdb(src_dir)
    else:
        sys.exit(f"error: no source given and {args.label!r} not in versions.json")

    meta_path.unlink(missing_ok=True)
    tool = c.tool_identity(c.delinker())
    objects, alignment = delink(args.label, exe, pdb, engine_path, args.align_to)
    n_objects = sum(1 for _ in objects.rglob("*.obj"))
    if n_objects == 0:
        sys.exit("error: delinker produced no objects; ingestion is incomplete")
    structure_status = "skipped"
    shutil.rmtree(meta_path.parent / "structure", ignore_errors=True)
    if not args.no_structure:
        structure_status = make_structure(args.label, pdb, engine_path)

    meta = {
        "label": args.label,
        "source": str(args.source.resolve()) if args.source else (entry.get("url") or "flake"),
        "engine_path": engine_path,
        "aligned_to": alignment["actual"],
        "alignment": alignment,
        "structure_status": structure_status,
        "delinker": tool,
        "flake_lock_sha256": c.sha256_file(c.REPO_DIR / "flake.lock"),
        "script_sha256": c.sha256_file(Path(__file__)),
        "exe": {"name": exe.name, "size": exe.stat().st_size, "sha256": c.sha256_file(exe)},
        "pdb": {"name": pdb.name, "size": pdb.stat().st_size, "sha256": c.sha256_file(pdb)},
        "n_objects": n_objects,
        "added": c.now_iso(),
    }
    meta_path.write_text(json.dumps(meta, indent=2) + "\n")

    cfg = c.load_config()
    if args.base:
        cfg["base"] = args.label
        c.log("add", f"base version = {args.label!r}")
        c.save_config(cfg)

    c.log("add", f"done: {args.label}  ({n_objects} objects); chain is configured in catalog/chain.json")


if __name__ == "__main__":
    main()
