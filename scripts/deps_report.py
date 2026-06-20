#!/usr/bin/env python3
"""
deps_report.py - third-party dependency versions across the build chain.

    python3 scripts/deps_report.py

Unlike the function-level diff (which needs a PDB), this works on the raw
`survarium.exe` of every registry build - including the symbol-less **0.23h**,
because the markers it reads live in `.rdata` (literal version strings + the
RTTI `.?AV...@@` type-descriptor names the compiler bakes into the image for
dynamic_cast/typeid), not in the PDB.

Two kinds of marker:

  * **version strings** baked by the library itself - zlib's
    "inflate 1.2.3 Copyright ...", OpenSSL's "OpenSSL 1.0.0g 18 Jan 2012",
    Scaleform GFx's bare "4.2.21", libpng's "1.5.13". These give an exact,
    binary-confirmed version that can *change* across builds (a real version
    bump, e.g. Scaleform 4.2.21 -> 4.2.22).
  * **presence markers** - mangled RTTI namespace tokens (`@boost@@`,
    `@stlp_std@@`, `@Wm4@@`, `@Opcode@@`, `btCollisionWorld`, `@Scaleform@@`,
    `OggVorbis_File`). These prove the library is *linked* even when it prints
    no version of its own; the version then comes from the engine's
    `sources/versions.txt` manifest.

The reference manifest (`vostok/sources/versions.txt`) lists declared dep
versions but is incomplete (no scaleform/bullet/lua) and is a single source
snapshot - the *binaries* are the ground truth, which is the whole point.

Writes reports/DEPENDENCY_VERSIONS.md. Needs only `nix` (to fetch each build
from the flake) and `strings`.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as c  # noqa: E402

REPORTS_DIR = c.REPO_DIR / "reports"
# Builds we could not put through the flake/registry: post-0.23 exes lifted out
# of an archive.org installer by hand (no PDB; see docs/extracting-exes.md). Each
# entry points at a raw survarium.exe under cache/extra/ (gitignored).
EXTRA_PATH = c.REPO_DIR / "extra_builds.json"


def extra_registry() -> list[dict]:
    return json.loads(EXTRA_PATH.read_text()) if EXTRA_PATH.exists() else []


def fetch_exe_via_flake(token: str) -> Path:
    """`nix build .#"<token>"` -> the store dir holding `<token>.exe`. Lets the
    report regenerate the exe-tier builds straight from `extra_builds.json`'s
    `exe_url`, with no dependency on the (gitignored) cache."""
    out = subprocess.run(
        ["nix", "build", f'.#"{token}"', "--no-link", "--print-out-paths"],
        cwd=c.REPO_DIR, stdout=subprocess.PIPE, text=True, check=True,
    )
    return Path(out.stdout.strip().splitlines()[-1]) / f"{token}.exe"

# A bare version atom: a whole string that is just a dotted version with at least
# three components (optionally a trailing letter, e.g. openssl "1.0.0g"). Three+
# components keeps real versions (1.2.3, 1.5.13, 4.2.21) and rejects the swarm of
# two-component float literals ("4.444", "508.9") that otherwise masquerade as
# versions. IPv4 dotted-quads are filtered separately.
BARE_VER = re.compile(r"^\d+\.\d+\.\d+(?:\.\d+)?[a-z]?$")
IPV4 = re.compile(r"^(\d{1,3}\.){3}\d{1,3}$")


def is_version_atom(s: str) -> bool:
    return bool(BARE_VER.match(s)) and not IPV4.match(s)


def exe_strings(exe: Path) -> list[str]:
    """ASCII + UTF-16LE strings of the image (markers seen are all ASCII, but
    pull both so nothing is missed)."""
    out = []
    for args in (["strings", "-n", "4", str(exe)],
                 ["strings", "-n", "4", "-e", "l", str(exe)]):
        out.append(subprocess.run(args, capture_output=True, text=True,
                                  errors="replace").stdout)
    return "\n".join(out).splitlines()


# --- version extractors (binary-confirmed exact version) -------------------

def v_zlib(blob: str):
    m = re.search(r"(?:inflate|deflate) (\d+\.\d+\.\d+) Copyright", blob)
    if m:
        return m.group(1)
    # Newer builds carry no zlib banner, but OpenSSL's BIO-zlib wrapper proves
    # zlib is linked (version no longer exposed in the exe). Case varies:
    # 1.0.x exports the `BIO_ZLIB_*` macro names, 1.1.x the lowercase functions.
    if re.search(r"bio_zlib_new|zlib compression", blob, re.I):
        return "present (no banner)"
    return None


def v_openssl(blob: str):
    m = re.search(r"OpenSSL (\d+\.\d+\.\d+[a-z]*) (\d+ \w+ \d+)", blob)
    if m:
        return f"{m.group(1)} ({m.group(2)})"
    # 1.1.x is built without the classic banner, but the static-build path and
    # CRYPTOGAMS asm strings leak the branch.
    if re.search(r"engines-1_1|/lib/engines-1_1", blob):
        return "1.1.x (static, no banner)"
    if "CRYPTOGAMS" in blob or "@openssl.org" in blob or "ssleay" in blob.lower():
        return "present (no banner)"
    return None


def v_scaleform(lines: list[str], blob: str):
    # Statically linked: the GFx RTTI namespace is in the exe and bakes a
    # 3-component "4.x.y" version string (source snapshot was 4.0.15; shipped
    # exes carry 4.2.21). Require all three components so two-component float
    # noise ("4.444", "4.565") can't masquerade as a version.
    if "@Scaleform@@" in blob:
        cands = sorted({s for s in lines if re.match(r"^4\.\d+\.\d+$", s)})
        return ", ".join(cands) if cands else "present (version not isolated)"
    # Later builds move GFx into vostok_scaleform.dll; the exe only references it.
    if "scaleform" in blob.lower() or ".gfx" in blob.lower():
        return "in vostok_scaleform.dll"
    return None


def v_stl(blob: str):
    """Which C++ standard library: STLport (early) vs the MSVC std:: (later)."""
    if "@stlp_std@@" in blob:
        return "STLport 5.2.1"
    if "@std@@" in blob or "char_traits@D@std@@" in blob:
        return "MSVC std::"
    return None


def pe_arch(exe: Path):
    """PE Machine field: 0x14c = x86, 0x8664 = x64."""
    try:
        with exe.open("rb") as f:
            f.seek(0x3C)
            pe = int.from_bytes(f.read(4), "little")
            f.seek(pe + 4)
            m = int.from_bytes(f.read(2), "little")
        return {0x14C: "x86", 0x8664: "x64", 0xAA64: "arm64"}.get(m, hex(m))
    except OSError:
        return "?"


def v_bugtrap(build_dir: Path):
    """BugTrap ships as a side-by-side bugtrap.dll; its 4-component FileVersion
    sits in the DLL's UTF-16 version resource (not in survarium.exe)."""
    dlls = list(build_dir.glob("bugtrap*.dll")) + list(build_dir.glob("BugTrap*.dll"))
    if not dlls:
        return None
    txt = subprocess.run(["strings", "-e", "l", "-n", "4", str(dlls[0])],
                         capture_output=True, text=True, errors="replace").stdout
    vers = sorted({s for s in txt.splitlines()
                   if re.match(r"^\d+\.\d+\.\d+\.\d+$", s)})
    return vers[0] if vers else None


