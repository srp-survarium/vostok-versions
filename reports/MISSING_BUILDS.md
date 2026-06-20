# Build catalog — what we have, what's missing

Full coverage map of numbered **Vostok Engine / Survarium** builds and our holdings,
across the whole life of the engine (**0.100b**, May 2013 → **0.69d0**, the last
Steam build, 2022). Supersedes the old 0.23h-capped view.

## Status legend

| tag | meaning | drives |
|---|---|---|
| **FULL+PDB** | full build with `survarium.pdb` → delink + **function diff** + deps | `versions.json`, the diff pipeline |
| **exe** | `survarium.exe` lifted from a game-tree dump → **deps only** | `extra_builds.json` |
| **pkg** | full game tree in hand **locally**, repackaged in `survarium-uploads/`, **pending archive.org upload** | `scripts/package_builds.sh` |
| **🔒 .sup** | on archive.org **only** as the encrypted custom installer — not extractable | see `docs/extracting-exes.md` (Method C) |
| **— missing** | no known source anywhere | — |

## Bottom line

- **FULL+PDB: 8** (+ **0.23h** present but PDB-stripped) — the delink/function-diff core.
- **exe-only: 4** — 0.26e0, 0.26g0, 0.34a0, 0.69d0 (archive.org game-tree dumps).
- **packaged & pending upload: 25** — the entire **0.25 → 0.31 era** (Nov 2014 – Oct
  2015), recovered from a local `Survarium_archives.zip`. **This unlocks versions
  archive.org only has as `.sup`** (0.27d, 0.28, 0.29a, 0.30a, 0.31a …).
- **🔒 `.sup`-locked on archive.org (can't extract): ~29 items** — 0.25c0, 0.27d0,
  0.30a3, and the **entire 0.32 → 0.69 line**.
- **— never sourced anywhere:** the **0.12 → 0.19 era (~33 versions, Aug 2013 – Feb
  2014)** + 0.22 / 0.24 + most early points of 0.20 / 0.21 / 0.23.

## By era

| era | dates | status | detail |
|---|---|---|---|
| **0.1 / 0.1.1** | May 2013 | **FULL+PDB** ×5 | 0.100b/802, 0.1.1a/816, 0.1.1b/826, 0.1.1c/870, 0.1.1e/884 |
| **0.12 → 0.19** | Aug 2013 – Feb 2014 | **— missing (the hole)** | ~33 versions; never on archive.org, no dump found. See `docs/finding-builds.md` (0.14h salvage) |
| **0.20 / 0.21** | Mar – Apr 2014 | **FULL+PDB** ×3 | 0.20e/1916, 0.20f/1923, 0.21d/2010 (early points 0.20a–d, 0.21a–c missing) |
| **0.22** | May – Jun 2014 | **— missing** | no source |
| **0.23** | Jun – Jul 2014 | **FULL** (no PDB) | 0.23h/2285 (string-only); 0.23a–g missing |
| **0.24** | Jun 2014 | **— missing** | no source |
| **0.25** | Oct – Nov 2014 | **pkg** 0.25d0 · 🔒 0.25c0 | local game tree for 0.25d0; archive.org 0.25c0 is `.sup` (`Survarium.iso`) |
| **0.26** | Dec 2014 – Jan 2015 | **exe** 0.26e0/0.26g0 · **pkg** 0.26e0/f0/g0/i0 | archive.org has 0.26e0/g0 as extractable `.7z`; local zip adds 0.26f0/i0 |
| **0.27** | Mar – Apr 2015 | **pkg** 0.27b1/c0/d2/d3 · 🔒 0.27d0 | local game trees; archive.org 0.27d0 is `.sup` |
| **0.28** | Apr – Jun 2015 | **pkg** 0.28a2/b0/d0 · 🔒 0.28a2/d0 (items) | local game trees unlock the archive.org `.sup` items |
| **0.29** | Jun – Jul 2015 | **pkg** 0.29a3/b0/c0 · 🔒 0.29a3 (item) | " |
| **0.30** | Aug 2015 | **pkg** 0.30a4/b0/c0/d0/e0 · 🔒 0.30a3 (item) | " |
| **0.31** | Sep – Oct 2015 | **pkg** 0.31a2/b0/c0/d0/e2 · 🔒 0.31a2 (item) | " |
| **0.32 / 0.33** | Oct – Dec 2015 | **🔒 .sup** | archive.org 0.32a4, 0.33a5 — installer only |
| **0.34** | Dec 2015 | **exe** 0.34a0 | archive.org `survarium_full_034a0.zip` (game-tree dump) |
| **0.44 → 0.47** | 2016 – 2017 | **🔒 .sup** | 0.44a5, 0.45a6, 0.46c2, 0.46e7, 0.47b2 |
| **0.50 → 0.56** | 2017 – 2018 | **🔒 .sup** | 0.50ac, 0.51c5, 0.54a5, 0.55ab, 0.56a0 |
| **0.60 → 0.68** | 2019 – 2021 | **🔒 .sup** | 0.60a0, 0.61a2, 0.62a0, 0.63c0, 0.64a0, 0.65a0, 0.66a0, 0.68a0/a1, 0.69a0 |
| **0.69d0** | 2022 (last Steam build) | **exe** | `survarium_202206/Survarium.zip` (x64) |

## The 25 packaged builds (0.25 → 0.31), pending upload

Repackaged from `Survarium_archives.zip` into `survarium-uploads/<identifier>.zip`
(version+date names; build#/internal-id come from the Steam depot, not the exe — see
the dependency report's sweep). Versions (exe-authoritative, folder names were loose):

    0.25d0  0.26e0 0.26f0 0.26g0 0.26i0  0.27b1 0.27c0 0.27d2 0.27d3
    0.28a2 0.28b0 0.28d0  0.29a3 0.29b0 0.29c0  0.30a4 0.30b0 0.30c0 0.30d0 0.30e0
    0.31a2 0.31b0 0.31c0 0.31d0 0.31e2

Once uploaded, each gets an `exe_url` row in `extra_builds.json` (then it's a
first-class `nix build .#"<token>"` target and shows in the dependency report).

## The two persistent holes

1. **0.12 → 0.19 (the original hole):** never on archive.org under any uploader, no
   dump surfaced anywhere — ~33 versions across Aug 2013 – Feb 2014. The 0.14h
   torrent is a known dead end (partial, unrepairable). See `docs/finding-builds.md`.
2. **0.32 → 0.68 (the `.sup` wall):** archive.org *has* these, but only as the
   encrypted custom installer (`.sup`). A **game-tree dump** (like
   `Survarium_archives.zip` provided for 0.25–0.31) is the practical unlock; the
   installer route needs the Method-C work in `docs/extracting-exes.md`.

## Source & method (canonical version list)

The numbered-version list is the wiki's **Updates** category via the MediaWiki API
(rendered pages 403 the fetcher; the API does not):

    https://survarium.fandom.com/api.php?action=query&list=categorymembers&cmtitle=Category:Updates&cmlimit=500&format=json

The archive.org availability/format split is from
`archive.org/advancedsearch.php?q=creator:"Vostok Games"` (42 items), classified by
each item's primary file (`survarium_full_*.7z`/`.zip` = extractable game tree;
`survarium(-steam)?-installer-*`/`.sup`/`.iso` = sealed). Per-build versions + dates
are read from each `survarium.exe` (`Vostok Engine v…` string + the `__DATE__`
literal).
