# Pulling just `survarium.exe` out of an archive.org build

These post-0.23 builds are **large** (1.4–13 GB) but the dependency scan only needs
`survarium.exe` (10–14 MB). This is how to get *only the exe* — preferably via Nix
so the result is pinned and reproducible.

**The one distinction that matters: a *game-tree dump* vs a *`.sup` installer`.***
A build is only extractable if someone packaged the **already-installed game tree**
(you'll see `…/binaries/{x86,x64}/survarium.exe` *inside* the archive). The
original **installers never contain the game exe** — every `survarium-installer-*`
(whether Inno `.exe`+`.bin`, an `.iso` with `setup.exe`+`setup-N.bin`, or a `.zip`
of those) is a thin bootstrapper whose multi-GB payload is a single encrypted
`installer.sup`; the updater unpacks it at install time. So:

| what you have | extractable? | method |
|---|---|---|
| **game-tree `.7z`/`.zip`** (`survarium_full_*.7z`, `Survarium.zip`) — has `…/binaries/…/survarium.exe` | **yes** | A — `view_archive.php` (remote) or `7z e` (local) |
| **`.sup` installer** (Inno `.exe`+`.bin`, `.iso` `setup.*`, `.zip` of an installer, `*.sup`) | **no** | C — sealed (run the updater under Wine, or re-source a game-tree dump) |

archive.org items expose their files at
`https://archive.org/download/<identifier>/<filename>`.

---

## Method A — `.7z`/`.zip`: extract one member, no full download

archive.org runs a server-side archive exploder: appending the **member path**
to the archive URL streams just that file (302 → `view_archive.php`). It works
for `.zip` *and* `.7z`, so a 13 GB zip costs a ~13 MB download.

**1. Find the member path** (list the archive's contents):

```sh
curl -sL 'https://archive.org/download/survarium_202206/Survarium.zip/' \
  | grep -ioE 'Survarium/[A-Za-z0-9_./-]*survarium\.exe'
# -> Survarium/game/binaries/x64/survarium.exe          (note: x64!)

curl -sL 'https://archive.org/download/vostok_engine_v0.26g0_build_2777_internal_id_1104_jan_14_2015/survarium_full_026g0.7z/' \
  | grep -ioE 'Survarium/[A-Za-z0-9_./-]*' | grep -i 'binaries'
# -> Survarium/game/binaries/x86/survarium.exe
```

**2a. Plain download** (curl follows the redirect):

```sh
curl -L -o survarium.exe \
 'https://archive.org/download/survarium_202206/Survarium.zip/Survarium/game/binaries/x64/survarium.exe'
```

**2b. Nix (pinned & reproducible)** — `fetchurl` follows the redirect and the
exe bytes are deterministic, so the member URL hashes cleanly:

```nix
# nix-build -E '...'  (or add to the flake)
let pkgs = import <nixpkgs> {}; in {
  exe-026g0 = pkgs.fetchurl {
    name = "survarium-026g0.exe";
    url  = "https://archive.org/download/vostok_engine_v0.26g0_build_2777_internal_id_1104_jan_14_2015/survarium_full_026g0.7z/Survarium/game/binaries/x86/survarium.exe";
    hash = "sha256-rDPZk3AVwimb9izGsSfLMItIo0dbMP/y3dZUea478VM=";
  };
  exe-069d0 = pkgs.fetchurl {
    name = "survarium-069d0.exe";
    url  = "https://archive.org/download/survarium_202206/Survarium.zip/Survarium/game/binaries/x64/survarium.exe";
    hash = "sha256-HhrgTcmB/E9XNMVlWfsPLg50x4e8xT67/cIz9EDWVEg=";
  };
}
```

Get a hash for a new member first with
`nix store prefetch-file --name survarium.exe '<member-url>'` (prints the SRI
hash), or `nix hash file survarium.exe` after a curl download.

### Local game-tree dumps (no download)

A `survarium_full_*.7z` (or the 2022 `Survarium.zip`) already on disk is the same
thing — pull one member with `7z`:

```sh
nix shell nixpkgs#p7zip -c 7z e -y -o026e0 survarium_v026e0.7z \
  "Survarium/game/binaries/x86/survarium.exe"
```

`7z l <archive> | grep -i survarium.exe` first to confirm it's a game-tree dump
(present) rather than a `.sup` installer (absent — see below).

---

## Method C — the `.sup` installer: sealed

Every *installer* (as opposed to a game-tree dump) hides the game behind a single
encrypted `installer.sup`, regardless of the outer wrapper:

- **Inno** `survarium-(steam-)installer-*.exe` + `*-N.bin` (e.g. 0.30a3, 0.52ab) —
  Inno Setup 5.5, but `innoextract --list` shows the only payload is
  `{tmp}/survarium/installer.sup` + `survarium_updater.exe`. No `survarium.exe`.
- **`.iso`** with `setup.exe` + `setup-N.bin` (e.g. 0.25d0) — same: `setup.exe`'s
  Inno manifest holds `tmp/survarium/installer.sup`.
- **`.zip`** of any of the above (e.g. 0.28a2/0.28d0/0.31a2/0.46c2) — just the
  archive.org item zipped; still the installer, still `.sup` inside.
- **bare `*.sup`** (e.g. 0.63c0, 0.28a0) — the payload on its own.

The `.sup` is **Vostok's own format** (the 0.63c0 stub names
`d:\survarium.public\binaries\x64\survarium_installer.pdb`, Spawnpoint Limited).
It starts with magic `21 73 75 70` = **`!sup`**, a 16-byte header, then payload
that is **uniform high-entropy** (a 1 MB sample histograms flat at ~3906/byte) with
no zlib block structure and zero plaintext paths across multi-GB — i.e. encrypted,
and the updater (`survarium_updater.exe`, a libtorrent downloader that
`CryptVerifySignature`s the package) is the only thing that reads it. `innoextract`,
`7z`, `view_archive.php` all reject it.

