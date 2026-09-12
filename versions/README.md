# Survarium versions

This directory accounts for Survarium releases by the version names players and update notes use. Each version page combines its reported game date and stage with the binary, function, source-file, and availability evidence that exists for it.

Public update names and archived binary labels are related explicitly rather than assumed identical. A build date can differ from the reported update date, and several binary version strings use an extra dot or build suffix.

## Evidence guide

- `update-note.wiki` is unmodified source text from the Survarium Wiki.
- `builds/` records executable and PDB identities for mapped binaries.
- `changes-from/` holds canonical comparisons ending at that version.
- [Dependency evidence](dependencies.md) and [build flags](build-flags.md) span versions.
- [Evidence provenance](evidence.json) records chain coverage, methods, tool identities, and limitations.
- Capture and analysis timestamps exist only in machine-readable provenance metadata.

## Coverage

Function evidence covers eight PDB-bearing builds and seven configured transitions from 0.10b through 0.21d. Source-file checksum evidence covers five of those builds; comparisons that skip unavailable builds say so at their target version. Update-note evidence contains 91 captured pages through 0.30a and one linked missing page, 0.28d. Later entries come from binary catalogs or historical build leads.

## Version index

| Version | Reported date | Stage | Update note | Binary evidence | Historical leads |
| --- | --- | --- | --- | --- | ---: |
| [0.1](0.1/README.md) | May 13, 2013 | Teamplay Closed Alpha | captured | — | — |
| [0.10b](0.10b/README.md) | May 11, 2013 | Teamplay Closed Alpha | captured | v0.10b-build802 | — |
| [0.11a](0.11a/README.md) | May 13, 2013 | Teamplay Closed Alpha | captured | v0.11a-build816 | — |
| [0.11b](0.11b/README.md) | May 15, 2013 | Teamplay Closed Alpha | captured | v0.11b-build826 | — |
| [0.11c](0.11c/README.md) | May 22, 2013 | Teamplay Closed Alpha | captured | v0.11c-build870 | — |
| [0.11d](0.11d/README.md) | May 30, 2013 | Teamplay Closed Alpha | captured | — | — |
| [0.11e](0.11e/README.md) | May 30, 2013 | Teamplay Closed Alpha | captured | v0.11e-build884 | — |
| [0.12a](0.12a/README.md) | August 14, 2013 | Teamplay Closed Alpha | captured | — | — |
| [0.12d](0.12d/README.md) | August 20, 2013 | Teamplay Closed Alpha | captured | — | — |
| [0.12e](0.12e/README.md) | August 20, 2013 | Teamplay Closed Alpha | captured | — | — |
| [0.12f](0.12f/README.md) | August 21, 2013 | Teamplay Closed Alpha | captured | — | — |
| [0.12g](0.12g/README.md) | August 22, 2013 | Teamplay Closed Alpha | captured | — | — |
| [0.13a](0.13a/README.md) | September 11, 2013 | Teamplay Closed Alpha | captured | — | — |
| [0.13b](0.13b/README.md) | September 17, 2013 | Teamplay Closed Alpha | captured | — | — |
| [0.13c](0.13c/README.md) | September 19, 2013 | Teamplay Closed Alpha | captured | — | — |
| [0.13d](0.13d/README.md) | September 18, 2013 | Teamplay Closed Alpha | captured | — | — |
| [0.14a](0.14a/README.md) | September 25, 2013 | Teamplay Closed Alpha | captured | — | — |
| [0.14b](0.14b/README.md) | September 26, 2013 | Teamplay Closed Alpha | captured | — | — |
| [0.14c](0.14c/README.md) | September 27, 2013 | Teamplay Closed Alpha | captured | — | — |
| [0.14d](0.14d/README.md) | September 28, 2013 | Teamplay Closed Alpha | captured | — | — |
| [0.14e](0.14e/README.md) | September 29, 2013 | Teamplay Closed Alpha | captured | — | — |
| [0.14f](0.14f/README.md) | October 1, 2013 | Teamplay Closed Alpha | captured | — | — |
| [0.14g](0.14g/README.md) | October 3, 2013 | Teamplay Closed Alpha | captured | — | — |
| [0.14h](0.14h/README.md) | October 9, 2013 | Teamplay Closed Alpha | captured | — | 1 |
| [0.15a](0.15a/README.md) | October 23, 2013 | Teamplay Closed Alpha | captured | — | — |
| [0.15b](0.15b/README.md) | October 25, 2013 | Teamplay Closed Alpha | captured | — | — |
| [0.15c](0.15c/README.md) | October 25, 2013 | Teamplay Closed Alpha | captured | — | — |
| [0.16a](0.16a/README.md) | November 4, 2013 | Teamplay Closed Alpha | captured | — | — |
| [0.16b](0.16b/README.md) | November 6, 2013 | Teamplay Closed Alpha | captured | — | — |
| [0.17a](0.17a/README.md) | November 25, 2013 | Teamplay Closed Alpha | captured | — | — |
| [0.18a](0.18a/README.md) | December 20, 2013 | Teamplay Closed Beta | captured | — | — |
| [0.18b](0.18b/README.md) | December 20, 2013 | Teamplay Closed Beta | captured | — | — |
| [0.18c](0.18c/README.md) | December 24, 2013 | Teamplay Closed Beta | captured | — | — |
| [0.18d](0.18d/README.md) | December 27, 2013 | Teamplay Closed Beta | captured | — | — |
| [0.18e](0.18e/README.md) | December 30, 2013 | Teamplay Closed Beta | captured | — | — |
| [0.18f](0.18f/README.md) | January 20, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.18g](0.18g/README.md) | January 23, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.19a](0.19a/README.md) | February 5, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.19b](0.19b/README.md) | February 6, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.19c](0.19c/README.md) | February 7, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.20a](0.20a/README.md) | March 17, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.20b](0.20b/README.md) | March 17, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.20c](0.20c/README.md) | March 19, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.20d](0.20d/README.md) | March 19, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.20e](0.20e/README.md) | March 21, 2014 | Teamplay Closed Beta | captured | v0.20e-build1916 | — |
| [0.20f](0.20f/README.md) | April 1, 2014 | Teamplay Closed Beta | captured | v0.20f-build1923 | — |
| [0.21a](0.21a/README.md) | April 22, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.21b](0.21b/README.md) | April 23, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.21c](0.21c/README.md) | April 24, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.21d](0.21d/README.md) | April 25, 2014 | Teamplay Closed Beta | captured | v0.21d-build2010 | — |
| [0.22a](0.22a/README.md) | May 30, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.22b](0.22b/README.md) | May 30, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.22c](0.22c/README.md) | May 30, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.22d](0.22d/README.md) | June 3, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.22e](0.22e/README.md) | June 3, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.22f](0.22f/README.md) | June 4, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.22g](0.22g/README.md) | June 6, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.23a](0.23a/README.md) | June 17, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.23b](0.23b/README.md) | June 18, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.23c](0.23c/README.md) | June 24, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.23e](0.23e/README.md) | June 30, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.23g](0.23g/README.md) | July 5, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.23h](0.23h/README.md) | July 17, 2014 | Teamplay Closed Beta | captured | v0.23h-build2285 | — |
| [0.24a](0.24a/README.md) | August 7, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.24b](0.24b/README.md) | August 9, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.24c](0.24c/README.md) | August 21, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.24d](0.24d/README.md) | August 22, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.25a](0.25a/README.md) | October 10, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.25b](0.25b/README.md) | October 17, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.25c](0.25c/README.md) | October 23, 2014 | Teamplay Closed Beta | captured | — | 1 |
| [0.25d](0.25d/README.md) | November 13, 2014 | Teamplay Closed Beta | captured | — | 1 |
| [0.26a](0.26a/README.md) | December 12, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.26b](0.26b/README.md) | December 15, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.26c](0.26c/README.md) | December 17, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.26d](0.26d/README.md) | December 23, 2014 | Teamplay Closed Beta | captured | — | — |
| [0.26e](0.26e/README.md) | December 26, 2014 | Teamplay Closed Beta | captured | v0.26e0-build2727 | 1 |
| [0.26f](0.26f/README.md) | December 30, 2014 | Teamplay Closed Beta | captured | — | 1 |
| [0.26g](0.26g/README.md) | January 16, 2015 | Teamplay Open Beta | captured | v0.26g0-build2777 | 1 |
| [0.26h](0.26h/README.md) | January 22, 2015 | Teamplay Open Beta | captured | — | — |
| [0.26i](0.26i/README.md) | January 23, 2015 | Teamplay Open Beta | captured | — | 1 |
| [0.27a](0.27a/README.md) | March 2nd, 2015 | Teamplay Open Beta | captured | — | — |
| [0.27b](0.27b/README.md) | March 6, 2015 | Teamplay Open Beta | captured | — | 1 |
| [0.27c](0.27c/README.md) | March 17, 2015 | Teamplay Open Beta | captured | — | 1 |
| [0.27d](0.27d/README.md) | April 1, 2015 | Teamplay Open Beta | captured | — | 3 |
| [0.28a](0.28a/README.md) | April 27, 2015 | Teamplay Open Beta | captured | — | 1 |
| [0.28b](0.28b/README.md) | April 29, 2015 | Teamplay Open Beta | captured | — | 1 |
| [0.28c](0.28c/README.md) | May 8, 2015 | Teamplay Open Beta | captured | — | — |
| [0.28d](0.28d/README.md) | — | — | missing | — | 1 |
| [0.29a](0.29a/README.md) | June 19, 2015 | Teamplay Open Beta | captured | — | 1 |
| [0.29b](0.29b/README.md) | June 24, 2015 | Teamplay Open Beta | captured | — | 1 |
| [0.29c](0.29c/README.md) | July 2, 2015 | Teamplay Open Beta | captured | — | 1 |
| [0.30a](0.30a/README.md) | August 7, 2015 | Teamplay Open Beta | captured | — | 2 |
| [0.30b](0.30b/README.md) | — | — | — | — | 1 |
| [0.30c](0.30c/README.md) | — | — | — | — | 1 |
| [0.30d](0.30d/README.md) | — | — | — | — | 1 |
| [0.30e](0.30e/README.md) | — | — | — | — | 1 |
| [0.31a](0.31a/README.md) | — | — | — | — | 1 |
| [0.31b](0.31b/README.md) | — | — | — | — | 1 |
| [0.31c](0.31c/README.md) | — | — | — | — | 1 |
| [0.31d](0.31d/README.md) | — | — | — | — | 1 |
| [0.31e](0.31e/README.md) | — | — | — | — | 1 |
| [0.32a](0.32a/README.md) | — | — | — | — | 1 |
| [0.33a](0.33a/README.md) | — | — | — | — | 1 |
| [0.34a](0.34a/README.md) | — | — | — | v0.34a0-build3545 | — |
| [0.44a](0.44a/README.md) | — | — | — | — | 1 |
| [0.45a](0.45a/README.md) | — | — | — | — | 1 |
| [0.46c](0.46c/README.md) | — | — | — | — | 1 |
| [0.46e](0.46e/README.md) | — | — | — | — | 1 |
| [0.47b](0.47b/README.md) | — | — | — | — | 1 |
| [0.50ac](0.50ac/README.md) | — | — | — | — | 1 |
| [0.51c](0.51c/README.md) | — | — | — | — | 1 |
| [0.54a](0.54a/README.md) | — | — | — | — | 1 |
| [0.55ab](0.55ab/README.md) | — | — | — | — | 1 |
| [0.56a](0.56a/README.md) | — | — | — | — | 1 |
| [0.60a](0.60a/README.md) | — | — | — | — | 1 |
| [0.61a](0.61a/README.md) | — | — | — | — | 1 |
| [0.62a](0.62a/README.md) | — | — | — | — | 1 |
| [0.63c](0.63c/README.md) | — | — | — | — | 1 |
| [0.64a](0.64a/README.md) | — | — | — | — | 1 |
| [0.65a](0.65a/README.md) | — | — | — | — | 1 |
| [0.66a](0.66a/README.md) | — | — | — | — | 1 |
| [0.68a](0.68a/README.md) | — | — | — | — | 2 |
| [0.69a](0.69a/README.md) | — | — | — | — | 1 |
| [0.69d](0.69d/README.md) | — | — | — | v0.69d0-2022 | — |
