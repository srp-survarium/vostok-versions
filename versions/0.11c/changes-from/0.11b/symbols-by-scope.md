# Build v0.11c-build870  —  what most likely changed

_vs v0.11b-build826 · 2013-05-14 → 2013-05-24_

From **added/deleted hand-written engine functions only** (+142 / −160), grouped by owning class/namespace. Added/deleted are clear non-drift signal; fuzzy `changed` is excluded.

## Likely changes at a glance

- **New (20):** `vostok::memory::single_size_buffer_allocator<32, class vostok::threading::single_threading_policy>`, `survarium::vector<class vostok::variant<32> >`, `vostok::buffer_vector<float>`, `vostok::memory::single_size_buffer_allocator<84, class vostok::threading::single_threading_policy>`, `vostok::memory::single_size_buffer_allocator<96, class vostok::threading::single_threading_policy>`, `vostok::intrusive_list<class vostok::particle::particle_emitter_instance, class vostok::particle::particle_emitter_instance *, 228, class vostok::threading::single_threading_policy, class vostok::size_policy, class vostok::no_debug_policy>`, `vostok::render::effect_compiler::shader_cache_info`, `vostok::render::render_target_instance`, `vostok::resources::resource_ptr<class vostok::physics::bt_collision_shape, class vostok::resources::unmanaged_intrusive_base>`, `vostok::vectora_allocator<class vostok::fixed_vector<unsigned int, 32> >`, `survarium::contacted_bones_comparator`, `survarium::calc_distance_functor` _+8 more_
- **Removed (26):** `vostok::sound::ogg_file_contents_cook`, `vostok::sound::ogg_sound_cook`, `vostok::sound::sound_environment_cook`, `vostok::sound::wav_encoded_sound_interface_cook`, `vostok::sound::ogg_source_cook`, `vostok::sound::wav_encoded_sound_interface`, `vostok::sound::ogg_file_contents`, `vostok::memory::single_size_buffer_allocator<108, class vostok::threading::single_threading_policy>`, `vostok::memory::single_size_buffer_allocator<136, class vostok::threading::single_threading_policy>`, `vostok::memory::single_size_buffer_allocator<28, class vostok::threading::single_threading_policy>`, `vostok::sound::effect_cross_fader`, `vostok::sound::ogg_sound` _+14 more_
- **Reworked (101):** `vostok::sound::sound_scene`, `vostok::sound::new_sound_propagator`, `vostok::memory::detail`, `survarium`, `survarium::weapon_core`, `survarium::booby_trap_set_core`, `survarium::game_world_ui`, `vostok::sound::sound_voice`, `survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state> >`, `survarium::network_client`, `vostok::sound::ogg_encoded_sound_interface_cook`, `vostok::sound::single_sound_cook` _+89 more_

---

## 🟡 REWORKED · `vostok::sound::sound_scene` (+7 / −14)

- `+` `calculate_channel_matrix(unsigned char, class vostok::resources::resource_ptr<class vostok::sound::panning_lut, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::sound::sound_instance_proxy_internal const &, class vostok::math::float3const &, float, float, float *const, float &) const`
- `+` `calculate_hdr_audio_frame(class vostok::vectora<class vostok::sound::new_sound_propagator *> &, unsigned int)`
- `+` `notify_listener(unsigned int)`
- `+` `notify_listener2(unsigned int)`
- `+` `process_fade(unsigned __int64)`
- `+` `tick(unsigned int)`
- `+` `x3daudio_calculate(class vostok::sound::sound_voice &)`
- `−` `add_environment_params(char const *, struct XAUDIO2FX_REVERB_I3DL2_PARAMETERS *, unsigned int &)`
- `−` `calculate_channel_matrix(class vostok::resources::resource_ptr<class vostok::sound::panning_lut, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::sound::sound_instance_proxy_internal const &, class vostok::math::float3const &, float, float, float *, float &) const`
- `−` `calculate_in_graph_position(class vostok::math::float3const &)`
- `−` `create_environment_submix_voice(class vostok::sound::sound_world const &) const`
- `−` `get_current_effect_submix(void)`
- `−` `get_current_environment(void)`
- `−` `get_environment_params(char const *)`
- `−` `get_environment_params(unsigned int)`
- `−` `get_environment_params_id(char const *)`
- `−` `insert_environment(class vostok::sound::sound_environment &, class vostok::math::float4x4const &)`
- `−` `notify_listener(class vostok::sound::sound_world const &)`
- `−` `process_fade(class vostok::sound::sound_world &, unsigned __int64)`
- `−` `tick(class vostok::sound::sound_world &, unsigned int)`
- `−` `x3daudio_calculate(class vostok::sound::sound_world const &, class vostok::sound::sound_voice &)`

---

## 🟡 REWORKED · `vostok::sound::new_sound_propagator` (+6 / −7)

- `+` `attach_voice(void)`
- `+` `detach_voice(void)`
- `+` `get_sound_rms_value(void) const`
- `+` `get_sound_spl_value(float) const`
- `+` `get_sound_spl_value(void) const`
- `+` `new_sound_propagator(enum vostok::sound::playback_mode, unsigned int, unsigned int, unsigned int, unsigned int, class vostok::sound::sound_instance_proxy_internal &, class vostok::sound::sound_propagator_emitter const &)`
- `−` `attach_voice(unsigned int)`
- `−` `attach_voices(unsigned int, class vostok::vectora<struct vostok::sound::sound_voice_params> const &)`
- `−` `detach_voice(class vostok::sound::sound_voice *)`
- `−` `detach_voices(unsigned int)`
- `−` `distribute_voices(unsigned int, class vostok::vectora<struct vostok::sound::sound_voice_params> const &)`
- `−` `new_sound_propagator(class vostok::math::float3const &, class vostok::math::float3const &, enum vostok::sound::playback_mode, unsigned int, unsigned int, unsigned int, unsigned int, class vostok::sound::sound_instance_proxy_internal &, class vostok::sound::sound_propagator_emitter const &)`
- `−` `set_voice_channel_matrix(class vostok::sound::sound_voice *, float const *, float)`

