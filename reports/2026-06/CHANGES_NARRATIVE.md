# Survarium build evolution — interpreted changes (May 2013)

What the team was most likely working on, **inferred only from added and deleted
hand-written engine functions** across the consecutive internal versions
v0.100b → v0.1.1a → v0.1.1b → v0.1.1c → v0.1.1e (9–28 May 2013). Added/deleted are
unambiguous "a function/class appeared or vanished" events, unlike fuzzy match-%
drift.

## How to read this (and where it lies)

Three ways add/del can mislead, accounted for below:

- **Same-day refactors look like add-then-remove.** v0.1.1a and v0.1.1b are the
  same day (14 May). A class added in v0.1.1a and "removed" in v0.1.1b was almost
  certainly *renamed/restructured*, not introduced and deleted.
- **Offset-parameterized templates are layout drift, not features.** Containers
  like `intrusive_list<…,608,…>` or `single_size_buffer_allocator<108>` bake a
  struct's member offset / object size into a template argument. When a member
  moves, the argument changes and the old/new instantiations show up as
  delete+add — a *layout* change, not a feature.
- The trustworthy signal is **named gameplay/engine classes**
  (`weapon_core`, `sound_rms`, `medkit`, `booby_trap`, `new_sound_propagator`).

---

## v0.100b → v0.1.1a (9 → 14 May): weapons, streamed rendering, sound trim

- **A major weapon state-machine buildout.** `weapon_core` alone gained 44
  functions and lost 20 — a wave of aim/fire/reload predicates (`aimed_fire_pred`,
  `chamber_a_round_*`, `can_jump/can_reload/can_sprint`) — alongside reworked
  `weapon`, `weapon_user_animations_selector`, `weapon_core_shotgun_reload_state`
  and `damage_model`. New `character_dispersion_skill_influence` + reworked
  `character_dispersion_calculator` suggest **weapon spread/accuracy now responds
  to a character skill**.
- **Texture streaming and SpeedTree entered the renderer:** new
  `streaming_ready_texture`, `requested_streamable_texture`,
  `streamable_texture_info` (a streamed-texture pipeline), `speedtree_data`
  (vegetation), plus `game_scene` and instanced `animated_model_instance`.
- **The `sound_rms` subsystem was removed** (`sound_rms`, `sound_rms_cook`,
  `sound_rms_pinned` and its resource pointers) — an RMS/loudness analysis path
  dropped.

## v0.1.1a → v0.1.1b (14 May, same day): a streaming-texture refactor

Nearly everything "new" in v0.1.1a's renderer — `streaming_ready_texture`,
`requested_streamable_texture`, `streamable_texture_info`, `speedtree_data`,
`animated_model_instance` — appears as **removed** the same day, while
`render::backend`, `shader_constant_buffer` and the `constants_handler` templates
are reworked. This is **not a feature reversal but a same-day refactor** of the
just-landed streaming-texture code (renamed or folded into other types).
`weapon_core` keeps churning; `particle::lod_entry` reappears.

## v0.1.1b → v0.1.1c (14 → 24 May): a sound-engine rearchitecture

The 10-day gap is the largest change in the window (101 reworked scopes), and the
dominant theme is **sound**:

- The old codec/"cook" pipeline was torn out — `ogg_sound_cook`,
  `ogg_source_cook`, `ogg_file_contents_cook`, `wav_encoded_sound_interface_cook`,
  `sound_environment_cook`, `ogg_sound`, `effect_cross_fader` all removed.
- A **new sound-propagation path** appears (`new_sound_propagator`) with heavily
  reworked `sound_scene`, `sound_voice`, `single_sound_cook`.
- **Memory pools were retuned:** allocator pools of size 28/108/136 removed and
  32/84/96 added — pooled object sizes changed (layout/tuning, not gameplay).
- Breadth elsewhere: `booby_trap_set_core` (mines/traps), `game_world_ui`,
  `network_client`, physics collision shapes as resources, a shader cache.

## v0.1.1c → v0.1.1e (24 → 28 May): resource/query layout + shadows

- Most add/del here is **layout drift, not features**: a cluster of
  `intrusive_list<resources::query_result, …, 600/608/616/624, …>` instantiations
  swap offsets — the `query_result` struct grew/shifted members, changing the
  baked-in offsets. It counts as +/− but is one structure changing shape.
