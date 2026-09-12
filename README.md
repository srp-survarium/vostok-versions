# vostok-versions

A version-by-version record of Survarium releases and Vostok Engine binaries.
The repository connects published update notes to archived builds, function
changes, PDB source-file checksums, compiler settings, and dependency markers.

## Browse the record

- [Versions](versions/README.md) is the main index. Every known public version
  has one directory and one page, including versions for which only an update
  note or historical build lead survives.
- [Catalog](catalog/README.md) contains machine-readable build identities,
  download locations, hashes, release associations, and the comparison chain.
- [Methods](METHODS.md) explains how update notes, binaries, functions, source
  checksums, and dependency markers are collected and interpreted.

Function comparisons cover eight symbol-bearing builds from 0.10b through
0.21d. Exact source-file checksum comparisons cover five locally verified PDBs.
The update-note collection contains 91 pages through 0.30a; the linked 0.28d
page is recorded as missing. Later version pages account for binary artifacts
and historical leads even when no update note was available.

Build 802 is named `v0.10b-build802`. Its installer and wiki page use the
spellings `v0100b` and `0.100b`; the catalog records those source spellings while
the public version directory uses `0.10b`. Likewise, binary strings such as
`0.1.1a` map explicitly to public release `0.11a`.

## Repository layout

| Path | Purpose |
| --- | --- |
| `versions/` | Release pages, archived update notes, build metadata, and comparisons ending at each version |
| `catalog/` | Build and release registries, hashes, dependency definitions, and bundle metadata |
| `scripts/` | Fetch, ingestion, comparison, reporting, and packaging tools |
| `patches/` | Pinned toolchain backports used by the flake |
| `tests/` | Workflow, catalog, layout, and integrity checks |
| `.generated/` | Downloads, delinked objects, raw comparisons, and draft analysis; ignored by Git |
| `flake.nix`, `flake.lock` | Reproducible binary sources and analysis tools |

Published evidence is stored under the version it describes. A transition such
as 0.10b to 0.11a lives at
[`versions/0.11a/changes-from/0.10b/`](versions/0.11a/changes-from/0.10b/README.md).
Its narrative, complete function accounting, object summary, and available
source checksum evidence stay together.

## Fetch and compare builds

```sh
nix develop
nix build .#version-v0_10b-build802
python3 scripts/add_version.py v0.10b-build802
python3 scripts/add_version.py v0.11a-build816 --align-to v0.10b-build802
python3 scripts/diff_versions.py v0.10b-build802 v0.11a-build816
```

Five builds use compact, hash-verified GitHub release bundles by default. Add
`-archive` to one of those Nix package names to extract the original Internet
Archive installer. Other entries use their original archive.

Generated objects and comparisons land in `.generated/`; commands never replace
the committed version record. `--force` re-ingests a completed build. Metadata
records hashes, effective symbol alignment, and tool identity.

After all eight labels in `catalog/chain.json` are ingested, generate drafts with:

```sh
python3 scripts/chain_report.py
python3 scripts/build_report.py
python3 scripts/flags_report.py
python3 scripts/deps_report.py
python3 scripts/source_files_report.py
```

The chain tools require every configured intermediate build. Cached comparisons
are reused only when the objects, metadata, scripts, lockfile, tool, and raw
report match. `source_files_report.py` can fetch PDBs through the flake or accept
`--pdb LABEL=/path/to/survarium.pdb`.

## Update notes

```sh
python3 scripts/fetch_update_notes.py
```

The collector stages a new raw collection under `.generated/wiki/`. It follows
the Updates categories and linked version pages, retaining unmodified wikitext
with revision, contributor, license, and checksum metadata. Review and associate
new pages before adding them to `versions/`; the collector does not guess binary
mappings.

## Checks

```sh
python3 -m unittest discover -s tests -v
ruff check scripts tests
bash -n scripts/package_builds.sh
```

Function match scores establish binary differences but do not by themselves
prove source behavior. Dependency results distinguish observed markers from
declared versions, and DLL-name strings are not treated as parsed PE imports.
See [Methods](METHODS.md) for the evidence rules.
