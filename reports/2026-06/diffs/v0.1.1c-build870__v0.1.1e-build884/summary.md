# v0.1.1c-build870 -> v0.1.1e-build884

Lists below: **hand-written engine** (`vostok/*`, compiler-generated excluded). Full breakdown:

| bucket | engine | generated | third-party |
| --- | ---: | ---: | ---: |
| identical | **12289** | 1443 | 10427 |
| changed | **463** | 1 | 9 |
| new / rewritten | **67** | 149 | 440 |
| units removed | **1** | - | 1 |

## Most-changed engine functions (50 shown)

| match % | unit | function |
| ---: | --- | --- |
| 2.05 | vostok/render/engine/sources/system_renderer.cpp | `public: void __thiscall vostok::render::system_renderer::draw_screen_lines(class vostok::math::float3const *, unsigned int, class vostok::math::color const &, float, unsigned int, bool, bool)` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.77 | vostok/render/engine/sources/stage_shadow_direct.cpp | `public: bool __thiscall vostok::render::remove_inappropriate_models::operator()(struct vostok::render::render_surface_instance *)` |
| 13.45 | vostok/render/engine/sources/renderer.cpp | `vostok::render::screen_factor` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 33.66 | vostok/game_core/sources/medkit.cpp | `private: __thiscall survarium::medkit::medkit(void)` |
| 53.74 | vostok/core/sources/resources_manager_new_queries.cpp | `public: void __thiscall vostok::resources::resources_manager::init_new_query(class vostok::resources::query_result &)` |
| 57.50 | vostok/intrusive_list_inline.h | `public: void __thiscall vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 608, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::push_back(class vostok::resources::query_result *, bool *)` |
| 60.23 | vostok/core/sources/resources_query_result_finalization.cpp | `public: virtual __thiscall vostok::resources::query_result_for_user::~query_result_for_user(void)` |
| 63.37 | vostok/game/sources/network_client_lobby.cpp | `private: virtual void __thiscall survarium::network_client::close_current_match(enum vostok::network_core::disconnect_event_types_enum)` |
| 73.70 | vostok/game_core/sources/damage_zone_core.cpp | `public: virtual float __thiscall survarium::dz_bone_data_contact_test_predicate::add_single_result(void *, enum vostok::physics::primitive_type, class vostok::math::float4x4const &, class vostok::math::float3const &, enum vostok::physics::primitive_type, class vostok::math::float4x4const &, class vostok::math::float3const &)` |
| 77.34 | vostok/render/core/dx11/sources/device.cpp | `private: void __thiscall vostok::render::device::create_d3d(void)` |
| 79.82 | vostok/game/sources/lobby_menu_ui.cpp | `public: void __thiscall survarium::lobby_menu::on_player_reputations_arrived(void)` |
| 83.83 | vostok/survarium/pc/sources/survarium_pc_application_win.cpp | `private: void __thiscall survarium::application::preinitialize(void)` |
| 84.42 | vostok/render/engine/sources/stage_postprocess.cpp | `public: virtual void __thiscall vostok::render::stage_postprocess::execute(void)` |
| 85.24 | vostok/render/engine/sources/stage_shadow_direct.cpp | `public: virtual void __thiscall vostok::render::stage_shadow_direct::execute(void)` |
| 89.17 | vostok/core/sources/resources_query_result_initialization.cpp | `public: __thiscall vostok::resources::query_result_for_user::query_result_for_user(void)` |
| 90.08 | vostok/render/engine/sources/render_engine_world_pc_dx11.cpp | `public: __thiscall vostok::render::renderer_context::~renderer_context(void)` |
| 90.10 | vostok/render/core/dx11/sources/options.cpp | `public: enum vostok::render::enum_options_changes_result __thiscall vostok::render::options::end_render_options_changing(class vostok::render::vector<class vostok::fs_new::virtual_path_string> &)` |
| 91.57 | vostok/render/facade/sources/game_renderer.cpp | `private: void __thiscall vostok::render::game::renderer::draw_scene_impl(struct vostok::render::game::renderer::draw_scene_params const &)` |
| 92.68 | vostok/render/engine/sources/renderer_context.cpp | `public: __thiscall vostok::render::renderer_context::renderer_context(void)` |
| 93.24 | vostok/game_core/sources/medkit.cpp | `private: virtual __thiscall survarium::medkit::~medkit(void)` |
| 93.40 | vostok/render/engine/sources/render_engine_world_pc_dx11.cpp | `public: void __thiscall vostok::render::engine::world::draw_scene(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct vostok::render::base_scene_view, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct vostok::render::base_output_window, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::rectangle<class vostok::math::float2> const &, class boost::function<void __cdecl (bool)> const &, struct vostok::ui::font const *)` |
| 94.75 | vostok/render/engine/sources/renderer.cpp | `public: void __thiscall vostok::render::renderer::render(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct vostok::render::base_scene_view, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct vostok::render::base_output_window, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::rectangle<class vostok::math::float2> const &, class boost::function<void __cdecl (bool)> const &, bool, struct vostok::ui::font const *)` |
| 95.08 | vostok/render/core/dx11/sources/options.cpp | `public: void __thiscall vostok::render::options::set_default_values(void)` |
| 95.41 | vostok/game/sources/player.cpp | `private: void __thiscall survarium::player::detect_usable_objects(unsigned int)` |
| 95.56 | vostok/render/core/dx11/sources/options.cpp | `public: void __thiscall vostok::render::options::register_console_commands(void)` |
| 95.99 | vostok/render/engine/sources/system_renderer.cpp | `public: void __thiscall vostok::render::system_renderer::draw_ui_vertices(struct vostok::render::vertex_formats::TL const *, unsigned int const &, int, int)` |
| 96.25 | vostok/render/engine/sources/render_particle_emitter_instance.cpp | `public: void __thiscall vostok::render::render_particle_emitter_instance::draw_debug(class vostok::math::float4x4const &, enum vostok::particle::enum_particle_render_mode)` |
| 97.23 | vostok/core/sources/resources_manager_new_queries.cpp | `public: void __thiscall vostok::resources::resources_manager::init_new_queries(class vostok::resources::query_result *)` |
| 98.57 | vostok/game/sources/game_world_ui.cpp | `public: void __thiscall survarium::game_world_ui::set_match_time(unsigned int)` |
| 99.01 | vostok/render/core/dx11/sources/device.cpp | `private: void __thiscall vostok::render::device::create(void)` |
| 99.38 | vostok/render/engine/sources/renderer_context.cpp | `private: void __thiscall vostok::render::renderer_context::update_near_far(void)` |
| 99.44 | vostok/core/sources/resources_query_result_initialization.cpp | `public: __thiscall vostok::resources::query_result_for_cook::query_result_for_cook(class vostok::resources::queries_result *)` |
| 99.50 | vostok/core/sources/resources_query_result.cpp | `private: void __thiscall vostok::resources::query_result::add_loaded_bytes(unsigned int)` |
| 99.50 | vostok/render/engine/sources/renderer_context.cpp | `public: void __thiscall vostok::render::renderer_context::set_scene(class vostok::render::scene *)` |

## Engine units in base but gone in target

- vostok/core/engine.h