def v_libpng(lines: list[str], blob: str):
    if "libpng" not in blob:
        return None
    # PNG_LIBPNG_VER_STRING is a bare "1.5.x"/"1.6.x" atom in .rdata.
    cands = sorted({s for s in lines if is_version_atom(s)
                    and re.match(r"1\.[5-9]\.", s)})
    return ", ".join(cands) if cands else "present (version string not isolated)"


# --- presence markers (linked, version from versions.txt) ------------------
# token substring -> proves the lib is statically linked into the exe.

PRESENCE = [
    # key,        display,                manifest ver,  markers (any-of),                          note
    ("scaleform", "Scaleform GFx",        None,          ["@Scaleform@@", "Scaleform ", "vostok_scaleform", "Scaleform textures"], "Flash UI middleware; **not in versions.txt** (its own source snapshot is 4.0.15, but every static exe carries 4.2.21). By the 2022 build it is split into `vostok_scaleform.dll`"),
    ("zlib",      "zlib (engine)",        "1.2.3",       ["inflate 1.2.3", "deflate 1.2.3", "bio_zlib_new", "zlib compression"], "the engine's own zlib (`inflate/deflate 1.2.3 Copyright …`). Distinct from the zlib Scaleform bundles for libpng, which shows as the bare `1.2.7` atom"),
    ("openssl",   "OpenSSL",              "1.0.0g",      ["part of OpenSSL", "OpenSSL 1.0", "CRYPTOGAMS", "engines-1_1"], "TLS/crypto; the ≤0.23h builds print `OpenSSL 1.0.0g 18 Jan 2012`. **Bumped over time** — see the matrix"),
    ("libpng",    "libpng (Scaleform)",  None,          ["libpng"],                                "PNG decoder **bundled inside Scaleform GFx** (`Application built with libpng-`, `GFx_InflateWrapper`); not a standalone engine dep"),
    ("libjpeg",   "libjpeg (Scaleform)", None,          ["Thomas G. Lane", "JPEG library version"], "JPEG decoder bundled with Scaleform GFx (`Copyright (C) 2012, Thomas G. Lane, Guido Vollbeding`); ships no clean version string, constant across builds"),
    ("expat",     "Expat (XML)",         None,          ["XML_DTD support in Expat", "expat_"],     "XML parser (Scaleform/engine); **not in versions.txt**, emits no version string"),
    ("boost",     "Boost",               "1.48.0",      ["@boost@@", "@gregorian@boost@@"],        "pervasive (bind/asio/gregorian); header/template lib, prints no version of its own — version is the manifest's"),
    ("stlport",   "STLport",             "5.2.1",       ["@stlp_std@@", "STLPORT_"],               "the STL implementation (`stlp_std` namespace) — Survarium does not use the MSVC STL"),
    ("bullet",    "Bullet",              None,          ["btCollisionWorld", "btCollisionObject"], "physics/collision (`btCollisionWorld`); **not in versions.txt** but linked in every build. Its **SoftBody module** (`@btSoftBody@@`) was present 0.100b→0.26e0 and **dropped at 0.26g0** (see the 0.25–0.31 sweep)"),
    ("opcode",    "OPCODE",              "1.3",         ["@Opcode@@"],                             "collision trees (`Opcode::AABB*Tree`); coexists with Bullet"),
    ("wildmagic", "WildMagic",           "4.9",         ["@Wm4@@"],                                "geometry math; the `Wm4` namespace pins the **major version at 4** (manifest says 4.9)"),
    ("vorbis",    "libVorbis",           "1.2.3",       ["OggVorbis_File", "vorbis bitstream"],    "audio codec (`OggVorbis_File`, `Error in vorbis bitstream`); vendor string not shipped, so version is the manifest's"),
    ("ogg",       "libogg",              "1.1.4",       ["OggVorbis_File"],                        "the Ogg container under libVorbis"),
    ("bugtrap",   "BugTrap",             "1.3.3291.42976", ["BugTrap.dll", "BugTrapN.dll"],        "crash reporter; the exe references `BugTrap.dll` and the **4-component FileVersion read from the side-by-side `bugtrap.dll` resource** confirms 1.3.3291.42976 in every build (matches the manifest)"),
    ("speedtree", "SpeedTree",           "5.2.1",       ["SpeedTree", "speedtree"],                "vegetation renderer (`SpeedTree::` namespace + engine `speedtree_cook`). Present through 2013, then **gone from every 2014 build** — dropped at the AI-shooter→PvP pivot (cf. `CHANGES_NARRATIVE.md`)"),
    # libs in the manifest/sources that we expect *might* be linked - report
    # found/not-found honestly:
    ("ode",       "ODE",                 "0.11.1",      ["dxBody", "dWorldStep", "@dxGeom"],       "listed in `versions.txt` (0.11.1) but **never linked** into any game exe — runtime physics is Bullet + OPCODE"),
    ("freeimage", "FreeImage",           "3.12.0",      ["FreeImage", "fipImage"],                 "listed in `versions.txt` (3.12.0) but no marker in any game exe — an editor/asset-pipeline lib, not the runtime"),
    ("theora",    "libtheora",           "1.1.1",       ["libtheora", "Xiph.Org libtheora", "@theora"], "listed in `versions.txt` (1.1.1) but no runtime marker — no in-engine Theora video playback"),
    ("mysql",     "MySQL client",        "6.02",        ["mysql_real_connect", "libmysql", "@mysql"], "listed in `versions.txt` (6.02) but no marker — a backend/master-server dep, not the client"),
    ("minizip",   "minizip",             "1.01",        ["unzReadCurrentFile", "Version made by"], "listed in `versions.txt` (1.01) but no distinct runtime marker"),
    ("lua",       "Lua / LuaJIT",        None,          ["LuaJIT", "Lua 5.1", "Mike Pall", "PUC-Rio"], "no Lua/LuaJIT VM banner in any exe — only data `.lua` asset paths (navmesh/victory_items) are referenced"),
    ("steam",     "Steam API",           None,          ["steam_api", "SteamAPI_", "@steam@@", "@CSteam"], "Valve Steamworks — appears only in the retail Steam build (`steam_api64.dll`)"),
    ("battleye",  "BattlEye",            None,          ["BattlEye", "BEClient", "BEService"],     "anti-cheat — retail Steam build only (`BEClient_x64.dll`)"),
]


