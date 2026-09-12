# v0.1.1a-build816 -> v0.100b-build802

Lists below: **hand-written engine** (`vostok/*`, compiler-generated excluded). Full breakdown:

| bucket | engine | generated | third-party |
| --- | ---: | ---: | ---: |
| identical | **12280** | 1444 | 10528 |
| changed | **394** | 14 | 12 |
| new / rewritten | **136** | 168 | 396 |
| units removed | **5** | - | 4 |

## Most-changed engine functions (50 shown)

| match % | unit | function |
| ---: | --- | --- |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 20.29 | vostok/game_core/sources/weapon_user_animations_selector.cpp | `private: bool __thiscall survarium::weapon_user_animations_selector::jump_predicate(void) const` |
| 27.87 | vostok/game_core/sources/weapon_core.cpp | `public: virtual void __thiscall survarium::weapon_core::tick(void)` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 41.51 | vostok/game_core/sources/weapon_core_shotgun_reload_state.cpp | `private: void __thiscall survarium::weapon_core_shotgun_reload_state::initialize_logic(class survarium::weapon_core_shotgun_reload_base_substate *, class survarium::weapon_core_shotgun_reload_base_substate *, class survarium::weapon_core_shotgun_reload_base_substate *)` |
| 43.81 | vostok/game_core/sources/weapon_core_shotgun_reload_finish_substate.cpp | `protected: virtual void __thiscall survarium::weapon_core_shotgun_reload_finish_substate::finalize(void)` |
| 46.53 | vostok/game_core/sources/weapon_core.cpp | `public: virtual void __thiscall survarium::weapon_core::instant_aim_start(void)` |
| 47.13 | vostok/game/sources/swf_input_translator.cpp | `public: bool __thiscall survarium::swf_input_translator::process_keyboard(struct vostok::input::world *, enum vostok::input::enum_keyboard, enum vostok::input::enum_keyboard_action, struct survarium::flash_movie *, unsigned int)` |
| 48.39 | vostok/game_core/sources/weapon_core_shotgun_reload_finish_substate.cpp | `private: enum vostok::animation::callback_return_type_enum __thiscall survarium::weapon_core_shotgun_reload_finish_substate::on_animation_end(struct vostok::animation::animation_callback_params &)` |
| 49.52 | vostok/game/sources/weapon.cpp | `private: virtual void __thiscall survarium::weapon::deactivate(void)` |
| 53.48 | vostok/game_core/sources/weapon_core_aimed_fire_state_base.cpp | `protected: virtual void __thiscall survarium::weapon_core_aimed_fire_state_base::initialize(void)` |
| 58.18 | vostok/game_core/sources/weapon_core_aimed_fire_state_base.cpp | `protected: virtual void __thiscall survarium::weapon_core_aimed_fire_state_base::finalize(void)` |
| 64.00 | vostok/game_core/sources/weapon_core.cpp | `public: void __thiscall survarium::weapon_core::instant_idle_start(void)` |
| 64.00 | vostok/game_core/sources/weapon_core_idle_state_base.cpp | `private: virtual void __thiscall survarium::weapon_core_idle_state_base::finalize(void)` |
| 64.70 | vostok/game/sources/lobby_menu_ui.cpp | `public: virtual void __thiscall survarium::relocate_item_func::call(struct survarium::flash_function_handler_params &)` |
| 65.52 | vostok/game_core/sources/weapon_core_fire_state_base.cpp | `protected: virtual void __thiscall survarium::weapon_core_fire_state_base::finalize(void)` |
| 66.53 | vostok/game_core/sources/weapon_core_fire_state_base.cpp | `protected: virtual void __thiscall survarium::weapon_core_fire_state_base::initialize(void)` |
| 70.00 | vostok/game_core/sources/weapon_core_hide_state_base.cpp | `protected: virtual void __thiscall survarium::weapon_core_hide_state_base::finalize(void)` |
| 70.00 | vostok/game_core/sources/weapon_core_show_state_base.cpp | `protected: virtual void __thiscall survarium::weapon_core_show_state_base::finalize(void)` |
| 71.87 | vostok/sound/sources/single_sound_cook.cpp | `private: void __thiscall vostok::sound::single_sound_cook::on_sub_resources_loaded(class vostok::resources::queries_result &)` |
| 75.00 | vostok/game_core/game_net_defines.h | `public: __thiscall survarium::player_profile::player_profile(void)` |
| 75.77 | vostok/render/engine/sources/lights_db.cpp | `vostok::render::fill_light` |
| 76.00 | vostok/game_core/sources/weapon_core_hide_state_base.cpp | `protected: virtual void __thiscall survarium::weapon_core_hide_state_base::initialize(void)` |
| 76.00 | vostok/game_core/sources/weapon_core_show_state_base.cpp | `protected: virtual void __thiscall survarium::weapon_core_show_state_base::initialize(void)` |
| 76.09 | vostok/network/sources/match_client.cpp | `private: void __thiscall vostok::network::match_client::on_packet_received_impl(unsigned char, class vostok::network_core::packet_reader &)` |
| 76.36 | vostok/game_core/sources/weapon_core.cpp | `public: virtual void __thiscall survarium::weapon_core::instant_aim_end(void)` |
| 77.94 | vostok/game_core/sources/weapon_core_shotgun_reload_state.cpp | `private: bool __thiscall survarium::weapon_core_shotgun_reload_state::finish_reload_predicate(void) const` |
| 79.09 | vostok/render/engine/sources/register_samplers.cpp | `void __cdecl vostok::render::register_samplers(void)` |

## Engine units in base but gone in target

- vostok/ai/fsm_state.h
- vostok/core/engine.h
- vostok/game_core/sources/character_dispersion_skill_influence.cpp
- vostok/network/sources/functor_order.h
- vostok/render/facade/base_command.h
