# vostok-versions

Build catalogs, published update notes, and cross-version binary research for
Survarium / Vostok Engine. This repository keeps source material and historical
findings alongside the tools used to investigate builds.

## Start here

- [Build catalog](catalog/README.md): download URLs, hashes, PDB availability, and
  the configured comparison chain.
- [Wiki update notes](sources/fandom-updates/2026-09-12/README.md): 91 update pages
  captured from Survarium Wiki, with source revisions and attribution.
- [June 2026 research](reports/2026-06/README.md): preserved function comparisons,
  compiler flags, dependency findings, build metadata, and symbol alignment map.
- [Recorded observations](observations/README.md): historical interpretation kept
  separately from new scanner output.
- [Finding builds](docs/finding-builds.md) and [extracting executables](docs/extracting-exes.md):
  June 2026 research notes; availability claims describe that investigation.

The catalog contains nine installer builds (eight with PDBs, plus stripped
0.23h) and four executable-only builds through 0.69d0. Function comparisons cover
0.100b through 0.21d. The wiki collection covers the pages available through 0.30a;
its linked `0.28d` page is missing. Published update names are retained as written
and are not automatically equated to binary build IDs.

## Structure and state

| Path | Contents | State |
| --- | --- | --- |
| `catalog/` | Build identities, download hashes, chain selection, dependency marker definitions | Maintained inputs |
| `sources/` | Captured external source text, revisions, licenses, and coverage records | Dated source collections |
| `observations/` | Manually recorded findings and interpretations | Historical evidence; not regenerated |
| `reports/2026-06/` | Original reports, input metadata, symbol map, and provenance | Frozen snapshot |
| `scripts/` | Fetching, ingestion, comparison, scanning, and packaging | Runnable tools with regression tests |
| `work/` | Downloads, objects, raw comparisons, new reports | Generated and ignored |
| `flake.nix`, `flake.lock` | Pinned tool and download environment | Maintained environment |

The root `versions.json` and `reports/builds` are links retained for existing
research references. Their contents live in the catalog and June snapshot.

## What the scripts do

| Script | Inputs and action | Output |
| --- | --- | --- |
| `add_version.py` | Installer/directory or catalog build; delink EXE with PDB, optionally emit headers | `work/versions/<label>/` objects, maps, metadata |
| `diff_versions.py` | Two ingested builds; run objdiff | `work/diffs/<base>__<target>/` configuration, raw report, summaries, input fingerprints |
| `chain_report.py` | Every build in `catalog/chain.json`; compare both directions | `work/reports/CHAIN_REPORT.{json,md}` |
| `build_report.py` | Same chain; group added/deleted names by class or scope | `work/reports/builds/` |
| `flags_report.py` | PDBs for the configured chain; read compiler settings | `work/reports/BUILD_FLAGS.{json,md}` |
| `deps_report.py` | Cataloged EXEs and adjacent BugTrap DLLs; scan string/RTTI markers | `work/reports/DEPENDENCY_MARKERS.{json,md}` |
| `fetch_update_notes.py` | Wiki update categories and linked version pages | New dated collection under `sources/fandom-updates/` |
| `package_builds.sh` | Local game-tree archive; name and ZIP each build | Local upload-ready ZIPs; does not upload |
| `common.py` | Registry, hashing, tool resolution, symbol classification | Shared implementation |

Binary match scores and changed symbol names are evidence of differences, not
proof of source-level feature changes. Dependency reports distinguish observed
markers and candidate versions from declared source versions. DLL-name strings
are labeled as markers, not parsed imports. Missing markers do not prove absence.
The old reports retain their original wording; consult the snapshot's limitations.

## Fetch and compare

Enter the pinned Linux development shell:

```sh
nix develop
nix build .#version-v0_100b-build802
nix build '.#"0.26g0"'
```

The first package extracts the build's binaries from its installer. The second
fetches an executable from a cataloged game-tree archive. `nix build .#all` fetches
all cataloged executables; it can require large installer downloads for early builds.

Ingest the base and one later PDB build, then compare them:

```sh
python3 scripts/add_version.py v0.100b-build802
python3 scripts/add_version.py v0.1.1a-build816 --align-to v0.100b-build802
python3 scripts/diff_versions.py v0.100b-build802 v0.1.1a-build816
python3 scripts/diff_versions.py v0.100b-build802 v0.100b-build802
```

The final command is an identity check: every function should score 100%.
`--force` re-ingests a completed build with new inputs/options. Missing objects
are rebuilt even if metadata remains. Metadata records requested and actual
alignment, fallback status, input hashes, and the executable tool used.

For chain/build reports, first ingest **all eight** labels in `catalog/chain.json`,
aligning later builds to the base. Missing builds cause an error instead of
silently changing the comparison sequence. Cached comparisons are reused only
when object contents, metadata, tool, lockfile, scripts, and raw report hash match.

```sh
python3 scripts/chain_report.py
python3 scripts/build_report.py
python3 scripts/flags_report.py
python3 scripts/deps_report.py
```

New outputs stay under `work/`; running analysis does not replace preserved reports.
Review new results before publishing another dated snapshot, including the hashes,
coverage, effective alignment, and tools that produced them.

## Preserve another wiki snapshot

```sh
python3 scripts/fetch_update_notes.py --output sources/fandom-updates/NEW-SNAPSHOT
```

Choose a new directory; existing snapshots are never overwritten. The collector
recurses into update subcategories and follows version-number links. It stores
unmodified wikitext and records missing pages, source dates, revision IDs,
contributor-history links, checksums, and the wiki's reported license. It does not
fetch game binaries or unrelated linked articles.

The captured wiki text retains the source's reported **CC BY-NC-SA** terms; it
is not relicensed as project code. See each snapshot for attribution and scope.

## Checks

```sh
python3 -m unittest discover -s tests -v
ruff check scripts tests
bash -n scripts/package_builds.sh
```

The regression suite uses temporary inputs and simulated external tools. It covers
alignment fallback, chain selection, cache invalidation, flag aggregation, marker
reporting, packaging paths, source collection, and snapshot integrity. A full
installer download/delink cycle has not been repeated as part of this reorganization.