---

## 🟡 REWORKED · `vostok::memory::detail` (+3 / −5)

- `+` `delete_helper_impl<class vostok::memory::single_size_buffer_allocator<32, class vostok::threading::single_threading_policy>, class vostok::sound::voice_bridge, struct vostok::memory::detail::call_destructor_predicate>(class vostok::memory::single_size_buffer_allocator<32, class vostok::threading::single_threading_policy> &, class vostok::sound::voice_bridge *&, struct vostok::memory::detail::call_destructor_predicate const &)`
- `+` `delete_helper_impl<class vostok::memory::single_size_buffer_allocator<84, class vostok::threading::single_threading_policy>, class vostok::sound::new_sound_propagator, struct vostok::memory::detail::call_destructor_predicate>(class vostok::memory::single_size_buffer_allocator<84, class vostok::threading::single_threading_policy> &, class vostok::sound::new_sound_propagator *&, struct vostok::memory::detail::call_destructor_predicate const &)`
- `+` `delete_helper_impl<class vostok::memory::single_size_buffer_allocator<96, class vostok::threading::single_threading_policy>, class vostok::sound::sound_voice, struct vostok::memory::detail::call_destructor_predicate>(class vostok::memory::single_size_buffer_allocator<96, class vostok::threading::single_threading_policy> &, class vostok::sound::sound_voice *&, struct vostok::memory::detail::call_destructor_predicate const &)`
- `−` `delete_helper_impl<class vostok::memory::doug_lea_allocator, class vostok::math::float4x4, struct vostok::memory::detail::call_destructor_predicate>(class vostok::memory::doug_lea_allocator &, class vostok::math::float4x4*&, struct vostok::memory::detail::call_destructor_predicate const &)`
- `−` `delete_helper_impl<class vostok::memory::doug_lea_allocator, struct vostok::sound::propagator_statistic, struct vostok::memory::detail::call_destructor_predicate>(class vostok::memory::doug_lea_allocator &, struct vostok::sound::propagator_statistic *&, struct vostok::memory::detail::call_destructor_predicate const &)`
- `−` `delete_helper_impl<class vostok::memory::single_size_buffer_allocator<108, class vostok::threading::single_threading_policy>, class vostok::sound::new_sound_propagator, struct vostok::memory::detail::call_destructor_predicate>(class vostok::memory::single_size_buffer_allocator<108, class vostok::threading::single_threading_policy> &, class vostok::sound::new_sound_propagator *&, struct vostok::memory::detail::call_destructor_predicate const &)`
- `−` `delete_helper_impl<class vostok::memory::single_size_buffer_allocator<136, class vostok::threading::single_threading_policy>, class vostok::sound::sound_voice, struct vostok::memory::detail::call_destructor_predicate>(class vostok::memory::single_size_buffer_allocator<136, class vostok::threading::single_threading_policy> &, class vostok::sound::sound_voice *&, struct vostok::memory::detail::call_destructor_predicate const &)`
- `−` `delete_helper_impl<class vostok::memory::single_size_buffer_allocator<28, class vostok::threading::single_threading_policy>, class vostok::sound::voice_bridge, struct vostok::memory::detail::call_destructor_predicate>(class vostok::memory::single_size_buffer_allocator<28, class vostok::threading::single_threading_policy> &, class vostok::sound::voice_bridge *&, struct vostok::memory::detail::call_destructor_predicate const &)`

---

## 🟡 REWORKED · `survarium` (+6 / −1)

- `+` `arbitrary_right`
- `+` `call_item_remove_game_world_objects`
- `+` `chamber_a_round_timescale_calculator(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, struct survarium::weapon_state_creation_params const &)`
- `+` `computed_hide_animation_time_scale(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, float)`
- `+` `hide_timescale_calculator(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, struct survarium::weapon_state_creation_params const &)`
- `+` `show_timescale_calculator(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, struct survarium::weapon_state_creation_params const &)`
- `−` `computed_reload_animation_time_scale(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, float)`

---

## 🟡 REWORKED · `survarium::weapon_core` (+5 / −2)

- `+` `get_dispersed_buckshot_direction(class vostok::math::float3const &)`
- `+` `hide_break_pred(void) const`
- `+` `idle_AE_or_show_break_pred(void) const`
- `+` `show_AE_pred(void) const`
- `+` `show_pred(void) const`
- `−` `idle_AE_or_chamber_a_round_break_pred(void) const`
- `−` `not_inactive_pred(void) const`

---

## 🟡 REWORKED · `survarium::booby_trap_set_core` (+3 / −2)

- `+` `find_free_trap(void)`
- `+` `remove_game_world_objects(void)`
- `+` `try_place_trap(class survarium::booby_trap_core &)`
- `−` `remove(void)`
- `−` `try_place_trap(void)`

---

## 🟡 REWORKED · `survarium::game_world_ui` (+4 / −1)

