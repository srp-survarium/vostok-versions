# Source-file checksum comparisons

Generated 2026-09-12T10:31:34. Explicit subset of the configured chain: 2 PDBs, 1 comparison(s).

BLOCKED for the other six configured builds: Archive.org returned connection failures and HTTP 503 on 2026-09-12. Searches of the project, home directory, Nix store, and mounted local archives found no matching game PDBs for those six builds. Local 0.26e0/0.26g0 archives contain no PDB files; 017a.7z contains no EXE/PDB files. SDK/reconstruction PDBs do not match the eight preserved game-PDB identities. Resume the full chain when the cataloged distributions are accessible.

Every checksum record under the catalog's source root is included, including headers. Paths are normalized across the 2013/2014 build-machine root change. Engine means `vostok/`; remaining paths are grouped as third-party. Files absent from debug records are outside this analysis.

**Changed** means different hashes of the same algorithm at the same path. **Unchanged** means equal recorded hashes. **Added/removed** mean present only in the target/base PDB coverage. **Unknown** means no comparable checksum. These counts measure recorded source contents, independently of function/object changes. They cannot identify changed lines, establish behavior, or exclude comments/line-ending changes.

## Engine files (sources and headers)

| Comparison | Changed | Unchanged | Added | Removed | Unknown |
| --- | ---: | ---: | ---: | ---: | ---: |
| [v0.10b-build802 → v0.20e-build1916](pairs/v0.10b-build802__v0.20e-build1916/README.md) | 1444 | 1298 | 553 | 260 | 0 |

## Source-file versus header changes

| Comparison | Changed source files | Changed headers/inlines | Changed other engine files | Changed third-party files |
| --- | ---: | ---: | ---: | ---: |
| v0.10b-build802 → v0.20e-build1916 | 639 | 805 | 0 | 25 |

## Per-build checksum coverage

| Build | All files | Engine files | Checksum kinds | Matches historical PDB SHA-256 |
| --- | ---: | ---: | --- | --- |
| [v0.10b-build802](builds/v0.10b-build802.tsv) | 4923 | 3002 | md5 | yes |
| [v0.20e-build1916](builds/v0.20e-build1916.tsv) | 5911 | 3295 | md5 | yes |

## Configured builds not analyzed in this run

- `v0.1.1a-build816`
- `v0.1.1b-build826`
- `v0.1.1c-build870`
- `v0.1.1e-build884`
- `v0.20f-build1923`
- `v0.21d-build2010`

The comparison above spans the explicitly selected endpoints. It does not replace the missing consecutive-build comparisons or localize changes to an intermediate release.

Each comparison directory includes complete `changed.txt`, `unchanged.txt`, `added.txt`, `removed.txt`, and `unknown.txt` lists. `files.tsv` records every path, status, scope, file kind, and both hashes. [manifest.json](manifest.json) records PDB SHA-256 identities, table hashes, selected coverage, tool and script identities, and all comparison counts.
