# Build v0.11a-build816  —  what most likely changed

_vs v0.10b-build802 · 2013-05-09 → 2013-05-14_

From **added/deleted hand-written engine functions only** (+88 / −56), grouped by owning class/namespace. Added/deleted are clear non-drift signal; fuzzy `changed` is excluded.

## Likely changes at a glance

- **New (7):** `survarium::character_dispersion_skill_influence`, `vostok::render::streaming_ready_texture`, `survarium::game_scene`, `vostok::render::requested_streamable_texture`, `vostok::render::speedtree_data`, `vostok::render::streamable_texture_info`, `survarium::animated_model_instance`
- **Removed (6):** `vostok::sound::sound_rms_cook`, `vostok::sound::sound_rms`, `vostok::resources::pinned_ptr_base<class vostok::sound::sound_rms>`, `vostok::particle::lod_entry`, `vostok::resources::resource_ptr<class vostok::sound::encoded_sound_with_qualities, class vostok::resources::unmanaged_intrusive_base>`, `vostok::sound::sound_rms_pinned`
- **Reworked (27):** `survarium::weapon_core`, `survarium::weapon_user_animations_selector`, `survarium::swf_input_translator`, `survarium::weapon`, `vostok::sound::single_sound`, `survarium::character_dispersion_calculator`, `survarium::weapon_core_base_state`, `vostok::input::receiver::keyboard`, `survarium::damage_model`, `survarium::weapon_core_shotgun_reload_state`, `vostok::ai::planning::plan_tracker`, `vostok::detail::abstract_type_helper` _+15 more_

---

## 🟡 REWORKED · `survarium::weapon_core` (+44 / −20)

- `+` `AE_pred(void) const`
- `+` `aimed_fire_AE_pred(void) const`
- `+` `aimed_fire_pred(void) const`
- `+` `aimed_fire_transfer_pred(void) const`
- `+` `aimed_idle_AE_not_fire_pred(void) const`
- `+` `aimed_idle_AE_pred(void) const`
- `+` `aimed_idle_transfer_pred(void) const`
- `+` `auto_reload_AE_not_fire_pred(void) const`
- `+` `auto_reload_AE_pred(void) const`
- `+` `can_jump(void) const`
- `+` `can_reload(void) const`
- `+` `can_sprint(void) const`
- `+` `chamber_a_round_AE_pred(void) const`
- `+` `chamber_a_round_aimed_AE_pred(void) const`
- `+` `chamber_a_round_aimed_pred(void) const`
- `+` `chamber_a_round_aimed_transfer_pred(void) const`
- `+` `chamber_a_round_on_reload_break_pred(void) const`
- `+` `chamber_a_round_pred(void) const`
- `+` `chamber_a_round_transfer_pred(void) const`
- `+` `check_for_fire_mode_or_ammunition_or_fire_queue_resetting(void)`
- `+` `check_for_forcing_not_to_aim(void)`
- `+` `check_for_no_ammo_message(void)`
- `+` `check_for_sprint_transition(void)`
- `+` `fire_AE_pred(void) const`
- `+` `fire_pred(void) const`
- `+` `fire_transfer_pred(void) const`
- `+` `hide_AE_pred(void) const`
- `+` `hide_pred(void) const`
- `+` `idle_AE_not_fire_pred(void) const`
- `+` `idle_AE_or_reload_break_pred(void) const`
- `+` `idle_transfer_pred(void) const`
- `+` `inactive_pred(void) const`
- `+` `is_aiming(void) const`
- `+` `is_aiming_and_will_not_break(void) const`
- `+` `is_chambering_a_round(void) const`
- `+` `is_firing(void) const`
- `+` `is_idle(void) const`
- `+` `is_reloading(void) const`
- `+` `is_trying_to_reload(void) const`
- `+` `not_inactive_pred(void) const`
- _+4 more added_
- `−` `can_and_must_reload_and_animation_ended_predicate(void) const`
- `−` `can_and_must_reload_predicate(void) const`
- `−` `could_be_aimed(struct survarium::base_player const &) const`
- `−` `get_target(void) const`
- `−` `instant_idle_end(void)`
- `−` `instant_idle_predicate(void) const`
- `−` `instant_toggle_end(void)`
- `−` `instant_toggle_start(void)`
- `−` `is_not_trying_to_aim_predicate(void) const`
- `−` `is_ready_to_shoot(void) const`
- `−` `is_trying_to_aim(void) const`
- `−` `must_chamber_a_round_aimed_and_animation_ended_predicate(void) const`
- `−` `must_chamber_a_round_aimed_predicate(void) const`
- `−` `must_chamber_a_round_and_animation_ended_predicate(void) const`
- `−` `must_chamber_a_round_predicate(void) const`
- `−` `ready_to_reload(void) const`
- `−` `set_target(enum survarium::weapon_targets)`
- `−` `target_and_animation_ended_predicate(enum survarium::weapon_targets) const`
- `−` `target_predicate(enum survarium::weapon_targets) const`
- `−` `user_animations_selector(void)`

