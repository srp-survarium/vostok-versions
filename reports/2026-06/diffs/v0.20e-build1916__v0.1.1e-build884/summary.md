# v0.20e-build1916 -> v0.1.1e-build884

Lists below: **hand-written engine** (`vostok/*`, compiler-generated excluded). Full breakdown:

| bucket | engine | generated | third-party |
| --- | ---: | ---: | ---: |
| identical | **295** | 142 | 724 |
| changed | **4040** | 485 | 2478 |
| new / rewritten | **8484** | 966 | 7674 |
| units removed | **354** | - | 29 |

## Most-changed engine functions (50 shown)

| match % | unit | function |
| ---: | --- | --- |
| 0.17 | vostok/game_core/sources/breath_vibration_calculator.cpp | `public: __thiscall survarium::breath_vibration_calculator::~breath_vibration_calculator(void)` |
| 0.19 | vostok/core/sources/game_resman_release.cpp | `public: bool __thiscall vostok::resources::releasing_functionality::release_all_resources(void)` |
| 0.20 | vostok/game_core/sources/game_material_manager_cook.cpp | `private: void __thiscall survarium::game_material_manager_cook::create_game_material_pairs(class vostok::resources::query_result_for_cook &, class survarium::game_material_manager *const, class vostok::configs::binary_config_value const &)` |
| 0.28 | vostok/core/sources/resources_fs_task_mount.cpp | `public: virtual void __thiscall vostok::resources::fs_task_mount::call_user_callback(void)` |
| 0.35 | vostok/game/sources/weapon_sound_effect.cpp | `public: enum vostok::animation::callback_return_type_enum __thiscall survarium::weapon_sound_effect::on_sound_event(struct vostok::animation::animation_callback_params &)` |
| 0.57 | vostok/particle/sources/particle_actions.cpp | `public: virtual unsigned int __thiscall vostok::particle::particle_action_color_over_lifetime::save_binary(class vostok::mutable_buffer &, bool)` |
| 0.60 | vostok/core/sources/resources_mount_ptr.cpp | `public: __thiscall vostok::resources::fs_task_unmount::fs_task_unmount(class vostok::resources::resource_ptr<class vostok::resources::vfs_sub_fat_resource, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 0.65 | vostok/game_core/sources/base_project.cpp | `public: virtual __thiscall survarium::base_project::~base_project(void)` |
| 0.77 | vostok/render/engine/sources/grass_patch.cpp | `public: void __thiscall vostok::render::grass_patch::sort_instances(class vostok::math::float3const &)` |
| 0.80 | vostok/particle/sources/particle_actions.cpp | `public: virtual void __thiscall vostok::particle::particle_action_billboard::init(class vostok::particle::particle_emitter_instance *, struct vostok::particle::base_particle *, float)` |
| 0.94 | vostok/math_aabb_inline.h | `class vostok::math::aabb __cdecl vostok::math::create_zero_aabb(void)` |
| 1.02 | vostok/game/sources/player_input_handler.cpp | `private: virtual void __thiscall survarium::player_input_handler::on_after_processing(struct vostok::input::world *)` |
| 1.05 | vostok/core/sources/resources_manager_deallocation.cpp | `public: void __thiscall vostok::resources::resources_manager::push_delayed_delete_unmanaged_resource(class vostok::resources::unmanaged_resource *)` |
| 1.08 | vostok/render/engine/sources/stage_shadow_direct.cpp | `public: virtual void __thiscall vostok::render::stage_shadow_direct::execute_disabled(void)` |
| 1.09 | vostok/vfs/sources/iterator.cpp | `public: __thiscall vostok::vfs::vfs_iterator::vfs_iterator(class vostok::vfs::base_node<1> *, class vostok::vfs::base_node<1> *, class vostok::vfs::vfs_hashset *, enum vostok::vfs::vfs_iterator::type_enum)` |
| 1.20 | vostok/physics/sources/bullet_physics_world.cpp | `private: void __thiscall vostok::physics::bullet_physics_world::notify_about_contact(void)` |
| 1.38 | vostok/particle/sources/particle_emitter_instance.cpp | `void __cdecl vostok::particle::prepare_render_emitter_instance(class vostok::particle::particle_emitter_instance *)` |
| 1.39 | vostok/fs/sources/asynchronous_device_interface.cpp | `private: void __thiscall vostok::fs_new::asynchronous_device_interface::get_synchronous_access(class vostok::fs_new::synchronous_device_interface *, class vostok::memory::base_allocator *)` |
| 1.40 | vostok/fs/sources/asynchronous_device_interface.cpp | `private: void __thiscall vostok::fs_new::asynchronous_device_interface::process_queries(class vostok::one_way_threads_channel_with_response<class vostok::fs_new::asynchronous_device_query, class vostok::intrusive_mpsc_queue<class vostok::fs_new::asynchronous_device_query, class vostok::threads_channel_query_base_helper<class vostok::fs_new::asynchronous_device_query>, 0>, class vostok::fs_new::null_device_query> *)` |
| 1.43 | vostok/game_core/sources/weapon_core_cook.cpp | `public: virtual void __thiscall survarium::weapon_core_cook::delete_resource(class vostok::resources::resource_base *)` |
| 1.46 | vostok/game_core/sources/collision_sensor.cpp | `public: virtual void __thiscall survarium::collision_sensor::tick(unsigned int, unsigned int)` |
| 1.48 | vostok/game_core/sources/weapon_core.cpp | `public: virtual void __thiscall survarium::weapon_core::set_next_ammo_type(void)` |
| 1.49 | vostok/core/sources/resources_resource_base.cpp | `private: void __thiscall vostok::resources::resource_base::on_deassociated_from_fat(void)` |
| 1.55 | vostok/render/engine/sources/renderer.cpp | `public: bool __thiscall vostok::render::sort_by_distance_predicate::operator()(struct vostok::render::render_surface_instance const *, struct vostok::render::render_surface_instance const *) const` |
| 1.62 | vostok/game/sources/login_menu.cpp | `public: virtual void __thiscall survarium::login_menu::on_activate(void)` |
| 1.65 | vostok/render/core/dx11/sources/shader_constant_table.cpp | `private: class vostok::render::shader_constant * __thiscall vostok::render::shader_constant_table::get(char const *const)` |
| 1.67 | vostok/animation/sources/bi_spline_skeleton_animation_baked_cook.cpp | `private: virtual void __thiscall vostok::animation::bi_spline_skeleton_animation_baked_cook::deallocate_resource(void *)` |
| 1.67 | vostok/core/sources/configs_binary_config_cook.cpp | `public: virtual void __thiscall vostok::core::configs::binary_config_cook_impl::deallocate_resource(void *)` |
| 1.67 | vostok/core/sources/unmanaged_allocation_cook.cpp | `public: virtual void __thiscall vostok::resources::unmanaged_allocation_cook::deallocate_resource(void *)` |
| 1.70 | vostok/core/sources/compressor_ppmd_allocator.h | `public: void * __thiscall ppmd_allocator::ExpandUnits(void *, unsigned int)` |
| 1.71 | vostok/intrusive_list_inline.h | `public: void __thiscall vostok::intrusive_list<class vostok::sound::receiver_collision, class vostok::sound::receiver_collision *, 12, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::for_each<struct vostok::sound::receiver_unconditional_erasing_predicate>(struct vostok::sound::receiver_unconditional_erasing_predicate const &) const` |
| 1.74 | vostok/engine/sources/editor_console.cpp | `public: virtual void __thiscall vostok::engine::editor_console::on_deactivate(void)` |
| 1.75 | vostok/vfs/sources/mount_utils.cpp | `class vostok::vfs::base_node<1> * __cdecl vostok::vfs::find_node_of_mount(class vostok::vfs::vfs_hashset &, class vostok::fs_new::virtual_path_string const &, unsigned int, unsigned int)` |
| 1.82 | vostok/render/facade/sources/debug_renderer.cpp | `private: void __thiscall vostok::render::debug::renderer::draw_primitive_solid(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float4x4const &, class vostok::math::float3const &, float const *, unsigned int, unsigned short const *, unsigned int, class vostok::math::color const &, bool)` |
| 1.82 | vostok/game/sources/game.cpp | `public: void __thiscall survarium::game::toggle_pause(void)` |
| 1.85 | vostok/sound/sources/sound_world.cpp | `public: virtual __thiscall vostok::sound::sound_world::~sound_world(void)` |
| 1.94 | vostok/core/sources/game_resman_quality_increase.cpp | `private: void __thiscall vostok::resources::quality_increase_functionality::update_current_satisfaction(void)` |
| 2.00 | vostok/core/sources/memory_override_operators.cpp | `__calloc_crt` |
| 2.09 | vostok/buffer_vector_inline.h | `public: void __thiscall vostok::buffer_vector<class survarium::bullet *>::erase(class survarium::bullet **const &, class survarium::bullet **const &)` |
| 2.09 | vostok/buffer_vector_inline.h | `public: void __thiscall vostok::buffer_vector<class survarium::bullet *>::erase(class survarium::bullet **const &, class survarium::bullet **const &)` |
| 2.09 | vostok/buffer_vector_inline.h | `public: void __thiscall vostok::buffer_vector<class survarium::bullet *>::erase(class survarium::bullet **const &, class survarium::bullet **const &)` |
| 2.09 | vostok/buffer_vector_inline.h | `public: void __thiscall vostok::buffer_vector<class survarium::bullet *>::erase(class survarium::bullet **const &, class survarium::bullet **const &)` |
| 2.09 | vostok/buffer_vector_inline.h | `public: void __thiscall vostok::buffer_vector<class survarium::bullet *>::erase(class survarium::bullet **const &, class survarium::bullet **const &)` |
| 2.20 | vostok/render/core/dx11/sources/render_target.cpp | `private: __thiscall vostok::render::render_target::~render_target(void)` |
| 2.24 | vostok/render/engine/sources/render_particle_emitter_instance.cpp | `public: void __thiscall vostok::render::render_particle_emitter_instance::render_trails(class vostok::math::float3const &, struct vostok::particle::base_particle *, unsigned int)` |
| 2.35 | vostok/render/core/dx11/sources/res_sampler_list.cpp | `public: int __thiscall vostok::render::res_sampler_list::compare(class vostok::render::res_sampler_list const &) const` |
| 2.44 | vostok/animation/sources/single_animation.cpp | `public: virtual class vostok::animation::mixing::expression __thiscall vostok::animation::single_animation::emit(class vostok::mutable_buffer &, bool &) const` |
| 2.50 | vostok/fs/sources/windows_hdd_file_system.cpp | `public: virtual void __thiscall vostok::fs_new::windows_hdd_file_system::flush(void *)` |
| 2.56 | vostok/core/sources/configs_binary_config_cook.cpp | `public: virtual void __thiscall vostok::core::configs::binary_config_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 2.79 | vostok/render/engine/sources/render_particle_emitter_instance.cpp | `public: virtual void __thiscall vostok::render::render_particle_emitter_instance::change_material(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)` |

