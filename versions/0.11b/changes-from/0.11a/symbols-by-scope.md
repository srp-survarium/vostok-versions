# Build v0.11b-build826  —  what most likely changed

_vs v0.11a-build816 · 2013-05-14 → 2013-05-14_

From **added/deleted hand-written engine functions only** (+19 / −26), grouped by owning class/namespace. Added/deleted are clear non-drift signal; fuzzy `changed` is excluded.

## Likely changes at a glance

- **New (1):** `vostok::particle::lod_entry`
- **Removed (6):** `vostok::render::streaming_ready_texture`, `vostok::render::render_target_instance`, `vostok::render::requested_streamable_texture`, `vostok::render::speedtree_data`, `vostok::render::streamable_texture_info`, `survarium::animated_model_instance`
- **Reworked (17):** `survarium::game`, `vostok::console_commands`, `vostok::render::backend`, `vostok::render::shader_constant_buffer`, `survarium::weapon_core`, `vostok::render::constants_handler<0>`, `vostok::render::constants_handler<1>`, `vostok::vectora<struct vostok::resources::request>`, `vostok::ai::selectors::sound_target_selector`, `vostok::particle::particle_system_instance`, `vostok::render::stage_postprocess`, `vostok::resources::fs_task_unmount` _+5 more_

---

## 🟡 REWORKED · `survarium::game` (+3 / −5)

- `+` `load_cc_script(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>, bool, bool)`
- `+` `load_config_query(char const *, bool, bool)`
- `+` `on_config_loaded(class vostok::resources::queries_result &, bool, bool)`
- `−` `load_cc_script(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>, bool)`
- `−` `load_cmd(char const *)`
- `−` `load_config_query(char const *, bool)`
- `−` `on_config_loaded(class vostok::resources::queries_result &, bool)`
- `−` `unload_cmd(char const *)`

---

## 🟡 REWORKED · `vostok::console_commands` (+3 / −3)

- `+` `execute(char const *, enum vostok::console_commands::execution_filter, bool)`
- `+` `execute_console_commands(class vostok::fs_new::native_path_string, enum vostok::console_commands::execution_filter, bool)`
- `+` `load(class vostok::memory::reader &, enum vostok::console_commands::execution_filter, bool)`
- `−` `execute(char const *, enum vostok::console_commands::execution_filter)`
- `−` `execute_console_commands(class vostok::fs_new::native_path_string, enum vostok::console_commands::execution_filter)`
- `−` `load(class vostok::memory::reader &, enum vostok::console_commands::execution_filter)`

---

## 🟡 REWORKED · `vostok::render::backend` (+3 / −1)

- `+` `set_gs_constant<float>(class vostok::render::shader_constant_host const *, float const &)`
- `+` `set_ps_constant<class vostok::math::float4>(class vostok::render::shader_constant_host const *, class vostok::math::float4const *, unsigned int)`
- `+` `set_vs_constant<float>(class vostok::render::shader_constant_host const *, float const &)`
- `−` `set_vs_constant<class vostok::math::float4>(class vostok::render::shader_constant_host const *, class vostok::math::float4const &)`

---

## 🟡 REWORKED · `vostok::render::shader_constant_buffer` (+2 / −1)

- `+` `set_typed<class vostok::math::float4>(class vostok::render::shader_constant_slot const &, class vostok::math::float4const *, unsigned int)`
- `+` `set_typed<int>(class vostok::render::shader_constant_slot const &, int const &)`
- `−` `set_memory(unsigned int, char const *, unsigned int)`

---

## 🟡 REWORKED · `survarium::weapon_core` (+2)

- `+` `idle_AE_or_chamber_a_round_break_pred(void) const`
- `+` `reload_break_pred(void) const`

---

## 🟡 REWORKED · `vostok::render::constants_handler<0>` (+0 / −2)

- `−` `set_constant<class vostok::math::float3>(class vostok::render::shader_constant_host const &, class vostok::math::float3const &)`
- `−` `set_constant_array<class vostok::math::float4>(class vostok::render::shader_constant_host const &, class vostok::math::float4const *, unsigned int)`

---

## 🟡 REWORKED · `vostok::render::constants_handler<1>` (+0 / −2)

- `−` `set_constant<int>(class vostok::render::shader_constant_host const &, int const &)`
- `−` `set_constant_array<class vostok::math::float4>(class vostok::render::shader_constant_host const &, class vostok::math::float4const *, unsigned int)`

---

## 🔴 REMOVED · `vostok::render::streaming_ready_texture` (+0 / −2)

- `−` `operator=(struct vostok::render::streaming_ready_texture const &)`
- `−` `streaming_ready_texture(struct vostok::render::streaming_ready_texture const &)`

---

## 🟢 NEW · `vostok::particle::lod_entry` (+1)

- `+` `~lod_entry(void)`

---

## 🟡 REWORKED · `vostok::vectora<struct vostok::resources::request>` (+1)

- `+` `~vectora<struct vostok::resources::request>(void)`

---

## 🟡 REWORKED · `vostok::ai::selectors::sound_target_selector` (+1)

- `+` `~sound_target_selector(void)`

---

## 🟡 REWORKED · `vostok::particle::particle_system_instance` (+1)

- `+` `~particle_system_instance(void)`

---

## 🟡 REWORKED · `vostok::render::stage_postprocess` (+1)

- `+` `~stage_postprocess(void)`

---

## 🟡 REWORKED · `vostok::resources::fs_task_unmount` (+1)

- `+` `~fs_task_unmount(void)`

---

## 🟡 REWORKED · `vostok::render::constants_handler<2>` (+0 / −1)

- `−` `set_constant<class vostok::math::float3>(class vostok::render::shader_constant_host const &, class vostok::math::float3const &)`

---

## 🟡 REWORKED · `vostok::detail::abstract_type_helper` (+0 / −1)

- `−` `abstract_type_helper(void)`

---

## 🟡 REWORKED · `vostok::render::geometry_batch` (+0 / −1)

- `−` `~geometry_batch(void)`

---

## 🔴 REMOVED · `vostok::render::render_target_instance` (+0 / −1)

- `−` `render_target_instance(void)`

---

## 🔴 REMOVED · `vostok::render::requested_streamable_texture` (+0 / −1)

- `−` `requested_streamable_texture(struct vostok::render::requested_streamable_texture const &)`

---

## 🔴 REMOVED · `vostok::render::speedtree_data` (+0 / −1)

- `−` `speedtree_data(void)`

---

## 🔴 REMOVED · `vostok::render::streamable_texture_info` (+0 / −1)

- `−` `streamable_texture_info(struct vostok::render::streamable_texture_info const &)`

---

## 🟡 REWORKED · `vostok::threading::mutex` (+0 / −1)

- `−` `~mutex(void)`

---

## 🔴 REMOVED · `survarium::animated_model_instance` (+0 / −1)

- `−` `~animated_model_instance(void)`

---

## 🟡 REWORKED · `survarium::player_logic_sprint_state` (+0 / −1)

- `−` `~player_logic_sprint_state(void)`

