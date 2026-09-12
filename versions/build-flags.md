# Build-flags comparison across versions

Per link-unit `cl.exe` flags / LTCG state from each PDB (`pdb_build_info`), by build number. `LTCG` = whole-program optimized, no per-TU command line (the matching "LTCG wall"). File-count-only diffs are normalized out.

## Engine libs (vostok/*) with changed flags (3)

### `vostok_core-static-gold`
- **802–884:** [no cmdline] LTCG
- **1916–2010:** /MT -GF -GS- -GT -MP -MT -O1 -Ob2 -Oi -Os -Oy -TP -Zi -arch:SSE2

### `vostok_libfoundation-static`
- **802–884:** [no cmdline] LTCG,/GS
- **1916–2010:** [no cmdline] LTCG

### `vostok_sound-static-gold`
- **802–884:** /MT -GF -GS- -GT -MP -MT -Ob2 -Od -Oi -Oy -TP -Zi -arch:SSE2
- **1916–2010:** [no cmdline] LTCG

## Other libs with changed flags (3)

### `libboost_regex-vc90-mt-sp-1_48`
- **802–1923:** _(absent / no per-TU flags)_
- **2010:** [no cmdline] /GS,no-debug

### `speedtreecore_v5.2_vc90mt_static`
- **802–884:** [no cmdline] /GS,no-debug
- **1916–2010:** _(absent / no per-TU flags)_

### `speedtreeforest_v5.2_vc90mt_static`
- **802–884:** [no cmdline] /GS,no-debug
- **1916–2010:** _(absent / no per-TU flags)_

_All other 25 engine libs are **LTCG in every build** (game_core, network_core, logging, core, render, physics, …) — unchanged._

## Optimization & floating-point notes

- **Only these engine libs are non-LTCG** (so a per-TU opt level is recorded): `vostok_core-static-gold`, `vostok_sound-static-gold`, `vostok_vorbisfile-static-gold`. Every other engine lib (game_core, network_core, logging, …) is whole-program **LTCG** — optimized at link, with no per-TU opt level recorded (so it is *not* unoptimized; the level just isn't visible). The only genuinely unoptimized code is the audio path: `vostok_sound` (`-Od`) until v0.20, and `vostok_vorbisfile` (no `-O`) throughout.
- **`/fp:fast` was not removed** — it appears in `vostok_core-static-gold`, `vostok_sound-static-gold`, `zlib` in every build. (LTCG libs record no command line, so their fp model isn't visible either way — we can't see whether game_core etc. use fp:fast.)

## Raw per-step tool labels (incl. file-count-only diffs)

| step | projects flagged by `pdb_build_info --compare` |
| --- | --- |
| 802 → 816 | _none_ |
| 816 → 826 | _none_ |
| 826 → 870 | _none_ |
| 870 → 884 | _none_ |
| 884 → 1916 | `libcmt` (DIFF-FLAGS), `libgfx` (DIFF-FLAGS), `vostok_core-static-gold` (PARTIAL (cmdline one side)), `vostok_libfoundation-static` (PARTIAL (cmdline one side)), `vostok_sound-static-gold` (PARTIAL (cmdline one side)), `d3dx9` (no cmdline), `speedtreecore_v5.2_vc90mt_static` (no cmdline), `speedtreeforest_v5.2_vc90mt_static` (no cmdline), `x3daudio` (no cmdline) |
| 1916 → 1923 | _none_ |
| 1923 → 2010 | `libgfx` (DIFF-FLAGS), `vostok_core-static-gold` (DIFF-FLAGS), `libboost_regex-vc90-mt-sp-1_48` (no cmdline) |
