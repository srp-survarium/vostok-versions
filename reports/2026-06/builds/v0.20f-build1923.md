# Build v0.20f-build1923  —  what most likely changed

_vs v0.20e-build1916 · 2014-03-20 → 2014-04-01_

From **added/deleted hand-written engine functions only** (+1 / −3), grouped by owning class/namespace. Added/deleted are clear non-drift signal; fuzzy `changed` is excluded.

## Likely changes at a glance

- **New (1):** ``vostok::render::stage_lights::accumulate_particle_lighting'::`6'::sort_probes_by_size_predicate`
- **Removed (2):** ``vostok::render::stage_visibility::filter_and_sort_env_probes'::`4'::sort_by_size_predicate`, `vostok::fixed_vector<class vostok::intrusive_ptr<class vostok::render::shader_buffer, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, 32>`
- **Reworked (1):** `(global)`

---

## 🟢 NEW · ``vostok::render::stage_lights::accumulate_particle_lighting'::`6'::sort_probes_by_size_predicate` (+1)

- `+` `operator()`

---

## 🔴 REMOVED · ``vostok::render::stage_visibility::filter_and_sort_env_probes'::`4'::sort_by_size_predicate` (+0 / −1)

- `−` `operator()`

---

## 🟡 REWORKED · `(global)` (+0 / −1)

- `−` `(class vostok::resources::queries_result &)> > > > const &)`

---

## 🔴 REMOVED · `vostok::fixed_vector<class vostok::intrusive_ptr<class vostok::render::shader_buffer, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, 32>` (+0 / −1)

- `−` `~fixed_vector<class vostok::intrusive_ptr<class vostok::render::shader_buffer, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, 32>(void)`