- Real work shows in **rendering/shadows** (`stage_shadow_direct`, `sun_cascade`
  removed, `renderer`, `portal_sector_system` culling), **resources**
  (`resources_manager`, `hdd_manager`), a **new filesystem** layer
  (`fs_new::virtual_path_string`), and `medkit` gameplay.

---

---

# Part II — into 2014 (v0.20+)

The 10-month gap from v0.1.1e (28 May 2013) to v0.20e (20 Mar 2014) is the
hinge of the dataset. One caveat first: across this jump the add/del counts carry
more noise than the 2013 steps — aligning a v0.20 build's folded symbols to the
year-older base v0.100b falls back heavily — so treat the **magnitude and the named
classes** as solid and the exact integers as approximate.

## v0.1.1e → v0.20e (28 May 2013 → 20 Mar 2014): the pivot — AI shooter → PvP

Near-total rewrite: only **172 functions byte-identical** (+4163 / −6812 / ~4526).
The named-class signal is unambiguous and matches Survarium's real history:

- **Removed — the single-player AI/NPC combat system:** `human_npc` (with
  `attack`, `attack_from_cover`, `attack_melee`, `move_to_position`,
  `is_target_in_melee_range`), `ai::brain_unit`, `ai::ai_world`, `ai::planning`;
  also the `light_propagation_volumes` GI stage and the collision double-dispatchers.
- **Removed — the SpeedTree vegetation middleware (a *third-party* drop):** the
  `SpeedTree::` SDK is linked into every 2013 build (802–884) and is **absent from
  every 2014 build** (1916+). It is the only *statically-linked* library that comes
  or goes in the whole 0.100b→0.23h window (the renderer's DirectX *imports* narrow
  at the same pivot — see below), and it tracks the move from open, foliage-heavy
  AI-shooter levels to compact PvP maps (see `DEPENDENCY_VERSIONS.md`).
- **Added — PvP match infrastructure:** `game_world_core`, `game_statistics_handler`,
  `player_respawn_rule`, `gather_victory_items_rule` (game-mode win rules),
  `artefact_spring_core`, an animation `n_ary_tree_serializer`.
- **Reworked broadly:** `render::effect_manager`, `weapon_core`, `player` /
  `base_player`, `memory`, `vfs`, `lobby_menu`, `game_world_ui`.

This is the cancelled-S.T.A.L.K.E.R.2 → free-to-play PvP shooter transition,
captured in which functions vanished and appeared. Build flags track it too (see
`BUILD_FLAGS.md`): `vostok_sound` flipped `-Od` → LTCG and `vostok_core` went
full-LTCG → explicit `-O1` — otherwise the toolchain/flags were unchanged.

## v0.20e → v0.20f (20 Mar → 1 Apr 2014): a hotfix

Essentially nothing: +1 / −3 / ~11, 8847 identical. A point release of the same
v0.20 engine; no flag changes.

## v0.20f → v0.21d (1 → 24 Apr 2014): netcode & match statistics

A normal ~3-week delta within v0.2x (+605 / −383 / ~2566 — not a rewrite),
concentrated on multiplayer plumbing:

- **New — a network telemetry subsystem:** `network_stats_packets`,
  `network_stats_ports`, `network_stats_sent_messages` / `_received_messages` /
  `_rejected_messages`, `network_stats_packets_sequence`,
  `network_stats_orders_channel`, `udp_match_stats`, `base_game_statistics_handler`
  — packet-loss / match-stats instrumentation.
- **Reworked:** `lobby_menu`, `lobby_client`, and a physics character-controller
  swap (`old_bullet_character_controller` removed, `bullet_character_controller`
  reworked).
- **Removed:** the debug renderer (`render::debug::renderer`, `draw_lines_command`,
  `draw_triangles_command`) and `jump_logic`.

---

## The full arc (May 2013 → Apr 2014)

**2013 (v0.1):** three weeks of iteration — weapon mechanics (dispersion-skill,
reload/chambering state machines) and a sound-engine rearchitecture (RMS → codec
cooks → new propagation), with renderer streaming-texture/SpeedTree churn.
**Early 2014 (v0.20):** the pivot — the single-player AI/NPC system torn out, PvP
match infrastructure (game modes, lobby, respawn rules, statistics) added, and the
audio path moved to LTCG. **Spring 2014 (v0.2x):** netcode and match-statistics
polish on the new PvP base, plus a physics character-controller swap.

