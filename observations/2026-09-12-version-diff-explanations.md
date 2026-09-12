# Evidence-based explanation of every version diff

This document explains every consecutive binary comparison in the configured
PDB chain. The explanations start with changed, added, and deleted demangled
function names. Source-file checksums, shader deltas, build flags, and public
update notes are supporting evidence. A public note is never used to turn an
unrelated symbol into a claimed implementation.

The binary labels and public update names are close but not proven identical.
Their dates differ by one or two days in several cases. Build 884 also crosses
the public 0.11d update before the 0.11e installer hotfix. The conclusions below
therefore describe the binary intervals first and mention public notes only as
corroboration.

## How the evidence was read

The frozen [chain report](../reports/2026-06/CHAIN_REPORT.md) compares
hand-written `vostok/*` functions, deduplicated by demangled name. `Added` and
`deleted` mean that a name occurs at only one endpoint. `Changed` means that the
same name was matched below 100%. Renaming, identical-code folding, template
instantiation, source movement, and imperfect object alignment can move a
function between these buckets without adding or removing behavior.

The [per-build reports](../reports/2026-06/README.md) group added and deleted
names by owning class or namespace. Their labels such as `NEW`, `REMOVED`, and
`REWORKED` describe symbol-set changes, not independently proven features. The
June snapshot also predates the workflow fixes that now record effective symbol
alignment, so the exact old counts are evidence with known limits. This matters
most for the ten-month 884 -> 1916 comparison.

The newer [source-file checksum report](../reports/2026-09-12-source-files-expanded/README.md)
contains five locally verified PDBs. Because builds 826, 884, and 1923 were not
available for that run, its four file-level comparisons combine some of the
seven consecutive function intervals:

| File-checksum comparison | Consecutive function intervals inside it |
| --- | --- |
| 802 -> 816 | 802 -> 816 |
| 816 -> 870 | 816 -> 826 and 826 -> 870 |
| 870 -> 1916 | 870 -> 884 and 884 -> 1916 |
| 1916 -> 2010 | 1916 -> 1923 and 1923 -> 2010 |

## Overview

| Binary interval | Added | Deleted | Changed | Identical | Main reading from symbols |
| --- | ---: | ---: | ---: | ---: | --- |
| 802 -> 816 | 88 | 56 | 400 | 11,060 | Weapon state machine and dispersion work; smaller rendering and sound changes |
| 816 -> 826 | 19 | 26 | 254 | 11,268 | Renderer/shader interfaces and console-command filtering |
| 826 -> 870 | 142 | 160 | 1,465 | 9,916 | Sound rearchitecture plus broad gameplay, UI, and rendering work |
| 870 -> 884 | 25 | 38 | 473 | 11,012 | Resource-query layout churn, shadows/culling, and medkit lifecycle changes |
| 884 -> 1916 | 4,163 | 6,812 | 4,526 | 172 | Ten months of structural replacement across most of the client |
| 1916 -> 1923 | 1 | 3 | 11 | 8,847 | Extremely small maintenance build |
| 1923 -> 2010 | 605 | 383 | 2,566 | 5,910 | Network telemetry, match statistics, lobby/UI, movement physics, and rendering work |

## 802 -> 816: weapon behavior was rebuilt around explicit states

The strongest evidence is the `survarium::weapon_core` symbol set: **44 functions
were added and 20 deleted**. New predicates include `aimed_fire_pred`,
`chamber_a_round_pred`, `chamber_a_round_on_reload_break_pred`, `can_reload`,
`can_jump`, `can_sprint`, and `ready_to_fire`. Existing implementations such as
`weapon_core::tick`, `weapon_core_aimed_fire_state_base::initialize`,
`weapon_core_fire_state_base::finalize`, and the shotgun reload substates also
changed substantially. This is evidence of a state-machine redesign rather than
a few weapon constants changing.

Accuracy work is visible independently. The new
`character_dispersion_skill_influence` scope supplies a constructor and `load`,
while `character_dispersion_calculator` gains `get_skill_coef` and
`set_character_dispersion_skill_influence`; its `tick` implementation changes.
`damage_model::reset` changes signature and `damage_model::hit_body_part` changes
code. These symbols directly support work on skill-dependent accuracy and damage.
The public [0.11a notes](../sources/fandom-updates/2026-09-12/pages/0.11a.wiki)
describe recoil, hip-fire accuracy, weapon-skill influence, shotgun behavior,
and damage-model changes, which is a close thematic match.

