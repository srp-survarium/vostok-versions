#!/usr/bin/env python3
"""
flags_report.py - compare per-project build flags across versions.

    python3 scripts/flags_report.py

Uses the project's `pdb_build_info` tool (from vostok-pdb-parser) to recover, per
link-unit "project", the cl.exe compile flags / LTCG state from each version's
PDB, and writes reports/BUILD_FLAGS.md:

  - per consecutive step: which projects changed flags (DIFF-FLAGS / PARTIAL),
  - an engine-lib (vostok_*) matrix of the libs whose flags/LTCG *vary* across
    versions (the constant ones are summarized in one line).

LTCG matters for matching: an LTCG lib has no per-TU command line (the compiler
defers codegen to link), which is the "LTCG wall" that makes those functions
hard to match. Needs only nix + pdb_build_info (no devShell).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as c  # noqa: E402

REPORTS_DIR = c.REPORTS_DIR


def pdb_build_info() -> str:
    for cand in (os.environ.get("PDB_BUILD_INFO"), "pdb_build_info"):
        if cand and shutil.which(cand):
            return cand
    sys.exit("pdb_build_info not found (run in devShell or set PDB_BUILD_INFO)")


def symbol_versions() -> list[dict]:
    """PDB-bearing entries in the explicitly configured order."""
    return c.chain_versions()


def project_configs(tool: str, pdb: Path) -> dict[str, str]:
    out = subprocess.run([tool, "--pdb", str(pdb)], capture_output=True, text=True, check=True).stdout
    cfg, proj = {}, None
    for line in out.splitlines():
        m = re.match(r"^project : (.+)$", line)
        if m:
            proj = m.group(1).strip()
        elif proj and line.startswith("config  : "):
            cfg[proj] = line[len("config  : "):].strip()
    return cfg


def full_flag_projects(tool: str, pdb: Path, needle: str) -> set[str]:
    """Projects whose FULL command line (`--full`, not the CRT/opt summary)
    contains `needle` - e.g. '-fp:fast', which the default summary omits."""
    out = subprocess.run([tool, "--pdb", str(pdb), "--full"], capture_output=True, text=True, check=True).stdout
    proj, hits = None, set()
    for line in out.splitlines():
        m = re.match(r"^project : (.+)$", line)
        if m:
            proj = m.group(1).strip()
        elif proj and line.lstrip().startswith("cmd") and (needle in line or needle.replace("-", "/", 1) in line):
            hits.add(proj)
    return hits


def changed_projects(tool: str, base_pdb: Path, target_pdb: Path) -> list[tuple[str, str]]:
    out = subprocess.run([tool, "--pdb", str(target_pdb), "--compare", str(base_pdb)],
                         capture_output=True, text=True, check=True).stdout
    changed = []
    for line in out.splitlines():
        if line.startswith("── ") and "[MATCH]" not in line:
            name = line[3:].split("  ")[0].strip()
            m = re.search(r"\[([^\]]+)\]", line)
            changed.append((name, m.group(1) if m else "?"))
    return changed


def normalize(cfg: str) -> str:
    """Drop per-file-count notes so a rebuild that merely LTCG'd a different
    subset of files (same flag set) doesn't read as a flag change. Configs that
    carry no flag info ('(none)', absent) collapse to '' so presence-only changes
    of flagless libs don't read as flag changes either."""
    cfg = re.sub(r"\s*\(\+\d+ files[^)]*\)", "", cfg)
    cfg = re.sub(r"\s+", " ", cfg).strip()
    return "" if cfg in ("[no cmdline] (none)", "(none)", "—") else cfg


def runs(labels: list[str], builds: dict, norm: dict[str, str]) -> list[tuple[str, str]]:
    """Collapse consecutive versions sharing a config into (build-range, config)."""
    groups: list[list] = []
    for lab in labels:
        cf = norm.get(lab, "") or "_(absent / no per-TU flags)_"
        if groups and groups[-1][1] == cf:
            groups[-1][0].append(builds[lab])
        else:
            groups.append([[builds[lab]], cf])
    out = []
    for bs, cf in groups:
        rng = str(bs[0]) if len(bs) == 1 else f"{bs[0]}–{bs[-1]}"
        out.append((rng, cf))
    return out


