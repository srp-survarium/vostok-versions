# v0.1.1e-build884 -> v0.20e-build1916

Lists below: **hand-written engine** (`vostok/*`, compiler-generated excluded). Full breakdown:

| bucket | engine | generated | third-party |
| --- | ---: | ---: | ---: |
| identical | **295** | 142 | 725 |
| changed | **2856** | 322 | 1900 |
| new / rewritten | **6883** | 1401 | 4252 |
| units removed | **441** | - | 60 |

## Most-changed engine functions (50 shown)

| match % | unit | function |
| ---: | --- | --- |
| 0.02 | vostok/engine/sources/engine_world_network.cpp | `private: void __thiscall vostok::engine::engine_world::initialize_network(void)` |
| 0.02 | vostok/engine/sources/engine_world_sound.cpp | `private: void __thiscall vostok::engine::engine_world::initialize_sound(void)` |
| 0.12 | vostok/game/sources/empty_hands_cook.cpp | `private: void __thiscall survarium::empty_hands_cook::on_empty_hands_config_loaded(class vostok::resources::queries_result &)` |
| 0.15 | vostok/render/engine/sources/render_engine_world_pc_dx11.cpp | `public: void __thiscall vostok::render::engine::world::set_model_visible_by_id(class vostok::resources::resource_ptr<class vostok::render::render_model_instance, class vostok::resources::unmanaged_intrusive_base> const &, unsigned int, unsigned int)` |
| 0.25 | vostok/render/engine/sources/light.cpp | `public: void __thiscall vostok::render::light::xform_calc(void)` |
| 0.33 | vostok/core/sources/resources_query_result_path.cpp | `private: void __thiscall vostok::resources::query_result::late_set_fat_it(class vostok::vfs::vfs_iterator)` |
| 0.42 | vostok/render/engine/sources/render_model_static.cpp | `public: virtual __thiscall vostok::render::static_render_model_instance::~static_render_model_instance(void)` |
| 0.44 | vostok/core/sources/math_quaternion.cpp | `public: __thiscall vostok::math::quaternion::quaternion(class vostok::math::float4x4const &)` |
| 0.44 | vostok/ai/sources/base_lexeme.cpp | `private: class vostok::ai::planning::base_lexeme_ptr __thiscall vostok::ai::planning::base_lexeme::expand_brackets_as_and(class vostok::memory::stack_allocator &, class vostok::ai::planning::base_lexeme const &) const` |
| 0.46 | vostok/render/facade/sources/scene_renderer.cpp | `public: void __thiscall vostok::render::scene_renderer::set_projection_matrix(class vostok::resources::resource_ptr<struct vostok::render::base_scene_view, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float4x4const &)` |
| 0.59 | vostok/render/engine/sources/renderer.cpp | `public: void __thiscall vostok::render::renderer::recreate_stage(enum vostok::render::enum_render_stage_type)` |
| 0.66 | vostok/render/engine/sources/hw_hiz_occlusion_manager.cpp | `private: void __thiscall vostok::render::hw_hiz_occlusion_manager::downsample_occlusion_buffer(void)` |
| 0.67 | vostok/particle/sources/help_functions.h | `float __cdecl vostok::particle::read_config_value<float, class vostok::configs::binary_config_value>(class vostok::configs::binary_config_value const &, char const *, float const &)` |
| 0.68 | vostok/render/core/dx11/sources/backend_handlers.cpp | `private: void __thiscall vostok::render::textures_handler<1>::assign(class vostok::render::res_texture_list const *)` |
| 0.68 | vostok/render/core/dx11/sources/backend_handlers.cpp | `private: void __thiscall vostok::render::textures_handler<1>::assign(class vostok::render::res_texture_list const *)` |
| 0.68 | vostok/render/core/dx11/sources/backend_handlers.cpp | `private: void __thiscall vostok::render::textures_handler<1>::assign(class vostok::render::res_texture_list const *)` |
| 0.69 | vostok/sound/sources/sound_scene_hdr.cpp | `private: void __thiscall vostok::sound::sound_scene::notify_listener2(unsigned int)` |
| 0.76 | vostok/vfs/sources/mounter.cpp | `protected: void __thiscall vostok::vfs::mounter::destroy_this_if_needed(void)` |
| 0.77 | vostok/render/engine/sources/stage_shadow_direct.cpp | `public: virtual void __thiscall vostok::render::stage_shadow_direct::execute(void)` |
| 0.77 | vostok/particle/sources/particle_actions.cpp | `public: virtual void __thiscall vostok::particle::particle_action_billboard::set_defaults(bool)` |
| 0.86 | vostok/sound/sources/sound_instance_proxy_internal.cpp | `public: __thiscall vostok::sound::sound_instance_proxy_internal::sound_instance_proxy_internal(class vostok::sound::sound_scene &, class vostok::resources::resource_ptr<class vostok::sound::sound_emitter, class vostok::resources::unmanaged_intrusive_base>, class vostok::sound::sound_propagator_emitter const &, class vostok::sound::world_user &, enum vostok::sound::sound_cone_type)` |
| 0.86 | vostok/render/engine/sources/decal_instance.cpp | `public: __thiscall vostok::render::decal_instance::decal_instance(struct vostok::collision::space_partitioning_tree *, struct vostok::render::decal_properties const &, unsigned int)` |
| 0.92 | vostok/game/sources/key_binder.cpp | `public: void __thiscall survarium::key_binder::bind_key(char const *, int)` |
| 1.02 | vostok/vfs/sources/mount_transfer.cpp | `public: __thiscall vostok::vfs::transfer_children::transfer_children(class vostok::vfs::vfs_hashset &, class vostok::fs_new::virtual_path_string const &, unsigned int, class vostok::vfs::base_node<1> *, class vostok::vfs::base_node<1> *)` |
| 1.03 | vostok/render/engine/sources/stage_lights.cpp | `private: void __thiscall vostok::render::stage_lights::create_pyramid_geometry(void)` |
| 1.06 | vostok/game_core/sources/weapon_ammunition_cook.cpp | `private: void __thiscall survarium::weapon_ammunition_cook::on_config_ready(class vostok::resources::queries_result &, class vostok::resources::query_result_for_cook *)` |
| 1.11 | vostok/particle/sources/particle_system_instance_cook.cpp | `public: virtual void __thiscall vostok::particle::particle_system_instance_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 1.12 | vostok/render/core/dx11/sources/backend.cpp | `public: void __thiscall vostok::render::backend::clear_render_targets(class vostok::math::color)` |
| 1.12 | vostok/game_core/sources/weapon_core.cpp | `private: bool __thiscall survarium::weapon_core::chamber_a_round_pred(void) const` |
| 1.14 | vostok/core/sources/resources_query_result_cook.cpp | `private: void __thiscall vostok::resources::query_result::finish_normal_query(enum vostok::resources::cook_base::result_enum)` |
| 1.19 | vostok/ui/sources/ui_text_inline.h | `public: virtual void __thiscall vostok::ui::ui_text<struct vostok::ui::static_text>::set_text(char const *)` |
| 1.20 | vostok/one_way_threads_channel_with_response_inline.h | `protected: class vostok::intrusive_spsc_queue<class vostok::fs_new::asynchronous_device_query, class vostok::threads_channel_query_base_helper<class vostok::fs_new::asynchronous_device_query>, 4> * __thiscall vostok::one_way_threads_channel_with_response<class vostok::fs_new::asynchronous_device_query, class vostok::intrusive_mpsc_queue<class vostok::fs_new::asynchronous_device_query, class vostok::threads_channel_query_base_helper<class vostok::fs_new::asynchronous_device_query>, 0>, class vostok::fs_new::null_device_query>::backward_queue_for_current_thread(class vostok::memory::base_allocator *)` |
| 1.21 | vostok/game_core/sources/weapon_core.cpp | `public: void __thiscall survarium::weapon_core::instant_fire(unsigned int)` |
| 1.22 | vostok/particle/sources/particle_system_instance_impl.cpp | `public: unsigned int __thiscall vostok::particle::particle_system_instance_impl::calc_num_new_particles(float)` |
| 1.23 | vostok/render/engine/sources/sky_ambient_occlusion.cpp | `public: __thiscall vostok::render::sky_ambient_occlusion::sky_ambient_occlusion(struct vostok::render::sky_ambient_occlusion_properties const &, unsigned int)` |
| 1.23 | vostok/render/engine/sources/render_model_cooker.cpp | `private: void __thiscall vostok::render::static_render_model_instance_cook::on_sub_resources_loaded(class vostok::resources::queries_result &)` |
| 1.26 | vostok/vfs/sources/virtual_file_system.cpp | `void __cdecl vostok::vfs::query_hot_mount_and_wait(class vostok::vfs::virtual_file_system &, class vostok::fs_new::native_path_string const &, class vostok::fs_new::virtual_path_string *, class vostok::vfs::vfs_locked_iterator *, class vostok::memory::base_allocator *, class boost::function<void __cdecl (void)> const &)` |
| 1.35 | vostok/scaleform/sources/movie.cpp | `public: void __thiscall survarium::flash_movie::SetViewport(unsigned int, unsigned int)` |
| 1.36 | vostok/render/engine/sources/system_renderer.cpp | `public: void __thiscall vostok::render::system_renderer::fill_surface(class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, bool, struct D3D11_VIEWPORT *, float, float, float, float)` |
| 1.41 | vostok/vfs/sources/find_async_tree.cpp | `void __cdecl vostok::vfs::try_find_tree(struct vostok::vfs::find_environment &)` |
| 1.43 | vostok/particle/sources/particle_system_instance.cpp | `public: void __thiscall vostok::particle::particle_system_instance::stop(float)` |
| 1.44 | vostok/game_core/sources/damage_model_cook.cpp | `survarium::calculate_model_size` |
| 1.46 | vostok/particle/sources/particle_actions.cpp | `public: virtual void __thiscall vostok::particle::particle_action_size_over_lifetime::set_defaults(bool)` |
| 1.46 | vostok/particle/sources/particle_actions.cpp | `public: virtual void __thiscall vostok::particle::particle_action_rotation_over_velocity::set_defaults(bool)` |
| 1.53 | vostok/render/engine/sources/render_engine_world_pc_dx11.cpp | `public: void __thiscall vostok::render::engine::world::remove_particle_system_instance(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>, class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 1.65 | vostok/render/facade/sources/debug_renderer.cpp | `public: void __thiscall vostok::render::debug::renderer::draw_triangle(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, struct vostok::render::vertex_colored const (&)[3], bool)` |
| 1.67 | vostok/core/sources/resources_resource_base.cpp | `public: virtual __thiscall vostok::resources::resource_base::~resource_base(void)` |
| 1.67 | vostok/particle/sources/particle_system_instance_impl.cpp | `public: virtual bool __thiscall vostok::particle::particle_system_instance_impl::is_finished(void)` |
| 1.68 | vostok/animation/sources/mixing_n_ary_tree_animation_time_calculator.cpp | `public: __thiscall vostok::animation::mixing::n_ary_tree_animation_time_calculator::n_ary_tree_animation_time_calculator(class vostok::animation::mixing::n_ary_tree_animation_node &, unsigned int, float, unsigned int, bool)` |
| 1.69 | vostok/render/core/dx11/sources/effect_manager.cpp | `public: void __thiscall vostok::render::effect_manager::delete_pass(class vostok::render::res_pass const *)` |

## Engine units in base but gone in target

- vostok/ai/fsm_state.h
- vostok/ai/npc.h
- vostok/ai/search/a_star_inline.h
- vostok/ai/search/dnf_world_state_inline.h
- vostok/ai/search/graph_wrapper_planner_backward_inline.h
- vostok/ai/search/graph_wrapper_planner_base_inline.h
- vostok/ai/search/graph_wrapper_planner_forward_inline.h
- vostok/ai/search/operator_base_inline.h
- vostok/ai/search/operator_inline.h
- vostok/ai/search/path_constructor_base_inline.h
- vostok/ai/search/path_constructor_edge_inline.h
- vostok/ai/search/path_constructor_planner_backward_inline.h
- vostok/ai/search/path_constructor_vertex_inline.h
- vostok/ai/search/priority_queue_binary_heap_inline.h
- vostok/ai/search/propositional_planner_base_inline.h
- vostok/ai/search/propositional_planner_inline.h
- vostok/ai/search/search_backward_inline.h
- vostok/ai/search/search_forward_inline.h
- vostok/ai/search/search_restrictor_planner_backward_inline.h
- vostok/ai/search/search_restrictor_planner_forward_inline.h
- vostok/ai/search/vertex_allocator_fixed_count_inline.h
- vostok/ai/search/vertex_manager_fixed_count_hash_inline.h
- vostok/ai/search/world_state_inline.h
- vostok/ai/search/world_state_property_inline.h
- vostok/ai/sensed_visual_object.h
- vostok/ai/sources/action_instance.cpp
- vostok/ai/sources/action_parameter.cpp
- vostok/ai/sources/ai_entry_point.cpp
- vostok/ai/sources/ai_world.cpp
- vostok/ai/sources/ai_world.h
- vostok/ai/sources/animation_filter.cpp
- vostok/ai/sources/animation_item.cpp
- vostok/ai/sources/animation_target_selector.cpp
- vostok/ai/sources/animation_target_selector.h
- vostok/ai/sources/base_filter.cpp
- vostok/ai/sources/behaviour.cpp
- vostok/ai/sources/behaviour.h
- vostok/ai/sources/behaviour_cook.cpp
- vostok/ai/sources/behaviour_domain.cpp
- vostok/ai/sources/behaviour_filters.cpp
- vostok/ai/sources/behaviour_goals.cpp
- vostok/ai/sources/behaviour_problem.cpp
- vostok/ai/sources/blackboard.cpp
- vostok/ai/sources/brain_unit.cpp
- vostok/ai/sources/brain_unit_cook.cpp
- vostok/ai/sources/brain_unit_perceptors.cpp
- vostok/ai/sources/brain_unit_selectors.cpp
- vostok/ai/sources/brain_unit_sensors.cpp
- vostok/ai/sources/const_oracle.cpp
- vostok/ai/sources/cover_filter.cpp
- vostok/ai/sources/damage_sensor.cpp
- vostok/ai/sources/damage_sensor_parameters.cpp
- vostok/ai/sources/disturbance_target_selector.cpp
- vostok/ai/sources/disturbance_target_selector.h
- vostok/ai/sources/enemy_filter.cpp
- vostok/ai/sources/enemy_perceptor.cpp
- vostok/ai/sources/enemy_target_selector.cpp
- vostok/ai/sources/enemy_target_selector.h
- vostok/ai/sources/goal.cpp
- vostok/ai/sources/goal_selector.cpp
- vostok/ai/sources/goal_specificator.cpp
- vostok/ai/sources/graph_wrapper_planner_backward.cpp
- vostok/ai/sources/graph_wrapper_planner_forward.cpp
- vostok/ai/sources/hearing_sensor.cpp
- vostok/ai/sources/hearing_sensor_parameters.cpp
- vostok/ai/sources/interaction_sensor.cpp
- vostok/ai/sources/interaction_sensor_parameters.cpp
- vostok/ai/sources/movement_target.cpp
- vostok/ai/sources/npc_subscriptions_manager_inline.h
- vostok/ai/sources/operator.cpp
- vostok/ai/sources/operator_base.cpp
- vostok/ai/sources/operator_holder.cpp
- vostok/ai/sources/oracle.cpp
- vostok/ai/sources/oracle_holder.cpp
- vostok/ai/sources/path_heuristics_planner_backward.cpp
- vostok/ai/sources/path_heuristics_planner_forward.cpp
- vostok/ai/sources/pddl_domain.cpp
- vostok/ai/sources/pddl_domain_inline.h
- vostok/ai/sources/pddl_planner.cpp
- vostok/ai/sources/pddl_predicate_inline.h
- vostok/ai/sources/pddl_predicate_redirector.cpp
- vostok/ai/sources/pddl_problem.cpp
- vostok/ai/sources/pddl_problem_inline.h
- vostok/ai/sources/percept_memory_object.h
- vostok/ai/sources/pickup_item_perceptor.cpp
- vostok/ai/sources/pickup_item_target_selector.cpp
- vostok/ai/sources/pickup_item_target_selector.h
- vostok/ai/sources/plan_tracker.cpp
- vostok/ai/sources/position_filter.cpp
- vostok/ai/sources/position_target_selector.cpp
- vostok/ai/sources/position_target_selector.h
- vostok/ai/sources/pre_perceptors_filter.cpp
- vostok/ai/sources/predicate.cpp
- vostok/ai/sources/predicate_inline.h
- vostok/ai/sources/propositional_planner.cpp
- vostok/ai/sources/search_base.cpp
- vostok/ai/sources/search_restrictor_planner_backward.cpp
- vostok/ai/sources/search_restrictor_planner_forward.cpp
- vostok/ai/sources/smell_sensor.cpp
- vostok/ai/sources/smell_sensor_parameters.cpp
- vostok/ai/sources/sound_filter.cpp
- vostok/ai/sources/sound_item.cpp
- vostok/ai/sources/sound_target_selector.cpp
- vostok/ai/sources/sound_target_selector.h
- vostok/ai/sources/specified_action.cpp
- vostok/ai/sources/specified_problem.cpp
- vostok/ai/sources/subscriptions_manager_inline.h
- vostok/ai/sources/threat_target_selector.cpp
- vostok/ai/sources/threat_target_selector.h
- vostok/ai/sources/vision_sensor.cpp
- vostok/ai/sources/vision_sensor_parameters.cpp
- vostok/ai/sources/weapon_filter.cpp
- vostok/ai/sources/weapon_target_selector.cpp
- vostok/ai/sources/weapon_target_selector.h
- vostok/ai/sources/working_memory.cpp
- vostok/ai/world.h
- vostok/ai_navigation/sources/ai_navigation_entry_point.cpp
- vostok/ai_navigation/sources/navigation_world.h
- vostok/animation/animation_playback_state.h
- vostok/animation/base_interpolator.h
- vostok/animation/cubic_spline_skeleton_animation.h
- vostok/animation/instant_interpolator.h
- vostok/animation/linear_interpolator.h
- vostok/animation/mixing_animation_interval.h
- vostok/animation/mixing_animation_lexeme_parameters.h
- vostok/animation/mixing_base_lexeme_inline.h
- vostok/animation/mixing_binary_operation_lexeme_inline.h
- vostok/animation/mixing_binary_tree_addition_node_inline.h
- vostok/animation/mixing_n_ary_tree.h
- vostok/animation/skeleton_bone.h
- vostok/animation/skeleton_inline.h
- vostok/animation/sources/interpolator_comparer.cpp
- vostok/animation/sources/mixing_n_ary_tree_weight_transition_node.h
- vostok/animation/sources/skeleton_bone.cpp
- vostok/animation/time_channel_inline.h
- vostok/associative_vector_inline.h
- vostok/c_array_functions.h
- vostok/collision/hit_targets_creation_utils_inline.h
- vostok/collision/sources/capsule_geometry_instance.cpp
- vostok/collision/sources/composite_geometry.cpp
- vostok/collision/sources/composite_geometry_instance.cpp
- vostok/collision/sources/containment_double_dispatcher_box.cpp
- vostok/collision/sources/containment_double_dispatcher_capsule.cpp
- vostok/collision/sources/containment_double_dispatcher_cylinder.cpp
- vostok/collision/sources/containment_double_dispatcher_sphere.cpp
- vostok/collision/sources/containment_double_dispatcher_truncated_sphere.cpp
- vostok/collision/sources/cylinder_geometry_instance.cpp
- vostok/collision/sources/intersection_double_dispatcher_box.cpp
- vostok/collision/sources/intersection_double_dispatcher_capsule.cpp
- vostok/collision/sources/intersection_double_dispatcher_cylinder.cpp
- vostok/collision/sources/intersection_double_dispatcher_sphere.cpp
- vostok/collision/sources/intersection_double_dispatcher_truncated_sphere.cpp
- vostok/collision/sources/terrain_data.cpp
- vostok/collision/sources/terrain_geometry_instance.cpp
- vostok/collision/sources/triangle_mesh_geometry_instance.cpp
- vostok/collision/sources/triangle_mesh_resource.cpp
- vostok/collision/sources/truncated_sphere_geometry_instance.cpp
- vostok/collision/terrain_collision_utils_inline.h
- vostok/configs_binary_config.h
- vostok/configs_binary_config_value.h
- vostok/configs_binary_config_value_inline.h
- vostok/console_command_inline.h
- vostok/core/sources/game_resman_data.h
- vostok/core/sources/math_convex.cpp
- vostok/core/sources/math_functions.cpp
- vostok/core/sources/memory_crt_allocator.cpp
- vostok/core/sources/resources_fs_task_composite.cpp
- vostok/core/sources/resources_fs_task_erase.cpp
- vostok/core/sources/resources_hdd_manager.h
- vostok/core/sources/resources_query_result_replication.cpp
- vostok/core/sources/threading_functions_win.cpp
- vostok/debug/macros.h
- vostok/debug/macros_inline.h
- vostok/debug/pointer_cast.h
- vostok/debug/sources/call_stack.h
- vostok/debug/sources/debug_win_xbox360.cpp
- vostok/debug/sources/initialize_win.cpp
- vostok/debug/static_cast_checked.h
- vostok/engine/sources/engine_world_build.cpp
- vostok/fixed_string.h
- vostok/fs/device_file_system_no_watcher.h
- vostok/fs/synchronous_device_interface.h
- vostok/game/sources/ai_sound_player.cpp
- vostok/game/sources/animation_controller_parameters.cpp
- vostok/game/sources/animation_space_graph.cpp
- vostok/game/sources/animation_space_graph.h
- vostok/game/sources/animation_space_graph_cook.cpp
- vostok/game/sources/animation_space_graph_wrapper_inline.h
- vostok/game/sources/animation_space_heuristics_inline.h
- vostok/game/sources/animations_search_service.cpp
- vostok/game/sources/animations_search_service.h
- vostok/game/sources/animations_selector.cpp
- vostok/game/sources/booby_trap_set.h
- vostok/game/sources/client_player_history_item.cpp
- vostok/game/sources/client_player_state.cpp
- vostok/game/sources/damage_model_stats.cpp
- vostok/game/sources/fingers_to_weapon_corrector.cpp
- vostok/game/sources/fingers_to_weapon_corrector.h
- vostok/game/sources/game_generate_shaders.cpp
- vostok/game/sources/game_generate_shaders.h
- vostok/game/sources/game_world_npc.cpp
- vostok/game/sources/human_npc.cpp
- vostok/game/sources/human_npc.h
- vostok/game/sources/human_npc_cook.cpp
- vostok/game/sources/lobby_menu_scene.cpp
- vostok/game/sources/main_menu.cpp
- vostok/game/sources/main_menu.h
- vostok/game/sources/main_menu_input.cpp
- vostok/game/sources/network_stats.cpp
- vostok/game/sources/network_stats.h
- vostok/game/sources/npc_stats.cpp
- vostok/game/sources/object_environment.cpp
- vostok/game/sources/object_sky.cpp
- vostok/game/sources/object_weapon.cpp
- vostok/game/sources/object_weapon.h
- vostok/game/sources/simple_animation_controller.cpp
- vostok/game/sources/single_position_animation_controller.cpp
- vostok/game/sources/sound_player_cook.cpp
- vostok/game/sources/victory_item.h
- vostok/game/sources/victory_item_cooker.cpp
- vostok/game/sources/weapon.h
- vostok/game_core/artefact_container_core.h
- vostok/game_core/artefact_lifebone_core.h
- vostok/game_core/breath_holding_params.h
- vostok/game_core/breath_vibration_calculator.h
- vostok/game_core/circular_buffer_inline.h
- vostok/game_core/collision_geometry_inline.h
- vostok/game_core/damage_model.h
- vostok/game_core/game_world_object.h
- vostok/game_core/hand_to_weapon_ik_processor.h
- vostok/game_core/ik_utils.h
- vostok/game_core/inventory.h
- vostok/game_core/inventory_holder.h
- vostok/game_core/material_pair.h
- vostok/game_core/normal_random.h
- vostok/game_core/player_death_subscriber.h
- vostok/game_core/player_parameters_cook.h
- vostok/game_core/sources/affects_threshold.cpp
- vostok/game_core/sources/animation_analyzer.cpp
- vostok/game_core/sources/character_dispersion_calculator.cpp
- vostok/game_core/sources/client_player_update.cpp
- vostok/game_core/sources/double_barreled_weapon_core_aimed_fire_state.cpp
- vostok/game_core/sources/double_barreled_weapon_core_aimed_idle_state.cpp
- vostok/game_core/sources/double_barreled_weapon_core_hide_state.cpp
- vostok/game_core/sources/double_barreled_weapon_core_show_state.cpp
- vostok/game_core/sources/entry_point.cpp
- vostok/game_core/sources/hand_to_weapon_ik_processor.cpp
- vostok/game_core/sources/ik_processor.cpp
- vostok/game_core/sources/jump_logic_state_inactive.cpp
- vostok/game_core/sources/jump_logic_state_inactive.h
- vostok/game_core/sources/legs_ik_drawer.cpp
- vostok/game_core/sources/legs_ik_processor.cpp
- vostok/game_core/sources/pistol_weapon_core_aimed_fire_state.cpp
- vostok/game_core/sources/pistol_weapon_core_aimed_idle_state.cpp
- vostok/game_core/sources/pistol_weapon_core_hide_state.cpp
- vostok/game_core/sources/pistol_weapon_core_show_state.cpp
- vostok/game_core/sources/player_parameters_cook.cpp
- vostok/game_core/sources/player_state.cpp
- vostok/game_core/sources/respawn_point.cpp
- vostok/game_core/sources/server_player_update.cpp
- vostok/game_core/sources/weapon_core_aimed_fire_state.cpp
- vostok/game_core/sources/weapon_core_aimed_fire_state_base.cpp
- vostok/game_core/sources/weapon_core_aimed_state.cpp
- vostok/game_core/sources/weapon_core_aimed_state_base.cpp
- vostok/game_core/sources/weapon_core_chamber_a_round_aimed_state.cpp
- vostok/game_core/sources/weapon_core_chamber_a_round_aimed_state_base.cpp
- vostok/game_core/sources/weapon_core_inactive_state.h
- vostok/game_core/sources/weapon_core_inactive_state_cook.cpp
- vostok/game_core/sources/weapon_core_shotgun_reload_state_cook.cpp
- vostok/game_core/sources/weapon_dispersion_calculator.cpp
- vostok/game_core/sources/weapon_lexeme_pair.cpp
- vostok/game_core/sources/weapon_state.cpp
- vostok/game_core/victory_items_container_core.h
- vostok/game_core/weapon_ammunition.h
- vostok/game_core/weapon_user_animations_selector.h
- vostok/input/sources/receiver_gamepad_win_xbox360.cpp
- vostok/input/sources/receiver_keyboard.cpp
- vostok/input/sources/receiver_keyboard_win.cpp
- vostok/input/sources/receiver_mouse.cpp
- vostok/input/sources/receiver_mouse_win.cpp
- vostok/intrusive_mpsc_queue_inline.h
- vostok/logging/format.h
- vostok/logging/sources/logging_filters_console_command.cpp
- vostok/math_constants.h
- vostok/math_curve.h
- vostok/math_extensions.h
- vostok/math_randoms_table_inline.h
- vostok/math_uint2_inline.h
- vostok/memory_allocator_helper.h
- vostok/memory_base_allocator.h
- vostok/memory_buffer.h
- vostok/memory_buffer_inline.h
- vostok/memory_debug.h
- vostok/memory_doug_lea_allocator.h
- vostok/memory_extensions.h
- vostok/memory_reader_inline.h
- vostok/memory_reader_wrapper_inline.h
- vostok/network/sources/functor_order.h
- vostok/network/sources/login_client_impl_sign_up.cpp
- vostok/network_core/base_packet.h
- vostok/network_core/http_client.h
- vostok/network_core/packet.h
- vostok/network_core/packet_inline.h
- vostok/network_core/packet_reader_inline.h
- vostok/network_core/sources/tcp_packet.cpp
- vostok/particle/sources/curve_line.cpp
- vostok/particle/sources/curve_line.h
- vostok/particle/sources/curve_line_inline.h
- vostok/particle/sources/evaluate_type.cpp
- vostok/particle/sources/particle_entry_point.cpp
- vostok/physics/bullet_utils.h
- vostok/platform_extensions.h
- vostok/platform_pointer.h
- vostok/render/core/dx11/custom_config_value_inline.h
- vostok/render/core/dx11/destroy_data_helper.h
- vostok/render/core/dx11/effect_manager.h
- vostok/render/core/dx11/effect_options_descriptor.h
- vostok/render/core/dx11/res_xs_hw.h
- vostok/render/core/dx11/sources/custom_config.cpp
- vostok/render/core/dx11/sources/custom_config_value.cpp
- vostok/render/core/dx11/sources/decl_utils.cpp
- vostok/render/core/dx11/sources/effect_descriptor.cpp
- vostok/render/core/dx11/sources/effect_options_descriptor.cpp
- vostok/render/core/dx11/sources/render_core_entry_point.cpp
- vostok/render/core/dx11/sources/res_gs_hw.cpp
- vostok/render/core/dx11/sources/res_ps_hw.cpp
- vostok/render/core/dx11/sources/res_signature.cpp
- vostok/render/core/dx11/sources/res_state.cpp
- vostok/render/core/dx11/sources/texture_storage.cpp
- vostok/render/core/res_xs.h
- vostok/render/core/static_type.h
- vostok/render/core/utils_inline.h
- vostok/render/engine/sources/camera_inline.h
- vostok/render/engine/sources/cloud_noise.cpp
- vostok/render/engine/sources/effect_aberration.cpp
- vostok/render/engine/sources/effect_apply_indirect_lighting.cpp
- vostok/render/engine/sources/effect_atmospheric_scattering.cpp
- vostok/render/engine/sources/effect_clouds.cpp
- vostok/render/engine/sources/effect_clouds_god_rays.cpp
- vostok/render/engine/sources/effect_downsample_gbuffer.cpp
- vostok/render/engine/sources/effect_downsample_reflective_shadow_map.cpp
- vostok/render/engine/sources/effect_editor_gbuffer_to_screen.cpp
- vostok/render/engine/sources/effect_forward_system.cpp
- vostok/render/engine/sources/effect_light_propagation_volumes.cpp
- vostok/render/engine/sources/effect_read_cloud_base.cpp
- vostok/render/engine/sources/effect_resolve_lighting.cpp
- vostok/render/engine/sources/effect_speedtree_selection.cpp
- vostok/render/engine/sources/effect_sun.cpp
- vostok/render/engine/sources/effect_translucency.cpp
- vostok/render/engine/sources/grass_instance.cpp
- vostok/render/engine/sources/grass_template.cpp
- vostok/render/engine/sources/help_math.h
- vostok/render/engine/sources/material_manager.cpp
- vostok/render/engine/sources/post_process_parameters.cpp
- vostok/render/engine/sources/radiance_volume.cpp
- vostok/render/engine/sources/renderer_probes_and_ao.cpp
- vostok/render/engine/sources/sky_default_material_effect.cpp
- vostok/render/engine/sources/speedtree.cpp
- vostok/render/engine/sources/speedtree_convert_type.cpp
- vostok/render/engine/sources/speedtree_cook.cpp
- vostok/render/engine/sources/speedtree_forest.cpp
- vostok/render/engine/sources/speedtree_instance_impl.cpp
- vostok/render/engine/sources/speedtree_shader_parameters.cpp
- vostok/render/engine/sources/speedtree_tree.cpp
- vostok/render/engine/sources/speedtree_tree.h
- vostok/render/engine/sources/speedtree_tree_component_billboard.cpp
- vostok/render/engine/sources/speedtree_tree_component_billboard.h
- vostok/render/engine/sources/speedtree_tree_component_branch.cpp
- vostok/render/engine/sources/speedtree_tree_component_branch.h
- vostok/render/engine/sources/speedtree_tree_component_frond.cpp
- vostok/render/engine/sources/speedtree_tree_component_frond.h
- vostok/render/engine/sources/speedtree_tree_component_leafcard.cpp
- vostok/render/engine/sources/speedtree_tree_component_leafcard.h
- vostok/render/engine/sources/speedtree_tree_component_leafmesh.cpp
- vostok/render/engine/sources/speedtree_tree_component_leafmesh.h
- vostok/render/engine/sources/stage_clouds.cpp
- vostok/render/engine/sources/stage_light_propagation_volumes.cpp
- vostok/render/engine/sources/stage_pre_lighting.cpp
- vostok/render/engine/sources/stage_resolve_lighting.cpp
- vostok/render/engine/sources/stage_sun.cpp
- vostok/render/engine/sources/stage_translucency.cpp
- vostok/render/facade/cloud_key_inline.h
- vostok/render/facade/sources/engine_renderer.cpp
- vostok/render/facade/sources/update_model_vertex_buffer_command.cpp
- vostok/render/facade/volume_fog_parameters.h
- vostok/resources.h
- vostok/resources_memory_usage.h
- vostok/resources_queries_result.h
- vostok/resources_resource_base.h
- vostok/resources_resource_children.h
- vostok/resources_unmanaged_resource.h
- vostok/size_policies.h
- vostok/sound/single_sound.h
- vostok/sound/sources/encoded_sound_interface.cpp
- vostok/sound/sources/graph_heuristics.h
- vostok/sound/sources/graph_wrapper.h
- vostok/sound/sources/panning_lut_cook.cpp
- vostok/sound/sources/search_restrictor.h
- vostok/sound/sources/search_service.cpp
- vostok/sound/sources/search_service.h
- vostok/sound/sources/sound_buffer.h
- vostok/sound/sources/sound_producer.cpp
- vostok/sound/sources/sound_receiver.cpp
- vostok/sound/sources/sound_scene_path_computation.cpp
- vostok/sound/sources/sound_spl.cpp
- vostok/sound/sources/sound_world.h
- vostok/sound/sources/sound_world_orders.cpp
- vostok/stdlib_extensions.h
- vostok/strings_concatenations.h
- vostok/strings_detail_tuples.h
- vostok/threading_event.h
- vostok/threading_mutex.h
- vostok/threading_policies.h
- vostok/threading_reader_writer_lock.h
- vostok/type_enum_flags.h
- vostok/ui/sources/ui_entry_point.cpp
- vostok/uninitialized_reference.h
- vostok/vector_inline.h
- vostok/vectora.h
- vostok/vectora_inline.h
- vostok/vfs/association.h
- vostok/vfs/iterator.h
- vostok/vfs/locked_iterator.h
- vostok/vfs/sources/archive_compressed_file_node.h
- vostok/vfs/sources/archive_file_node.h
- vostok/vfs/sources/archive_folder_mount_root_node.h
- vostok/vfs/sources/archive_inline_compressed_file_node.h
- vostok/vfs/sources/archive_inline_file_node.h
- vostok/vfs/sources/external_subfat_node.h
- vostok/vfs/sources/fat_header.cpp
- vostok/vfs/sources/find_environment.h
- vostok/vfs/sources/hard_link_node.h
- vostok/vfs/sources/mount_helper_node.h
- vostok/vfs/sources/mount_referers.h
- vostok/vfs/sources/mounter.h
- vostok/vfs/sources/pack_archive_utils.cpp
- vostok/vfs/sources/test.cpp
- vostok/vfs/sources/test_find.cpp
- vostok/vfs/sources/test_log.cpp
- vostok/vfs/sources/test_utils.cpp
- vostok/vfs/sources/universal_file_node.h