There is a smaller rendering thread. `weapon` gains `add_weapon_fire_light` and
`remove_weapon_fire_light`, matching the public firing-light change. Shader
evidence records five code-changing shader names, led by `gbuffer_pass.ps`, with
changes to environment-probe lighting, terrain G-buffer, post-processing, and
God rays. The renderer also gains several streaming-texture and SpeedTree-related
types. Those types disappear in the next same-day build, so they are better read
as an in-flight renderer refactor than as durable features.

Finally, the `sound_rms`, `sound_rms_cook`, and `sound_rms_pinned` scopes and their
source units disappear. That is direct evidence that an RMS resource path was
removed, although the symbols alone do not establish what replaced it.

The PDB checksums independently find **44 changed engine sources and 29 changed
headers**, with only two target-only and two base-only records. That shape agrees
with concentrated edits to existing weapon code rather than a wholesale source
tree replacement. Full symbol evidence is in the
[816 build report](../reports/2026-06/builds/v0.1.1a-build816.md) and the
[directional diff](../reports/2026-06/diffs/v0.100b-build802__v0.1.1a-build816/summary.md).

## 816 -> 826: a same-day renderer drop and command filtering

This is a smaller function diff, but its shader change is disproportionate. The
shader evidence records **23 code-changing names**, while the permutation count
rises from 3,408 to 4,569. `gbuffer_pass.ps` doubles its permutations, and the
forward-lighting family changes together. In the function symbols,
`render::backend`, `shader_constant_buffer`, and `constants_handler<0/1>` gain and
lose typed constant-setting overloads. That combination points to a coordinated
lighting/material and shader-binding change.

Several renderer types introduced at 816 disappear immediately:
`streaming_ready_texture`, `requested_streamable_texture`,
`streamable_texture_info`, `speedtree_data`, `animated_model_instance`, and
`render_target_instance`. Because both binaries carry the same catalog date,
this is most safely described as code being folded, renamed, or backed out during
a same-day integration pass. The symbols do not prove that texture streaming or
SpeedTree support vanished from the product.

The non-rendering additions are unusually specific. `console_commands::execute`,
`execute_console_commands`, and `load` all gain an extra boolean parameter while
retaining `execution_filter`; `survarium::game::load_cc_script`,
`load_config_query`, and `on_config_loaded` change in parallel. This directly
supports a new command/config filtering path and aligns with the public
[0.11b note](../sources/fandom-updates/2026-09-12/pages/0.11b.wiki) that internal
console commands were prohibited. `weapon_core` also gains `reload_break_pred`
and `idle_AE_or_chamber_a_round_break_pred`, a focused continuation of the prior
weapon-state work.

The evidence supports renderer/shader integration and command filtering. The
public level addition is content and need not leave new client function names.
See the [826 build report](../reports/2026-06/builds/v0.1.1b-build826.md) and
[directional diff](../reports/2026-06/diffs/v0.1.1a-build816__v0.1.1b-build826/summary.md).

## 826 -> 870: HDR sound landed with broad gameplay and rendering changes

This is the largest May 2013 function interval: **142 names added, 160 deleted,
and 1,465 changed**. The sound symbols show a structural replacement. Removed
scopes include `ogg_file_contents_cook`, `ogg_sound_cook`, `ogg_source_cook`,
`wav_encoded_sound_interface_cook`, `sound_environment_cook`, `ogg_sound`, and
`effect_cross_fader`. At the same time:

- `sound_scene` gains `calculate_hdr_audio_frame`, `calculate_channel_matrix`,
  `x3daudio_calculate`, `process_fade`, and listener notification methods;
- `new_sound_propagator` changes its voice attachment, detachment, SPL, RMS, and
  timing interfaces;
- `sound_voice` changes buffer refill, muting, filtering, callback, and quality
  handling;
- allocator specializations change from 28/108/136-byte objects to
  32/84/96-byte objects, consistent with changed sound-object layouts.

That is direct evidence for the public [0.11c notes](../sources/fandom-updates/2026-09-12/pages/0.11c.wiki)
about HDR audio and sound-direction fixes. The file checksums across 816 -> 870
find **45 changed sound files, six sound files present only at 870, and twenty
sound files present only at 816**. Since that checksum interval also contains
build 826, the exact file changes cannot be assigned between the two steps, but
the consecutive symbol diff locates the sound rearchitecture at 826 -> 870.

The gameplay symbols likewise match several independent areas from the notes:
`booby_trap_set_core::load`, trap state/timer/defuse functions, and network trap
messages changed; `player_logic_stand_state` and `player_logic_crouch_state`
animation selection changed; `damage_model`, hit processing, and
`game_world_ui::on_hit_from_pos` changed; reload-break and shotgun reload
functions changed; and the UI gains or changes player-list, quick-slot, ammo,
health, victory-point, and match-state methods.

