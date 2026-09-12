# v0.1.1b-build826 -> v0.1.1c-build870

Lists below: **hand-written engine** (`vostok/*`, compiler-generated excluded). Full breakdown:

| bucket | engine | generated | third-party |
| --- | ---: | ---: | ---: |
| identical | **11154** | 1383 | 10278 |
| changed | **1407** | 26 | 43 |
| new / rewritten | **277** | 222 | 479 |
| units removed | **14** | - | 3 |

## Most-changed engine functions (50 shown)

| match % | unit | function |
| ---: | --- | --- |
| 3.33 | vostok/game/sources/game_world_input.cpp | `public: virtual bool __thiscall survarium::game_world::on_mouse_move(struct vostok::input::world *, int, int, int)` |
| 3.64 | vostok/game_core/sources/double_barreled_weapon_core_hide_state.cpp | `private: class survarium::double_barreled_weapon_core_hide_state * __thiscall survarium::weapon_core_state_cook_template<class survarium::double_barreled_weapon_core_hide_state>::new_object(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)` |
| 3.64 | vostok/game_core/sources/double_barreled_weapon_core_show_state.cpp | `private: class survarium::double_barreled_weapon_core_show_state * __thiscall survarium::weapon_core_state_cook_template<class survarium::double_barreled_weapon_core_show_state>::new_object(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)` |
| 3.64 | vostok/game_core/sources/pistol_weapon_core_hide_state.cpp | `private: class survarium::pistol_weapon_core_hide_state * __thiscall survarium::weapon_core_state_cook_template<class survarium::pistol_weapon_core_hide_state>::new_object(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)` |
| 3.64 | vostok/game_core/sources/pistol_weapon_core_show_state.cpp | `private: class survarium::pistol_weapon_core_show_state * __thiscall survarium::weapon_core_state_cook_template<class survarium::pistol_weapon_core_show_state>::new_object(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)` |
| 3.64 | vostok/game_core/sources/weapon_core_hide_state.cpp | `private: class survarium::weapon_core_hide_state * __thiscall survarium::weapon_core_state_cook_template<class survarium::weapon_core_hide_state>::new_object(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)` |
| 3.64 | vostok/game_core/sources/weapon_core_show_state.cpp | `private: class survarium::weapon_core_show_state * __thiscall survarium::weapon_core_state_cook_template<class survarium::weapon_core_show_state>::new_object(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)` |
| 4.09 | vostok/sound/sources/sound_world.cpp | `public: virtual void __thiscall vostok::sound::sound_world::clear_resources(void)` |
| 4.58 | vostok/sound/sources/sound_voice_callbacks.cpp | `public: void __thiscall vostok::sound::sound_voice::on_buffer_end(void *)` |
| 5.59 | vostok/game/sources/game_world_input.cpp | `public: virtual bool __thiscall survarium::game_world::on_mouse_key_action(struct vostok::input::world *, enum vostok::input::mouse_button, enum vostok::input::enum_mouse_key_action)` |
| 8.01 | vostok/sound/sources/voice_bridge.cpp | `private: virtual void __stdcall vostok::sound::voice_bridge::OnBufferEnd(void *)` |
| 8.89 | vostok/core/sources/resources_query_result_finalization.cpp | `public: void __thiscall vostok::resources::query_result_for_cook::finish_query(enum vostok::resources::query_result_for_user::error_type_enum, enum assert_on_fail_bool)` |
| 10.33 | vostok/game/sources/player.cpp | `private: void __thiscall survarium::player::remove_alive(void)` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 15.23 | vostok/game/sources/human_npc.cpp | `private: void __thiscall survarium::human_npc::set_brain_unit(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 22.38 | vostok/sound/sources/voice_bridge.cpp | `private: virtual void __stdcall vostok::sound::voice_bridge::OnBufferStart(void *)` |
| 22.38 | vostok/sound/sources/voice_bridge.cpp | `private: virtual void __stdcall vostok::sound::voice_bridge::OnLoopEnd(void *)` |
| 24.89 | vostok/game_core/sources/weapon_core_hide_state_base.cpp | `private: virtual void __thiscall survarium::weapon_core_hide_state_base::on_animation_end_impl(bool &)` |
| 24.89 | vostok/game_core/sources/weapon_core_show_state_base.cpp | `private: virtual void __thiscall survarium::weapon_core_show_state_base::on_animation_end_impl(bool &)` |
| 25.00 | vostok/sound/sources/voice_bridge.cpp | `private: virtual void __stdcall vostok::sound::voice_bridge::OnVoiceProcessingPassStart(unsigned int)` |
| 25.17 | vostok/type_variant_inline.h | `public: virtual void __thiscall vostok::detail::concrete_type_helper<struct vostok::render::static_model_instance_user_data>::copy(class vostok::mutable_buffer, class vostok::const_buffer)` |
| 26.65 | vostok/render/engine/sources/grass_patch.cpp | `public: __thiscall vostok::render::grass_patch::grass_patch(struct vostok::collision::space_partitioning_tree *const, struct vostok::render::grass_template *, class vostok::math::float3const &, float)` |
| 27.67 | vostok/resources_resource_ptr_inline.h | `class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> __cdecl vostok::static_cast_resource_ptr<class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>, class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &)` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.57 | vostok/sound/sources/voice_bridge.cpp | `private: virtual void __stdcall vostok::sound::voice_bridge::OnVoiceProcessingPassEnd(void)` |
| 30.00 | vostok/resources_resource_ptr_inline.h | `public: class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> & __thiscall vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>::operator=(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 31.00 | vostok/sound/sources/voice_bridge.cpp | `private: virtual void __stdcall vostok::sound::voice_bridge::OnVoiceError(void *, long)` |
| 32.07 | vostok/sound/sources/voice_bridge.cpp | `private: virtual void __stdcall vostok::sound::voice_bridge::OnStreamEnd(void)` |
| 34.23 | vostok/sound/sources/voice_bridge.cpp | `public: void __thiscall vostok::sound::voice_bridge::set_low_pass_filter_params(float)` |
| 34.82 | vostok/game_core/sources/booby_trap_core.cpp | `private: virtual void __thiscall survarium::booby_trap_core::on_enter(class vostok::buffer_vector<class vostok::physics::base_physics_object *> const &)` |
| 35.21 | vostok/game/sources/object_solid_visual.cpp | `public: virtual void __thiscall survarium::object_particle_visual::load(class vostok::configs::binary_config_value const &, char const *, class boost::function<void __cdecl (class survarium::game_object_&)> &)` |
| 35.60 | vostok/game_core/sources/animation_analysis_result_cook.cpp | `public: virtual void __thiscall survarium::animation_analysis_result_cook::delete_resource(class vostok::resources::resource_base *)` |
| 35.60 | vostok/game_core/sources/items_cook.cpp | `public: virtual void __thiscall survarium::items_cook::delete_resource(class vostok::resources::resource_base *)` |
| 35.60 | vostok/game_core/sources/items_dictionary_cook.cpp | `public: virtual void __thiscall survarium::items_dictionary_cook::delete_resource(class vostok::resources::resource_base *)` |
| 35.60 | vostok/game_core/sources/player_parameters_cook.cpp | `public: virtual void __thiscall survarium::player_parameters_modifyer_cook::delete_resource(class vostok::resources::resource_base *)` |
| 35.60 | vostok/game_core/sources/weapon_ammunition_cook.cpp | `public: virtual void __thiscall survarium::weapon_ammunition_cook::delete_resource(class vostok::resources::resource_base *)` |

## Engine units in base but gone in target

- vostok/core_debug_engine.h
- vostok/game/sources/weapon_sound_events_handler_state_cook_specializations.h
- vostok/game_core/weapon_core_show_state_base.h
- vostok/sound/sound_spl.h
- vostok/sound/sources/ogg_file_contents.cpp
- vostok/sound/sources/ogg_file_contents_cook.cpp
- vostok/sound/sources/ogg_sound.cpp
- vostok/sound/sources/ogg_sound_cook.cpp
- vostok/sound/sources/ogg_source_cook.cpp
- vostok/sound/sources/sound_environment.cpp
- vostok/sound/sources/sound_environment_cook.cpp
- vostok/sound/sources/sound_scene_environment.cpp
- vostok/sound/sources/wav_encoded_sound_interface.cpp
- vostok/sound/sources/wav_encoded_sound_interface_cook.cpp
