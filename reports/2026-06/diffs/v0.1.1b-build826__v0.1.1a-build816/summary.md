# v0.1.1b-build826 -> v0.1.1a-build816

Lists below: **hand-written engine** (`vostok/*`, compiler-generated excluded). Full breakdown:

| bucket | engine | generated | third-party |
| --- | ---: | ---: | ---: |
| identical | **12481** | 1388 | 10480 |
| changed | **256** | 22 | 9 |
| new / rewritten | **110** | 151 | 524 |
| units removed | **2** | - | 1 |

## Most-changed engine functions (50 shown)

| match % | unit | function |
| ---: | --- | --- |
| 11.05 | vostok/render/engine/sources/decal_instance.cpp | `public: void __thiscall vostok::render::decal_shader_constants_and_geometry::set(class vostok::render::renderer_context *, class vostok::math::float4x4const &, class vostok::math::float4x4const &, float, float, class vostok::math::float3const &, class vostok::math::float4x4const &)` |
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
| 13.91 | vostok/render/engine/sources/renderer_context.cpp | `public: void __thiscall vostok::render::renderer_context::set_w(class vostok::math::float4x4const &)` |
| 18.91 | vostok/render/engine/sources/renderer_context.cpp | `public: void __thiscall vostok::render::renderer_context::set_v(class vostok::math::float4x4const &)` |
| 19.77 | vostok/render/engine/sources/stage_postprocess.cpp | `public: void __thiscall vostok::render::scene_shader_constants::set(class vostok::render::renderer_context *, class vostok::math::float3const &, class vostok::math::float3const &, class vostok::math::float3const &, class vostok::math::float3const &, float, float, float, class vostok::math::float4const &, struct vostok::render::post_process_parameters const &)` |
| 20.68 | vostok/render/engine/sources/stage_lights.cpp | `private: void __thiscall vostok::render::stage_lights::draw_geometry(class vostok::render::light *)` |
| 24.83 | vostok/render/engine/sources/stage_light_propagation_volumes.cpp | `private: void __thiscall vostok::render::stage_light_propagation_volumes::set_rsm_contants(class vostok::math::float3const &, class vostok::math::float3const &, float)` |
| 26.25 | vostok/render/engine/sources/stage_particles.cpp | `public: void __thiscall vostok::render::particle_shader_constants::set_time(float)` |
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
| 29.64 | vostok/render/engine/sources/renderer_context.cpp | `public: void __thiscall vostok::render::renderer_context::set_p(class vostok::math::float4x4const &)` |
| 32.18 | vostok/render/engine/sources/stage_light_propagation_volumes.cpp | `private: void __thiscall vostok::render::stage_light_propagation_volumes::pre_lpv_batch_render(class vostok::math::float3const &, float, struct vostok::render::geometry_batch const &)` |
| 32.57 | vostok/render/engine/sources/stage_postprocess.cpp | `public: void __thiscall vostok::render::dof_shader_constants::set(class vostok::math::float3const &, float, float, float, float, float, float, float)` |
| 34.44 | vostok/render/engine/sources/grass_world.cpp | `public: void __thiscall vostok::render::grass_world::set_shadow_parameters(unsigned int)` |
| 35.79 | vostok/render/engine/sources/stage_particles.cpp | `public: void __thiscall vostok::render::particle_shader_constants::set(class vostok::math::float3, class vostok::math::float3, class vostok::math::float3, enum vostok::particle::enum_particle_locked_axis, enum vostok::particle::enum_particle_screen_alignment)` |
| 36.95 | vostok/render/engine/sources/speedtree_shader_parameters.cpp | `public: void __thiscall vostok::render::speedtree_wind_parameters::set(class SpeedTree::CWind const &)` |
| 39.14 | vostok/render/engine/sources/speedtree_shader_parameters.cpp | `public: void __thiscall vostok::render::speedtree_tree_parameters::set(class vostok::render::speedtree_tree_component *, class SpeedTree::CInstance const *, struct SpeedTree::SInstanceLod const *)` |
| 43.11 | vostok/render/engine/sources/radiance_volume.cpp | `public: void __thiscall vostok::render::radiance_volume::inject_lighting(class vostok::math::float3const &, class vostok::math::float3const &, float, unsigned int)` |
| 43.59 | vostok/render/engine/sources/stage_lights.cpp | `private: void __thiscall vostok::render::stage_lights::render_particle_lighting(class vostok::render::render_particle_emitter_instance *, class vostok::render::light *, unsigned int)` |
| 45.20 | vostok/render/engine/sources/stage_ambient_lighting.cpp | `public: virtual void __thiscall vostok::render::stage_ambient_lighting::execute(void)` |
| 47.64 | vostok/render/engine/sources/grass_world.cpp | `public: void __thiscall vostok::render::grass_world::set_wind_parameters(class vostok::math::float2const &, float)` |
| 47.91 | vostok/render/engine/sources/speedtree_shader_parameters.cpp | `public: void __thiscall vostok::render::speedtree_billboard_parameters::set(class vostok::render::renderer_context *, class vostok::render::speedtree_tree_component *)` |
| 49.17 | vostok/render/engine/sources/grass_world.cpp | `public: void __thiscall vostok::render::grass_world::set_patch_parameters(struct vostok::render::grass_patch *)` |
| 49.64 | vostok/render/engine/sources/radiance_volume.cpp | `public: void __thiscall vostok::render::radiance_volume::propagate_lighting_iter(unsigned int, unsigned int)` |
| 50.07 | vostok/render/engine/sources/stage_postprocess.cpp | `public: void __thiscall vostok::render::bloom_shader_constants::set(float, float, class vostok::math::float3const &)` |
| 51.38 | vostok/game/sources/game.cpp | `private: void __thiscall survarium::game::register_console_commands(void)` |
| 51.86 | vostok/render/engine/sources/speedtree_shader_parameters.cpp | `public: void __thiscall vostok::render::speedtree_common_parameters::set(class vostok::render::renderer_context *, class vostok::render::speedtree_tree_component *, class vostok::math::float3const &)` |
| 52.94 | vostok/render/engine/sources/stage_lights.cpp | `private: void __thiscall vostok::render::stage_lights::render_model_lighting(struct vostok::render::render_surface_instance *, class vostok::render::light *)` |
| 53.18 | vostok/render/engine/sources/radiance_volume.cpp | `public: void __thiscall vostok::render::radiance_volume::inject_camera_occluders(class vostok::render::renderer_context *)` |

## Engine units in base but gone in target

- vostok/core_debug_engine.h
- vostok/engine/sources/apc.h