## Engine units in base but gone in target

- vostok/animation/animation_callback.h
- vostok/animation/animation_states_dumper.h
- vostok/animation/fingers_to_weapon_corrector.h
- vostok/animation/hand_to_weapon_ik_solver.h
- vostok/animation/ik_utils.h
- vostok/animation/mixing_binary_tree_binary_operation_node_inline.h
- vostok/animation/sources/anim_track.cpp
- vostok/animation/sources/anim_track_eval.cpp
- vostok/animation/sources/anim_track_io.cpp
- vostok/animation/sources/animation_player_serialization.cpp
- vostok/animation/sources/fingers_to_weapon_corrector.cpp
- vostok/animation/sources/hand_to_weapon_ik_solver.cpp
- vostok/animation/sources/ik_solver.cpp
- vostok/animation/sources/legs_ik_drawer.cpp
- vostok/animation/sources/legs_ik_solver.cpp
- vostok/animation/sources/mixing_animation_event.h
- vostok/animation/sources/mixing_n_ary_tree.h
- vostok/animation/sources/mixing_n_ary_tree_deserializer.cpp
- vostok/animation/sources/mixing_n_ary_tree_event_iterator_inline.h
- vostok/animation/sources/mixing_n_ary_tree_node_cloner.cpp
- vostok/animation/sources/mixing_n_ary_tree_node_cloner.h
- vostok/animation/sources/mixing_n_ary_tree_serializer.cpp
- vostok/animation/sources/mixing_n_ary_tree_time_scale_node_inline.h
- vostok/animation/sources/mixing_n_ary_tree_weight_calculator_inline.h
- vostok/animation/sources/mixing_n_ary_tree_weight_event_iterator_inline.h
- vostok/animation/sources/skeleton_animation_scene.cpp
- vostok/animation/sources/skeleton_animation_scene_cook.cpp
- vostok/bit_extensions.h
- vostok/circular_buffer.h
- vostok/circular_buffer_inline.h
- vostok/collision/sources/animated_object_cook.cpp
- vostok/collision/sources/colliders_ray_aabb.h
- vostok/collision/sources/colliders_ray_geometry_base.h
- vostok/core/sources/compressor_ppmd_stream_inline.h
- vostok/core/sources/game_resman_free_collection.h
- vostok/core/sources/journaling_extensions.cpp
- vostok/core/sources/journaling_journal.cpp
- vostok/core/sources/logging_filters_console_command.cpp
- vostok/core/sources/memory_monitor.cpp
- vostok/core/sources/replay_match_io.cpp
- vostok/core/sources/timing_floating_timer.cpp
- vostok/debug/crash_handler.h
- vostok/debug/sources/crash_handling.cpp
- vostok/fs/file_type.h
- vostok/fs/physical_path_info_data.h
- vostok/fs/physical_path_iterator.h
- vostok/game/sources/artefact_cook.cpp
- vostok/game/sources/artefact_inline.h
- vostok/game/sources/base_match_client.h
- vostok/game/sources/breath_holding_sound_effect.cpp
- vostok/game/sources/damage_sound_effect.cpp
- vostok/game/sources/demo_camera.cpp
- vostok/game/sources/effect_zone.cpp
- vostok/game/sources/effect_zone_cook.cpp
- vostok/game/sources/firewall_exception.cpp
- vostok/game/sources/first_person_game_effect_presenter.cpp
- vostok/game/sources/game_effect_presenter.h
- vostok/game/sources/game_statistics_handler.cpp
- vostok/game/sources/generic_anomaly.h
- vostok/game/sources/generic_anomaly_cook.h
- vostok/game/sources/grenade.cpp
- vostok/game/sources/grenade_cook.cpp
- vostok/game/sources/grenade_cook.h
- vostok/game/sources/grenade_set.cpp
- vostok/game/sources/grenade_set_cook.cpp
- vostok/game/sources/hud_game_effect.cpp
- vostok/game/sources/hud_game_effect_emitter.cpp
- vostok/game/sources/hud_game_effect_emitter_cook.cpp
- vostok/game/sources/hud_game_effect_presenter.cpp
- vostok/game/sources/journaling_match_client.cpp
- vostok/game/sources/journaling_match_client.h
- vostok/game/sources/lobby_camera.h
- vostok/game/sources/lobby_menu_character.cpp
- vostok/game/sources/match_client.h
- vostok/game/sources/object_ambient_light.cpp
- vostok/game/sources/object_track.cpp
- vostok/game/sources/particle_game_effect.cpp
- vostok/game/sources/particle_game_effect_emitter.cpp
- vostok/game/sources/particle_game_effect_emitter_cook.cpp
- vostok/game/sources/particle_game_effect_presenter.cpp
- vostok/game/sources/player_equipment_sound_effect.cpp
- vostok/game/sources/portable_interactive_object.cpp
- vostok/game/sources/portable_interactive_object_with_finger_correction.cpp
- vostok/game/sources/post_process_game_effect.cpp
- vostok/game/sources/post_process_game_effect_emitter.cpp
- vostok/game/sources/post_process_game_effect_emitter_cook.cpp
- vostok/game/sources/post_process_game_effect_presenter.cpp
- vostok/game/sources/sound_game_effect.cpp
- vostok/game/sources/sound_game_effect_emitter.cpp
- vostok/game/sources/sound_game_effect_emitter_cook.cpp
- vostok/game/sources/sound_game_effect_presenter.cpp
- vostok/game/sources/sound_game_effect_presenter.h
- vostok/game/sources/stamina_sound_effect.cpp
- vostok/game/sources/third_person_game_effect_presenter.cpp
- vostok/game/sources/timelimit_rule.cpp
- vostok/game/sources/timelimit_rule.h
- vostok/game/sources/timelimit_rule_cook.cpp
- vostok/game/sources/victory_item_cook.cpp
- vostok/game/sources/victory_items_container_cook.cpp
- vostok/game/sources/weapon_preview_state.cpp
- vostok/game/sources/weapon_preview_state_cook.cpp
- vostok/game_core/animations_registrator.h
- vostok/game_core/animations_registry.h
- vostok/game_core/artefact_base.h
- vostok/game_core/artefact_core_cook.h
- vostok/game_core/artefact_rattle_core.h
- vostok/game_core/base_game_effect_presenter.h
- vostok/game_core/body_part_regeneration_modifier.h
- vostok/game_core/bullet_manager_history_item_inline.h
- vostok/game_core/carryable_object.h
- vostok/game_core/character_breath_vibration_params.h
- vostok/game_core/composite_game_effect_emitter_cook_inline.h
- vostok/game_core/effect_zone_core.h
- vostok/game_core/game_effect.h
- vostok/game_core/game_effect_emitter.h
- vostok/game_core/game_effect_node.h
- vostok/game_core/game_effect_player.h
- vostok/game_core/game_match_rule_base.h
- vostok/game_core/game_material_manager.h
- vostok/game_core/game_objects_history_item_inline.h
- vostok/game_core/game_rules_history_item_inline.h
- vostok/game_core/game_world_core_impl_inline.h
- vostok/game_core/generic_anomaly_core_cook.h
- vostok/game_core/grenade_core.h
- vostok/game_core/grenade_core_cook.h
- vostok/game_core/grenade_set_core.h
- vostok/game_core/grenade_set_core_cook.h
- vostok/game_core/history.h
- vostok/game_core/history_inline.h
- vostok/game_core/hit_types.h
- vostok/game_core/kd_stats_rule.h
- vostok/game_core/player_move_direction.h
- vostok/game_core/player_serialized_state_inline.h
- vostok/game_core/player_speed_parameters.h
- vostok/game_core/portable_interactive_object_core.h
- vostok/game_core/portable_interactive_object_core_inline.h
- vostok/game_core/single_game_effect.h
- vostok/game_core/sources/animations_container_utils_inline.h
- vostok/game_core/sources/animations_registry.cpp
- vostok/game_core/sources/anomaly_damage_protector.cpp
- vostok/game_core/sources/artefact_base.cpp
- vostok/game_core/sources/artefact_base_config.cpp
- vostok/game_core/sources/artefact_core_cook.cpp
- vostok/game_core/sources/artefact_lifebone_core_config.cpp
- vostok/game_core/sources/artefact_onyx_core.cpp
- vostok/game_core/sources/artefact_onyx_core_config.cpp
- vostok/game_core/sources/artefact_rattle_core_config.cpp
- vostok/game_core/sources/artefact_spring_core.cpp
- vostok/game_core/sources/artefact_spring_core_config.cpp
- vostok/game_core/sources/bullet_manager_explosion.cpp
- vostok/game_core/sources/collision_user.cpp
- vostok/game_core/sources/composite_game_effect.cpp
- vostok/game_core/sources/composite_game_effect_emitter.cpp
- vostok/game_core/sources/curing_event_status.cpp
- vostok/game_core/sources/damage_zone_core_cook.cpp
- vostok/game_core/sources/effect_zone_core.cpp
- vostok/game_core/sources/factions.cpp
- vostok/game_core/sources/fwd_animation_interval_end_time_calculator.cpp
- vostok/game_core/sources/game_effect_emitter.cpp
- vostok/game_core/sources/game_effect_emitter_cook.cpp
- vostok/game_core/sources/game_effect_player.cpp
- vostok/game_core/sources/game_effect_time_calculator.cpp
- vostok/game_core/sources/game_event_history_item.cpp
- vostok/game_core/sources/game_state_history_item.cpp
- vostok/game_core/sources/game_world_core.cpp
- vostok/game_core/sources/gather_victory_items_rule.cpp
- vostok/game_core/sources/gather_victory_items_rule_cook.cpp
- vostok/game_core/sources/generic_anomaly_core_cook.cpp
- vostok/game_core/sources/grenade_core.cpp
- vostok/game_core/sources/grenade_core_cook.cpp
- vostok/game_core/sources/grenade_set_core.cpp
- vostok/game_core/sources/grenade_set_core_cook.cpp
- vostok/game_core/sources/hit_animation_selector_body_part.cpp
- vostok/game_core/sources/hit_animations_selector.cpp
- vostok/game_core/sources/jump_logic_base_state.cpp
- vostok/game_core/sources/jump_logic_state_prepare.cpp
- vostok/game_core/sources/jump_logic_state_prepare.h
- vostok/game_core/sources/kd_stats_rule.cpp
- vostok/game_core/sources/kd_stats_rule_cook.cpp
- vostok/game_core/sources/match_options.cpp
- vostok/game_core/sources/player_history_item.cpp
- vostok/game_core/sources/player_logic_dead_state.cpp
- vostok/game_core/sources/player_params_modifiers_container.cpp
- vostok/game_core/sources/player_profile.cpp
- vostok/game_core/sources/player_respawn_rule.cpp
- vostok/game_core/sources/player_respawn_rule.h
- vostok/game_core/sources/player_respawn_rule_cook.cpp
- vostok/game_core/sources/player_shared_statistics.cpp
- vostok/game_core/sources/portable_interactive_object_core.cpp
- vostok/game_core/sources/pvp_match_core.cpp
- vostok/game_core/sources/pvp_match_core_cook.cpp
- vostok/game_core/sources/quest.cpp
- vostok/game_core/sources/random_permutation_game_effect_emitter.cpp
- vostok/game_core/sources/registry_of_artefacts.cpp
- vostok/game_core/sources/respawn_point_core.cpp
- vostok/game_core/sources/selected_animations_dumper.cpp
- vostok/game_core/sources/server_game_project.cpp
- vostok/game_core/sources/shared_statistics.cpp
- vostok/game_core/sources/short_jump_landing_state.cpp
- vostok/game_core/sources/short_jump_landing_state.h
- vostok/game_core/sources/short_jump_start_state.cpp
- vostok/game_core/sources/short_jump_start_state.h
- vostok/game_core/sources/single_game_effect.cpp
- vostok/game_core/sources/teammate_cure_event_manager.cpp
- vostok/game_core/sources/timelimit_rule_core.cpp
- vostok/game_core/sources/timelimit_rule_core_cook.cpp
- vostok/game_core/sources/transition_helper.cpp
- vostok/game_core/sources/victory_item_core_animation_end_aware_state.cpp
- vostok/game_core/sources/victory_item_core_base_state.cpp
- vostok/game_core/sources/victory_item_core_base_state.h
- vostok/game_core/sources/victory_item_core_carry_state.cpp
- vostok/game_core/sources/victory_item_core_carry_state.h
- vostok/game_core/sources/victory_item_core_put_state.cpp
- vostok/game_core/sources/victory_item_core_put_state.h
- vostok/game_core/sources/victory_item_core_take_state.cpp
- vostok/game_core/sources/victory_item_core_take_state.h
- vostok/game_core/sources/victory_item_event_manager.cpp
- vostok/game_core/sources/weapon_core_melee_state.cpp
- vostok/game_core/sources/weapon_core_melee_state_cook.cpp
- vostok/game_core/sources/weapon_core_throw_grenade_state.cpp
- vostok/game_core/sources/weapon_core_throw_grenade_state_cook.cpp
- vostok/game_core/sources/weapon_core_throw_grenade_substate.cpp
- vostok/game_core/sources/weapon_damage_params.cpp
- vostok/game_core/sources/weapon_user_animations_container.cpp
- vostok/game_core/statistics_history_item_inline.h
- vostok/game_core/timelimit_rule_core.h
- vostok/game_core/weapon_breath_vibration_params.h
- vostok/game_core/weapon_core_animation_end_aware_state.h
- vostok/game_core/weapon_sound_events_channel_subscriber.h
- vostok/input/sources/journaling_gamepad.cpp
- vostok/input/sources/journaling_gamepad.h
- vostok/input/sources/journaling_input_handler.cpp
- vostok/input/sources/journaling_input_handler.h
- vostok/input/sources/journaling_keyboard.cpp
- vostok/input/sources/journaling_keyboard.h
- vostok/input/sources/journaling_mouse.cpp
- vostok/input/sources/journaling_mouse.h
- vostok/input/sources/platform_gamepad_win_xbox360.cpp
- vostok/input/sources/platform_keyboard.cpp
- vostok/input/sources/platform_keyboard.h
- vostok/input/sources/platform_keyboard_win.cpp
- vostok/input/sources/platform_mouse.cpp
- vostok/input/sources/platform_mouse.h
- vostok/input/sources/platform_mouse_win.cpp
- vostok/journaling_extensions.h
- vostok/journaling_reader_inline.h
- vostok/logging/fs_new_device_impl.h
- vostok/logging/fs_new_file_impl.h
- vostok/logging/memory_base_allocator_wrapper.h
- vostok/loose_ptr_base_inline.h
- vostok/loose_ptr_data_inline.h
- vostok/loose_ptr_inline.h
- vostok/macro_unreferenced_parameter.h
- vostok/map_inline.h
- vostok/math_frustum.h
- vostok/memory_allocator_adapter.h
- vostok/network/sources/functor_response.h
- vostok/network/sources/network_world.h
- vostok/network_core/buffer_reader_inline.h
- vostok/network_core/buffer_writer.h
- vostok/network_core/buffer_writer_inline.h
- vostok/network_core/mutable_buffer_inline.h
- vostok/particle/sources/particle_emitter_inline.h
- vostok/particle/sources/particle_system_inline.h
- vostok/physics/animated_rigid_body.h
- vostok/physics/base_physics_object.h
- vostok/physics/dynamic_rigid_body.h
- vostok/physics/sources/bt_closest_convex_not_me_result_callback.h
- vostok/physics/sources/character_controller_can_stand_tester.cpp
- vostok/physics/sources/character_controller_capsule_move_step_tester.cpp
- vostok/physics/sources/character_controller_jump_tester.cpp
- vostok/physics/sources/character_controller_jump_vertical_tester.cpp
- vostok/physics/sources/character_controller_move_step_tester.cpp
- vostok/physics/sources/character_controller_step_down_tester.cpp
- vostok/physics/sources/character_controller_straighten_tester.cpp
- vostok/physics/sources/character_controller_sweep_test_cache_template.h
- vostok/physics/sources/character_controller_utilities.h
- vostok/physics/sources/character_move_sweep_callback.cpp
- vostok/physics/sources/character_up_sweep_test_callback.h
- vostok/physics/sources/dynamic_rigid_body.cpp
- vostok/physics/sources/old_bullet_character_controller.cpp
- vostok/physics/sources/old_bullet_character_controller.h
- vostok/physics/static_rigid_body.h
- vostok/render/core/dx11/backend_handlers_inline.h
- vostok/render/core/dx11/sampler_state_descriptor_inline.h
- vostok/render/core/dx11/sources/hw_buffer_pool.cpp
- vostok/render/core/dx11/sources/pix_event_wrapper.cpp
- vostok/render/core/dx11/sources/res_buffer_list.cpp
- vostok/render/core/dx11/sources/shader_buffer.cpp
- vostok/render/core/dx11/sources/texture_converter_params.cpp
- vostok/render/core/dx11/untyped_buffer_inline.h
- vostok/render/core/dx11/xs_data.h
- vostok/render/core/hw_buffer_pool.h
- vostok/render/engine/sources/ambient_light.cpp
- vostok/render/engine/sources/bake_decal_cook.cpp
- vostok/render/engine/sources/decal_instance.h
- vostok/render/engine/sources/effect_aberration.h
- vostok/render/engine/sources/effect_add_border_padding.cpp
- vostok/render/engine/sources/effect_ambient_light.h
- vostok/render/engine/sources/effect_apply_ambient_lights.cpp
- vostok/render/engine/sources/effect_apply_ssao.cpp
- vostok/render/engine/sources/effect_atmospheric_scattering.h
- vostok/render/engine/sources/effect_block_compression.cpp
- vostok/render/engine/sources/effect_channel_blur.cpp
- vostok/render/engine/sources/effect_color_grading_lut_blending.cpp
- vostok/render/engine/sources/effect_composition.h
- vostok/render/engine/sources/effect_copy_shadow_map.cpp
- vostok/render/engine/sources/effect_editor_show_cascaded_shadow_map_depth.cpp
- vostok/render/engine/sources/effect_editor_view_mode.cpp
- vostok/render/engine/sources/effect_fstage_fake_translucency_materials.cpp
- vostok/render/engine/sources/effect_fstage_sphere_projection_materials.cpp
- vostok/render/engine/sources/effect_mask_far_plane.cpp
- vostok/render/engine/sources/effect_offscreen_particle_lighting_materials.cpp
- vostok/render/engine/sources/effect_radial_motion_blur.cpp
- vostok/render/engine/sources/effect_shadow_mask.cpp
- vostok/render/engine/sources/effect_shadow_mask.h
- vostok/render/engine/sources/render_particle_emitter_instance.h
- vostok/render/engine/sources/render_texture_cook.cpp
- vostok/render/engine/sources/scene_texture_streaming.cpp
- vostok/render/engine/sources/sliced_cube_geometry.cpp
- vostok/render/engine/sources/stage_accumulate_distortion.h
- vostok/render/engine/sources/stage_apply_distortion.h
- vostok/render/engine/sources/stage_atmosphere.h
- vostok/render/engine/sources/stage_composition.cpp
- vostok/render/engine/sources/stage_composition.h
- vostok/render/engine/sources/stage_debug.h
- vostok/render/engine/sources/stage_foreground.cpp
- vostok/render/engine/sources/stage_foreground.h
- vostok/render/engine/sources/stage_forward.h
- vostok/render/engine/sources/stage_rain.h
- vostok/render/engine/sources/stage_screen_space_reflections.cpp
- vostok/render/engine/sources/stage_screen_space_reflections.h
- vostok/render/engine/sources/stage_shadow_mask.cpp
- vostok/render/engine/sources/stage_view_mode.h
- vostok/render/engine/sources/texture_gpu_converter_cook.cpp
- vostok/render/engine/sources/texture_streaming_async_worker.cpp
- vostok/render/facade/common_types.h
- vostok/render/facade/environment_properties_inline.h
- vostok/render/facade/gamma_correction.h
- vostok/render/facade/sources/environment_properties.cpp
- vostok/render/facade/sources/light_props.cpp
- vostok/render/facade/sources/user_render_options_values.cpp
- vostok/render/facade/sources/vertex_input_type.cpp
- vostok/scaleform/sources/d3d1x_events.h
- vostok/sound/sources/single_sound.h
- vostok/sound/sources/sound_instance_proxy_internal.h
- vostok/sound/sources/sound_propagator.h
- vostok/strings_shared_profile.h
- vostok/tasks_task.h
- vostok/timing_floating_timer_inline.h
- vostok/unique_ptr_inline.h
- vostok/vfs/mount_args.h
- vostok/vfs/sources/archive_file_node_base.h
- vostok/vfs/sources/base_folder_node.h
