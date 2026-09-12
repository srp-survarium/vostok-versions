# Build v0.21d-build2010  —  what most likely changed

_vs v0.20f-build1923 · 2014-04-01 → 2014-04-24_

From **added/deleted hand-written engine functions only** (+605 / −383), grouped by owning class/namespace. Added/deleted are clear non-drift signal; fuzzy `changed` is excluded.

## Likely changes at a glance

- **New (82):** `survarium::base_game_statistics_handler`, `vostok::configs`, `survarium::network_stats_orders_channel`, `survarium::network_stats_packets`, `survarium::network_stats_packets_sequence`, `survarium::network_stats_ports`, `survarium::network_stats_received_messages`, `survarium::network_stats_seconds`, `survarium::network_stats_sent_messages`, `survarium::network_stats_rejected_messages`, `survarium::base_local_network_client`, `survarium::net_stats` _+70 more_
- **Removed (41):** `vostok::physics::old_bullet_character_controller`, `vostok::render::debug::renderer`, `survarium::jump_logic`, `vostok::render::debug::draw_lines_command`, `vostok::render::debug::draw_triangles_command`, `survarium::weapon_ammunition_cook`, `survarium::match_total_stats`, `vostok::physics::character_move_test_callback`, `vostok::intrusive_list<struct survarium::player_stamina_subscriber, struct survarium::player_stamina_subscriber *, 32, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>`, ``vostok::render::scene::process_streaming'::`51'::remove_texture_predicate`, `vostok::resources::pinned_ptr_mutable<struct vostok::render::texture_data_resource>`, `vostok::memory::single_size_buffer_allocator<1364, class vostok::threading::multi_threading_policy>` _+29 more_
- **Reworked (171):** `(global)`, `vostok::network_core::udp_match_stats`, `survarium::lobby_menu`, `vostok::physics::bullet_character_controller`, `survarium::game_statistics_handler`, `survarium::lobby_client`, `survarium`, `vostok::animation::bone_matrices_computer`, `survarium::player_logic_jump_state`, `survarium::game_world_ui`, `vostok::render`, `vostok::network_core` _+159 more_

---

## 🟡 REWORKED · `(global)` (+51 / −31)

- `+` `(bool)> const &, bool, bool, bool)`
- `+` `(char const *, class vostok::network_core::udp_match_packet const *)> const &, class vostok::network_core::udp_match_stats &)`
- `+` `(class boost::system::error_code const &, unsigned int)> > > >)`
- `+` `(class boost::system::error_code const &, unsigned int)> const &)`
- `+` `(class vostok::memory::single_size_buffer_allocator<684, class vostok::threading::multi_threading_policy> const &)> const &)`
- `+` `(class vostok::memory::single_size_buffer_allocator<80, class vostok::threading::single_threading_policy> const &)> const &)`
- `+` `(class vostok::network_core::udp_match_packet &)> > > &)`
- `+` `(class vostok::network_core::udp_match_packet &)> > >(void)`
- `+` `(class vostok::network_core::udp_match_packet &)> > const &)`
- `+` `(class vostok::network_core::udp_match_packet &)> > const &) const`
- `+` `(class vostok::network_core::udp_match_packet &)> const &)`
- `+` `(class vostok::network_core::udp_match_packet &)> const &)> const &)`
- `+` `(class vostok::network_core::udp_match_packet &)> const &)> const &)`
- `+` `(class vostok::network_core::udp_match_packet &)> const &)> const &)`
- `+` `(class vostok::network_core::udp_match_packet &)> const &, unsigned int, unsigned int)`
- `+` `(class vostok::network_core::udp_match_packet &, bool)> > > &)`
- `+` `(class vostok::network_core::udp_match_packet &, bool)> > const &)`
- `+` `(class vostok::network_core::udp_match_packet &, bool)> > const &) const`
- `+` `(class vostok::network_core::udp_match_packet &, bool)> const &, unsigned int, unsigned int)`
- `+` `(class vostok::network_core::udp_match_packet &, class boost::system::error_code const &, unsigned int)> const &)`
- `+` `(class vostok::resources::queries_result &)> const &)`
- `+` `(enum vostok::connection_error_types_enum)> >, class boost::_bi::value<class boost::asio::ip::basic_resolver_iterator<class boost::asio::ip::tcp> > >(void)`
- `+` `(float, float, unsigned int, unsigned int, unsigned int, float)> const &, float, class vostok::animation::mixing::animation_lexeme &)`
- `+` `(float, float, unsigned int, unsigned int, unsigned int, float)> const &, float, class vostok::animation::mixing::animation_lexeme &)`
- `+` `(float, float, unsigned int, unsigned int, unsigned int, float)> const &, float, class vostok::animation::mixing::animation_lexeme &)`
- `+` `(float, float, unsigned int, unsigned int, unsigned int, float)> const &, float, class vostok::animation::mixing::animation_lexeme &) const`
- `+` `(float, float, unsigned int, unsigned int, unsigned int, float)> const &, float, struct survarium::weapon_animation_parameters const &)`
- `+` `(float, float, unsigned int, unsigned int, unsigned int, float)> const &, float, struct survarium::weapon_animation_parameters const &)`
- `+` `(float, float, unsigned int, unsigned int, unsigned int, float)> const &, float, struct survarium::weapon_animation_parameters const &)`
- `+` `(float, float, unsigned int, unsigned int, unsigned int, float)> const &, float, struct survarium::weapon_animation_parameters const &)`
- `+` `(float, float, unsigned int, unsigned int, unsigned int, float)> const &, float, struct survarium::weapon_animation_parameters const &)`
- `+` `(struct vostok::animation::animation_callback_params &)> const &)`
- `+` `(unsigned char, short)> const &)`
- `+` `(unsigned short)> const &, bool) const`
- `+` `(unsigned short)> const &, unsigned char, bool) const`
- `+` `(unsigned short)> const &, unsigned char, bool) const`
- `+` `(unsigned short)> const &, unsigned char, bool) const`
- `+` `(unsigned short)> const &, unsigned char, bool) const`
- `+` `(void)> const &)`
- `+` `?set_size@render_output_window@render@vostok@@QAEXII_N_N11@Z`
- _+11 more added_
- `−` `(bool)> const &, bool, bool)`
- `−` `(char const *, class vostok::network_core::udp_match_packet const *)> const &)`
- `−` `(class vostok::memory::single_size_buffer_allocator<1364, class vostok::threading::multi_threading_policy> const &)> const &)`
- `−` `(class vostok::memory::single_size_buffer_allocator<76, class vostok::threading::single_threading_policy> const &)> const &)`
- `−` `(class vostok::network_core::buffer_reader &)> const &, class vostok::intrusive_ptr<class vostok::network_core::udp_match_packets_allocator, class vostok::network_core::udp_match_packets_allocator, class vostok::threading::multi_threading_policy> const &, class vostok::network_core::udp_match_packet &, struct vostok::network_core::udp_match_stats const &, struct vostok::network_core::udp_match_stats &)`
- `−` `(class vostok::network_core::buffer_reader &, class boost::asio::ip::basic_endpoint<class boost::asio::ip::udp> const &, struct vostok::network_core::socket_handler *)> const &)`
- `−` `(class vostok::network_core::udp_match_packet &)> const &, class vostok::network_core::udp_match_packet &, class vostok::intrusive_ptr<class vostok::network_core::udp_match_packets_allocator, class vostok::network_core::udp_match_packets_allocator, class vostok::threading::multi_threading_policy> const &, struct vostok::network_core::udp_match_stats const &, struct vostok::network_core::udp_match_stats &)`
- `−` `(class vostok::network_core::udp_match_packet &, class boost::system::error_code const &, unsigned int)> const &)`
- `−` `(class vostok::network_core::udp_match_packet &, class boost::system::error_code const &, unsigned int)> const &)> const &)`
- `−` `(class vostok::network_core::udp_match_packet &, class boost::system::error_code const &, unsigned int)> const &)> const &)`
- `−` `(class vostok::network_core::udp_match_packet &, class boost::system::error_code const &, unsigned int)> const &)> const &)`
- `−` `(enum vostok::connection_error_types_enum)> >, class boost::_bi::value<class boost::asio::ip::basic_resolver_iterator<class boost::asio::ip::tcp> >, struct boost::arg<1>, struct boost::arg<2> > >(void)`
- `−` `(float)> const &, float)`
- `−` `(float, float, unsigned int, unsigned int, unsigned int, float)> const &, class vostok::animation::mixing::animation_lexeme &)`
- `−` `(float, float, unsigned int, unsigned int, unsigned int, float)> const &, class vostok::animation::mixing::animation_lexeme &)`
- `−` `(float, float, unsigned int, unsigned int, unsigned int, float)> const &, class vostok::animation::mixing::animation_lexeme &)`
- `−` `(float, float, unsigned int, unsigned int, unsigned int, float)> const &, class vostok::animation::mixing::animation_lexeme &)`
- `−` `(float, float, unsigned int, unsigned int, unsigned int, float)> const &, struct survarium::weapon_animation_parameters const &)`
- `−` `(float, float, unsigned int, unsigned int, unsigned int, float)> const &, struct survarium::weapon_animation_parameters const &)`
- `−` `(float, float, unsigned int, unsigned int, unsigned int, float)> const &, struct survarium::weapon_animation_parameters const &)`
- `−` `(float, float, unsigned int, unsigned int, unsigned int, float)> const &, struct survarium::weapon_animation_parameters const &)`
- `−` `(float, float, unsigned int, unsigned int, unsigned int, float)> const &, struct survarium::weapon_animation_parameters const &)`
- `−` `(struct vostok::animation::animation_callback_params &)> const &)`
- `−` `(unsigned int, unsigned int)> const &, bool, unsigned int, unsigned int, unsigned int)`
- `−` `(unsigned short)> const &) const`
- `−` `(unsigned short)> const &, unsigned char) const`
- `−` `(unsigned short)> const &, unsigned char) const`
- `−` `(unsigned short)> const &, unsigned char) const`
- `−` `(unsigned short)> const &, unsigned char) const`
- `−` `?set_size@render_output_window@render@vostok@@QAEXII_N_N1@Z`
- `−` `?set_size@res_render_output@render@vostok@@QAEXII_N_N1@Z`

---

## 🟡 REWORKED · `vostok::network_core::udp_match_stats` (+22 / −1)

- `+` `register_acknowledged_message(class vostok::network_core::udp_match_packet const &)`
- `+` `register_constructed_message(class vostok::network_core::udp_match_packet const &)`
- `+` `register_different_message(unsigned char)`
- `+` `register_discarded_message(unsigned char, unsigned int)`
- `+` `register_duplicated_message(unsigned char)`
- `+` `register_enqueued_message(class vostok::network_core::udp_match_packet const &)`
- `+` `register_low_level_message(class vostok::network_core::udp_match_packet const &)`
- `+` `register_message_processed_by_logic(class vostok::network_core::udp_match_packet const &)`
- `+` `register_message_waiting_for_logic(class vostok::network_core::udp_match_packet const &)`
- `+` `register_ordered_message(class vostok::network_core::udp_match_packet const &)`
- `+` `register_packet(enum vostok::network_core::udp_match_raw_stats::packets_types_enum, unsigned int, unsigned int)`
- `+` `register_received_duplicated_packet(class vostok::network_core::buffer_reader const &, unsigned short, class vostok::network_core::sequence_number<unsigned short> const &, unsigned __int64const &, class vostok::network_core::sequence_number<unsigned short> const &, unsigned __int64const &)`
- `+` `register_received_message(class vostok::network_core::buffer_reader const &, unsigned char)`
- `+` `register_received_message(class vostok::network_core::udp_match_packet const &)`
- `+` `register_received_packet(class vostok::network_core::buffer_reader const &, class vostok::network_core::sequence_number<unsigned short> const &, unsigned short, class vostok::network_core::sequence_number<unsigned short> const &, unsigned __int64const &, class vostok::network_core::sequence_number<unsigned short> const &, unsigned __int64const &)`
- `+` `register_sent_message(class vostok::network_core::udp_match_packet const &)`
- `+` `register_sent_packet(class vostok::network_core::udp_match_packet const &)`
- `+` `register_skipped_message(unsigned char, class vostok::network_core::buffer_reader const &, unsigned int)`
- `+` `register_too_new_message(unsigned char)`
- `+` `register_too_old_message(unsigned char)`
- `+` `register_unacknowledged_message(class vostok::network_core::udp_match_packet const &)`
- `+` `udp_match_stats(struct vostok::network_core::udp_match_packets_orderer &, unsigned char, unsigned char)`
- `−` `udp_match_stats(void)`

---

## 🟡 REWORKED · `survarium::lobby_menu` (+9 / −13)

- `+` `create_quest_ui_message(char const *, unsigned char)`
- `+` `fill_match_statistic(struct survarium::match_stats const &, struct survarium::player_result_full const &, unsigned char)`
- `+` `fill_player_statistic(struct survarium::player_result_brief const &, struct survarium::player_result_full const &)`
- `+` `fill_reputation_levels(void)`
- `+` `fill_squad_info(struct survarium::squad<struct survarium::squad_member_item_with_name> const &, bool)`
- `+` `get_next_number_from_message(class vostok::fixed_string<256> &)`
- `+` `on_price_items_arrived(void)`
- `+` `prepare_quest_object(struct survarium::flash_value &, struct survarium::quest_instance const &, struct survarium::quest_descriptor const &)`
- `+` `show_match_statistic(void)`
- `−` `fill_match_statistic(struct survarium::match_total_stats const &, class vostok::vectora<struct survarium::player_results_item> const &)`
- `−` `fill_player_statistic(struct survarium::match_player_stats const &)`
- `−` `fill_squad_info(class vostok::fixed_vector<struct survarium::squad_member_item, 3> const &, bool)`
- `−` `on_operation_permitted_received(enum vostok::lobby::client::messages_enum)`
- `−` `on_price_items_arrived(unsigned char)`
- `−` `on_profile_arrived(unsigned char)`
- `−` `query_account_data(void)`
- `−` `query_lobby_info(void)`
- `−` `request_squad_status_from_server(unsigned int)`
- `−` `request_squad_status_from_server_impl(unsigned int, unsigned int)`
- `−` `request_status_from_server(unsigned int)`
- `−` `request_status_from_server_impl(unsigned int, unsigned int)`
- `−` `update_status(void)`

---

## 🔴 REMOVED · `vostok::physics::old_bullet_character_controller` (+0 / −22)

- `−` `can_stand(void)`
- `−` `convex_sweep_test(class btTransform const &, class btTransform const &, class btVector3const &, float, float, class btVector3&, class btVector3&, float &)`
- `−` `deserialize(class vostok::network_core::buffer_reader &, unsigned int)`
- `−` `get_bt_collision_obect(void)`
- `−` `get_collision_group(void) const`
- `−` `get_transform(void)`
- `−` `insert(class btDynamicsWorld *)`
- `−` `old_bullet_character_controller(class vostok::math::float2const &, class vostok::math::float2const &, short, short, class vostok::memory::base_allocator &)`
- `−` `on_ground(void) const`
- `−` `player_step(float, class btVector3const &)`
- `−` `recover_from_penetration(int)`
- `−` `remove(class btDynamicsWorld *)`
- `−` `serialize(class vostok::network_core::buffer_writer const &, unsigned int) const`
- `−` `set_desired_walk_vector(class btVector3const &)`
- `−` `set_transform(class btTransform const &)`
- `−` `setup_crouch_state(bool, bool)`
- `−` `setup_shape_dim(class vostok::math::float2const &)`
- `−` `step_down(float, bool, class btVector3const &, bool, class btVector3const &, float)`
- `−` `step_forward_and_strafe(class btVector3const &)`
- `−` `step_up(bool, class btVector3&)`
- `−` `updateAction(class btCollisionWorld *, float)`
- `−` `updateTargetPositionBasedOnCollision(class btVector3const &, class btVector3const &, float, float)`

---

## 🟡 REWORKED · `vostok::physics::bullet_character_controller` (+11 / −10)

- `+` `can_skeep_player_step(void) const`
- `+` `impassable_slope_down_slide(class btVector3const &, class btVector3const &, class btVector3const &, float, class btVector3&)`
- `+` `initialize(void)`
- `+` `need_slide_on_supporting_surface(void) const`
- `+` `on_ground(float) const`
- `+` `on_steep_slope(float) const`
- `+` `side_slide_on_low_ceiling(class btVector3const &, class btVector3const &, class btVector3const &, float, float, class btVector3const &, class btVector3&)`
- `+` `side_slide_on_slope(class btVector3const &, class btVector3const &, class btVector3const &, float, float, class btVector3&)`
- `+` `slide_in_impassable_case_impl(class btVector3const &, class btVector3const &, class btVector3const &, float, float, class btVector3&)`
- `+` `step_down_sweep_test_impl(float, class btVector3const &, float, class btVector3const &, class btVector3&, class btVector3&)`
- `+` `update_slide_velocity(class btVector3const &, class btVector3const &)`
- `−` `can_jump(void) const`
- `−` `end_jump(void)`
- `−` `get_transform(void)`
- `−` `on_ground(void) const`
- `−` `on_steep_slope(void) const`
- `−` `side_slide_on_low_ceiling(class btVector3const &, class btVector3const &, class btVector3const &, float, float, class btVector3const &, class btVector3&, float &)`
- `−` `side_slide_on_slope(class btVector3const &, class btVector3const &, class btVector3const &, float, float, class btVector3&, float &)`
- `−` `slide_in_impassable_case_impl(class btVector3const &, class btVector3const &, class btVector3const &, float, float, class btVector3&, float &)`
- `−` `step_down_sweep_test_impl(float, float, class btVector3const &, float, class btVector3const &, class btVector3&, class btVector3&, float &)`
- `−` `update_slide_velocity(class btVector3const &, class btVector3const &, float)`

---

## 🟡 REWORKED · `survarium::game_statistics_handler` (+2 / −17)

- `+` `on_event(unsigned char, enum survarium::match_stats_events_dict_enum, unsigned short)`
- `+` `start_match(class survarium::game_world_core &, struct survarium::match_options const &)`
- `−` `clear(void)`
- `−` `deserialize(class vostok::network_core::buffer_reader &, unsigned int)`
- `−` `emit_score_changed_event(unsigned char, short)`
- `−` `finish_match(void)`
- `−` `game_statistics_handler(void)`
- `−` `on_artefact_took(unsigned char)`
- `−` `on_event(unsigned char, enum survarium::match_stats_events_dict_enum, unsigned short)`
- `−` `on_limb_affect(unsigned int, unsigned char, enum survarium::affect_event_type_enum)`
- `−` `on_medkit_action(class survarium::medkit const &, bool, unsigned char)`
- `−` `on_pain_body_part_damage_received(unsigned char, unsigned char, float)`
- `−` `on_pain_body_part_regenerated(unsigned char)`
- `−` `on_player_damaged(unsigned int, unsigned char, enum survarium::player_stances_enum, unsigned char, float, enum survarium::profile_slot_enum, bool)`
- `−` `on_player_killed(unsigned int, unsigned char, enum survarium::player_stances_enum, unsigned short, class vostok::math::float3const &, bool, unsigned char, class vostok::math::float3const &, bool, enum survarium::profile_slot_enum, bool, bool)`
- `−` `recalculate_scores(void)`
- `−` `serialize(class vostok::network_core::buffer_writer const &, unsigned int) const`
- `−` `start_match(class survarium::game_world_core &, struct survarium::match_options const &)`
- `−` `~game_statistics_handler(void)`

---

## 🟢 NEW · `survarium::base_game_statistics_handler` (+19)

- `+` `base_game_statistics_handler(void)`
- `+` `clear(void)`
- `+` `deserialize(class vostok::network_core::buffer_reader &, unsigned int)`
- `+` `emit_score_changed_event(unsigned char, short)`
- `+` `finish_match(void)`
- `+` `on_artefact_took(unsigned char)`
- `+` `on_event(unsigned char, enum survarium::match_stats_events_dict_enum, unsigned short)`
- `+` `on_limb_affect(unsigned int, unsigned char, enum survarium::affect_event_type_enum)`
- `+` `on_medkit_action(class survarium::medkit const &, bool, unsigned char)`
- `+` `on_pain_body_part_damage_received(unsigned char, unsigned char, float)`
- `+` `on_pain_body_part_regenerated(unsigned char)`
- `+` `on_player_damaged(unsigned int, unsigned char, enum survarium::player_stances_enum, unsigned char, float, enum survarium::profile_slot_enum, bool, unsigned int, unsigned short)`
- `+` `on_player_killed(unsigned int, unsigned char, enum survarium::player_stances_enum, unsigned short, class vostok::math::float3const &, bool, unsigned char, class vostok::math::float3const &, bool, enum survarium::profile_slot_enum, bool, bool)`
- `+` `on_player_weapon_firing(unsigned char, enum survarium::profile_slot_enum, enum survarium::player_stances_enum, unsigned short)`
- `+` `on_victory_item_event(unsigned char, enum survarium::victory_item_event_type, class survarium::victory_item_core const &)`
- `+` `recalculate_scores(void)`
- `+` `serialize(class vostok::network_core::buffer_writer const &, unsigned int) const`
- `+` `start_match(class survarium::game_world_core &, struct survarium::match_options const &)`
- `+` `~base_game_statistics_handler(void)`

---

## 🟡 REWORKED · `survarium::lobby_client` (+6 / −11)

- `+` `buy_item(unsigned short, unsigned int, unsigned char, bool, enum survarium::profile_slot_enum)`
- `+` `query_info_from_server(enum vostok::lobby::query_info_types)`
- `+` `query_match_stats(unsigned int)`
- `+` `read_match_stats(class vostok::network_core::buffer_reader &)`
- `+` `read_price_items(class vostok::network_core::buffer_reader &)`
- `+` `squad_ready_count(void) const`
- `−` `buy_item(unsigned short, unsigned int, unsigned char, bool)`
- `−` `ping_server(void)`
- `−` `query_client_status(enum vostok::lobby::query_info_types)`
- `−` `query_prices(unsigned int)`
- `−` `query_profile_leveling(unsigned int)`
- `−` `query_squad_info(void)`
- `−` `read_account_money(class vostok::network_core::buffer_reader &)`
- `−` `read_last_played_match_stats(class vostok::network_core::buffer_reader &)`
- `−` `read_new_profile(class vostok::network_core::buffer_reader &)`
- `−` `read_price_items(class vostok::network_core::buffer_reader &)`
- `−` `squad_ready_count(void) const`

---

## 🟡 REWORKED · `survarium` (+14 / −2)

- `+` `apply_modifier(enum survarium::player_params_modifiers_enum, float, struct survarium::player_profile const &, class survarium::items_dictionary const &)`
- `+` `calculate_profile_icon(class survarium::inventory const &)`
- `+` `calculate_profile_icon(class survarium::items_dictionary const &, struct survarium::player_profile const &)`
- `+` `disable_game_statistics_gathering(void)`
- `+` `find`
- `+` `get_modifier_value(enum survarium::player_params_modifiers_enum, struct survarium::inventory_item_descr const &, class survarium::items_dictionary const &)`
- `+` `get_profile_faction_affinity(class survarium::inventory const &, enum survarium::factions_enum &, float &)`
- `+` `item_faction(class survarium::items_dictionary const &, struct survarium::inventory_item_descr const &)`
- `+` `item_weight(struct survarium::inventory_item_descr const &, class survarium::items_dictionary const &)`
- `+` `message_id_to_string(unsigned char)`
- `+` `parse_resolution`
- `+` `query_inventory_item(enum survarium::profile_slot_enum, struct survarium::inventory_cooker_data *const, class vostok::buffer_vector<struct vostok::resources::request> &, class vostok::buffer_vector<class vostok::variant<32> const *> &, class vostok::variant<32> *const)`
- `+` `shotgun_reload_end_timescale_calculator(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, struct survarium::weapon_state_creation_params const &)`
- `+` `shotgun_reload_start_timescale_calculator(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, struct survarium::weapon_state_creation_params const &)`
- `−` `calculate_profile_icon(struct survarium::player_profile const &, class survarium::items_dictionary const &)`
- `−` `setup_damage_model_from_profile(class survarium::damage_model &, struct survarium::player_profile const &, class survarium::items_dictionary const &)`

---

## 🔴 REMOVED · `vostok::render::debug::renderer` (+0 / −16)

- `−` `draw_aabb(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float3const &, class vostok::math::float3const &, class vostok::math::color const &, bool)`
- `−` `draw_cross(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float3const &, float, class vostok::math::color const &, bool)`
- `−` `draw_cube(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float4x4const &, class vostok::math::float3const &, class vostok::math::color const &, bool)`
- `−` `draw_cube_solid(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float4x4const &, class vostok::math::float3const &, class vostok::math::color const &, bool)`
- `−` `draw_cylinder(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float4x4const &, class vostok::math::float3const &, class vostok::math::color const &, bool)`
- `−` `draw_line(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float3const &, class vostok::math::float3const &, class vostok::math::color const &, bool)`
- `−` `draw_line_capsule(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float4x4const &, class vostok::math::float3const &, class vostok::math::color const &, bool)`
- `−` `draw_line_hemisphere(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float4x4const &, class vostok::math::float3const &, bool, class vostok::math::color const &, bool)`
- `−` `draw_lines(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float4x4const &, class vostok::math::float3const &, float const *, unsigned int, unsigned short const *, unsigned int, class vostok::math::color const &, bool)`
- `−` `draw_lines(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float4x4const &, float const *, unsigned int, unsigned short const *, unsigned int, class vostok::math::color const &, bool)`
- `−` `draw_origin(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float4x4const &, float, bool)`
- `−` `draw_primitive_solid(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float4x4const &, class vostok::math::float3const &, float const *, unsigned int, unsigned short const *, unsigned int, class vostok::math::color const &, bool)`
- `−` `draw_solid_capsule(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float4x4const &, class vostok::math::float3const &, class vostok::math::color const &, bool)`
- `−` `draw_sphere(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float4x4const &, float const &, class vostok::math::color const &, bool)`
- `−` `draw_sphere_solid(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float3const &, float const &, class vostok::math::color const &, bool)`
- `−` `draw_triangle(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, struct vostok::render::vertex_colored const (&)[3], bool)`

---

## 🟡 REWORKED · `vostok::animation::bone_matrices_computer` (+7 / −7)

- `+` `compute_bones_local_matrices(class vostok::math::float4x4*, class vostok::math::float4x4*, unsigned int const *, unsigned char, bool) const`
- `+` `compute_bones_matrices(class vostok::math::float4x4*, class vostok::math::float4x4*, unsigned int const *, unsigned char, bool) const`
- `+` `compute_skeleton_branch(class vostok::animation::skeleton_bone const &, class vostok::math::float4x4*, class vostok::math::float4x4const &, unsigned int const *, unsigned int const *, unsigned char, bool) const`
- `+` `compute_skeleton_branch_local(class vostok::animation::skeleton_bone const &, class vostok::math::float4x4*, unsigned int const *, unsigned int const *, unsigned char, bool) const`
- `+` `computed_bone_matrix(class vostok::animation::skeleton_bone const &, unsigned int const *, bool) const`
- `+` `computed_local_bone_matrix(class vostok::animation::skeleton_bone const &, unsigned int, bool) const`
- `+` `computed_local_bone_transform(class vostok::animation::skeleton_bone const &, unsigned int, unsigned int, bool) const`
- `−` `compute_bones_local_matrices(class vostok::math::float4x4*, class vostok::math::float4x4*, unsigned int const *, unsigned char) const`
- `−` `compute_bones_matrices(class vostok::math::float4x4*, class vostok::math::float4x4*, unsigned int const *, unsigned char) const`
- `−` `compute_skeleton_branch(class vostok::animation::skeleton_bone const &, class vostok::math::float4x4*, class vostok::math::float4x4const &, unsigned int const *, unsigned int const *, unsigned char) const`
- `−` `compute_skeleton_branch_local(class vostok::animation::skeleton_bone const &, class vostok::math::float4x4*, unsigned int const *, unsigned int const *, unsigned char) const`
- `−` `computed_bone_matrix(class vostok::animation::skeleton_bone const &, unsigned int const *) const`
- `−` `computed_local_bone_matrix(class vostok::animation::skeleton_bone const &, unsigned int) const`
- `−` `computed_local_bone_transform(class vostok::animation::skeleton_bone const &, unsigned int, unsigned int) const`

---

## 🟡 REWORKED · `survarium::player_logic_jump_state` (+11 / −1)

- `+` `get_animation(enum survarium::jump_animation_parts) const`
- `+` `get_animation(enum survarium::jump_type_enum, enum survarium::jump_animation_parts) const`
- `+` `get_move_animation(void) const`
- `+` `initialize_logic(void)`
- `+` `initialize_weight_for_on_site_animation(void)`
- `+` `is_short_jump(void) const`
- `+` `player_logic_jump_state(class survarium::weapon_user_animations_selector &)`
- `+` `remove_animation_callback(char const *, void const *)`
- `+` `remove_animation_callback(enum vostok::animation::reserved_channel_ids_enum, void const *)`
- `+` `start_jump(void)`
- `+` `~player_logic_jump_state(void)`
- `−` `set_user(class survarium::base_player &)`

---

## 🟡 REWORKED · `survarium::game_world_ui` (+6 / −5)

- `+` `draw_damage_collector(struct survarium::player::inflicted_damage_collector const &)`
- `+` `on_player_killed(unsigned char, unsigned char, bool, unsigned char)`
- `+` `refresh_minimap_screen_position(void) const`
- `+` `refresh_quests_progress_text_alpha(void) const`
- `+` `refresh_quests_progress_visibility(void) const`
- `+` `set_quests_progress(struct survarium::quest_ui_data *, unsigned int)`
- `−` `initialize_quick_slots(void)`
- `−` `on_enemy_hitted(unsigned int, bool, unsigned int, float)`
- `−` `on_player_killed(unsigned char, unsigned char, bool, unsigned short)`
- `−` `show_oxygene(bool)`
- `−` `update_back_slot(class vostok::resources::resource_ptr<class survarium::inventory_item, class vostok::resources::unmanaged_intrusive_base> const &)`

---

## 🟡 REWORKED · `vostok::render` (+6 / −4)

- `+` `defer_execution(class vostok::render::base_command &, class vostok::resources::resource_ptr<struct vostok::render::base_scene_view, class vostok::resources::unmanaged_intrusive_base> const &)`
- `+` `fix_header_and_get_offset_to_body`
- `+` `flush_hw_commands`
- `+` `is_visible_statistics`
- `+` `read_file_chunk(class vostok::fs_new::native_path_string const &, unsigned char *, unsigned __int64, unsigned __int64, unsigned __int64, class vostok::fs_new::synchronous_device_interface const &)`
- `+` `strings_width`
- `−` `defer_execution(class vostok::render::base_command &, class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &)`
- `−` `parse_resolution`
- `−` `reclaim<class vostok::render::res_render_output, 64>(class vostok::fixed_vector<class vostok::render::res_render_output *, 64> &, class vostok::render::res_render_output const *)`
- `−` `reclaim<class vostok::render::res_xs<struct vostok::render::gs_data>, struct vostok::render::resource_manager::compare_shader_predicate<struct vostok::render::gs_data> >(class vostok::render::set<class vostok::render::res_xs<struct vostok::render::gs_data> *, struct vostok::render::resource_manager::compare_shader_predicate<struct vostok::render::gs_data> > &, class vostok::render::res_xs<struct vostok::render::gs_data> const *)`

---

## 🟡 REWORKED · `vostok::network_core` (+6 / −4)

- `+` `default_message_converter`
- `+` `delete_udp_match_packet(class vostok::memory::single_size_buffer_allocator<684, class vostok::threading::multi_threading_policy> &, class vostok::network_core::udp_match_packet *&)`
- `+` `finalize_logging`
- `+` `initialize_logging`
- `+` `logging_callback`
- `+` `new_udp_match_packet(class vostok::memory::single_size_buffer_allocator<684, class vostok::threading::multi_threading_policy> &)`
- `−` `delete_udp_match_packet(class vostok::memory::single_size_buffer_allocator<1364, class vostok::threading::multi_threading_policy> &, class vostok::network_core::udp_match_packet *&)`
- `−` `new_udp_match_packet(class vostok::memory::single_size_buffer_allocator<1364, class vostok::threading::multi_threading_policy> &)`
- `−` `operator>=(struct vostok::network_core::udp_match_stats const &, struct vostok::network_core::udp_match_stats const &)`
- `−` `operator>=(struct vostok::network_core::udp_match_stream_stats const &, struct vostok::network_core::udp_match_stream_stats const &)`

---

## 🔴 REMOVED · `survarium::jump_logic` (+0 / −10)

- `−` `get_animation(enum survarium::jump_animation_parts) const`
- `−` `get_animation(enum survarium::jump_type_enum, enum survarium::jump_animation_parts) const`
- `−` `get_move_animation(void) const`
- `−` `get_preface_animation_timescale(float) const`
- `−` `initialize(void)`
- `−` `initialize_logic(void)`
- `−` `initialize_weight_for_on_site_move_animation(void)`
- `−` `jump_logic(class survarium::weapon_user_animations_selector &, class survarium::player_logic_jump_state &)`
- `−` `serialize(class vostok::network_core::buffer_writer const &, class vostok::network_core::buffer_writer const *) const`
- `−` `~jump_logic(void)`

---

## 🟢 NEW · `vostok::configs` (+9)

- `+` `construct`
- `+` `create_binary_config(class vostok::mutable_buffer const &, class vostok::memory::base_allocator &)`
- `+` `create_binary_config_buffer`
- `+` `create_binary_config_buffer_impl(class vostok::configs::binary_config_value &, class vostok::memory::stream &)`
- `+` `fill_info_for_fix_up`
- `+` `free_memory`
- `+` `modify_binary_config(class vostok::configs::binary_config_value const &, class boost::intrusive::set<struct vostok::configs::modifier, struct boost::intrusive::member_hook<struct vostok::configs::modifier, class boost::intrusive::set_member_hook<struct boost::intrusive::none, struct boost::intrusive::none, struct boost::intrusive::none, struct boost::intrusive::none>, 32>, struct boost::intrusive::compare<struct vostok::configs::modifier::comparer>, struct boost::intrusive::none, struct boost::intrusive::none> const &, class vostok::memory::base_allocator &)`
- `+` `process_string`
- `+` `sort`

---

## 🟡 REWORKED · `survarium::grenade_set_core_cook` (+4 / −5)

- `+` `finish_query(class vostok::resources::query_result_for_cook *, class survarium::grenade_set_core *)`
- `+` `new_derived_resource(void *const, class vostok::configs::binary_config_value const &, unsigned char)`
- `+` `query_for_derived_resources(class vostok::resources::query_result_for_cook *, class survarium::grenade_set_core *, struct survarium::grenade_set_cook_data const &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>)`
- `+` `translate_query(class vostok::resources::query_result_for_cook &)`
- `−` `finish_query(class vostok::resources::query_result_for_cook *, class survarium::grenade_set_core *)`
- `−` `get_derived_resource_size(void)`
- `−` `new_derived_resource(void *const)`
- `−` `query_for_derived_resources(class vostok::resources::query_result_for_cook *, class survarium::grenade_set_core *, struct survarium::grenade_set_cook_data const &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>)`
- `−` `translate_query(class vostok::resources::query_result_for_cook &)`

---

## 🟡 REWORKED · `survarium::base_player` (+4 / −5)

- `+` `generate_hit_event(unsigned int, unsigned char, unsigned char, float, float, class survarium::bullet const *, bool, unsigned short)`
- `+` `generate_killed_event(unsigned int, unsigned char, char const *, class survarium::inventory_item const *, class survarium::bullet const *)`
- `+` `hit(unsigned int, struct survarium::hit_initiator const *const, class vostok::collision::bone_collision_data const &, enum survarium::hit_type_enum, float, float, class survarium::bullet *const, class survarium::inventory_item const *const)`
- `+` `hit(unsigned int, struct survarium::hit_initiator const *const, unsigned int, enum survarium::hit_type_enum, float, float, class survarium::bullet *const, class vostok::math::float3const &, enum survarium::triangle_orientation, class survarium::inventory_item const *const)`
- `−` `generate_hit_event(unsigned int, unsigned char, unsigned char, float, float, class survarium::bullet const *, bool)`
- `−` `generate_killed_event(unsigned int, unsigned char, char const *, unsigned short, class survarium::bullet const *)`
- `−` `hit(unsigned int, struct survarium::hit_initiator const *const, class vostok::collision::bone_collision_data const &, enum survarium::hit_type_enum, float, float, class survarium::bullet *const, unsigned short)`
- `−` `hit(unsigned int, struct survarium::hit_initiator const *const, unsigned int, enum survarium::hit_type_enum, float, float, class survarium::bullet *const, class vostok::math::float3const &, enum survarium::triangle_orientation, unsigned short)`
- `−` `jump(enum survarium::jump_type_enum)`

---

## 🟢 NEW · `survarium::network_stats_orders_channel` (+9)

- `+` `add_row(struct survarium::flash_value &, unsigned int, char const *const, class vostok::network_core::sequence_number<unsigned short> const &)`
- `+` `advance(unsigned int)`
- `+` `fill_data(struct vostok::network_core::udp_match_raw_stats &, unsigned int)`
- `+` `fill_header(void)`
- `+` `hide_movie(class survarium::base_game_scene &)`
- `+` `initialize_header(void)`
- `+` `network_stats_orders_channel(class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `+` `on_enabled_changed(char const *)`
- `+` `update_position(unsigned int, unsigned int)`

---

## 🟢 NEW · `survarium::network_stats_packets` (+9)

- `+` `add_row(struct survarium::flash_value &, unsigned int, char const *const, struct vostok::network_core::udp_match_bytes_count_stats &, unsigned int)`
- `+` `advance(unsigned int)`
- `+` `fill_data(struct vostok::network_core::udp_match_raw_stats &, unsigned int)`
- `+` `fill_header(void)`
- `+` `hide_movie(class survarium::base_game_scene &)`
- `+` `initialize_header(void)`
- `+` `network_stats_packets(class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `+` `on_enabled_changed(char const *)`
- `+` `update_position(unsigned int, unsigned int)`

---

## 🟢 NEW · `survarium::network_stats_packets_sequence` (+9)

- `+` `add_row(struct survarium::flash_value &, unsigned int, char const *const, struct vostok::network_core::udp_match_raw_stats &, unsigned int)`
- `+` `advance(unsigned int)`
- `+` `fill_data(struct vostok::network_core::udp_match_raw_stats &, unsigned int)`
- `+` `fill_header(void)`
- `+` `hide_movie(class survarium::base_game_scene &)`
- `+` `initialize_header(void)`
- `+` `network_stats_packets_sequence(class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `+` `on_enabled_changed(char const *)`
- `+` `update_position(unsigned int, unsigned int)`

---

## 🟢 NEW · `survarium::network_stats_ports` (+9)

- `+` `add_column(struct survarium::flash_value (&)[8], unsigned int, struct vostok::network_core::udp_match_port_sent_received_stats &, unsigned int)`
- `+` `advance(unsigned int)`
- `+` `fill_data(struct vostok::network_core::udp_match_raw_stats &, unsigned int, unsigned short, unsigned short)`
- `+` `fill_header(void)`
- `+` `hide_movie(class survarium::base_game_scene &)`
- `+` `initialize_header_impl(unsigned short, unsigned short)`
- `+` `network_stats_ports(class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `+` `on_enabled_changed(char const *)`
- `+` `update_position(unsigned int, unsigned int)`

---

## 🟢 NEW · `survarium::network_stats_received_messages` (+9)

- `+` `add_row(struct survarium::flash_value &, unsigned int, char const *const, struct vostok::network_core::udp_match_received_message_stats &, struct vostok::network_core::udp_match_raw_stats const &, unsigned int)`
- `+` `advance(unsigned int)`
- `+` `fill_data(struct vostok::network_core::udp_match_raw_stats &, unsigned int)`
- `+` `fill_header(void)`
- `+` `hide_movie(class survarium::base_game_scene &)`
- `+` `initialize_header(void)`
- `+` `network_stats_received_messages(class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `+` `on_enabled_changed(char const *)`
- `+` `update_position(unsigned int, unsigned int)`

---

## 🟢 NEW · `survarium::network_stats_seconds` (+9)

- `+` `add_row(struct survarium::flash_value &, unsigned int, char const *const, struct vostok::network_core::udp_match_raw_stats &, unsigned int)`
- `+` `advance(unsigned int)`
- `+` `fill_data(struct vostok::network_core::udp_match_raw_stats &, unsigned int)`
- `+` `fill_header(void)`
- `+` `hide_movie(class survarium::base_game_scene &)`
- `+` `initialize_header(void)`
- `+` `network_stats_seconds(class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `+` `on_enabled_changed(char const *)`
- `+` `update_position(unsigned int, unsigned int)`

---

## 🟢 NEW · `survarium::network_stats_sent_messages` (+9)

- `+` `add_row(struct survarium::flash_value &, unsigned int, char const *const, struct vostok::network_core::udp_match_sent_message_stats &, struct vostok::network_core::udp_match_raw_stats const &, unsigned int)`
- `+` `advance(unsigned int)`
- `+` `fill_data(struct vostok::network_core::udp_match_raw_stats &, unsigned int)`
- `+` `fill_header(void)`
- `+` `hide_movie(class survarium::base_game_scene &)`
- `+` `initialize_header(void)`
- `+` `network_stats_sent_messages(class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `+` `on_enabled_changed(char const *)`
- `+` `update_position(unsigned int, unsigned int)`

---

## 🟡 REWORKED · `vostok::network_core::udp_match_client` (+7 / −2)

- `+` `connect_impl(class vostok::network_core::udp_match_packet *const, unsigned int)`
- `+` `destroy_packet(class vostok::network_core::udp_match_packet &)`
- `+` `duplicate_packet_send_handler(class boost::system::error_code const &, unsigned int)`
- `+` `enqueue(unsigned char, class vostok::network_core::buffer_reader &, unsigned int)`
- `+` `on_delayed_packet_received(class vostok::network_core::udp_match_packet &, class boost::asio::ip::basic_endpoint<class boost::asio::ip::udp> const &)`
- `+` `on_error(enum vostok::network_core::client_error_codes_enum, class boost::system::error_code)`
- `+` `udp_match_client(class boost::asio::io_service &, class vostok::memory::single_size_buffer_allocator<684, class vostok::threading::multi_threading_policy> &, struct vostok::network_core::udp_match_packets_orderer &, class vostok::network_core::udp_network_flow_emulator *)`
- `−` `enqueue(unsigned char, class vostok::network_core::buffer_reader &)`
- `−` `udp_match_client(class boost::asio::io_service &, class vostok::memory::single_size_buffer_allocator<1364, class vostok::threading::multi_threading_policy> &, struct vostok::network_core::udp_match_packets_orderer &, class vostok::network_core::udp_network_flow_emulator *)`

---

## 🟡 REWORKED · `survarium::weapon_cook` (+4 / −4)

- `+` `allocate_weapon(class vostok::configs::binary_config_value const &, class survarium::base_game_scene &, unsigned int, unsigned char, unsigned char)`
- `+` `on_weapon_config_loaded(class vostok::resources::queries_result &, void *, bool)`
- `+` `on_weapon_subresources_ready(class vostok::resources::queries_result &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class survarium::weapon_core *, void *, bool)`
- `+` `query_weapon_states(class vostok::resources::query_result_for_cook *const, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class survarium::weapon_core *, void *, bool)`
- `−` `allocate_weapon(class survarium::base_game_scene &, unsigned int, unsigned char, unsigned char)`
- `−` `on_weapon_config_loaded(class vostok::resources::queries_result &)`
- `−` `on_weapon_subresources_ready(class vostok::resources::queries_result &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class survarium::weapon_core *)`
- `−` `query_weapon_states(class vostok::resources::query_result_for_cook *const, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class survarium::weapon_core *)`

---

## 🟡 REWORKED · `survarium::game_world_core` (+5 / −3)

- `+` `discard_input(unsigned char, unsigned int)`
- `+` `enter_match(unsigned char, unsigned int)`
- `+` `leave_match(unsigned char, unsigned int)`
- `+` `serialize(void)`
- `+` `tick_game_objects(unsigned int, unsigned int)`
- `−` `discard_input(unsigned char, unsigned int)`
- `−` `enter_match(unsigned char, unsigned int)`
- `−` `leave_match(unsigned char, unsigned int)`

---

## 🟢 NEW · `survarium::network_stats_rejected_messages` (+8)

- `+` `add_row(struct survarium::flash_value &, unsigned int, struct vostok::network_core::udp_match_received_message_stats &, unsigned int)`
- `+` `advance(unsigned int)`
- `+` `fill_data(struct vostok::network_core::udp_match_raw_stats &, unsigned int)`
- `+` `hide_movie(class survarium::base_game_scene &)`
- `+` `initialize_header(void)`
- `+` `network_stats_rejected_messages(class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `+` `on_enabled_changed(char const *)`
- `+` `update_position(unsigned int, unsigned int)`

---

## 🟡 REWORKED · `survarium::player_stamina` (+2 / −6)

- `+` `sprint(unsigned int)`
- `+` `tick(unsigned int, bool, bool)`
- `−` `clear_subscribers(void)`
- `−` `deplete(bool)`
- `−` `jump(void)`
- `−` `player_stamina(struct survarium::stamina_base_parameters const &, class survarium::player_params_modifiers_container &)`
- `−` `subscribe_on_depletion(struct survarium::player_stamina_subscriber *const)`
- `−` `~player_stamina(void)`

---

## 🟡 REWORKED · `survarium::weapon_core_cook` (+4 / −4)

- `+` `on_core_subresources_ready(class vostok::resources::queries_result &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class survarium::weapon_core *, void *, bool)`
- `+` `on_weapon_config_loaded(class vostok::resources::queries_result &, void *, bool)`
- `+` `process_loading_weapon_core(class vostok::resources::query_result_for_cook *const, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class survarium::weapon_core *, void *, bool)`
- `+` `query_weapon_states(class vostok::resources::query_result_for_cook *const, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class survarium::weapon_core *, void *, bool)`
- `−` `on_core_subresources_ready(class vostok::resources::queries_result &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class survarium::weapon_core *)`
- `−` `on_weapon_config_loaded(class vostok::resources::queries_result &)`
- `−` `process_loading_weapon_core(class vostok::resources::query_result_for_cook *const, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class survarium::weapon_core *)`
- `−` `query_weapon_states(class vostok::resources::query_result_for_cook *const, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class survarium::weapon_core *)`

---

## 🟡 REWORKED · `vostok::network_core::udp_match_connection` (+4 / −4)

- `+` `connect(unsigned int, class vostok::network_core::udp_match_packet *)`
- `+` `enqueue(unsigned char, class vostok::network_core::buffer_reader &, unsigned int)`
- `+` `process_incoming_packet<class vostok::network_core::process_packet_predicate>(class vostok::network_core::buffer_reader &, class vostok::network_core::process_packet_predicate const &, unsigned short)`
- `+` `udp_match_connection(class vostok::memory::single_size_buffer_allocator<684, class vostok::threading::multi_threading_policy> &, struct vostok::network_core::udp_match_packets_orderer &, unsigned int, unsigned int, char const *const, unsigned char, unsigned char)`
- `−` `connect(class vostok::network_core::udp_match_packet *)`
- `−` `enqueue(unsigned char, class vostok::network_core::buffer_reader &)`
- `−` `process_incoming_packet<class vostok::network_core::process_packet_predicate>(class vostok::network_core::buffer_reader &, class vostok::network_core::process_packet_predicate const &)`
- `−` `udp_match_connection(class vostok::memory::single_size_buffer_allocator<1364, class vostok::threading::multi_threading_policy> &, struct vostok::network_core::udp_match_packets_orderer &, unsigned int, unsigned int, char const *const)`

---

## 🟡 REWORKED · `vostok::variant<32>` (+7 / −1)

- `+` `set<struct survarium::item_config_cook_data>(struct survarium::item_config_cook_data const &)`
- `+` `set<struct survarium::pvp_match_core_query_user_data>(struct survarium::pvp_match_core_query_user_data const &)`
- `+` `set<unsigned int>(unsigned int const &)`
- `+` `try_get<struct survarium::item_config_cook_data>(struct survarium::item_config_cook_data &)`
- `+` `try_get<struct survarium::item_cook_data>(struct survarium::item_cook_data &)`
- `+` `try_get<unsigned int>(unsigned int &)`
- `+` `~variant<32>(void)`
- `−` `try_get<unsigned short>(unsigned short &)`

---

## 🟡 REWORKED · `vostok::physics::bt_character_controller` (+2 / −6)

- `+` `can_jump(void) const`
- `+` `get_transform(void) const`
- `−` `can_stand(void) const`
- `−` `initialize(class vostok::math::float4x4const &, unsigned int, unsigned char)`
- `−` `is_activated(void) const`
- `−` `is_in_jump(void) const`
- `−` `set_crouch(bool)`
- `−` `~bt_character_controller(void)`

---

## 🟢 NEW · `survarium::base_local_network_client` (+8)

- `+` `attach_to_next_player(void)`
- `+` `attach_to_player(class vostok::resources::resource_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base>)`
- `+` `attach_to_prev_player(void)`
- `+` `attach_to_target_player(void)`
- `+` `detach_from_player(void)`
- `+` `get_active_player(unsigned char) const`
- `+` `get_player(unsigned char) const`
- `+` `~base_local_network_client(void)`

---

## 🟡 REWORKED · `vostok::network::match_client` (+5 / −2)

- `+` `match_client(struct vostok::network::world &, struct vostok::network_core::udp_match_packets_orderer &, struct vostok::network_core::udp_network_flow_emulator_options const *, class vostok::timing::timer const &)`
- `+` `new_packet_impl(unsigned char)`
- `+` `on_packet_received(unsigned char, class vostok::network_core::buffer_reader &, unsigned int)`
- `+` `send_heart_beat(void)`
- `+` `stats(void) const`
- `−` `match_client(struct vostok::network::world &, struct vostok::network_core::udp_match_packets_orderer &, struct vostok::network_core::udp_network_flow_emulator_options const *)`
- `−` `on_packet_received(unsigned char, class vostok::network_core::buffer_reader &)`

---

## 🟡 REWORKED · `vostok::render::effect_manager` (+7)

- `+` `create_effect<class vostok::render::effect_probe_brdf>(class render::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base> *)'::`2'::descriptor_object::`dynamic atexit destructor'(void)`
- `+` `create_effect<class vostok::render::effect_probe_brdf>(class vostok::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base> *)`
- `+` `create_effect<class vostok::render::effect_ssr>(class render::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base> *)'::`2'::descriptor_object::`dynamic atexit destructor'(void)`
- `+` `create_effect<class vostok::render::effect_ssr>(class vostok::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base> *)`
- `+` `create_effect<class vostok::render::effect_ssr_mask>(class render::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base> *)'::`2'::descriptor_object::`dynamic atexit destructor'(void)`
- `+` `create_effect<class vostok::render::effect_ssr_mask>(class vostok::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base> *)`
- `+` `delete_effect_technique(class vostok::render::res_shader_technique const *)`

---

## 🟡 REWORKED · `vostok::render::scene` (+3 / −4)

- `+` `process_pending_move_texture_instances(void)`
- `+` `render_lines(bool, bool)`
- `+` `render_triangles(bool, bool)`
- `−` `draw_lines(class vostok::buffer_vector<struct vostok::render::vertex_colored> const &, class vostok::buffer_vector<unsigned short> const &)`
- `−` `draw_triangles(class vostok::buffer_vector<struct vostok::render::vertex_colored> const &, class vostok::buffer_vector<unsigned short> const &)`
- `−` `render_lines(bool)`
- `−` `render_triangles(bool)`

---

## 🟡 REWORKED · `survarium::booby_trap_set_core_cook` (+2 / −4)

- `+` `new_derived_resource(class vostok::configs::binary_config_value const &, unsigned char, struct vostok::physics::world &, class vostok::resources::resource_ptr<class survarium::game_material_manager, class vostok::resources::unmanaged_intrusive_base> const &, void *const)`
- `+` `translate_query(class vostok::resources::query_result_for_cook &)`
- `−` `get_derived_resource_size(void)`
- `−` `new_derived_resource(struct vostok::physics::world &, class vostok::resources::resource_ptr<class survarium::game_material_manager, class vostok::resources::unmanaged_intrusive_base> const &, void *const)`
- `−` `query_for_derived_resources(class vostok::resources::query_result_for_cook *, class survarium::booby_trap_set_core *, struct survarium::booby_trap_set_cook_data const &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>)`
- `−` `translate_query(class vostok::resources::query_result_for_cook &)`

---

## 🟡 REWORKED · `survarium::weapon_core` (+3 / −3)

- `+` `apply_look_pitch(float)`
- `+` `look_pitch(void) const`
- `+` `weapon_core(class vostok::configs::binary_config_value const &)`
- `−` `set_inventory(class survarium::inventory *, enum survarium::profile_slot_enum)`
- `−` `update_recoil(unsigned int)`
- `−` `weapon_core(void)`

---

## 🟡 REWORKED · `survarium::booby_trap_core` (+3 / −3)

- `+` `fixed_tick(unsigned int, unsigned int)`
- `+` `hit(unsigned int, struct survarium::hit_initiator const *const, class vostok::collision::bone_collision_data const &, enum survarium::hit_type_enum, float, float, class survarium::bullet *const, class survarium::inventory_item const *const)`
- `+` `hit(unsigned int, struct survarium::hit_initiator const *const, unsigned int, enum survarium::hit_type_enum, float, float, class survarium::bullet *const, class vostok::math::float3const &, enum survarium::triangle_orientation, class survarium::inventory_item const *const)`
- `−` `hit(unsigned int, struct survarium::hit_initiator const *const, class vostok::collision::bone_collision_data const &, enum survarium::hit_type_enum, float, float, class survarium::bullet *const, unsigned short)`
- `−` `hit(unsigned int, struct survarium::hit_initiator const *const, unsigned int, enum survarium::hit_type_enum, float, float, class survarium::bullet *const, class vostok::math::float3const &, enum survarium::triangle_orientation, unsigned short)`
- `−` `tick(unsigned int, unsigned int)`

---

## 🟡 REWORKED · `survarium::items_cook` (+3 / −3)

- `+` `create_item_and_finish_query(class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class vostok::resources::query_result_for_cook *)`
- `+` `on_config_ready(class vostok::resources::queries_result &)`
- `+` `translate_query(class vostok::resources::query_result_for_cook &)`
- `−` `create_item_and_finish_query(enum survarium::item_types_enum, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class vostok::resources::query_result_for_cook *)`
- `−` `on_config_ready(class vostok::resources::queries_result &, class vostok::resources::query_result_for_cook *)`
- `−` `translate_query(class vostok::resources::query_result_for_cook &)`

---

## 🟢 NEW · `survarium::net_stats` (+6)

- `+` `add_text_cell(class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &, char const *const, unsigned int, enum survarium::net_stats::column_info::text_align, unsigned int, struct survarium::flash_value &)`
- `+` `last_values_max(class vostok::circular_buffer<struct stlp_std::pair<unsigned int, unsigned int>, 128> const &, unsigned int)`
- `+` `last_values_sum`
- `+` `sprintf_big_number(char (&)[32], unsigned int, unsigned int, unsigned int, char const *const, char const *const, char const *const)`
- `+` `sprintf_big_number_helper(char (&)[32], unsigned int, unsigned int, char const *const, char, char const *const)`
- `+` `sprintf_time_4_digits(char (&)[32], unsigned int)`

---

## 🟢 NEW · `survarium::match_time_vi_spawn_rule` (+5)

- `+` `deserialize(class vostok::network_core::buffer_reader &, unsigned int)`
- `+` `match_time_vi_spawn_rule(unsigned int)`
- `+` `on_match_ready(unsigned int)`
- `+` `serialize(class vostok::network_core::buffer_writer const &, unsigned int) const`
- `+` `tick(unsigned int, unsigned int)`

---

## 🟡 REWORKED · `character_step_down_sweep_test_callback` (+3 / −2)

- `+` `character_step_down_sweep_test_callback(class btCollisionWorld &, class btCollisionObject &, class btVector3const &, float, class btVector3const &, float, float, float)`
- `+` `get_normal_for_impassable_slope(class btVector3const &) const`
- `+` `get_normal_for_terminal_passable_slope(class btVector3const &) const`
- `−` `character_step_down_sweep_test_callback(class btCollisionWorld &, class btCollisionObject &, class btVector3const &, float, class btVector3const &, float, float)`
- `−` `get_normal_for_impassable_slope(class btVector3const &)`

---

## 🟢 NEW · `survarium::swear_filter_cook` (+5)

- `+` `count_buffer_size(class vostok::configs::binary_config_value &, wchar_t *)`
- `+` `delete_resource(class vostok::resources::resource_base *)`
- `+` `fill_buffers(unsigned int, class vostok::configs::binary_config_value, wchar_t *, unsigned char *const, wchar_t **)`
- `+` `on_resources_loaded(class vostok::resources::queries_result &)`
- `+` `translate_query(class vostok::resources::query_result_for_cook &)`

---

## 🟡 REWORKED · `survarium::chat_handler` (+4 / −1)

- `+` `add_squad_tab(enum vostok::messaging::message_channel_enum)`
- `+` `filter_message(char (&)[256])`
- `+` `on_message_typed(char const (&)[256], enum vostok::messaging::message_channel_enum)`
- `+` `remove_squad_tab(void)`
- `−` `on_message_typed(char const *, enum vostok::messaging::message_channel_enum)`

---

## 🟡 REWORKED · `survarium::network_client` (+3 / −2)

- `+` `draw_match_stats(unsigned int)`
- `+` `register_message_in_stats(enum survarium::input_action_enum, enum vostok::match::server::messages_enum) const`
- `+` `try_send_all(unsigned int, bool)`
- `−` `on_new_input(unsigned int)`
- `−` `try_send_all(unsigned int, bool)`

---

## 🟢 NEW · `survarium::replay_network_client` (+5)

- `+` `close_current_match(enum vostok::network_core::disconnect_event_types_enum)`
- `+` `load_replay(class vostok::replay_match_reader *const)`
- `+` `on_match_replay_ready(class vostok::resources::queries_result &, class vostok::replay_match_reader *const)`
- `+` `replay_network_client(class survarium::game &)`
- `+` `unload(void)`

---

## 🟡 REWORKED · `vostok::render::device` (+5)

- `+` `device(unsigned __int64, bool)`
- `+` `find_outputs(void)`
- `+` `get_max_supported_resolution(void) const`
- `+` `get_output(unsigned int) const`
- `+` `~device(void)`

---

## 🟡 REWORKED · `vostok::render::texture_cook_wrapper` (+4 / −1)

- `+` `on_dds_header_ready(class vostok::resources::query_result_for_cook *, class vostok::fs_new::asynchronous_device_interface *, class vostok::fs_new::native_path_string *, unsigned __int64, unsigned char *, unsigned __int64, unsigned __int64, bool)`
- `+` `on_fs_iterators_ready_converted(class vostok::resources::queries_result &)`
- `+` `query_converted_texture(class vostok::vfs::vfs_iterator, class vostok::resources::query_result_for_cook *)`
- `+` `query_converted_texture_mip(class vostok::vfs::vfs_iterator, class vostok::resources::query_result_for_cook *)`
- `−` `query_converted_texture(class vostok::resources::query_result_for_cook *)`

---

## 🟡 REWORKED · `survarium::items_dictionary` (+3 / −2)

- `+` `item_by_id(unsigned int) const`
- `+` `item_modification_by_id(unsigned int) const`
- `+` `items_dictionary(class vostok::memory::base_allocator *, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &)`
- `−` `item_by_id(unsigned int) const`
- `−` `items_dictionary(class vostok::memory::base_allocator *, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &)`

---

## 🟢 NEW · `vostok::network_core::udp_match_message_item_flow_stats` (+5)

- `+` `add(unsigned int)`
- `+` `remove(unsigned int, unsigned int)`
- `+` `udp_match_message_item_flow_stats(struct vostok::network_core::udp_match_message_item_flow_stats const &)`
- `+` `udp_match_message_item_flow_stats(void)`
- `+` `~udp_match_message_item_flow_stats(void)`

---

## 🟡 REWORKED · `vostok::render::renderer` (+4 / −1)

- `+` `blur(class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, unsigned int)`
- `+` `downsample(class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, class vostok::intrusive_ptr<class vostok::render::res_texture, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, bool)`
- `+` `draw_top_dip_models_list(struct vostok::ui::world &, unsigned int, unsigned int, unsigned int) const`
- `+` `prepare_scene_to_render(class vostok::render::scene *)`
- `−` `downsample(class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, class vostok::intrusive_ptr<class vostok::render::res_texture, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>)`

---

## 🟡 REWORKED · `vostok::render::stage_shadow_direct` (+2 / −3)

- `+` `prepare_visibile_objects(class vostok::fixed_vector<struct vostok::render::caster_model, 4096> *, class vostok::memory::base_allocator *, class vostok::math::float3const &, unsigned int, unsigned int, unsigned int)`
- `+` `render_models(class vostok::fixed_vector<struct vostok::render::caster_model, 4096> &, class vostok::math::float3const &, unsigned int, bool)`
- `−` `get_texture_space_transform(void) const`
- `−` `prepare_visibile_objects(class vostok::fixed_vector<struct vostok::render::caster_model, 2048> *, class vostok::memory::base_allocator *, class vostok::math::float3const &, unsigned int, unsigned int, unsigned int)`
- `−` `render_models(class vostok::fixed_vector<struct vostok::render::caster_model, 2048> &, class vostok::math::float3const &, unsigned int, bool)`

---

## 🟡 REWORKED · `vostok::memory` (+3 / −2)

- `+` `delete_helper<class vostok::memory::pthreads3_allocator, class vostok::console_commands::logging_filters_console_command>(class vostok::memory::pthreads3_allocator &, class vostok::console_commands::logging_filters_console_command *&, char const *const, char const *const, unsigned int)`
- `+` `delete_helper<class vostok::memory::pthreads3_allocator, class vostok::logging::fs_new_device_impl>(class vostok::memory::pthreads3_allocator &, class vostok::logging::fs_new_device_impl *&, char const *const, char const *const, unsigned int)`
- `+` `delete_helper<class vostok::memory::pthreads3_allocator, class vostok::logging::memory_base_allocator_wrapper>(class vostok::memory::pthreads3_allocator &, class vostok::logging::memory_base_allocator_wrapper *&, char const *const, char const *const, unsigned int)`
- `−` `delete_helper<class vostok::memory::base_allocator, class vostok::animation::legs_ik_drawer>(class vostok::memory::base_allocator &, class vostok::animation::legs_ik_drawer *&, char const *const, char const *const, unsigned int)`
- `−` `zero(void *, unsigned int)`

---

## 🔴 REMOVED · `vostok::render::debug::draw_lines_command` (+0 / −5)

- `−` `ctor<2, 2>(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::engine::world &, class vostok::memory::base_allocator &, struct vostok::render::vertex_colored const (&)[2], unsigned short const (&)[2], bool)`
- `−` `ctor<6, 6>(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::engine::world &, class vostok::memory::base_allocator &, struct vostok::render::vertex_colored const (&)[6], unsigned short const (&)[6], bool)`
- `−` `ctor<class vostok::buffer_vector>(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::engine::world &, class vostok::memory::base_allocator &, class vostok::buffer_vector<struct vostok::render::vertex_colored> const &, class vostok::buffer_vector<unsigned short> const &, bool)`
- `−` `defer_execution(void)`
- `−` `execute(void)`

---

## 🔴 REMOVED · `vostok::render::debug::draw_triangles_command` (+0 / −5)

- `−` `ctor<3, 3>(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::engine::world &, class vostok::memory::base_allocator &, struct vostok::render::vertex_colored const (&)[3], unsigned short const (&)[3], bool)`
- `−` `defer_execution(void)`
- `−` `draw_triangles_command(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::engine::world &, class vostok::memory::base_allocator &, class vostok::buffer_vector<struct vostok::render::vertex_colored> const &, class vostok::buffer_vector<unsigned short> const &, bool)`
- `−` `execute(void)`
- `−` `~draw_triangles_command(void)`

---

## 🟡 REWORKED · `survarium::medkit` (+1 / −3)

- `+` `medkit(class vostok::configs::binary_config_value const &)`
- `−` `load(class vostok::configs::binary_config_value)`
- `−` `medkit(void)`
- `−` `set_inventory(class survarium::inventory *, enum survarium::profile_slot_enum)`

---

## 🟡 REWORKED · `survarium::match_client` (+2 / −2)

- `+` `match_client(struct vostok::network::world &, class vostok::timing::timer const &)`
- `+` `stats(void) const`
- `−` `get_stats(void) const`
- `−` `match_client(struct vostok::network::world &)`

---

## 🟢 NEW · `vostok::network_core::udp_match_bytes_count_stats` (+4)

- `+` `append(unsigned int, unsigned int)`
- `+` `udp_match_bytes_count_stats(struct vostok::network_core::udp_match_bytes_count_stats const &)`
- `+` `udp_match_bytes_count_stats(void)`
- `+` `~udp_match_bytes_count_stats(void)`

---

## 🟡 REWORKED · `vostok::network_core::udp_network_flow_emulator` (+2 / −2)

- `+` `tick(unsigned int)`
- `+` `udp_network_flow_emulator(class vostok::memory::base_allocator &, struct vostok::network_core::udp_network_flow_emulator_options const &, unsigned int)`
- `−` `add_packet(unsigned char *, unsigned int, class boost::asio::ip::basic_endpoint<class boost::asio::ip::udp> const &, unsigned int, unsigned int, struct vostok::network_core::socket_handler *const)`
- `−` `udp_network_flow_emulator(class vostok::memory::base_allocator &, class vostok::memory::single_size_buffer_allocator<1364, class vostok::threading::multi_threading_policy> &, struct vostok::network_core::udp_network_flow_emulator_options const &)`

---

## 🟢 NEW · `vostok::network_core::lost_packets_detector` (+4)

- `+` `call_predicate_on_every_bit<struct vostok::network_core::not_received_packets_predicate>(unsigned __int64const &, unsigned int, class vostok::network_core::sequence_number<unsigned short> const &, struct vostok::network_core::not_received_packets_predicate const &)`
- `+` `call_predicate_on_every_bit<struct vostok::network_core::sent_lost_packets_predicate>(unsigned __int64const &, unsigned int, class vostok::network_core::sequence_number<unsigned short> const &, struct vostok::network_core::sent_lost_packets_predicate const &)`
- `+` `register_packet<struct vostok::network_core::not_received_packets_predicate>(class vostok::network_core::sequence_number<unsigned short> const &, unsigned int, struct vostok::network_core::not_received_packets_predicate const &)`
- `+` `register_packet<struct vostok::network_core::sent_lost_packets_predicate>(class vostok::network_core::sequence_number<unsigned short> const &, unsigned int, struct vostok::network_core::sent_lost_packets_predicate const &)`

---

## 🟡 REWORKED · `survarium::base_game_scene` (+2 / −2)

- `+` `hide_movie(class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `+` `show_movie(class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `−` `hide_movie(class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> &)`
- `−` `show_movie(class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> &)`

---

## 🟡 REWORKED · `vostok::physics` (+1 / −2)

- `+` `perpindicularComponent(class btVector3const &, class btVector3const &)`
- `−` `getNormalizedVector`
- `−` `set_max_slope_angle`

---

## 🟡 REWORKED · `survarium::oxygen_tank` (+1 / −2)

- `+` `oxygen_tank(class vostok::configs::binary_config_value const &)`
- `−` `load(class vostok::configs::binary_config_value)`
- `−` `oxygen_tank(void)`

---

## 🟡 REWORKED · `vostok::render::statistics` (+3)

- `+` `is_visible_group(struct vostok::render::statistics_group *) const`
- `+` `render(struct vostok::ui::world &, unsigned int, unsigned int)`
- `+` `start(void)`

---

## 🟡 REWORKED · `survarium::player_logic_sprint_state` (+1 / −2)

- `+` `get_hands_idle_lexeme(class vostok::mutable_buffer &, class vostok::animation::mixing::animation_lexeme &) const`
- `−` `deserialize(class vostok::network_core::buffer_reader &, class vostok::network_core::buffer_reader *)`
- `−` `on_stamina_depleted(bool &)`

---

## 🟡 REWORKED · `survarium::game` (+3)

- `+` `on_clipboard_changed(wchar_t const *)`
- `+` `on_match_stats_movies_loaded(class vostok::resources::queries_result &)`
- `+` `set_time_in_ms(unsigned int)`

---

## 🟡 REWORKED · `vostok::network::login_client_impl` (+3)

- `+` `process_ping_answer(class boost::system::error_code const &, unsigned int)`
- `+` `schedule_ping(unsigned int)`
- `+` `start_ping_answer_acception(void)`

---

## 🟢 NEW · `vostok::render::texture_mip_cook` (+3)

- `+` `calculate_resource_size(class vostok::const_buffer, bool)`
- `+` `create_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>)`
- `+` `on_dds_body_ready(class vostok::resources::query_result_for_cook *, struct vostok::render::texture_mip_cook_data const *, bool)`

---

## 🟡 REWORKED · `survarium::artefact_base` (+1 / −2)

- `+` `artefact_base(class vostok::configs::binary_config_value const &, class vostok::resources::resource_ptr<class survarium::game_effect_emitter, class vostok::resources::unmanaged_intrusive_base> const &)`
- `−` `artefact_base(struct survarium::artefact_base::config const &, class vostok::resources::resource_ptr<class survarium::game_effect_emitter, class vostok::resources::unmanaged_intrusive_base> const &)`
- `−` `load_config(class vostok::configs::binary_config_value const &)`

---

## 🟡 REWORKED · `survarium::booby_trap_set_core` (+1 / −2)

- `+` `booby_trap_set_core(class vostok::configs::binary_config_value const &, unsigned char, struct vostok::physics::world &, class vostok::resources::resource_ptr<class survarium::game_material_manager, class vostok::resources::unmanaged_intrusive_base> const &)`
- `−` `booby_trap_set_core(struct vostok::physics::world &, class vostok::resources::resource_ptr<class survarium::game_material_manager, class vostok::resources::unmanaged_intrusive_base> const &)`
- `−` `load(class vostok::configs::binary_config_value const &, unsigned char)`

---

## 🟡 REWORKED · `survarium::gather_victory_items_rule` (+2 / −1)

- `+` `gather_victory_items_rule(unsigned int)`
- `+` `~gather_victory_items_rule(void)`
- `−` `gather_victory_items_rule(unsigned int)`

---

## 🟡 REWORKED · `survarium::jump_logic_base_state` (+1 / −2)

- `+` `jump_logic_base_state(class survarium::player_logic_jump_state &)`
- `−` `jump_logic_base_state(class survarium::jump_logic &)`
- `−` `set_user(class survarium::base_player &)`

---

## 🟡 REWORKED · `survarium::grenade_set_core` (+1 / −2)

- `+` `grenade_set_core(class vostok::configs::binary_config_value const &, unsigned char)`
- `−` `grenade_set_core(void)`
- `−` `load(class vostok::configs::binary_config_value const &, unsigned char)`

---

## 🟡 REWORKED · `survarium::portable_interactive_object` (+1 / −2)

- `+` `portable_interactive_object(class survarium::base_game_scene &)`
- `−` `on_weapon_user_sprint(bool, bool)`
- `−` `portable_interactive_object(class survarium::base_game_scene &, enum vostok::animation::hand_to_weapon_ik_solver::ik_locator_id_enum)`

---

## 🟢 NEW · `survarium::swear_filter` (+3)

- `+` `filter_text(wchar_t *, unsigned short, wchar_t const *) const`
- `+` `filter_text(wchar_t *, unsigned short, wchar_t const *) const'::`2'::mes_excepts const &)`
- `+` `swear_filter(wchar_t **const, unsigned int, wchar_t *const, unsigned int, wchar_t **const, unsigned int, wchar_t *const, unsigned int, char *)`

---

## 🟢 NEW · `vostok::circular_buffer<struct stlp_std::pair<unsigned int, unsigned int>, 128>` (+3)

- `+` `push_back(struct stlp_std::pair<unsigned int, unsigned int> const &)`
- `+` `push_back<class vostok::circular_buffer<struct stlp_std::pair<unsigned int, unsigned int>, 128>::const_iterator>(class vostok::circular_buffer<struct stlp_std::pair<unsigned int, unsigned int>, 128>::const_iterator const &, class vostok::circular_buffer<struct stlp_std::pair<unsigned int, unsigned int>, 128>::const_iterator const &)`
- `+` `~circular_buffer<struct stlp_std::pair<unsigned int, unsigned int>, 128>(void)`

---

## 🟢 NEW · `vostok::network_core::udp_match_raw_stats` (+3)

- `+` `udp_match_raw_stats(struct vostok::network_core::udp_match_raw_stats const &)`
- `+` `udp_match_raw_stats(void)`
- `+` `~udp_match_raw_stats(void)`

---

## 🟢 NEW · `vostok::network_core::udp_match_received_message_stats` (+3)

- `+` `udp_match_received_message_stats(struct vostok::network_core::udp_match_received_message_stats const &)`
- `+` `udp_match_received_message_stats(void)`
- `+` `~udp_match_received_message_stats(void)`

---

## 🟢 NEW · `vostok::network_core::udp_match_sent_message_stats` (+3)

- `+` `udp_match_sent_message_stats(struct vostok::network_core::udp_match_sent_message_stats const &)`
- `+` `udp_match_sent_message_stats(void)`
- `+` `~udp_match_sent_message_stats(void)`

---

## 🟢 NEW · `vostok::render::particle_rain_drops_geometry` (+3)

- `+` `draw(float)`
- `+` `particle_rain_drops_geometry(unsigned int)`
- `+` `~particle_rain_drops_geometry(void)`

---

## 🟡 REWORKED · `vostok::buffer_vector<unsigned int>` (+2 / −1)

- `+` `operator=(class vostok::buffer_vector<unsigned int> const &)`
- `+` `resize(unsigned int)`
- `−` `assign<unsigned int const *>(unsigned int const *, unsigned int const *const &)`

---

## 🟡 REWORKED · `vostok::render::resource_manager` (+2 / −1)

- `+` `get_texture_video_memory_size(void)`
- `+` `on_texture_loaded_res_impl(unsigned char const *, unsigned int, unsigned int, unsigned int, unsigned int, unsigned int, char const *, unsigned int, bool)`
- `−` `on_texture_loaded_res_impl(unsigned char const *, unsigned int, char const *, unsigned int, bool)`

---

## 🟡 REWORKED · `survarium::grenade_set_cook` (+1 / −2)

- `+` `new_derived_resource(void *const, class vostok::configs::binary_config_value const &, unsigned char)`
- `−` `get_derived_resource_size(void)`
- `−` `new_derived_resource(void *const)`

---

## 🟢 NEW · `survarium::base_view_network_client` (+3)

- `+` `to_first_view_mode(class survarium::game_world &)`
- `+` `to_free_fly_mode(class survarium::game_world &)`
- `+` `to_third_view_mode(class survarium::game_world &)`

---

## 🟢 NEW · `survarium::game_quest_progress_calculator` (+3)

- `+` `calculate_player_game_progress(unsigned char, enum survarium::match_stats_events_dict_enum)`
- `+` `calculate_victory_item_progress(unsigned char, enum survarium::victory_item_event_type)`
- `+` `set_player_quests(class vostok::vectora<struct survarium::quest_instance> const *, unsigned char)`

---

## 🟡 REWORKED · `survarium::shared_statistics` (+2 / −1)

- `+` `on_player_damaged(unsigned int, unsigned char, unsigned char, bool, unsigned short)`
- `+` `start_match(class survarium::game_world_core const &, struct survarium::match_options const &)`
- `−` `~shared_statistics(void)`

---

## 🟡 REWORKED · `vostok` (+2 / −1)

- `+` `create_file_name_by_replay(class vostok::fs_new::native_path_string *const, char const *const)`
- `+` `open_file_impl(class vostok::fs_new::device_file_system_no_watcher_proxy &, char const *, enum vostok::fs_new::file_access::access_enum)`
- `−` `static_cast_resource_ptr<class vostok::resources::resource_ptr<class vostok::render::scene, class vostok::resources::unmanaged_resource>, struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &)`

---

## 🟡 REWORKED · `vostok::math` (+0 / −3)

- `−` `normalize_safe(class vostok::math::float2_pod const &, class vostok::math::float2_pod const &)`
- `−` `operator*(class vostok::math::aabb const &, float)`
- `−` `operator*(class vostok::math::float4x4const &, class vostok::math::float4x4const &)`

---

## 🟡 REWORKED · `vostok::collision::box_geometry_instance` (+0 / −3)

- `−` `render(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::debug::renderer &) const`
- `−` `render(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::debug::renderer &, class vostok::math::float4x4const &) const`
- `−` `render(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::debug::renderer &, class vostok::math::float4x4const &, class vostok::math::color const &) const`

---

## 🟡 REWORKED · `vostok::strings` (+2)

- `+` `copy<256>(char (&)[256], char const *)`
- `+` `utf8towcs(wchar_t *, unsigned int, char const *, unsigned int)`

---

## 🟢 NEW · `survarium::armor` (+2)

- `+` `armor(class vostok::configs::binary_config_value const &)`
- `+` `on_holder_assigned(void)`

---

## 🟡 REWORKED · `survarium::booby_trap_set` (+1 / −1)

- `+` `booby_trap_set(class vostok::configs::binary_config_value const &, unsigned char, class survarium::base_game_scene &, struct vostok::physics::world &, class vostok::resources::resource_ptr<class survarium::game_material_manager, class vostok::resources::unmanaged_intrusive_base> const &)`
- `−` `booby_trap_set(class survarium::base_game_scene &, struct vostok::physics::world &, class vostok::resources::resource_ptr<class survarium::game_material_manager, class vostok::resources::unmanaged_intrusive_base> const &)`

---

## 🟡 REWORKED · `survarium::booby_trap_set_cook` (+1 / −1)

- `+` `new_derived_resource(class vostok::configs::binary_config_value const &, unsigned char, struct vostok::physics::world &, class vostok::resources::resource_ptr<class survarium::game_material_manager, class vostok::resources::unmanaged_intrusive_base> const &, void *const)`
- `−` `new_derived_resource(struct vostok::physics::world &, class vostok::resources::resource_ptr<class survarium::game_material_manager, class vostok::resources::unmanaged_intrusive_base> const &, void *const)`

---

## 🟡 REWORKED · `survarium::gather_victory_items_rule_cook` (+2)

- `+` `create_resource(unsigned int)`
- `+` `get_derived_resource_size(void)`

---

## 🟢 NEW · `survarium::match_time_vi_spawn_rule_cook` (+2)

- `+` `create_resource(unsigned int)`
- `+` `get_derived_resource_size(void)`

---

## 🟢 NEW · `survarium::item_config_cook` (+2)

- `+` `create_request(struct survarium::item_config_cook_data const &, class vostok::fs_new::virtual_path_string &, enum vostok::resources::class_id_enum &)`
- `+` `translate_query(class vostok::resources::query_result_for_cook &)`

---

## 🟢 NEW · `survarium::swear_filter_config_cook` (+2)

- `+` `on_binary_config_loaded(class vostok::resources::queries_result &, class vostok::resources::query_result_for_cook *)`
- `+` `translate_query(class vostok::resources::query_result_for_cook &)`

---

## 🟡 REWORKED · `survarium::victory_item_core_put_state` (+1 / −1)

- `+` `on_animation_end_impl(bool &)`
- `−` `is_ready_for_transition(void) const`

---

## 🟡 REWORKED · `vostok::intrusive_ptr<class vostok::render::res_shader_technique, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>` (+1 / −1)

- `+` `dec(void)`
- `−` `~intrusive_ptr<class vostok::render::res_shader_technique, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>(void)`

---

## 🟡 REWORKED · `vostok::network::match_client_impl` (+1 / −1)

- `+` `on_packet_received(unsigned char, class vostok::network_core::buffer_reader &, unsigned int)`
- `−` `on_packet_received(unsigned char, class vostok::network_core::buffer_reader &)`

---

## 🟡 REWORKED · `survarium::artefact_lifebone_core` (+1 / −1)

- `+` `artefact_lifebone_core(class vostok::configs::binary_config_value const &, class vostok::resources::resource_ptr<class survarium::game_effect_emitter, class vostok::resources::unmanaged_intrusive_base> const &)`
- `−` `artefact_lifebone_core(struct survarium::artefact_lifebone_core::config const &, class vostok::resources::resource_ptr<class survarium::game_effect_emitter, class vostok::resources::unmanaged_intrusive_base> const &)`

---

## 🟡 REWORKED · `survarium::artefact_onyx_core` (+1 / −1)

- `+` `artefact_onyx_core(class vostok::configs::binary_config_value const &, class vostok::resources::resource_ptr<class survarium::game_effect_emitter, class vostok::resources::unmanaged_intrusive_base> const &)`
- `−` `artefact_onyx_core(struct survarium::artefact_onyx_core::config const &, class vostok::resources::resource_ptr<class survarium::game_effect_emitter, class vostok::resources::unmanaged_intrusive_base> const &)`

---

## 🟡 REWORKED · `survarium::artefact_spring_core` (+1 / −1)

- `+` `artefact_spring_core(class vostok::configs::binary_config_value const &, class vostok::resources::resource_ptr<class survarium::game_effect_emitter, class vostok::resources::unmanaged_intrusive_base> const &)`
- `−` `artefact_spring_core(struct survarium::artefact_spring_core::config const &, class vostok::resources::resource_ptr<class survarium::game_effect_emitter, class vostok::resources::unmanaged_intrusive_base> const &)`

---

## 🟡 REWORKED · `survarium::dictionary_item` (+1 / −1)

- `+` `~dictionary_item(void)`
- `−` `is_ammo(void) const`

---

## 🟡 REWORKED · `survarium::hit_info` (+1 / −1)

- `+` `hit_info(unsigned int, unsigned char, unsigned char, char const *const, enum survarium::hit_type_enum, float, float, class survarium::bullet *const, class vostok::math::float3const &, enum survarium::triangle_orientation, class survarium::inventory_item const *const)`
- `−` `hit_info(unsigned int, unsigned char, unsigned char, char const *const, enum survarium::hit_type_enum, float, float, class survarium::bullet *const, class vostok::math::float3const &, enum survarium::triangle_orientation, unsigned short)`

---

## 🟡 REWORKED · `survarium::inventory_item` (+1 / −1)

- `+` `inventory_item(class vostok::configs::binary_config_value const &, enum survarium::inventory_item::action_behaviour_type, bool)`
- `−` `inventory_item(enum survarium::inventory_item::action_behaviour_type, bool)`

---

## 🟡 REWORKED · `survarium::inventory_item_descr` (+2)

- `+` `inventory_item_descr(void)`
- `+` `~inventory_item_descr(void)`

---

## 🟢 NEW · `survarium::match_stats` (+2)

- `+` `deserialize(class vostok::network_core::buffer_reader &)`
- `+` `match_stats(void)`

---

## 🟢 NEW · `survarium::player_result_brief` (+2)

- `+` `deserialize(class vostok::network_core::buffer_reader &)`
- `+` `player_result_brief(void)`

---

## 🟢 NEW · `survarium::player_result_full` (+2)

- `+` `deserialize(class vostok::network_core::buffer_reader &)`
- `+` `player_result_full(void)`

---

## 🟡 REWORKED · `survarium::weapon` (+1 / −1)

- `+` `weapon(class vostok::configs::binary_config_value const &, class survarium::base_game_scene &, unsigned int)`
- `−` `weapon(class survarium::base_game_scene &, unsigned int)`

---

## 🟡 REWORKED · `survarium::weapon_ammunition` (+1 / −1)

- `+` `weapon_ammunition(class vostok::configs::binary_config_value const &)`
- `−` `load(class vostok::configs::binary_config_value const &)`

---

## 🟡 REWORKED · `vostok::animation::animation_player` (+1 / −1)

- `+` `animation_player(unsigned int)`
- `−` `animation_player(void)`

---

## 🟢 NEW · `vostok::network_core::udp_match_max_value_stats` (+2)

- `+` `append(unsigned int, unsigned int)`
- `+` `udp_match_max_value_stats(struct vostok::network_core::udp_match_max_value_stats const &)`

---

## 🟢 NEW · `vostok::network_core::udp_match_message_item_duplicates_stats` (+2)

- `+` `append(unsigned int)`
- `+` `udp_match_message_item_duplicates_stats(struct vostok::network_core::udp_match_message_item_duplicates_stats const &)`

---

## 🟢 NEW · `vostok::network_core::udp_match_messages_stats_template<struct vostok::network_core::udp_match_received_message_stats>` (+2)

- `+` `udp_match_messages_stats_template<struct vostok::network_core::udp_match_received_message_stats>(struct vostok::network_core::udp_match_messages_stats_template<struct vostok::network_core::udp_match_received_message_stats> const &)`
- `+` `~udp_match_messages_stats_template<struct vostok::network_core::udp_match_received_message_stats>(void)`

---

## 🟢 NEW · `vostok::network_core::udp_match_messages_stats_template<struct vostok::network_core::udp_match_sent_message_stats>` (+2)

- `+` `udp_match_messages_stats_template<struct vostok::network_core::udp_match_sent_message_stats>(struct vostok::network_core::udp_match_messages_stats_template<struct vostok::network_core::udp_match_sent_message_stats> const &)`
- `+` `~udp_match_messages_stats_template<struct vostok::network_core::udp_match_sent_message_stats>(void)`

---

## 🟡 REWORKED · `survarium::packet_sender` (+1 / −1)

- `+` `on_player_input_changed(struct survarium::player_update &) const`
- `−` `on_player_input_changed(struct survarium::player_update &) const`

---

## 🟡 REWORKED · `vostok::buffer_vector<class vostok::render::buffer_slot>` (+1 / −1)

- `+` `operator=(class vostok::buffer_vector<class vostok::render::buffer_slot> const &)`
- `−` `assign<class vostok::render::buffer_slot const *>(class vostok::render::buffer_slot const *, class vostok::render::buffer_slot const *const &)`

---

## 🟡 REWORKED · `vostok::buffer_vector<class vostok::render::texture_slot>` (+1 / −1)

- `+` `operator=(class vostok::buffer_vector<class vostok::render::texture_slot> const &)`
- `−` `assign<class vostok::render::texture_slot const *>(class vostok::render::texture_slot const *, class vostok::render::texture_slot const *const &)`

---

## 🟡 REWORKED · `vostok::render::resource_intrusive_base` (+1 / −1)

- `+` `destroy<class vostok::render::res_state>(class vostok::render::res_state const *const)`
- `−` `destroy<class vostok::render::res_shader_technique>(class vostok::render::res_shader_technique const *const)`

---

## 🟡 REWORKED · `vostok::render::statistics_group` (+2)

- `+` `calc_sizes(struct vostok::ui::font const *, unsigned int &, unsigned int &, enum vostok::render::statistics_group::enum_item_column)`
- `+` `render_column(struct vostok::ui::world &, unsigned int, unsigned int, enum vostok::render::statistics_group::enum_item_column)`

---

## 🟢 NEW · `vostok::detail::concrete_type_helper<struct survarium::item_cook_data>` (+2)

- `+` `copy(class vostok::mutable_buffer, class vostok::const_buffer)`
- `+` `copy_helper(class vostok::mutable_buffer)`

---

## 🟢 NEW · `survarium::interactive_object` (+2)

- `+` `apply_look_pitch(float)`
- `+` `look_pitch(void) const`

---

## 🟡 REWORKED · `survarium::portable_interactive_object_with_finger_correction` (+1 / −1)

- `+` `on_weapon_user_sprint(bool, bool)`
- `−` `on_weapon_user_sprint(bool, bool)`

---

## 🟡 REWORKED · `vostok::particle::particle_world` (+1 / −1)

- `+` `get_render_emitter_instances(class vostok::math::float4x4const &, class vostok::fixed_vector<struct vostok::particle::render_particle_emitter_instance *, 2048> &)`
- `−` `get_render_emitter_instances(class vostok::math::float4x4const &, class vostok::fixed_vector<struct vostok::particle::render_particle_emitter_instance *, 1024> &)`

---

## 🟡 REWORKED · `vostok::sound::composite_sound` (+1 / −1)

- `+` `emit_sound_propagators(class vostok::sound::sound_instance_proxy_internal &, unsigned int, unsigned int, unsigned int) const`
- `−` `emit_sound_propagators(class vostok::sound::sound_instance_proxy_internal &, unsigned int, unsigned int) const`

---

## 🟡 REWORKED · `vostok::sound::single_sound` (+1 / −1)

- `+` `emit_sound_propagators(class vostok::sound::sound_instance_proxy_internal &, unsigned int, unsigned int, unsigned int) const`
- `−` `emit_sound_propagators(class vostok::sound::sound_instance_proxy_internal &, unsigned int, unsigned int) const`

---

## 🟡 REWORKED · `vostok::sound::sound_collection` (+1 / −1)

- `+` `emit_sound_propagators(class vostok::sound::sound_instance_proxy_internal &, unsigned int, unsigned int, unsigned int) const`
- `−` `emit_sound_propagators(class vostok::sound::sound_instance_proxy_internal &, unsigned int, unsigned int) const`

---

## 🟡 REWORKED · `survarium::messaging_client` (+1 / −1)

- `+` `on_message_typed(char const *, char const (&)[256], enum vostok::messaging::message_channel_enum)`
- `−` `on_message_typed(char const *, char const *, enum vostok::messaging::message_channel_enum)`

---

## 🟢 NEW · `survarium::player::inflicted_damage_collector` (+2)

- `+` `deserialize(class vostok::network_core::buffer_reader &, unsigned int)`
- `+` `serialize(class vostok::network_core::buffer_writer const &, unsigned int) const`

---

## 🟡 REWORKED · `survarium::player_params_modifiers_container` (+1 / −1)

- `+` `clear_modifiers(void)`
- `−` `get_modifier_value(enum survarium::player_params_modifiers_enum) const`

---

## 🟡 REWORKED · `vostok::animation::fingers_to_weapon_corrector` (+1 / −1)

- `+` `activate_hand(enum vostok::animation::fingers_to_weapon_corrector::hands_enum, bool, enum vostok::animation::fingers_to_weapon_corrector::fingers_locator_set_id_enum, unsigned int)`
- `−` `activate_hand(enum vostok::animation::fingers_to_weapon_corrector::hands_enum, bool, bool, enum vostok::animation::fingers_to_weapon_corrector::fingers_locator_set_id_enum, unsigned int)`

---

## 🟡 REWORKED · `vostok::animation::hand_to_weapon_ik_solver` (+1 / −1)

- `+` `activate_hand(enum vostok::animation::hand_to_weapon_ik_solver::hands_enum, bool, enum vostok::animation::hand_to_weapon_ik_solver::ik_locator_id_enum, unsigned int)`
- `−` `activate_hand(enum vostok::animation::hand_to_weapon_ik_solver::hands_enum, bool, bool, enum vostok::animation::hand_to_weapon_ik_solver::ik_locator_id_enum, unsigned int)`

---

## 🟢 NEW · `vostok::buffer_vector<class vostok::configs::binary_config_value>` (+2)

- `+` `insert(class vostok::configs::binary_config_value *const &, unsigned int, class vostok::configs::binary_config_value const &)`
- `+` `push_back(class vostok::configs::binary_config_value const &)`

---

## 🟡 REWORKED · `vostok::network_core::process_packet_predicate` (+1 / −1)

- `+` `operator()(unsigned char, class vostok::network_core::buffer_reader &, unsigned int) const`
- `−` `operator()(unsigned char, class vostok::network_core::buffer_reader &) const`

---

## 🟡 REWORKED · `vostok::render::res_render_output` (+2)

- `+` `minimize(void)`
- `+` `show(void)`

---

## 🟡 REWORKED · `vostok::render::stage_screen_space_reflections` (+1 / −1)

- `+` `render_models_with_reflections(class vostok::buffer_vector<struct vostok::render::render_surface_instance *> const &, bool, class vostok::intrusive_ptr<class vostok::render::res_texture, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy> const &)`
- `−` `render_models_with_reflections(class vostok::buffer_vector<struct vostok::render::render_surface_instance *> const &, bool)`

---

## 🟡 REWORKED · `vostok::logging` (+2)

- `+` `delete_filter_tree(class vostok::logging::filter_tree *&)`
- `+` `delete_log_file(class vostok::logging::log_file *&)`

---

## 🔴 REMOVED · `survarium::weapon_ammunition_cook` (+0 / −2)

- `−` `on_config_ready(class vostok::resources::queries_result &, class vostok::resources::query_result_for_cook *)`
- `−` `translate_query(class vostok::resources::query_result_for_cook &)`

---

## 🟡 REWORKED · `vostok::collision::loose_oct_tree` (+0 / −2)

- `−` `render(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::debug::renderer &)`
- `−` `render_iterate(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::debug::renderer &, struct vostok::collision::oct_node const *const, class vostok::math::float3const &, float)`

---

## 🔴 REMOVED · `survarium::match_total_stats` (+0 / −2)

- `−` `deserialize(class vostok::network_core::buffer_reader &)`
- `−` `match_total_stats(void)`

---

## 🟡 REWORKED · `vostok::buffer_vector<struct vostok::render::vertex_colored>` (+0 / −2)

- `−` `ctor<struct vostok::render::vertex_colored const *>(void *const, unsigned int, struct vostok::render::vertex_colored const *const &, struct vostok::render::vertex_colored const *const &)`
- `−` `insert<struct vostok::render::vertex_colored const *>(struct vostok::render::vertex_colored *const &, struct vostok::render::vertex_colored const *, struct vostok::render::vertex_colored const *const &)`

---

## 🔴 REMOVED · `vostok::physics::character_move_test_callback` (+0 / −2)

- `−` `addSingleResult(struct btCollisionWorld::LocalConvexResult &, bool)`
- `−` `character_move_test_callback(class btCollisionObject *, class btVector3const &, float)`

---

## 🔴 REMOVED · `vostok::intrusive_list<struct survarium::player_stamina_subscriber, struct survarium::player_stamina_subscriber *, 32, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>` (+0 / −2)

- `−` `contains_object(struct survarium::player_stamina_subscriber *)`
- `−` `erase(struct survarium::player_stamina_subscriber *)`

---

## 🟡 REWORKED · `vostok::collision::sphere_geometry_instance` (+0 / −2)

- `−` `render(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::debug::renderer &, class vostok::math::float4x4const &) const`
- `−` `render(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::debug::renderer &, class vostok::math::float4x4const &, class vostok::math::color const &) const`

---

## 🟡 REWORKED · `survarium::weapon_user_animations_selector` (+0 / −2)

- `−` `remove_animation_callback(char const *, void const *)`
- `−` `remove_animation_callback(enum vostok::animation::reserved_channel_ids_enum, void const *)`

---

## 🟢 NEW · ``vostok::configs::create_binary_config_buffer_impl'::`3'::remap_disposer` (+1)

- `+` `operator()`

---

## 🟢 NEW · ``vostok::configs::sort'::`5'::predicate` (+1)

- `+` `compare`

---

## 🟢 NEW · ``vostok::render::renderer::draw_top_dip_models_list'::`4'::sort_predicate` (+1)

- `+` `operator()`

---

## 🟡 REWORKED · `vostok::animation::mixing` (+1)

- `+` `operator+<class vostok::animation::mixing::addition_lexeme, class vostok::animation::mixing::animation_lexeme>(class vostok::animation::mixing::addition_lexeme &, class vostok::animation::mixing::animation_lexeme &)`

---

## 🟢 NEW · `vostok::resources::pinned_ptr_mutable<class vostok::animation::cubic_spline_skeleton_animation>` (+1)

- `+` `pinned_ptr_mutable<class vostok::animation::cubic_spline_skeleton_animation>(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>)`

---

## 🟡 REWORKED · `survarium::short_jump_start_state` (+1)

- `+` `is_ready_for_transition(void) const`

---

## 🟡 REWORKED · `survarium::player` (+1)

- `+` `generate_hit_event(unsigned int, unsigned char, unsigned char, float, float, class survarium::bullet const *, bool, unsigned short)`

---

## 🟡 REWORKED · `survarium::effect_zone_cook` (+1)

- `+` `create_resource(class vostok::resources::query_result_for_cook &, struct survarium::effect_zone_construct_params const &, class vostok::configs::binary_config_value const &)`

---

## 🟡 REWORKED · `survarium::login_menu` (+1)

- `+` `update_online_queue(unsigned int)`

---

## 🟡 REWORKED · `survarium::player_input_handler` (+1)

- `+` `process_third_person_mode(void)`

---

## 🟡 REWORKED · `vostok::network_core::async_connector` (+1)

- `+` `connect(class boost::asio::ip::basic_resolver_iterator<class boost::asio::ip::tcp> const &)`

---

## 🟢 NEW · `vostok::render::buffers_handler<2>` (+1)

- `+` `apply(void)`

---

## 🟡 REWORKED · `vostok::render::textures_handler<1>` (+1)

- `+` `reset(void)`

---

## 🟡 REWORKED · `vostok::resources::cook_base` (+1)

- `+` `pin_for_write<class vostok::animation::cubic_spline_skeleton_animation>(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>)`

---

## 🟡 REWORKED · `survarium::match_options` (+1)

- `+` `~match_options(void)`

---

## 🟢 NEW · `vostok::buffer_vector<class boost::basic_regex<wchar_t, struct boost::regex_traits<wchar_t, class boost::w32_regex_traits<wchar_t> > > >` (+1)

- `+` `~buffer_vector<class boost::basic_regex<wchar_t, struct boost::regex_traits<wchar_t, class boost::w32_regex_traits<wchar_t> > > >(void)`

---

## 🟡 REWORKED · `vostok::console_commands::logging_filters_console_command` (+1)

- `+` `logging_filters_console_command(class vostok::logging::filter_tree &, char const *const, bool, enum vostok::console_commands::command_type, enum vostok::console_commands::execution_filter)`

---

## 🟢 NEW · `vostok::fixed_vector<struct vostok::particle::render_particle_emitter_instance *, 2048>` (+1)

- `+` `fixed_vector<struct vostok::particle::render_particle_emitter_instance *, 2048>(class vostok::fixed_vector<struct vostok::particle::render_particle_emitter_instance *, 2048> const &)`

---

## 🟢 NEW · `vostok::intrusive_ptr<class vostok::render::skin, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock>` (+1)

- `+` `~intrusive_ptr<class vostok::render::skin, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock>(void)`

---

## 🟡 REWORKED · `vostok::math::float4x4` (+1)

- `+` `float4x4(void)`

---

## 🟢 NEW · `vostok::math::half2` (+1)

- `+` `half2(class vostok::math::float2const &)`

---

## 🟢 NEW · `vostok::network::udp_match_fixed_packets_allocator<4096>` (+1)

- `+` `udp_match_fixed_packets_allocator<4096>(class vostok::memory::base_allocator &)`

---

## 🟢 NEW · `vostok::network_core::udp_match_messages_stats` (+1)

- `+` `udp_match_messages_stats(void)`

---

## 🟢 NEW · `vostok::network_core::udp_match_messages_stats_cumulative_template<struct vostok::network_core::udp_match_received_message_stats, 10>` (+1)

- `+` `~udp_match_messages_stats_cumulative_template<struct vostok::network_core::udp_match_received_message_stats, 10>(void)`

---

## 🟢 NEW · `vostok::network_core::udp_match_messages_stats_cumulative_template<struct vostok::network_core::udp_match_received_message_stats, 3>` (+1)

- `+` `~udp_match_messages_stats_cumulative_template<struct vostok::network_core::udp_match_received_message_stats, 3>(void)`

---

## 🟢 NEW · `vostok::network_core::udp_match_messages_stats_cumulative_template<struct vostok::network_core::udp_match_sent_message_stats, 10>` (+1)

- `+` `~udp_match_messages_stats_cumulative_template<struct vostok::network_core::udp_match_sent_message_stats, 10>(void)`

---

## 🟢 NEW · `vostok::network_core::udp_match_messages_stats_cumulative_template<struct vostok::network_core::udp_match_sent_message_stats, 3>` (+1)

- `+` `~udp_match_messages_stats_cumulative_template<struct vostok::network_core::udp_match_sent_message_stats, 3>(void)`

---

## 🟡 REWORKED · `vostok::resources::managed_cook` (+1)

- `+` `managed_cook(enum vostok::resources::class_id_enum, enum vostok::resources::cook_base::reuse_enum, unsigned int, class vostok::enum_flags<enum vostok::resources::cook_base::flags_enum>)`

---

## 🟢 NEW · `vostok::network_core::move_to_list_predicate` (+1)

- `+` `operator()(class vostok::network_core::udp_match_packet *const) const`

---

## 🟢 NEW · `vostok::physics::character_controller_impassable_slide_down_tester` (+1)

- `+` `convex_sweep_test(class btVector3const &, class btVector3const &, class btVector3&, class btVector3&, float &)`

---

## 🟡 REWORKED · `vostok::render::options` (+1)

- `+` `use_ssr(void) const`

---

## 🟡 REWORKED · `vostok::render::remove_texture_predicate` (+1)

- `+` `operator()(struct vostok::render::streamable_texture_info const &)`

---

## 🟡 REWORKED · `vostok::fs_new::virtual_path_string` (+1)

- `+` `operator=<class vostok::configs::binary_config_value>(class vostok::configs::binary_config_value const &)`

---

## 🟡 REWORKED · `survarium::base_network_client` (+1)

- `+` `get_last_current_player(void)`

---

## 🟡 REWORKED · `vostok::resources::query_result_for_cook` (+1)

- `+` `assert_on_fail(void) const`

---

## 🟢 NEW · `vostok::memory::new_array_helper<struct survarium::price_item>` (+1)

- `+` `call<class vostok::memory::doug_lea_allocator>(class vostok::memory::doug_lea_allocator &, unsigned int, char const *const, char const *const, unsigned int)`

---

## 🟢 NEW · `vostok::memory::multi_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<684, class vostok::threading::multi_threading_policy>::node>` (+1)

- `+` `allocate(union vostok::memory::multi_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<684, class vostok::threading::multi_threading_policy>::node>::free_list_type &)`

---

## 🟢 NEW · `vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<80, class vostok::threading::single_threading_policy>::node>` (+1)

- `+` `allocate(class vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<80, class vostok::threading::single_threading_policy>::node>::free_list_type &)`

---

## 🟢 NEW · `vostok::detail::type_to_int<struct survarium::item_config_cook_data>` (+1)

- `+` `get(void)`

---

## 🟢 NEW · `vostok::detail::type_to_int<struct survarium::item_cook_data>` (+1)

- `+` `get(void)`

---

## 🟢 NEW · `vostok::detail::type_to_int<unsigned int>` (+1)

- `+` `get(void)`

---

## 🟢 NEW · `vostok::memory::detail::call_constructor_helper<struct survarium::dictionary_item, 0>` (+1)

- `+` `call(struct survarium::dictionary_item *const, struct survarium::dictionary_item *const)`

---

## 🟡 REWORKED · `survarium::lobby_player_profile` (+1)

- `+` `operator=(struct survarium::lobby_player_profile const &)`

---

## 🟡 REWORKED · `survarium::player_profile` (+1)

- `+` `operator=(struct survarium::player_profile const &)`

---

## 🟡 REWORKED · `vostok::render::hw_buffer_pool` (+1)

- `+` `total_allocated_memory(void) const`

---

## 🟡 REWORKED · `vostok::render::texture_storage` (+1)

- `+` `occupied_memory(void) const`

---

## 🟡 REWORKED · `vostok::vfs::vfs_iterator` (+1)

- `+` `get_file_size(void) const`

---

## 🟡 REWORKED · `survarium::game_world` (+1)

- `+` `on_mouse_key_action(struct vostok::input::world *, enum vostok::input::mouse_button, enum vostok::input::enum_mouse_key_action)`

---

## 🟢 NEW · `vostok::detail::concrete_type_helper<struct survarium::item_config_cook_data>` (+1)

- `+` `copy_helper(class vostok::mutable_buffer)`

---

## 🟢 NEW · `vostok::detail::concrete_type_helper<unsigned int>` (+1)

- `+` `copy_helper(class vostok::mutable_buffer)`

---

## 🟡 REWORKED · `vostok::render::render_model_instance_impl` (+1)

- `+` `transform(void) const`

---

## 🟢 NEW · `closest_convex_not_me_result_callback` (+1)

- `+` `addSingleResult(struct btCollisionWorld::LocalConvexResult &, bool)`

---

## 🟢 NEW · `btRigidBody` (+1)

- `+` `calculateSerializeBufferSize(void) const`

---

## 🟡 REWORKED · `survarium::player_logic_base_state` (+1)

- `+` `set_user(class survarium::base_player &)`

---

## 🟢 NEW · `survarium::text_clipboard` (+1)

- `+` `OnTextStore(wchar_t const *, unsigned int)`

---

## 🟡 REWORKED · `vostok::animation::cubic_spline_skeleton_animation_cook` (+1)

- `+` `destroy_resource(class vostok::resources::managed_resource *)`

---

## 🟢 NEW · `vostok::render::effect_probe_brdf` (+1)

- `+` `compile(class vostok::render::effect_compiler &, class vostok::configs::binary_config_value const &, struct vostok::render::surface_effect_parameters const &)`

---

## 🟢 NEW · `vostok::render::effect_ssr` (+1)

- `+` `compile(class vostok::render::effect_compiler &, class vostok::configs::binary_config_value const &, struct vostok::render::surface_effect_parameters const &)`

---

## 🟢 NEW · `vostok::render::effect_ssr_mask` (+1)

- `+` `compile(class vostok::render::effect_compiler &, class vostok::configs::binary_config_value const &, struct vostok::render::surface_effect_parameters const &)`

---

## 🟡 REWORKED · `vostok::render::user_render_model_instance` (+1)

- `+` `get_surface_stats(unsigned int, struct vostok::render::surface_stats &) const`

---

## 🟡 REWORKED · `survarium::curing_event_status` (+1)

- `+` `serialize(class vostok::network_core::buffer_writer const &, unsigned int) const`

---

## 🟢 NEW · `survarium::dictionary_item_params` (+1)

- `+` `load(class vostok::configs::binary_config_value const &)`

---

## 🟢 NEW · `survarium::new_player_damage_protector` (+1)

- `+` `reduce_damage(float &, unsigned char)`

---

## 🟡 REWORKED · `survarium::player_shared_statistics` (+1)

- `+` `serialize(class vostok::network_core::buffer_writer const &, unsigned int) const`

---

## 🟡 REWORKED · `survarium::pvp_match_core` (+1)

- `+` `tick(unsigned int)`

---

## 🟢 NEW · `vostok::buffer_vector<class vostok::variant<32> *>` (+1)

- `+` `push_back(class vostok::variant<32> *const &)`

---

## 🟢 NEW · `vostok::buffer_vector<struct survarium::armor::body_part_params>` (+1)

- `+` `push_back(struct survarium::armor::body_part_params const &)`

---

## 🟢 NEW · `vostok::buffer_vector<struct survarium::item_modification *>` (+1)

- `+` `push_back(struct survarium::item_modification *const &)`

---

## 🟢 NEW · `vostok::buffer_vector<struct survarium::net_stats::column_info>` (+1)

- `+` `push_back(struct survarium::net_stats::column_info const &)`

---

## 🟡 REWORKED · `vostok::engine::engine_world` (+1)

- `+` `on_clipboard_changed(void)`

---

## 🟡 REWORKED · `vostok::intrusive_list<struct vostok::particle::base_particle, struct vostok::particle::base_particle *, 208, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>` (+1)

- `+` `clear(void)`

---

## 🟡 REWORKED · `vostok::memory::detail::call_destructor_predicate` (+1)

- `+` `operator()<class vostok::render::game::renderer>(class vostok::render::game::renderer *const) const`

---

## 🟢 NEW · `vostok::memory::stream` (+1)

- `+` `append(void const *, unsigned int)`

---

## 🟢 NEW · `vostok::network_core::udp_match_cumulative_value_stats` (+1)

- `+` `append(unsigned int, unsigned int)`

---

## 🟡 REWORKED · `vostok::render::engine::world` (+1)

- `+` `draw_render_statistics(struct vostok::ui::world *)`

---

## 🟡 REWORKED · `vostok::render::scene_renderer` (+1)

- `+` `draw_render_statistics(struct vostok::ui::world &, class vostok::resources::resource_ptr<struct vostok::render::base_scene_view, class vostok::resources::unmanaged_intrusive_base> const &)`

---

## 🟡 REWORKED · `vostok::render::stage_ambient_lighting` (+1)

- `+` `accumulate_probe_brdf(void)`

---

## 🟡 REWORKED · `vostok::replay_match_reader` (+1)

- `+` `open_replay(char const *)`

---

## 🟡 REWORKED · `vostok::sound::new_sound_propagator` (+1)

- `+` `set_offsets(unsigned int, unsigned int)`

---

## 🟡 REWORKED · `survarium::game_module` (+1)

- `+` `create_world(struct vostok::engine_user::engine &, class vostok::render::world &, struct vostok::sound::world &, struct vostok::network::world &)`

---

## 🔴 REMOVED · ``vostok::render::scene::process_streaming'::`51'::remove_texture_predicate` (+0 / −1)

- `−` `operator()`

---

## 🔴 REMOVED · `vostok::resources::pinned_ptr_mutable<struct vostok::render::texture_data_resource>` (+0 / −1)

- `−` `pinned_ptr_mutable<struct vostok::render::texture_data_resource>(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>)`

---

## 🟡 REWORKED · `vostok::buffer_vector<class vostok::intrusive_ptr<class vostok::render::res_shader_technique, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy> >` (+0 / −1)

- `−` `destroy(class vostok::intrusive_ptr<class vostok::render::res_shader_technique, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy> *, class vostok::intrusive_ptr<class vostok::render::res_shader_technique, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy> *const &)`

---

## 🟡 REWORKED · `survarium::jump_logic_state_prepare` (+0 / −1)

- `−` `is_ready_for_transition(void) const`

---

## 🟡 REWORKED · `vostok::render::stage_rain` (+0 / −1)

- `−` `is_effects_ready(void) const`

---

## 🔴 REMOVED · `vostok::memory::single_size_buffer_allocator<1364, class vostok::threading::multi_threading_policy>` (+0 / −1)

- `−` `allocate_impl(void)`

---

## 🟡 REWORKED · `vostok::animation::mixing::n_ary_tree_serializer` (+0 / −1)

- `−` `save_bits(unsigned char *const)`

---

## 🔴 REMOVED · `vostok::intrusive_ptr<class vostok::render::scene, class vostok::resources::unmanaged_resource, class vostok::threading::simple_lock>` (+0 / −1)

- `−` `dec(void)`

---

## 🟡 REWORKED · `vostok::render::stage_postprocess` (+0 / −1)

- `−` `process_blur(enum vostok::render::enum_render_target_index, enum vostok::render::enum_render_target_index, unsigned int)`

---

## 🔴 REMOVED · `survarium::artefact_rattle_core` (+0 / −1)

- `−` `load_config(class vostok::configs::binary_config_value const &)`

---

## 🟡 REWORKED · `survarium::artefact_lifebone_core::config` (+0 / −1)

- `−` `config(struct survarium::artefact_lifebone_core::config const &)`

---

## 🔴 REMOVED · `survarium::artefact_onyx_core::config` (+0 / −1)

- `−` `config(struct survarium::artefact_onyx_core::config const &)`

---

## 🔴 REMOVED · `survarium::weapon_sound_effect::sounds` (+0 / −1)

- `−` `~sounds(void)`

---

## 🔴 REMOVED · `vostok::animation::fingers_to_weapon_corrector::hand` (+0 / −1)

- `−` `hand(void)`

---

## 🟡 REWORKED · `vostok::buffer_vector<struct vostok::render::render_surface_instance *>` (+0 / −1)

- `−` `buffer_vector<struct vostok::render::render_surface_instance *>(void *, unsigned int, class vostok::buffer_vector<struct vostok::render::render_surface_instance *> const &)`

---

## 🔴 REMOVED · `vostok::fixed_vector<struct vostok::particle::render_particle_emitter_instance *, 1024>` (+0 / −1)

- `−` `fixed_vector<struct vostok::particle::render_particle_emitter_instance *, 1024>(class vostok::fixed_vector<struct vostok::particle::render_particle_emitter_instance *, 1024> const &)`

---

## 🔴 REMOVED · `vostok::fixed_vector<struct vostok::render::caster_model, 2048>` (+0 / −1)

- `−` `~fixed_vector<struct vostok::render::caster_model, 2048>(void)`

---

## 🔴 REMOVED · `vostok::fixed_vector<struct vostok::render::geometry_batch, 32>` (+0 / −1)

- `−` `~fixed_vector<struct vostok::render::geometry_batch, 32>(void)`

---

## 🔴 REMOVED · `vostok::fixed_vector<unsigned short, 1024>` (+0 / −1)

- `−` `ctor<unsigned short const *>(unsigned short const *const &, unsigned short const *const &)`

---

## 🟡 REWORKED · `vostok::intrusive_ptr<class vostok::render::res_pass, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>` (+0 / −1)

- `−` `intrusive_ptr<class vostok::render::res_pass, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>(class vostok::intrusive_ptr<class vostok::render::res_pass, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy> const &)`

---

## 🟡 REWORKED · `vostok::math::aabb_plane` (+0 / −1)

- `−` `aabb_plane(void)`

---

## 🔴 REMOVED · `vostok::network_core::udp_match_packets_allocator` (+0 / −1)

- `−` `udp_match_packets_allocator(class vostok::memory::base_allocator &, void *, unsigned int)`

---

## 🟡 REWORKED · `vostok::physics::character_controller_can_stand_tester` (+0 / −1)

- `−` `character_controller_can_stand_tester(class btVector3const &, class btCollisionObject &, class btCapsuleShape &, float)`

---

## 🔴 REMOVED · `vostok::render::batched_vertex_source` (+0 / −1)

- `−` `batched_vertex_source(struct vostok::render::batched_vertex_source const &)`

---

## 🟡 REWORKED · `vostok::render::game::renderer` (+0 / −1)

- `−` `~renderer(void)`

---

## 🔴 REMOVED · `vostok::resources::resource_ptr<class survarium::weapon_core, class vostok::resources::unmanaged_intrusive_base>` (+0 / −1)

- `−` `resource_ptr<class survarium::weapon_core, class vostok::resources::unmanaged_intrusive_base>(class survarium::weapon_core *)`

---

## 🔴 REMOVED · `delayed_packets_predicate` (+0 / −1)

- `−` `operator()(struct stlp_std::pair<class vostok::network_core::udp_match_packet *, struct stlp_std::pair<class boost::asio::ip::basic_endpoint<class boost::asio::ip::udp>, struct vostok::network_core::socket_handler *> > const &) const`

---

## 🔴 REMOVED · `vostok::physics::old_bullet_character_controller::sweep_test_key` (+0 / −1)

- `−` `operator==(struct vostok::physics::old_bullet_character_controller::sweep_test_key const &) const`

---

## 🟡 REWORKED · `vostok::buffer_vector<float>` (+0 / −1)

- `−` `operator=(class vostok::buffer_vector<float> const &)`

---

## 🔴 REMOVED · `vostok::fixed_vector<class vostok::render::buffer_slot, 128>` (+0 / −1)

- `−` `operator=(class vostok::fixed_vector<class vostok::render::buffer_slot, 128> const &)`

---

## 🔴 REMOVED · `vostok::fixed_vector<class vostok::render::texture_slot, 128>` (+0 / −1)

- `−` `operator=(class vostok::fixed_vector<class vostok::render::texture_slot, 128> const &)`

---

## 🟡 REWORKED · `vostok::math::cuboid` (+0 / −1)

- `−` `test(class vostok::math::sphere const &) const`

---

## 🔴 REMOVED · `vostok::memory::new_array_helper<struct survarium::dictionary_item>` (+0 / −1)

- `−` `call<class vostok::memory::base_allocator>(class vostok::memory::base_allocator &, unsigned int, char const *const, char const *const, unsigned int)`

---

## 🔴 REMOVED · `vostok::memory::multi_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<1364, class vostok::threading::multi_threading_policy>::node>` (+0 / −1)

- `−` `allocate(union vostok::memory::multi_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<1364, class vostok::threading::multi_threading_policy>::node>::free_list_type &)`

---

## 🔴 REMOVED · `vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<76, class vostok::threading::single_threading_policy>::node>` (+0 / −1)

- `−` `allocate(class vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<76, class vostok::threading::single_threading_policy>::node>::free_list_type &)`

---

## 🔴 REMOVED · `vostok::detail::type_to_int<unsigned short>` (+0 / −1)

- `−` `get(void)`

---

## 🔴 REMOVED · `vostok::memory::new_helper<class vostok::render::debug::draw_lines_command>` (+0 / −1)

- `−` `call<class vostok::memory::base_allocator>(class vostok::memory::base_allocator &, char const *const, char const *const, unsigned int)`

---

## 🔴 REMOVED · `vostok::memory::new_helper<class vostok::render::debug::draw_triangles_command>` (+0 / −1)

- `−` `call<class vostok::memory::base_allocator>(class vostok::memory::base_allocator &, char const *const, char const *const, unsigned int)`

---

## 🔴 REMOVED · `survarium::base_match_client` (+0 / −1)

- `−` `~base_match_client(void)`

---

## 🟡 REWORKED · `survarium::pistol_weapon_core_fire_state` (+0 / −1)

- `−` `~pistol_weapon_core_fire_state(void)`

---

## 🟡 REWORKED · `survarium::weapon_core_fire_state` (+0 / −1)

- `−` `~weapon_core_fire_state(void)`

---

## 🟡 REWORKED · `survarium::weapon_core_hide_state` (+0 / −1)

- `−` `~weapon_core_hide_state(void)`

---

## 🟡 REWORKED · `survarium::weapon_core_reload_state` (+0 / −1)

- `−` `~weapon_core_reload_state(void)`

---

## 🟡 REWORKED · `survarium::weapon_core_shotgun_reload_base_substate` (+0 / −1)

- `−` `~weapon_core_shotgun_reload_base_substate(void)`

---

## 🟡 REWORKED · `vostok::render::stage_particles` (+0 / −1)

- `−` `is_effects_ready(void) const`

---

## 🟡 REWORKED · `vostok::collision::aabb_object` (+0 / −1)

- `−` `render(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::debug::renderer &) const`

---

## 🟡 REWORKED · `vostok::collision::collision_object` (+0 / −1)

- `−` `render(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::debug::renderer &) const`

---

## 🟡 REWORKED · `vostok::collision::triangle_mesh_geometry` (+0 / −1)

- `−` `render(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::debug::renderer &, class vostok::math::float4x4const &) const`

---

## 🟡 REWORKED · `vostok::detail::concrete_type_helper<struct survarium::pvp_match_core_query_user_data>` (+0 / −1)

- `−` `copy(class vostok::mutable_buffer, class vostok::const_buffer)`

---

## 🟡 REWORKED · `vostok::network::send_queued_order` (+0 / −1)

- `−` `execute(void)`

---

## 🟡 REWORKED · `vostok::render::stage_decals_accumulate` (+0 / −1)

- `−` `clear_surfaces(void)`

---

## 🟡 REWORKED · `survarium::flash_value` (+0 / −1)

- `−` `SetElement(unsigned int, char const *)`

---

## 🔴 REMOVED · `survarium::match_player_stats` (+0 / −1)

- `−` `deserialize(class vostok::network_core::buffer_reader &)`

---

## 🔴 REMOVED · `survarium::player_results_item` (+0 / −1)

- `−` `deserialize(class vostok::network_core::buffer_reader &)`

---

## 🟡 REWORKED · `survarium::teammate_cure_event_manager` (+0 / −1)

- `−` `serialize(class vostok::network_core::buffer_writer const &, unsigned int) const`

---

## 🔴 REMOVED · `vostok::animation::legs_ik_drawer` (+0 / −1)

- `−` `draw_leg(class vostok::math::float4x4const &, class vostok::math::float4x4const &, class vostok::math::float4x4const &, class vostok::math::float4x4const &, class vostok::math::color const &, class vostok::math::color const &, class vostok::math::color const &, class vostok::math::color const &, float)`

---

## 🟡 REWORKED · `vostok::buffer_vector<class vostok::physics::loose_ptr<class vostok::physics::base_physics_object, class vostok::physics::loose_ptr_data, class vostok::threading::multi_threading_policy> >` (+0 / −1)

- `−` `assign<class vostok::physics::loose_ptr<class vostok::physics::base_physics_object, class vostok::physics::loose_ptr_data, class vostok::threading::multi_threading_policy> *>(class vostok::physics::loose_ptr<class vostok::physics::base_physics_object, class vostok::physics::loose_ptr_data, class vostok::threading::multi_threading_policy> *, class vostok::physics::loose_ptr<class vostok::physics::base_physics_object, class vostok::physics::loose_ptr_data, class vostok::threading::multi_threading_policy> *const &)`

---

## 🔴 REMOVED · `vostok::buffer_vector<struct stlp_std::pair<class vostok::network_core::udp_match_packet *, struct stlp_std::pair<class boost::asio::ip::basic_endpoint<class boost::asio::ip::udp>, struct vostok::network_core::socket_handler *> > >` (+0 / −1)

- `−` `push_back(struct stlp_std::pair<class vostok::network_core::udp_match_packet *, struct stlp_std::pair<class boost::asio::ip::basic_endpoint<class boost::asio::ip::udp>, struct vostok::network_core::socket_handler *> > const &)`

---

## 🔴 REMOVED · `vostok::buffer_vector<struct survarium::squad_member_item>` (+0 / −1)

- `−` `resize(unsigned int)`

---

## 🔴 REMOVED · `vostok::buffer_vector<struct vostok::physics::old_bullet_character_controller::sweep_test_cache_item *>` (+0 / −1)

- `−` `resize(unsigned int)`

---

## 🟡 REWORKED · `vostok::buffer_vector<unsigned short>` (+0 / −1)

- `−` `assign<unsigned short const *>(unsigned short const *, unsigned short const *const &)`

---

## 🟡 REWORKED · `vostok::render::backend` (+0 / −1)

- `−` `flush_rt_shader_resources(void)`

---

## 🟡 REWORKED · `vostok::render::hw_hiz_point_list` (+0 / −1)

- `−` `render(unsigned int)`