def main() -> None:
    argparse.ArgumentParser(description="Compare recorded compiler flags for catalog/chain.json.").parse_args()
    tool = pdb_build_info()
    versions = symbol_versions()
    if len(versions) < 2:
        sys.exit("flags_report: need >= 2 symbol-bearing versions")
    labels = [v["label"] for v in versions]
    builds = {v["label"]: v["build"] for v in versions}
    pdbs = {v["label"]: c.fetch_from_flake(v["label"]) / "survarium.pdb" for v in versions}

    configs = {lab: project_configs(tool, pdbs[lab]) for lab in labels}
    steps = [(a, b, changed_projects(tool, pdbs[a], pdbs[b])) for a, b in zip(labels, labels[1:])]

    # genuine flag changes: normalized config differs across versions (file-count
    # only diffs collapse away). Split engine (vostok_*) from other libs.
    all_projs = sorted({p for cfg in configs.values() for p in cfg})
    norm = {p: {lab: normalize(configs[lab].get(p, "")) for lab in labels} for p in all_projs}
    varying = [p for p in all_projs if len(set(norm[p].values())) > 1]
    eng_var = [p for p in varying if p.startswith("vostok_")]
    other_var = [p for p in varying if not p.startswith("vostok_")]
    eng_const_ltcg = [p for p in all_projs
                      if p.startswith("vostok_") and p not in varying
                      and all("LTCG" in configs[lab].get(p, "") for lab in labels)]

    md = ["# Build-flags comparison across versions", "",
          "Per link-unit `cl.exe` flags / LTCG state from each PDB (`pdb_build_info`), "
          "by build number. `LTCG` = whole-program optimized, no per-TU command line "
          "(the matching \"LTCG wall\"). File-count-only diffs are normalized out.", ""]

    def section(title: str, projs: list[str]) -> list[str]:
        out = [f"## {title} ({len(projs)})", ""]
        if not projs:
            return out + ["_none_", ""]
        for p in projs:
            out.append(f"### `{p}`")
            for rng, cf in runs(labels, builds, norm[p]):
                out.append(f"- **{rng}:** {cf}")
            out.append("")
        return out

    md += section("Engine libs (vostok/*) with changed flags", eng_var)
    md += section("Other libs with changed flags", other_var)
    md += [f"Engine projects with unchanged configurations and an LTCG flag in every selected build: "
           f"{len(eng_const_ltcg)}.", ""]

    # Optimization landscape + fp model, computed from the data.
    noltcg = [p for p in all_projs if p.startswith("vostok_")
              and any(configs[lab].get(p) and "LTCG" not in configs[lab][p] for lab in labels)]
    fp = {lab: full_flag_projects(tool, pdbs[lab], "-fp:fast") for lab in labels}
    md += ["## Observed optimization flags", "",
           "Projects with at least one recorded configuration without an LTCG label: "
           + (", ".join(f"`{p}`" for p in noltcg) or "none") + ".", "",
           "The absence of a command line does not establish an optimization level or floating-point mode.",
           "", "### `/fp:fast` observations", "",
           "Each row lists only builds whose recorded command lines contain the flag. "
           "An unlisted build may have no recorded command line.", "",
           "| Project | Builds with the flag observed |", "| --- | --- |"]
    for project in sorted(set().union(*fp.values())):
        md.append(f"| `{project}` | " + ", ".join(lab for lab in labels if project in fp[lab]) + " |")
    md.append("")

    md += ["## Raw per-step tool labels (incl. file-count-only diffs)", "",
           "| step | projects flagged by `pdb_build_info --compare` |", "| --- | --- |"]
    for a, b, ch in steps:
        cell = ", ".join(f"`{n}` ({lbl})" for n, lbl in ch) if ch else "_none_"
        md.append(f"| {builds[a]} → {builds[b]} | {cell} |")

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    (REPORTS_DIR / "BUILD_FLAGS.md").write_text("\n".join(md) + "\n")
    (REPORTS_DIR / "BUILD_FLAGS.json").write_text(json.dumps({
        "generated_at": c.now_iso(), "tool": c.tool_identity(tool),
        "flake_lock_sha256": c.sha256_file(c.REPO_DIR / "flake.lock"),
        "builds": {lab: {"pdb_sha256": c.sha256_file(pdbs[lab]),
                         "configs": configs[lab], "fp_fast_projects": sorted(fp[lab])}
                   for lab in labels},
    }, indent=2) + "\n")
    c.log("flags", f"{len(varying)} libs with real flag changes "
                   f"({len(eng_var)} engine, {len(other_var)} other) -> reports/BUILD_FLAGS.md")


if __name__ == "__main__":
    main()