- `+` `callback(struct survarium::flash_movie *, char const *, struct survarium::flash_value const *, unsigned int)`
- `+` `initialize_resources(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `+` `show_cursor(bool)`
- `+` `show_match_stats_wnd(void)`
- `−` `initialize_resources(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)`

---

## 🔴 REMOVED · `vostok::sound::ogg_file_contents_cook` (+0 / −5)

- `−` `delete_resource(class vostok::resources::resource_base *)`
- `−` `ogg_file_contents_cook(void)`
- `−` `on_sub_resources_loaded(class vostok::resources::queries_result &)`
- `−` `translate_query(class vostok::resources::query_result_for_cook &)`
- `−` `~ogg_file_contents_cook(void)`

---

## 🔴 REMOVED · `vostok::sound::ogg_sound_cook` (+0 / −5)

- `−` `delete_resource(class vostok::resources::resource_base *)`
- `−` `ogg_sound_cook(void)`
- `−` `on_sub_resources_loaded(class vostok::resources::queries_result &)`
- `−` `translate_query(class vostok::resources::query_result_for_cook &)`
- `−` `~ogg_sound_cook(void)`

---

## 🔴 REMOVED · `vostok::sound::sound_environment_cook` (+0 / −5)

- `−` `delete_resource(class vostok::resources::resource_base *)`
- `−` `on_environment_options_loaded(class vostok::resources::queries_result &, class vostok::math::float4x4*)`
- `−` `on_model_config_loaded(class vostok::resources::queries_result &)`
- `−` `sound_environment_cook(void)`
- `−` `translate_query(class vostok::resources::query_result_for_cook &)`

---

## 🔴 REMOVED · `vostok::sound::wav_encoded_sound_interface_cook` (+0 / −5)

- `−` `delete_resource(class vostok::resources::resource_base *)`
- `−` `on_file_loaded(class vostok::resources::queries_result &)`
- `−` `translate_query(class vostok::resources::query_result_for_cook &)`
- `−` `wav_encoded_sound_interface_cook(void)`
- `−` `~wav_encoded_sound_interface_cook(void)`

---

## 🟡 REWORKED · `vostok::sound::sound_voice` (+2 / −2)

- `+` `set_volume(float)`
- `+` `sound_voice(class vostok::sound::sound_instance_proxy_internal &, class vostok::sound::sound_propagator_emitter const &, class vostok::resources::resource_ptr<class vostok::sound::sound_spl, class vostok::resources::unmanaged_intrusive_base> const &)`
- `−` `can_be_deleted(void) const`
- `−` `sound_voice(int, unsigned int, unsigned int, class vostok::sound::sound_instance_proxy_internal &, class vostok::sound::sound_propagator_emitter const &, class vostok::resources::resource_ptr<class vostok::sound::sound_spl, class vostok::resources::unmanaged_intrusive_base> const &)`

---

## 🔴 REMOVED · `vostok::sound::ogg_source_cook` (+0 / −4)

- `−` `delete_resource(class vostok::resources::resource_base *)`
- `−` `ogg_source_cook(void)`
- `−` `on_ogg_file_loaded(class vostok::resources::queries_result &, class vostok::resources::query_result_for_cook *)`
- `−` `translate_query(class vostok::resources::query_result_for_cook &)`

---

## 🔴 REMOVED · `vostok::sound::wav_encoded_sound_interface` (+0 / −4)

- `−` `decompress(unsigned char *, unsigned int, unsigned int &, unsigned int)`
- `−` `read_riff(void)`
- `−` `wav_encoded_sound_interface(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>)`
- `−` `~wav_encoded_sound_interface(void)`

---

## 🟡 REWORKED · `survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state> >` (+2 / −1)

- `+` `allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)`
- `+` `destroy_resource(class vostok::resources::unmanaged_resource *)`
- `−` `new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state> >::config_params const &)`

---

## 🟡 REWORKED · `survarium::network_client` (+2 / −1)

- `+` `close_current_match(enum vostok::network_core::disconnect_event_types_enum)`
- `+` `remove_player(class vostok::network_core::packet_reader &)`
- `−` `close_current_match(bool)`

---

## 🟡 REWORKED · `vostok::sound::ogg_encoded_sound_interface_cook` (+2 / −1)

- `+` `on_ogg_resources_loaded(class vostok::resources::queries_result &, class vostok::resources::query_result_for_cook *)`
- `+` `query_converted_resources(class vostok::resources::query_result_for_cook *)`
- `−` `on_sub_resources_loaded(class vostok::resources::queries_result &)`

---

## 🟡 REWORKED · `vostok::sound::single_sound_cook` (+2 / −1)

- `+` `on_sound_options_loaded(class vostok::resources::queries_result &, class vostok::resources::query_result_for_cook *)`
- `+` `on_sub_resources_loaded(class vostok::resources::queries_result &, float)`
- `−` `on_sub_resources_loaded(class vostok::resources::queries_result &)`

---

## 🟡 REWORKED · `survarium::weapon_core_hide_state_base` (+1 / −2)

- `+` `weapon_core_hide_state_base(class survarium::weapon_core &)`
- `−` `is_ready_for_transition(void) const`
- `−` `weapon_core_hide_state_base(class survarium::weapon_core &, bool &)`

---

## 🟡 REWORKED · `survarium::body_part_parameters` (+1 / −2)

- `+` `body_part_parameters(char const *, float, float, float, float, bool, class survarium::damage_model &, unsigned char)`
- `−` `body_part_parameters(char const *, float, float, float, bool, class survarium::damage_model &, unsigned char)`
- `−` `can_affect_death(void)`

---

## 🟢 NEW · `vostok::memory::single_size_buffer_allocator<32, class vostok::threading::single_threading_policy>` (+3)

- `+` `allocate(void)`
- `+` `malloc_impl(unsigned int)`
- `+` `single_size_buffer_allocator<32, class vostok::threading::single_threading_policy>(void *, unsigned int)`

---

## 🟡 REWORKED · `vostok::sound::ogg_encoded_sound_interface` (+2 / −1)

- `+` `get_rms_by_time(unsigned __int64) const`
- `+` `ogg_encoded_sound_interface(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, float const *, unsigned int, unsigned int)`
- `−` `ogg_encoded_sound_interface(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>)`

---

## 🟡 REWORKED · `vostok::sound::single_sound` (+2 / −1)

- `+` `get_sound_spl_value(void) const`
- `+` `single_sound(class vostok::resources::resource_ptr<class vostok::sound::encoded_sound_with_qualities, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::sound::sound_spl, class vostok::resources::unmanaged_intrusive_base> const &, float)`
- `−` `single_sound(class vostok::resources::resource_ptr<class vostok::sound::encoded_sound_with_qualities, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::sound::sound_spl, class vostok::resources::unmanaged_intrusive_base> const &)`

---

## 🟡 REWORKED · `vostok::sound::sound_world` (+1 / −2)

- `+` `create_sound_voice(class vostok::sound::sound_scene &, class vostok::sound::sound_instance_proxy_internal *, class vostok::sound::sound_propagator_emitter const &, class vostok::resources::resource_ptr<class vostok::sound::sound_spl, class vostok::resources::unmanaged_intrusive_base> const &)`
- `−` `create_sound_voice(class vostok::sound::sound_scene &, int, unsigned int, unsigned int, class vostok::sound::sound_instance_proxy_internal *, class vostok::sound::sound_propagator_emitter const &, class vostok::resources::resource_ptr<class vostok::sound::sound_spl, class vostok::resources::unmanaged_intrusive_base> const &)`
- `−` `try_delete_stoping_voices(void)`

---

## 🟡 REWORKED · `survarium::game_world` (+3)

- `+` `input_priority(void)`
- `+` `on_finish_match(void)`
- `+` `set_match_stats_state(void)`

---

## 🟡 REWORKED · `(global)` (+2 / −1)

- `+` `(void)> const &)`
- `+` `(void)> const &)`
- `−` `(void)> const &)`

---

## 🟡 REWORKED · `vostok::sound::voice_bridge` (+1 / −2)

- `+` `set_volume(float)`
- `−` `set_channel_volumes(unsigned char, float const *)`
- `−` `set_sample_rate(unsigned int)`

---

## 🟡 REWORKED · `vostok::sound` (+2 / −1)

- `+` `test_ogg_query(void)`
- `+` `test_snd_loaded(class vostok::resources::queries_result &)`
- `−` `compare_propagator_info_by_distance`

---

## 🟡 REWORKED · `survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state> >` (+0 / −3)

- `−` `allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)`
- `−` `destroy_resource(class vostok::resources::unmanaged_resource *)`
- `−` `new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state> >::config_params const &)`

---

## 🟡 REWORKED · `survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state> >` (+0 / −3)

- `−` `allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)`
- `−` `destroy_resource(class vostok::resources::unmanaged_resource *)`
- `−` `new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state> >::config_params const &)`

---

## 🔴 REMOVED · `vostok::sound::ogg_file_contents` (+0 / −3)

- `−` `decompress(unsigned char *, unsigned int, unsigned int &, unsigned int)`
- `−` `ogg_file_contents(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>)`
- `−` `~ogg_file_contents(void)`

---

## 🟡 REWORKED · `survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state>` (+1 / −1)

- `+` `weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `−` `weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char, bool &)`

