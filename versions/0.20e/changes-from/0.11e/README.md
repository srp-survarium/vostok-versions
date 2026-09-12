# 0.11e → 0.20e: a ten-month structural replacement

Binary builds **884 → 1916**. Catalog dates: 2013-05-28 → 2014-03-20.

Function accounting: **4163 added, 6812 deleted, 4526 changed, and 172 identical** demangled names.

This interval crosses the entire 0.12-0.19 gap and the early 0.20 updates. The
function-name comparison finds only **172 identical functions**, against 4,163
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
[1916 build report](symbols-by-scope.md) and
[directional diff](object-summary.md).

## Canonical evidence

- [Complete function accounting](functions.json)
- [Object-level summary](object-summary.md) and [machine-readable form](object-summary.json)
- [Added and deleted symbols grouped by scope](symbols-by-scope.md)
