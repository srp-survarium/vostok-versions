# Methods and evidence rules

The repository treats a public release name, archived installer label, and
binary build as separate facts. Explicit catalog fields join them. Similar
spellings or nearby dates alone do not establish identity.

## Public versions and update notes

`catalog/releases.json` defines the public version directories. Captured update
notes are unmodified MediaWiki wikitext from fixed revisions. The wiki manifest
records page and revision URLs, contributor-history links, source timestamps,
hashes, and the source site's reported license.

The collection follows `Category:Updates`, its subcategories, and version links
from captured pages and navigation material. It contains 91 update pages through
0.30a and one linked missing page, 0.28d. Support pages and category membership
live in `versions/wiki/` so coverage remains auditable.

## Build identity

Catalog labels combine a normalized version token with an internal build number
when known. Original archive names and binary strings remain separate fields. A
public release association is marked as a candidate when based on spelling and
date proximity rather than an authoritative manifest.

Verified build metadata records the source URL and root, EXE/PDB sizes and
SHA-256 hashes, object count, and ingestion provenance. Five exact EXE/PDB pairs
are also compressed release assets whose outer and contained hashes are recorded
in `catalog/binary-release.json`.

## Function comparison

`vostok-delinker` uses the PDB to split `survarium.exe` into COFF objects by
source unit and function. Folded symbols can share machine code, so later builds
are aligned to the base symbol map where possible. `objdiff-cli` compares the
corresponding objects in both directions.

Each transition directory contains complete function accounting, an object
summary, added and deleted hand-written functions grouped by scope, and a
narrative grounded in those symbols. Compiler-generated thunks, deleting
destructors, RTTI records, static initializers, and third-party namespace
instantiations are excluded from source-oriented grouping. Complete object data
remains available for audit.

The May 2013 transition narratives also cite the separately maintained
[shader evolution record](https://github.com/srp-survarium/vostok-shader-evolution/tree/3c95be0e19d8e809b223d419d074c94d22b97f0f).
Those shader counts are corroboration and remain traceable to that fixed commit.

A match below 100 percent proves differing machine code for that object. It does
not identify an exact source edit or behavior. The 884 to 1916 interval has
extreme alignment churn, so its explanation relies on coherent symbol families
and corroborating evidence rather than reading each alignment result literally.

## Source-file checksums

The patched PDB tool exports every file checksum record below the build's source
root, including headers. Paths are lowercased, slash-normalized, and stripped of
the build-machine root. Equal algorithms and hashes are unchanged; different
hashes are changed; one-sided paths are added or removed from PDB coverage;
absent or incompatible hashes are unknown.

These records detect source-file byte changes but provide no source contents or
changed lines. A one-sided record can reflect build coverage as well as a real
file addition or deletion. Comparisons that skip an unavailable configured build
state their endpoints and cannot localize changes to the skipped release.

## Compiler flags and dependency markers

Compiler reports read per-module command lines and LTCG records from PDBs. LTCG
can hide per-translation-unit optimization flags, so an absent flag is not an
optimization setting.

Dependency scans use version banners, RTTI names, and library-specific strings
from executables and selected adjacent DLLs. A DLL filename string is a marker,
not proof of a PE import. Declared versions are shown separately when the binary
proves library presence but contains no version banner. Missing markers do not
prove absence.

## Obtaining binaries

The Nix flake pins archived inputs. Early Inno Setup installers and later
game-tree archives can be extracted directly. Internet Archive member URLs can
stream only `survarium.exe` from large `.zip` and `.7z` trees; the extra-build
catalog pins those bytes.

Most later official installers contain an encrypted `!sup` payload rather than
an installed game tree. Standard archive tools do not expose the game executable
from it. The catalog distinguishes verified artifacts from these sealed leads.

The incomplete 0.14h artifact remains a lead. Its recovered executable prefix is
5,488,640 bytes with SHA-256
`b6edffcd5357889de360704e2b3b06ff1c20a8ca84b025095b2d344e4b5ab7e5`;
the PE timestamp is `0x52556A76` and expected version string is `0.14h`. Those
values can authenticate a future candidate, but the missing PDB prevents
function analysis.

## Generated and canonical data

Scripts write downloads, objects, raw comparisons, and drafts under
`.generated/`. A result becomes canonical after its coverage, hashes, tool
identity, and counts are checked and it is placed with the version it describes.
`versions/manifest.json` hashes the complete public evidence tree. Capture and
analysis timestamps appear only in provenance metadata.