# DirectX / system DLLs the exe imports. Grouped D3D11 (kept throughout) vs the
# D3D9/X3DAudio helper path (June-2010 SDK "_43" / "1_7") dropped after 2013.
DX_DLLS = [
    "d3d11.dll", "d3dx11_43.dll", "dxgi.dll", "D3DCOMPILER_43.dll",
    "d3dx9_43.dll", "X3DAudio1_7.dll",
    "d3d9.dll", "ddraw.dll", "XINPUT1_3.dll", "DINPUT8.dll",
    # GPU-vendor + network helper DLLs that appear mid-life (pinned in the
    # 0.25–0.31 sweep): NVAPI/ADL at 0.27b1, iphlpapi at 0.29a3.
    "nvapi.dll", "nvpowerapi.dll", "atiadlxx.dll", "iphlpapi.dll",
]


def scan(exe: Path, build_dir: Path) -> dict:
    lines = exe_strings(exe)
    blob = "\n".join(lines)
    res = {}
    exact = {
        "zlib": v_zlib(blob),
        "openssl": v_openssl(blob),
        "scaleform": v_scaleform(lines, blob),
        "libpng": v_libpng(lines, blob),
        "bugtrap": v_bugtrap(build_dir),
    }
    for key, disp, manifest, markers, note in PRESENCE:
        present = any(mk in blob for mk in markers)
        res[key] = {
            "display": disp,
            "manifest": manifest,
            "note": note,
            "present": present,
            "binary_version": exact.get(key),
        }
    # bare version atoms (cross-check appendix)
    res["_atoms"] = sorted({s for s in lines if is_version_atom(s)})
    # DirectX / system imports (the "43" = June-2010 DX SDK generation; the D3D9
    # helper + X3DAudio path is what the 2014 renderer drops).
    low = blob.lower()
    res["_dx"] = {dll: (dll.lower() in low) for dll in DX_DLLS}
    res["_arch"] = pe_arch(exe)
    res["_stl"] = v_stl(blob)
    return res