**No standalone extraction**, and the Wine route was tried and does **not** work
out of the box — three independent blockers (from the 0.46c2 attempt, Wine 10.0):

1. **The Inno installer aborts in `InitializeSetup`.** Its `[Code]` does a WMI
   `Win32_DiskDrive.MediaType` check expecting `'Fixed hard disk media'`; Wine
   returns `'Fixed hard disk'`, and setup dies with `Runtime Error (at 120:1310)`
   before it ever runs the updater.
2. **The updater can't be driven standalone.** `survarium_updater.exe` is a child
   process that talks to the installer GUI over IPC (`send_error_message`,
   `send_cannot_move_file_message`, `install_progress(progress_data&)`, …) — run
   directly it just exits (verbs seen: `extract`/`install`/`patch`/`update` +
   `save_path`, but it reports nothing and writes no file without its parent).
3. **It requires NTFS + transactional moves.** `survarium_updater::check_is_ntfs`
   gates install, and it uses `move_transacted` / `install_to_extraction` (TxF),
   which Wine doesn't faithfully implement.

So unlocking the `.sup` era needs real work: patch/skip the installer's WMI check
(rebuild or hook Wine's `wbemprox`), give Wine an NTFS-backed drive, and hope its
TxF fallback holds — or reverse the updater's IPC protocol to feed it directly.
**Cheaper:** re-source a **game-tree dump** (`survarium_full_*.7z` / a `.zip`) of
that version (Method A) instead of the installer.

---

## Per-build cheat-sheet

`✓` = game-tree dump, exe lifted out. `✗` = `.sup` installer, sealed.

| build | source seen | exe? | internal exe path | arch |
|---|---|:-:|---|---|
| 0.26e0 / 2727 | local `survarium_v026e0.7z` | ✓ | `Survarium/game/binaries/x86/survarium.exe` | x86 |
| 0.26g0 / 2777 | `…/survarium_full_026g0.7z` (archive.org **or** local) | ✓ | `Survarium/game/binaries/x86/survarium.exe` | x86 |
| 0.34a0 / 3545 | `…034a0…/survarium_full_034a0.zip` (archive.org) | ✓ | `Survarium/game/binaries/x86/survarium.exe` | x86 |
| 0.69d0 / 2022 | `survarium_202206/Survarium.zip` | ✓ | `Survarium/game/binaries/x64/survarium.exe` | x64 |
| 0.25d0 | local `.iso` (`setup.exe`→`installer.sup`) | ✗ | — sealed | — |
| 0.28a2 / 0.28d0 / 0.31a2 | local `.zip` (steam-installer + `.sup`) | ✗ | — sealed | — |
| 0.30a3 / 0.44a5 / 0.50ac | archive.org Inno installer + `.bin`→`.sup` | ✗ | — sealed | — |
| 0.46c2 / 0.52ab / 0.63c0 | local/archive.org installer → `.sup` | ✗ | — sealed | — |

Extracted exes (and any mined component DLLs) are kept under
`cache/extra/<label>/` (gitignored); `scripts/deps_report.py` reads them via
`extra_builds.json`. **None of the extractable post-0.23 builds ship a `.pdb`** —
the dev-build PDBs stop at 0.23h; 0.26+ are retail (exe + DLLs only).

---

## All 42 `creator:"Vostok Games"` items on archive.org, by extractability

From `archive.org/advancedsearch.php?q=creator:"Vostok Games"`, classified by each
item's largest data file. **Only a `survarium_full_*` dump (or the 2013 InnoSetup
exes / the 2022 `Survarium.zip`) is extractable** — everything that ships an
`-installer-*` / `setup-*` / `*.sup` / `.iso` is the sealed `!sup` (Method C).

**Extractable game-tree dumps / direct installers (10 versions):**

| version | item file | note |
|---|---|---|
| 0.1 (802/816/826/870/884) | `survarium_(alpha_)setup_*.exe` | 2013 InnoSetup, exe **+ pdb** (the registry builds) |
| 0.20e / 0.20f / 0.21d | `survarium_full_02xx.7z` | exe + pdb (registry) |
| 0.23h | `survarium_full_023h.7z` | exe only (no pdb) |
| 0.26e0 / 0.26g0 | `survarium_full_026x0.7z` | exe only — **in report** |
| **0.34a0** | `survarium_full_034a0.zip` | exe only — **in report** (the one new find) |
| 0.69d0 (2022) | `survarium_202206/Survarium.zip` | x64, exe + DLLs — **in report** |

**Sealed `!sup` installers (the rest — not extractable):** 0.25c0 (`Survarium.iso`
→`setup.exe`→`.sup`), 0.27d0, 0.28a2, 0.28d0, 0.29a3, 0.30a3, 0.31a2, 0.32a4,
0.33a5, 0.44a5, 0.45a6, 0.46c2, 0.46e7, 0.47b2, 0.50ac, 0.51c5, 0.54a5, 0.55ab,
0.56a0, 0.60a0, 0.61a2, 0.62a0, 0.63c0, 0.64a0, 0.65a0, 0.66a0, 0.68a0, 0.68a1,
0.69a0 — `survarium(-steam)?-installer-*` with `.bin`/`.sup`.

So past 0.23h the readable set is exactly **0.26e0, 0.26g0, 0.34a0, 0.69d0**; the
whole 0.4x–0.6x line is `.sup`-only on archive.org and would need the Method-C
unlock (or a game-tree dump surfacing elsewhere).
