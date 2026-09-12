# v0.1.1a-build816 -> v0.1.1b-build826

Lists below: **hand-written engine** (`vostok/*`, compiler-generated excluded). Full breakdown:

| bucket | engine | generated | third-party |
| --- | ---: | ---: | ---: |
| identical | **12481** | 1388 | 10480 |
| changed | **264** | 22 | 9 |
| new / rewritten | **95** | 227 | 409 |
| units removed | **4** | - | 3 |

## Most-changed engine functions (50 shown)

| match % | unit | function |
| ---: | --- | --- |
| 6.08 | vostok/game/sources/game_project.cpp | `public: class survarium::victory_items_container_core * __thiscall survarium::simple_game_project::get_items_container(unsigned char)` |
| 9.96 | vostok/game/sources/game.cpp | `private: void __thiscall survarium::game::register_console_commands(void)` |
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
| 16.09 | vostok/render/core/dx11/sources/backend_handlers.cpp | `private: void __thiscall vostok::render::constants_handler<1>::update_buffers(void)` |
| 16.09 | vostok/render/core/dx11/sources/backend_handlers.cpp | `private: void __thiscall vostok::render::constants_handler<1>::update_buffers(void)` |
| 16.09 | vostok/render/core/dx11/sources/backend_handlers.cpp | `private: void __thiscall vostok::render::constants_handler<1>::update_buffers(void)` |
| 23.90 | vostok/render/core/dx11/sources/shader_constant_buffer.cpp | `public: void __thiscall vostok::render::shader_constant_buffer::update(void)` |
| 24.99 | vostok/render/engine/sources/stage_lights.cpp | `private: void __thiscall vostok::render::stage_lights::render_particle_lighting(class vostok::render::render_particle_emitter_instance *, class vostok::render::light *, unsigned int)` |
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
| 28.38 | vostok/render/engine/sources/radiance_volume.cpp | `public: void __thiscall vostok::render::radiance_volume::inject_camera_occluders(class vostok::render::renderer_context *)` |
| 29.48 | vostok/render/engine/sources/stage_lights.cpp | `private: void __thiscall vostok::render::stage_lights::render_model_lighting(struct vostok::render::render_surface_instance *, class vostok::render::light *)` |
| 31.50 | vostok/render/core/dx11/backend_inline.h | `public: void __thiscall vostok::render::backend::set_ps_constant<unsigned int>(class vostok::render::shader_constant_host const *, unsigned int const &)` |
| 31.50 | vostok/render/core/dx11/backend_inline.h | `public: void __thiscall vostok::render::backend::set_ps_constant<unsigned int>(class vostok::render::shader_constant_host const *, unsigned int const &)` |
| 31.50 | vostok/render/core/dx11/backend_inline.h | `public: void __thiscall vostok::render::backend::set_ps_constant<unsigned int>(class vostok::render::shader_constant_host const *, unsigned int const &)` |
| 31.50 | vostok/render/core/dx11/backend_inline.h | `public: void __thiscall vostok::render::backend::set_ps_constant<unsigned int>(class vostok::render::shader_constant_host const *, unsigned int const &)` |
| 31.50 | vostok/render/core/dx11/backend_inline.h | `public: void __thiscall vostok::render::backend::set_ps_constant<unsigned int>(class vostok::render::shader_constant_host const *, unsigned int const &)` |
| 34.20 | vostok/render/engine/sources/stage_lights.cpp | `private: void __thiscall vostok::render::stage_lights::render_speedtree_lighting(struct vostok::render::lod_entry const *, class SpeedTree::CInstance const *, struct SpeedTree::SInstanceLod const *, class vostok::render::speedtree_tree_component *, class vostok::render::light *)` |
| 34.68 | vostok/render/engine/sources/grass_world.cpp | `public: void __thiscall vostok::render::grass_world::set_trample_parameters(struct vostok::render::trample_desc &)` |
| 35.79 | vostok/render/engine/sources/system_renderer.cpp | `public: void __thiscall vostok::render::system_renderer::draw_triangles(struct vostok::render::vertex_colored const *const, struct vostok::render::vertex_colored const *const, unsigned short const *const, unsigned short const *const, bool)` |
| 37.90 | vostok/game_core/sources/weapon_core.cpp | `private: bool __thiscall survarium::weapon_core::chamber_a_round_on_reload_break_pred(void) const` |
| 38.32 | vostok/render/engine/sources/radiance_volume.cpp | `public: void __thiscall vostok::render::radiance_volume::propagate_lighting_iter(unsigned int, unsigned int)` |
| 40.29 | vostok/render/engine/sources/stage_lights.cpp | `private: void __thiscall vostok::render::stage_lights::render_light(class vostok::render::light *, bool)` |
| 42.34 | vostok/render/engine/sources/render_model_skeleton.cpp | `public: virtual void __thiscall vostok::render::skeleton_render_model_instance::set_constants(void)` |
| 42.73 | vostok/render/engine/sources/stage_ambient_lighting.cpp | `public: virtual void __thiscall vostok::render::stage_ambient_lighting::execute(void)` |
| 45.14 | vostok/render/engine/sources/stage_postprocess.cpp | `public: void __thiscall vostok::render::scene_shader_constants::set(class vostok::render::renderer_context *, class vostok::math::float3const &, class vostok::math::float3const &, class vostok::math::float3const &, class vostok::math::float3const &, float, float, float, class vostok::math::float4const &, struct vostok::render::post_process_parameters const &)` |
| 46.13 | vostok/render/engine/sources/decal_instance.cpp | `public: void __thiscall vostok::render::decal_shader_constants_and_geometry::set(class vostok::render::renderer_context *, class vostok::math::float4x4const &, class vostok::math::float4x4const &, float, float, class vostok::math::float3const &, class vostok::math::float4x4const &)` |
| 50.52 | vostok/render/engine/sources/renderer_context.cpp | `public: void __thiscall vostok::render::renderer_context::set_v(class vostok::math::float4x4const &)` |
| 50.89 | vostok/render/engine/sources/stage_particles.cpp | `public: void __thiscall vostok::render::particle_shader_constants::set_time(float)` |

## Engine units in base but gone in target

- vostok/ai/fsm_state.h
- vostok/core/engine.h
- vostok/render/core/dx11/backend_handlers_inline.h
- vostok/render/facade/base_command.h