---

## 🟡 REWORKED · `survarium::weapon_user_animations_selector` (+11 / −5)

- `+` `is_crouching(void) const`
- `+` `is_going_to_jump(void) const`
- `+` `is_going_to_sprint(void) const`
- `+` `is_trying_to_jump(void) const`
- `+` `is_trying_to_sprint(void) const`
- `+` `is_weapon_allowing_to_jump(void) const`
- `+` `is_weapon_allowing_to_sprint(void) const`
- `+` `not_sprint_predicate(void) const`
- `+` `on_sprint_start(void)`
- `+` `sprint_predicate(void) const`
- `+` `stand_from_crouch_predicate(void) const`
- `−` `is_weapon_firing(void) const`
- `−` `is_weapon_in_idle(void) const`
- `−` `is_weapon_toggling(void) const`
- `−` `sprint_predicate(void) const`
- `−` `stand_predicate(void) const`

---

## 🟡 REWORKED · `survarium::swf_input_translator` (+3 / −3)

- `+` `register_char_bind(enum vostok::input::enum_keyboard, int, bool, bool)`
- `+` `register_char_bind(enum vostok::input::enum_keyboard, wchar_t, wchar_t, int, bool, bool)`
- `+` `translate_key_action(struct vostok::input::world *, bool, bool, struct survarium::dik_to_swf_bind &)`
- `−` `register_char_bind(enum vostok::input::enum_keyboard, int, bool)`
- `−` `register_char_bind(enum vostok::input::enum_keyboard, wchar_t, wchar_t, int, bool)`
- `−` `translate_key_action(struct vostok::input::world *, bool, struct survarium::dik_to_swf_bind &)`

---

## 🟡 REWORKED · `survarium::weapon` (+4 / −1)

- `+` `add_weapon_fire_light(void)`
- `+` `on_fire_state_end(void)`
- `+` `on_fire_state_start(void)`
- `+` `remove_weapon_fire_light(void)`
- `−` `set_target(enum survarium::weapon_targets)`

---

## 🔴 REMOVED · `vostok::sound::sound_rms_cook` (+0 / −5)

- `−` `delete_resource(class vostok::resources::resource_base *)`
- `−` `on_sub_resources_loaded(class vostok::resources::queries_result &)`
- `−` `sound_rms_cook(void)`
- `−` `translate_query(class vostok::resources::query_result_for_cook &)`
- `−` `~sound_rms_cook(void)`

---

## 🔴 REMOVED · `vostok::sound::sound_rms` (+0 / −4)

- `−` `find_min_value_time_in_interval(unsigned __int64, unsigned __int64, float) const`
- `−` `get_rms_by_time(unsigned __int64) const`
- `−` `sound_rms(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, float)`
- `−` `~sound_rms(void)`

---

## 🟡 REWORKED · `vostok::sound::single_sound` (+1 / −2)

- `+` `single_sound(class vostok::resources::resource_ptr<class vostok::sound::encoded_sound_with_qualities, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::sound::sound_spl, class vostok::resources::unmanaged_intrusive_base> const &)`
- `−` `get_sound_rms(void) const`
- `−` `single_sound(class vostok::resources::resource_ptr<class vostok::sound::encoded_sound_with_qualities, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::sound::sound_spl, class vostok::resources::unmanaged_intrusive_base> const &)`

---

## 🔴 REMOVED · `vostok::resources::pinned_ptr_base<class vostok::sound::sound_rms>` (+0 / −3)

- `−` `pinned_ptr_base<class vostok::sound::sound_rms>(class vostok::resources::pinned_ptr_base<class vostok::sound::sound_rms> const &)`
- `−` `pinned_ptr_base<class vostok::sound::sound_rms>(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>)`
- `−` `~pinned_ptr_base<class vostok::sound::sound_rms>(void)`

---

## 🟡 REWORKED · `survarium::character_dispersion_calculator` (+2)

- `+` `get_skill_coef(enum survarium::weapon_user_state_enum, bool, bool) const`
- `+` `set_character_dispersion_skill_influence(struct survarium::character_dispersion_skill_influence const *)`

---

## 🟡 REWORKED · `survarium::weapon_core_base_state` (+1 / −1)

- `+` `weapon_core_base_state(class survarium::weapon_core &, bool, enum survarium::weapon_state_id_enum)`
- `−` `weapon_core_base_state(class survarium::weapon_core &, bool)`

---

## 🟢 NEW · `survarium::character_dispersion_skill_influence` (+2)

- `+` `character_dispersion_skill_influence(void)`
- `+` `load(class vostok::configs::binary_config_value const &)`

