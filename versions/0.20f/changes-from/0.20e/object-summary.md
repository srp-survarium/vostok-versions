# v0.20e-build1916 -> v0.20f-build1923

Lists below: **hand-written engine** (`vostok/*`, compiler-generated excluded). Full breakdown:

| bucket | engine | generated | third-party |
| --- | ---: | ---: | ---: |
| identical | **9986** | 1645 | 6697 |
| changed | **2** | 0 | 0 |
| new / rewritten | **39** | 118 | 300 |
| units removed | **1** | - | 2 |

## Most-changed engine functions (2 shown)

| match % | unit | function |
| ---: | --- | --- |
| 99.97 | vostok/network/sources/network_world.cpp | `public: virtual void __thiscall vostok::network::network_world::dispatch_callbacks(void)` |
| 99.97 | vostok/render/engine/sources/stage_shadow_direct.cpp | `public: void __thiscall vostok::render::stage_shadow_direct::prepare_visibile_objects(class vostok::fixed_vector<struct vostok::render::caster_model, 2048> *, class vostok::memory::base_allocator *, class vostok::math::float3const &, unsigned int, unsigned int, unsigned int)` |

## Engine units in base but gone in target

- vostok/engine/sources/apc.h
