#!/usr/bin/env python3
"""
build_report.py - per-build "what most likely changed" reports.

    python3 scripts/build_report.py

For each new build (vs its predecessor in the chain) writes
.generated/analysis/builds/<label>.md, inferred ONLY from added/deleted hand-written engine
functions - the unambiguous "a function appeared / vanished" signal, which
unlike fuzzy `changed` %s doesn't blur with codegen/folding drift. Functions are
grouped by owning class/namespace and each group is labelled:

  NEW       scope present in the build but not the predecessor (likely new feature)
  REMOVED   scope gone from the build (likely a dropped feature)
  REWORKED  scope kept, but functions added and/or removed

Reuses chain_report's per-pair diff machinery (reverse diff for deletions).
Run inside this repo's `nix develop` (needs objdiff-cli) the first time;
re-runs reuse existing reports.
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import chain_report as cr  # noqa: E402
import common as c  # noqa: E402

PER_SCOPE_CAP = 40


def scope_rows(added: list[str], deleted: list[str],
               scopes_prev: set[str], scopes_build: set[str]) -> list[dict]:
    groups: dict[str, dict] = defaultdict(lambda: {"added": [], "deleted": []})
    for n in added:
        groups[c.owning_scope(n)]["added"].append(c.split_qualified(n)[1])
    for n in deleted:
        groups[c.owning_scope(n)]["deleted"].append(c.split_qualified(n)[1])

    rows = []
    for scope, d in groups.items():
        if scope in scopes_build and scope not in scopes_prev:
            label = "NEW"
        elif scope in scopes_prev and scope not in scopes_build:
            label = "REMOVED"
        else:
            label = "REWORKED"
        rows.append({"scope": scope or "(global)", "label": label,
                     "added": sorted(d["added"]), "deleted": sorted(d["deleted"])})
    # most activity first
    rows.sort(key=lambda r: (len(r["added"]) + len(r["deleted"])), reverse=True)
    return rows


def render(prev: dict, build: dict, rows: list[dict], n_add: int, n_del: int) -> str:
    new = [r for r in rows if r["label"] == "NEW"]
    removed = [r for r in rows if r["label"] == "REMOVED"]
    reworked = [r for r in rows if r["label"] == "REWORKED"]

    md = [f"# Build {build['label']}  —  what most likely changed",
          "",
          f"_vs {prev['label']} · {prev.get('date', '?')} → {build.get('date', '?')}_",
          "",
          f"From **added/deleted hand-written engine functions only** "
          f"(+{n_add} / −{n_del}), grouped by owning class/namespace. "
          "Names can change through renaming, folding, or layout changes; these labels "
          "describe observed scopes, not proven feature additions/removals. Fuzzy `changed` is excluded.",
          ""]

    def headline(title: str, rs: list[dict]) -> list[str]:
        if not rs:
            return []
        items = ", ".join(f"`{r['scope']}`" for r in rs[:12])
        more = f" _+{len(rs) - 12} more_" if len(rs) > 12 else ""
        return [f"- **{title}:** {items}{more}"]

    md += ["## Likely changes at a glance", ""]
    md += headline(f"New ({len(new)})", new)
    md += headline(f"Removed ({len(removed)})", removed)
    md += headline(f"Reworked ({len(reworked)})", reworked)
    md += [""]

    for r in rows:
        tag = {"NEW": "🟢 NEW", "REMOVED": "🔴 REMOVED", "REWORKED": "🟡 REWORKED"}[r["label"]]
        counts = f"+{len(r['added'])}" + (f" / −{len(r['deleted'])}" if r["deleted"] else "")
        md += ["---", "", f"## {tag} · `{r['scope']}` ({counts})", ""]
        for leaf in r["added"][:PER_SCOPE_CAP]:
            md.append(f"- `+` `{leaf}`")
        if len(r["added"]) > PER_SCOPE_CAP:
            md.append(f"- _+{len(r['added']) - PER_SCOPE_CAP} more added_")
        for leaf in r["deleted"][:PER_SCOPE_CAP]:
            md.append(f"- `−` `{leaf}`")
        if len(r["deleted"]) > PER_SCOPE_CAP:
            md.append(f"- _+{len(r['deleted']) - PER_SCOPE_CAP} more deleted_")
        md.append("")
    return "\n".join(md) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description="Per-build 'what most likely changed' reports.")
    ap.add_argument("--with-generated", action="store_true",
                    help="include compiler-generated functions in added/deleted")
    args = ap.parse_args()

    versions = cr.ingested_ordered()
    if len(versions) < 2:
        sys.exit("build_report: need >= 2 ingested versions")
    out_dir = c.REPORTS_DIR / "builds"
    out_dir.mkdir(parents=True, exist_ok=True)

    for prev, build in zip(versions, versions[1:]):
        fa = cr.reportable_funcs(cr.ensure_report(build["label"], prev["label"]), args.with_generated)
        fb = cr.reportable_funcs(cr.ensure_report(prev["label"], build["label"]), args.with_generated)
        names_prev, names_build = set(fa), set(fb)
        added = sorted(names_build - names_prev)
        deleted = sorted(names_prev - names_build)
        scopes_prev = {c.owning_scope(n) for n in names_prev}
        scopes_build = {c.owning_scope(n) for n in names_build}
        rows = scope_rows(added, deleted, scopes_prev, scopes_build)
        (out_dir / f"{build['label']}.md").write_text(
            render(prev, build, rows, len(added), len(deleted)))
        c.log("build-report", f"{build['label']}: +{len(added)} / -{len(deleted)} "
                              f"across {len(rows)} scopes")


if __name__ == "__main__":
    main()