---

## 🟢 NEW · `vostok::render::streaming_ready_texture` (+2)

- `+` `operator=(struct vostok::render::streaming_ready_texture const &)`
- `+` `streaming_ready_texture(struct vostok::render::streaming_ready_texture const &)`

---

## 🟡 REWORKED · `vostok::input::receiver::keyboard` (+2)

- `+` `caps_lock_state(void) const`
- `+` `get_scan_unicode(int, wchar_t *, unsigned int) const`

---

## 🟡 REWORKED · `survarium::damage_model` (+1 / −1)

- `+` `reset(unsigned int)`
- `−` `reset(void)`

---

## 🟡 REWORKED · `survarium::weapon_core_shotgun_reload_state` (+1)

- `+` `player_wants_to_fire_predicate(void) const`

---

## 🟢 NEW · `survarium::game_scene` (+1)

- `+` `~game_scene(void)`

---

## 🟡 REWORKED · `vostok::ai::planning::plan_tracker` (+1)

- `+` `~plan_tracker(void)`

---

## 🟡 REWORKED · `vostok::detail::abstract_type_helper` (+1)

- `+` `abstract_type_helper(void)`

---

## 🟡 REWORKED · `vostok::intrusive_ptr<class vostok::sound::encoded_sound_interface, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock>` (+1)

- `+` `intrusive_ptr<class vostok::sound::encoded_sound_interface, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock>(class vostok::sound::encoded_sound_interface *)`

---

## 🟡 REWORKED · `vostok::render::geometry_batch` (+1)

- `+` `~geometry_batch(void)`

---

## 🟢 NEW · `vostok::render::requested_streamable_texture` (+1)

- `+` `requested_streamable_texture(struct vostok::render::requested_streamable_texture const &)`

---

## 🟢 NEW · `vostok::render::speedtree_data` (+1)

- `+` `speedtree_data(void)`

---

## 🟢 NEW · `vostok::render::streamable_texture_info` (+1)

- `+` `streamable_texture_info(struct vostok::render::streamable_texture_info const &)`

---

## 🟢 NEW · `survarium::animated_model_instance` (+1)

- `+` `~animated_model_instance(void)`

---

## 🟡 REWORKED · `survarium::player_logic_sprint_state` (+1)

- `+` `~player_logic_sprint_state(void)`

---

## 🟡 REWORKED · `vostok::ai::selectors::enemy_target_selector` (+1)

- `+` `~enemy_target_selector(void)`

---

## 🟡 REWORKED · `vostok::console_commands::cc_u32` (+1)

- `+` `~cc_u32(void)`

---

## 🟡 REWORKED · `survarium::base_player` (+1)

- `+` `on_fire(void)`

---

## 🟡 REWORKED · `vostok::render` (+1)

- `+` `index_to_shadow_size`

---

## 🟡 REWORKED · `vostok::resources` (+0 / −1)

- `−` `allocate_managed_resource(unsigned int, enum vostok::resources::class_id_enum)`

---

## 🟡 REWORKED · `vostok::resources::cook_base` (+0 / −1)

- `−` `pin_for_write<class vostok::sound::sound_rms>(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>)`

---

## 🟡 REWORKED · `survarium::weapon_core_aimed_fire_state_base` (+0 / −1)

- `−` `on_aiming_event(struct vostok::animation::animation_callback_params &)`

---

## 🔴 REMOVED · `vostok::particle::lod_entry` (+0 / −1)

- `−` `~lod_entry(void)`

---

## 🔴 REMOVED · `vostok::resources::resource_ptr<class vostok::sound::encoded_sound_with_qualities, class vostok::resources::unmanaged_intrusive_base>` (+0 / −1)

- `−` `resource_ptr<class vostok::sound::encoded_sound_with_qualities, class vostok::resources::unmanaged_intrusive_base>(class vostok::sound::encoded_sound_with_qualities *)`

---

## 🔴 REMOVED · `vostok::sound::sound_rms_pinned` (+0 / −1)

- `−` `sound_rms_pinned(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>)`

---

## 🟡 REWORKED · `survarium::rifle_scope` (+0 / −1)

- `−` `~rifle_scope(void)`

---

## 🟡 REWORKED · `survarium::weapon_core_fire_state_base` (+0 / −1)

- `−` `~weapon_core_fire_state_base(void)`

---

## 🟡 REWORKED · `vostok::particle::particle_system_instance` (+0 / −1)

- `−` `~particle_system_instance(void)`

---

## 🟡 REWORKED · `vostok::sound::composite_sound` (+0 / −1)

- `−` `get_sound_rms(void) const`

---

## 🟡 REWORKED · `vostok::memory` (+0 / −1)

- `−` `zero<char, 14>(char (&)[14])`