Rendering changed at the same time. `stage_ambient_occlusion::execute`, shader
macro registration, and shader-cache interfaces changed. The shader registry
shrinks from 81 to 68 slots; six shader names are added and two removed. Motion
blur splits into low/medium/high variants and `ssao_accumulation_hq.ps` appears.
These symbols and shader deltas support HDAO/quality-tier and graphics work,
although they do not map each internal name to a particular public option.

The broad source count is therefore expected rather than a checksum accident.
Across the combined 816 -> 870 file interval, 222 of the 258 changed engine files
sit in `game_core` (71), `render` (58), `game` (48), and `sound` (45), while all
1,921 recorded third-party files remain identical. See the
[870 build report](../reports/2026-06/builds/v0.1.1c-build870.md) and
[directional diff](../reports/2026-06/diffs/v0.1.1b-build826__v0.1.1c-build870/summary.md).

## 870 -> 884: resource layouts moved while shadows and medkits changed

Most added/deleted names here are template-layout evidence. Resource-query
intrusive lists move among offsets 600, 608, and 616; a double-linked query list
moves from offsets 616/612 to 624/620. `resources_manager::create_resources`,
`allocate_functionality::allocate_final_resources`, and
`hdd_manager::grab_sorted_queries` acquire the corresponding new template
specializations. Many apparent additions and deletions therefore express a
changed `query_result` layout rather than separate new behavior.

The durable behavioral clusters are smaller:

- `stage_shadow_direct::execute_cascade` and `prepare_models` change signatures,
  `sun_cascade` disappears, and renderer/portal-sector culling functions change;
- `medkit` gains `on_player_death`, `holder_assigned`, `holder_removed`, and
  `remove`, while several methods move from protected to private signatures;
- `fs_new::virtual_path_string` gains a constructor specialization;
- `network_client::close_current_match`, post-processing, render options, and
  collision-contact code change.

Shader evidence calls this a settling pass: 259 of 265 shader names are
byte-identical, two change only their permutation matrices, and four change code.
That supports a focused renderer/resource maintenance build rather than another
broad graphics rewrite.

Build 884 is dated May 28, while the public [0.11d](../sources/fandom-updates/2026-09-12/pages/0.11d.wiki)
and [0.11e](../sources/fandom-updates/2026-09-12/pages/0.11e.wiki) pages are dated
May 30. The interval may include work associated with 0.11d, whereas 0.11e is
described only as an installer repair. The executable symbols cannot establish
that mapping, and the observed client changes should not be attributed to the
installer hotfix. See the [884 build report](../reports/2026-06/builds/v0.1.1e-build884.md)
and [directional diff](../reports/2026-06/diffs/v0.1.1c-build870__v0.1.1e-build884/summary.md).

## 884 -> 1916: a ten-month structural replacement

This interval crosses the entire 0.12-0.19 gap and the early 0.20 updates. The
preserved name comparison finds only **172 identical functions**, against 4,163
added, 6,812 deleted, and 4,526 changed names. The old alignment metadata cannot
prove that every exact bucket assignment is correct across such a large gap, but
the named clusters and the overall scale establish a broad replacement.

One clear deletion is the shipped client-side AI/NPC framework:
`survarium::human_npc` loses 64 functions, `ai::brain_unit` loses 47,
`ai::ai_world` loses 42, and planning/path-selection scopes and units disappear.
This proves that those implementations are absent from the later executable. It
does **not** prove a transition from a single-player product to PvP: the 2013
public notes already describe teams, matches, spawning, and networked players.
The safe explanation is that legacy, experimental, server-side, or unused AI
code was removed from this client during the ten-month restructuring.

New match architecture is visible independently. `game_world_core` adds 41
functions. `game_statistics_handler` appears with 18. `artefact_spring_core`,
`gather_victory_items_rule`, and `player_respawn_rule` add explicit match-event,
HUD-state, serialization, winner-selection, item-spawner, and player-spawn
methods. `buffer_writer` and many game/network serialization interfaces appear
or change. These names support a more formal rule-driven multiplayer client.

The renderer also changes architecture. `stage_light_propagation_volumes` loses
25 functions and `radiance_volume` loses 19, removing the old LPV global-
illumination path. SpeedTree link markers and associated renderer scopes disappear.
Effect management, shader compilation/caching, ambient lighting, decals,
post-processing, particles, water, and texture handling all show large symbol
changes. The PDB checksum comparison across 870 -> 1916 records 1,445 changed,
544 target-only, and 237 base-only engine files; because build 884 is missing
from that checksum run, those file counts combine the small 870 -> 884 step with
this large interval.