---

## 🟡 REWORKED · `survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_show_state>` (+1 / −1)

- `+` `weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_show_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `−` `weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_show_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char, bool &)`

---

## 🟡 REWORKED · `survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state>` (+1 / −1)

- `+` `weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `−` `weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char, bool &)`

---

## 🟡 REWORKED · `survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_show_state>` (+1 / −1)

- `+` `weapon_sound_events_handler_state<class survarium::pistol_weapon_core_show_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `−` `weapon_sound_events_handler_state<class survarium::pistol_weapon_core_show_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char, bool &)`

---

## 🟡 REWORKED · `survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state>` (+1 / −1)

- `+` `weapon_sound_events_handler_state<class survarium::weapon_core_hide_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `−` `weapon_sound_events_handler_state<class survarium::weapon_core_hide_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char, bool &)`

---

## 🟡 REWORKED · `survarium::weapon_sound_events_handler_state<class survarium::weapon_core_show_state>` (+1 / −1)

- `+` `weapon_sound_events_handler_state<class survarium::weapon_core_show_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `−` `weapon_sound_events_handler_state<class survarium::weapon_core_show_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char, bool &)`

---

## 🟡 REWORKED · `vostok::render::stage_lights` (+1 / −1)

- `+` `index_to_shadow_size(class vostok::render::light *, unsigned int) const`
- `−` `index_to_shadow_size(unsigned int) const`

---

## 🟡 REWORKED · `survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_start_substate> >` (+2)

- `+` `allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)`
- `+` `destroy_resource(class vostok::resources::unmanaged_resource *)`

---

## 🟡 REWORKED · `vostok::render::resource_manager` (+2)

- `+` `log_texture_stats(void)`
- `+` `tick(void)`

---

## 🟡 REWORKED · `survarium::double_barreled_weapon_core_hide_state` (+1 / −1)

- `+` `double_barreled_weapon_core_hide_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)`
- `−` `double_barreled_weapon_core_hide_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int, bool &)`

---

## 🟡 REWORKED · `survarium::double_barreled_weapon_core_show_state` (+1 / −1)

- `+` `double_barreled_weapon_core_show_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)`
- `−` `double_barreled_weapon_core_show_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int, bool &)`

---

## 🟡 REWORKED · `survarium::pistol_weapon_core_hide_state` (+1 / −1)

- `+` `pistol_weapon_core_hide_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)`
- `−` `pistol_weapon_core_hide_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int, bool &)`

---

## 🟡 REWORKED · `survarium::pistol_weapon_core_show_state` (+1 / −1)

- `+` `pistol_weapon_core_show_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)`
- `−` `pistol_weapon_core_show_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int, bool &)`

---

## 🟡 REWORKED · `survarium::weapon_core_hide_state` (+1 / −1)

- `+` `weapon_core_hide_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)`
- `−` `weapon_core_hide_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int, bool &)`

---

## 🟡 REWORKED · `survarium::weapon_core_show_state` (+1 / −1)

- `+` `weapon_core_show_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)`
- `−` `weapon_core_show_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int, bool &)`

---

## 🟡 REWORKED · `survarium::weapon_core_show_state_base` (+1 / −1)

- `+` `weapon_core_show_state_base(class survarium::weapon_core &)`
- `−` `weapon_core_show_state_base(class survarium::weapon_core &, bool &)`

---

## 🟢 NEW · `survarium::vector<class vostok::variant<32> >` (+2)

- `+` `vector<class vostok::variant<32> >(unsigned int)`
- `+` `~vector<class vostok::variant<32> >(void)`

---

## 🟢 NEW · `vostok::buffer_vector<float>` (+2)

- `+` `buffer_vector<float>(void *, unsigned int, unsigned int)`
- `+` `push_back(float const &)`

---

## 🟢 NEW · `vostok::memory::single_size_buffer_allocator<84, class vostok::threading::single_threading_policy>` (+2)

- `+` `malloc_impl(unsigned int)`
- `+` `single_size_buffer_allocator<84, class vostok::threading::single_threading_policy>(void *, unsigned int)`

---

## 🟢 NEW · `vostok::memory::single_size_buffer_allocator<96, class vostok::threading::single_threading_policy>` (+2)

- `+` `malloc_impl(unsigned int)`
- `+` `single_size_buffer_allocator<96, class vostok::threading::single_threading_policy>(void *, unsigned int)`

---

## 🟡 REWORKED · `vostok::sound::voice_factory` (+1 / −1)

- `+` `voice_factory(unsigned char *, unsigned int, class vostok::sound::sound_world &, struct vostok::sound::pool_parametrs const &)`
- `−` `voice_factory(unsigned char *, unsigned int, class vostok::sound::sound_world const &, struct vostok::sound::pool_parametrs const &)`

---

## 🟢 NEW · `vostok::intrusive_list<class vostok::particle::particle_emitter_instance, class vostok::particle::particle_emitter_instance *, 228, class vostok::threading::single_threading_policy, class vostok::size_policy, class vostok::no_debug_policy>` (+2)

- `+` `erase(class vostok::particle::particle_emitter_instance *)`
- `+` `push_back(class vostok::particle::particle_emitter_instance *, bool *)`

---

## 🟡 REWORKED · `vostok::render::effect_compiler` (+1 / −1)

- `+` `begin_pass(char const *, char const *, char const *, struct vostok::render::shader_configuration, struct vostok::render::shader_include_getter *)`
- `−` `begin_pass(char const *, char const *, char const *, struct vostok::render::shader_configuration const &, struct vostok::render::shader_include_getter *)`

---

## 🟡 REWORKED · `survarium::damage_model` (+1 / −1)

- `+` `get_pain_health(void)`
- `−` `get_total_health(void)`

---

## 🟡 REWORKED · `survarium::jump_logic` (+2)

- `+` `end_jump(void)`
- `+` `start_jump(void)`

---

## 🟡 REWORKED · `vostok::render::effect_manager` (+2)

- `+` `create_effect<class vostok::render::effect_environment_probe_index>(class render::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base> *)'::`2'::descriptor_object::`dynamic atexit destructor'(void)`
- `+` `create_effect<class vostok::render::effect_environment_probe_index>(class vostok::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base> *)`