From a S.T.A.L.K.E.R.2-style AI shooter to a free-to-play PvP match game, traced
function by function.

## Third-party dependencies (version bumps)

Dependency versions are tracked separately in
[`DEPENDENCY_VERSIONS.md`](DEPENDENCY_VERSIONS.md) — read from each `survarium.exe`
via `.rdata` version strings + RTTI markers, so that report **covers v0.23h too**
despite its missing PDB. The headline for this narrative: **no third-party library
was version-bumped anywhere in the 0.100b → 0.23h window.** Scaleform GFx stays
**4.2.21**, engine zlib **1.2.3**, OpenSSL **1.0.0g**, libpng **1.5.13** and BugTrap
**1.3.3291.42976** in every build; Boost 1.48.0, STLport 5.2.1, Bullet, OPCODE 1.3,
WildMagic 4.x and libVorbis/libogg are linked throughout. (Scaleform's "4.2.21" is
exactly the marker to grep — it just never advanced to 4.2.22 inside this range.)
The two dependency-level changes both fall on the 2013→2014 pivot: the **SpeedTree**
removal above, and the renderer dropping its **Direct3D 9 helper path** — the 2013
builds import `d3dx9_43.dll` + `X3DAudio1_7.dll`, the 2014 builds are D3D11-only
(`d3dx11_43` + `D3DCOMPILER_43`). ODE, FreeImage, libtheora, MySQL and minizip
appear in the engine's `versions.txt` manifest but are **not** linked into any
shipped game exe.

### Past 0.23h: the first real version bumps (0.26g0, 2015 → 0.69d0, 2022)

Four later exes could be lifted from game-tree dumps (`survarium_full_026e0.7z`,
`survarium_full_026g0.7z`, `survarium_full_034a0.zip`, and the 2022 `Survarium.zip`;
the *many* builds in between — 0.25/0.27–0.33/0.44–0.68 — are sealed in an encrypted
`!sup` installer, see [`docs/extracting-exes.md`](../docs/extracting-exes.md)). They
show where the dependency surface finally moves:

- **OpenSSL is the library that actually gets bumped:** `1.0.0g` (18 Jan 2012)
  throughout ≤0.23h → **`1.0.1h`** (5 Jun 2014, the post-Heartbleed branch) already
  by **0.26e0** (Dec 2014), held through **0.34a0** → **`1.1.x`** by the 2022 build.
  So the "version bump" the task asked to watch for *does* happen — to OpenSSL, just
  past the 0.23 line.
- **0.26e0 / 0.26g0 (Dec 2014 / Jan 2015)** are otherwise still the 2014 engine:
  x86, STLport, Scaleform GFx **4.2.21** statically linked, zlib 1.2.3, libpng
  1.5.13 — byte-for-byte the same dep set. Only OpenSSL moved.
- **The toolchain modernizes in two steps.** A 25-build 0.25–0.31 sweep (recovered
  from a local `Survarium_archives.zip`; see `DEPENDENCY_VERSIONS.md`) pins the
  **STLport → MSVC `std::` switch to 0.28a2 (24 Apr 2015)** — 0.27d3 (17 Apr) is the
  last STLport build. By **0.34a0 (Dec 2015)** — still x86, static Scaleform 4.2.21 /
  OpenSSL 1.0.1h — the standalone zlib banner is gone too (it now rides in through
  OpenSSL's BIO). Then the **2022 build (0.69d0)** finishes it: first **x64**
  exe, **Scaleform split into `vostok_scaleform.dll`** (libpng bumped **1.5.13 →
  1.5.27**, GFx still 4.x AS2/AS3), OpenSSL to **1.1.x**, plus **Steam**
  (`steam_api64`) + **BattlEye**. The static core (Boost, Bullet, OPCODE,
  libVorbis/ogg) is unchanged throughout. No FMOD/libcurl — audio/HTTP stayed on the
  in-house + boost::asio path.

_Function-level diff covers v0.100b → v0.21d (PDB-bearing). v0.23h is string-only
(no PDB). The dependency analysis in `DEPENDENCY_VERSIONS.md` additionally spans
0.26g0 and the 2022 build; the encrypted-`!sup` era (0.27–0.68) can't be read._
