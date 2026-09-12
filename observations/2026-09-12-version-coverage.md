# Version coverage and evidence assessment — 2026-09-12

The maintained catalog covers **13 builds**: eight with game EXE/PDB evidence,
one further full distribution without a game PDB, and four executable-only
entries. Preserved function comparisons cover eight builds and seven intervals;
the neighboring shader project covers the first five builds. The wiki archive
contains 91 update pages through 0.30a. These datasets overlap, but describe
different things: binary builds, public updates, and historical observations.

The initial assessment read the local catalogs, preserved reports, archived wiki
text, and neighboring shader research. Follow-up work fetched available cataloged
installers through the pinned flake and compared their PDB file checksums; it did
not rerun delinking. Counts of cataloged builds are not counts of playable installations.

## Cataloged builds

The canonical project name for build 802 is **0.10b**. Its archived metadata and
wiki page use **0.100b**; that spelling is preserved as source provenance. This is
a naming normalization of the same build, not an additional catalog entry.

Dates below are the catalog's date field, not a new determination of release
date. A matching public version name is a candidate association; it does not
prove that the archived binary is exactly the build deployed for that update.

| Catalog version | Build | Catalog date | Binary evidence | Existing comparison coverage | Candidate wiki page |
| --- | ---: | --- | --- | --- | --- |
| 0.10b | 802 | 2013-05-09 | EXE + PDB | Function baseline; shaders | 0.100b, May 11 |
| 0.1.1a | 816 | 2013-05-14 | EXE + PDB | Functions + shaders | 0.11a, May 13; spelling/date unresolved |
| 0.1.1b | 826 | 2013-05-14 | EXE + PDB | Functions + shaders | 0.11b, May 15; spelling differs |
| 0.1.1c | 870 | 2013-05-24 | EXE + PDB | Functions + shaders | 0.11c, May 22; spelling/date unresolved |
| 0.1.1e | 884 | 2013-05-28 | EXE + PDB | Functions + shaders | 0.11e, May 30; intervening 0.11d lacks a catalog build |
| 0.20e | 1916 | 2014-03-20 | EXE + PDB | Functions | 0.20e, March 21 |
| 0.20f | 1923 | 2014-04-01 | EXE + PDB | Functions | 0.20f, April 1 |
| 0.21d | 2010 | 2014-04-24 | EXE + PDB | Functions | 0.21d, April 25; 0.21a–c lack catalog builds |
| 0.23h | 2285 | 2014-07-17 | Full distribution; no game PDB | Historical dependency scan | 0.23h, July 17 |
| 0.26e0 | 2727 | 2014-12-24 | x86 EXE | Historical dependency scan | 0.26e, December 26; suffix mapping unproven |
| 0.26g0 | 2777 | 2015-01-14 | x86 EXE | Historical dependency scan | 0.26g, January 16; suffix mapping unproven |
| 0.34a0 | 3545 | 2015-12-25 | x86 EXE | Historical dependency scan | Outside this wiki collection |
| 0.69d0 | Unknown | 2022-06-01 | x64 EXE | Historical dependency scan | Outside this wiki collection |

Sources: [installer catalog](../catalog/versions.json),
[executable catalog](../catalog/extra_builds.json),
[comparison chain](../catalog/chain.json),
[wiki index](../sources/fandom-updates/2026-09-12/README.md),
[shader coverage](../../vostok-shader-evolution/README.md).

## What is physically verified here

At the start of this assessment the checkout had no `work/`, legacy `cache/`, or
`survarium-uploads/` directory. `work/` now holds checksum-analysis intermediates;
fresh comparison objects have not been generated in the maintained work area.

Two game EXE/PDB pairs were found in the local Nix store and hashed in this
assessment. All four hashes match the corresponding June metadata:

| Build | Local directory | EXE SHA-256 | PDB SHA-256 |
| --- | --- | --- | --- |
| 0.10b / 802 | `/nix/store/vjxddzw2jm0agicpwyxq3rz0i7pxank7-survarium` | `6cde21fac0fc508c140814c83d8a9d0158c0bff8f99c322cd7454c3d3103f737` | `0ffe85c27f8b95f23a65d91866af3384ab24ca343b3865a57f71a08902d5a238` |
| 0.20e / 1916 | `/nix/store/4n8ff1vlnvk0rx689kh5k6v192gp1xml-survarium-v0.20e` | `ceee6e16b01e25bc8228c4335224eb78dd470f84672c94272907c68567347a87` | `eab7c2ac31c4b8ad56cbc2381c25bc954f30df6a367b05d59cf9f350633cf186` |

The latter directory also contains launcher, service, and updater EXE/PDB files.
These are additional component-analysis opportunities within 0.20e, not additional
game versions. This was a targeted local check, not an exhaustive inventory of
every mounted disk or backup. Nix cache presence is not permanent archival storage.