Core infrastructure changes too: resource/query APIs, VFS, memory allocation,
animation serialization, collision geometry, lobby/menu code, player state, and
weapon code all have large scope-level deltas. The build-flags report also places
changes to core and sound optimization visibility at this boundary. There is no
single release-note explanation for this diff; it is accumulated development
across roughly ten months and dozens of public updates. See the
[1916 build report](../reports/2026-06/builds/v0.20e-build1916.md) and
[directional diff](../reports/2026-06/diffs/v0.1.1e-build884__v0.20e-build1916/summary.md).

## 1916 -> 1923: a true maintenance-sized binary change

This interval has **8,847 identical names** and only one added, three deleted,
and eleven changed. The directional object summary identifies just two cleanly
matched changed engine functions, both at 99.97% similarity:
`network_world::dispatch_callbacks` and
`stage_shadow_direct::prepare_visibile_objects`. The other name-set differences
are a renderer sort predicate, a shader-buffer `fixed_vector` destructor, a bind
template instance, and several zero-match symbols that are consistent with
folding/alignment noise.

The public [0.20f notes](../sources/fandom-updates/2026-09-12/pages/0.20f.wiki)
describe synchronization improvements for high ping, low-end computers, and
heavy player activity. The near-identical change to
`network_world::dispatch_callbacks` is compatible with a small synchronization
fix, but the binary evidence is too thin to derive all three claims or their
mechanism. What the symbols firmly establish is that 0.20f was a very small
client maintenance build with no build-flag change.

See the [1923 build report](../reports/2026-06/builds/v0.20f-build1923.md) and
[directional diff](../reports/2026-06/diffs/v0.20e-build1916__v0.20f-build1923/summary.md).

## 1923 -> 2010: network instrumentation and match systems expanded

This interval spans the public 0.21a, 0.21b, 0.21c, and 0.21d updates, not only
the final 0.21d hotfix. Network instrumentation is the clearest new subsystem.
New scopes include `network_stats_packets`, `network_stats_ports`,
`network_stats_sent_messages`, `network_stats_received_messages`,
`network_stats_rejected_messages`, `network_stats_packets_sequence`, and
`network_stats_orders_channel`. `network_core::udp_match_stats` gains 22 methods,
including registration of acknowledged, unacknowledged, duplicated, discarded,
ordered, skipped, too-old, and too-new packets/messages. That is direct evidence
for detailed synchronization telemetry and aligns with the public
[0.21a notes](../sources/fandom-updates/2026-09-12/pages/0.21a.wiki).

Match statistics are refactored rather than simply added. A new
`base_game_statistics_handler` receives 19 lifecycle, serialization, score,
damage, kill, weapon-fire, medkit, and victory-item methods while
`game_statistics_handler` loses the corresponding implementations and keeps a
smaller derived role. `lobby_menu` gains `show_match_statistic`,
`fill_match_statistic`, `fill_player_statistic`, quest-message preparation, and
squad display changes; `lobby_client` changes match-stat and price-item queries.
This supports the public match-results, rewards/tasks, lobby, and squad work.

Movement physics is another independent cluster. The 22-function
`old_bullet_character_controller` scope disappears. The surviving
`bullet_character_controller` changes eleven methods in and ten out, adding
explicit slope, ceiling, sliding, grounding, and step-down handling.
`jump_logic` loses ten functions, while player jump/landing/sprint code changes.
Those names establish a controller redesign, although they do not identify one
specific public bug fix.

The remaining breadth includes weapons and inventory, animations and bone
matrices, rendering and texture pools, quests, artefacts, chat/filtering, and UI.
The internal render-debug `renderer`, `draw_lines_command`, and
`draw_triangles_command` scopes disappear. These are meaningful secondary
changes, but the network/statistics and controller clusters provide the strongest
explanation for the interval.

The 1916 -> 2010 file-checksum comparison finds 295 changed source files and 243
changed headers. It includes the tiny 1916 -> 1923 step, so the preserved
consecutive function evidence strongly suggests that almost all of that file
churn belongs after build 1923. The exact allocation still requires the missing
1923 PDB checksum table. See the [2010 build report](../reports/2026-06/builds/v0.21d-build2010.md)
and [directional diff](../reports/2026-06/diffs/v0.20f-build1923__v0.21d-build2010/summary.md).

## What remains unknown

These explanations identify the strongest subsystem-level causes visible in the
binaries. They do not recover changed source lines, guarantee that every added
name is new behavior, or assign every public patch-note bullet to one function.
The next material improvement is to recover builds 826, 884, and 1923 again and
produce consecutive PDB source-checksum tables. That would split the three
currently aggregated file intervals while leaving the seven function-level
explanations above intact.
