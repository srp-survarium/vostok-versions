# v0.100b-build802 -> v0.1.1a-build816

Lists below: **hand-written engine** (`vostok/*`, compiler-generated excluded). Full breakdown:

| bucket | engine | generated | third-party |
| --- | ---: | ---: | ---: |
| identical | **12280** | 1444 | 10528 |
| changed | **393** | 14 | 12 |
| new / rewritten | **174** | 103 | 473 |
| units removed | **5** | - | 2 |

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
| 21.12 | vostok/game_core/sources/weapon_core_aimed_fire_state_base.cpp | `protected: virtual void __thiscall survarium::weapon_core_aimed_fire_state_base::initialize(void)` |
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
| 39.68 | vostok/game_core/sources/weapon_core_aimed_fire_state_base.cpp | `protected: virtual void __thiscall survarium::weapon_core_aimed_fire_state_base::finalize(void)` |
| 40.13 | vostok/game/sources/swf_input_translator.cpp | `public: bool __thiscall survarium::swf_input_translator::process_keyboard(struct vostok::input::world *, enum vostok::input::enum_keyboard, enum vostok::input::enum_keyboard_action, struct survarium::flash_movie *, unsigned int)` |
| 40.60 | vostok/game_core/sources/weapon_core_aimed_fire_state_base.cpp | `private: virtual void __thiscall survarium::weapon_core_aimed_fire_state_base::on_animation_end_impl(bool &)` |
| 40.60 | vostok/game_core/sources/weapon_core_fire_state_base.cpp | `protected: virtual void __thiscall survarium::weapon_core_fire_state_base::on_animation_end_impl(bool &)` |
| 48.57 | vostok/game_core/sources/weapon_core_idle_state_base.cpp | `private: virtual void __thiscall survarium::weapon_core_idle_state_base::finalize(void)` |
| 51.73 | vostok/game_core/sources/weapon_core_fire_state_base.cpp | `protected: virtual void __thiscall survarium::weapon_core_fire_state_base::finalize(void)` |
| 59.61 | vostok/game_core/sources/weapon_core_shotgun_reload_state.cpp | `private: void __thiscall survarium::weapon_core_shotgun_reload_state::initialize_logic(class survarium::weapon_core_shotgun_reload_base_substate *, class survarium::weapon_core_shotgun_reload_base_substate *, class survarium::weapon_core_shotgun_reload_base_substate *)` |
| 59.90 | vostok/game_core/sources/weapon_core.cpp | `public: virtual void __thiscall survarium::weapon_core::instant_aim_start(void)` |
| 60.00 | vostok/game_core/sources/weapon_core_hide_state_base.cpp | `protected: virtual void __thiscall survarium::weapon_core_hide_state_base::finalize(void)` |
| 60.00 | vostok/game_core/sources/weapon_core_show_state_base.cpp | `protected: virtual void __thiscall survarium::weapon_core_show_state_base::finalize(void)` |
| 65.95 | vostok/game/sources/weapon.cpp | `private: virtual void __thiscall survarium::weapon::deactivate(void)` |
| 65.96 | vostok/game_core/sources/weapon_core_shotgun_reload_finish_substate.cpp | `private: enum vostok::animation::callback_return_type_enum __thiscall survarium::weapon_core_shotgun_reload_finish_substate::on_animation_end(struct vostok::animation::animation_callback_params &)` |
| 65.98 | vostok/game_core/sources/weapon_core_fire_state_base.cpp | `protected: virtual void __thiscall survarium::weapon_core_fire_state_base::initialize(void)` |
| 67.05 | vostok/game_core/game_net_defines.h | `public: __thiscall survarium::player_profile::player_profile(void)` |
| 69.82 | vostok/game/sources/lobby_menu_ui.cpp | `public: virtual void __thiscall survarium::relocate_item_func::call(struct survarium::flash_function_handler_params &)` |
| 70.00 | vostok/game_core/sources/weapon_core_hide_state_base.cpp | `protected: virtual void __thiscall survarium::weapon_core_hide_state_base::initialize(void)` |
| 70.00 | vostok/game_core/sources/weapon_core_show_state_base.cpp | `protected: virtual void __thiscall survarium::weapon_core_show_state_base::initialize(void)` |
| 70.89 | vostok/sound/sources/single_sound_cook.cpp | `private: void __thiscall vostok::sound::single_sound_cook::on_sub_resources_loaded(class vostok::resources::queries_result &)` |
| 70.92 | vostok/game_core/sources/weapon_core.cpp | `public: void __thiscall survarium::weapon_core::instant_idle_start(void)` |
| 71.11 | vostok/game_core/sources/weapon_core.cpp | `public: virtual void __thiscall survarium::weapon_core::instant_aim_end(void)` |
| 73.21 | vostok/game_core/sources/weapon_core_shotgun_reload_state.cpp | `private: bool __thiscall survarium::weapon_core_shotgun_reload_state::finish_reload_predicate(void) const` |
| 76.91 | vostok/render/engine/sources/lights_db.cpp | `vostok::render::fill_light` |
| 80.30 | vostok/render/engine/sources/register_samplers.cpp | `void __cdecl vostok::render::register_samplers(void)` |
| 80.36 | vostok/network/sources/match_client.cpp | `private: void __thiscall vostok::network::match_client::on_packet_received_impl(unsigned char, class vostok::network_core::packet_reader &)` |
| 80.70 | vostok/game_core/sources/weapon_core.cpp | `private: void __thiscall survarium::weapon_core::initialize_weapon_logic(class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &)` |

## Engine units in base but gone in target

- vostok/core_debug_engine.h
- vostok/detail_noncopyable.h
- vostok/network/sources/functor_response.h
- vostok/sound/sources/sound_rms.cpp
- vostok/sound/sources/sound_rms_cook.cpp