---

## 🟡 REWORKED · `vostok::sound::sound_instance_proxy_internal` (+1 / −1)

- `+` `tick(class vostok::math::float3const &, unsigned int)`
- `−` `tick(unsigned int)`

---

## 🟡 REWORKED · `vostok::debug::platform` (+1 / −1)

- `+` `terminate(int, char const *)`
- `−` `terminate(char const *, int)`

---

## 🟡 REWORKED · `vostok::render` (+2)

- `+` `format_name`
- `+` `modify_shader_configuration`

---

## 🔴 REMOVED · `vostok::memory::single_size_buffer_allocator<108, class vostok::threading::single_threading_policy>` (+0 / −2)

- `−` `allocate(void)`
- `−` `single_size_buffer_allocator<108, class vostok::threading::single_threading_policy>(void *, unsigned int)`

---

## 🔴 REMOVED · `vostok::memory::single_size_buffer_allocator<136, class vostok::threading::single_threading_policy>` (+0 / −2)

- `−` `malloc_impl(unsigned int)`
- `−` `single_size_buffer_allocator<136, class vostok::threading::single_threading_policy>(void *, unsigned int)`

---

## 🔴 REMOVED · `vostok::memory::single_size_buffer_allocator<28, class vostok::threading::single_threading_policy>` (+0 / −2)

