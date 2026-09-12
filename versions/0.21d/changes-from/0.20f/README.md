# 0.20f → 0.21d: network instrumentation and match systems expanded

Binary builds **1923 → 2010**. Catalog dates: 2014-04-01 → 2014-04-24.

Function accounting: **605 added, 383 deleted, 2566 changed, and 5910 identical** demangled names.

This interval spans the public 0.21a, 0.21b, 0.21c, and 0.21d updates, not only
the final 0.21d hotfix. Network instrumentation is the clearest new subsystem.
New scopes include `network_stats_packets`, `network_stats_ports`,
`network_stats_sent_messages`, `network_stats_received_messages`,
`network_stats_rejected_messages`, `network_stats_packets_sequence`, and
`network_stats_orders_channel`. `network_core::udp_match_stats` gains 22 methods,
including registration of acknowledged, unacknowledged, duplicated, discarded,
ordered, skipped, too-old, and too-new packets/messages. That is direct evidence
for detailed synchronization telemetry and aligns with the public
[0.21a notes](../../../0.21a/update-note.wiki).

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
changed headers. It includes the tiny 1916 -> 1923 step, so the measured
consecutive function evidence strongly suggests that almost all of that file
churn belongs after build 1923. The exact allocation still requires the missing
1923 PDB checksum table. See the [2010 build report](symbols-by-scope.md)
and [directional diff](object-summary.md).

## Canonical evidence

- [Complete function accounting](functions.json)
- [Object-level summary](object-summary.md) and [machine-readable form](object-summary.json)
- [Added and deleted symbols grouped by scope](symbols-by-scope.md)
