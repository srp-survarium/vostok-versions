# Source-file checksum comparisons

Generated 2026-09-12T11:01:29. Explicit subset of the configured chain: 5 PDBs, 4 comparison(s).

Five game EXE/PDB pairs were verified against the preserved SHA-256 identities. Builds 816, 870, and 2010 were fetched successfully through the flake in this resumed run. Builds 826, 884, and 1923 remain unavailable after repeated Archive.org 502/503/504 and connection failures. Comparisons across those omitted builds span multiple configured steps; their changes cannot be assigned to a single intermediate release.

Every checksum record under the catalog's source root is included, including headers. Paths are normalized across the 2013/2014 build-machine root change. Engine means `vostok/`; remaining paths are grouped as third-party. Files absent from debug records are outside this analysis.

**Changed** means different hashes of the same algorithm at the same path. **Unchanged** means equal recorded hashes. **Added/removed** mean present only in the target/base PDB coverage. **Unknown** means no comparable checksum. These counts measure recorded source contents, independently of function/object changes. They cannot identify changed lines, establish behavior, or exclude comments/line-ending changes.

## Engine files (sources and headers)

| Comparison | Changed | Unchanged | Added | Removed | Unknown |
| --- | ---: | ---: | ---: | ---: | ---: |
| [v0.10b-build802 → v0.1.1a-build816](pairs/v0.10b-build802__v0.1.1a-build816/README.md) | 73 | 2927 | 2 | 2 | 0 |
| [v0.1.1a-build816 → v0.1.1c-build870](pairs/v0.1.1a-build816__v0.1.1c-build870/README.md) | 258 | 2723 | 7 | 21 | 0 |
| [v0.1.1c-build870 → v0.20e-build1916](pairs/v0.1.1c-build870__v0.20e-build1916/README.md) | 1445 | 1306 | 544 | 237 | 0 |
| [v0.20e-build1916 → v0.21d-build2010](pairs/v0.20e-build1916__v0.21d-build2010/README.md) | 538 | 2739 | 68 | 18 | 0 |

## Source-file versus header changes

| Comparison | Changed source files | Changed headers/inlines | Changed other engine files | Changed third-party files |
| --- | ---: | ---: | ---: | ---: |
| v0.10b-build802 → v0.1.1a-build816 | 44 | 29 | 0 | 0 |
| v0.1.1a-build816 → v0.1.1c-build870 | 157 | 101 | 0 | 0 |
| v0.1.1c-build870 → v0.20e-build1916 | 644 | 801 | 0 | 25 |
| v0.20e-build1916 → v0.21d-build2010 | 295 | 243 | 0 | 2 |

## Per-build checksum coverage

| Build | All files | Engine files | Checksum kinds | Matches historical PDB SHA-256 |
| --- | ---: | ---: | --- | --- |
| [v0.10b-build802](builds/v0.10b-build802.tsv) | 4923 | 3002 | md5 | yes |
| [v0.1.1a-build816](builds/v0.1.1a-build816.tsv) | 4923 | 3002 | md5 | yes |
| [v0.1.1c-build870](builds/v0.1.1c-build870.tsv) | 4909 | 2988 | md5 | yes |
| [v0.20e-build1916](builds/v0.20e-build1916.tsv) | 5911 | 3295 | md5 | yes |
| [v0.21d-build2010](builds/v0.21d-build2010.tsv) | 6019 | 3345 | md5 | yes |

## Configured builds not analyzed in this run

- `v0.1.1b-build826`
- `v0.1.1e-build884`
- `v0.20f-build1923`

The comparison above spans the explicitly selected endpoints. It does not replace the missing consecutive-build comparisons or localize changes to an intermediate release.

Each comparison directory includes complete `changed.txt`, `unchanged.txt`, `added.txt`, `removed.txt`, and `unknown.txt` lists. `files.tsv` records every path, status, scope, file kind, and both hashes. [manifest.json](manifest.json) records PDB SHA-256 identities, table hashes, selected coverage, tool and script identities, and all comparison counts.
