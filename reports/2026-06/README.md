# June 2026 research snapshot

Original cross-version findings preserved from commit
`4621fd37` (the full source commit is recorded in [manifest.json](manifest.json)).
The manifest maps original paths to snapshot files and records SHA-256 hashes.
All listed file contents are unchanged. Generated objdiff configurations can be
recovered from that source commit; they are not needed to read these results.

| Material | Contents |
| --- | --- |
| [CHAIN_REPORT.md](CHAIN_REPORT.md), [CHAIN_REPORT.json](CHAIN_REPORT.json) | Consecutive-build function changes, eight builds / seven steps |
| [builds/](builds/) | Added/deleted symbol names grouped by owning scope |
| [diffs/](diffs/) | Fourteen directional pair summaries |
| [BUILD_FLAGS.md](BUILD_FLAGS.md) | Historical compiler-setting report |
| [DEPENDENCY_VERSIONS.md](DEPENDENCY_VERSIONS.md) | Dependency observations and the manually recorded 25-build sweep |
| [CHANGES_NARRATIVE.md](CHANGES_NARRATIVE.md) | Interpretation of engine changes |
| [MISSING_BUILDS.md](MISSING_BUILDS.md) | Holdings and availability as recorded then |
| [versions/](versions/) | EXE/PDB hashes and metadata, plus the base folded-symbol map |
| [provenance/](provenance/) | Original catalogs, chain configuration, and lockfile |

## Interpretation limits

These are historical results, not a newly validated analysis. The original scripts
could record a requested symbol alignment even when delinking fell back to an
unaligned run. Their metadata therefore does not prove effective alignment.
Compiler-flag aggregation could describe a flag observed in some builds as present
in every build. The dependency scanner used string markers, including DLL names;
it did not parse imports, and missing markers did not establish library absence.
Some dependency narrative and the 25-build sweep were hardcoded observations.

Symbol names may change through folding, renaming, or layout changes. Added/deleted
names are not by themselves proof that a gameplay feature appeared or disappeared.
Availability and local-holdings claims describe the June investigation.

The old tool revisions are pinned in `provenance/flake.lock`, but per-run tool
identities and raw objdiff reports were not recorded here. Use the original source
commit to inspect the old workflow. The maintained workflow now keeps generated
outputs in `work/` and records effective alignment and comparison fingerprints.