def cell(info: dict) -> str:
    """Matrix cell: exact binary version if known, else ✓/✗ for presence."""
    if info["binary_version"]:
        return f"**{info['binary_version']}**"
    if info["present"]:
        return f"✓ ({info['manifest']})" if info["manifest"] else "✓"
    return "—"


# 0.25–0.31 Steam game-tree builds recovered from a local `Survarium_archives.zip`
# (25 full installs, archive.org-uploadable). Their dep surface is uniform —
# OpenSSL 1.0.1h, Scaleform GFx 4.2.21, libpng 1.5.13, x86 — so rather than 25
# near-identical matrix columns, they are summarized here. The one thing that
# moves is the C++ STL, which pins the STLport→std switch precisely. Version +
# date are read from each exe ("Vostok Engine v…" string + the __DATE__ literal).
SWEEP_BUILDS = [
    ("v0.25d0", "2014-11-10"), ("v0.26e0", "2014-12-24"), ("v0.26f0", "2014-12-29"),
    ("v0.26g0", "2015-01-14"), ("v0.26i0", "2015-01-23"), ("v0.27b1", "2015-03-06"),
    ("v0.27c0", "2015-03-13"), ("v0.27d2", "2015-04-01"), ("v0.27d3", "2015-04-17"),
    ("v0.28a2", "2015-04-24"), ("v0.28b0", "2015-04-28"), ("v0.28d0", "2015-06-06"),
    ("v0.29a3", "2015-06-17"), ("v0.29b0", "2015-06-23"), ("v0.29c0", "2015-07-02"),
    ("v0.30a4", "2015-08-07"), ("v0.30b0", "2015-08-12"), ("v0.30c0", "2015-08-20"),
    ("v0.30d0", "2015-08-27"), ("v0.30e0", "2015-08-31"), ("v0.31a2", "2015-09-11"),
    ("v0.31b0", "2015-09-16"), ("v0.31c0", "2015-09-29"), ("v0.31d0", "2015-10-01"),
    ("v0.31e2", "2015-10-12"),
]
# First build on the MSVC std:: STL (everything before is STLport 5.2.1).
SWEEP_STD_FROM = "v0.28a2"
SWEEP_SECTION = (
    ["## 0.25–0.31 sweep (25 Steam game-tree builds)", "",
     "25 full Steam builds (Nov 2014 – Oct 2015) recovered from a local "
     "`Survarium_archives.zip` — the era archive.org only has as sealed `.sup`. "
     "The *versioned* libraries are constant — **x86**, **OpenSSL 1.0.1h**, "
     "**Scaleform GFx 4.2.21**, **libpng 1.5.13**, Boost/OPCODE/WildMagic/libVorbis "
     "static — but the **dependency *surface* is not uniform**; a full per-build diff "
     "finds six transition points:", "",
     "| at version | date | change |",
     "| --- | --- | --- |",
     "| **0.26g0** | 14 Jan 2015 | **Bullet SoftBody dropped** (`@btSoftBody@@` — present 0.100b→0.26e0, gone after) |",
     "| **0.27b1** | 6 Mar 2015 | **NVAPI** (`nvapi`/`nvpowerapi.dll`) + **AMD ADL** (`atiadlxx.dll`) GPU-vendor APIs **added**; **XInput 1.3 removed** |",
     "| **0.27d2** | 1 Apr 2015 | **Steam** integration **added** (`steam_api.dll`) — the Steam launch |",
     "| **0.28a2** | 24 Apr 2015 | **STLport → MSVC `std::`** STL, and the standalone **zlib banner drops** (zlib now via OpenSSL's BIO). 0.27d3 is the last STLport build |",
     "| **0.29a3** | 17 Jun 2015 | **`iphlpapi.dll`** (IP-helper / network) **added** |",
     "",
     "Downstream: NVAPI is later dropped again (absent by the 2022 build); AMD ADL, "
     "iphlpapi and Steam persist to 2022. (0.28d0 is a one-off build whose OpenSSL "
     "module banners were stripped — OpenSSL is still linked; its lone `2.3.5` atom "
     "is binary noise, not a library.) Build # / internal id are **not** in these "
     "exes — the Steam depot supplies them at launch — so only version + date are "
     "binary-derivable.", "",
     "**Per-build version, date, STL** (the rest is constant per above):", "",
     "| version | date | C++ STL |", "| --- | --- | --- |"]
    + [f"| {v} | {d[2:]} | {'STLport 5.2.1' if v < SWEEP_STD_FROM else 'MSVC std::'} |"
       for (v, d) in SWEEP_BUILDS]
    + [""]
)