- `−` `allocate(void)`
- `−` `single_size_buffer_allocator<28, class vostok::threading::single_threading_policy>(void *, unsigned int)`

---

## 🔴 REMOVED · `vostok::sound::effect_cross_fader` (+0 / −2)

- `−` `effect_cross_fader(class vostok::sound::sound_scene &, unsigned int, struct IXAudio2SubmixVoice *, struct IXAudio2SubmixVoice *)`
- `−` `tick(unsigned int, class vostok::sound::sound_environment *)`

---

## 🔴 REMOVED · `vostok::sound::ogg_sound` (+0 / −2)

- `−` `ogg_sound(class vostok::resources::resource_ptr<class vostok::sound::ogg_file_contents, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &)`
- `−` `~ogg_sound(void)`

---

## 🔴 REMOVED · `vostok::sound::sound_environment` (+0 / −2)

- `−` `sound_environment(unsigned int)`
- `−` `~sound_environment(void)`

---

## 🔴 REMOVED · `vostok::intrusive_list<class vostok::particle::particle_emitter_instance, class vostok::particle::particle_emitter_instance *, 224, class vostok::threading::single_threading_policy, class vostok::size_policy, class vostok::no_debug_policy>` (+0 / −2)

- `−` `erase(class vostok::particle::particle_emitter_instance *)`
- `−` `push_back(class vostok::particle::particle_emitter_instance *, bool *)`

---

## 🔴 REMOVED · `vostok::intrusive_list<class vostok::sound::sound_voice, class vostok::sound::sound_voice *, 0, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>` (+0 / −2)

- `−` `erase(class vostok::sound::sound_voice *)`
- `−` `push_back(class vostok::sound::sound_voice *, bool *)`

---

## 🟡 REWORKED · `vostok::strings` (+1)

- `+` `compare(char const *, char const *)`

---

## 🟡 REWORKED · `survarium::weapon_core_shotgun_reload_state` (+1)

- `+` `player_wants_to_aim_predicate(void) const`

---

## 🟡 REWORKED · `survarium::player` (+1)

- `+` `get_movement_speed_factor(void) const`

---

## 🟡 REWORKED · `survarium::damage_zone_core` (+1)

- `+` `contact_test_body_parts(struct survarium::hit_receiver_info const &, class vostok::vectora<struct stlp_std::pair<class vostok::collision::bone_collision_data *, float> > &)`

---

## 🟡 REWORKED · `vostok::intrusive_ptr<class vostok::sound::panning_lut, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock>` (+1)

- `+` `set(class vostok::intrusive_ptr<class vostok::sound::panning_lut, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock> const &)`

---

## 🟡 REWORKED · `survarium::client_player_update` (+1)

- `+` `client_player_update(void)`

---

## 🟡 REWORKED · `survarium::player_state` (+1)

- `+` `player_state(void)`

---

## 🟡 REWORKED · `vostok::fixed_string<128>` (+1)

- `+` `fixed_string<128>(void)`

---

## 🟡 REWORKED · `vostok::particle::particle_action_billboard` (+1)

- `+` `particle_action_billboard(void)`

---

## 🟢 NEW · `vostok::render::effect_compiler::shader_cache_info` (+1)

- `+` `shader_cache_info(void)`

---

## 🟢 NEW · `vostok::render::render_target_instance` (+1)

- `+` `render_target_instance(void)`

---

## 🟡 REWORKED · `vostok::render::vs_data` (+1)

- `+` `~vs_data(void)`

---

## 🟡 REWORKED · `vostok::render::xs_descriptor<struct vostok::render::gs_data>` (+1)

- `+` `~xs_descriptor<struct vostok::render::gs_data>(void)`

---

## 🟡 REWORKED · `vostok::render::xs_descriptor<struct vostok::render::ps_data>` (+1)

- `+` `~xs_descriptor<struct vostok::render::ps_data>(void)`

---

## 🟢 NEW · `vostok::resources::resource_ptr<class vostok::physics::bt_collision_shape, class vostok::resources::unmanaged_intrusive_base>` (+1)

- `+` `resource_ptr<class vostok::physics::bt_collision_shape, class vostok::resources::unmanaged_intrusive_base>(class vostok::physics::bt_collision_shape *)`

---

## 🟡 REWORKED · `vostok::shared_string` (+1)

- `+` `~shared_string(void)`

---

## 🟡 REWORKED · `vostok::threading::mutex` (+1)

- `+` `~mutex(void)`

---

## 🟢 NEW · `vostok::vectora_allocator<class vostok::fixed_vector<unsigned int, 32> >` (+1)

- `+` `ctor<void *>(class vostok::vectora_allocator<void *> const &)`

---

## 🟡 REWORKED · `vostok::vfs::query_mount_arguments` (+1)

- `+` `query_mount_arguments(class vostok::vfs::query_mount_arguments const &)`

---

## 🟢 NEW · `survarium::contacted_bones_comparator` (+1)

- `+` `operator()(struct stlp_std::pair<class vostok::collision::bone_collision_data *, float> const &, struct stlp_std::pair<class vostok::collision::bone_collision_data *, float> const &) const`

