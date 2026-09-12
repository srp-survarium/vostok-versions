# vostok-versions

Cross-version analysis of **Survarium** (Vostok Engine / X-Ray 2.0) builds —
from the first archived dev build (**0.100b**, May 2013) to the last Steam build
(**0.69d0**, 2022). Two things, at two levels of depth:

1. **Function-level diffs** — for builds that shipped a **PDB**, delink each
   `survarium.exe` into per-function COFF objects and diff version→version to see
   exactly which functions are unchanged, churned, or new.
2. **Dependency analysis** — for **any** `survarium.exe` (PDB or not), read which
   third-party libraries are linked and at what version, straight from the binary.

The committed reports record investigations from June 2026. Build availability,
local holdings, and tool output may have changed since then. See
[`reports/README.md`](reports/README.md) for their scope and how to reproduce them.

## Two tiers of builds

| tier | registry | what you can do | how to get it |
|---|---|---|---|
| **installer** | `versions.json` | **function diff** when a PDB is present; deps for all builds | `nix build .#version-<label>` (extract `survarium.exe` and any PDB) |
| **exe-only** | `extra_builds.json` | **deps only** | `nix build .#"<token>"` (just the exe, via an archive.org `view_archive.php` member URL) |

Both registries are plain JSON, read by *both* `flake.nix` and the Python scripts.
The installer registry contains eight PDB-bearing builds and the stripped
`v0.23h-build2285` (`symbols: false`); that last build supports dependency analysis
only. `config.json` records the eight-build function-diff chain.
What exists, what we hold, and what's still missing/locked is catalogued in
[`reports/MISSING_BUILDS.md`](reports/MISSING_BUILDS.md).

## Reports

| report | what it answers |
|---|---|
| [`reports/DEPENDENCY_VERSIONS.md`](reports/DEPENDENCY_VERSIONS.md) | **what each exe brings** — every third-party lib + version across builds (0.100b → 2022), incl. the 0.25–0.31 sweep. `scripts/deps_report.py` |
| [`reports/CHANGES_NARRATIVE.md`](reports/CHANGES_NARRATIVE.md) | the engine's evolution, interpreted (gameplay + deps) |
| [`reports/CHAIN_REPORT.md`](reports/CHAIN_REPORT.md) + [`reports/builds/`](reports/builds/) | **function-level diffs** per consecutive PDB build. `scripts/chain_report.py`, `build_report.py` |
| [`reports/BUILD_FLAGS.md`](reports/BUILD_FLAGS.md) | per-project `cl.exe` flags / LTCG state from each PDB. `scripts/flags_report.py` |
| [`reports/MISSING_BUILDS.md`](reports/MISSING_BUILDS.md) | **what we have / what's missing / what's `.sup`-locked** |
| [`docs/extracting-exes.md`](docs/extracting-exes.md) | how to pull a `survarium.exe` out of any archive.org item (+ the full format classification) |
| [`docs/finding-builds.md`](docs/finding-builds.md) | how to hunt the still-missing builds |

## Getting builds with the flake

`nix develop` puts the toolchain on PATH (`vostok-delinker`, `pdb_parser`,
`objdiff-cli`, `innoextract`, `p7zip`, `binutils`, `python3`). Then:

    # full build (PDB tier) — fetch installer, innoextract to survarium.{exe,pdb}
    nix build .#version-v0_100b-build802

    # just the exe, by bare version token (quote the dots!)
    nix build '.#"0.26g0"'     # -> result/0.26g0.exe
    nix build '.#"0.69d0"'     # -> result/0.69d0.exe   (2022 x64)
    nix build .#all            # -> result/ with every <token>.exe

    nix develop '.#"0.34a0"'   # shell with $SURV_EXE -> that exe
    nix develop .#all          # shell with $SURV_EXES -> dir of all exes

Tokens: `0.100b 0.1.1a 0.1.1b 0.1.1c 0.1.1e 0.20e 0.20f 0.21d 0.23h` (PDB tier,
extracted from their installer) + `0.26e0 0.26g0 0.34a0 0.69d0` (exe tier, ~13 MB
member fetch). The `.sup`-locked 0.32–0.68 line can't be a target — see
`MISSING_BUILDS.md` / `docs/extracting-exes.md`.

To add a build: append `url` + `sha256` (PDB tier, `nix-prefetch-url`) to
`versions.json` and run `add_version.py`; or `exe_url` + `exe_sha256` (exe tier,
`nix store prefetch-file '<member-url>'`) to `extra_builds.json`.

## Function-diff workflow (PDB tier)

    python3 scripts/add_version.py v0.100b-build802 --force
    python3 scripts/add_version.py v0.1.1a-build816 --force --align-to v0.100b-build802
    python3 scripts/diff_versions.py v0.100b-build802 v0.1.1a-build816

`--align-to <base>` reuses the base's folded-symbol names so diffs stay stable. A
version diffed against itself must report 100% on every function — the end-to-end
sanity check.

The examples use `--force` because this repository tracks `meta.json`, but ignores
the delinked objects. Without it, `add_version.py` sees the existing metadata and
skips ingestion even on a fresh clone. Diffing regenerates `objdiff.json` and the
dummy object automatically; those files only describe the local object layout.

## Packaging builds for upload

`scripts/package_builds.sh <archive.zip> [out-dir]` repackages every game-tree
build inside a big local archive into upload-ready `vostok_engine_v<ver>_<date>.zip`
files (version + date read from each exe; build#/internal-id come from the Steam
depot, not the binary). Output lands in `survarium-uploads/` (gitignored).

## Layout

    versions.json          installer registry (label, url, sha256, base, engine_path, symbols)
    extra_builds.json      exe-tier registry (label, exe_url, exe_sha256, date, arch)
    config.json            { "base": <label>, "versions": [...] }  (diff chain)
    flake.nix              version-<label> (full) + .#"<token>" / .#all (exes) + toolchain
    scripts/
      common.py            shared helpers + tool resolution
      add_version.py       installer/dir -> delink -> objects + structure + meta.json
      diff_versions.py     base,target -> objdiff -> summary.{md,json}
      build_report.py      per-build function report
      chain_report.py      consecutive-build diff chain
      flags_report.py      cl.exe flags / LTCG from PDBs
      deps_report.py       third-party dependency versions from each exe
      package_builds.sh    repackage local game trees for archive.org upload
    versions/<label>/      objects/ (gitignored), structure/ (gitignored), symbol-map.tsv, meta.json
    diffs/<base>__<target>/  summary.{md,json} (objdiff.json, report.json, dummy.obj gitignored)
    cache/                 extracted exe/pdb + hand-pulled exes (gitignored)

## The base: v0.100b build 802 (May 2013)

The oldest known PDB-bearing build, version #1 in `versions.json`. Bootstrap it:

    python3 scripts/add_version.py v0.100b-build802 --force
