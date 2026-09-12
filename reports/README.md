# Report scope and reproduction

These reports preserve the June 2026 cross-version investigations. They can be
read without downloading the game or rebuilding the analysis tools. Dates and
availability claims in `MISSING_BUILDS.md`, `../docs/finding-builds.md`, and
`../docs/extracting-exes.md` describe what was known during those investigations;
they are not a live inventory of archive.org or the current local workspace.

## Preserved evidence

| Files | Role |
| --- | --- |
| `../versions.json`, `../extra_builds.json` | Build identities, archive URLs, and pinned download hashes. |
| `../versions/*/meta.json` | Hashes and sizes of the analyzed executables/PDBs, source roots, and alignment choices. |
| `../versions/v0.100b-build802/symbol-map.tsv` | Base folded-symbol naming map used for alignment. |
| `../diffs/*/summary.{md,json}`, `CHAIN_REPORT.{md,json}`, `builds/*.md` | Saved comparison results; the larger reports preserve function lists beyond the per-pair summaries. |
| `CHANGES_NARRATIVE.md`, `BUILD_FLAGS.md`, `DEPENDENCY_VERSIONS.md` | Interpretation, compiler evidence, and dependency observations. |
| `MISSING_BUILDS.md`, `../docs/` | Historical build-discovery and extraction research. |

Function reports compare eight PDB-bearing builds from 0.100b through 0.21d.
The dependency registry also includes stripped 0.23h and four executable-only
builds through 0.69d0. `DEPENDENCY_VERSIONS.md` additionally contains a manually
recorded 25-build sweep and DLL observations; those inputs are not all registered
for automatic download.

Comparison scores describe the pinned tool's output. Changed bytes or a changed
symbol name do not by themselves prove a source-level feature change: compiler
optimization, folding, renaming, and type-layout changes can affect the result.
Dependency markers distinguish observed presence from a missing marker; lack of
a marker does not by itself prove a library was absent. Treat broader narrative
conclusions as interpretations of the recorded evidence.

## Regenerating a comparison

Use the checked-in `flake.lock` to recover the pinned analysis tools. Record any
tool updates when publishing new results: historical metadata records input
hashes, but not a separate tool revision for each report.

From the repository root:

```sh
nix develop
python3 scripts/add_version.py v0.100b-build802 --force
python3 scripts/add_version.py v0.1.1a-build816 --force --align-to v0.100b-build802
python3 scripts/diff_versions.py v0.100b-build802 v0.1.1a-build816
python3 scripts/diff_versions.py v0.1.1a-build816 v0.100b-build802
```

`--force` is needed on a fresh clone because the tracked `meta.json` otherwise
causes ingestion to be skipped, even though the ignored objects are absent.
Ingestion rewrites metadata and may regenerate the symbol map. Review those
changes along with new comparison output.

The diff command creates the ignored `objdiff.json`, `dummy.obj`, and raw
`report.json` for each pair. Open the generated `objdiff.json` in objdiff for
interactive inspection. Only the distilled pair summaries are tracked.

For an identity check, compare a rebuilt version against itself:

```sh
python3 scripts/diff_versions.py v0.100b-build802 v0.100b-build802
```

Every function should report 100%. Before regenerating the complete chain, ingest
all eight labels in `config.json`, aligning each later build to the base. Then run:

```sh
python3 scripts/chain_report.py
python3 scripts/build_report.py
python3 scripts/flags_report.py
python3 scripts/deps_report.py
```

Chain and build reports use the versions with local objects present and reuse
existing raw pair reports. Rerun each pair with `diff_versions.py` after changing
tools or inputs. Generating reports with only part of the chain ingested produces
partial coverage. The report scripts overwrite their outputs; preserve manually
written observations separately before rerunning `deps_report.py`.