---

## 🟢 NEW · `survarium::calc_distance_functor` (+1)

- `+` `operator()(class vostok::physics::base_physics_object *const &)`

---

## 🟢 NEW · `vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<32, class vostok::threading::single_threading_policy>::node>` (+1)

- `+` `allocate(class vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<32, class vostok::threading::single_threading_policy>::node>::free_list_type &)`

---

## 🟢 NEW · `vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<84, class vostok::threading::single_threading_policy>::node>` (+1)

- `+` `allocate(class vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<84, class vostok::threading::single_threading_policy>::node>::free_list_type &)`

---

## 🟢 NEW · `vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<96, class vostok::threading::single_threading_policy>::node>` (+1)

- `+` `allocate(class vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<96, class vostok::threading::single_threading_policy>::node>::free_list_type &)`

---

## 🟡 REWORKED · `vostok::render::resource_intrusive_base` (+1)

- `+` `destroy<class vostok::render::light>(class vostok::render::light const *const)`

---

## 🟢 NEW · `associative_vector<struct vostok::render::texture_stats_key, unsigned int, class vostok::render::vector, struct stlp_std::less<struct vostok::render::texture_stats_key> >` (+1)

- `+` `insert(struct stlp_std::pair<struct vostok::render::texture_stats_key, unsigned int> const &)`

---

## 🟡 REWORKED · `vostok::ai::brain_unit_cook_params` (+1)

- `+` `operator=(struct vostok::ai::brain_unit_cook_params const &)`

---

## 🟡 REWORKED · `vostok::render::options` (+1)

- `+` `get_cascaded_shadow_map_size(void) const`

---

## 🟢 NEW · `survarium::animated_model_instance` (+1)

- `+` `~animated_model_instance(void)`

---

## 🟡 REWORKED · `survarium::rifle_scope` (+1)

- `+` `~rifle_scope(void)`

---

## 🟡 REWORKED · `vostok::sound::composite_sound` (+1)

- `+` `get_sound_spl_value(void) const`

---

## 🟡 REWORKED · `survarium::base_player` (+1)

- `+` `remove_game_world_objects(void)`

---

## 🟢 NEW · `vostok::render::effect_environment_probe_index` (+1)

- `+` `compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)`

---

## 🟡 REWORKED · `vostok::memory::single_size_buffer_allocator<536, class vostok::threading::multi_threading_policy>` (+1)

- `+` `malloc_impl(unsigned int)`

---

## 🟡 REWORKED · `survarium::inventory` (+1)

- `+` `remove_game_world_objects(void)`

---

## 🟡 REWORKED · `survarium::lobby_client` (+1)

- `+` `sell_item(unsigned int, unsigned int)`

---

## 🟢 NEW · `survarium::std_allocator<class vostok::variant<32> >` (+1)

- `+` `deallocate(class vostok::variant<32> *, unsigned int) const`

---

## 🟡 REWORKED · `vostok::buffer_vector<struct survarium::client_player_update>` (+1)

- `+` `push_back(struct survarium::client_player_update const &)`

---

## 🟡 REWORKED · `vostok::intrusive_list<struct vostok::ai::fsm_state_transition, struct vostok::ai::fsm_state_transition *, 36, class vostok::threading::single_threading_policy, class vostok::size_policy, class vostok::no_debug_policy>` (+1)

- `+` `push_front(struct vostok::ai::fsm_state_transition *, bool *)`

---

## 🟢 NEW · `vostok::render::shader_configuration` (+1)

- `+` `merge_with(char const *, struct vostok::render::shader_configuration)`

---

## 🟡 REWORKED · `vostok::render::stage_ambient_lighting` (+1)

- `+` `make_probe_indices_map(class vostok::render::vector<struct vostok::render::environment_probe *> &)`

---

## 🟡 REWORKED · `vostok::animation::mixing` (+0 / −1)

- `−` `operator+<class vostok::animation::mixing::animation_lexeme, class vostok::animation::mixing::animation_lexeme>(class vostok::animation::mixing::animation_lexeme &, class vostok::animation::mixing::animation_lexeme &)`

---

## 🟡 REWORKED · `survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_show_state> >` (+0 / −1)

- `−` `new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_show_state> >::config_params const &)`

---

## 🟡 REWORKED · `survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_show_state> >` (+0 / −1)

- `−` `new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_show_state> >::config_params const &)`

---

## 🟡 REWORKED · `survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_show_state> >` (+0 / −1)

- `−` `new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_show_state> >::config_params const &)`

---

## 🟡 REWORKED · `vostok::intrusive_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base, class vostok::threading::simple_lock>` (+0 / −1)

- `−` `set(class vostok::resources::managed_resource *)`

---

## 🟡 REWORKED · `vostok::intrusive_ptr<class vostok::sound::encoded_sound_interface, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock>` (+0 / −1)

- `−` `set(class vostok::intrusive_ptr<class vostok::sound::encoded_sound_interface, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock> const &)`

---

## 🟡 REWORKED · `vostok::buffer_vector<class vostok::variant<32> const *>` (+0 / −1)

- `−` `buffer_vector<class vostok::variant<32> const *>(void *, unsigned int, unsigned int)`

---

## 🟡 REWORKED · `vostok::fixed_string<256>` (+0 / −1)

- `−` `fixed_string<256>(void)`

---

## 🟡 REWORKED · `vostok::fixed_string<64>` (+0 / −1)

