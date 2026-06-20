# Third-party dependency versions across builds (0.100b → 2022)

Which third-party libraries are linked into each `survarium.exe`, and at what version, read **straight from the binary** — so this covers the symbol-less builds too (0.23h, and the hand-extracted post-0.23 exes): the markers are `.rdata` version strings + RTTI `.?AV…@@` type-descriptor names, neither of which lives in a PDB. Method/markers: `scripts/deps_report.py`; how the post-0.23 exes were pulled: `docs/extracting-exes.md`.

**Bold = exact version read from a binary marker** (the library's own version string, or the `bugtrap.dll` resource) — so it can change build-to-build and reveal a real bump. `✓ (x.y)` = library is linked (RTTI/symbol marker present) but prints no version, so the version is the one declared in `vostok/sources/versions.txt`. `—` = no marker found.

**Coverage:** the nine ≤0.23h builds + **0.26e0 / 0.26g0** (Dec 2014 / Jan 2015) + **0.34a0** (Dec 2015) + **0.69d0** (the last Steam build, 2022). The many builds in between (0.25/0.27–0.33/0.44–0.68) ship their game tree inside an **encrypted custom `!sup` installer** (uniform-entropy payload, RSA-signed) that no tool extracts — see `docs/extracting-exes.md`. Only the four archive.org items that happen to be **game-tree dumps** (`survarium_full_026e0/026g0/034a0` and the 2022 `Survarium.zip`) are readable past 0.23h.

## Bottom line

**The ≤0.23h core (9 builds, 2013–2014) is rock-stable:** every binary-readable version is identical across all of them — Scaleform GFx **4.2.21**, engine zlib **1.2.3** (+ Scaleform's bundled zlib **1.2.7**), OpenSSL **1.0.0g**, libpng **1.5.13**, BugTrap **1.3.3291.42976** — with the only motion being SpeedTree and the D3D9 helper path dropping at the 2014 PvP pivot (see `CHANGES_NARRATIVE.md`).

**What actually moves once you go past 0.23h:**
- **OpenSSL is the one library that gets version-bumped.** `1.0.0g (18 Jan 2012)` all through ≤0.23h → **`1.0.1h (5 Jun 2014)`** by 0.26e0/0.26g0 (the post-Heartbleed branch) → **`1.1.x`** (static, no banner) in the 2022 build. Everything else binary-readable holds: Scaleform stays **4.2.21** through 0.26g0, zlib **1.2.3**, libpng **1.5.13**.
- **The toolchain modernizes in two steps, not one.** The STL swap is pinned by a 25-build 0.25–0.31 sweep (see below): **STLport through 0.27d3 (17 Apr 2015) → the MSVC `std::` STL at 0.28a2 (24 Apr 2015)** — still an x86 build with Scaleform 4.2.21 / OpenSSL 1.0.1h. By **0.34a0 (Dec 2015)** the standalone zlib banner is also gone (zlib rides in via OpenSSL's BIO). Then the **2022 build (0.69d0)** finishes the job: first **x64** exe, **Scaleform moved out into `vostok_scaleform.dll`**, OpenSSL to **1.1.x**, plus **Steam** (`steam_api64`) and **BattlEye**. Boost, Bullet, OPCODE and libVorbis/ogg stay statically linked throughout.
- **Mining the 2022 component DLLs** (per the same method): `vostok_scaleform.dll` still carries Scaleform GFx 4.x (AS2+AS3, now with DefineBitsJPEG4) but with **libpng bumped 1.5.13 → 1.5.27** and the same bundled zlib 1.2.3/1.2.7; the side-by-side `bugtrap.dll`, `steam_api64.dll` and `BEClient_x64.dll` are the only other shipped libraries.
- **Still never linked into any runtime exe** (manifest/editor-only): ODE, FreeImage, libtheora, MySQL client, minizip, Lua / LuaJIT. The "FMOD"/"libcurl" one might expect in a modern build are **not** present — those string hits are the libc `fmod()` and "curly-bracket", not the middleware.

## Matrix (columns = version)

| dependency \ version | 0.100b | 0.1.1a | 0.1.1b | 0.1.1c | 0.1.1e | 0.20e | 0.20f | 0.21d | 0.23h | 0.26e0 | 0.26g0 | 0.34a0 | 0.69d0 |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| _build_ | 802 | 816 | 826 | 870 | 884 | 1916 | 1923 | 2010 | 2285 | 2727 | 2777 | 3545 | — |
| _date_ | 13-05-09 | 13-05-14 | 13-05-14 | 13-05-24 | 13-05-28 | 14-03-20 | 14-04-01 | 14-04-24 | 14-07-17 | 14-12-24 | 15-01-14 | 15-12-25 | 22-06-01 |
| _arch_ | x86 | x86 | x86 | x86 | x86 | x86 | x86 | x86 | x86 | x86 | x86 | x86 | x64 |
| _C++ STL_ | STLport 5.2.1 | STLport 5.2.1 | STLport 5.2.1 | STLport 5.2.1 | STLport 5.2.1 | STLport 5.2.1 | STLport 5.2.1 | STLport 5.2.1 | STLport 5.2.1 | STLport 5.2.1 | STLport 5.2.1 | MSVC std:: | MSVC std:: |
| Scaleform GFx | **4.2.21** | **4.2.21** | **4.2.21** | **4.2.21** | **4.2.21** | **4.2.21** | **4.2.21** | **4.2.21** | **4.2.21** | **4.2.21** | **4.2.21** | **4.2.21** | **in vostok_scaleform.dll** |
| zlib (engine) | **1.2.3** | **1.2.3** | **1.2.3** | **1.2.3** | **1.2.3** | **1.2.3** | **1.2.3** | **1.2.3** | **1.2.3** | **1.2.3** | **1.2.3** | **present (no banner)** | **present (no banner)** |
| OpenSSL | **1.0.0g (18 Jan 2012)** | **1.0.0g (18 Jan 2012)** | **1.0.0g (18 Jan 2012)** | **1.0.0g (18 Jan 2012)** | **1.0.0g (18 Jan 2012)** | **1.0.0g (18 Jan 2012)** | **1.0.0g (18 Jan 2012)** | **1.0.0g (18 Jan 2012)** | **1.0.0g (18 Jan 2012)** | **1.0.1h (5 Jun 2014)** | **1.0.1h (5 Jun 2014)** | **1.0.1h (5 Jun 2014)** | **1.1.x (static, no banner)** |
| libpng (Scaleform) | **1.5.13** | **1.5.13** | **1.5.13** | **1.5.13** | **1.5.13** | **1.5.13** | **1.5.13** | **1.5.13** | **1.5.13** | **1.5.13** | **1.5.13** | **1.5.13** | — |
| libjpeg (Scaleform) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| Expat (XML) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| Boost | ✓ (1.48.0) | ✓ (1.48.0) | ✓ (1.48.0) | ✓ (1.48.0) | ✓ (1.48.0) | ✓ (1.48.0) | ✓ (1.48.0) | ✓ (1.48.0) | ✓ (1.48.0) | ✓ (1.48.0) | ✓ (1.48.0) | ✓ (1.48.0) | ✓ (1.48.0) |
| STLport | ✓ (5.2.1) | ✓ (5.2.1) | ✓ (5.2.1) | ✓ (5.2.1) | ✓ (5.2.1) | ✓ (5.2.1) | ✓ (5.2.1) | ✓ (5.2.1) | ✓ (5.2.1) | ✓ (5.2.1) | ✓ (5.2.1) | — | — |
| Bullet | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| OPCODE | ✓ (1.3) | ✓ (1.3) | ✓ (1.3) | ✓ (1.3) | ✓ (1.3) | ✓ (1.3) | ✓ (1.3) | ✓ (1.3) | ✓ (1.3) | ✓ (1.3) | ✓ (1.3) | ✓ (1.3) | ✓ (1.3) |
| WildMagic | ✓ (4.9) | ✓ (4.9) | ✓ (4.9) | ✓ (4.9) | ✓ (4.9) | ✓ (4.9) | ✓ (4.9) | ✓ (4.9) | ✓ (4.9) | ✓ (4.9) | ✓ (4.9) | ✓ (4.9) | — |
| libVorbis | ✓ (1.2.3) | ✓ (1.2.3) | ✓ (1.2.3) | ✓ (1.2.3) | ✓ (1.2.3) | ✓ (1.2.3) | ✓ (1.2.3) | ✓ (1.2.3) | ✓ (1.2.3) | ✓ (1.2.3) | ✓ (1.2.3) | ✓ (1.2.3) | ✓ (1.2.3) |
| libogg | ✓ (1.1.4) | ✓ (1.1.4) | ✓ (1.1.4) | ✓ (1.1.4) | ✓ (1.1.4) | ✓ (1.1.4) | ✓ (1.1.4) | ✓ (1.1.4) | ✓ (1.1.4) | ✓ (1.1.4) | ✓ (1.1.4) | ✓ (1.1.4) | ✓ (1.1.4) |
| BugTrap | **1.3.3291.42976** | **1.3.3291.42976** | **1.3.3291.42976** | **1.3.3291.42976** | **1.3.3291.42976** | **1.3.3291.42976** | **1.3.3291.42976** | **1.3.3291.42976** | **1.3.3291.42976** | ✓ (1.3.3291.42976) | ✓ (1.3.3291.42976) | ✓ (1.3.3291.42976) | ✓ (1.3.3291.42976) |
| SpeedTree | ✓ (5.2.1) | ✓ (5.2.1) | ✓ (5.2.1) | ✓ (5.2.1) | ✓ (5.2.1) | — | — | — | — | — | — | — | — |
| ODE | — | — | — | — | — | — | — | — | — | — | — | — | — |
| FreeImage | — | — | — | — | — | — | — | — | — | — | — | — | — |
| libtheora | — | — | — | — | — | — | — | — | — | — | — | — | — |
| MySQL client | — | — | — | — | — | — | — | — | — | — | — | — | — |
| minizip | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Lua / LuaJIT | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Steam API | — | — | — | — | — | — | — | — | — | — | — | ✓ | ✓ |
| BattlEye | — | — | — | — | — | — | — | — | — | — | — | — | ✓ |

## Per-dependency notes

- **Scaleform GFx** — **changes across builds**: Flash UI middleware; **not in versions.txt** (its own source snapshot is 4.0.15, but every static exe carries 4.2.21). By the 2022 build it is split into `vostok_scaleform.dll`.
  - 0.100b–0.34a0 → **4.2.21**; 0.69d0 → **in vostok_scaleform.dll**
- **zlib (engine)** — **changes across builds**: the engine's own zlib (`inflate/deflate 1.2.3 Copyright …`). Distinct from the zlib Scaleform bundles for libpng, which shows as the bare `1.2.7` atom.
  - 0.100b–0.26g0 → **1.2.3**; 0.34a0–0.69d0 → **present (no banner)**
- **OpenSSL** — **changes across builds**: TLS/crypto; the ≤0.23h builds print `OpenSSL 1.0.0g 18 Jan 2012`. **Bumped over time** — see the matrix.
  - 0.100b–0.23h → **1.0.0g (18 Jan 2012)**; 0.26e0–0.34a0 → **1.0.1h (5 Jun 2014)**; 0.69d0 → **1.1.x (static, no banner)**
- **libpng (Scaleform)** — **changes across builds**: PNG decoder **bundled inside Scaleform GFx** (`Application built with libpng-`, `GFx_InflateWrapper`); not a standalone engine dep.
  - 0.100b–0.34a0 → **1.5.13**; 0.69d0 → —
- **libjpeg (Scaleform)** — **changes across builds**: JPEG decoder bundled with Scaleform GFx (`Copyright (C) 2012, Thomas G. Lane, Guido Vollbeding`); ships no clean version string, constant across builds.
  - 0.100b–0.34a0 → ✓; 0.69d0 → —
- **Expat (XML)** — **changes across builds**: XML parser (Scaleform/engine); **not in versions.txt**, emits no version string.
  - 0.100b–0.34a0 → ✓; 0.69d0 → —
- **Boost**: pervasive (bind/asio/gregorian); header/template lib, prints no version of its own — version is the manifest's.
- **STLport** — **changes across builds**: the STL implementation (`stlp_std` namespace) — Survarium does not use the MSVC STL.
  - 0.100b–0.26g0 → ✓ (5.2.1); 0.34a0–0.69d0 → —
- **Bullet**: physics/collision (`btCollisionWorld`); **not in versions.txt** but linked in every build. Its **SoftBody module** (`@btSoftBody@@`) was present 0.100b→0.26e0 and **dropped at 0.26g0** (see the 0.25–0.31 sweep).
- **OPCODE**: collision trees (`Opcode::AABB*Tree`); coexists with Bullet.
- **WildMagic** — **changes across builds**: geometry math; the `Wm4` namespace pins the **major version at 4** (manifest says 4.9).
  - 0.100b–0.34a0 → ✓ (4.9); 0.69d0 → —
- **libVorbis**: audio codec (`OggVorbis_File`, `Error in vorbis bitstream`); vendor string not shipped, so version is the manifest's.
- **libogg**: the Ogg container under libVorbis.
- **BugTrap** — **changes across builds**: crash reporter; the exe references `BugTrap.dll` and the **4-component FileVersion read from the side-by-side `bugtrap.dll` resource** confirms 1.3.3291.42976 in every build (matches the manifest).
  - 0.100b–0.23h → **1.3.3291.42976**; 0.26e0–0.69d0 → ✓ (1.3.3291.42976)
- **SpeedTree** — **changes across builds**: vegetation renderer (`SpeedTree::` namespace + engine `speedtree_cook`). Present through 2013, then **gone from every 2014 build** — dropped at the AI-shooter→PvP pivot (cf. `CHANGES_NARRATIVE.md`).
  - 0.100b–0.1.1e → ✓ (5.2.1); 0.20e–0.69d0 → —
- **ODE**: listed in `versions.txt` (0.11.1) but **never linked** into any game exe — runtime physics is Bullet + OPCODE.
- **FreeImage**: listed in `versions.txt` (3.12.0) but no marker in any game exe — an editor/asset-pipeline lib, not the runtime.
- **libtheora**: listed in `versions.txt` (1.1.1) but no runtime marker — no in-engine Theora video playback.
- **MySQL client**: listed in `versions.txt` (6.02) but no marker — a backend/master-server dep, not the client.
- **minizip**: listed in `versions.txt` (1.01) but no distinct runtime marker.
- **Lua / LuaJIT**: no Lua/LuaJIT VM banner in any exe — only data `.lua` asset paths (navmesh/victory_items) are referenced.
- **Steam API** — **changes across builds**: Valve Steamworks — appears only in the retail Steam build (`steam_api64.dll`).
  - 0.100b–0.26g0 → —; 0.34a0–0.69d0 → ✓
- **BattlEye** — **changes across builds**: anti-cheat — retail Steam build only (`BEClient_x64.dll`).
  - 0.100b–0.34a0 → —; 0.69d0 → ✓

## DirectX / system imports

Imported DLLs (not statically linked, so no version *string* — the filename suffix is the version: `_43` = the June-2010 DirectX SDK generation, `1_7`/`1_3` = X3DAudio/XInput versions). The renderer transition shows here: the **Direct3D 9 helper lib `d3dx9_43` and `X3DAudio1_7` are dropped after the 2013 builds**, leaving the D3DX/shader surface D3D11-only (`d3dx11_43` + `D3DCOMPILER_43`); by 2022 even the D3DX redists are gone (the exe links D3D11/DXGI directly). The **GPU-vendor + network helpers** (`nvapi`/`nvpowerapi` = NVAPI, `atiadlxx` = AMD ADL, `iphlpapi`) are a **mid-life addition** — the 0.25–0.31 sweep pins NVAPI+ADL to 0.27b1 and iphlpapi to 0.29a3; NVAPI is then dropped again by the 2022 build, ADL/iphlpapi persist.

| import \ version | 0.100b | 0.1.1a | 0.1.1b | 0.1.1c | 0.1.1e | 0.20e | 0.20f | 0.21d | 0.23h | 0.26e0 | 0.26g0 | 0.34a0 | 0.69d0 |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| `d3d11.dll` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `d3dx11_43.dll` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| `dxgi.dll` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `D3DCOMPILER_43.dll` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| `d3dx9_43.dll` | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | — | — | — | — | — |
| `X3DAudio1_7.dll` | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | — | — | — | — | — |
| `d3d9.dll` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| `ddraw.dll` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| `XINPUT1_3.dll` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — |
| `DINPUT8.dll` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `nvapi.dll` | — | — | — | — | — | — | — | — | — | — | — | ✓ | — |
| `nvpowerapi.dll` | — | — | — | — | — | — | — | — | — | — | — | ✓ | ✓ |
| `atiadlxx.dll` | — | — | — | — | — | — | — | — | — | — | — | ✓ | ✓ |
| `iphlpapi.dll` | — | — | — | — | — | — | — | — | — | — | — | ✓ | ✓ |

## 0.25–0.31 sweep (25 Steam game-tree builds)

25 full Steam builds (Nov 2014 – Oct 2015) recovered from a local `Survarium_archives.zip` — the era archive.org only has as sealed `.sup`. The *versioned* libraries are constant — **x86**, **OpenSSL 1.0.1h**, **Scaleform GFx 4.2.21**, **libpng 1.5.13**, Boost/OPCODE/WildMagic/libVorbis static — but the **dependency *surface* is not uniform**; a full per-build diff finds six transition points:

| at version | date | change |
| --- | --- | --- |
| **0.26g0** | 14 Jan 2015 | **Bullet SoftBody dropped** (`@btSoftBody@@` — present 0.100b→0.26e0, gone after) |
| **0.27b1** | 6 Mar 2015 | **NVAPI** (`nvapi`/`nvpowerapi.dll`) + **AMD ADL** (`atiadlxx.dll`) GPU-vendor APIs **added**; **XInput 1.3 removed** |
| **0.27d2** | 1 Apr 2015 | **Steam** integration **added** (`steam_api.dll`) — the Steam launch |
| **0.28a2** | 24 Apr 2015 | **STLport → MSVC `std::`** STL, and the standalone **zlib banner drops** (zlib now via OpenSSL's BIO). 0.27d3 is the last STLport build |
| **0.29a3** | 17 Jun 2015 | **`iphlpapi.dll`** (IP-helper / network) **added** |

Downstream: NVAPI is later dropped again (absent by the 2022 build); AMD ADL, iphlpapi and Steam persist to 2022. (0.28d0 is a one-off build whose OpenSSL module banners were stripped — OpenSSL is still linked; its lone `2.3.5` atom is binary noise, not a library.) Build # / internal id are **not** in these exes — the Steam depot supplies them at launch — so only version + date are binary-derivable.

**Per-build version, date, STL** (the rest is constant per above):

| version | date | C++ STL |
| --- | --- | --- |
| v0.25d0 | 14-11-10 | STLport 5.2.1 |
| v0.26e0 | 14-12-24 | STLport 5.2.1 |
| v0.26f0 | 14-12-29 | STLport 5.2.1 |
| v0.26g0 | 15-01-14 | STLport 5.2.1 |
| v0.26i0 | 15-01-23 | STLport 5.2.1 |
| v0.27b1 | 15-03-06 | STLport 5.2.1 |
| v0.27c0 | 15-03-13 | STLport 5.2.1 |
| v0.27d2 | 15-04-01 | STLport 5.2.1 |
| v0.27d3 | 15-04-17 | STLport 5.2.1 |
| v0.28a2 | 15-04-24 | MSVC std:: |
| v0.28b0 | 15-04-28 | MSVC std:: |
| v0.28d0 | 15-06-06 | MSVC std:: |
| v0.29a3 | 15-06-17 | MSVC std:: |
| v0.29b0 | 15-06-23 | MSVC std:: |
| v0.29c0 | 15-07-02 | MSVC std:: |
| v0.30a4 | 15-08-07 | MSVC std:: |
| v0.30b0 | 15-08-12 | MSVC std:: |
| v0.30c0 | 15-08-20 | MSVC std:: |
| v0.30d0 | 15-08-27 | MSVC std:: |
| v0.30e0 | 15-08-31 | MSVC std:: |
| v0.31a2 | 15-09-11 | MSVC std:: |
| v0.31b0 | 15-09-16 | MSVC std:: |
| v0.31c0 | 15-09-29 | MSVC std:: |
| v0.31d0 | 15-10-01 | MSVC std:: |
| v0.31e2 | 15-10-12 | MSVC std:: |

## Appendix — bare version atoms in each image

Every standalone `x.y[.z]` string in the image (cross-check / unattributed leftovers). Useful to spot a version that moved without a named marker.

- **0.100b** (`v0.100b-build802`): `1.2.3`, `1.2.7`, `1.5.13`, `4.2.21`
- **0.1.1a** (`v0.1.1a-build816`): `1.2.3`, `1.2.7`, `1.5.13`, `4.2.21`
- **0.1.1b** (`v0.1.1b-build826`): `1.2.3`, `1.2.7`, `1.5.13`, `4.2.21`
- **0.1.1c** (`v0.1.1c-build870`): `1.2.3`, `1.2.7`, `1.5.13`, `4.2.21`
- **0.1.1e** (`v0.1.1e-build884`): `1.2.3`, `1.2.7`, `1.5.13`, `4.2.21`
- **0.20e** (`v0.20e-build1916`): `1.2.3`, `1.2.7`, `1.5.13`, `4.2.21`
- **0.20f** (`v0.20f-build1923`): `1.2.3`, `1.2.7`, `1.5.13`, `4.2.21`
- **0.21d** (`v0.21d-build2010`): `1.2.3`, `1.2.7`, `1.5.13`, `4.2.21`
- **0.23h** (`v0.23h-build2285`): `1.2.3`, `1.2.7`, `1.5.13`, `4.2.21`
- **0.26e0** (`v0.26e0-build2727`): `1.2.3`, `1.2.7`, `1.5.13`, `4.2.21`
- **0.26g0** (`v0.26g0-build2777`): `1.2.3`, `1.2.7`, `1.5.13`, `4.2.21`
- **0.34a0** (`v0.34a0-build3545`): `1.2.3`, `1.2.7`, `1.5.13`, `4.2.21`
- **0.69d0** (`v0.69d0-2022`): _none isolated_