A follow-up search of the home directory, Nix store, and mounted local storage
found no matching game PDBs for the six other cataloged PDB builds. SDK and local
reconstruction PDBs were hash-checked and do not match those cataloged identities.
The local `survarium_v026e0.7z` and `survarium_v026g0.7z` archives contain no PDB
files, and `017a.7z` contains no EXE/PDB files. Archive.org returned HTTP 503 and
connection failures when the flake tried to fetch the missing distributions.
After archive availability improved, the flake successfully fetched builds **816,
870, and 2010**, bringing the verified total to **five EXE/PDB pairs**. Builds
**826, 884, and 1923** still failed with archive connection errors and HTTP
502/503/504 responses on retry. The
[expanded report](../reports/2026-09-12-source-files-expanded/README.md) records
the five-build coverage and these three remaining gaps. Each included game EXE
and PDB was verified against its preserved SHA-256 identity.

## Source-file comparison at the initial two endpoints

The [September checksum report](../reports/2026-09-12-source-files/README.md)
compares all recorded source files and headers under the two available PDBs'
catalog source roots. The build-machine prefix is removed independently on each
side, Windows path case is normalized, and duplicate identical records count once.

| v0.10b / 802 → v0.20e / 1916 | Changed | Unchanged | Target-only | Base-only | Unknown |
| --- | ---: | ---: | ---: | ---: | ---: |
| Engine sources and headers | 1,444 | 1,298 | 553 | 260 | 0 |
| All recorded files under the source roots | 1,469 | 3,156 | 1,286 | 298 | 0 |

The 1,444 changed engine files comprise **639 source files and 805 headers/inlines**.
There are also 25 changed third-party files. All 4,923 baseline records and 5,911
target records carry MD5 hashes. Every changed file's path and both hashes are in
the report's complete TSV and status-specific lists.

Different recorded hashes establish a content difference at a path, not the
number or meaning of changed lines. Target-only/base-only records describe PDB
coverage rather than proving source-tree creation/deletion. The endpoints span
the missing intermediate builds; this result does not replace the seven intended
consecutive-build comparisons.

## Additional version comparisons

The [expanded report](../reports/2026-09-12-source-files-expanded/README.md) adds
intermediate builds as their distributions become available. It includes complete
file lists and both checksums for every measured interval; explicitly selected
endpoints across a missing build are not presented as a consecutive release step.

| Measured interval (build IDs) | Changed sources | Changed headers/inlines | Total changed engine files | Missing configured build within interval |
| --- | ---: | ---: | ---: | --- |
| 802 → 816 | 44 | 29 | 73 | None |
| 816 → 870 | 157 | 101 | 258 | 826 |
| 870 → 1916 | 644 | 801 | 1,445 | 884 |
| 1916 → 2010 | 295 | 243 | 538 | 1923 |

All compared records have usable MD5 checksums; unknown counts are zero. The
third-party changed-file counts for these four intervals are 0, 0, 25, and 2.
The full report also lists unchanged and PDB-only paths, including their hashes.