def main() -> None:
    if shutil.which("strings") is None:
        sys.exit("deps_report: `strings` not found (binutils) - run in nix develop")
    # Merge the flake-fetched registry builds (≤0.23h, PDB-bearing) with the
    # hand-extracted post-0.23 exes, ordered chronologically by release date.
    reg = [{**v, "kind": "registry"} for v in c.registry()]
    # exe-tier builds: keep any with a local cached exe OR a flake-fetchable
    # exe_url; drop only ones with neither source.
    extra = []
    for v in extra_registry():
        if (c.REPO_DIR / v["exe"]).exists() or v.get("exe_url"):
            extra.append({**v, "kind": "extra"})
        else:
            c.log("deps", f"skip {v['label']}: no local exe and no exe_url")
    entries = sorted(reg + extra, key=lambda v: v.get("date", "9999"))
    labels = [v["label"] for v in entries]
    meta = {v["label"]: v for v in entries}
    dates = {v["label"]: v.get("date", "?") for v in entries}

    def col(lab: str) -> str:                       # version token for headers
        return lab.split("-")[0].replace("v", "")

    scans = {}
    for v in entries:
        lab = v["label"]
        if v["kind"] == "registry":
            c.log("deps", f"scanning {lab} (build {v.get('build')})")
            d = c.fetch_from_flake(lab)
            exe = d / "survarium.exe"
            if not exe.exists():
                exe, _ = c.find_exe_pdb(d)
            bdir = d
        else:
            exe = c.REPO_DIR / v["exe"]
            if exe.exists():
                c.log("deps", f"scanning {lab} ({v.get('arch', '?')}, cached exe)")
            else:
                token = col(lab)
                c.log("deps", f"fetching {lab} exe via flake .#\"{token}\"")
                exe = fetch_exe_via_flake(token)
            bdir = exe.parent
        scans[lab] = scan(exe, bdir)

    keys = [k for (k, *_rest) in PRESENCE]

    def display_of(k):
        return scans[labels[0]][k]["display"]

    md = ["# Third-party dependency versions across builds (0.100b → 2022)", "",
          "Which third-party libraries are linked into each `survarium.exe`, and at "
          "what version, read **straight from the binary** — so this covers the "
          "symbol-less builds too (0.23h, and the hand-extracted post-0.23 exes): the "
          "markers are `.rdata` version strings + RTTI `.?AV…@@` type-descriptor names, "
          "neither of which lives in a PDB. Method/markers: `scripts/deps_report.py`; "
          "how the post-0.23 exes were pulled: `docs/extracting-exes.md`.", "",
          "**Bold = exact version read from a binary marker** (the library's own "
          "version string, or the `bugtrap.dll` resource) — so it can change "
          "build-to-build and reveal a real bump. `✓ (x.y)` = library is linked "
          "(RTTI/symbol marker present) but prints no version, so the version is the "
          "one declared in `vostok/sources/versions.txt`. `—` = no marker found.", "",
          "**Coverage:** the nine ≤0.23h builds + **0.26e0 / 0.26g0** (Dec 2014 / Jan "
          "2015) + **0.34a0** (Dec 2015) + **0.69d0** (the last Steam build, 2022). The "
          "many builds in between (0.25/0.27–0.33/0.44–0.68) ship their game tree inside "
          "an **encrypted custom `!sup` installer** (uniform-entropy payload, RSA-signed) "
          "that no tool extracts — see `docs/extracting-exes.md`. Only the four archive.org "
          "items that happen to be **game-tree dumps** (`survarium_full_026e0/026g0/034a0` "
          "and the 2022 `Survarium.zip`) are readable past 0.23h.", ""]

    # --- bottom line: the stable ≤0.23h core, then what moved after ---------
    core = [lab for lab in labels if meta[lab]["kind"] == "registry"]
    md += ["## Bottom line", "",
           f"**The ≤0.23h core ({len(core)} builds, 2013–2014) is rock-stable:** every "
           "binary-readable version is identical across all of them — Scaleform GFx "
           "**4.2.21**, engine zlib **1.2.3** (+ Scaleform's bundled zlib **1.2.7**), "
           "OpenSSL **1.0.0g**, libpng **1.5.13**, BugTrap **1.3.3291.42976** — with the "
           "only motion being SpeedTree and the D3D9 helper path dropping at the 2014 "
           "PvP pivot (see `CHANGES_NARRATIVE.md`).", "",
           "**What actually moves once you go past 0.23h:**",
           "- **OpenSSL is the one library that gets version-bumped.** "
           "`1.0.0g (18 Jan 2012)` all through ≤0.23h → **`1.0.1h (5 Jun 2014)`** by "
           "0.26e0/0.26g0 (the post-Heartbleed branch) → **`1.1.x`** (static, no banner) "
           "in the 2022 build. Everything else binary-readable holds: Scaleform stays "
           "**4.2.21** through 0.26g0, zlib **1.2.3**, libpng **1.5.13**.",
           "- **The toolchain modernizes in two steps, not one.** The STL swap is "
           "pinned by a 25-build 0.25–0.31 sweep (see below): **STLport through 0.27d3 "
           "(17 Apr 2015) → the MSVC `std::` STL at 0.28a2 (24 Apr 2015)** — still an "
           "x86 build with Scaleform 4.2.21 / OpenSSL 1.0.1h. By **0.34a0 (Dec 2015)** "
           "the standalone zlib banner is also gone (zlib rides in via OpenSSL's BIO). "
           "Then the **2022 build (0.69d0)** finishes the job: first **x64** exe, "
           "**Scaleform moved out into `vostok_scaleform.dll`**, OpenSSL to **1.1.x**, "
           "plus **Steam** (`steam_api64`) and **BattlEye**. Boost, Bullet, OPCODE and "
           "libVorbis/ogg stay statically linked throughout.",
           "- **Mining the 2022 component DLLs** (per the same method): "
           "`vostok_scaleform.dll` still carries Scaleform GFx 4.x (AS2+AS3, now with "
           "DefineBitsJPEG4) but with **libpng bumped 1.5.13 → 1.5.27** and the same "
           "bundled zlib 1.2.3/1.2.7; the side-by-side `bugtrap.dll`, `steam_api64.dll` "
           "and `BEClient_x64.dll` are the only other shipped libraries.",
           "- **Still never linked into any runtime exe** (manifest/editor-only): " +
           ", ".join(display_of(k) for k in keys
                     if not any(scans[lab][k]["present"] for lab in labels)) +
           ". The \"FMOD\"/\"libcurl\" one might expect in a modern build are **not** "
           "present — those string hits are the libc `fmod()` and \"curly-bracket\", "
           "not the middleware.", ""]

    # matrix ----------------------------------------------------------------
    md += ["## Matrix (columns = version)", "",
           "| dependency \\ version | " + " | ".join(col(lab) for lab in labels) + " |",
           "| --- | " + " | ".join(":-:" for _ in labels) + " |"]
    md.append("| _build_ | " + " | ".join(
        (str(meta[lab].get("build")) if meta[lab].get("build") else "—") for lab in labels) + " |")
    md.append("| _date_ | " + " | ".join(dates[lab][2:] for lab in labels) + " |")
    md.append("| _arch_ | " + " | ".join(scans[lab]["_arch"] for lab in labels) + " |")
    md.append("| _C++ STL_ | " + " | ".join(
        (scans[lab]["_stl"] or "—") for lab in labels) + " |")
    for k in keys:
        row = [cell(scans[lab][k]) for lab in labels]
        md.append(f"| {display_of(k)} | " + " | ".join(row) + " |")
    md.append("")

    # per-dep prose: highlight changes (segment by version token) -----------
    md += ["## Per-dependency notes", ""]
    for k in keys:
        note = scans[labels[0]][k]["note"]
        series = [cell(scans[lab][k]) for lab in labels]
        changed = len(set(series)) > 1
        bump = " — **changes across builds**" if changed else ""
        md.append(f"- **{display_of(k)}**{bump}: {note}.")
        if changed:
            runs = []
            for lab in labels:
                ver = cell(scans[lab][k])
                if runs and runs[-1][1] == ver:
                    runs[-1][0].append(col(lab))
                else:
                    runs.append([[col(lab)], ver])
            seg = "; ".join(
                f"{(bs[0] if len(bs) == 1 else f'{bs[0]}–{bs[-1]}')} → {ver}"
                for bs, ver in runs)
            md.append(f"  - {seg}")
    md.append("")

    # DirectX / system import generation ------------------------------------
    md += ["## DirectX / system imports", "",
           "Imported DLLs (not statically linked, so no version *string* — the "
           "filename suffix is the version: `_43` = the June-2010 DirectX SDK "
           "generation, `1_7`/`1_3` = X3DAudio/XInput versions). The renderer "
           "transition shows here: the **Direct3D 9 helper lib `d3dx9_43` and "
           "`X3DAudio1_7` are dropped after the 2013 builds**, leaving the "
           "D3DX/shader surface D3D11-only (`d3dx11_43` + `D3DCOMPILER_43`); by 2022 "
           "even the D3DX redists are gone (the exe links D3D11/DXGI directly). The "
           "**GPU-vendor + network helpers** (`nvapi`/`nvpowerapi` = NVAPI, "
           "`atiadlxx` = AMD ADL, `iphlpapi`) are a **mid-life addition** — the "
           "0.25–0.31 sweep pins NVAPI+ADL to 0.27b1 and iphlpapi to 0.29a3; NVAPI is "
           "then dropped again by the 2022 build, ADL/iphlpapi persist.", "",
           "| import \\ version | " + " | ".join(col(lab) for lab in labels) + " |",
           "| --- | " + " | ".join(":-:" for _ in labels) + " |"]
    for dll in DX_DLLS:
        row = ["✓" if scans[lab]["_dx"][dll] else "—" for lab in labels]
        md.append(f"| `{dll}` | " + " | ".join(row) + " |")
    md.append("")

    # 0.25-0.31 dense sweep (25 Steam game-tree builds from Survarium_archives.zip)
    md += SWEEP_SECTION

    # appendix: bare version atoms per build --------------------------------
    md += ["## Appendix — bare version atoms in each image", "",
           "Every standalone `x.y[.z]` string in the image (cross-check / unattributed "
           "leftovers). Useful to spot a version that moved without a named marker.", ""]
    for lab in labels:
        md.append(f"- **{col(lab)}** (`{lab}`): " +
                  (", ".join(f"`{a}`" for a in scans[lab]["_atoms"]) or "_none isolated_"))
    md.append("")

    REPORTS_DIR.mkdir(exist_ok=True)
    (REPORTS_DIR / "DEPENDENCY_VERSIONS.md").write_text("\n".join(md) + "\n")
    c.log("deps", f"{len(keys)} deps × {len(labels)} builds -> reports/DEPENDENCY_VERSIONS.md")


if __name__ == "__main__":
    main()
