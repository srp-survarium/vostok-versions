# v0.10b-build802 → v0.11a-build816: source-file checksums

Changed/unchanged compare checksums at the same normalized path. Added/removed mean present in only one PDB's selected file records. They do not prove repository creation/deletion. Unknown means absent checksums or incompatible algorithms.

Source contents are not embedded here; changed hashes cannot identify changed lines or distinguish comments/line endings from functional edits.

| Scope | Changed | Unchanged | Added | Removed | Unknown |
| --- | ---: | ---: | ---: | ---: | ---: |
| all | 73 | 4848 | 2 | 2 | 0 |
| engine | 73 | 2927 | 2 | 2 | 0 |
| engine_source | 44 | 1068 | 1 | 2 | 0 |
| engine_header | 29 | 1859 | 1 | 0 | 0 |
| engine_other | 0 | 0 | 0 | 0 | 0 |
| third_party | 0 | 1921 | 0 | 0 | 0 |

[Complete per-file records and both hashes](files.tsv). Each status also has an exhaustive plain-text path list in this directory.

## Changed engine files

- `vostok/animation/animation_player.h`
- `vostok/engine/sources/engine_entry_point.cpp`
- `vostok/game/sources/key_binder.cpp`
- `vostok/game/sources/lobby_client.h`
- `vostok/game/sources/lobby_menu.cpp`
- `vostok/game/sources/lobby_menu_ui.cpp`
- `vostok/game/sources/network_client.cpp`
- `vostok/game/sources/player.cpp`
- `vostok/game/sources/player_cook.cpp`
- `vostok/game/sources/player_tick.cpp`
- `vostok/game/sources/swf_input_translator.cpp`
- `vostok/game/sources/swf_input_translator.h`
- `vostok/game/sources/weapon.cpp`
- `vostok/game/sources/weapon.h`
- `vostok/game_core/base_player.h`
- `vostok/game_core/character_dispersion_calculator.h`
- `vostok/game_core/damage_model.h`
- `vostok/game_core/dispersion_calculator.h`
- `vostok/game_core/game_net_defines.h`
- `vostok/game_core/player_input.h`
- `vostok/game_core/player_input_inline.h`
- `vostok/game_core/respawn_point.h`
- `vostok/game_core/sources/base_player.cpp`
- `vostok/game_core/sources/character_dispersion_calculator.cpp`
- `vostok/game_core/sources/damage_model.cpp`
- `vostok/game_core/sources/dispersion_calculator.cpp`
- `vostok/game_core/sources/player_logic_sprint_state.cpp`
- `vostok/game_core/sources/respawn_point.cpp`
- `vostok/game_core/sources/weapon_core.cpp`
- `vostok/game_core/sources/weapon_core_aimed_fire_state_base.cpp`
- `vostok/game_core/sources/weapon_core_aimed_state_base.cpp`
- `vostok/game_core/sources/weapon_core_base_state.cpp`
- `vostok/game_core/sources/weapon_core_chamber_a_round_aimed_state_base.cpp`
- `vostok/game_core/sources/weapon_core_chamber_a_round_state_base.cpp`
- `vostok/game_core/sources/weapon_core_fire_state_base.cpp`
- `vostok/game_core/sources/weapon_core_hide_state_base.cpp`
- `vostok/game_core/sources/weapon_core_idle_state_base.cpp`
- `vostok/game_core/sources/weapon_core_inactive_state.h`
- `vostok/game_core/sources/weapon_core_reload_state_base.cpp`
- `vostok/game_core/sources/weapon_core_shotgun_reload_finish_substate.cpp`
- `vostok/game_core/sources/weapon_core_shotgun_reload_state.cpp`
- `vostok/game_core/sources/weapon_core_show_state_base.cpp`
- `vostok/game_core/sources/weapon_dispersion_calculator.cpp`
- `vostok/game_core/sources/weapon_user_animations_selector.cpp`
- `vostok/game_core/weapon_core.h`
- `vostok/game_core/weapon_core_aimed_fire_state_base.h`
- `vostok/game_core/weapon_core_animation_end_aware_state.h`
- `vostok/game_core/weapon_core_base_state.h`
- `vostok/game_core/weapon_core_shotgun_reload_state.h`
- `vostok/game_core/weapon_user_animations_selector.h`
- `vostok/input/keyboard.h`
- `vostok/input/sources/direct_input_include.h`
- `vostok/input/sources/receiver_keyboard.cpp`
- `vostok/input/sources/receiver_keyboard.h`
- `vostok/input/sources/receiver_keyboard_win.cpp`
- `vostok/login_server/constants.h`
- `vostok/login_server/login_structures.h`
- `vostok/network/sources/login_client_impl.h`
- `vostok/network/sources/login_client_impl_sign_in.cpp`
- `vostok/network/sources/login_client_impl_sign_up.cpp`
- `vostok/network/sources/match_client.cpp`
- `vostok/render/core/dx11/sources/backend.cpp`
- `vostok/render/engine/sources/lights_db.cpp`
- `vostok/render/engine/sources/register_samplers.cpp`
- `vostok/render/engine/sources/stage_lights.cpp`
- `vostok/sound/single_sound.h`
- `vostok/sound/sound_propagator_emitter.h`
- `vostok/sound/sources/composite_sound.h`
- `vostok/sound/sources/single_sound.cpp`
- `vostok/sound/sources/single_sound_cook.cpp`
- `vostok/sound/sources/sound_world.cpp`
- `vostok/vfs/sources/fat_header.h`
- `vostok/vfs/sources/virtual_file_system.cpp`

## Changed third-party files

None.