Build **802 → 816** (`v0.10b` → the catalog's `v0.1.1a`, commonly written `v0.11a`)
has **73 changed engine files: 44 sources and 29 headers**, with 2,927 unchanged,
two target-only, two base-only, and zero unknown records. No recorded third-party
file changed in this interval. The two target-only paths are
`vostok/game_core/character_dispersion_skill_influence.h` and its source `.cpp`;
the two base-only paths are `vostok/sound/sources/sound_rms.cpp` and
`vostok/sound/sources/sound_rms_cook.cpp`.

This gives file-content evidence supporting the earlier weapon-dispersion and
sound-system findings, while retaining the distinction between PDB coverage
changes and proven source-tree additions/deletions.

## The additional historical holdings

The [June sweep](2026-06-dependencies.md) records 25 packaged game-tree builds:

```text
0.25d0
0.26e0 0.26f0 0.26g0 0.26i0
0.27b1 0.27c0 0.27d2 0.27d3
0.28a2 0.28b0 0.28d0
0.29a3 0.29b0 0.29c0
0.30a4 0.30b0 0.30c0 0.30d0 0.30e0
0.31a2 0.31b0 0.31c0 0.31d0 0.31e2
```

Two, 0.26e0 and 0.26g0, overlap the maintained catalog. The union therefore
contains **36 documented version labels**, of which **23 have only the historical
holding/sweep record in this repository**. The union count does not establish
that all 36 binaries are currently accessible. No per-build hashes or current
locations for those 23 additional packages are recorded in the maintained catalog.
The June claim that uploads were pending is historical, not rechecked here.

## Where coverage breaks

| Interval | Evidence available | Limitation |
| --- | --- | --- |
| May 2013 | Five PDB builds, four function intervals, shader manifests, candidate patch notes | Public naming differs; 0.11d binary missing |
| 0.12–0.19 | Exactly 33 captured wiki update pages | No builds in the maintained catalog; major blind interval between May 2013 and March 2014 |
| 0.20–0.21 | Three PDB builds and public notes | Most intermediate updates have no cataloged binary |
| 0.22 | Seven captured wiki pages | No cataloged build |
| 0.23 | Six captured wiki pages; 0.23h distribution | No game PDB for 0.23h; earlier points unavailable in catalog |
| 0.24 | Four wiki pages dated August 2014 | No cataloged build; the June holdings report incorrectly places this era in June |
| 0.25–0.31 | 25 historical package labels; two maintained EXE entries | Reconcile packages and hashes; wiki text ends at 0.30a |
| 0.32–0.68 | One maintained EXE entry, 0.34a0; historical installer leads | Large binary and patch-note coverage gaps |
| 2022 | 0.69d0 x64 EXE entry | Unknown numeric build ID; no captured patch notes or cataloged game PDB |

The archive records linked page **0.28d as missing** even though a **0.28d0 binary
is described in the historical sweep**. Text gaps and binary gaps are independent.
Likewise, the June `.sup` installer findings describe extraction constraints at
that time, not proof that no later game-tree copy exists anywhere.

## What the evidence says about change

The preserved function counts below were produced by the old workflow. Its
alignment and compiler-flag limitations remain applicable; these are useful
leads, not newly validated source-level change counts.

| Comparison | Preserved counts: added / deleted / changed / identical | Interpretation supported by the available material |
| --- | --- | --- |
| 802 → 816 | 88 / 56 / 400 / 11,060 | Weapon-state and dispersion changes are thematically consistent with wiki 0.11a's recoil/accuracy notes; exact build association unresolved |
| 816 → 826 | 19 / 26 / 254 / 11,268 | Shader report finds 23 names with changed code; wiki 0.11b describes graphics changes, but does not prove the cause of each bytecode delta |
| 826 → 870 | 142 / 160 / 1,465 / 9,916 | Strong candidate correlation: sound-system changes and new shader variants alongside wiki 0.11c's HDR audio, sound fixes, and HDAO |
| 870 → 884 | 25 / 38 / 473 / 11,012 | Aggregate interval spanning missing 0.11d; cannot attribute all differences to 0.11e's installer hotfix |
| 884 → 1916 | 4,163 / 6,812 / 4,526 / 172 | Broad engine restructuring across roughly ten months; cannot assign these changes to one update or infer their development purpose from counts |
| 1916 → 1923 | 1 / 3 / 11 / 8,847 | Small measured client-code change; wiki 0.20f describes synchronization fixes, a useful focused investigation |
| 1923 → 2010 | 605 / 383 / 2,566 / 5,910 | Networking/statistics and other changes across 0.21a–d; 0.21d's short patch notes describe only the endpoint update |

Sources: [function report](../reports/2026-06/CHAIN_REPORT.md),
[historical interpretation](../reports/2026-06/CHANGES_NARRATIVE.md),
[shader evolution](../../vostok-shader-evolution/EVOLUTION.md), and archived
[0.11a](../sources/fandom-updates/2026-09-12/pages/0.11a.wiki),
[0.11c](../sources/fandom-updates/2026-09-12/pages/0.11c.wiki),
[0.11e](../sources/fandom-updates/2026-09-12/pages/0.11e.wiki),
[0.20f](../sources/fandom-updates/2026-09-12/pages/0.20f.wiki),
[0.21d](../sources/fandom-updates/2026-09-12/pages/0.21d.wiki).

The old narrative's claim that the 2013–2014 interval captures a transition from
an AI shooter to PvP is too strong. May 2013 wiki notes already describe team
spawn rules, match starts, and player combat. AI symbols disappearing can reflect
removal of unused or inherited code; their presence does not establish a playable
single-player mode. The defensible finding is substantial engine restructuring
between two already multiplayer-era endpoints.

The shader evidence is particularly useful for May 2013: the reports record a
define-registry width change from 82 to 81 to 68, and identical distinct-bytecode
hash sets for 224 of the initial 261 shader names at build 884. This supports
selective reuse of shader reconstruction, while requiring version-specific
permutation interpretation. It does not imply equivalent whole-game behavior.

Later observations provide candidate transition boundaries: Bullet SoftBody
markers disappear by 0.26g0; Steam markers appear by 0.27d2; STL namespace markers
switch between 0.27d3 and 0.28a2. These historical scanner conclusions need fresh
per-file evidence before being promoted into verified dependency or linkage facts.

## Most useful next work

1. Reconcile the 25 historical packages with actual files. Record each EXE hash,
   package hash/location, embedded version/date, architecture, and game-PDB
   presence. This could promote 23 additional labels into the maintained catalog.
2. Add an explicit public-update/build mapping with evidence and confidence.
   Preserve separate date fields and one-to-many mappings: e.g. 0.27d2 and
   0.27d3 are not interchangeable merely because both resemble wiki 0.27d.
3. Revalidate the small 0.20e → 0.20f interval with the corrected workflow, then
   inspect the changed networking functions against the archived synchronization
   notes. This gives a bounded check of both the method and a historical claim.
4. Extend shader/resource analysis to 0.20e, whose local EXE/PDB pair is already
   verified. Asset changes can explain patch notes that leave little client-code
   evidence; server-only and launcher changes require their own artifacts.
5. Target the 0.12–0.19 binary gap and post-0.30a patch-note gap separately.
   A release note cannot replace a missing binary, and a client binary cannot
   fully establish server behavior or published release timing.