- `−` `fixed_string<64>(class vostok::fixed_string<64> const &)`

---

## 🟡 REWORKED · `vostok::particle::curve_line_ranged_float` (+0 / −1)

- `−` `curve_line_ranged_float(void)`

---

## 🟡 REWORKED · `vostok::render::cascaded_sun_shadow_statistics_group` (+0 / −1)

- `−` `~cascaded_sun_shadow_statistics_group(void)`

---

## 🟡 REWORKED · `vostok::render::debug_statistics_group` (+0 / −1)

- `−` `~debug_statistics_group(void)`

---

## 🟡 REWORKED · `vostok::render::lpv_statistics_group` (+0 / −1)

- `−` `~lpv_statistics_group(void)`

---

## 🟡 REWORKED · `vostok::render::particles_statistics_group` (+0 / −1)

- `−` `~particles_statistics_group(void)`

---

## 🟡 REWORKED · `vostok::render::visibility_statistics_group` (+0 / −1)

- `−` `~visibility_statistics_group(void)`

---

## 🔴 REMOVED · `vostok::resources::resource_ptr<class survarium::game_world_object, class vostok::resources::unmanaged_intrusive_base>` (+0 / −1)

- `−` `resource_ptr<class survarium::game_world_object, class vostok::resources::unmanaged_intrusive_base>(class survarium::game_world_object *)`

---

## 🔴 REMOVED · `vostok::resources::resource_ptr<class vostok::sound::panning_lut, class vostok::resources::unmanaged_intrusive_base>` (+0 / −1)

- `−` `resource_ptr<class vostok::sound::panning_lut, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::resource_ptr<class vostok::sound::panning_lut, class vostok::resources::unmanaged_intrusive_base> const &)`

---

## 🔴 REMOVED · `vostok::sound::unique_propagator_info` (+0 / −1)

- `−` `unique_propagator_info(void)`

---

## 🔴 REMOVED · `vostok::vectora_allocator<struct vostok::sound::propagator_info>` (+0 / −1)

- `−` `ctor<void *>(class vostok::vectora_allocator<void *> const &)`

---

## 🟡 REWORKED · `survarium::player_input_handler` (+0 / −1)

- `−` `alt_is_held(void) const`

---

## 🟡 REWORKED · `survarium::weapon_core_base_state` (+0 / −1)

- `−` `has_animation_ended(void) const`

---

## 🔴 REMOVED · `vostok::intrusive_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock>` (+0 / −1)

- `−` `operator=(class vostok::intrusive_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock> const &)`

---

## 🟡 REWORKED · `vostok::animation::cubic_spline_skeleton_animation` (+0 / −1)

- `−` `length_in_frames(void) const`

---

## 🟡 REWORKED · `vostok::sound::sound_spl` (+0 / −1)

- `−` `get_loudness(float) const`

---

## 🔴 REMOVED · `vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<108, class vostok::threading::single_threading_policy>::node>` (+0 / −1)

- `−` `allocate(class vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<108, class vostok::threading::single_threading_policy>::node>::free_list_type &)`

---

## 🔴 REMOVED · `vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<136, class vostok::threading::single_threading_policy>::node>` (+0 / −1)

- `−` `allocate(class vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<136, class vostok::threading::single_threading_policy>::node>::free_list_type &)`

---

## 🔴 REMOVED · `vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<28, class vostok::threading::single_threading_policy>::node>` (+0 / −1)

- `−` `allocate(class vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<28, class vostok::threading::single_threading_policy>::node>::free_list_type &)`

---

## 🔴 REMOVED · `vostok::detail::type_to_int<struct vostok::particle::world *>` (+0 / −1)

- `−` `get(void)`

---

## 🟡 REWORKED · `vostok::render::engine::world` (+0 / −1)

- `−` `particle_world(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &)`

---

## 🟡 REWORKED · `vostok::render::scene_renderer` (+0 / −1)

- `−` `particle_world(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &)`

---

## 🟡 REWORKED · `vostok::ai::selectors::sound_target_selector` (+0 / −1)

- `−` `~sound_target_selector(void)`

---

## 🟡 REWORKED · `vostok::resources::fs_task_unmount` (+0 / −1)

- `−` `~fs_task_unmount(void)`

---

## 🔴 REMOVED · `vostok::detail::concrete_type_helper<struct vostok::particle::world *>` (+0 / −1)

- `−` `copy_helper(class vostok::mutable_buffer)`

---

## 🔴 REMOVED · `survarium::std_allocator<struct survarium::base_project::resolve_link_object>` (+0 / −1)

- `−` `deallocate(struct survarium::base_project::resolve_link_object *, unsigned int) const`

---

## 🟡 REWORKED · `vostok::render::grass_patch` (+0 / −1)

- `−` `try_accumulate_trample(struct vostok::render::trample_desc &, struct vostok::render::grass_world *, class vostok::render::renderer *, class vostok::render::renderer_context *)`

---

## 🟡 REWORKED · `vostok::render::scene` (+0 / −1)

- `−` `build_lpv_geometry(void)`

---

## 🟡 REWORKED · `vostok::variant<32>` (+0 / −1)

- `−` `set<struct vostok::render::static_model_instance_user_data>(struct vostok::render::static_model_instance_user_data const &)`

---

## 🟡 REWORKED · `vostok::memory` (+0 / −1)

- `−` `delete_helper<class vostok::memory::doug_lea_allocator, class vostok::render::light const>(class vostok::memory::doug_lea_allocator &, class vostok::render::light const *&)`

