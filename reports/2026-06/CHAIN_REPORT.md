# Survarium cross-version chain report

hand-written engine (compiler-generated excluded) functions under `vostok/*`, deduped by demangled name. `changed` magnitude is the lowest match % across units.

## Overview

| step | from | to | +added | -deleted | ~changed | =identical |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| 1 | v0.100b-build802 | v0.1.1a-build816 | 88 | 56 | 400 | 11060 |
| 2 | v0.1.1a-build816 | v0.1.1b-build826 | 19 | 26 | 254 | 11268 |
| 3 | v0.1.1b-build826 | v0.1.1c-build870 | 142 | 160 | 1465 | 9916 |
| 4 | v0.1.1c-build870 | v0.1.1e-build884 | 25 | 38 | 473 | 11012 |
| 5 | v0.1.1e-build884 | v0.20e-build1916 | 4163 | 6812 | 4526 | 172 |
| 6 | v0.20e-build1916 | v0.20f-build1923 | 1 | 3 | 11 | 8847 |
| 7 | v0.20f-build1923 | v0.21d-build2010 | 605 | 383 | 2566 | 5910 |

---

## v0.100b-build802 → v0.1.1a-build816
_2013-05-09 → 2013-05-14 · +88 / -56 / ~400_

### Changed (400)

| match % | function |
| ---: | --- |
| 0.00 | `long __cdecl vostok::threading::interlocked_decrement(long volatile &)` |
| 0.00 | `private: bool __thiscall survarium::weapon_user_animations_selector::jump_predicate(void) const` |
| 0.00 | `private: virtual void __thiscall survarium::medkit::tick(void)` |
| 0.00 | `protected: virtual void __thiscall survarium::weapon_core_shotgun_reload_finish_substate::finalize(void)` |
| 0.00 | `public: __thiscall survarium::vector<class vostok::variant<32> const *>::~vector<class vostok::variant<32> const *>(void)` |
| 0.00 | `public: __thiscall vostok::ai::brain_unit_cook_params::~brain_unit_cook_params(void)` |
| 0.00 | `public: __thiscall vostok::animation::mixing::animation_interval::~animation_interval(void)` |
| 0.00 | `public: __thiscall vostok::math::float3::float3(void)` |
| 0.00 | `public: __thiscall vostok::network::order::order(void)` |
| 0.00 | `public: __thiscall vostok::one_way_threads_channel<class vostok::intrusive_spsc_queue<class vostok::network::order, class vostok::network::order, 4>, class vostok::intrusive_spsc_queue<class vostok::network::order, class vostok::network::order, 4> >::~one_way_threads_channel<class vostok::intrusive_spsc_queue<class vostok::network::order, class vostok::network::order, 4>, class vostok::intrusive_spsc_queue<class vostok::network::order, class vostok::network::order, 4> >(void)` |
| 0.00 | `public: __thiscall vostok::render::box_geometry::~box_geometry(void)` |
| 0.00 | `public: __thiscall vostok::render::stage_lights::lights_instance::lights_instance(void)` |
| 0.00 | `public: __thiscall vostok::render::sun_cascade::sun_cascade(struct vostok::render::sun_cascade const &)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::render::material, class vostok::resources::unmanaged_intrusive_base>::~resource_ptr<class vostok::render::material, class vostok::resources::unmanaged_intrusive_base>(void)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::unmanaged_resource *)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>::~resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>(void)` |
| 0.00 | `public: __thiscall vostok::vfs::query_mount_arguments::~query_mount_arguments(void)` |
| 0.00 | `public: __thiscall vostok::vfs::vfs_mount::~vfs_mount(void)` |
| 0.00 | `public: class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> & __thiscall vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>::operator=(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &)` |
| 0.00 | `public: class vostok::vfs::query_mount_arguments & __thiscall vostok::vfs::query_mount_arguments::operator=(class vostok::vfs::query_mount_arguments const &)` |
| 0.00 | `public: virtual __thiscall survarium::inventory_cook::~inventory_cook(void)` |
| 0.00 | `public: virtual __thiscall vostok::render::functor_command::~functor_command(void)` |
| 0.00 | `public: virtual void __thiscall survarium::game_camera::on_focus(bool)` |
| 0.00 | `public: virtual void __thiscall survarium::weapon_core::tick(void)` |
| 0.00 | `public: virtual void __thiscall vostok::network::functor_order::execute(void)` |
| 0.00 | `survarium::true_predicate` |
| 0.00 | `vec_begin` |
| 12.00 | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 21.12 | `protected: virtual void __thiscall survarium::weapon_core_aimed_fire_state_base::initialize(void)` |
| 39.68 | `protected: virtual void __thiscall survarium::weapon_core_aimed_fire_state_base::finalize(void)` |
| 40.13 | `public: bool __thiscall survarium::swf_input_translator::process_keyboard(struct vostok::input::world *, enum vostok::input::enum_keyboard, enum vostok::input::enum_keyboard_action, struct survarium::flash_movie *, unsigned int)` |
| 40.60 | `private: virtual void __thiscall survarium::weapon_core_aimed_fire_state_base::on_animation_end_impl(bool &)` |
| 40.60 | `protected: virtual void __thiscall survarium::weapon_core_fire_state_base::on_animation_end_impl(bool &)` |
| 48.57 | `private: virtual void __thiscall survarium::weapon_core_idle_state_base::finalize(void)` |
| 51.73 | `protected: virtual void __thiscall survarium::weapon_core_fire_state_base::finalize(void)` |
| 59.61 | `private: void __thiscall survarium::weapon_core_shotgun_reload_state::initialize_logic(class survarium::weapon_core_shotgun_reload_base_substate *, class survarium::weapon_core_shotgun_reload_base_substate *, class survarium::weapon_core_shotgun_reload_base_substate *)` |
| 59.90 | `public: virtual void __thiscall survarium::weapon_core::instant_aim_start(void)` |
| 60.00 | `protected: virtual void __thiscall survarium::weapon_core_hide_state_base::finalize(void)` |
| 60.00 | `protected: virtual void __thiscall survarium::weapon_core_show_state_base::finalize(void)` |
| 65.95 | `private: virtual void __thiscall survarium::weapon::deactivate(void)` |
| 65.96 | `private: enum vostok::animation::callback_return_type_enum __thiscall survarium::weapon_core_shotgun_reload_finish_substate::on_animation_end(struct vostok::animation::animation_callback_params &)` |
| 65.98 | `protected: virtual void __thiscall survarium::weapon_core_fire_state_base::initialize(void)` |
| 67.05 | `public: __thiscall survarium::player_profile::player_profile(void)` |
| 69.82 | `public: virtual void __thiscall survarium::relocate_item_func::call(struct survarium::flash_function_handler_params &)` |
| 70.00 | `protected: virtual void __thiscall survarium::weapon_core_hide_state_base::initialize(void)` |
| 70.00 | `protected: virtual void __thiscall survarium::weapon_core_show_state_base::initialize(void)` |
| 70.89 | `private: void __thiscall vostok::sound::single_sound_cook::on_sub_resources_loaded(class vostok::resources::queries_result &)` |
| 70.92 | `public: void __thiscall survarium::weapon_core::instant_idle_start(void)` |
| 71.11 | `public: virtual void __thiscall survarium::weapon_core::instant_aim_end(void)` |
| 73.21 | `private: bool __thiscall survarium::weapon_core_shotgun_reload_state::finish_reload_predicate(void) const` |
| 76.91 | `vostok::render::fill_light` |
| 80.30 | `void __cdecl vostok::render::register_samplers(void)` |
| 80.36 | `private: void __thiscall vostok::network::match_client::on_packet_received_impl(unsigned char, class vostok::network_core::packet_reader &)` |
| 80.70 | `private: void __thiscall survarium::weapon_core::initialize_weapon_logic(class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 82.15 | `protected: void __thiscall survarium::swf_input_translator::initialize(void)` |
| 85.60 | `private: virtual void __thiscall survarium::player_logic_sprint_state::initialize(void)` |
| 85.88 | `private: virtual void __thiscall survarium::weapon_core::serialize(class vostok::network_core::udp_match_packet &, unsigned int) const` |
| 86.81 | `public: bool __thiscall survarium::damage_model::hit_body_part(unsigned char, char const *, char const *, float, float, unsigned int, class survarium::bullet *const)` |
| 88.39 | `public: virtual __thiscall vostok::sound::single_sound::~single_sound(void)` |
| 88.88 | `public: void __thiscall survarium::weapon_user_animations_selector::serialize(class vostok::network_core::udp_match_packet &) const` |
| 89.35 | `private: virtual void __thiscall survarium::player::on_fire(void)` |
| 89.57 | `private: void __thiscall survarium::lobby_menu::request_status_from_server_impl(unsigned int, unsigned int)` |
| 89.61 | `public: void __thiscall survarium::weapon_user_animations_selector::tick(void)` |
| 90.17 | `public: void __thiscall survarium::character_dispersion_calculator::tick(enum survarium::weapon_user_state_enum, bool, bool, unsigned char, bool, unsigned int)` |
| 91.08 | `public: virtual void __thiscall vostok::sound::single_sound_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 91.11 | `private: void __thiscall vostok::sound::sound_world::register_sound_cooks(void)` |
| 91.19 | `public: void __thiscall survarium::weapon_user_animations_selector::deserialize(class vostok::network_core::packet_reader &)` |
| 91.20 | `public: virtual void __thiscall survarium::respawn_point_core::load(class vostok::configs::binary_config_value const &)` |
| 91.39 | `private: virtual void __thiscall survarium::weapon_core::deserialize(class vostok::network_core::packet_reader &)` |
| 92.18 | `public: void __thiscall survarium::weapon_core::instant_fire(unsigned int)` |
| 92.24 | `public: __thiscall survarium::weapon_core::weapon_core(void)` |
| 92.43 | `public: __thiscall survarium::respawn_point_core::respawn_point_core(void)` |
| 93.24 | `public: float __thiscall survarium::dispersion_calculator::get_dispersion(void) const` |
| 94.08 | `public: virtual bool __thiscall survarium::lobby_menu::on_keyboard_action(struct vostok::input::world *, enum vostok::input::enum_keyboard, enum vostok::input::enum_keyboard_action)` |
| 94.08 | `private: void __thiscall survarium::player::insert_alive(void)` |
| 94.12 | `protected: void __thiscall survarium::swf_input_translator::register_ctl_bind(enum vostok::input::enum_keyboard, int)` |
| 94.19 | `public: __thiscall survarium::base_player_creation_params::base_player_creation_params(void)` |
| 94.32 | `public: void __thiscall survarium::player_profile::deserialize(class vostok::network_core::packet_reader &)` |
| 94.39 | `protected: __thiscall survarium::weapon_core_aimed_state_base::weapon_core_aimed_state_base(class survarium::weapon_core &)` |
| 94.39 | `protected: __thiscall survarium::weapon_core_idle_state_base::weapon_core_idle_state_base(class survarium::weapon_core &)` |
| 94.56 | `public: void __thiscall survarium::lobby_menu::on_stats_message_arrived(wchar_t const *, wchar_t const *, enum messaging::message_channel_enum)` |
| 95.10 | `public: void __thiscall survarium::player::tick(unsigned int)` |
| 95.13 | `public: virtual void __thiscall survarium::weapon_core::set_next_ammo_type(void)` |
| 95.56 | `public: __thiscall survarium::base_player::base_player(struct survarium::base_player_creation_params const &, class survarium::scheduler &)` |
| 95.91 | `public: virtual bool __thiscall survarium::chat_handler::on_keyboard_action(struct vostok::input::world *, enum vostok::input::enum_keyboard, enum vostok::input::enum_keyboard_action)` |
| 96.39 | `protected: __thiscall survarium::weapon_core_aimed_fire_state_base::weapon_core_aimed_fire_state_base(class survarium::weapon_core &, float)` |
| 96.60 | `protected: __thiscall survarium::weapon_core_chamber_a_round_aimed_state_base::weapon_core_chamber_a_round_aimed_state_base(class survarium::weapon_core &, float)` |
| 96.60 | `protected: __thiscall survarium::weapon_core_chamber_a_round_state_base::weapon_core_chamber_a_round_state_base(class survarium::weapon_core &, float)` |
| 96.60 | `protected: __thiscall survarium::weapon_core_hide_state_base::weapon_core_hide_state_base(class survarium::weapon_core &, bool &)` |
| 96.60 | `protected: __thiscall survarium::weapon_core_reload_state_base::weapon_core_reload_state_base(class survarium::weapon_core &, float)` |
| 96.63 | `protected: __thiscall survarium::weapon_core_fire_state_base::weapon_core_fire_state_base(class survarium::weapon_core &, float)` |
| 96.63 | `protected: __thiscall survarium::weapon_core_show_state_base::weapon_core_show_state_base(class survarium::weapon_core &, bool &)` |
| 96.81 | `public: virtual class vostok::animation::mixing::expression __thiscall survarium::weapon_core::selected_animations(class vostok::mutable_buffer &, bool) const` |
| 96.81 | `public: __thiscall survarium::weapon_core_shotgun_reload_state::weapon_core_shotgun_reload_state(class survarium::weapon_core &, class survarium::weapon_core_shotgun_reload_base_substate *, class survarium::weapon_core_shotgun_reload_base_substate *, class survarium::weapon_core_shotgun_reload_base_substate *)` |
| 97.09 | `public: __thiscall survarium::damage_model::damage_model(enum survarium::affects_applying_type_enum)` |
| 97.59 | `public: void __thiscall survarium::weapon_core::reload_one_round(void)` |
| 98.08 | `private: void __thiscall vostok::render::stage_lights::render_to_hw_shadowmap(class vostok::render::light *, unsigned int, float, unsigned int, unsigned int, class vostok::math::float4x4const &, class vostok::math::float4x4const &, unsigned int)` |
| 98.42 | `private: void __thiscall survarium::player_cook::on_config_loaded(class vostok::resources::queries_result &)` |
| 98.44 | `public: virtual void __thiscall survarium::weapon_core_inactive_state_cook::create_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, class vostok::mutable_buffer)` |
| 98.61 | `public: __thiscall survarium::weapon_user_animations_selector::weapon_user_animations_selector(void)` |
| 98.62 | `private: void __thiscall vostok::network::login_client_impl::sign_up_on_connected(enum vostok::connection_error_types_enum, class boost::function<void __cdecl (enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::login_server_message_types_enum, struct vostok::sign_up_info const &)> const &, struct vostok::sign_up_info const &)` |
| 98.71 | `public: virtual bool __thiscall survarium::game_options::on_keyboard_action(struct vostok::input::world *, enum vostok::input::enum_keyboard, enum vostok::input::enum_keyboard_action)` |
| 98.93 | `private: void __thiscall vostok::render::stage_lights::make_spot_light_shadowmap(unsigned int, class vostok::render::light *)` |
| 99.21 | `private: void __thiscall vostok::render::stage_lights::make_plane_spot_light_shadowmap(unsigned int, class vostok::render::light *)` |
| 99.31 | `public: virtual void __thiscall survarium::weapon_core::activate(struct survarium::base_player &, struct survarium::engine &)` |
| 99.32 | `private: void __thiscall vostok::vfs::archive_mounter::mount_archive_to_parent(void **, class vostok::vfs::base_folder_node<1> *, class vostok::fs_new::synchronous_device_interface &)` |
| 99.33 | `public: __thiscall vostok::animation::animation_player::animation_player(void)` |
| 99.33 | `public: void __thiscall survarium::player::set_target_fov_factor(float, float)` |
| 99.40 | `public: void __thiscall survarium::player::reset_fov_factor(void)` |
| 99.50 | `private: virtual bool __thiscall survarium::player::is_replaying_history(void) const` |
| 99.50 | `private: virtual class survarium::player_stamina & __thiscall survarium::player::stamina(void)` |
| 99.50 | `private: virtual class vostok::animation::animation_player & __thiscall survarium::player::animation_player(void)` |
| 99.50 | `private: virtual class vostok::math::float3const & __thiscall survarium::player::position(void) const` |
| 99.50 | `private: virtual class vostok::math::float4x4const & __thiscall survarium::player::get_transform(void) const` |
| 99.50 | `private: virtual class vostok::physics::bt_character_controller & __thiscall survarium::player::physics_controller(void)` |
| 99.50 | `private: virtual float __thiscall survarium::player::get_look_pitch(void) const` |
| 99.50 | `private: virtual struct survarium::player_input const & __thiscall survarium::player::input(void) const` |
| 99.50 | `private: void __thiscall survarium::player::remove_oldest_history_item(void)` |
| 99.50 | `public: bool __thiscall survarium::base_player::is_alive(void) const` |
| 99.50 | `public: bool __thiscall survarium::weapon_core::round_is_chambered(void) const` |
| 99.50 | `public: struct survarium::base_player * __thiscall survarium::weapon_core::get_user(void) const` |
| 99.50 | `public: unsigned int __thiscall vostok::animation::animation_player::last_tick_time_in_ms(void) const` |
| 99.50 | `public: virtual class vostok::resources::resource_ptr<class survarium::damage_model, class vostok::resources::unmanaged_intrusive_base> const & __thiscall survarium::player::damage_model(void) const` |
| 99.50 | `public: virtual enum survarium::game_team_id __thiscall survarium::player::team(void) const` |
| 99.50 | `public: void __thiscall survarium::base_player::force_animation_selection(void)` |
| 99.53 | `private: virtual void __thiscall survarium::weapon::instant_aim_end(void)` |
| 99.53 | `private: void __thiscall survarium::player::remove_oldest_history_items(unsigned int)` |
| 99.62 | `private: void * __thiscall vostok::animation::animation_player::get_next_buffer(unsigned int)` |
| 99.66 | `public: __thiscall survarium::player::player(struct survarium::player_creation_params const &)` |
| 99.67 | `private: virtual class vostok::animation::skeleton const & __thiscall survarium::player::skeleton(void) const` |
| 99.67 | `public: virtual struct vostok::physics::world * __thiscall survarium::player::get_physics_world(void)` |
| 99.68 | `private: void __thiscall survarium::network_client::on_connected_to_match(enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::lobby_server_message_types_enum)` |
| 99.68 | `private: void __thiscall vostok::render::stage_lights::render_shadowed_light(class vostok::render::light *)` |
| 99.68 | `private: void __thiscall survarium::player::remove_alive(void)` |
| 99.69 | `private: virtual void __thiscall survarium::weapon::instant_aim_start(void)` |
| 99.70 | `private: virtual void __thiscall survarium::player::end_jump(void)` |
| 99.75 | `public: unsigned short __thiscall survarium::weapon_core::fire_queue_length(void) const` |
| 99.75 | `public: void __thiscall survarium::player::attach_controller(class survarium::player_input_handler *, class survarium::stats_graph *, class survarium::stats_graph *, class survarium::game_world_ui *)` |
| 99.75 | `public: void __thiscall survarium::player::detach_controller(void)` |
| 99.75 | `survarium::is_alive` |
| 99.77 | `public: __thiscall survarium::character_dispersion_calculator::character_dispersion_calculator(void)` |
| 99.78 | `private: void __thiscall survarium::player::serialize_current_state(unsigned int)` |
| 99.79 | `public: void __thiscall survarium::dispersion_calculator::set_weapon(class survarium::weapon_core *)` |
| 99.80 | `public: void __thiscall survarium::player::time_warp(struct survarium::server_player_update const &, unsigned int)` |
| 99.80 | `private: void __thiscall vostok::intrusive_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock>::dec(void)` |
| 99.81 | `private: void __thiscall survarium::player::set_head_visibility(bool)` |
| 99.82 | `public: bool __thiscall vostok::animation::animation_player::tick(unsigned int)` |
| 99.83 | `public: __thiscall survarium::base_player_creation_params::~base_player_creation_params(void)` |
| 99.83 | `public: void __thiscall survarium::player::update_camera(void)` |
| 99.83 | `public: __thiscall vostok::resources::resource_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base>::~resource_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base>(void)` |
| 99.83 | `public: virtual __thiscall survarium::player::~player(void)` |
| 99.83 | `private: void __thiscall survarium::dispersion_calculator::apply_aim_speed(void)` |
| 99.83 | `private: void __thiscall survarium::player::replay_history(unsigned int, class vostok::math::float4x4&)` |
| 99.83 | `private: virtual void __thiscall survarium::player::subscribe_on_actions(class survarium::player_actions_subscriber *)` |
| 99.83 | `public: void __thiscall survarium::player::hide(void)` |
| 99.83 | `public: void __thiscall survarium::player::set_near_plane_factor(float)` |
| 99.83 | `public: void __thiscall survarium::player::show(void)` |
| 99.83 | `public: void __thiscall vostok::animation::animation_player::set_object_transform(class vostok::math::float4x4const &, void const *const)` |
| 99.83 | `survarium::is_dead` |
| 99.83 | `private: void __thiscall survarium::player::update_speed_info(void)` |
| 99.84 | `private: void __thiscall survarium::network_client::setup_camera_for_warmup(void)` |
| 99.84 | `public: void __thiscall survarium::player::insert(bool)` |
| 99.84 | `public: float __thiscall survarium::player::fov_factor(unsigned int) const` |
| 99.85 | `private: unsigned int __thiscall survarium::player::history_lower_bound_index(unsigned int) const` |
| 99.85 | `private: void __thiscall survarium::player::add_models_to_scene(void)` |
| 99.85 | `public: bool __thiscall vostok::animation::animation_player::tick_to_nearest_user_handled_callback(unsigned int)` |
| 99.86 | `private: virtual struct survarium::engine & __thiscall survarium::player::get_engine(void)` |
| 99.86 | `private: void __thiscall survarium::player::render(unsigned int, unsigned int)` |
| 99.86 | `public: __thiscall survarium::dispersion_calculator::dispersion_calculator(void)` |
| 99.86 | `public: void __thiscall vostok::animation::animation_player::convert_to_object_matrices(class vostok::animation::skeleton const &, class vostok::math::float4x4*, class vostok::math::float4x4*, void const *const) const` |
| 99.86 | `private: void __thiscall survarium::player::compute_bones(unsigned int)` |
| 99.87 | `private: void __thiscall survarium::player::notify_actions_subscribers(void)` |
| 99.87 | `private: struct survarium::player_input __thiscall survarium::player::remote_input(void) const` |
| 99.87 | `private: void __thiscall survarium::player::set_physics_controller_walk_vector(struct survarium::client_player_state &)` |
| 99.87 | `private: void __thiscall survarium::weapon_core::update_breath_vibration(bool, unsigned int, float)` |
| 99.87 | `public: void __thiscall survarium::client_player_state::update_transform(void)` |
| 99.87 | `public: void __thiscall survarium::player::remove(void)` |
| 99.87 | `private: virtual void __thiscall survarium::player::jump(void)` |
| 99.88 | `public: virtual bool __thiscall survarium::login_menu::on_keyboard_action(struct vostok::input::world *, enum vostok::input::enum_keyboard, enum vostok::input::enum_keyboard_action)` |
| 99.88 | `public: void __thiscall survarium::player::set_character_transform(class vostok::math::float3const &, float, float)` |
| 99.88 | `public: __thiscall survarium::client_player_state::~client_player_state(void)` |
| 99.88 | `public: void __thiscall vostok::animation::animation_player::reset(bool)` |
| 99.88 | `public: virtual __thiscall survarium::weapon_core::~weapon_core(void)` |
| 99.89 | `private: void __thiscall survarium::player::restore_history_item(struct survarium::client_player_history_item &)` |
| 99.89 | `public: class vostok::math::float4x4 __thiscall vostok::animation::animation_player::get_object_transform(void const *const) const` |
| 99.89 | `public: virtual class vostok::resources::resource_ptr<class vostok::sound::sound_spl, class vostok::resources::unmanaged_intrusive_base> const & __thiscall vostok::sound::single_sound::get_sound_spl(void) const` |
| 99.89 | `public: void __thiscall survarium::player::set_use_physics_controller_for_current(bool)` |
| 99.89 | `public: void __thiscall survarium::weapon_core::remove_animation_callback(char const *, void const *)` |
| 99.89 | `public: void __thiscall survarium::weapon_core::remove_animation_callback(enum vostok::animation::reserved_channel_ids_enum, void const *)` |
| 99.89 | `public: void __thiscall vostok::animation::animation_player::compute_bones_local_matrices(class vostok::animation::skeleton const &, class vostok::math::float4x4*, class vostok::math::float4x4*, void const *const, unsigned int *) const` |
| 99.89 | `public: void __thiscall vostok::animation::animation_player::compute_bones_matrices(class vostok::animation::skeleton const &, class vostok::math::float4x4*, class vostok::math::float4x4*, void const *const, unsigned int *) const` |
| 99.89 | `public: void __thiscall survarium::player::kill(unsigned int)` |
| 99.89 | `private: void __thiscall survarium::player::remove_models_from_scene(void)` |
| 99.89 | `public: void __thiscall survarium::character_dispersion_calculator::set_character_dispersion_params(struct survarium::character_dispersion_params const *)` |
| 99.89 | `private: enum vostok::animation::body_part_masks_enum __thiscall survarium::weapon_core::get_body_part_mask_for_user(void) const` |
| 99.89 | `private: void __thiscall survarium::network_client::game_world_object_state_arrived(class vostok::network_core::packet_reader &)` |
| 99.90 | `public: char const * __thiscall vostok::network::login_client::host_ip_address(void) const` |
| 99.90 | `public: char const * __thiscall vostok::network::login_client::server_browser_address(void) const` |
| 99.90 | `public: char const * __thiscall vostok::network::login_client::server_browser_initial_query(void) const` |
| 99.90 | `public: void __thiscall survarium::dispersion_calculator::set_shooting_skill_coeff(float)` |
| 99.90 | `private: void __thiscall survarium::profile_character::character_model_ready(class vostok::resources::queries_result &)` |
| 99.90 | `public: void __thiscall survarium::base_network_client::attach_to_player(class vostok::resources::resource_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base>)` |
| 99.90 | `public: void __thiscall vostok::animation::animation_player::serialize_state(void *, unsigned int)` |
| 99.90 | `private: void __thiscall survarium::network_client::damage_model_state_arrived(class vostok::network_core::packet_reader &)` |
| 99.91 | `private: void __thiscall survarium::network_client::player_visibility_change(class vostok::network_core::packet_reader &)` |
| 99.91 | `private: virtual void __thiscall survarium::player::unsubscribe_from_actions(class survarium::player_actions_subscriber *)` |
| 99.91 | `private: bool __thiscall vostok::animation::animation_player::try_get_transform(void const *, class vostok::math::float4x4&) const` |
| 99.91 | `public: virtual void __thiscall survarium::weapon_core::deactivate(void)` |
| 99.91 | `public: void __thiscall vostok::animation::animation_player::subscribe(char const *, class boost::function<enum vostok::animation::callback_return_type_enum __cdecl (struct vostok::animation::animation_callback_params &)> const &, void const *, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, unsigned char, void const *const)` |
| 99.91 | `private: void __thiscall survarium::weapon_core::update_dispersion(bool, unsigned int)` |
| 99.91 | `public: virtual class vostok::resources::resource_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base> __thiscall survarium::network_client::get_player(unsigned char) const` |
| 99.91 | `public: void __thiscall survarium::profile_player_character::clear_resources(void)` |
| 99.91 | `private: void __thiscall survarium::network_client::destroy_player_impl(unsigned char)` |
| 99.91 | `private: virtual void __thiscall survarium::network_client::apply_use_physics_controller_for_current(void)` |
| 99.92 | `private: virtual void __thiscall survarium::player::unsubscribe_animation_player(enum vostok::animation::reserved_channel_ids_enum, void const *)` |
| 99.92 | `private: virtual void __thiscall survarium::weapon::on_chamber_a_round(void)` |
| 99.92 | `private: virtual void __thiscall survarium::weapon::on_unload_chambered_round(void)` |
| 99.92 | `protected: bool __thiscall survarium::weapon_core_base_state::deserializing(void) const` |
| 99.92 | `public: void __thiscall survarium::dispersion_calculator::set_aiming_speed_coeff(float)` |
| 99.92 | `private: void __thiscall survarium::network_client::process_player_hit(class vostok::network_core::packet_reader &)` |
| 99.92 | `private: bool __thiscall vostok::animation::animation_player::set_target(class vostok::animation::mixing::expression const &, unsigned int, class boost::function<class vostok::math::float4x4 __cdecl (void const *)> const &)` |
| 99.92 | `private: bool __thiscall survarium::weapon_user_animations_selector::broken_legs_predicate(void) const` |
| 99.92 | `private: void __thiscall survarium::network_client::process_player_kill(class vostok::network_core::packet_reader &)` |
| 99.92 | `private: void __thiscall survarium::profile_player_character::on_player_ready(class vostok::resources::queries_result &, struct survarium::player_profile *)` |
| 99.92 | `private: virtual void __thiscall survarium::player::unsubscribe_animation_player(char const *, void const *)` |
| 99.92 | `private: virtual void __thiscall survarium::weapon::set_next_fire_queue_type(void)` |
| 99.92 | `private: void __thiscall survarium::network_client::on_trap_disarmed(class vostok::network_core::packet_reader &)` |
| 99.92 | `private: void __thiscall survarium::network_client::on_trap_fired(class vostok::network_core::packet_reader &)` |
| 99.92 | `private: void __thiscall survarium::network_client::on_trap_removed(class vostok::network_core::packet_reader &)` |
| 99.92 | `public: __thiscall vostok::resources::resource_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base>::resource_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base>(class survarium::player *)` |
| 99.92 | `public: virtual void __thiscall survarium::base_player::insert_game_world_object(class survarium::game_world_object &)` |
| 99.92 | `public: void __thiscall survarium::weapon_core::set_skeleton(class vostok::resources::resource_ptr<class vostok::animation::skeleton, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 99.93 | `public: unsigned short __thiscall survarium::weapon_core::maximum_ammo_in_weapon(void) const` |
| 99.93 | `private: enum vostok::animation::callback_return_type_enum __thiscall survarium::weapon::on_foot_step(struct vostok::animation::animation_callback_params &)` |
| 99.93 | `private: void __thiscall survarium::player::apply_input(struct survarium::client_player_state &, class vostok::math::float2const &)` |
| 99.93 | `public: __thiscall vostok::animation::animation_player::~animation_player(void)` |
| 99.93 | `public: virtual void __thiscall survarium::base_player::remove_game_world_object(class survarium::game_world_object &)` |
| 99.93 | `public: void __thiscall survarium::weapon_core::set_ammunition(class vostok::resources::resource_ptr<class survarium::weapon_ammunition, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 99.93 | `private: void __thiscall survarium::weapon_core::load_ammo(void)` |
| 99.93 | `public: void __thiscall survarium::weapon_core::set_animation_callback(enum vostok::animation::reserved_channel_ids_enum, void const *, class boost::function<enum vostok::animation::callback_return_type_enum __cdecl (struct vostok::animation::animation_callback_params &)> const &)` |
| 99.93 | `protected: virtual void __thiscall survarium::weapon_core_aimed_state_base::initialize(void)` |
| 99.93 | `public: void __thiscall survarium::weapon_core::set_animation_callback(char const *, void const *, class boost::function<enum vostok::animation::callback_return_type_enum __cdecl (struct vostok::animation::animation_callback_params &)> const &)` |
| 99.94 | `private: void __thiscall survarium::damage_model::on_broken_limb_affect(char const *, enum survarium::hit_affects_type_enum, enum survarium::affect_event_type_enum)` |
| 99.94 | `public: bool __thiscall survarium::weapon_core::could_be_used(struct survarium::base_player const &) const` |
| 99.94 | `public: virtual __thiscall survarium::damage_model::~damage_model(void)` |
| 99.94 | `public: __thiscall vostok::resources::resource_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base>::resource_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::resource_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 99.94 | `public: class vostok::resources::resource_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base> __thiscall survarium::base_network_client::get_current_player(void)` |
| 99.94 | `public: class vostok::resources::resource_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base> __thiscall survarium::network_client::get_local_player(void)` |
| 99.94 | `public: float __thiscall survarium::animation_space_graph::max_speed(void) const` |
| 99.94 | `private: void __thiscall survarium::network_client::on_trap_placed(class vostok::network_core::packet_reader &)` |
| 99.94 | `protected: virtual void __thiscall survarium::weapon_core_chamber_a_round_aimed_state_base::finalize(void)` |
| 99.94 | `protected: virtual void __thiscall survarium::weapon_core_chamber_a_round_aimed_state_base::initialize(void)` |
| 99.94 | `private: void __thiscall survarium::network_client::process_player_respawn(class vostok::network_core::packet_reader &)` |
| 99.94 | `private: virtual void __thiscall survarium::player::take_inventory_item(class vostok::resources::resource_ptr<class survarium::inventory_item, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 99.94 | `protected: virtual void __thiscall survarium::weapon_core_aimed_state_base::finalize(void)` |
| 99.94 | `public: virtual class vostok::math::float3 __thiscall survarium::base_network_client::get_current_player_position(void) const` |
| 99.94 | `public: virtual void __thiscall survarium::network_client::unload(void)` |
| 99.95 | `public: void __thiscall survarium::weapon_core::unload_ammo(void)` |
| 99.95 | `public: void __thiscall survarium::base_network_client::detach_from_player(void)` |
| 99.95 | `private: void __thiscall survarium::player::apply_input_before_new_transform(struct survarium::client_player_state &, struct survarium::player_input const &, float)` |
| 99.95 | `private: void __thiscall survarium::network_client::process_affect_damage_model(class vostok::network_core::packet_reader &)` |
| 99.95 | `public: bool __thiscall vostok::animation::animation_player::set_target_and_tick(class vostok::animation::mixing::expression const &, unsigned int, class boost::function<class vostok::math::float4x4 __cdecl (void const *)> const &)` |
| 99.95 | `private: void __thiscall survarium::player_cook::on_hit_params_loaded(class vostok::resources::queries_result &, struct survarium::player_creation_params *)` |
| 99.95 | `private: virtual void __thiscall survarium::player::hit(struct survarium::hit_initiator const *const, unsigned int, char const *, float, float, class survarium::bullet *const)` |
| 99.95 | `public: void __thiscall survarium::player::apply_damage_model_affect(char const *, enum survarium::hit_affects_type_enum, enum survarium::affect_event_type_enum)` |
| 99.95 | `private: virtual void __thiscall survarium::player::crouch(void)` |
| 99.95 | `private: virtual void __thiscall survarium::player::stand_up(void)` |
| 99.95 | `private: virtual bool __thiscall survarium::player_logic_jump_state::is_ready_for_transition(void) const` |
| 99.95 | `private: void __thiscall survarium::game_world::clear_player_spawn_info(void)` |
| 99.95 | `private: void __thiscall survarium::player::select_animations(unsigned int)` |
| 99.95 | `private: struct survarium::player_input __thiscall survarium::player::local_input(void) const` |
| 99.95 | `private: void __thiscall survarium::player::smooth(float)` |
| 99.95 | `protected: void __thiscall survarium::weapon_core_cook::load_weapon_parameters(class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class survarium::weapon_core *)` |
| 99.95 | `private: virtual void __thiscall survarium::weapon::on_after_fire(void)` |
| 99.96 | `public: void __thiscall survarium::player::apply_hit_directly(struct survarium::hit_info const &, unsigned int)` |
| 99.96 | `public: void __thiscall survarium::weapon_core::chamber_a_round(void)` |
| 99.96 | `private: void __thiscall survarium::player::render_crosshair_info(void)` |
| 99.96 | `public: virtual __thiscall survarium::base_network_client::~base_network_client(void)` |
| 99.96 | `public: void __thiscall vostok::animation::animation_player::deserialize_state(void *, unsigned int)` |
| 99.96 | `private: virtual float __thiscall survarium::player::get_speed(void) const` |
| 99.96 | `private: virtual void __thiscall survarium::player::on_before_active_object_changed(class vostok::resources::resource_ptr<class survarium::interactive_object, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::interactive_object, class vostok::resources::unmanaged_intrusive_base> const &) const` |
| 99.96 | `public: void __thiscall survarium::weapon_core::reset_fire_queue(void)` |
| 99.96 | `void __cdecl vostok::bind_pointer_to_buffer_mt_safe<class vostok::memory::doug_lea_mt_allocator, struct vostok::memory::inplace_constructor>(class vostok::memory::doug_lea_mt_allocator *&, char (&)[112], long volatile &, struct vostok::memory::inplace_constructor)` |
| 99.96 | `public: void __thiscall survarium::weapon_core::unload_chambered_round(void)` |
| 99.96 | `private: void __thiscall survarium::player::update_history_item(struct survarium::client_player_history_item &, struct survarium::client_player_history_item const *, struct survarium::server_player_update const &, unsigned int, class vostok::math::float4x4&, bool &)` |
| 99.96 | `public: virtual __thiscall survarium::network_client::~network_client(void)` |
| 99.96 | `public: virtual __thiscall survarium::base_player::~base_player(void)` |
| 99.97 | `private: void __thiscall survarium::player::process_quick_slots_for_current_player(void)` |
| 99.97 | `private: void __thiscall survarium::human_npc::tick_animation_player(unsigned int)` |
| 99.97 | `public: void __thiscall survarium::weapon_core::load_magazine(void)` |
| 99.97 | `private: void __thiscall survarium::network_client::on_world_sync_request(void)` |
| 99.97 | `private: float __thiscall survarium::weapon_core::computed_horizontal_recoil_time(float, float, unsigned int, unsigned int, unsigned int, float)` |
| 99.97 | `private: float __thiscall survarium::weapon_core::computed_vertical_recoil_time(float, float, unsigned int, unsigned int, unsigned int, float)` |
| 99.97 | `private: void __thiscall vostok::network::login_client::create_client(void)` |
| 99.97 | `protected: virtual void __thiscall survarium::weapon_core_reload_state_base::initialize(void)` |
| 99.97 | `private: virtual void __thiscall survarium::weapon_core::update_bones_matrices(class vostok::resources::resource_ptr<class vostok::animation::skeleton, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float4x4*const, unsigned int, unsigned int, class vostok::math::float4x4&, class vostok::math::float4x4&, class vostok::animation::animation_player const &)` |
| 99.97 | `public: void __thiscall survarium::game_world_ui::update_minimap_local_player(void)` |
| 99.97 | `private: class vostok::animation::mixing::expression __thiscall survarium::weapon_core::get_weapon_and_hands_animation_expression(class vostok::mutable_buffer &, bool, enum survarium::weapon_user_state_enum, class vostok::animation::mixing::animation_lexeme &) const` |
| 99.97 | `public: virtual bool __thiscall survarium::weapon_core::is_ready_to_be_deactivated(void) const` |
| 99.97 | `public: virtual void __thiscall survarium::player_cook::delete_resource(class vostok::resources::resource_base *)` |
| 99.97 | `private: void __thiscall vostok::animation::animation_player::compact_callbacks(void)` |
| 99.97 | `private: void __thiscall survarium::animation_space_graph_cook::generate_graph_edges(class survarium::animation_space_graph *)` |
| 99.97 | `private: void __thiscall vostok::animation::animation_player::skip_time_if_needed(unsigned int)` |
| 99.97 | `private: void __thiscall survarium::player::update_history_item_from_previous(struct survarium::client_player_history_item const &, struct survarium::client_player_history_item &, class vostok::math::float4x4&)` |
| 99.97 | `private: void __thiscall survarium::network_client::on_players_ready(class vostok::resources::queries_result &, unsigned int)` |
| 99.97 | `private: virtual void __thiscall survarium::weapon::on_show(void)` |
| 99.97 | `private: void __thiscall survarium::player::detect_usable_objects(unsigned int)` |
| 99.97 | `private: float __thiscall survarium::weapon_core::computed_backward_recoil_time(float, float, unsigned int, unsigned int, unsigned int, float)` |
| 99.97 | `private: virtual void __thiscall survarium::player::hit(struct survarium::hit_initiator const *const, class vostok::collision::bone_collision_data const &, char const *, float, float, class survarium::bullet *const)` |
| 99.97 | `private: virtual void __thiscall survarium::weapon::on_skeleton_matrices_changed(unsigned int, class vostok::math::float4x4const &, class vostok::math::float4x4const *const, class vostok::math::float4x4const *const, class vostok::math::float4x4const &, class vostok::math::float4x4*const, class vostok::math::float4x4*const, class vostok::math::float4x4const &)` |
| 99.97 | `public: void __thiscall survarium::human_npc::set_transform(class vostok::math::float4x4const &)` |
| 99.97 | `private: virtual void __thiscall survarium::player::subscribe_animation_player(char const *, class boost::function<enum vostok::animation::callback_return_type_enum __cdecl (struct vostok::animation::animation_callback_params &)> const &, void const *, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, unsigned char, void const *const)` |
| 99.97 | `public: __thiscall vostok::network::login_client_impl::login_client_impl(class boost::asio::io_service &)` |
| 99.97 | `private: void __thiscall survarium::player_cook::on_subresources_loaded(class vostok::resources::queries_result &, struct survarium::player_creation_params *, struct survarium::inventory_cooker_data *, struct survarium::player_parameters_cooker_data *)` |
| 99.97 | `public: void __thiscall survarium::game_world_ui::update_minimap_players(void)` |
| 99.97 | `private: float __thiscall survarium::weapon_core::vertical_recoil_value(void) const` |
| 99.97 | `private: virtual void __thiscall survarium::player::subscribe_animation_player(enum vostok::animation::reserved_channel_ids_enum, class boost::function<enum vostok::animation::callback_return_type_enum __cdecl (struct vostok::animation::animation_callback_params &)> const &, void const *, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, void const *const)` |
| 99.98 | `private: float __thiscall survarium::weapon_core::horizontal_recoil_value(void) const` |
| 99.98 | `public: void __thiscall vostok::animation::animation_player::unsubscribe(char const *, void const *)` |
| 99.98 | `private: void __thiscall vostok::network::login_client_impl::sign_out_on_connected(enum vostok::connection_error_types_enum, class boost::function<void __cdecl (enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::login_server_message_types_enum)> const &)` |
| 99.98 | `private: class vostok::math::float3 __thiscall survarium::weapon_core::get_dispersed_bullet_dir(void)` |
| 99.98 | `private: void __thiscall survarium::profile_character::character_animation_ready(class vostok::resources::queries_result &)` |
| 99.98 | `public: void __thiscall survarium::game_world_ui::update_ui(unsigned int, unsigned int)` |
| 99.98 | `public: virtual void __thiscall survarium::animated_model_instance_cook::delete_resource(class vostok::resources::resource_base *)` |
| 99.98 | `private: void __thiscall vostok::network::login_client_impl::sign_in_on_connected(enum vostok::connection_error_types_enum, class boost::function<void __cdecl (enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::login_server_message_types_enum)> const &)` |
| 99.98 | `private: virtual bool __thiscall survarium::player::set_new_active_item(class vostok::resources::resource_ptr<class survarium::inventory_item, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 99.98 | `public: void __thiscall survarium::game_world_ui::on_player_killed(unsigned char, unsigned char, bool, unsigned int)` |
| 99.98 | `protected: virtual void __thiscall survarium::weapon_core_shotgun_reload_start_substate::initialize(void)` |
| 99.98 | `private: void __thiscall survarium::profile_character::weapon_resources_ready(class vostok::resources::queries_result &)` |
| 99.98 | `private: void __thiscall vostok::network::login_client_impl::on_sign_in_handshaked(class boost::function<void __cdecl (enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::login_server_message_types_enum)> const &, enum vostok::handshaking_error_types_enum)` |
| 99.98 | `private: void __thiscall vostok::network::login_client_impl::on_sign_out_handshaked(class boost::function<void __cdecl (enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::login_server_message_types_enum)> const &, enum vostok::handshaking_error_types_enum)` |
| 99.98 | `public: bool __thiscall vostok::animation::animation_player::set_target_and_tick(class vostok::animation::mixing::expression const &, unsigned int, class vostok::math::float4x4const &)` |
| 99.98 | `public: virtual void __thiscall survarium::lobby_menu::clear_resources(void)` |
| 99.98 | `public: void __thiscall survarium::game_world_ui::set_victory_points(signed char, signed char)` |
| 99.98 | `private: virtual struct stlp_std::pair<class vostok::animation::mixing::expression, class vostok::animation::mixing::animation_lexeme> __thiscall survarium::player_logic_crouch_state::selected_animations(class vostok::mutable_buffer &, struct survarium::weapon_animation_parameters const &, bool) const` |
| 99.98 | `public: void __thiscall survarium::game_world_ui::add_victory_points(signed char, signed char)` |
| 99.98 | `public: void __thiscall survarium::game_world_ui::on_victory_item_put_take(unsigned char, bool, bool)` |
| 99.98 | `public: virtual void __thiscall survarium::network_client::tick(unsigned int, bool)` |
| 99.98 | `private: void __thiscall vostok::network::login_client_impl::on_sign_in_answer_received(class boost::function<void __cdecl (enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::login_server_message_types_enum)> const &, class boost::system::error_code const &, unsigned int)` |
| 99.98 | `private: void __thiscall survarium::network_client::on_connected_to_login(enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::login_server_message_types_enum)` |
| 99.98 | `private: void __thiscall vostok::network::login_client_impl::sign_up_on_handshaked(class boost::function<void __cdecl (enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::login_server_message_types_enum, struct vostok::sign_up_info const &)> const &, struct vostok::sign_up_info const &, enum vostok::handshaking_error_types_enum)` |
| 99.98 | `private: void __thiscall vostok::network::login_client_impl::on_user_name_answer_received(class boost::function<void __cdecl (enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::login_server_message_types_enum)> const &, class boost::system::error_code const &, unsigned int)` |
| 99.98 | `public: void __thiscall survarium::game_world_ui::fill_quick_slots(void)` |
| 99.98 | `public: void __thiscall vostok::network::login_client_impl::sign_in(char const *, unsigned short, char const *, char const *, class boost::function<void __cdecl (enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::login_server_message_types_enum)> const &)` |
| 99.99 | `private: virtual void __thiscall survarium::weapon::activate(struct survarium::base_player &, struct survarium::engine &)` |
| 99.99 | `public: void __thiscall vostok::input::receiver::keyboard::execute(void)` |
| 99.99 | `private: void __thiscall survarium::game_world_ui::update_quick_slot(enum survarium::profile_slot_enum)` |
| 99.99 | `private: void __thiscall survarium::network_client::process_sync_response(class vostok::network_core::packet_reader &)` |
| 99.99 | `protected: virtual enum vostok::animation::callback_return_type_enum __thiscall survarium::weapon_core_aimed_fire_state_base::on_shot_event(struct vostok::animation::animation_callback_params &)` |
| 99.99 | `protected: virtual enum vostok::animation::callback_return_type_enum __thiscall survarium::weapon_core_fire_state_base::on_shot_event(struct vostok::animation::animation_callback_params &)` |
| 99.99 | `private: void __thiscall survarium::network_client::on_http_error(class boost::system::error_code)` |
| 99.99 | `private: void __thiscall vostok::input::input_world::destroy_devices(void)` |
| 99.99 | `private: void __thiscall survarium::weapon::set_ui_ammo(bool)` |
| 99.99 | `private: void __thiscall survarium::damage_model_cook::on_hit_params_received(class vostok::resources::queries_result &)` |
| 99.99 | `private: void __thiscall survarium::human_npc::render_model(void)` |
| 99.99 | `private: enum vostok::animation::callback_return_type_enum __thiscall survarium::weapon_core::on_animation_ik_interval(struct vostok::animation::animation_callback_params &)` |
| 99.99 | `public: void __thiscall vostok::input::receiver::keyboard::on_activate(void)` |
| 99.99 | `public: void __thiscall survarium::step_manager::on_step(class survarium::player const &, class vostok::math::float3const &, class vostok::math::float3const &, class survarium::game_world &) const` |
| 99.99 | `public: virtual void __thiscall survarium::player::deserialize(class vostok::network_core::packet_reader &)` |
| 99.99 | `private: void __thiscall survarium::network_client::process_initialize_victory_items(class vostok::network_core::packet_reader &)` |
| 99.99 | `private: void __thiscall vostok::network::login_client_impl::on_sign_up_account_answer_received(class boost::function<void __cdecl (enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::login_server_message_types_enum, struct vostok::sign_up_info const &)> const &, struct vostok::sign_up_info const &, class boost::system::error_code const &, unsigned int)` |
| 99.99 | `public: void __thiscall survarium::weapon_core::get_ammo_info(struct survarium::weapon_ammo_info &)` |
| 99.99 | `public: __thiscall survarium::bullet::bullet(class survarium::bullet_manager &, class vostok::math::float3const &, class vostok::math::float3const &, unsigned int, float, class vostok::resources::resource_ptr<class survarium::weapon_ammunition, class vostok::resources::unmanaged_intrusive_base> const &, class survarium::weapon_core const &, struct survarium::hit_initiator const *const, struct survarium::hit_receiver const *const)` |
| 99.99 | `public: void __thiscall survarium::human_npc::enable(void)` |
| 99.99 | `survarium::calculate_model_size` |
| 99.99 | `public: void __thiscall survarium::inventory::setup_demo_profile(void)` |
| 99.99 | `protected: void __thiscall survarium::base_player::tick_active_object(void)` |
| 99.99 | `private: void __thiscall survarium::weapon::load_weapon(class vostok::resources::resource_ptr<class vostok::render::skeleton_model_instance, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::rifle_scope, class vostok::resources::unmanaged_resource> const &)` |
| 99.99 | `private: void __thiscall survarium::weapon_recoil_calculator::process_compensation(float)` |
| 99.99 | `protected: __thiscall survarium::weapon_core_hide_state::weapon_core_hide_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int, bool &)` |
| 99.99 | `public: void __thiscall survarium::game_world_ui::on_attached_to_player(class vostok::resources::resource_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base>)` |
| 99.99 | `private: virtual void __thiscall survarium::empty_hands::update_bones_matrices(class vostok::resources::resource_ptr<class vostok::animation::skeleton, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float4x4*const, unsigned int, unsigned int, class vostok::math::float4x4&, class vostok::math::float4x4&, class vostok::animation::animation_player const &)` |
| 99.99 | `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::player_logic_crouch_state::movement_lexeme(class vostok::mutable_buffer &, unsigned int, enum vostok::animation::body_part_masks_enum, bool, bool, bool) const` |
| 99.99 | `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::player_logic_stand_state::movement_lexeme(class vostok::mutable_buffer &, unsigned int, enum vostok::animation::body_part_masks_enum, bool, bool, bool) const` |
| 99.99 | `private: void __thiscall survarium::network_client::process_player_action(class vostok::network_core::packet_reader &, unsigned int)` |
| 99.99 | `public: void __thiscall survarium::weapon_recoil_calculator::fire(void)` |
| 99.99 | `public: void __thiscall survarium::inventory::setup_from_profile(struct survarium::player_profile &, class survarium::items_dictionary const &)` |
| 99.99 | `private: void __thiscall vostok::network::login_client_impl::on_sign_in_written(class boost::function<void __cdecl (enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::login_server_message_types_enum)> const &, class boost::system::error_code const &, unsigned int)` |
| 99.99 | `private: void __thiscall vostok::network::login_client_impl::on_sign_up_answer_received(class boost::function<void __cdecl (enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::login_server_message_types_enum, struct vostok::sign_up_info const &)> const &, struct vostok::sign_up_info const &, class boost::system::error_code const &, unsigned int)` |
| 99.99 | `private: virtual struct stlp_std::pair<class vostok::animation::mixing::expression, class vostok::animation::mixing::animation_lexeme> __thiscall survarium::player_logic_sprint_state::selected_animations(class vostok::mutable_buffer &, struct survarium::weapon_animation_parameters const &, bool) const` |
| 99.99 | `public: void __thiscall survarium::game_world_ui::update_minimap_objects(void)` |
| 100.00 | `private: void __thiscall vostok::network::login_client_impl::on_sign_up_written(class boost::function<void __cdecl (enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::login_server_message_types_enum, struct vostok::sign_up_info const &)> const &, struct vostok::sign_up_info const &, class boost::system::error_code const &, unsigned int)` |
| 100.00 | `private: void __thiscall vostok::network::login_client_impl::on_sign_up_info_written(class boost::function<void __cdecl (enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::login_server_message_types_enum, struct vostok::sign_up_info const &)> const &, struct vostok::sign_up_info const &, class boost::system::error_code const &, unsigned int)` |
| 100.00 | `private: void __thiscall vostok::network::login_client_impl::connect(enum vostok::resolve_error_types_enum, class boost::asio::ip::basic_resolver_iterator<class boost::asio::ip::tcp>, unsigned int, class boost::function<void __cdecl (enum vostok::connection_error_types_enum)> const &)` |
| 100.00 | `public: static struct survarium::animation_space_vertex_id __cdecl survarium::animation_space_graph::get_movement(class vostok::animation::animation_player &, struct survarium::animation_space_vertex const *, struct survarium::animation_space_vertex const *, float)` |
| 100.00 | `private: void __thiscall vostok::network::login_client_impl::on_sign_in_password_written(class boost::function<void __cdecl (enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::login_server_message_types_enum)> const &, class boost::system::error_code const &, unsigned int)` |
| 100.00 | `public: virtual void __thiscall survarium::network_client::connect_to_login(char const *, unsigned short, char const *, char const *)` |
| 100.00 | `public: void __thiscall survarium::weapon_recoil_calculator::tick(unsigned int, float)` |
| 100.00 | `private: void __thiscall survarium::network_client::process_victory_item_take_or_put(class vostok::network_core::packet_reader &)` |
| 100.00 | `public: enum vostok::animation::callback_return_type_enum __thiscall survarium::weapon_sound_effect::on_sound_event(struct vostok::animation::animation_callback_params &)` |
| 100.00 | `private: void __thiscall survarium::animated_model_instance_cook::on_subresources_loaded(class vostok::resources::queries_result &)` |
| 100.00 | `public: void __thiscall survarium::player_parameters_modifyer::apply(struct survarium::base_player *)` |
| 100.00 | `public: virtual void __thiscall vostok::render::stage_lights::execute(void)` |
| 100.00 | `public: void __thiscall survarium::lobby_menu::fill_items_dictionary(void)` |
| 100.00 | `private: void __thiscall survarium::project_cooker_simple::create_game_objects(class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class vostok::resources::query_result_for_cook *)` |

### Added (88)

- `private: bool __thiscall survarium::weapon_core::AE_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::aimed_fire_AE_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::aimed_fire_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::aimed_fire_transfer_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::aimed_idle_AE_not_fire_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::aimed_idle_AE_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::aimed_idle_transfer_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::auto_reload_AE_not_fire_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::auto_reload_AE_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::can_reload(void) const`
- `private: bool __thiscall survarium::weapon_core::chamber_a_round_AE_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::chamber_a_round_aimed_AE_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::chamber_a_round_aimed_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::chamber_a_round_aimed_transfer_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::chamber_a_round_on_reload_break_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::chamber_a_round_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::chamber_a_round_transfer_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::fire_AE_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::fire_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::fire_transfer_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::hide_AE_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::hide_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::idle_AE_not_fire_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::idle_AE_or_reload_break_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::idle_transfer_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::inactive_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::is_aiming(void) const`
- `private: bool __thiscall survarium::weapon_core::is_aiming_and_will_not_break(void) const`
- `private: bool __thiscall survarium::weapon_core::is_trying_to_reload(void) const`
- `private: bool __thiscall survarium::weapon_core::not_inactive_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::reload_AE_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::reload_pred(void) const`
- `private: bool __thiscall survarium::weapon_core_shotgun_reload_state::player_wants_to_fire_predicate(void) const`
- `private: bool __thiscall survarium::weapon_user_animations_selector::is_trying_to_jump(void) const`
- `private: bool __thiscall survarium::weapon_user_animations_selector::is_trying_to_sprint(void) const`
- `private: bool __thiscall survarium::weapon_user_animations_selector::is_weapon_allowing_to_jump(void) const`
- `private: bool __thiscall survarium::weapon_user_animations_selector::is_weapon_allowing_to_sprint(void) const`
- `private: bool __thiscall survarium::weapon_user_animations_selector::not_sprint_predicate(void) const`
- `private: bool __thiscall survarium::weapon_user_animations_selector::sprint_predicate(void) const`
- `private: bool __thiscall survarium::weapon_user_animations_selector::stand_from_crouch_predicate(void) const`
- `private: float __thiscall survarium::character_dispersion_calculator::get_skill_coef(enum survarium::weapon_user_state_enum, bool, bool) const`
- `private: virtual void __thiscall survarium::weapon::on_fire_state_end(void)`
- `private: virtual void __thiscall survarium::weapon::on_fire_state_start(void)`
- `private: void __thiscall survarium::weapon::add_weapon_fire_light(void)`
- `private: void __thiscall survarium::weapon::remove_weapon_fire_light(void)`
- `private: void __thiscall survarium::weapon_core::check_for_fire_mode_or_ammunition_or_fire_queue_resetting(void)`
- `private: void __thiscall survarium::weapon_core::check_for_forcing_not_to_aim(void)`
- `private: void __thiscall survarium::weapon_core::check_for_no_ammo_message(void)`
- `private: void __thiscall survarium::weapon_core::check_for_sprint_transition(void)`
- `protected: __thiscall survarium::weapon_core_base_state::weapon_core_base_state(class survarium::weapon_core &, bool, enum survarium::weapon_state_id_enum)`
- `protected: void __thiscall survarium::swf_input_translator::register_char_bind(enum vostok::input::enum_keyboard, int, bool, bool)`
- `protected: void __thiscall survarium::swf_input_translator::register_char_bind(enum vostok::input::enum_keyboard, wchar_t, wchar_t, int, bool, bool)`
- `protected: wchar_t __thiscall survarium::swf_input_translator::translate_key_action(struct vostok::input::world *, bool, bool, struct survarium::dik_to_swf_bind &)`
- `public: __thiscall survarium::character_dispersion_skill_influence::character_dispersion_skill_influence(void)`
- `public: __thiscall survarium::game_scene::~game_scene(void)`
- `public: __thiscall vostok::ai::planning::plan_tracker::~plan_tracker(void)`
- `public: __thiscall vostok::detail::abstract_type_helper::abstract_type_helper(void)`
- `public: __thiscall vostok::intrusive_ptr<class vostok::sound::encoded_sound_interface, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock>::intrusive_ptr<class vostok::sound::encoded_sound_interface, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock>(class vostok::sound::encoded_sound_interface *)`
- `public: __thiscall vostok::render::geometry_batch::~geometry_batch(void)`
- `public: __thiscall vostok::render::requested_streamable_texture::requested_streamable_texture(struct vostok::render::requested_streamable_texture const &)`
- `public: __thiscall vostok::render::speedtree_data::speedtree_data(void)`
- `public: __thiscall vostok::render::streamable_texture_info::streamable_texture_info(struct vostok::render::streamable_texture_info const &)`
- `public: __thiscall vostok::render::streaming_ready_texture::streaming_ready_texture(struct vostok::render::streaming_ready_texture const &)`
- `public: __thiscall vostok::sound::single_sound::single_sound(class vostok::resources::resource_ptr<class vostok::sound::encoded_sound_with_qualities, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::sound::sound_spl, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: bool __thiscall survarium::weapon_core::can_jump(void) const`
- `public: bool __thiscall survarium::weapon_core::can_sprint(void) const`
- `public: bool __thiscall survarium::weapon_core::is_chambering_a_round(void) const`
- `public: bool __thiscall survarium::weapon_core::is_firing(void) const`
- `public: bool __thiscall survarium::weapon_core::is_idle(void) const`
- `public: bool __thiscall survarium::weapon_core::is_reloading(void) const`
- `public: bool __thiscall survarium::weapon_core::ready_to_fire(void) const`
- `public: bool __thiscall survarium::weapon_core::tick_in_cycle_fire(bool) const`
- `public: bool __thiscall survarium::weapon_user_animations_selector::is_crouching(void) const`
- `public: bool __thiscall survarium::weapon_user_animations_selector::is_going_to_jump(void) const`
- `public: bool __thiscall survarium::weapon_user_animations_selector::is_going_to_sprint(void) const`
- `public: struct vostok::render::streaming_ready_texture & __thiscall vostok::render::streaming_ready_texture::operator=(struct vostok::render::streaming_ready_texture const &)`
- `public: virtual __thiscall survarium::animated_model_instance::~animated_model_instance(void)`
- `public: virtual __thiscall survarium::player_logic_sprint_state::~player_logic_sprint_state(void)`
- `public: virtual __thiscall vostok::ai::selectors::enemy_target_selector::~enemy_target_selector(void)`
- `public: virtual __thiscall vostok::console_commands::cc_u32::~cc_u32(void)`
- `public: virtual bool __thiscall vostok::input::receiver::keyboard::caps_lock_state(void) const`
- `public: virtual bool __thiscall vostok::input::receiver::keyboard::get_scan_unicode(int, wchar_t *, unsigned int) const`
- `public: virtual void __thiscall survarium::base_player::on_fire(void)`
- `public: void __thiscall survarium::character_dispersion_calculator::set_character_dispersion_skill_influence(struct survarium::character_dispersion_skill_influence const *)`
- `public: void __thiscall survarium::character_dispersion_skill_influence::load(class vostok::configs::binary_config_value const &)`
- `public: void __thiscall survarium::damage_model::reset(unsigned int)`
- `public: void __thiscall survarium::weapon_user_animations_selector::on_sprint_start(void)`
- `vostok::render::index_to_shadow_size`

### Deleted (56)

- `class vostok::resources::managed_resource * __cdecl vostok::resources::allocate_managed_resource(unsigned int, enum vostok::resources::class_id_enum)`
- `private: bool __thiscall survarium::weapon_core::can_and_must_reload_and_animation_ended_predicate(void) const`
- `private: bool __thiscall survarium::weapon_core::can_and_must_reload_predicate(void) const`
- `private: bool __thiscall survarium::weapon_core::instant_idle_predicate(void) const`
- `private: bool __thiscall survarium::weapon_core::is_not_trying_to_aim_predicate(void) const`
- `private: bool __thiscall survarium::weapon_core::is_trying_to_aim(void) const`
- `private: bool __thiscall survarium::weapon_core::must_chamber_a_round_aimed_and_animation_ended_predicate(void) const`
- `private: bool __thiscall survarium::weapon_core::must_chamber_a_round_aimed_predicate(void) const`
- `private: bool __thiscall survarium::weapon_core::must_chamber_a_round_and_animation_ended_predicate(void) const`
- `private: bool __thiscall survarium::weapon_core::must_chamber_a_round_predicate(void) const`
- `private: bool __thiscall survarium::weapon_core::target_and_animation_ended_predicate(enum survarium::weapon_targets) const`
- `private: bool __thiscall survarium::weapon_core::target_predicate(enum survarium::weapon_targets) const`
- `private: bool __thiscall survarium::weapon_user_animations_selector::is_weapon_firing(void) const`
- `private: bool __thiscall survarium::weapon_user_animations_selector::is_weapon_in_idle(void) const`
- `private: bool __thiscall survarium::weapon_user_animations_selector::is_weapon_toggling(void) const`
- `private: bool __thiscall survarium::weapon_user_animations_selector::stand_predicate(void) const`
- `private: virtual void __thiscall survarium::weapon::set_target(enum survarium::weapon_targets)`
- `private: void __thiscall vostok::sound::sound_rms_cook::on_sub_resources_loaded(class vostok::resources::queries_result &)`
- `protected: __thiscall survarium::weapon_core_base_state::weapon_core_base_state(class survarium::weapon_core &, bool)`
- `protected: __thiscall vostok::resources::pinned_ptr_base<class vostok::sound::sound_rms>::pinned_ptr_base<class vostok::sound::sound_rms>(class vostok::resources::pinned_ptr_base<class vostok::sound::sound_rms> const &)`
- `protected: __thiscall vostok::resources::pinned_ptr_base<class vostok::sound::sound_rms>::pinned_ptr_base<class vostok::sound::sound_rms>(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>)`
- `protected: class vostok::resources::pinned_ptr_mutable<class vostok::sound::sound_rms> __thiscall vostok::resources::cook_base::pin_for_write<class vostok::sound::sound_rms>(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>)`
- `protected: virtual enum vostok::animation::callback_return_type_enum __thiscall survarium::weapon_core_aimed_fire_state_base::on_aiming_event(struct vostok::animation::animation_callback_params &)`
- `protected: void __thiscall survarium::swf_input_translator::register_char_bind(enum vostok::input::enum_keyboard, int, bool)`
- `protected: void __thiscall survarium::swf_input_translator::register_char_bind(enum vostok::input::enum_keyboard, wchar_t, wchar_t, int, bool)`
- `protected: wchar_t __thiscall survarium::swf_input_translator::translate_key_action(struct vostok::input::world *, bool, struct survarium::dik_to_swf_bind &)`
- `public: __thiscall vostok::particle::lod_entry::~lod_entry(void)`
- `public: __thiscall vostok::resources::pinned_ptr_base<class vostok::sound::sound_rms>::~pinned_ptr_base<class vostok::sound::sound_rms>(void)`
- `public: __thiscall vostok::resources::resource_ptr<class vostok::sound::encoded_sound_with_qualities, class vostok::resources::unmanaged_intrusive_base>::resource_ptr<class vostok::sound::encoded_sound_with_qualities, class vostok::resources::unmanaged_intrusive_base>(class vostok::sound::encoded_sound_with_qualities *)`
- `public: __thiscall vostok::sound::single_sound::single_sound(class vostok::resources::resource_ptr<class vostok::sound::encoded_sound_with_qualities, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::sound::sound_spl, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: __thiscall vostok::sound::sound_rms::sound_rms(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, float)`
- `public: __thiscall vostok::sound::sound_rms::~sound_rms(void)`
- `public: __thiscall vostok::sound::sound_rms_cook::sound_rms_cook(void)`
- `public: __thiscall vostok::sound::sound_rms_pinned::sound_rms_pinned(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>)`
- `public: bool __thiscall survarium::weapon_core::could_be_aimed(struct survarium::base_player const &) const`
- `public: bool __thiscall survarium::weapon_core::is_ready_to_shoot(void) const`
- `public: bool __thiscall survarium::weapon_core::ready_to_reload(void) const`
- `public: bool __thiscall survarium::weapon_user_animations_selector::sprint_predicate(void) const`
- `public: class survarium::weapon_user_animations_selector & __thiscall survarium::weapon_core::user_animations_selector(void)`
- `public: enum survarium::weapon_targets __thiscall survarium::weapon_core::get_target(void) const`
- `public: float __thiscall vostok::sound::sound_rms::get_rms_by_time(unsigned __int64) const`
- `public: unsigned __int64 __thiscall vostok::sound::sound_rms::find_min_value_time_in_interval(unsigned __int64, unsigned __int64, float) const`
- `public: virtual __thiscall survarium::rifle_scope::~rifle_scope(void)`
- `public: virtual __thiscall survarium::weapon_core_fire_state_base::~weapon_core_fire_state_base(void)`
- `public: virtual __thiscall vostok::particle::particle_system_instance::~particle_system_instance(void)`
- `public: virtual __thiscall vostok::sound::sound_rms_cook::~sound_rms_cook(void)`
- `public: virtual class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const & __thiscall vostok::sound::composite_sound::get_sound_rms(void) const`
- `public: virtual class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const & __thiscall vostok::sound::single_sound::get_sound_rms(void) const`
- `public: virtual void __thiscall survarium::weapon_core::set_target(enum survarium::weapon_targets)`
- `public: virtual void __thiscall vostok::sound::sound_rms_cook::delete_resource(class vostok::resources::resource_base *)`
- `public: virtual void __thiscall vostok::sound::sound_rms_cook::translate_query(class vostok::resources::query_result_for_cook &)`
- `public: void __thiscall survarium::damage_model::reset(void)`
- `public: void __thiscall survarium::weapon_core::instant_idle_end(void)`
- `public: void __thiscall survarium::weapon_core::instant_toggle_end(void)`
- `public: void __thiscall survarium::weapon_core::instant_toggle_start(void)`
- `void __cdecl vostok::memory::zero<char, 14>(char (&)[14])`

---

## v0.1.1a-build816 → v0.1.1b-build826
_2013-05-14 → 2013-05-14 · +19 / -26 / ~254_

### Changed (254)

| match % | function |
| ---: | --- |
| 0.00 | `long __cdecl vostok::threading::interlocked_increment(long volatile &)` |
| 0.00 | `private: void __thiscall vostok::render::stage_lights::draw_geometry(class vostok::render::light *)` |
| 0.00 | `public: __thiscall survarium::game_scene::~game_scene(void)` |
| 0.00 | `public: __thiscall vostok::ai::brain_unit_cook_params::~brain_unit_cook_params(void)` |
| 0.00 | `public: __thiscall vostok::animation::mixing::animation_interval::~animation_interval(void)` |
| 0.00 | `public: __thiscall vostok::intrusive_list<struct vostok::ai::percept_memory_object, struct vostok::ai::percept_memory_object *, 40, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::~intrusive_list<struct vostok::ai::percept_memory_object, struct vostok::ai::percept_memory_object *, 40, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>(void)` |
| 0.00 | `public: __thiscall vostok::one_way_threads_channel<class vostok::intrusive_spsc_queue<class vostok::network::order, class vostok::network::order, 4>, class vostok::intrusive_spsc_queue<class vostok::network::order, class vostok::network::order, 4> >::~one_way_threads_channel<class vostok::intrusive_spsc_queue<class vostok::network::order, class vostok::network::order, 4>, class vostok::intrusive_spsc_queue<class vostok::network::order, class vostok::network::order, 4> >(void)` |
| 0.00 | `public: __thiscall vostok::render::skeleton_combined_cook_data::~skeleton_combined_cook_data(void)` |
| 0.00 | `public: __thiscall vostok::render::stage_lights::lights_instance::lights_instance(void)` |
| 0.00 | `public: __thiscall vostok::render::sun_cascade::sun_cascade(struct vostok::render::sun_cascade const &)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::render::material, class vostok::resources::unmanaged_intrusive_base>::~resource_ptr<class vostok::render::material, class vostok::resources::unmanaged_intrusive_base>(void)` |
| 0.00 | `public: __thiscall vostok::vfs::vfs_mount::~vfs_mount(void)` |
| 0.00 | `public: virtual __thiscall survarium::inventory_cook::~inventory_cook(void)` |
| 0.00 | `public: virtual __thiscall vostok::console_commands::cc_u32::~cc_u32(void)` |
| 0.00 | `public: virtual __thiscall vostok::render::functor_command::~functor_command(void)` |
| 0.00 | `public: virtual void __thiscall survarium::game_camera::on_focus(bool)` |
| 0.00 | `public: void __thiscall vostok::render::backend::set_ps_constant<unsigned int>(class vostok::render::shader_constant_host const *, unsigned int const &)` |
| 0.00 | `vec_begin` |
| 6.08 | `public: class survarium::victory_items_container_core * __thiscall survarium::simple_game_project::get_items_container(unsigned char)` |
| 9.96 | `private: void __thiscall survarium::game::register_console_commands(void)` |
| 12.00 | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 16.09 | `private: void __thiscall vostok::render::constants_handler<1>::update_buffers(void)` |
| 23.90 | `public: void __thiscall vostok::render::shader_constant_buffer::update(void)` |
| 24.99 | `private: void __thiscall vostok::render::stage_lights::render_particle_lighting(class vostok::render::render_particle_emitter_instance *, class vostok::render::light *, unsigned int)` |
| 28.38 | `public: void __thiscall vostok::render::radiance_volume::inject_camera_occluders(class vostok::render::renderer_context *)` |
| 29.48 | `private: void __thiscall vostok::render::stage_lights::render_model_lighting(struct vostok::render::render_surface_instance *, class vostok::render::light *)` |
| 34.20 | `private: void __thiscall vostok::render::stage_lights::render_speedtree_lighting(struct vostok::render::lod_entry const *, class SpeedTree::CInstance const *, struct SpeedTree::SInstanceLod const *, class vostok::render::speedtree_tree_component *, class vostok::render::light *)` |
| 34.68 | `public: void __thiscall vostok::render::grass_world::set_trample_parameters(struct vostok::render::trample_desc &)` |
| 35.79 | `public: void __thiscall vostok::render::system_renderer::draw_triangles(struct vostok::render::vertex_colored const *const, struct vostok::render::vertex_colored const *const, unsigned short const *const, unsigned short const *const, bool)` |
| 37.90 | `private: bool __thiscall survarium::weapon_core::chamber_a_round_on_reload_break_pred(void) const` |
| 38.32 | `public: void __thiscall vostok::render::radiance_volume::propagate_lighting_iter(unsigned int, unsigned int)` |
| 40.29 | `private: void __thiscall vostok::render::stage_lights::render_light(class vostok::render::light *, bool)` |
| 42.34 | `public: virtual void __thiscall vostok::render::skeleton_render_model_instance::set_constants(void)` |
| 42.73 | `public: virtual void __thiscall vostok::render::stage_ambient_lighting::execute(void)` |
| 45.14 | `public: void __thiscall vostok::render::scene_shader_constants::set(class vostok::render::renderer_context *, class vostok::math::float3const &, class vostok::math::float3const &, class vostok::math::float3const &, class vostok::math::float3const &, float, float, float, class vostok::math::float4const &, struct vostok::render::post_process_parameters const &)` |
| 46.13 | `public: void __thiscall vostok::render::decal_shader_constants_and_geometry::set(class vostok::render::renderer_context *, class vostok::math::float4x4const &, class vostok::math::float4x4const &, float, float, class vostok::math::float3const &, class vostok::math::float4x4const &)` |
| 50.52 | `public: void __thiscall vostok::render::renderer_context::set_v(class vostok::math::float4x4const &)` |
| 50.89 | `public: void __thiscall vostok::render::particle_shader_constants::set_time(float)` |
| 52.50 | `public: void __thiscall vostok::render::renderer_context::set_w(class vostok::math::float4x4const &)` |
| 52.83 | `private: void __thiscall vostok::render::stage_light_propagation_volumes::set_rsm_contants(class vostok::math::float3const &, class vostok::math::float3const &, float)` |
| 52.95 | `private: void __thiscall vostok::render::stage_light_propagation_volumes::pre_lpv_batch_render(class vostok::math::float3const &, float, struct vostok::render::geometry_batch const &)` |
| 53.18 | `private: void __thiscall vostok::render::stage_lights::make_skin_scattering_texture(struct vostok::render::render_surface_instance *, class vostok::render::light *)` |
| 54.07 | `public: void __thiscall vostok::render::dof_shader_constants::set(class vostok::math::float3const &, float, float, float, float, float, float, float)` |
| 54.67 | `public: void __thiscall vostok::render::grass_world::set_shadow_parameters(unsigned int)` |
| 54.76 | `private: bool __thiscall survarium::weapon_core::idle_AE_or_reload_break_pred(void) const` |
| 54.79 | `public: void __thiscall vostok::render::particle_shader_constants::set(class vostok::math::float3, class vostok::math::float3, class vostok::math::float3, enum vostok::particle::enum_particle_locked_axis, enum vostok::particle::enum_particle_screen_alignment)` |
| 54.97 | `public: void __thiscall vostok::render::speedtree_tree_parameters::set(class vostok::render::speedtree_tree_component *, class SpeedTree::CInstance const *, struct SpeedTree::SInstanceLod const *)` |
| 56.58 | `public: virtual void __thiscall vostok::render::stage_atmosphere::execute(void)` |
| 58.30 | `public: void __thiscall vostok::render::speedtree_wind_parameters::set(class SpeedTree::CWind const &)` |
| 58.72 | `public: void __thiscall vostok::render::renderer_context::set_p(class vostok::math::float4x4const &)` |
| 60.67 | `public: void __thiscall vostok::render::grass_world::set_wind_parameters(class vostok::math::float2const &, float)` |
| 60.74 | `public: void __thiscall vostok::render::radiance_volume::inject_lighting(class vostok::math::float3const &, class vostok::math::float3const &, float, unsigned int)` |
| 61.40 | `public: void __thiscall vostok::render::bloom_shader_constants::set(float, float, class vostok::math::float3const &)` |
| 62.14 | `public: void __thiscall vostok::render::speedtree_billboard_parameters::set(class vostok::render::renderer_context *, class vostok::render::speedtree_tree_component *)` |
| 62.23 | `public: void __thiscall vostok::render::grass_world::set_patch_parameters(struct vostok::render::grass_patch *)` |
| 63.25 | `private: void __thiscall vostok::render::stage_lights::render_shadowed_light(class vostok::render::light *)` |
| 63.42 | `public: virtual void __thiscall vostok::render::stage_sun::execute(void)` |
| 63.79 | `public: void __thiscall vostok::render::speedtree_common_parameters::set(class vostok::render::renderer_context *, class vostok::render::speedtree_tree_component *, class vostok::math::float3const &)` |
| 64.79 | `private: void __thiscall vostok::render::stage_light_propagation_volumes::inject_occluders(unsigned int, class vostok::math::float3const &, class vostok::math::float3const &, class vostok::render::vector<class vostok::math::float4x4>)` |
| 65.41 | `public: void __thiscall vostok::render::stage_forward::render_forward_models(class vostok::render::vector<struct vostok::render::render_surface_instance *> &, unsigned int)` |
| 65.65 | `private: void __thiscall vostok::render::stage_gbuffer::render_models(class vostok::render::vector<struct vostok::render::render_surface_instance *> &, unsigned int, unsigned int &, bool)` |
| 67.38 | `public: void __thiscall vostok::render::radiance_volume::inject_occluder_geometry(class vostok::render::renderer_context *, class vostok::math::float3const &, class vostok::math::float3const &, class vostok::render::vector<class vostok::math::float4x4> const &)` |
| 67.63 | `private: void __thiscall vostok::render::stage_lights::render_to_hw_shadowmap(class vostok::render::light *, unsigned int, float, unsigned int, unsigned int, class vostok::math::float4x4const &, class vostok::math::float4x4const &, unsigned int)` |
| 68.51 | `public: void __thiscall vostok::render::radiance_volume::inject_occluders(class vostok::render::renderer_context *, class vostok::math::float3const &, class vostok::math::float3const &, unsigned int)` |
| 70.45 | `public: void __thiscall vostok::render::radiance_volume::propagate_lighting(unsigned int)` |
| 71.01 | `private: void __thiscall vostok::render::stage_light_propagation_volumes::render_to_rms(class vostok::math::float3const &, float, class vostok::math::float4x4const &, class vostok::math::float4x4const &, class vostok::render::vector<class vostok::math::float4x4>, unsigned int)` |
| 72.87 | `public: void __thiscall vostok::render::stage_forward::accumulate_local_reflections(void)` |
| 73.75 | `private: void __thiscall vostok::render::constants_handler<0>::assign(class vostok::render::shader_constant_table const *)` |
| 73.75 | `private: void __thiscall vostok::render::constants_handler<1>::assign(class vostok::render::shader_constant_table const *)` |
| 73.75 | `private: void __thiscall vostok::render::constants_handler<2>::assign(class vostok::render::shader_constant_table const *)` |
| 75.84 | `public: virtual void __thiscall vostok::render::stage_volume_fog::execute(void)` |
| 75.97 | `public: void __thiscall vostok::render::stage_debug::render_environment_probe_preview(void)` |
| 76.85 | `public: virtual void __thiscall vostok::render::stage_translucency::execute(void)` |
| 77.12 | `public: void __thiscall vostok::render::hw_hiz_occlusion_manager::render_debug(class vostok::render::renderer_context *, class vostok::math::float4const *, unsigned char const *, unsigned int)` |
| 77.15 | `public: virtual void __thiscall vostok::render::stage_postprocess::execute(void)` |
| 77.46 | `public: __thiscall vostok::render::backend::~backend(void)` |
| 78.55 | `public: virtual void __thiscall vostok::render::stage_clouds::execute(void)` |
| 78.86 | `public: void __thiscall vostok::render::grass_patch::try_accumulate_trample(struct vostok::render::trample_desc &, struct vostok::render::grass_world *, class vostok::render::renderer *, class vostok::render::renderer_context *)` |
| 79.55 | `private: void __thiscall vostok::render::stage_lights::render_model_probe_lighting(struct vostok::render::render_surface_instance *, struct vostok::render::environment_probe *, float)` |
| 80.43 | `private: bool __thiscall survarium::weapon_core::chamber_a_round_aimed_transfer_pred(void) const` |
| 80.43 | `private: bool __thiscall survarium::weapon_core::chamber_a_round_transfer_pred(void) const` |
| 81.02 | `public: void __thiscall vostok::render::res_render_output::set_size(unsigned int, unsigned int, bool, bool)` |
| 81.40 | `public: void __thiscall vostok::render::render_particle_emitter_instance::render_sprites(void)` |
| 81.49 | `private: bool __thiscall survarium::weapon_core::chamber_a_round_pred(void) const` |
| 81.59 | `public: void __thiscall vostok::render::stage_shadow_direct::render_models(class vostok::render::vector<struct vostok::render::render_surface_instance *> &, class vostok::math::float4x4const &, unsigned int, unsigned int, class vostok::math::float3const &, unsigned int, unsigned int)` |
| 81.84 | `public: virtual void __thiscall vostok::render::stage_gbuffer::execute(void)` |
| 82.64 | `private: void __thiscall vostok::render::speedtree_billboard_parameters::set_billboard_tangents(float)` |
| 82.88 | `private: void __thiscall vostok::render::stage_lights::render_particle_probe_lighting(class vostok::render::render_particle_emitter_instance *, struct vostok::render::environment_probe *, unsigned int)` |
| 83.31 | `private: void __thiscall vostok::render::hw_hiz_occlusion_manager::render_model_bounds(class vostok::render::renderer_context *, class vostok::math::float4const *, unsigned int)` |
| 83.37 | `public: void __thiscall vostok::render::stage_light_propagation_volumes::execute_smoothed_impl(unsigned int, unsigned int, unsigned int, unsigned int, unsigned int)` |
| 83.37 | `public: void __thiscall vostok::render::system_renderer::draw_screen_lines(class vostok::math::float3const *, unsigned int, class vostok::math::color const &, float, unsigned int, bool, bool)` |
| 83.50 | `private: void __thiscall vostok::render::stage_postprocess::compute_per_pixel_eye_adaptated_luminance(void)` |
| 84.11 | `private: void __thiscall vostok::render::stage_light_propagation_volumes::render_to_rms_smoothed2(class vostok::math::float3const &, float, class vostok::math::float4x4const &, class vostok::math::float4x4const &, class vostok::render::vector<class vostok::math::float4x4>, unsigned int, unsigned int, unsigned int)` |
| 84.22 | `public: void __thiscall vostok::render::stage_resolve_lighting::render_models(class vostok::render::vector<struct vostok::render::render_surface_instance *> &, unsigned int &)` |
| 85.31 | `private: void __thiscall survarium::network_client::process_victory_item_take_or_put(class vostok::network_core::packet_reader &)` |
| 86.00 | `public: virtual void __thiscall vostok::render::stage_postprocess::execute_disabled(void)` |
| 86.40 | `private: void __thiscall vostok::render::hw_hiz_occlusion_manager::downsample_occlusion_buffer(void)` |
| 86.45 | `private: class vostok::math::float4x4 __thiscall vostok::render::stage_pre_rain::render_rain_shadow_map(void)` |
| 86.63 | `private: void __thiscall vostok::render::stage_postprocess::accumulate_motion_vectors(void)` |
| 87.18 | `private: void __thiscall vostok::render::stage_postprocess::advanced_bloom(void)` |
| 87.19 | `public: virtual void __thiscall survarium::respawn_point_core::load(class vostok::configs::binary_config_value const &)` |
| 87.66 | `public: __thiscall vostok::render::render_cc_bool::render_cc_bool(char const *, enum vostok::render::enum_options_changes_result, char const *, bool &, bool &, bool, enum vostok::console_commands::command_type)` |
| 87.75 | `protected: __thiscall vostok::render::shader_constant_buffer::shader_constant_buffer(class vostok::fixed_string<64> const &, enum vostok::render::enum_shader_type, enum _D3D_CBUFFER_TYPE, unsigned int)` |
| 88.19 | `public: virtual void __thiscall vostok::render::stage_rain::execute(void)` |
| 89.67 | `private: bool __thiscall survarium::weapon_core::is_aiming(void) const` |
| 89.74 | `public: void __thiscall vostok::render::stage_light_propagation_volumes::execute_impl(void)` |
| 91.14 | `private: void __thiscall vostok::render::stage_postprocess::process_blur(class vostok::render::render_target *, class vostok::render::res_texture *, class vostok::render::render_target *, class vostok::render::res_texture *, unsigned int)` |
| 91.44 | `public: void __thiscall vostok::render::render_particle_emitter_instance::render_subuv_sprites(void)` |
| 91.98 | `public: __thiscall vostok::render::backend::backend(void)` |
| 92.65 | `public: void __thiscall vostok::render::render_output_window::set_size(unsigned int, unsigned int, bool, bool)` |
| 92.76 | `bool __cdecl vostok::render::set_client_rect(struct HWND__*, int, int, int, int)` |
| 92.82 | `private: void __thiscall survarium::network_client::process_initialize_victory_items(class vostok::network_core::packet_reader &)` |
| 93.01 | `public: virtual void __thiscall vostok::render::stage_ambient_occlusion::execute(void)` |
| 93.10 | `private: void __thiscall vostok::render::options::load_impl(class vostok::memory::reader &)` |
| 93.20 | `public: void __thiscall vostok::render::options::set_default_values(void)` |
| 93.63 | `public: virtual void __thiscall vostok::render::effect_god_rays::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 93.70 | `private: bool __thiscall survarium::weapon_core::can_reload(void) const` |
| 94.46 | `public: void __thiscall vostok::render::options::register_console_commands(void)` |
| 94.49 | `public: virtual void __thiscall vostok::render::stage_pre_rain::execute(void)` |
| 94.54 | `private: void __thiscall vostok::render::decal_instance::render(class vostok::render::renderer_context *, enum vostok::render::enum_render_stage_type)` |
| 95.31 | `private: void __thiscall vostok::render::stage_light_propagation_volumes::downsample_rsm(class vostok::math::float3const &, class vostok::math::float3const &, float, unsigned int)` |
| 96.14 | `public: virtual bool __thiscall survarium::free_fly_camera::on_keyboard_action(struct vostok::input::world *, enum vostok::input::enum_keyboard, enum vostok::input::enum_keyboard_action)` |
| 96.58 | `private: virtual bool __thiscall survarium::player_input_handler::on_keyboard_action(struct vostok::input::world *, enum vostok::input::enum_keyboard, enum vostok::input::enum_keyboard_action)` |
| 97.56 | `public: virtual void __thiscall vostok::render::stage_resolve_lighting::execute(void)` |
| 97.61 | `public: void __thiscall vostok::render::grass_world::accumulate_trample(class vostok::render::renderer *, class vostok::render::renderer_context *)` |
| 98.49 | `private: void __thiscall vostok::render::shader_macros::register_available_macros(void)` |
| 98.88 | `private: void __thiscall survarium::game::on_configs_loaded(class vostok::resources::queries_result &)` |
| 98.92 | `private: bool __thiscall vostok::console_impl::on_text_commit(struct vostok::ui::window *, int, int)` |
| 99.33 | `public: void __thiscall vostok::render::backend::reset_depth_stencil_target(void)` |
| 99.50 | `public: void __thiscall vostok::render::backend::set_vb(class vostok::render::untyped_buffer *, unsigned int, unsigned int)` |
| 99.50 | `public: void __thiscall vostok::render::backend::set_vb_stream_1(class vostok::render::untyped_buffer *, unsigned int, unsigned int)` |
| 99.50 | `public: void __thiscall vostok::render::res_state::apply(void) const` |
| 99.54 | `private: void __thiscall survarium::player_input_handler::process_first_person_mode(bool)` |
| 99.56 | `public: void __thiscall vostok::render::res_geometry::apply(void)` |
| 99.57 | `private: void __thiscall vostok::render::backend::flush_rt(void)` |
| 99.57 | `public: virtual void __thiscall vostok::render::stage_debug::execute(void)` |
| 99.58 | `public: void __thiscall vostok::render::backend::reset(void)` |
| 99.62 | `public: void __thiscall vostok::render::grass_patch::remove_trample(void)` |
| 99.64 | `public: void __thiscall vostok::render::hw_hiz_point_list::render(unsigned int)` |
| 99.66 | `public: void __thiscall vostok::render::injection_geometry::draw(void)` |
| 99.67 | `public: void __thiscall vostok::render::backend::set_render_target(enum vostok::render::enum_render_target_enum, class vostok::render::render_target const *)` |
| 99.68 | `public: void __thiscall vostok::render::radiance_volume::prepare_gv(void)` |
| 99.69 | `public: void __thiscall vostok::render::res_xs<struct vostok::render::vs_data>::apply(void) const` |
| 99.69 | `public: void __thiscall vostok::render::backend::set_render_targets(class vostok::render::render_target const *, class vostok::render::render_target const *, class vostok::render::render_target const *, class vostok::render::render_target const *)` |
| 99.70 | `public: void __thiscall vostok::render::backend::on_device_destroy(void)` |
| 99.70 | `public: void __thiscall vostok::render::backend::reset_render_targets(bool)` |
| 99.71 | `public: void __thiscall vostok::render::box_geometry::draw(void)` |
| 99.71 | `public: void __thiscall vostok::render::sky_dome_geometry::draw(void)` |
| 99.71 | `public: void __thiscall vostok::render::sphere_geometry::draw(void)` |
| 99.72 | `public: void __thiscall vostok::render::res_xs<struct vostok::render::ps_data>::apply(void) const` |
| 99.72 | `public: void __thiscall vostok::render::sliced_cube_geometry::draw(void)` |
| 99.72 | `public: virtual void __thiscall vostok::render::stage_lights::execute(void)` |
| 99.72 | `private: void __thiscall vostok::render::stage_postprocess::clear_surface(class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>)` |
| 99.73 | `private: void __thiscall vostok::render::backend::update_input_layout(void)` |
| 99.74 | `public: virtual void __thiscall vostok::render::stage_forward::execute(void)` |
| 99.75 | `public: void __thiscall vostok::render::res_xs<struct vostok::render::gs_data>::apply(void) const` |
| 99.76 | `private: virtual void __thiscall vostok::render::stage_light_propagation_volumes::execute_disabled(void)` |
| 99.78 | `public: void __thiscall vostok::render::backend::set_ps_texture(char const *, class vostok::render::res_texture *)` |
| 99.78 | `public: void __thiscall vostok::render::backend::flush(void)` |
| 99.79 | `public: virtual void __thiscall vostok::render::stage_decals_accumulate::execute_disabled(void)` |
| 99.80 | `public: virtual void __thiscall vostok::render::stage_shadow_direct::execute_disabled(void)` |
| 99.81 | `public: void __thiscall vostok::render::backend::set_render_output(class vostok::render::res_render_output const *)` |
| 99.81 | `private: void __thiscall vostok::render::radiance_volume::end_render_to_cells(void)` |
| 99.82 | `public: virtual void __thiscall vostok::render::stage_ambient_occlusion::execute_disabled(void)` |
| 99.84 | `public: void __thiscall vostok::render::backend::render(enum D3D_PRIMITIVE_TOPOLOGY, unsigned int, unsigned int)` |
| 99.84 | `public: virtual void __thiscall vostok::render::stage_lights::execute_disabled(void)` |
| 99.85 | `public: virtual void __thiscall vostok::render::stage_pre_lighting::execute(void)` |
| 99.85 | `public: void __thiscall vostok::render::stage_forward::render_opaque_models(void)` |
| 99.86 | `private: void __thiscall vostok::render::hw_hiz_occlusion_manager::render_occluders(class vostok::render::renderer_context *)` |
| 99.86 | `public: virtual void __thiscall vostok::render::stage_shadow_direct::execute(void)` |
| 99.87 | `public: void __thiscall vostok::render::engine::world::begin_render_options_changing(long volatile *)` |
| 99.87 | `public: void __thiscall vostok::render::statistics::start(void)` |
| 99.88 | `private: void __thiscall vostok::render::stage_lights::fill_surface(class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>)` |
| 99.88 | `public: void __thiscall vostok::render::fog_box_geometry::render(void)` |
| 99.88 | `public: void __thiscall vostok::render::sphere_occluder_geometry::render(void)` |
| 99.88 | `private: void __thiscall vostok::render::decal_instance::render_geometry(void)` |
| 99.88 | `private: void __thiscall vostok::render::stage_postprocess::fill_surface(class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>)` |
| 99.88 | `public: void __thiscall vostok::render::scene::flush(class boost::function<void __cdecl (bool)> const &, bool, bool)` |
| 99.89 | `public: void __thiscall vostok::render::backend::render_indexed(enum D3D_PRIMITIVE_TOPOLOGY, unsigned int, unsigned int, unsigned int)` |
| 99.89 | `public: void __thiscall vostok::render::stage_atmosphere::fill_surfaces(class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, bool)` |
| 99.89 | `vostok::render::fill_surface` |
| 99.89 | `public: bool __thiscall vostok::render::ambient_volume::is_occluded(void) const` |
| 99.89 | `public: bool __thiscall vostok::render::decal_instance::is_occluded(void) const` |
| 99.89 | `public: bool __thiscall vostok::render::environment_probe::is_occluded(void) const` |
| 99.89 | `public: bool __thiscall vostok::render::grass_patch::is_occluded(void) const` |
| 99.89 | `public: bool __thiscall vostok::render::light::is_occluded(void) const` |
| 99.89 | `public: bool __thiscall vostok::render::render_surface_instance::is_occluded(void) const` |
| 99.89 | `public: virtual bool __thiscall vostok::render::render_particle_emitter_instance::is_occluded(void) const` |
| 99.89 | `public: enum vostok::render::enum_options_changes_result __thiscall vostok::render::options::end_render_options_changing(class vostok::render::vector<class vostok::fs_new::virtual_path_string> &)` |
| 99.89 | `public: void __thiscall vostok::render::renderer::draw_debug(class vostok::render::scene *, class vostok::render::scene_view *, float, struct vostok::ui::font const *)` |
| 99.90 | `vostok::render::is_occluded_predicate<vostok::render::ambient_volume>` |
| 99.90 | `vostok::render::is_occluded_predicate<vostok::render::decal_instance>` |
| 99.90 | `vostok::render::is_occluded_predicate<vostok::render::environment_probe>` |
| 99.90 | `vostok::render::is_occluded_predicate<vostok::render::grass_patch>` |
| 99.90 | `vostok::render::is_occluded_predicate<vostok::render::render_surface_instance>` |
| 99.91 | `public: __thiscall vostok::render::render_output_window::render_output_window(struct vostok::render::output_window_configuration const &)` |
| 99.91 | `public: void __thiscall vostok::render::stage_screen_image::execute(class vostok::intrusive_ptr<class vostok::render::res_texture, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>)` |
| 99.91 | `private: void __thiscall vostok::render::stage_postprocess::fill_surface2(class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>)` |
| 99.91 | `vostok::render::is_occluded_predicate_light` |
| 99.92 | `public: void __thiscall vostok::render::radiance_volume::prepare_final(void)` |
| 99.93 | `private: void __thiscall vostok::render::radiance_volume::begin_render_to_cells(void)` |
| 99.93 | `public: void __thiscall vostok::render::renderer::setup_render_output_window(class vostok::resources::resource_ptr<struct vostok::render::base_output_window, class vostok::resources::unmanaged_intrusive_base>, class vostok::math::rectangle<class vostok::math::float2> const &)` |
| 99.93 | `public: void __thiscall vostok::render::batched_geometry<struct vostok::render::lpv_vertex>::for_each_batch_render(class vostok::render::renderer_context *, class boost::function<void __cdecl (struct vostok::render::geometry_batch const &)> const &, class boost::function<void __cdecl (struct vostok::render::geometry_batch const &)> const &)` |
| 99.93 | `public: __thiscall singletons_on_preinitialize::singletons_on_preinitialize(class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &, bool)` |
| 99.94 | `public: virtual void __thiscall vostok::render::stage_particles::execute(void)` |
| 99.94 | `public: void __thiscall vostok::render::renderer::render(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct vostok::render::base_scene_view, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct vostok::render::base_output_window, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::rectangle<class vostok::math::float2> const &, class boost::function<void __cdecl (bool)> const &, bool, struct vostok::ui::font const *)` |
| 99.94 | `public: void __thiscall vostok::render::backend::clear_depth_stencil(unsigned int, float, unsigned char)` |
| 99.94 | `vostok::render::is_not_occluded_predicate<vostok::render::ambient_volume>` |
| 99.94 | `vostok::render::is_not_occluded_predicate<vostok::render::decal_instance>` |
| 99.94 | `vostok::render::is_not_occluded_predicate<vostok::render::environment_probe>` |
| 99.94 | `vostok::render::is_not_occluded_predicate<vostok::render::grass_patch>` |
| 99.94 | `vostok::render::is_not_occluded_predicate<vostok::render::render_surface_instance>` |
| 99.95 | `vostok::render::is_not_occluded_predicate_light` |
| 99.95 | `public: virtual void __thiscall vostok::render::stage_accumulate_distortion::execute(void)` |
| 99.95 | `public: void __thiscall vostok::render::system_renderer::draw_ui_vertices(struct vostok::render::vertex_formats::TL const *, unsigned int const &, int, int)` |
| 99.95 | `private: void __thiscall vostok::render::renderer_context_targets::create_targets(class vostok::math::uint2, bool)` |
| 99.95 | `public: class vostok::render::shader_constant_host * __thiscall vostok::render::backend::register_constant_host(class vostok::shared_string const &, enum vostok::render::enum_constant_type)` |
| 99.95 | `public: void __thiscall vostok::render::hw_hiz_occlusion_manager::process_culling(class vostok::render::renderer_context *, class vostok::math::float4const *, unsigned int)` |
| 99.96 | `private: void __thiscall vostok::render::stage_visibility::gather_statistics(void) const` |
| 99.96 | `private: void __thiscall vostok::render::stage_light_propagation_volumes::render_quad(void)` |
| 99.96 | `public: void __thiscall vostok::render::system_renderer::fill_surface(class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, bool, struct D3D11_VIEWPORT *, float, float, float, float)` |
| 99.96 | `public: virtual void __thiscall vostok::render::stage_lights::debug_render(void)` |
| 99.96 | `public: bool __thiscall vostok::render::remove_model_if_not_lod_predicate::operator()(struct vostok::render::render_surface_instance *)` |
| 99.97 | `private: void __thiscall vostok::render::stage_postprocess::measure_per_pixel_luminance(class vostok::render::res_texture *, class vostok::math::float4&)` |
| 99.97 | `public: virtual void __thiscall vostok::render::stage_apply_distortion::execute(void)` |
| 99.97 | `public: void __thiscall vostok::render::backend::clear_render_targets(float, float, float, float)` |
| 99.97 | `public: void __thiscall vostok::render::grass_world::render(class vostok::render::renderer_context *, class vostok::math::float3const &, enum vostok::render::enum_render_stage_type, unsigned int, float, bool, class vostok::render::res_effect *, bool, unsigned int)` |
| 99.97 | `private: void __thiscall vostok::render::renderer::draw_frame_histogram(void) const` |
| 99.98 | `public: void __thiscall vostok::render::backend::clear_render_targets(class vostok::math::color, class vostok::math::color, class vostok::math::color, class vostok::math::color)` |
| 99.98 | `public: void __thiscall vostok::render::engine::world::initialize(bool)` |
| 99.98 | `private: void __thiscall vostok::render::renderer::execute_stages(void)` |
| 99.98 | `public: virtual void __thiscall vostok::render::stage_decals_accumulate::execute(void)` |
| 99.98 | `public: void __thiscall vostok::render::grass_patch::render(struct vostok::render::grass_world *, class vostok::render::renderer_context *, class vostok::math::float3const &, enum vostok::render::enum_render_stage_type, unsigned int, float, class vostok::render::res_effect *, unsigned int)` |
| 99.98 | `public: void __thiscall vostok::render::backend::flush_rt_shader_resources(void)` |
| 99.98 | `public: void __thiscall vostok::render::backend::clear_render_targets(class vostok::math::color)` |
| 99.99 | `public: bool __thiscall vostok::render::remove_inappropriate_models::operator()(struct vostok::render::render_surface_instance *)` |
| 99.99 | `vostok::render::get_format_block_size` |
| 99.99 | `void __cdecl vostok::console_commands::show_help(char const *)` |
| 99.99 | `public: void __thiscall vostok::render::render_particle_emitter_instance::render_trails(class vostok::math::float3const &, struct vostok::particle::base_particle *, unsigned int)` |
| 99.99 | `public: void __thiscall vostok::render::system_renderer::draw_3D_point(class vostok::math::float3const &, float, class vostok::math::color const &, bool)` |
| 99.99 | `public: class vostok::render::effect_compiler & __thiscall vostok::render::effect_compiler::set_texture(char const *, char const *, class vostok::intrusive_ptr<class vostok::render::res_texture, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy> *, bool, unsigned int)` |
| 99.99 | `public: void __thiscall vostok::render::radiance_volume::prepare(class vostok::math::float3const &, class vostok::math::float3const &, float)` |
| 99.99 | `public: __thiscall vostok::render::grass_patch::grass_patch(struct vostok::collision::space_partitioning_tree *const, struct vostok::render::grass_template *, class vostok::math::float3const &, float)` |
| 99.99 | `public: void __thiscall vostok::render::scene::select_models(class vostok::math::float4x4const &, class vostok::render::vector<struct vostok::render::render_surface_instance *> &, class vostok::math::float3const &, unsigned int, bool)` |
| 99.99 | `public: void __thiscall vostok::render::stage_shadow_direct::execute_cascade(unsigned int, unsigned int, unsigned int)` |
| 99.99 | `public: void __thiscall vostok::render::cloud_simulation::generate(struct vostok::render::cloud_key_parameters const &, class vostok::math::float3const &)` |
| 100.00 | `public: __thiscall vostok::render::system_renderer::system_renderer(class vostok::render::renderer_context *)` |
| 100.00 | `public: virtual void __thiscall vostok::render::stage_visibility::execute(void)` |
| 100.00 | `public: __thiscall vostok::render::stage_atmosphere::stage_atmosphere(class vostok::render::renderer *, class vostok::render::renderer_context *, enum vostok::render::stage_atmosphere::stage_type)` |
| 100.00 | `public: __thiscall vostok::render::stage_volume_fog::stage_volume_fog(class vostok::render::renderer *, class vostok::render::renderer_context *)` |
| 100.00 | `public: void __thiscall vostok::render::renderer::fill_opaque_models(void)` |

### Added (19)

- `bool __cdecl vostok::console_commands::execute_console_commands(class vostok::fs_new::native_path_string, enum vostok::console_commands::execution_filter, bool)`
- `private: bool __thiscall survarium::weapon_core::idle_AE_or_chamber_a_round_break_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::reload_break_pred(void) const`
- `public: __thiscall vostok::particle::lod_entry::~lod_entry(void)`
- `public: __thiscall vostok::vectora<struct vostok::resources::request>::~vectora<struct vostok::resources::request>(void)`
- `public: virtual __thiscall vostok::ai::selectors::sound_target_selector::~sound_target_selector(void)`
- `public: virtual __thiscall vostok::particle::particle_system_instance::~particle_system_instance(void)`
- `public: virtual __thiscall vostok::render::stage_postprocess::~stage_postprocess(void)`
- `public: virtual __thiscall vostok::resources::fs_task_unmount::~fs_task_unmount(void)`
- `public: void __thiscall survarium::game::load_cc_script(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>, bool, bool)`
- `public: void __thiscall survarium::game::load_config_query(char const *, bool, bool)`
- `public: void __thiscall survarium::game::on_config_loaded(class vostok::resources::queries_result &, bool, bool)`
- `public: void __thiscall vostok::render::backend::set_gs_constant<float>(class vostok::render::shader_constant_host const *, float const &)`
- `public: void __thiscall vostok::render::backend::set_ps_constant<class vostok::math::float4>(class vostok::render::shader_constant_host const *, class vostok::math::float4const *, unsigned int)`
- `public: void __thiscall vostok::render::backend::set_vs_constant<float>(class vostok::render::shader_constant_host const *, float const &)`
- `public: void __thiscall vostok::render::shader_constant_buffer::set_typed<class vostok::math::float4>(class vostok::render::shader_constant_slot const &, class vostok::math::float4const *, unsigned int)`
- `public: void __thiscall vostok::render::shader_constant_buffer::set_typed<int>(class vostok::render::shader_constant_slot const &, int const &)`
- `void __cdecl vostok::console_commands::execute(char const *, enum vostok::console_commands::execution_filter, bool)`
- `void __cdecl vostok::console_commands::load(class vostok::memory::reader &, enum vostok::console_commands::execution_filter, bool)`

### Deleted (26)

- `bool __cdecl vostok::console_commands::execute_console_commands(class vostok::fs_new::native_path_string, enum vostok::console_commands::execution_filter)`
- `private: void __thiscall survarium::game::load_cmd(char const *)`
- `private: void __thiscall survarium::game::unload_cmd(char const *)`
- `private: void __thiscall vostok::render::constants_handler<0>::set_constant<class vostok::math::float3>(class vostok::render::shader_constant_host const &, class vostok::math::float3const &)`
- `private: void __thiscall vostok::render::constants_handler<0>::set_constant_array<class vostok::math::float4>(class vostok::render::shader_constant_host const &, class vostok::math::float4const *, unsigned int)`
- `private: void __thiscall vostok::render::constants_handler<1>::set_constant<int>(class vostok::render::shader_constant_host const &, int const &)`
- `private: void __thiscall vostok::render::constants_handler<1>::set_constant_array<class vostok::math::float4>(class vostok::render::shader_constant_host const &, class vostok::math::float4const *, unsigned int)`
- `private: void __thiscall vostok::render::constants_handler<2>::set_constant<class vostok::math::float3>(class vostok::render::shader_constant_host const &, class vostok::math::float3const &)`
- `private: void __thiscall vostok::render::shader_constant_buffer::set_memory(unsigned int, char const *, unsigned int)`
- `public: __thiscall vostok::detail::abstract_type_helper::abstract_type_helper(void)`
- `public: __thiscall vostok::render::geometry_batch::~geometry_batch(void)`
- `public: __thiscall vostok::render::render_target_instance::render_target_instance(void)`
- `public: __thiscall vostok::render::requested_streamable_texture::requested_streamable_texture(struct vostok::render::requested_streamable_texture const &)`
- `public: __thiscall vostok::render::speedtree_data::speedtree_data(void)`
- `public: __thiscall vostok::render::streamable_texture_info::streamable_texture_info(struct vostok::render::streamable_texture_info const &)`
- `public: __thiscall vostok::render::streaming_ready_texture::streaming_ready_texture(struct vostok::render::streaming_ready_texture const &)`
- `public: __thiscall vostok::threading::mutex::~mutex(void)`
- `public: struct vostok::render::streaming_ready_texture & __thiscall vostok::render::streaming_ready_texture::operator=(struct vostok::render::streaming_ready_texture const &)`
- `public: virtual __thiscall survarium::animated_model_instance::~animated_model_instance(void)`
- `public: virtual __thiscall survarium::player_logic_sprint_state::~player_logic_sprint_state(void)`
- `public: void __thiscall survarium::game::load_cc_script(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>, bool)`
- `public: void __thiscall survarium::game::load_config_query(char const *, bool)`
- `public: void __thiscall survarium::game::on_config_loaded(class vostok::resources::queries_result &, bool)`
- `public: void __thiscall vostok::render::backend::set_vs_constant<class vostok::math::float4>(class vostok::render::shader_constant_host const *, class vostok::math::float4const &)`
- `void __cdecl vostok::console_commands::execute(char const *, enum vostok::console_commands::execution_filter)`
- `void __cdecl vostok::console_commands::load(class vostok::memory::reader &, enum vostok::console_commands::execution_filter)`

---

## v0.1.1b-build826 → v0.1.1c-build870
_2013-05-14 → 2013-05-24 · +142 / -160 / ~1465_

### Changed (1465)

| match % | function |
| ---: | --- |
| 0.00 | `long __cdecl vostok::threading::interlocked_increment(long volatile &)` |
| 0.00 | `private: virtual class vostok::mutable_buffer __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_reload_state> >::allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)` |
| 0.00 | `private: virtual class vostok::mutable_buffer __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_fire_state> >::allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)` |
| 0.00 | `private: virtual void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_reload_state> >::destroy_resource(class vostok::resources::unmanaged_resource *)` |
| 0.00 | `private: virtual void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_fire_state> >::destroy_resource(class vostok::resources::unmanaged_resource *)` |
| 0.00 | `private: void __thiscall vostok::sound::sound_scene::init_allocators(class vostok::resources::query_result_for_cook &)` |
| 0.00 | `private: void __thiscall vostok::sound::sound_scene::notify_receivers(void)` |
| 0.00 | `private: void __thiscall vostok::sound::sound_scene::on_unmanaged_resources_allocated(class vostok::resources::queries_result &)` |
| 0.00 | `private: void __thiscall vostok::sound::sound_scene::update_receivers_position(void)` |
| 0.00 | `private: void __thiscall vostok::sound::sound_spl_cook::on_config_loaded(class vostok::resources::queries_result &, class vostok::resources::query_result_for_cook *)` |
| 0.00 | `private: void __thiscall vostok::sound::sound_voice::on_buffer_end_impl(void *)` |
| 0.00 | `protected: virtual bool __thiscall btCollisionObject::checkCollideWithOverride(class btCollisionObject *)` |
| 0.00 | `public: __thiscall survarium::vector<class vostok::variant<32> const *>::~vector<class vostok::variant<32> const *>(void)` |
| 0.00 | `public: __thiscall vostok::animation::mixing::animation_interval::~animation_interval(void)` |
| 0.00 | `public: __thiscall vostok::buffer_vector<unsigned int>::~buffer_vector<unsigned int>(void)` |
| 0.00 | `public: __thiscall vostok::intrusive_list<struct vostok::ai::percept_memory_object, struct vostok::ai::percept_memory_object *, 40, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::~intrusive_list<struct vostok::ai::percept_memory_object, struct vostok::ai::percept_memory_object *, 40, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>(void)` |
| 0.00 | `public: __thiscall vostok::math::float3::float3(void)` |
| 0.00 | `public: __thiscall vostok::render::box_geometry::~box_geometry(void)` |
| 0.00 | `public: __thiscall vostok::render::sun_cascade::sun_cascade(struct vostok::render::sun_cascade const &)` |
| 0.00 | `public: __thiscall vostok::resources::pinned_ptr_const<class vostok::animation::cubic_spline_skeleton_animation>::~pinned_ptr_const<class vostok::animation::cubic_spline_skeleton_animation>(void)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class survarium::inventory_item, class vostok::resources::unmanaged_intrusive_base>::resource_ptr<class survarium::inventory_item, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::resource_ptr<class survarium::inventory_item, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::render::material, class vostok::resources::unmanaged_intrusive_base>::~resource_ptr<class vostok::render::material, class vostok::resources::unmanaged_intrusive_base>(void)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>(class vostok::resources::managed_resource *)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::unmanaged_resource *)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>::~resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>(void)` |
| 0.00 | `public: __thiscall vostok::size_policy::size_policy(void)` |
| 0.00 | `public: __thiscall vostok::sound::new_sound_propagator::~new_sound_propagator(void)` |
| 0.00 | `public: __thiscall vostok::sound::receiver_collision::receiver_collision(class vostok::sound::sound_receiver *, class vostok::sound::atomic_half3*)` |
| 0.00 | `public: __thiscall vostok::sound::receiver_collision::~receiver_collision(void)` |
| 0.00 | `public: __thiscall vostok::sound::sound_scene::sound_scene(class vostok::sound::sound_world &, struct vostok::sound::sound_scene_creation_params const &, struct IXAudio2SubmixVoice *, unsigned int, class vostok::resources::query_result_for_cook &)` |
| 0.00 | `public: bool __thiscall vostok::sound::sound_scene::graph_exist(void) const` |
| 0.00 | `public: bool __thiscall vostok::sound::sound_scene::is_segment_pass_portal(unsigned int, class vostok::math::float3, class vostok::math::float3) const` |
| 0.00 | `public: char const * __thiscall vostok::buffer_string::end(void) const` |
| 0.00 | `public: char const * __thiscall vostok::fs_new::path_string_impl::c_str(void) const` |
| 0.00 | `public: class vostok::buffer_string const & __thiscall vostok::buffer_string::operator=(class vostok::buffer_string const &)` |
| 0.00 | `public: class vostok::math::float3 __thiscall vostok::sound::sound_scene::get_portal_center(unsigned int) const` |
| 0.00 | `public: class vostok::math::float3 __thiscall vostok::sound::sound_scene::get_portal_nearest_point(unsigned int, class vostok::math::float3, class vostok::math::float3) const` |
| 0.00 | `public: class vostok::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base> & __thiscall vostok::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base>::operator=(class vostok::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 0.00 | `public: class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> & __thiscall vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>::operator=(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &)` |
| 0.00 | `public: class vostok::sound::atomic_half3* __thiscall vostok::sound::sound_scene::create_receiver_position(void)` |
| 0.00 | `public: class vostok::variant<32> & __thiscall vostok::buffer_vector<class vostok::variant<32> >::operator[](unsigned int)` |
| 0.00 | `public: struct IXAudio2SubmixVoice * __thiscall vostok::sound::sound_world::create_submix_voice(unsigned char, unsigned char) const` |
| 0.00 | `public: struct vostok::sound::sound_scene_statistic * __thiscall vostok::sound::sound_scene::create_statistic(void) const` |
| 0.00 | `public: virtual __thiscall survarium::inventory_cook::~inventory_cook(void)` |
| 0.00 | `public: virtual __thiscall survarium::victory_items_container_core::~victory_items_container_core(void)` |
| 0.00 | `public: virtual void __thiscall survarium::game_camera::on_focus(bool)` |
| 0.00 | `public: virtual void __thiscall vostok::sound::ogg_encoded_sound_interface_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 0.00 | `public: void __thiscall survarium::game_world_ui::on_unload(void)` |
| 0.00 | `public: void __thiscall vostok::render::engine::world::build_lpv_geometry(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 0.00 | `public: void __thiscall vostok::render::grass_world::accumulate_trample(class vostok::render::renderer *, class vostok::render::renderer_context *)` |
| 0.00 | `public: void __thiscall vostok::render::stage_shadow_direct::execute_cascade(unsigned int, unsigned int, unsigned int)` |
| 0.00 | `public: void __thiscall vostok::sound::proxy_statistic::fill_text_tree(class vostok::strings::text_tree_item *, bool) const` |
| 0.00 | `public: void __thiscall vostok::sound::receiver_collision::delete_position(class vostok::sound::sound_scene &)` |
| 0.00 | `public: void __thiscall vostok::sound::sound_scene::clear_resources(void)` |
| 0.00 | `public: void __thiscall vostok::sound::sound_scene::delete_receiver_position(class vostok::sound::atomic_half3*)` |
| 0.00 | `public: void __thiscall vostok::sound::sound_scene::delete_statistic(struct vostok::sound::sound_scene_statistic *) const` |
| 0.00 | `public: void __thiscall vostok::sound::sound_scene::fade_in(class vostok::sound::sound_world &, unsigned int)` |
| 0.00 | `public: void __thiscall vostok::sound::sound_scene::fade_out(unsigned int)` |
| 0.00 | `public: void __thiscall vostok::sound::sound_scene::find_path(class vostok::math::float3const &, class vostok::vectora<class vostok::fixed_vector<unsigned int, 32> > &) const` |
| 0.00 | `public: void __thiscall vostok::sound::sound_scene::free_sound_instance_proxy(class vostok::sound::sound_instance_proxy *)` |
| 0.00 | `public: void __thiscall vostok::sound::sound_scene::register_receiver(class vostok::sound::sound_receiver *, class vostok::sound::atomic_half3*)` |
| 0.00 | `public: void __thiscall vostok::sound::sound_scene::set_graph(class vostok::resources::resource_ptr<class vostok::render::culling::portal_sector_structure, class vostok::resources::unmanaged_intrusive_base> &)` |
| 0.00 | `public: void __thiscall vostok::sound::sound_scene::unregister_receiver(class vostok::sound::world_user &, class vostok::sound::sound_receiver *)` |
| 0.00 | `public: void __thiscall vostok::sound::sound_scene::update_stats(class vostok::sound::sound_debug_stats &) const` |
| 0.00 | `public: void __thiscall vostok::sound::sound_voice::on_buffer_start(void *)` |
| 0.00 | `public: void __thiscall vostok::sound::sound_voice::set_output_matrix(float const *)` |
| 0.00 | `vec_begin` |
| 0.00 | `void __cdecl vostok::memory::delete_helper<class vostok::memory::doug_lea_allocator, class vostok::render::stage>(class vostok::memory::doug_lea_allocator &, class vostok::render::stage *&)` |
| 0.00 | `void __cdecl vostok::memory::delete_helper<class vostok::memory::doug_lea_allocator, struct vostok::ai::sound_item_wrapper>(class vostok::memory::doug_lea_allocator &, struct vostok::ai::sound_item_wrapper *&)` |
| 0.00 | `void __cdecl vostok::memory::detail::delete_helper_impl<class vostok::memory::base_allocator, class vostok::vfs::mounter, struct vostok::memory::detail::call_destructor_predicate>(class vostok::memory::base_allocator &, class vostok::vfs::mounter *&, struct vostok::memory::detail::call_destructor_predicate const &)` |
| 0.00 | `vostok::sound::closest_point_on_segment` |
| 3.33 | `public: virtual bool __thiscall survarium::game_world::on_mouse_move(struct vostok::input::world *, int, int, int)` |
| 3.64 | `private: class survarium::double_barreled_weapon_core_hide_state * __thiscall survarium::weapon_core_state_cook_template<class survarium::double_barreled_weapon_core_hide_state>::new_object(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)` |
| 3.64 | `private: class survarium::double_barreled_weapon_core_show_state * __thiscall survarium::weapon_core_state_cook_template<class survarium::double_barreled_weapon_core_show_state>::new_object(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)` |
| 3.64 | `private: class survarium::pistol_weapon_core_hide_state * __thiscall survarium::weapon_core_state_cook_template<class survarium::pistol_weapon_core_hide_state>::new_object(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)` |
| 3.64 | `private: class survarium::pistol_weapon_core_show_state * __thiscall survarium::weapon_core_state_cook_template<class survarium::pistol_weapon_core_show_state>::new_object(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)` |
| 3.64 | `private: class survarium::weapon_core_hide_state * __thiscall survarium::weapon_core_state_cook_template<class survarium::weapon_core_hide_state>::new_object(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)` |
| 3.64 | `private: class survarium::weapon_core_show_state * __thiscall survarium::weapon_core_state_cook_template<class survarium::weapon_core_show_state>::new_object(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)` |
| 4.09 | `public: virtual void __thiscall vostok::sound::sound_world::clear_resources(void)` |
| 4.58 | `public: void __thiscall vostok::sound::sound_voice::on_buffer_end(void *)` |
| 5.59 | `public: virtual bool __thiscall survarium::game_world::on_mouse_key_action(struct vostok::input::world *, enum vostok::input::mouse_button, enum vostok::input::enum_mouse_key_action)` |
| 8.01 | `private: virtual void __stdcall vostok::sound::voice_bridge::OnBufferEnd(void *)` |
| 8.89 | `public: void __thiscall vostok::resources::query_result_for_cook::finish_query(enum vostok::resources::query_result_for_user::error_type_enum, enum assert_on_fail_bool)` |
| 10.33 | `private: void __thiscall survarium::player::remove_alive(void)` |
| 12.00 | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 15.23 | `private: void __thiscall survarium::human_npc::set_brain_unit(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 22.38 | `private: virtual void __stdcall vostok::sound::voice_bridge::OnBufferStart(void *)` |
| 22.38 | `private: virtual void __stdcall vostok::sound::voice_bridge::OnLoopEnd(void *)` |
| 24.89 | `private: virtual void __thiscall survarium::weapon_core_hide_state_base::on_animation_end_impl(bool &)` |
| 24.89 | `private: virtual void __thiscall survarium::weapon_core_show_state_base::on_animation_end_impl(bool &)` |
| 25.00 | `private: virtual void __stdcall vostok::sound::voice_bridge::OnVoiceProcessingPassStart(unsigned int)` |
| 25.17 | `public: virtual void __thiscall vostok::detail::concrete_type_helper<struct vostok::render::static_model_instance_user_data>::copy(class vostok::mutable_buffer, class vostok::const_buffer)` |
| 26.65 | `public: __thiscall vostok::render::grass_patch::grass_patch(struct vostok::collision::space_partitioning_tree *const, struct vostok::render::grass_template *, class vostok::math::float3const &, float)` |
| 27.67 | `class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> __cdecl vostok::static_cast_resource_ptr<class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>, class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &)` |
| 28.57 | `private: virtual void __stdcall vostok::sound::voice_bridge::OnVoiceProcessingPassEnd(void)` |
| 30.00 | `public: class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> & __thiscall vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>::operator=(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 31.00 | `private: virtual void __stdcall vostok::sound::voice_bridge::OnVoiceError(void *, long)` |
| 32.07 | `private: virtual void __stdcall vostok::sound::voice_bridge::OnStreamEnd(void)` |
| 34.23 | `public: void __thiscall vostok::sound::voice_bridge::set_low_pass_filter_params(float)` |
| 34.82 | `private: virtual void __thiscall survarium::booby_trap_core::on_enter(class vostok::buffer_vector<class vostok::physics::base_physics_object *> const &)` |
| 35.21 | `public: virtual void __thiscall survarium::object_particle_visual::load(class vostok::configs::binary_config_value const &, char const *, class boost::function<void __cdecl (class survarium::game_object_&)> &)` |
| 35.60 | `public: virtual void __thiscall survarium::animation_analysis_result_cook::delete_resource(class vostok::resources::resource_base *)` |
| 35.60 | `public: virtual void __thiscall survarium::items_cook::delete_resource(class vostok::resources::resource_base *)` |
| 35.60 | `public: virtual void __thiscall survarium::items_dictionary_cook::delete_resource(class vostok::resources::resource_base *)` |
| 35.60 | `public: virtual void __thiscall survarium::player_parameters_modifyer_cook::delete_resource(class vostok::resources::resource_base *)` |
| 35.60 | `public: virtual void __thiscall survarium::weapon_ammunition_cook::delete_resource(class vostok::resources::resource_base *)` |
| 35.71 | `private: void __thiscall vostok::sound::sound_scene::emit_sound_propagators_impl(struct vostok::sound::create_sound_propagator_params const &)` |
| 36.16 | `public: virtual bool __thiscall vostok::render::render_cc_u32::fill_macro(struct vostok::render::shader_macro &) const` |
| 38.05 | `public: virtual void __thiscall vostok::sound::ogg_encoded_sound_interface_cook::delete_resource(class vostok::resources::resource_base *)` |
| 38.15 | `public: class vostok::intrusive_ptr<class vostok::sound::sound_instance_proxy, class vostok::sound::sound_instance_proxy, class vostok::threading::single_threading_policy> __thiscall vostok::sound::sound_scene::new_point_sound_instance_proxy(class vostok::resources::resource_ptr<class vostok::sound::sound_emitter, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::sound::sound_propagator_emitter const &, class vostok::sound::world_user &)` |
| 38.94 | `public: class vostok::intrusive_ptr<class vostok::sound::sound_instance_proxy, class vostok::sound::sound_instance_proxy, class vostok::threading::single_threading_policy> __thiscall vostok::sound::sound_scene::new_spot_sound_instance_proxy(class vostok::resources::resource_ptr<class vostok::sound::sound_emitter, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::sound::sound_propagator_emitter const &, class vostok::sound::world_user &, enum vostok::sound::sound_cone_type)` |
| 40.07 | `public: class vostok::intrusive_ptr<class vostok::sound::sound_instance_proxy, class vostok::sound::sound_instance_proxy, class vostok::threading::single_threading_policy> __thiscall vostok::sound::sound_scene::new_volumetric_sound_instance_proxy(class vostok::resources::resource_ptr<class vostok::sound::sound_emitter, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::sound::sound_propagator_emitter const &, class vostok::sound::world_user &, class vostok::collision::geometry_instance &, float)` |
| 41.25 | `private: void __thiscall vostok::render::device::create_d3d(void)` |
| 41.50 | `public: virtual void __thiscall vostok::detail::concrete_type_helper<struct vostok::ai::brain_unit_cook_params>::copy(class vostok::mutable_buffer, class vostok::const_buffer)` |
| 42.11 | `public: void __thiscall vostok::sound::propagator_statistic::fill_text_tree(class vostok::strings::text_tree_item *) const` |
| 42.77 | `private: void __thiscall vostok::sound::sound_world::register_sound_cooks(void)` |
| 43.84 | `private: void __thiscall survarium::network_client::process_shop_action(class vostok::network_core::packet_reader &)` |
| 43.90 | `private: void __thiscall vostok::sound::voice_bridge::set_handler(class vostok::sound::sound_voice *)` |
| 44.82 | `public: class vostok::sound::new_sound_propagator * __thiscall vostok::sound::sound_scene::create_sound_propagator(class vostok::sound::sound_propagator_emitter const &, class vostok::sound::sound_instance_proxy_internal &, enum vostok::sound::playback_mode, unsigned int, unsigned int, unsigned int, unsigned int, class vostok::sound::sound_producer const *const, class vostok::sound::sound_receiver const *const)` |
| 45.29 | `public: virtual void __thiscall survarium::victory_item_core_cook::delete_resource(class vostok::resources::resource_base *)` |
| 45.29 | `public: virtual void __thiscall survarium::weapon_core_cook::delete_resource(class vostok::resources::resource_base *)` |
| 45.29 | `public: virtual void __thiscall survarium::weapon_user_animations_container_cook::delete_resource(class vostok::resources::resource_base *)` |
| 45.29 | `public: virtual void __thiscall vostok::ai::brain_unit_cook::delete_resource(class vostok::resources::resource_base *)` |
| 45.77 | `public: virtual void __thiscall survarium::object_environment_probe::insert(void)` |
| 47.35 | `public: void __thiscall vostok::resources::query_result_for_cook::set_managed_resource(class vostok::resources::managed_resource *)` |
| 48.63 | `survarium::compare_bone_data_predicate` |
| 50.76 | `private: void __thiscall vostok::ui::ui_text_edit::add_action(class vostok::ui::base_edit_action *)` |
| 51.04 | `public: void __thiscall vostok::sound::voice_bridge::set_output_matrix(float const *)` |
| 51.70 | `public: __thiscall survarium::base_game_scene::base_game_scene(class survarium::game &)` |
| 52.23 | `public: virtual void __thiscall survarium::network_client::send_local_player_input(struct survarium::player_input const &, unsigned int, class vostok::math::float4x4const &, float)` |
| 52.78 | `public: virtual void __thiscall vostok::animation::cubic_spline_skeleton_animation_cook::destroy_resource(class vostok::resources::managed_resource *)` |
| 52.78 | `public: virtual void __thiscall vostok::render::texture_cook::destroy_resource(class vostok::resources::managed_resource *)` |
| 52.79 | `public: __thiscall vostok::ui::ui_scroll_bar::ui_scroll_bar(class vostok::memory::base_allocator &)` |
| 53.01 | `public: class vostok::render::res_texture * __thiscall vostok::render::resource_manager::create_texture2d(char const *, unsigned int, unsigned int, struct D3D11_SUBRESOURCE_DATA const *, enum DXGI_FORMAT, enum D3D11_USAGE, unsigned int, unsigned int, bool)` |
| 53.11 | `protected: virtual void __thiscall survarium::weapon_core_hide_state_base::initialize(void)` |
| 53.11 | `protected: virtual void __thiscall survarium::weapon_core_show_state_base::initialize(void)` |
| 54.35 | `public: virtual void __thiscall vostok::render::effect_motion_blur::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 54.41 | `public: void __thiscall vostok::sound::sound_world::delete_sound_voice(class vostok::sound::sound_scene &, class vostok::sound::sound_voice *)` |
| 55.61 | `public: void __thiscall survarium::weapon_core::instant_show(void)` |
| 56.52 | `public: __thiscall vostok::render::radiance_volume::radiance_volume(unsigned int, unsigned int, unsigned int, float, float)` |
| 56.83 | `private: void __thiscall survarium::player_input_handler::process_third_person_mode(void)` |
| 57.29 | `public: void __thiscall vostok::intrusive_list<struct vostok::strings::text_tree_item_base, class vostok::strings::text_tree_item *, 0, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::for_each<struct vostok::intrusive_list<struct vostok::strings::text_tree_item_base, class vostok::strings::text_tree_item *, 0, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::void_predicate_ref<struct vostok::strings::text_tree_item::text_tree_item_deleter> >(struct vostok::intrusive_list<struct vostok::strings::text_tree_item_base, class vostok::strings::text_tree_item *, 0, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::void_predicate_ref<struct vostok::strings::text_tree_item::text_tree_item_deleter> const &) const` |
| 57.46 | `public: void __thiscall survarium::human_npc::get_available_weapons(class vostok::vectora<struct vostok::ai::weapon *> &) const` |
| 57.54 | `public: void __thiscall vostok::render::options::register_console_commands(void)` |
| 58.07 | `public: void __thiscall vostok::sound::sound_spl::load(class vostok::configs::binary_config_value const &)` |
| 58.18 | `public: __thiscall vostok::fixed_string<64>::fixed_string<64>(char const *)` |
| 58.33 | `char * __cdecl vostok::strings::copy(char *, unsigned int, char const *)` |
| 58.33 | `public: class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> __thiscall vostok::resources::query_result_for_user::get_managed_resource(void) const` |
| 58.50 | `private: void __thiscall survarium::player::insert_alive(void)` |
| 58.68 | `public: virtual void __thiscall vostok::render::effect_editor_show_batched_geometry::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 59.07 | `private: void __thiscall vostok::render::stage_lights::make_plane_spot_light_shadowmap(unsigned int, class vostok::render::light *)` |
| 60.26 | `private: void __thiscall survarium::network_client::on_match_disconnected(enum vostok::network_core::disconnect_event_types_enum)` |
| 60.28 | `public: void __thiscall vostok::render::engine::world::initialize(bool)` |
| 60.32 | `public: __thiscall survarium::game_world_ui::game_world_ui(class survarium::game_world &)` |
| 60.39 | `public: void __thiscall vostok::sound::sound_scene_statistic::fill_text_tree(class vostok::strings::text_tree_item *) const` |
| 60.80 | `public: __thiscall vostok::strings::text_tree::~text_tree(void)` |
| 60.94 | `public: __thiscall survarium::max_angular_velocity_command::max_angular_velocity_command(char const *, float, float, bool, enum vostok::console_commands::command_type, enum vostok::console_commands::execution_filter)` |
| 60.98 | `private: void __thiscall vostok::render::decal_instance::set_materail_effects(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 61.16 | `public: virtual void __thiscall vostok::sound::single_sound_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 61.58 | `private: virtual void __thiscall survarium::booby_trap_set::action(bool)` |
| 62.23 | `public: virtual void __thiscall vostok::particle::particle_action_billboard::init(class vostok::particle::particle_emitter_instance *, struct vostok::particle::base_particle *, float)` |
| 62.28 | `public: void __thiscall survarium::weapon_core::instant_hide(void)` |
| 62.47 | `public: void __thiscall vostok::render::renderer_context_targets::new_rt(enum vostok::render::enum_render_target_index, enum DXGI_FORMAT, class vostok::math::uint2, enum vostok::render::enum_rt_usage, bool)` |
| 63.27 | `public: virtual void __thiscall vostok::render::effect_fstage_default_view_angle_dependent_materials::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 63.28 | `public: __thiscall vostok::ui::ui_scroll_view::ui_scroll_view(class vostok::memory::base_allocator &)` |
| 63.28 | `public: void __thiscall vostok::sound::new_sound_propagator::stop_propagation(void)` |
| 63.57 | `public: __thiscall vostok::fs_new::virtual_path_string::ctor<char const *>(char const *const &)` |
| 64.67 | `public: virtual void __thiscall survarium::game_world::get_available_weapons(struct vostok::ai::npc *, class vostok::vectora<struct vostok::ai::weapon *> &) const` |
| 66.32 | `public: virtual __thiscall survarium::game_world_ui::~game_world_ui(void)` |
| 66.48 | `private: void __thiscall survarium::damage_zone_core::hit_on_enter(unsigned int, unsigned int)` |
| 66.51 | `bool __cdecl survarium::state_prio(struct survarium::anomaly_state *, struct survarium::anomaly_state *)` |
| 66.67 | `public: class vostok::buffer_string & __thiscall vostok::buffer_string::append(char const *, char const *)` |
| 66.72 | `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::player_logic_stand_state::movement_lexeme(class vostok::mutable_buffer &, unsigned int, enum vostok::animation::body_part_masks_enum, bool, bool, bool) const` |
| 66.88 | `private: void __thiscall vostok::render::stage_lights::make_spot_light_shadowmap(unsigned int, class vostok::render::light *)` |
| 67.00 | `public: __thiscall vostok::fs_new::path_string_impl::ctor<char const *>(char, char const *const &)` |
| 67.15 | `char * __cdecl vostok::strings::copy<32>(char (&)[32], char const *)` |
| 67.22 | `public: virtual void __thiscall vostok::render::effect_system_colored::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 67.41 | `public: __thiscall vostok::console_commands::cc_delegate::cc_delegate(char const *, class boost::function<void __cdecl (char const *)> const &, bool, enum vostok::console_commands::command_type)` |
| 67.84 | `public: void __thiscall vostok::resources::association_callback_helper::get_managed(struct vostok::vfs::vfs_association *&)` |
| 68.18 | `public: virtual void __thiscall vostok::render::effect_wireframe_colored::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 68.23 | `public: void __thiscall survarium::collision_geometry::query_objects_by_type<class survarium::usable_object>(class vostok::vectora<class survarium::usable_object *> &, class survarium::usable_object * (__thiscall survarium::collision_geometry_subscriber::*)(void))` |
| 68.42 | `private: void __thiscall vostok::render::hw_hiz_occlusion_manager::check_culling_buffer(unsigned int)` |
| 68.48 | `public: void __thiscall vostok::sound::new_sound_propagator::pause_propagation(void)` |
| 69.32 | `private: void __thiscall survarium::player::detect_usable_objects(unsigned int)` |
| 70.05 | `public: class vostok::intrusive_ptr<class vostok::sound::sound_instance_proxy, class vostok::sound::sound_instance_proxy, class vostok::threading::single_threading_policy> __thiscall vostok::sound::sound_scene::new_hud_sound_instance_proxy(class vostok::resources::resource_ptr<class vostok::sound::sound_emitter, class vostok::resources::unmanaged_intrusive_base>, class vostok::sound::sound_propagator_emitter const &, class vostok::sound::world_user &)` |
| 71.19 | `public: virtual void __thiscall vostok::render::effect_gather_luminance::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 71.50 | `public: class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> & __thiscall vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>::operator=(class vostok::resources::managed_resource *)` |
| 71.67 | `public: __thiscall vostok::strings::text_tree_item::~text_tree_item(void)` |
| 71.80 | `public: virtual void __thiscall survarium::object_environment_probe::load(class vostok::configs::binary_config_value const &, char const *, class boost::function<void __cdecl (class survarium::game_object_&)> &)` |
| 72.55 | `public: enum vostok::render::enum_options_changes_result __thiscall vostok::render::options::end_render_options_changing(class vostok::render::vector<class vostok::fs_new::virtual_path_string> &)` |
| 72.85 | `public: void __thiscall vostok::particle::particle_emitter_instance::change_material(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 73.00 | `public: __thiscall vostok::collision::collision_object::collision_object(class vostok::memory::base_allocator *, unsigned int, class vostok::collision::geometry_instance *, void *const)` |
| 73.08 | `survarium::distance_from_cylinder_center_to_point_on_shape` |
| 73.16 | `public: void __thiscall vostok::ai::planning::animation_filter::add_filtered_item(char const *)` |
| 73.16 | `public: void __thiscall vostok::ai::planning::sound_filter::add_filtered_item(char const *)` |
| 73.33 | `public: void __thiscall vostok::vfs::base_node<1>::set_name(char const *)` |
| 73.34 | `private: void __thiscall survarium::damage_zone_core::hit_on_inside(unsigned int, unsigned int)` |
| 73.50 | `public: void __thiscall vostok::particle::particle_system_instance_impl::set_template(unsigned int, class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>)` |
| 74.13 | `public: virtual void __thiscall vostok::render::static_model_instance_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 74.18 | `public: __thiscall vostok::buffer_string::ctor<char const *>(char *, unsigned int const &, char const *const &, char const *const &)` |
| 74.67 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state> >::config_params)` |
| 74.67 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_show_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_show_state> >::config_params)` |
| 74.67 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state> >::config_params)` |
| 74.67 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_show_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_show_state> >::config_params)` |
| 74.67 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state> >::config_params)` |
| 74.67 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_show_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_show_state> >::config_params)` |
| 74.71 | `private: __thiscall vostok::sound::voice_bridge::voice_bridge(struct vostok::sound::voice_bridge::creation_parametrs &)` |
| 74.88 | `public: __thiscall survarium::client_player_history_item::client_player_history_item(void)` |
| 74.92 | `public: virtual void __thiscall vostok::render::effect_post_process_downsample_frame::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 75.00 | `public: class vostok::buffer_string & __thiscall vostok::buffer_string::assign<char const *>(char const *const &, char const *const &)` |
| 75.20 | `public: virtual void __thiscall vostok::ui::ui_window::add_child(struct vostok::ui::window *, bool)` |
| 75.45 | `private: void __thiscall survarium::damage_zone_core::hit_on_motion_inside(unsigned int, unsigned int)` |
| 75.71 | `public: __thiscall vostok::ai::animation_item::animation_item(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &, char const *)` |
| 75.71 | `public: __thiscall vostok::ai::sound_item::sound_item(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &, char const *)` |
| 75.97 | `public: __thiscall vostok::render::render_cc_float::render_cc_float(char const *, enum vostok::render::enum_options_changes_result, char const *, float &, float &, float, float, bool, enum vostok::console_commands::command_type)` |
| 76.54 | `public: unsigned char __thiscall survarium::body_part_parameters::get_health_in_percentage(void)` |
| 76.87 | `public: void __thiscall survarium::body_part_parameters::regenerate(unsigned int, unsigned int)` |
| 77.04 | `public: virtual void __thiscall vostok::render::effect_hiz_occlusion::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 77.14 | `public: virtual void __thiscall survarium::game_object_static::load(class vostok::configs::binary_config_value const &, char const *, class boost::function<void __cdecl (class survarium::game_object_&)> &)` |
| 77.20 | `public: virtual void __thiscall vostok::render::effect_sky_sphere_default_materials::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 77.25 | `public: virtual void __thiscall vostok::render::effect_god_rays::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 77.46 | `public: class vostok::render::render_target * __thiscall vostok::render::resource_manager::create_render_target(char const *, unsigned int, unsigned int, enum DXGI_FORMAT, enum vostok::render::enum_rt_usage, class vostok::intrusive_ptr<class vostok::render::res_texture, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, unsigned int, enum D3D11_USAGE, unsigned int, unsigned int)` |
| 77.76 | `public: __thiscall vostok::ai::planning::operator_impl::operator_impl(char const *, unsigned int)` |
| 77.88 | `public: virtual void __thiscall vostok::render::effect_eye_adaptation::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 77.89 | `private: virtual void __thiscall vostok::animation::skeleton_animation_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 78.01 | `private: class vostok::render::res_texture * __thiscall vostok::render::resource_manager::create_texture2d_impl(unsigned int, unsigned int, struct D3D11_SUBRESOURCE_DATA const *, enum DXGI_FORMAT, enum D3D11_USAGE, unsigned int, unsigned int, bool)` |
| 78.14 | `public: virtual void __thiscall vostok::render::effect_gather_luminance_histogram::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 78.61 | `public: virtual void __thiscall vostok::render::effect_post_process_mlaa::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 78.79 | `private: void __thiscall survarium::sound_player_cook::on_sounds_loaded(class vostok::resources::queries_result &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>)` |
| 79.33 | `public: virtual void __thiscall survarium::victory_items_container_core::put_item(class survarium::victory_item_core *)` |
| 79.46 | `public: void __thiscall survarium::game_world_ui::update_ui(unsigned int, unsigned int)` |
| 79.75 | `public: virtual void __thiscall vostok::render::effect_light_propagation_volumes::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 79.86 | `class vostok::math::float4x4 __cdecl vostok::math::create_rotation(class vostok::math::float3const &)` |
| 79.97 | `public: virtual void __thiscall survarium::respawn_point_core::load(class vostok::configs::binary_config_value const &)` |
| 80.22 | `private: void __thiscall survarium::game::draw_debug_window(void)` |
| 80.33 | `public: bool __thiscall vostok::variant<32>::try_get<struct vostok::ai::brain_unit_cook_params>(struct vostok::ai::brain_unit_cook_params &)` |
| 80.48 | `public: __thiscall vostok::render::stage_ambient_lighting::stage_ambient_lighting(class vostok::render::renderer *, class vostok::render::renderer_context *)` |
| 80.48 | `vostok::ai::clone_string_from_config` |
| 80.60 | `public: virtual void __thiscall survarium::object_sound::load(class vostok::configs::binary_config_value const &, char const *, class boost::function<void __cdecl (class survarium::game_object_&)> &)` |
| 80.62 | `public: virtual void __thiscall vostok::render::effect_post_process_sharpen::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 80.66 | `public: virtual void __thiscall vostok::render::effect_fstage_default_materials::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 80.68 | `public: class vostok::fs_new::path_string_impl & __thiscall vostok::fs_new::path_string_impl::append<class vostok::fixed_string<260> >(class vostok::fixed_string<260> const &)` |
| 80.78 | `public: __thiscall vostok::render::render_cc_u32::render_cc_u32(char const *, enum vostok::render::enum_options_changes_result, char const *, unsigned int &, unsigned int &, unsigned int, unsigned int, bool, enum vostok::console_commands::command_type)` |
| 80.83 | `private: bool __thiscall survarium::weapon_core::hide_pred(void) const` |
| 80.83 | `public: __thiscall vostok::console_commands::cc_value<bool>::cc_value<bool>(char const *, bool &, bool, bool, bool, enum vostok::console_commands::command_type, enum vostok::console_commands::execution_filter)` |
| 80.90 | `public: __thiscall vostok::render::render_cc_bool::render_cc_bool(char const *, enum vostok::render::enum_options_changes_result, char const *, bool &, bool &, bool, enum vostok::console_commands::command_type)` |
| 80.92 | `public: virtual void __thiscall vostok::render::effect_downsample_reflective_shadow_map::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 81.24 | `public: void __thiscall survarium::weapon_core::instant_fire(unsigned int)` |
| 81.33 | `private: void __thiscall vostok::resources::query_result::on_refered_query_ended(class vostok::resources::query_result *)` |
| 81.34 | `public: __thiscall vostok::network::login_client::login_client(struct vostok::network::world &)` |
| 81.49 | `private: struct vostok::ui::text * __thiscall vostok::console_impl::get_item(void)` |
| 81.57 | `public: void __thiscall vostok::render::grass_patch::render(struct vostok::render::grass_world *, class vostok::render::renderer_context *, class vostok::math::float3const &, enum vostok::render::enum_render_stage_type, unsigned int, float, class vostok::render::res_effect *, unsigned int)` |
| 81.78 | `public: __thiscall vostok::console_commands::cc_float::cc_float(char const *, float &, float, float, bool, enum vostok::console_commands::command_type, enum vostok::console_commands::execution_filter)` |
| 81.82 | `private: virtual void __thiscall survarium::booby_trap_set::remove(void)` |
| 81.87 | `public: virtual void __thiscall vostok::render::stage_postprocess::execute(void)` |
| 81.90 | `private: void __thiscall vostok::render::effect_manager::on_effects_recompiled(class vostok::vectora<struct vostok::render::effect_manager::effect_to_recompile_struct> *, class vostok::resources::queries_result &)` |
| 82.12 | `public: __thiscall vostok::fixed_string<24>::fixed_string<24>(class vostok::fixed_string<24> const &)` |
| 82.12 | `public: __thiscall vostok::fixed_string<260>::fixed_string<260>(class vostok::buffer_string const &)` |
| 82.12 | `public: __thiscall vostok::fixed_string<46>::fixed_string<46>(class vostok::fixed_string<46> const &)` |
| 82.22 | `public: virtual float __thiscall vostok::sound::world::get_speed_of_sound(void) const` |
| 82.39 | `public: void __thiscall survarium::booby_trap_set::on_trap_placed_message(unsigned char, class vostok::math::float3const &, class vostok::math::float3const &)` |
| 82.40 | `public: __thiscall vostok::vfs::async_callbacks_data::async_callbacks_data(enum vostok::vfs::async_callbacks_data::type_enum, struct vostok::vfs::find_environment const &)` |
| 82.58 | `public: virtual void __thiscall vostok::render::render_model::load_properties(class vostok::configs::binary_config_value const &)` |
| 82.69 | `public: virtual void __thiscall vostok::render::effect_debug_environment_probe_preview::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 82.69 | `public: virtual void __thiscall vostok::render::sky_default_material_effect::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 82.71 | `public: class vostok::fs_new::path_string_impl const & __thiscall vostok::fs_new::path_string_impl::append_with_conversion<char const *>(char const *const, char const *const)` |
| 82.75 | `public: virtual void __thiscall vostok::render::effect_olta::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 82.87 | `private: bool __thiscall vostok::resources::query_result::check_fat_for_resource_reusage(void)` |
| 82.91 | `public: virtual void __thiscall vostok::render::effect_copy_image::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 83.00 | `public: virtual void __thiscall vostok::render::effect_downsample_skin_irradiance_texture::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 83.00 | `public: virtual void __thiscall vostok::render::effect_post_process_fxaa::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 83.14 | `public: virtual void __thiscall vostok::render::effect_atmospheric_scattering::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 83.21 | `private: void __thiscall survarium::human_npc_cook::on_subresources_loaded(class vostok::resources::queries_result &, class survarium::human_npc *const)` |
| 83.24 | `private: enum vostok::resources::allocation_result_enum __thiscall vostok::resources::query_result::allocate_final_managed_resource_if_needed(void)` |
| 83.29 | `public: virtual void __thiscall vostok::render::effect_system_line::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 83.36 | `public: virtual void __thiscall vostok::render::effect_decal_mask::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 83.58 | `public: virtual void __thiscall vostok::render::effect_fill_reflective_shadow_map::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 83.77 | `public: __thiscall vostok::render::hw_hiz_occlusion_manager::hw_hiz_occlusion_manager(bool, unsigned int, unsigned int)` |
| 83.79 | `public: virtual void __thiscall vostok::render::scr_quad_effect::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 83.81 | `public: __thiscall survarium::console_command_bind::console_command_bind(class survarium::key_binder *, int)` |
| 83.82 | `public: struct stlp_std::pair<class vostok::vfs::overlapped_node_initializer, class vostok::vfs::overlapped_node_initializer> __thiscall vostok::vfs::vfs_hashset::equal_range(char const *, enum vostok::vfs::lock_type_enum)` |
| 83.94 | `public: class vostok::render::res_texture * __thiscall vostok::render::resource_manager::create_texture3d(char const *, unsigned int, unsigned int, unsigned int, struct D3D11_SUBRESOURCE_DATA const *, enum DXGI_FORMAT, unsigned int, unsigned int)` |
| 84.00 | `public: bool __thiscall vostok::vfs::vfs_hashset::find_no_branch_lock(class vostok::vfs::base_node<1> *&, char const *, enum vostok::vfs::lock_type_enum, enum vostok::vfs::lock_operation_enum)` |
| 84.00 | `public: void __thiscall vostok::sound::sound_voice::stop(void)` |
| 84.20 | `public: virtual void __thiscall vostok::render::effect_apply_distortion::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 84.22 | `class vostok::math::float4x4 __cdecl vostok::animation::calculated_head_matrix(class vostok::math::float4x4const &, class vostok::math::float4x4const &)` |
| 84.26 | `private: void __thiscall survarium::weapon_core_cook::query_weapon_states(class vostok::resources::query_result_for_cook *const, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class survarium::weapon_core *)` |
| 84.32 | `public: virtual void __thiscall vostok::render::effect_simple_fog::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 84.33 | `public: virtual void __thiscall vostok::render::effect_ssao_downsample_position_and_normal::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 84.41 | `public: void __thiscall survarium::player::remove(void)` |
| 84.44 | `void __cdecl vostok::fs_new::get_path_without_last_item<class vostok::fs_new::native_path_string>(class vostok::fs_new::native_path_string *, char const *)` |
| 84.44 | `void __cdecl vostok::fs_new::get_path_without_last_item<class vostok::fs_new::virtual_path_string>(class vostok::fs_new::virtual_path_string *, char const *)` |
| 84.45 | `public: virtual void __thiscall vostok::render::stage_ambient_lighting::execute(void)` |
| 84.62 | `private: void __thiscall vostok::render::static_model_instance_cook::on_subresources_loaded(class vostok::resources::queries_result &, class vostok::resources::query_result_for_cook *)` |
| 84.67 | `public: virtual void __thiscall vostok::render::effect_aberration::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 84.67 | `public: virtual void __thiscall vostok::render::effect_downsample_gbuffer::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 84.67 | `public: virtual void __thiscall vostok::render::effect_fix_irradiance_texture::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 84.67 | `public: virtual void __thiscall vostok::render::effect_read_cloud_base::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 84.79 | `survarium::fill_damage_model` |
| 84.88 | `public: void __thiscall survarium::game::create_lobby_menu(void)` |
| 84.88 | `public: void __thiscall survarium::game::create_login_menu(void)` |
| 84.92 | `public: virtual void __thiscall vostok::render::effect_apply_indirect_lighting::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 85.05 | `class vostok::collision::object * __cdecl vostok::collision::new_collision_object(class vostok::memory::base_allocator *, unsigned int, class vostok::collision::geometry_instance *, void *)` |
| 85.08 | `private: void __thiscall vostok::ui::ui_text_edit::init_internals(enum vostok::ui::enum_text_edit_mode)` |
| 85.34 | `public: virtual void __thiscall vostok::render::effect_light_mask::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 85.46 | `private: virtual void __thiscall vostok::render::depth_accumulate_material_effect::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 85.49 | `public: virtual void __thiscall vostok::render::effect_apply_decal::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 85.68 | `private: virtual void __thiscall survarium::weapon::instant_aim_end(void)` |
| 85.73 | `public: virtual void __thiscall vostok::render::effect_rain::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 85.83 | `public: __thiscall survarium::main_menu::main_menu(class survarium::game &)` |
| 85.85 | `private: void __thiscall survarium::body_part_parameters::apply_affects(class survarium::affects_threshold const *, unsigned int)` |
| 85.89 | `private: bool __thiscall survarium::weapon_core::AE_pred(void) const` |
| 86.00 | `public: virtual void __thiscall vostok::render::effect_ssao_filter4x4::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 86.00 | `public: virtual void __thiscall vostok::render::effect_environment_probe_lighting<1, 1, 0>::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 86.04 | `public: virtual void __thiscall vostok::render::effect_gather_bloom::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 86.04 | `public: virtual void __thiscall vostok::render::effect_grass_trample::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 86.04 | `public: virtual void __thiscall vostok::render::effect_post_process_sraa::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 86.06 | `public: class vostok::sound::voice_bridge * __thiscall vostok::sound::voice_factory::new_voice(class vostok::sound::sound_voice *, unsigned char, unsigned int)` |
| 86.14 | `public: void __thiscall survarium::player::insert(bool)` |
| 86.24 | `public: virtual void __thiscall vostok::render::effect_system_ui::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 86.28 | `public: bool __thiscall vostok::variant<32>::try_get<struct vostok::render::static_model_instance_user_data>(struct vostok::render::static_model_instance_user_data &)` |
| 86.43 | `private: void __thiscall vostok::render::renderer_context_targets::create_targets(class vostok::math::uint2, bool)` |
| 86.45 | `public: virtual void __thiscall vostok::render::effect_forward_system::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 86.47 | `public: __thiscall survarium::game_material::game_material(void)` |
| 86.50 | `private: class survarium::weapon_core_chamber_a_round_aimed_state * __thiscall survarium::weapon_core_state_cook_template<class survarium::weapon_core_chamber_a_round_aimed_state>::new_object(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)` |
| 86.50 | `private: class survarium::weapon_core_chamber_a_round_state * __thiscall survarium::weapon_core_state_cook_template<class survarium::weapon_core_chamber_a_round_state>::new_object(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)` |
| 86.56 | `public: virtual void __thiscall vostok::render::effect_environment_probe_lighting<0, 1, 1>::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 86.56 | `public: virtual void __thiscall vostok::render::effect_environment_probe_lighting<1, 0, 1>::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 86.58 | `private: void __thiscall vostok::resources::game_resources_manager::dispatch_capture(class vostok::resources::resource_base *)` |
| 86.64 | `public: virtual void __thiscall vostok::render::effect_copy_depth_rt::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 86.72 | `public: void __thiscall vostok::render::options::set_default_values(void)` |
| 86.76 | `public: virtual void __thiscall vostok::render::effect_skylight::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 86.77 | `public: void __thiscall survarium::player::kill(unsigned int)` |
| 86.83 | `public: virtual void __thiscall vostok::render::effect_editor_apply_wireframe::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 86.83 | `public: virtual void __thiscall vostok::render::effect_reflection_mask::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 86.86 | `private: void __thiscall vostok::render::shader_macros::register_available_macros(void)` |
| 87.06 | `public: __thiscall vostok::console_commands::cc_bool::cc_bool(char const *, bool &, bool, enum vostok::console_commands::command_type, enum vostok::console_commands::execution_filter)` |
| 87.08 | `public: virtual __thiscall vostok::sound::single_sound::~single_sound(void)` |
| 87.17 | `private: virtual struct stlp_std::pair<class vostok::animation::mixing::expression, class vostok::animation::mixing::animation_lexeme> __thiscall survarium::player_logic_sprint_state::selected_animations(class vostok::mutable_buffer &, struct survarium::weapon_animation_parameters const &, bool) const` |
| 87.19 | `char const * __cdecl vostok::strings::get_token(char const *, char *, unsigned int, char)` |
| 87.19 | `public: virtual void __thiscall vostok::render::effect_lens_flares::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 87.19 | `public: virtual void __thiscall vostok::render::effect_temporal_antialiasing::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 87.29 | `private: void __thiscall survarium::project_cooker_simple::create_game_objects(class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class vostok::resources::query_result_for_cook *)` |
| 87.36 | `public: virtual void __thiscall vostok::render::effect_clouds_god_rays::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 87.36 | `public: virtual void __thiscall vostok::render::effect_exponential_volume_fog::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 87.38 | `public: void __thiscall survarium::damage_model::add_damage_protector(char const *, float, float)` |
| 87.50 | `public: virtual void __thiscall vostok::render::effect_wet_surface::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 87.51 | `public: void __thiscall vostok::render::environment_probe::set_properties(struct vostok::render::environment_probe_properties const &)` |
| 87.53 | `public: virtual void __thiscall vostok::render::effect_fill_sky_ao_map::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 87.56 | `private: virtual void __thiscall survarium::booby_trap_core::deserialize(class vostok::network_core::packet_reader &)` |
| 87.65 | `public: void __thiscall vostok::fs_new::path_part_iterator::append_to_string<class vostok::fs_new::native_path_string>(class vostok::fs_new::native_path_string &) const` |
| 87.86 | `public: virtual void __thiscall vostok::render::effect_image_space_reflections::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 87.86 | `public: virtual void __thiscall vostok::render::effect_resolve_particles::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 87.87 | `vostok::vfs::hot_mount_helper` |
| 87.88 | `public: virtual void __thiscall vostok::render::effect_environment_probe_lighting<0, 0, 0>::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 87.90 | `public: void __thiscall survarium::body_part_parameters::apply_affect_by_force(enum survarium::hit_affects_type_enum, enum survarium::affect_event_type_enum, unsigned int)` |
| 87.94 | `public: void __thiscall survarium::jump_logic::deactivate(void)` |
| 87.97 | `public: virtual void __thiscall vostok::render::effect_post_process_blend_texture_materials::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 88.00 | `public: static class vostok::vfs::physical_folder_node<1> * __cdecl vostok::vfs::physical_folder_node<1>::create(class vostok::memory::base_allocator *, class vostok::vfs::mount_root_node_base<1> *, class vostok::fs_new::virtual_path_string const &)` |
| 88.01 | `public: virtual void __thiscall vostok::render::effect_pick_light_luminance::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 88.03 | `public: virtual void __thiscall vostok::render::effect_ssao_accumulation::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 88.05 | `public: virtual void __thiscall vostok::render::effect_environment_probe_lighting<0, 0, 1>::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 88.05 | `public: virtual void __thiscall vostok::render::effect_environment_probe_lighting<0, 1, 0>::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 88.05 | `public: virtual void __thiscall vostok::render::effect_environment_probe_lighting<1, 0, 0>::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 88.05 | `public: virtual void __thiscall vostok::render::effect_environment_probe_lighting<1, 1, 1>::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 88.14 | `public: __thiscall vostok::ai::planning::movement_target_wrapper::movement_target_wrapper(class vostok::math::float3const &, class vostok::math::float3const &, class vostok::math::float3const &, char const *)` |
| 88.32 | `public: void __thiscall vostok::render::effect_material_base::compile_begin(char const *, char const *, char const *, class vostok::render::effect_compiler &, struct vostok::render::shader_configuration *, class vostok::render::custom_config_value const &)` |
| 88.32 | `public: virtual void __thiscall vostok::render::effect_blur<13>::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 88.32 | `public: virtual void __thiscall vostok::render::effect_blur<17>::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 88.32 | `public: virtual void __thiscall vostok::render::effect_blur<21>::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 88.32 | `public: virtual void __thiscall vostok::render::effect_blur<25>::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 88.32 | `public: virtual void __thiscall vostok::render::effect_blur<3>::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 88.32 | `public: virtual void __thiscall vostok::render::effect_blur<5>::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 88.32 | `public: virtual void __thiscall vostok::render::effect_blur<7>::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 88.32 | `public: virtual void __thiscall vostok::render::effect_blur<9>::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 88.40 | `public: __thiscall vostok::console_commands::cc_value<float>::cc_value<float>(char const *, float &, float, float, bool, enum vostok::console_commands::command_type, enum vostok::console_commands::execution_filter)` |
| 88.58 | `public: virtual __thiscall vostok::sound::sound_world::~sound_world(void)` |
| 88.75 | `private: void __thiscall vostok::network::login_client::create_client(void)` |
| 88.86 | `public: __thiscall vostok::console_commands::console_command::console_command(char const *, bool, enum vostok::console_commands::command_type, enum vostok::console_commands::execution_filter)` |
| 89.15 | `public: void __thiscall survarium::game_world::load(char const *, struct vostok::resources::request *, struct vostok::resources::request *, class vostok::variant<32> const **, class boost::function<void __cdecl (class vostok::resources::queries_result &)> const &)` |
| 89.16 | `public: static class vostok::vfs::physical_folder_mount_root_node<1> * __cdecl vostok::vfs::mount_root_node_functions::create<class vostok::vfs::physical_folder_mount_root_node, 1>(char const *, unsigned int, class vostok::vfs::virtual_file_system *, class vostok::vfs::query_mount_arguments &)` |
| 89.16 | `private: void __thiscall vostok::vfs::archive_mounter::mount_fat(class vostok::vfs::archive_folder_mount_root_node<1> *, class vostok::vfs::base_folder_node<1> *)` |
| 89.20 | `public: virtual void __thiscall survarium::damage_zone_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 89.25 | `public: class vostok::fs_new::path_string_impl & __thiscall vostok::fs_new::path_string_impl::append_path<class vostok::fixed_string<260> >(class vostok::fixed_string<260> const &)` |
| 89.25 | `public: virtual void __thiscall vostok::render::effect_fill_environment_probe_face::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 89.26 | `public: __thiscall survarium::victory_item::victory_item(class survarium::game_world &)` |
| 89.33 | `private: void __thiscall vostok::render::shader_macros::fill_shader_configuration_macros(class vostok::fixed_vector<struct vostok::render::shader_macro, 128> &, struct vostok::render::shader_configuration)` |
| 89.54 | `private: virtual void __thiscall survarium::empty_hands::update_bones_matrices(class vostok::resources::resource_ptr<class vostok::animation::skeleton, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float4x4*const, unsigned int, unsigned int, class vostok::math::float4x4&, class vostok::math::float4x4&, class vostok::animation::animation_player const &)` |
| 89.60 | `public: void __thiscall vostok::render::grass_world::populate(float)` |
| 89.65 | `private: virtual void __thiscall vostok::render::capsule_light_effect::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 89.67 | `public: __thiscall vostok::render::binary_shader_source::binary_shader_source(void)` |
| 89.68 | `public: __thiscall vostok::sound::sound_voice::~sound_voice(void)` |
| 89.69 | `private: void __thiscall vostok::particle::particle_emitter_instance::on_material_loaded(class vostok::resources::queries_result &)` |
| 89.75 | `public: void __thiscall vostok::intrusive_list<struct vostok::strings::text_tree_column_item, struct vostok::strings::text_tree_column_item *, 0, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::for_each<struct vostok::intrusive_list<struct vostok::strings::text_tree_column_item, struct vostok::strings::text_tree_column_item *, 0, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::void_predicate_ref<struct vostok::strings::text_tree_item::text_tree_item_deleter> >(struct vostok::intrusive_list<struct vostok::strings::text_tree_column_item, struct vostok::strings::text_tree_column_item *, 0, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::void_predicate_ref<struct vostok::strings::text_tree_item::text_tree_item_deleter> const &) const` |
| 89.77 | `public: virtual void __thiscall vostok::render::effect_fstage_volume_sphere_base_materials::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 89.77 | `public: __thiscall vostok::render::stage_shadow_direct::stage_shadow_direct(class vostok::render::renderer *, class vostok::render::renderer_context *)` |
- _...and 1065 more_

### Added (142)

- `float __cdecl survarium::chamber_a_round_timescale_calculator(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, struct survarium::weapon_state_creation_params const &)`
- `float __cdecl survarium::computed_hide_animation_time_scale(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, float)`
- `float __cdecl survarium::hide_timescale_calculator(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, struct survarium::weapon_state_creation_params const &)`
- `float __cdecl survarium::show_timescale_calculator(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, struct survarium::weapon_state_creation_params const &)`
- `int __cdecl vostok::strings::compare(char const *, char const *)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state>::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_show_state>::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_show_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state>::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_show_state>::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_show_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state>::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::weapon_core_show_state>::weapon_sound_events_handler_state<class survarium::weapon_core_show_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: bool __thiscall survarium::weapon_core::hide_break_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::idle_AE_or_show_break_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::show_AE_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::show_pred(void) const`
- `private: bool __thiscall survarium::weapon_core_shotgun_reload_state::player_wants_to_aim_predicate(void) const`
- `private: class vostok::math::float3 __thiscall survarium::weapon_core::get_dispersed_buckshot_direction(class vostok::math::float3const &)`
- `private: unsigned int __thiscall vostok::render::stage_lights::index_to_shadow_size(class vostok::render::light *, unsigned int) const`
- `private: virtual class vostok::mutable_buffer __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state> >::allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)`
- `private: virtual class vostok::mutable_buffer __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_start_substate> >::allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)`
- `private: virtual float __thiscall survarium::player::get_movement_speed_factor(void) const`
- `private: virtual void __thiscall survarium::booby_trap_set_core::remove_game_world_objects(void)`
- `private: virtual void __thiscall survarium::network_client::close_current_match(enum vostok::network_core::disconnect_event_types_enum)`
- `private: virtual void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state> >::destroy_resource(class vostok::resources::unmanaged_resource *)`
- `private: virtual void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_start_substate> >::destroy_resource(class vostok::resources::unmanaged_resource *)`
- `private: void __thiscall survarium::damage_zone_core::contact_test_body_parts(struct survarium::hit_receiver_info const &, class vostok::vectora<struct stlp_std::pair<class vostok::collision::bone_collision_data *, float> > &)`
- `private: void __thiscall survarium::network_client::remove_player(class vostok::network_core::packet_reader &)`
- `private: void __thiscall vostok::intrusive_ptr<class vostok::sound::panning_lut, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock>::set(class vostok::intrusive_ptr<class vostok::sound::panning_lut, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock> const &)`
- `private: void __thiscall vostok::render::resource_manager::log_texture_stats(void)`
- `private: void __thiscall vostok::sound::ogg_encoded_sound_interface_cook::on_ogg_resources_loaded(class vostok::resources::queries_result &, class vostok::resources::query_result_for_cook *)`
- `private: void __thiscall vostok::sound::ogg_encoded_sound_interface_cook::query_converted_resources(class vostok::resources::query_result_for_cook *)`
- `private: void __thiscall vostok::sound::single_sound_cook::on_sound_options_loaded(class vostok::resources::queries_result &, class vostok::resources::query_result_for_cook *)`
- `private: void __thiscall vostok::sound::single_sound_cook::on_sub_resources_loaded(class vostok::resources::queries_result &, float)`
- `private: void __thiscall vostok::sound::sound_scene::calculate_channel_matrix(unsigned char, class vostok::resources::resource_ptr<class vostok::sound::panning_lut, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::sound::sound_instance_proxy_internal const &, class vostok::math::float3const &, float, float, float *const, float &) const`
- `private: void __thiscall vostok::sound::sound_scene::calculate_hdr_audio_frame(class vostok::vectora<class vostok::sound::new_sound_propagator *> &, unsigned int)`
- `private: void __thiscall vostok::sound::sound_scene::notify_listener(unsigned int)`
- `private: void __thiscall vostok::sound::sound_scene::notify_listener2(unsigned int)`
- `private: void __thiscall vostok::sound::sound_scene::process_fade(unsigned __int64)`
- `private: void __thiscall vostok::sound::sound_scene::x3daudio_calculate(class vostok::sound::sound_voice &)`
- `protected: __thiscall survarium::double_barreled_weapon_core_hide_state::double_barreled_weapon_core_hide_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)`
- `protected: __thiscall survarium::double_barreled_weapon_core_show_state::double_barreled_weapon_core_show_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)`
- `protected: __thiscall survarium::pistol_weapon_core_hide_state::pistol_weapon_core_hide_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)`
- `protected: __thiscall survarium::pistol_weapon_core_show_state::pistol_weapon_core_show_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)`
- `protected: __thiscall survarium::weapon_core_hide_state::weapon_core_hide_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)`
- `protected: __thiscall survarium::weapon_core_hide_state_base::weapon_core_hide_state_base(class survarium::weapon_core &)`
- `protected: __thiscall survarium::weapon_core_show_state::weapon_core_show_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)`
- `protected: __thiscall survarium::weapon_core_show_state_base::weapon_core_show_state_base(class survarium::weapon_core &)`
- `protected: bool __thiscall survarium::booby_trap_set_core::try_place_trap(class survarium::booby_trap_core &)`
- `protected: class survarium::booby_trap_core * __thiscall survarium::booby_trap_set_core::find_free_trap(void)`
- `public: __thiscall survarium::body_part_parameters::body_part_parameters(char const *, float, float, float, float, bool, class survarium::damage_model &, unsigned char)`
- `public: __thiscall survarium::client_player_update::client_player_update(void)`
- `public: __thiscall survarium::player_state::player_state(void)`
- `public: __thiscall survarium::vector<class vostok::variant<32> >::vector<class vostok::variant<32> >(unsigned int)`
- `public: __thiscall survarium::vector<class vostok::variant<32> >::~vector<class vostok::variant<32> >(void)`
- `public: __thiscall vostok::buffer_vector<float>::buffer_vector<float>(void *, unsigned int, unsigned int)`
- `public: __thiscall vostok::fixed_string<128>::fixed_string<128>(void)`
- `public: __thiscall vostok::memory::single_size_buffer_allocator<32, class vostok::threading::single_threading_policy>::single_size_buffer_allocator<32, class vostok::threading::single_threading_policy>(void *, unsigned int)`
- `public: __thiscall vostok::memory::single_size_buffer_allocator<84, class vostok::threading::single_threading_policy>::single_size_buffer_allocator<84, class vostok::threading::single_threading_policy>(void *, unsigned int)`
- `public: __thiscall vostok::memory::single_size_buffer_allocator<96, class vostok::threading::single_threading_policy>::single_size_buffer_allocator<96, class vostok::threading::single_threading_policy>(void *, unsigned int)`
- `public: __thiscall vostok::particle::particle_action_billboard::particle_action_billboard(void)`
- `public: __thiscall vostok::render::effect_compiler::shader_cache_info::shader_cache_info(void)`
- `public: __thiscall vostok::render::render_target_instance::render_target_instance(void)`
- `public: __thiscall vostok::render::vs_data::~vs_data(void)`
- `public: __thiscall vostok::render::xs_descriptor<struct vostok::render::gs_data>::~xs_descriptor<struct vostok::render::gs_data>(void)`
- `public: __thiscall vostok::render::xs_descriptor<struct vostok::render::ps_data>::~xs_descriptor<struct vostok::render::ps_data>(void)`
- `public: __thiscall vostok::resources::resource_ptr<class vostok::physics::bt_collision_shape, class vostok::resources::unmanaged_intrusive_base>::resource_ptr<class vostok::physics::bt_collision_shape, class vostok::resources::unmanaged_intrusive_base>(class vostok::physics::bt_collision_shape *)`
- `public: __thiscall vostok::shared_string::~shared_string(void)`
- `public: __thiscall vostok::sound::new_sound_propagator::new_sound_propagator(enum vostok::sound::playback_mode, unsigned int, unsigned int, unsigned int, unsigned int, class vostok::sound::sound_instance_proxy_internal &, class vostok::sound::sound_propagator_emitter const &)`
- `public: __thiscall vostok::sound::ogg_encoded_sound_interface::ogg_encoded_sound_interface(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, float const *, unsigned int, unsigned int)`
- `public: __thiscall vostok::sound::single_sound::single_sound(class vostok::resources::resource_ptr<class vostok::sound::encoded_sound_with_qualities, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::sound::sound_spl, class vostok::resources::unmanaged_intrusive_base> const &, float)`
- `public: __thiscall vostok::sound::sound_voice::sound_voice(class vostok::sound::sound_instance_proxy_internal &, class vostok::sound::sound_propagator_emitter const &, class vostok::resources::resource_ptr<class vostok::sound::sound_spl, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: __thiscall vostok::sound::voice_factory::voice_factory(unsigned char *, unsigned int, class vostok::sound::sound_world &, struct vostok::sound::pool_parametrs const &)`
- `public: __thiscall vostok::threading::mutex::~mutex(void)`
- `public: __thiscall vostok::vectora_allocator<class vostok::fixed_vector<unsigned int, 32> >::ctor<void *>(class vostok::vectora_allocator<void *> const &)`
- `public: __thiscall vostok::vfs::query_mount_arguments::query_mount_arguments(class vostok::vfs::query_mount_arguments const &)`
- `public: bool __thiscall survarium::contacted_bones_comparator::operator()(struct stlp_std::pair<class vostok::collision::bone_collision_data *, float> const &, struct stlp_std::pair<class vostok::collision::bone_collision_data *, float> const &) const`
- `public: bool __thiscall vostok::intrusive_list<class vostok::particle::particle_emitter_instance, class vostok::particle::particle_emitter_instance *, 228, class vostok::threading::single_threading_policy, class vostok::size_policy, class vostok::no_debug_policy>::erase(class vostok::particle::particle_emitter_instance *)`
- `public: class vostok::render::effect_compiler & __thiscall vostok::render::effect_compiler::begin_pass(char const *, char const *, char const *, struct vostok::render::shader_configuration, struct vostok::render::shader_include_getter *)`
- `public: class vostok::sound::sound_voice * __thiscall vostok::sound::sound_world::create_sound_voice(class vostok::sound::sound_scene &, class vostok::sound::sound_instance_proxy_internal *, class vostok::sound::sound_propagator_emitter const &, class vostok::resources::resource_ptr<class vostok::sound::sound_spl, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: float __thiscall survarium::calc_distance_functor::operator()(class vostok::physics::base_physics_object *const &)`
- `public: float __thiscall vostok::sound::new_sound_propagator::get_sound_rms_value(void) const`
- `public: float __thiscall vostok::sound::new_sound_propagator::get_sound_spl_value(float) const`
- `public: float __thiscall vostok::sound::new_sound_propagator::get_sound_spl_value(void) const`
- `public: static union vostok::memory::single_size_buffer_allocator<32, class vostok::threading::single_threading_policy>::node * __cdecl vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<32, class vostok::threading::single_threading_policy>::node>::allocate(class vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<32, class vostok::threading::single_threading_policy>::node>::free_list_type &)`
- `public: static union vostok::memory::single_size_buffer_allocator<84, class vostok::threading::single_threading_policy>::node * __cdecl vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<84, class vostok::threading::single_threading_policy>::node>::allocate(class vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<84, class vostok::threading::single_threading_policy>::node>::free_list_type &)`
- `public: static union vostok::memory::single_size_buffer_allocator<96, class vostok::threading::single_threading_policy>::node * __cdecl vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<96, class vostok::threading::single_threading_policy>::node>::allocate(class vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<96, class vostok::threading::single_threading_policy>::node>::free_list_type &)`
- `public: static void __cdecl vostok::render::resource_intrusive_base::destroy<class vostok::render::light>(class vostok::render::light const *const)`
- `public: struct stlp_std::pair<struct stlp_std::pair<struct vostok::render::texture_stats_key, unsigned int> *, bool> __thiscall associative_vector<struct vostok::render::texture_stats_key, unsigned int, class vostok::render::vector, struct stlp_std::less<struct vostok::render::texture_stats_key> >::insert(struct stlp_std::pair<struct vostok::render::texture_stats_key, unsigned int> const &)`
- `public: struct vostok::ai::brain_unit_cook_params & __thiscall vostok::ai::brain_unit_cook_params::operator=(struct vostok::ai::brain_unit_cook_params const &)`
- `public: unsigned char __thiscall survarium::damage_model::get_pain_health(void)`
- `public: unsigned int __thiscall vostok::render::options::get_cascaded_shadow_map_size(void) const`
- `public: virtual __thiscall survarium::animated_model_instance::~animated_model_instance(void)`
- `public: virtual __thiscall survarium::rifle_scope::~rifle_scope(void)`
- `public: virtual float __thiscall vostok::sound::composite_sound::get_sound_spl_value(void) const`
- `public: virtual float __thiscall vostok::sound::ogg_encoded_sound_interface::get_rms_by_time(unsigned __int64) const`
- `public: virtual float __thiscall vostok::sound::single_sound::get_sound_spl_value(void) const`
- `public: virtual int __thiscall survarium::game_world::input_priority(void)`
- `public: virtual void __thiscall survarium::base_player::remove_game_world_objects(void)`
- `public: virtual void __thiscall survarium::game_world_ui::callback(struct survarium::flash_movie *, char const *, struct survarium::flash_value const *, unsigned int)`
- `public: virtual void __thiscall vostok::render::effect_environment_probe_index::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)`
- `public: void * __thiscall vostok::memory::single_size_buffer_allocator<32, class vostok::threading::single_threading_policy>::allocate(void)`
- `public: void * __thiscall vostok::memory::single_size_buffer_allocator<32, class vostok::threading::single_threading_policy>::malloc_impl(unsigned int)`
- `public: void * __thiscall vostok::memory::single_size_buffer_allocator<536, class vostok::threading::multi_threading_policy>::malloc_impl(unsigned int)`
- `public: void * __thiscall vostok::memory::single_size_buffer_allocator<84, class vostok::threading::single_threading_policy>::malloc_impl(unsigned int)`
- `public: void * __thiscall vostok::memory::single_size_buffer_allocator<96, class vostok::threading::single_threading_policy>::malloc_impl(unsigned int)`
- `public: void __thiscall survarium::game_world::on_finish_match(void)`
- `public: void __thiscall survarium::game_world::set_match_stats_state(void)`
- `public: void __thiscall survarium::game_world_ui::initialize_resources(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: void __thiscall survarium::game_world_ui::show_cursor(bool)`
- `public: void __thiscall survarium::game_world_ui::show_match_stats_wnd(void)`
- `public: void __thiscall survarium::inventory::remove_game_world_objects(void)`
- `public: void __thiscall survarium::jump_logic::end_jump(void)`
- `public: void __thiscall survarium::jump_logic::start_jump(void)`
- `public: void __thiscall survarium::lobby_client::sell_item(unsigned int, unsigned int)`
- `public: void __thiscall survarium::std_allocator<class vostok::variant<32> >::deallocate(class vostok::variant<32> *, unsigned int) const`
- `public: void __thiscall vostok::ai::fsm::append_transition(struct vostok::ai::fsm_state *, struct vostok::ai::fsm_state *, class boost::function<bool __cdecl (void)> const &)`
- `public: void __thiscall vostok::ai::fsm::prepend_transition(struct vostok::ai::fsm_state *, struct vostok::ai::fsm_state *, class boost::function<bool __cdecl (void)> const &)`
- `public: void __thiscall vostok::buffer_vector<float>::push_back(float const &)`
- `public: void __thiscall vostok::buffer_vector<struct survarium::client_player_update>::push_back(struct survarium::client_player_update const &)`
- `public: void __thiscall vostok::intrusive_list<class vostok::particle::particle_emitter_instance, class vostok::particle::particle_emitter_instance *, 228, class vostok::threading::single_threading_policy, class vostok::size_policy, class vostok::no_debug_policy>::push_back(class vostok::particle::particle_emitter_instance *, bool *)`
- `public: void __thiscall vostok::intrusive_list<struct vostok::ai::fsm_state_transition, struct vostok::ai::fsm_state_transition *, 36, class vostok::threading::single_threading_policy, class vostok::size_policy, class vostok::no_debug_policy>::push_front(struct vostok::ai::fsm_state_transition *, bool *)`
- `public: void __thiscall vostok::render::effect_manager::create_effect<class vostok::render::effect_environment_probe_index>(class vostok::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base> *)`
- `public: void __thiscall vostok::render::resource_manager::tick(void)`
- `public: void __thiscall vostok::render::shader_configuration::merge_with(char const *, struct vostok::render::shader_configuration)`
- `public: void __thiscall vostok::render::stage_ambient_lighting::make_probe_indices_map(class vostok::render::vector<struct vostok::render::environment_probe *> &)`
- `public: void __thiscall vostok::sound::new_sound_propagator::attach_voice(void)`
- `public: void __thiscall vostok::sound::new_sound_propagator::detach_voice(void)`
- `public: void __thiscall vostok::sound::sound_instance_proxy_internal::tick(class vostok::math::float3const &, unsigned int)`
- `public: void __thiscall vostok::sound::sound_scene::tick(unsigned int)`
- `public: void __thiscall vostok::sound::sound_voice::set_volume(float)`
- `public: void __thiscall vostok::sound::voice_bridge::set_volume(float)`
- `survarium::arbitrary_right`
- `survarium::call_item_remove_game_world_objects`
- `void __cdecl `public: void __thiscall vostok::render::effect_manager::create_effect<class vostok::render::effect_environment_probe_index>(class render::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base> *)'::`2'::descriptor_object::`dynamic atexit destructor'(void)`
- `void __cdecl vostok::debug::platform::terminate(int, char const *)`
- `void __cdecl vostok::memory::detail::delete_helper_impl<class vostok::memory::single_size_buffer_allocator<32, class vostok::threading::single_threading_policy>, class vostok::sound::voice_bridge, struct vostok::memory::detail::call_destructor_predicate>(class vostok::memory::single_size_buffer_allocator<32, class vostok::threading::single_threading_policy> &, class vostok::sound::voice_bridge *&, struct vostok::memory::detail::call_destructor_predicate const &)`
- `void __cdecl vostok::memory::detail::delete_helper_impl<class vostok::memory::single_size_buffer_allocator<84, class vostok::threading::single_threading_policy>, class vostok::sound::new_sound_propagator, struct vostok::memory::detail::call_destructor_predicate>(class vostok::memory::single_size_buffer_allocator<84, class vostok::threading::single_threading_policy> &, class vostok::sound::new_sound_propagator *&, struct vostok::memory::detail::call_destructor_predicate const &)`
- `void __cdecl vostok::memory::detail::delete_helper_impl<class vostok::memory::single_size_buffer_allocator<96, class vostok::threading::single_threading_policy>, class vostok::sound::sound_voice, struct vostok::memory::detail::call_destructor_predicate>(class vostok::memory::single_size_buffer_allocator<96, class vostok::threading::single_threading_policy> &, class vostok::sound::sound_voice *&, struct vostok::memory::detail::call_destructor_predicate const &)`
- `void __cdecl vostok::sound::test_ogg_query(void)`
- `void __cdecl vostok::sound::test_snd_loaded(class vostok::resources::queries_result &)`
- `vostok::render::format_name`
- `vostok::render::modify_shader_configuration`

### Deleted (160)

- `class vostok::animation::mixing::addition_lexeme & __cdecl vostok::animation::mixing::operator+<class vostok::animation::mixing::animation_lexeme, class vostok::animation::mixing::animation_lexeme>(class vostok::animation::mixing::animation_lexeme &, class vostok::animation::mixing::animation_lexeme &)`
- `float __cdecl survarium::computed_reload_animation_time_scale(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, float)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state>::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char, bool &)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_show_state>::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_show_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char, bool &)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state>::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char, bool &)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_show_state>::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_show_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char, bool &)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state>::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char, bool &)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::weapon_core_show_state>::weapon_sound_events_handler_state<class survarium::weapon_core_show_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char, bool &)`
- `private: bool __thiscall survarium::weapon_core::idle_AE_or_chamber_a_round_break_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::not_inactive_pred(void) const`
- `private: class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state> * __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state> >::new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state> >::config_params const &)`
- `private: class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_show_state> * __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_show_state> >::new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_show_state> >::config_params const &)`
- `private: class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state> * __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state> >::new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state> >::config_params const &)`
- `private: class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_show_state> * __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_show_state> >::new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_show_state> >::config_params const &)`
- `private: class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state> * __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state> >::new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state> >::config_params const &)`
- `private: class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_show_state> * __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_show_state> >::new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_show_state> >::config_params const &)`
- `private: class vostok::sound::sound_voice * __thiscall vostok::sound::new_sound_propagator::attach_voice(unsigned int)`
- `private: struct IXAudio2SubmixVoice * __thiscall vostok::sound::sound_scene::create_environment_submix_voice(class vostok::sound::sound_world const &) const`
- `private: unsigned int __thiscall vostok::render::stage_lights::index_to_shadow_size(unsigned int) const`
- `private: virtual bool __thiscall survarium::weapon_core_hide_state_base::is_ready_for_transition(void) const`
- `private: virtual class vostok::mutable_buffer __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state> >::allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)`
- `private: virtual class vostok::mutable_buffer __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state> >::allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)`
- `private: virtual void __thiscall survarium::network_client::close_current_match(bool)`
- `private: virtual void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state> >::destroy_resource(class vostok::resources::unmanaged_resource *)`
- `private: virtual void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state> >::destroy_resource(class vostok::resources::unmanaged_resource *)`
- `private: void __thiscall vostok::intrusive_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base, class vostok::threading::simple_lock>::set(class vostok::resources::managed_resource *)`
- `private: void __thiscall vostok::intrusive_ptr<class vostok::sound::encoded_sound_interface, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock>::set(class vostok::intrusive_ptr<class vostok::sound::encoded_sound_interface, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock> const &)`
- `private: void __thiscall vostok::sound::new_sound_propagator::attach_voices(unsigned int, class vostok::vectora<struct vostok::sound::sound_voice_params> const &)`
- `private: void __thiscall vostok::sound::new_sound_propagator::detach_voice(class vostok::sound::sound_voice *)`
- `private: void __thiscall vostok::sound::new_sound_propagator::detach_voices(unsigned int)`
- `private: void __thiscall vostok::sound::new_sound_propagator::set_voice_channel_matrix(class vostok::sound::sound_voice *, float const *, float)`
- `private: void __thiscall vostok::sound::ogg_encoded_sound_interface_cook::on_sub_resources_loaded(class vostok::resources::queries_result &)`
- `private: void __thiscall vostok::sound::ogg_file_contents_cook::on_sub_resources_loaded(class vostok::resources::queries_result &)`
- `private: void __thiscall vostok::sound::ogg_sound_cook::on_sub_resources_loaded(class vostok::resources::queries_result &)`
- `private: void __thiscall vostok::sound::ogg_source_cook::on_ogg_file_loaded(class vostok::resources::queries_result &, class vostok::resources::query_result_for_cook *)`
- `private: void __thiscall vostok::sound::single_sound_cook::on_sub_resources_loaded(class vostok::resources::queries_result &)`
- `private: void __thiscall vostok::sound::sound_environment_cook::on_environment_options_loaded(class vostok::resources::queries_result &, class vostok::math::float4x4*)`
- `private: void __thiscall vostok::sound::sound_environment_cook::on_model_config_loaded(class vostok::resources::queries_result &)`
- `private: void __thiscall vostok::sound::sound_scene::calculate_channel_matrix(class vostok::resources::resource_ptr<class vostok::sound::panning_lut, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::sound::sound_instance_proxy_internal const &, class vostok::math::float3const &, float, float, float *, float &) const`
- `private: void __thiscall vostok::sound::sound_scene::calculate_in_graph_position(class vostok::math::float3const &)`
- `private: void __thiscall vostok::sound::sound_scene::notify_listener(class vostok::sound::sound_world const &)`
- `private: void __thiscall vostok::sound::sound_scene::process_fade(class vostok::sound::sound_world &, unsigned __int64)`
- `private: void __thiscall vostok::sound::sound_scene::x3daudio_calculate(class vostok::sound::sound_world const &, class vostok::sound::sound_voice &)`
- `private: void __thiscall vostok::sound::sound_world::try_delete_stoping_voices(void)`
- `private: void __thiscall vostok::sound::wav_encoded_sound_interface::read_riff(void)`
- `private: void __thiscall vostok::sound::wav_encoded_sound_interface_cook::on_file_loaded(class vostok::resources::queries_result &)`
- `protected: __thiscall survarium::double_barreled_weapon_core_hide_state::double_barreled_weapon_core_hide_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int, bool &)`
- `protected: __thiscall survarium::double_barreled_weapon_core_show_state::double_barreled_weapon_core_show_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int, bool &)`
- `protected: __thiscall survarium::pistol_weapon_core_hide_state::pistol_weapon_core_hide_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int, bool &)`
- `protected: __thiscall survarium::pistol_weapon_core_show_state::pistol_weapon_core_show_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int, bool &)`
- `protected: __thiscall survarium::weapon_core_hide_state::weapon_core_hide_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int, bool &)`
- `protected: __thiscall survarium::weapon_core_hide_state_base::weapon_core_hide_state_base(class survarium::weapon_core &, bool &)`
- `protected: __thiscall survarium::weapon_core_show_state::weapon_core_show_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int, bool &)`
- `protected: __thiscall survarium::weapon_core_show_state_base::weapon_core_show_state_base(class survarium::weapon_core &, bool &)`
- `protected: class vostok::resources::resource_ptr<class survarium::booby_trap_core, class vostok::resources::unmanaged_intrusive_base> * __thiscall survarium::booby_trap_set_core::try_place_trap(void)`
- `protected: virtual void __thiscall survarium::booby_trap_set_core::remove(void)`
- `public: __thiscall survarium::body_part_parameters::body_part_parameters(char const *, float, float, float, bool, class survarium::damage_model &, unsigned char)`
- `public: __thiscall vostok::buffer_vector<class vostok::variant<32> const *>::buffer_vector<class vostok::variant<32> const *>(void *, unsigned int, unsigned int)`
- `public: __thiscall vostok::fixed_string<256>::fixed_string<256>(void)`
- `public: __thiscall vostok::fixed_string<64>::fixed_string<64>(class vostok::fixed_string<64> const &)`
- `public: __thiscall vostok::memory::single_size_buffer_allocator<108, class vostok::threading::single_threading_policy>::single_size_buffer_allocator<108, class vostok::threading::single_threading_policy>(void *, unsigned int)`
- `public: __thiscall vostok::memory::single_size_buffer_allocator<136, class vostok::threading::single_threading_policy>::single_size_buffer_allocator<136, class vostok::threading::single_threading_policy>(void *, unsigned int)`
- `public: __thiscall vostok::memory::single_size_buffer_allocator<28, class vostok::threading::single_threading_policy>::single_size_buffer_allocator<28, class vostok::threading::single_threading_policy>(void *, unsigned int)`
- `public: __thiscall vostok::particle::curve_line_ranged_float::curve_line_ranged_float(void)`
- `public: __thiscall vostok::render::cascaded_sun_shadow_statistics_group::~cascaded_sun_shadow_statistics_group(void)`
- `public: __thiscall vostok::render::debug_statistics_group::~debug_statistics_group(void)`
- `public: __thiscall vostok::render::lpv_statistics_group::~lpv_statistics_group(void)`
- `public: __thiscall vostok::render::particles_statistics_group::~particles_statistics_group(void)`
- `public: __thiscall vostok::render::visibility_statistics_group::~visibility_statistics_group(void)`
- `public: __thiscall vostok::resources::resource_ptr<class survarium::game_world_object, class vostok::resources::unmanaged_intrusive_base>::resource_ptr<class survarium::game_world_object, class vostok::resources::unmanaged_intrusive_base>(class survarium::game_world_object *)`
- `public: __thiscall vostok::resources::resource_ptr<class vostok::sound::panning_lut, class vostok::resources::unmanaged_intrusive_base>::resource_ptr<class vostok::sound::panning_lut, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::resource_ptr<class vostok::sound::panning_lut, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: __thiscall vostok::sound::effect_cross_fader::effect_cross_fader(class vostok::sound::sound_scene &, unsigned int, struct IXAudio2SubmixVoice *, struct IXAudio2SubmixVoice *)`
- `public: __thiscall vostok::sound::new_sound_propagator::new_sound_propagator(class vostok::math::float3const &, class vostok::math::float3const &, enum vostok::sound::playback_mode, unsigned int, unsigned int, unsigned int, unsigned int, class vostok::sound::sound_instance_proxy_internal &, class vostok::sound::sound_propagator_emitter const &)`
- `public: __thiscall vostok::sound::ogg_encoded_sound_interface::ogg_encoded_sound_interface(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>)`
- `public: __thiscall vostok::sound::ogg_file_contents::ogg_file_contents(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>)`
- `public: __thiscall vostok::sound::ogg_file_contents_cook::ogg_file_contents_cook(void)`
- `public: __thiscall vostok::sound::ogg_sound::ogg_sound(class vostok::resources::resource_ptr<class vostok::sound::ogg_file_contents, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &)`
- `public: __thiscall vostok::sound::ogg_sound_cook::ogg_sound_cook(void)`
- `public: __thiscall vostok::sound::ogg_source_cook::ogg_source_cook(void)`
- `public: __thiscall vostok::sound::single_sound::single_sound(class vostok::resources::resource_ptr<class vostok::sound::encoded_sound_with_qualities, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::sound::sound_spl, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: __thiscall vostok::sound::sound_environment::sound_environment(unsigned int)`
- `public: __thiscall vostok::sound::sound_environment_cook::sound_environment_cook(void)`
- `public: __thiscall vostok::sound::sound_voice::sound_voice(int, unsigned int, unsigned int, class vostok::sound::sound_instance_proxy_internal &, class vostok::sound::sound_propagator_emitter const &, class vostok::resources::resource_ptr<class vostok::sound::sound_spl, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: __thiscall vostok::sound::unique_propagator_info::unique_propagator_info(void)`
- `public: __thiscall vostok::sound::voice_factory::voice_factory(unsigned char *, unsigned int, class vostok::sound::sound_world const &, struct vostok::sound::pool_parametrs const &)`
- `public: __thiscall vostok::sound::wav_encoded_sound_interface::wav_encoded_sound_interface(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>)`
- `public: __thiscall vostok::sound::wav_encoded_sound_interface_cook::wav_encoded_sound_interface_cook(void)`
- `public: __thiscall vostok::vectora_allocator<struct vostok::sound::propagator_info>::ctor<void *>(class vostok::vectora_allocator<void *> const &)`
- `public: bool __thiscall survarium::body_part_parameters::can_affect_death(void)`
- `public: bool __thiscall survarium::player_input_handler::alt_is_held(void) const`
- `public: bool __thiscall survarium::weapon_core_base_state::has_animation_ended(void) const`
- `public: bool __thiscall vostok::intrusive_list<class vostok::particle::particle_emitter_instance, class vostok::particle::particle_emitter_instance *, 224, class vostok::threading::single_threading_policy, class vostok::size_policy, class vostok::no_debug_policy>::erase(class vostok::particle::particle_emitter_instance *)`
- `public: bool __thiscall vostok::intrusive_list<class vostok::sound::sound_voice, class vostok::sound::sound_voice *, 0, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::erase(class vostok::sound::sound_voice *)`
- `public: bool __thiscall vostok::sound::sound_voice::can_be_deleted(void) const`
- `public: class vostok::intrusive_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock> & __thiscall vostok::intrusive_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock>::operator=(class vostok::intrusive_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock> const &)`
- `public: class vostok::render::effect_compiler & __thiscall vostok::render::effect_compiler::begin_pass(char const *, char const *, char const *, struct vostok::render::shader_configuration const &, struct vostok::render::shader_include_getter *)`
- `public: class vostok::sound::sound_environment * __thiscall vostok::sound::sound_scene::get_current_environment(void)`
- `public: class vostok::sound::sound_voice * __thiscall vostok::sound::sound_world::create_sound_voice(class vostok::sound::sound_scene &, int, unsigned int, unsigned int, class vostok::sound::sound_instance_proxy_internal *, class vostok::sound::sound_propagator_emitter const &, class vostok::resources::resource_ptr<class vostok::sound::sound_spl, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: float __thiscall vostok::animation::cubic_spline_skeleton_animation::length_in_frames(void) const`
- `public: float __thiscall vostok::sound::sound_spl::get_loudness(float) const`
- `public: static union vostok::memory::single_size_buffer_allocator<108, class vostok::threading::single_threading_policy>::node * __cdecl vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<108, class vostok::threading::single_threading_policy>::node>::allocate(class vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<108, class vostok::threading::single_threading_policy>::node>::free_list_type &)`
- `public: static union vostok::memory::single_size_buffer_allocator<136, class vostok::threading::single_threading_policy>::node * __cdecl vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<136, class vostok::threading::single_threading_policy>::node>::allocate(class vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<136, class vostok::threading::single_threading_policy>::node>::free_list_type &)`
- `public: static union vostok::memory::single_size_buffer_allocator<28, class vostok::threading::single_threading_policy>::node * __cdecl vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<28, class vostok::threading::single_threading_policy>::node>::allocate(class vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<28, class vostok::threading::single_threading_policy>::node>::free_list_type &)`
- `public: static unsigned int __cdecl vostok::detail::type_to_int<struct vostok::particle::world *>::get(void)`
- `public: struct IXAudio2SubmixVoice * __thiscall vostok::sound::sound_scene::get_current_effect_submix(void)`
- `public: struct XAUDIO2FX_REVERB_I3DL2_PARAMETERS * __thiscall vostok::sound::sound_scene::get_environment_params(char const *)`
- `public: struct XAUDIO2FX_REVERB_I3DL2_PARAMETERS * __thiscall vostok::sound::sound_scene::get_environment_params(unsigned int)`
- `public: struct vostok::particle::world & __thiscall vostok::render::engine::world::particle_world(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: struct vostok::particle::world & __thiscall vostok::render::scene_renderer::particle_world(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: unsigned char __thiscall survarium::damage_model::get_total_health(void)`
- `public: unsigned int __thiscall vostok::sound::ogg_file_contents::decompress(unsigned char *, unsigned int, unsigned int &, unsigned int)`
- `public: unsigned int __thiscall vostok::sound::sound_scene::get_environment_params_id(char const *)`
- `public: virtual __thiscall vostok::ai::selectors::sound_target_selector::~sound_target_selector(void)`
- `public: virtual __thiscall vostok::resources::fs_task_unmount::~fs_task_unmount(void)`
- `public: virtual __thiscall vostok::sound::ogg_file_contents::~ogg_file_contents(void)`
- `public: virtual __thiscall vostok::sound::ogg_file_contents_cook::~ogg_file_contents_cook(void)`
- `public: virtual __thiscall vostok::sound::ogg_sound::~ogg_sound(void)`
- `public: virtual __thiscall vostok::sound::ogg_sound_cook::~ogg_sound_cook(void)`
- `public: virtual __thiscall vostok::sound::sound_environment::~sound_environment(void)`
- `public: virtual __thiscall vostok::sound::wav_encoded_sound_interface::~wav_encoded_sound_interface(void)`
- `public: virtual __thiscall vostok::sound::wav_encoded_sound_interface_cook::~wav_encoded_sound_interface_cook(void)`
- `public: virtual class vostok::detail::abstract_type_helper * __thiscall vostok::detail::concrete_type_helper<struct vostok::particle::world *>::copy_helper(class vostok::mutable_buffer)`
- `public: virtual unsigned int __thiscall vostok::sound::wav_encoded_sound_interface::decompress(unsigned char *, unsigned int, unsigned int &, unsigned int)`
- `public: virtual void __thiscall vostok::sound::ogg_file_contents_cook::delete_resource(class vostok::resources::resource_base *)`
- `public: virtual void __thiscall vostok::sound::ogg_file_contents_cook::translate_query(class vostok::resources::query_result_for_cook &)`
- `public: virtual void __thiscall vostok::sound::ogg_sound_cook::delete_resource(class vostok::resources::resource_base *)`
- `public: virtual void __thiscall vostok::sound::ogg_sound_cook::translate_query(class vostok::resources::query_result_for_cook &)`
- `public: virtual void __thiscall vostok::sound::ogg_source_cook::delete_resource(class vostok::resources::resource_base *)`
- `public: virtual void __thiscall vostok::sound::ogg_source_cook::translate_query(class vostok::resources::query_result_for_cook &)`
- `public: virtual void __thiscall vostok::sound::sound_environment_cook::delete_resource(class vostok::resources::resource_base *)`
- `public: virtual void __thiscall vostok::sound::sound_environment_cook::translate_query(class vostok::resources::query_result_for_cook &)`
- `public: virtual void __thiscall vostok::sound::wav_encoded_sound_interface_cook::delete_resource(class vostok::resources::resource_base *)`
- `public: virtual void __thiscall vostok::sound::wav_encoded_sound_interface_cook::translate_query(class vostok::resources::query_result_for_cook &)`
- `public: void * __thiscall vostok::memory::single_size_buffer_allocator<108, class vostok::threading::single_threading_policy>::allocate(void)`
- `public: void * __thiscall vostok::memory::single_size_buffer_allocator<136, class vostok::threading::single_threading_policy>::malloc_impl(unsigned int)`
- `public: void * __thiscall vostok::memory::single_size_buffer_allocator<28, class vostok::threading::single_threading_policy>::allocate(void)`
- `public: void __thiscall survarium::game_world_ui::initialize_resources(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: void __thiscall survarium::std_allocator<struct survarium::base_project::resolve_link_object>::deallocate(struct survarium::base_project::resolve_link_object *, unsigned int) const`
- `public: void __thiscall vostok::ai::fsm::add_transition(struct vostok::ai::fsm_state *, struct vostok::ai::fsm_state *, class boost::function<bool __cdecl (void)> const &)`
- `public: void __thiscall vostok::intrusive_list<class vostok::particle::particle_emitter_instance, class vostok::particle::particle_emitter_instance *, 224, class vostok::threading::single_threading_policy, class vostok::size_policy, class vostok::no_debug_policy>::push_back(class vostok::particle::particle_emitter_instance *, bool *)`
- `public: void __thiscall vostok::intrusive_list<class vostok::sound::sound_voice, class vostok::sound::sound_voice *, 0, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::push_back(class vostok::sound::sound_voice *, bool *)`
- `public: void __thiscall vostok::render::grass_patch::try_accumulate_trample(struct vostok::render::trample_desc &, struct vostok::render::grass_world *, class vostok::render::renderer *, class vostok::render::renderer_context *)`
- `public: void __thiscall vostok::render::scene::build_lpv_geometry(void)`
- `public: void __thiscall vostok::sound::effect_cross_fader::tick(unsigned int, class vostok::sound::sound_environment *)`
- `public: void __thiscall vostok::sound::new_sound_propagator::distribute_voices(unsigned int, class vostok::vectora<struct vostok::sound::sound_voice_params> const &)`
- `public: void __thiscall vostok::sound::sound_instance_proxy_internal::tick(unsigned int)`
- `public: void __thiscall vostok::sound::sound_scene::add_environment_params(char const *, struct XAUDIO2FX_REVERB_I3DL2_PARAMETERS *, unsigned int &)`
- `public: void __thiscall vostok::sound::sound_scene::insert_environment(class vostok::sound::sound_environment &, class vostok::math::float4x4const &)`
- `public: void __thiscall vostok::sound::sound_scene::tick(class vostok::sound::sound_world &, unsigned int)`
- `public: void __thiscall vostok::sound::voice_bridge::set_channel_volumes(unsigned char, float const *)`
- `public: void __thiscall vostok::sound::voice_bridge::set_sample_rate(unsigned int)`
- `public: void __thiscall vostok::variant<32>::set<struct vostok::render::static_model_instance_user_data>(struct vostok::render::static_model_instance_user_data const &)`
- `void __cdecl vostok::debug::platform::terminate(char const *, int)`
- `void __cdecl vostok::memory::delete_helper<class vostok::memory::doug_lea_allocator, class vostok::render::light const>(class vostok::memory::doug_lea_allocator &, class vostok::render::light const *&)`
- `void __cdecl vostok::memory::detail::delete_helper_impl<class vostok::memory::doug_lea_allocator, class vostok::math::float4x4, struct vostok::memory::detail::call_destructor_predicate>(class vostok::memory::doug_lea_allocator &, class vostok::math::float4x4*&, struct vostok::memory::detail::call_destructor_predicate const &)`
- `void __cdecl vostok::memory::detail::delete_helper_impl<class vostok::memory::doug_lea_allocator, struct vostok::sound::propagator_statistic, struct vostok::memory::detail::call_destructor_predicate>(class vostok::memory::doug_lea_allocator &, struct vostok::sound::propagator_statistic *&, struct vostok::memory::detail::call_destructor_predicate const &)`
- `void __cdecl vostok::memory::detail::delete_helper_impl<class vostok::memory::single_size_buffer_allocator<108, class vostok::threading::single_threading_policy>, class vostok::sound::new_sound_propagator, struct vostok::memory::detail::call_destructor_predicate>(class vostok::memory::single_size_buffer_allocator<108, class vostok::threading::single_threading_policy> &, class vostok::sound::new_sound_propagator *&, struct vostok::memory::detail::call_destructor_predicate const &)`
- `void __cdecl vostok::memory::detail::delete_helper_impl<class vostok::memory::single_size_buffer_allocator<136, class vostok::threading::single_threading_policy>, class vostok::sound::sound_voice, struct vostok::memory::detail::call_destructor_predicate>(class vostok::memory::single_size_buffer_allocator<136, class vostok::threading::single_threading_policy> &, class vostok::sound::sound_voice *&, struct vostok::memory::detail::call_destructor_predicate const &)`
- `void __cdecl vostok::memory::detail::delete_helper_impl<class vostok::memory::single_size_buffer_allocator<28, class vostok::threading::single_threading_policy>, class vostok::sound::voice_bridge, struct vostok::memory::detail::call_destructor_predicate>(class vostok::memory::single_size_buffer_allocator<28, class vostok::threading::single_threading_policy> &, class vostok::sound::voice_bridge *&, struct vostok::memory::detail::call_destructor_predicate const &)`
- `vostok::sound::compare_propagator_info_by_distance`

---

## v0.1.1c-build870 → v0.1.1e-build884
_2013-05-24 → 2013-05-28 · +25 / -38 / ~473_

### Changed (473)

| match % | function |
| ---: | --- |
| 0.00 | `long __cdecl vostok::threading::interlocked_decrement(long volatile &)` |
| 0.00 | `long __cdecl vostok::threading::interlocked_increment(long volatile &)` |
| 0.00 | `public: __thiscall btSoftBody::Body::Body(void)` |
| 0.00 | `public: __thiscall vostok::ai::pre_perceptors_filter::~pre_perceptors_filter(void)` |
| 0.00 | `public: __thiscall vostok::animation::mixing::animation_interval::~animation_interval(void)` |
| 0.00 | `public: __thiscall vostok::intrusive_list<struct vostok::ai::percept_memory_object, struct vostok::ai::percept_memory_object *, 40, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::~intrusive_list<struct vostok::ai::percept_memory_object, struct vostok::ai::percept_memory_object *, 40, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>(void)` |
| 0.00 | `public: __thiscall vostok::network::order::order(void)` |
| 0.00 | `public: __thiscall vostok::one_way_threads_channel<class vostok::intrusive_spsc_queue<class vostok::network::order, class vostok::network::order, 4>, class vostok::intrusive_spsc_queue<class vostok::network::order, class vostok::network::order, 4> >::~one_way_threads_channel<class vostok::intrusive_spsc_queue<class vostok::network::order, class vostok::network::order, 4>, class vostok::intrusive_spsc_queue<class vostok::network::order, class vostok::network::order, 4> >(void)` |
| 0.00 | `public: __thiscall vostok::render::skeleton_combined_cook_data::~skeleton_combined_cook_data(void)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::render::material, class vostok::resources::unmanaged_intrusive_base>::~resource_ptr<class vostok::render::material, class vostok::resources::unmanaged_intrusive_base>(void)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::unmanaged_resource *)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>::~resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>(void)` |
| 0.00 | `public: __thiscall vostok::vectora<struct vostok::resources::request>::~vectora<struct vostok::resources::request>(void)` |
| 0.00 | `public: __thiscall vostok::vfs::query_mount_arguments::~query_mount_arguments(void)` |
| 0.00 | `public: class survarium::inventory & __thiscall survarium::inventory_holder::inventory(void)` |
| 0.00 | `public: class vostok::buffer_string const & __thiscall vostok::buffer_string::operator=(class vostok::buffer_string const &)` |
| 0.00 | `public: class vostok::vfs::query_mount_arguments & __thiscall vostok::vfs::query_mount_arguments::operator=(class vostok::vfs::query_mount_arguments const &)` |
| 0.00 | `public: enum survarium::profile_slot_enum __thiscall survarium::inventory::get_active_slot(void) const` |
| 0.00 | `public: virtual __thiscall survarium::inventory_cook::~inventory_cook(void)` |
| 0.00 | `public: virtual __thiscall vostok::console_commands::cc_u32::~cc_u32(void)` |
| 0.00 | `public: virtual void __thiscall survarium::game_camera::on_focus(bool)` |
| 0.00 | `vec_begin` |
| 2.05 | `public: void __thiscall vostok::render::system_renderer::draw_screen_lines(class vostok::math::float3const *, unsigned int, class vostok::math::color const &, float, unsigned int, bool, bool)` |
| 12.00 | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 12.77 | `public: bool __thiscall vostok::render::remove_inappropriate_models::operator()(struct vostok::render::render_surface_instance *)` |
| 13.45 | `vostok::render::screen_factor` |
| 33.66 | `private: __thiscall survarium::medkit::medkit(void)` |
| 53.74 | `public: void __thiscall vostok::resources::resources_manager::init_new_query(class vostok::resources::query_result &)` |
| 57.50 | `public: void __thiscall vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 608, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::push_back(class vostok::resources::query_result *, bool *)` |
| 60.23 | `public: virtual __thiscall vostok::resources::query_result_for_user::~query_result_for_user(void)` |
| 63.37 | `private: virtual void __thiscall survarium::network_client::close_current_match(enum vostok::network_core::disconnect_event_types_enum)` |
| 73.70 | `public: virtual float __thiscall survarium::dz_bone_data_contact_test_predicate::add_single_result(void *, enum vostok::physics::primitive_type, class vostok::math::float4x4const &, class vostok::math::float3const &, enum vostok::physics::primitive_type, class vostok::math::float4x4const &, class vostok::math::float3const &)` |
| 77.34 | `private: void __thiscall vostok::render::device::create_d3d(void)` |
| 79.82 | `public: void __thiscall survarium::lobby_menu::on_player_reputations_arrived(void)` |
| 83.83 | `private: void __thiscall survarium::application::preinitialize(void)` |
| 84.42 | `public: virtual void __thiscall vostok::render::stage_postprocess::execute(void)` |
| 85.24 | `public: virtual void __thiscall vostok::render::stage_shadow_direct::execute(void)` |
| 89.17 | `public: __thiscall vostok::resources::query_result_for_user::query_result_for_user(void)` |
| 90.08 | `public: __thiscall vostok::render::renderer_context::~renderer_context(void)` |
| 90.10 | `public: enum vostok::render::enum_options_changes_result __thiscall vostok::render::options::end_render_options_changing(class vostok::render::vector<class vostok::fs_new::virtual_path_string> &)` |
| 91.57 | `private: void __thiscall vostok::render::game::renderer::draw_scene_impl(struct vostok::render::game::renderer::draw_scene_params const &)` |
| 92.68 | `public: __thiscall vostok::render::renderer_context::renderer_context(void)` |
| 93.24 | `private: virtual __thiscall survarium::medkit::~medkit(void)` |
| 93.40 | `public: void __thiscall vostok::render::engine::world::draw_scene(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct vostok::render::base_scene_view, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct vostok::render::base_output_window, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::rectangle<class vostok::math::float2> const &, class boost::function<void __cdecl (bool)> const &, struct vostok::ui::font const *)` |
| 94.75 | `public: void __thiscall vostok::render::renderer::render(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct vostok::render::base_scene_view, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct vostok::render::base_output_window, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::rectangle<class vostok::math::float2> const &, class boost::function<void __cdecl (bool)> const &, bool, struct vostok::ui::font const *)` |
| 95.08 | `public: void __thiscall vostok::render::options::set_default_values(void)` |
| 95.41 | `private: void __thiscall survarium::player::detect_usable_objects(unsigned int)` |
| 95.56 | `public: void __thiscall vostok::render::options::register_console_commands(void)` |
| 95.99 | `public: void __thiscall vostok::render::system_renderer::draw_ui_vertices(struct vostok::render::vertex_formats::TL const *, unsigned int const &, int, int)` |
| 96.25 | `public: void __thiscall vostok::render::render_particle_emitter_instance::draw_debug(class vostok::math::float4x4const &, enum vostok::particle::enum_particle_render_mode)` |
| 97.23 | `public: void __thiscall vostok::resources::resources_manager::init_new_queries(class vostok::resources::query_result *)` |
| 98.57 | `public: void __thiscall survarium::game_world_ui::set_match_time(unsigned int)` |
| 99.01 | `private: void __thiscall vostok::render::device::create(void)` |
| 99.38 | `private: void __thiscall vostok::render::renderer_context::update_near_far(void)` |
| 99.44 | `public: __thiscall vostok::resources::query_result_for_cook::query_result_for_cook(class vostok::resources::queries_result *)` |
| 99.50 | `private: void __thiscall vostok::resources::query_result::add_loaded_bytes(unsigned int)` |
| 99.50 | `public: class vostok::render::scene_view * __thiscall vostok::render::renderer_context::get_scene_view(void)` |
| 99.50 | `public: class vostok::render::scene_view const * __thiscall vostok::render::renderer_context::scene_view(void) const` |
| 99.50 | `public: void __thiscall vostok::render::renderer_context::set_scene(class vostok::render::scene *)` |
| 99.50 | `public: void __thiscall vostok::resources::query_result_for_cook::set_out_of_memory(class vostok::resources::memory_type &, unsigned int)` |
| 99.54 | `private: void __thiscall vostok::resources::query_result::clear_reference(void)` |
| 99.60 | `public: void __thiscall vostok::render::renderer_context::reset_matrices(void)` |
| 99.62 | `public: __thiscall vostok::resources::query_result::query_result(unsigned short, class vostok::resources::queries_result *, class vostok::memory::base_allocator *, unsigned int, float, bool, unsigned int, enum vostok::resources::query_type_enum, enum vostok::resources::autoselect_quality_bool)` |
| 99.67 | `public: class vostok::resources::query_result_for_cook * __thiscall vostok::resources::query_result_for_cook::get_parent_query(void) const` |
| 99.67 | `public: class vostok::resources::query_result_for_user const & __thiscall vostok::resources::queries_result::operator[](unsigned int) const` |
| 99.68 | `public: void __thiscall vostok::render::renderer_context::update_eye_rays(void)` |
| 99.69 | `public: __thiscall vostok::render::stage_light_propagation_volumes::stage_light_propagation_volumes(class vostok::render::renderer *, class vostok::render::renderer_context *)` |
| 99.73 | `private: void __thiscall vostok::resources::query_result::prepare_requery(void)` |
| 99.73 | `public: class vostok::math::float4x4const & __thiscall vostok::render::renderer_context::get_view2shadow(unsigned int) const` |
| 99.75 | `private: void __thiscall vostok::resources::query_result::increase_query_end_guard(void)` |
| 99.75 | `private: void __thiscall vostok::resources::query_result::on_observed_resource_destroyed(char const *)` |
| 99.75 | `public: class vostok::resources::query_result_for_user & __thiscall vostok::resources::queries_result::operator[](unsigned int)` |
| 99.78 | `private: bool __thiscall vostok::resources::query_result::ready_to_retry_action_that_caused_out_of_memory(void)` |
| 99.79 | `public: __thiscall singletons_on_initialize::singletons_on_initialize(void)` |
| 99.80 | `private: unsigned int __thiscall vostok::resources::query_result::decrease_query_end_guard(void)` |
| 99.80 | `public: bool __thiscall vostok::resources::query_result_for_cook::is_autoselect_quality_query(void) const` |
| 99.80 | `public: virtual class vostok::mutable_buffer __thiscall vostok::resources::vfs_sub_fat_cook::allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)` |
| 99.81 | `public: void __thiscall vostok::render::renderer_context::push_set_p(class vostok::math::float4x4const &)` |
| 99.82 | `private: bool __thiscall vostok::resources::queries_result::quality_loaded(unsigned int)` |
| 99.82 | `private: void __thiscall vostok::resources::query_result::requery(void)` |
| 99.82 | `public: virtual void __thiscall vostok::resources::vfs_sub_fat_cook::create_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, class vostok::mutable_buffer)` |
| 99.83 | `private: void __thiscall vostok::resources::query_result::observe_resource_destruction(class vostok::resources::resource_base *)` |
| 99.83 | `private: void __thiscall vostok::resources::query_result::set_flag(unsigned int)` |
| 99.83 | `public: bool __thiscall vostok::resources::query_result_for_cook::is_helper_query_for_mount(void) const` |
| 99.83 | `public: void __thiscall vostok::render::renderer_context::clear_resources(void)` |
| 99.85 | `public: void __thiscall vostok::render::temporal_projection_matrix_modifier::pop_jittering(void)` |
| 99.86 | `private: bool __thiscall vostok::resources::game_resources_manager::try_reallocate_queue_front(class vostok::resources::memory_type *)` |
| 99.86 | `public: void __thiscall vostok::render::renderer::clear_resources(void)` |
| 99.87 | `private: void __thiscall vostok::resources::query_result::propogate_sub_fats_to_resources(void)` |
| 99.87 | `private: void __thiscall vostok::resources::query_result::init_save(class vostok::resources::save_generated_data *, class vostok::resources::query_result *)` |
| 99.87 | `public: void __thiscall vostok::render::renderer_context::set_v(class vostok::math::float4x4const &)` |
| 99.88 | `private: void __thiscall vostok::resources::query_result::unset_flag(unsigned int)` |
| 99.88 | `public: virtual __thiscall vostok::resources::query_result_for_cook::~query_result_for_cook(void)` |
| 99.88 | `public: void __thiscall vostok::render::engine::world::clear_resources(void)` |
| 99.88 | `public: void __thiscall vostok::render::renderer_context::set_w(class vostok::math::float4x4const &)` |
| 99.88 | `private: void __thiscall vostok::resources::query_result::on_refered_query_ended(class vostok::resources::query_result *)` |
| 99.89 | `private: bool __thiscall vostok::resources::game_resources_manager::try_free_or_decrease_quality(class vostok::resources::query_result *, class vostok::resources::memory_type *)` |
| 99.89 | `public: void __thiscall vostok::render::renderer_context::set_view2shadow(class vostok::math::float4x4const &, unsigned int)` |
| 99.89 | `public: bool __thiscall vostok::render::ambient_volume::is_occluded(void) const` |
| 99.89 | `public: bool __thiscall vostok::render::decal_instance::is_occluded(void) const` |
| 99.89 | `public: bool __thiscall vostok::render::environment_probe::is_occluded(void) const` |
| 99.89 | `public: bool __thiscall vostok::render::grass_patch::is_occluded(void) const` |
| 99.89 | `public: bool __thiscall vostok::render::light::is_occluded(void) const` |
| 99.89 | `public: bool __thiscall vostok::render::render_surface_instance::is_occluded(void) const` |
| 99.89 | `public: enum assert_on_fail_bool __thiscall vostok::resources::query_result_for_cook::assert_on_fail(void) const` |
| 99.89 | `public: virtual bool __thiscall vostok::render::render_particle_emitter_instance::is_occluded(void) const` |
| 99.89 | `public: void __thiscall vostok::render::world::clear_resources(void)` |
| 99.89 | `private: void __thiscall vostok::resources::resources_manager::dispatch_tasks_finished_callback(class vostok::resources::query_result *, bool)` |
| 99.89 | `private: void __thiscall vostok::resources::query_result::on_create_resource_end(void)` |
| 99.90 | `public: void __thiscall vostok::render::renderer_context::set_p(class vostok::math::float4x4const &)` |
| 99.90 | `private: bool __thiscall vostok::resources::query_result::end_query_might_destroy_this(void)` |
| 99.90 | `public: virtual bool __thiscall vostok::resources::fs_task_iterator::is_helper_query_for_mount(void) const` |
| 99.90 | `vostok::render::is_occluded_predicate<vostok::render::ambient_volume>` |
| 99.90 | `vostok::render::is_occluded_predicate<vostok::render::decal_instance>` |
| 99.90 | `vostok::render::is_occluded_predicate<vostok::render::environment_probe>` |
| 99.90 | `vostok::render::is_occluded_predicate<vostok::render::grass_patch>` |
| 99.90 | `vostok::render::is_occluded_predicate<vostok::render::render_surface_instance>` |
| 99.90 | `private: void __thiscall vostok::resources::queries_result::mark_inconsistent_qualities_as_failed(void)` |
| 99.91 | `private: void __thiscall vostok::resources::query_result::on_save_operation_end(void)` |
| 99.91 | `private: void __thiscall vostok::render::stage_gbuffer::render_grass(bool)` |
| 99.91 | `private: void __thiscall vostok::resources::query_result::set_create_resource_result(enum vostok::resources::cook_base::result_enum, enum vostok::resources::query_result_for_user::error_type_enum)` |
| 99.91 | `public: void __thiscall vostok::resources::query_result_for_cook::clear_user_data(void)` |
| 99.91 | `vostok::render::is_occluded_predicate_light` |
| 99.91 | `public: virtual __thiscall vostok::resources::query_result::~query_result(void)` |
| 99.91 | `private: void __thiscall vostok::render::speedtree_forest::cull_and_compute_lod(class vostok::render::renderer_context *, class vostok::math::float3const &, bool)` |
| 99.91 | `private: void __thiscall vostok::resources::query_result::unpin_raw_file(class vostok::const_buffer const &)` |
| 99.92 | `public: void __thiscall vostok::resources::resources_manager::push_new_query(class vostok::resources::query_result *)` |
| 99.92 | `public: void __thiscall vostok::render::system_renderer::draw_particle_system_instance_selections(class vostok::render::vector<class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> > const &)` |
| 99.92 | `private: bool __thiscall vostok::resources::game_resources_manager::try_reallocate_queue(class vostok::resources::memory_type *)` |
| 99.92 | `private: void __thiscall vostok::render::stage_gbuffer::render_particles(bool)` |
| 99.92 | `public: virtual void __thiscall vostok::render::stage_particles::execute(void)` |
| 99.92 | `private: void __thiscall vostok::resources::query_result::bind_unmanaged_resource_buffer_to_creation_or_inline_data(void)` |
| 99.92 | `private: void __thiscall vostok::resources::query_result::lock_fat_it(void)` |
| 99.92 | `private: void __thiscall vostok::resources::query_result::unlock_fat_it(void)` |
| 99.93 | `private: class vostok::vfs::vfs_iterator __thiscall vostok::resources::query_result::get_fat_it_zero_if_physical_path_it(void) const` |
| 99.93 | `private: void __thiscall vostok::resources::resources_manager::remove_from_generate_if_no_file_queue(class vostok::resources::query_result &)` |
| 99.93 | `public: virtual class vostok::mutable_buffer __thiscall survarium::weapon_core_inactive_state_cook::allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)` |
| 99.93 | `public: virtual class vostok::mutable_buffer __thiscall survarium::weapon_core_shotgun_reload_state_cook::allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)` |
| 99.93 | `private: void __thiscall vostok::render::stage_lights::render_particle_lighting(class vostok::render::render_particle_emitter_instance *, class vostok::render::light *, unsigned int)` |
| 99.93 | `private: void __thiscall vostok::resources::query_result::on_request_iterator_ready(class vostok::vfs::vfs_iterator &, bool)` |
| 99.93 | `private: bool __thiscall vostok::resources::query_result::need_create_resource_if_no_file(void)` |
| 99.93 | `private: void __thiscall vostok::resources::query_result::on_decompressing_end(void)` |
| 99.93 | `public: virtual float __thiscall vostok::resources::query_result_for_cook::satisfaction_with(unsigned int) const` |
| 99.93 | `private: void __thiscall vostok::resources::query_result::finish_normal_query(enum vostok::resources::cook_base::result_enum)` |
| 99.94 | `private: void __thiscall vostok::resources::query_result::free_unmanaged_buffer(void)` |
| 99.94 | `public: virtual class vostok::mutable_buffer __thiscall vostok::particle::particle_system_cook::allocate_resource(class vostok::resources::query_result_for_cook &, unsigned int, unsigned int &, bool)` |
| 99.94 | `vostok::render::fill_surface` |
| 99.94 | `private: enum vostok::resources::allocation_result_enum __thiscall vostok::resources::query_result::allocate_compressed_resource_if_needed(void)` |
| 99.94 | `private: void __thiscall vostok::resources::resources_manager::add_to_generate_if_no_file_queue(class vostok::resources::query_result &)` |
| 99.94 | `private: bool __thiscall vostok::resources::query_result::retry_action_that_caused_out_of_memory(void)` |
| 99.94 | `private: void __thiscall vostok::render::stage_lights::render_model_lighting(struct vostok::render::render_surface_instance *, class vostok::render::light *)` |
| 99.94 | `private: void __thiscall vostok::render::stage_lights::render_speedtree_lighting(struct vostok::render::lod_entry const *, class SpeedTree::CInstance const *, struct SpeedTree::SInstanceLod const *, class vostok::render::speedtree_tree_component *, class vostok::render::light *)` |
| 99.94 | `private: void __thiscall vostok::render::stage_lights::render_to_hw_shadowmap(class vostok::render::light *, unsigned int, float, unsigned int, unsigned int, class vostok::math::float4x4const &, class vostok::math::float4x4const &, unsigned int)` |
| 99.94 | `private: void __thiscall vostok::resources::query_result::on_file_operation_end(class vostok::resources::query_result *)` |
| 99.94 | `public: virtual class vostok::mutable_buffer __thiscall vostok::core::configs::binary_config_cook_impl::allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)` |
| 99.94 | `public: void __thiscall vostok::render::temporal_projection_matrix_modifier::push_jittering(void)` |
| 99.94 | `public: virtual void __thiscall vostok::render::stage_accumulate_distortion::execute(void)` |
| 99.94 | `private: unsigned int __thiscall vostok::resources::queries_result::calculate_fs_iterator_requests_count(void)` |
| 99.94 | `private: unsigned int __thiscall vostok::resources::query_result::allocate_thread_id(void) const` |
| 99.94 | `private: unsigned int __thiscall vostok::resources::query_result::translate_thread_id(void) const` |
| 99.94 | `vostok::render::is_not_occluded_predicate<vostok::render::ambient_volume>` |
| 99.94 | `vostok::render::is_not_occluded_predicate<vostok::render::decal_instance>` |
| 99.94 | `vostok::render::is_not_occluded_predicate<vostok::render::environment_probe>` |
| 99.94 | `vostok::render::is_not_occluded_predicate<vostok::render::grass_patch>` |
| 99.94 | `vostok::render::is_not_occluded_predicate<vostok::render::render_surface_instance>` |
| 99.95 | `private: void __thiscall vostok::render::stage_lights::render_particle_probe_lighting(class vostok::render::render_particle_emitter_instance *, struct vostok::render::environment_probe *, unsigned int)` |
| 99.95 | `private: void __thiscall vostok::resources::query_result::do_unmanaged_create_resource(class vostok::resources::unmanaged_cook *)` |
| 99.95 | `private: void __thiscall vostok::resources::query_result::set_result_iterator(class vostok::vfs::vfs_locked_iterator const &)` |
| 99.95 | `vostok::render::is_not_occluded_predicate_light` |
| 99.95 | `private: void __thiscall survarium::medkit::load(class vostok::configs::binary_config_value)` |
| 99.95 | `private: class vostok::math::float4x4 __thiscall vostok::render::stage_pre_rain::render_rain_shadow_map(void)` |
| 99.95 | `public: void __thiscall vostok::render::speedtree_forest::tick(class vostok::render::renderer_context *)` |
| 99.95 | `private: bool __thiscall vostok::resources::device_manager::pre_allocate(class vostok::resources::query_result *)` |
| 99.95 | `private: bool __thiscall vostok::resources::queries_result::calculate_result_from_children(void)` |
| 99.95 | `private: void __thiscall vostok::render::stage_visibility::gather_statistics(void) const` |
| 99.95 | `private: void __thiscall vostok::resources::query_result::do_inplace_unmanaged_create_resource(class vostok::resources::inplace_unmanaged_cook *)` |
| 99.95 | `public: void __thiscall vostok::render::renderer::sort_models_by_distance(class vostok::render::vector<struct vostok::render::render_surface_instance *> &, bool)` |
| 99.95 | `private: void __thiscall vostok::resources::query_result::set_deleter_object(class vostok::resources::unmanaged_resource *)` |
| 99.95 | `private: void __thiscall vostok::resources::query_result::copy_data_to_resource(class vostok::const_buffer)` |
| 99.96 | `private: void __thiscall vostok::resources::resources_manager::dispatch_decompressed_resources(void)` |
| 99.96 | `public: void __thiscall vostok::resources::resource_freeing_functionality::free_collected(void)` |
| 99.96 | `private: enum vostok::resources::allocation_result_enum __thiscall vostok::resources::query_result::allocate_raw_unmanaged_resource_if_needed(void)` |
| 99.96 | `private: void __thiscall vostok::render::stage_lights::render_light(class vostok::render::light *, bool)` |
| 99.96 | `private: void __thiscall vostok::resources::query_result::do_inplace_managed_create_resource(class vostok::resources::inplace_managed_cook *)` |
| 99.96 | `private: void __thiscall vostok::resources::query_result::add_referrer(class vostok::resources::query_result *, bool)` |
| 99.96 | `private: enum vostok::resources::allocation_result_enum __thiscall vostok::resources::query_result::allocate_final_managed_resource_if_needed(void)` |
| 99.96 | `private: enum vostok::resources::resource_base::creation_source_enum __thiscall vostok::resources::query_result::creation_source_for_resource(void)` |
| 99.96 | `private: void __thiscall vostok::resources::resources_manager::decompress_resource(class vostok::resources::query_result *)` |
| 99.96 | `public: void __thiscall vostok::resources::game_resources_manager::out_of_memory_callback(class vostok::resources::query_result *)` |
| 99.96 | `private: void __thiscall vostok::resources::query_result::end_query_might_destroy_this_impl(void)` |
| 99.96 | `public: virtual void __thiscall vostok::sound::panning_lut_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 99.96 | `public: void __thiscall vostok::render::grass_world::render(class vostok::render::renderer_context *, class vostok::math::float3const &, enum vostok::render::enum_render_stage_type, unsigned int, float, bool, class vostok::render::res_effect *, bool, unsigned int)` |
| 99.96 | `private: enum vostok::resources::allocation_result_enum __thiscall vostok::resources::query_result::allocate_raw_managed_resource_if_needed(void)` |
| 99.96 | `private: void __thiscall vostok::resources::allocate_functionality::allocate_raw_resources(class vostok::resources::thread_local_data *, bool)` |
| 99.96 | `private: void __thiscall vostok::resources::query_result::requery_on_out_of_memory(void)` |
| 99.96 | `private: void __thiscall vostok::resources::query_result::unpin_compressed_file(class vostok::const_buffer const &)` |
| 99.96 | `private: void __thiscall vostok::resources::query_result::unpin_raw_buffer(class vostok::const_buffer const &)` |
| 99.96 | `public: void __thiscall vostok::render::radiance_volume::inject_camera_occluders(class vostok::render::renderer_context *)` |
| 99.96 | `private: void __thiscall vostok::render::stage_light_propagation_volumes::render_to_sun_rms(class vostok::render::light *, unsigned int, class vostok::render::vector<class vostok::math::float4x4>)` |
| 99.96 | `public: __thiscall vostok::render::engine::world::~world(void)` |
| 99.96 | `public: long __thiscall vostok::resources::resources_manager::query_resources_impl(struct vostok::resources::query_resource_params const &)` |
| 99.96 | `private: void __thiscall vostok::resources::query_result::propogate_sub_fats_to_resource<class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> >(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> &)` |
| 99.96 | `private: void __thiscall vostok::resources::query_result::propogate_sub_fats_to_resource<class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> >(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> &)` |
| 99.96 | `public: void __thiscall vostok::resources::resources_manager::continue_init_new_query(class vostok::resources::query_result &)` |
| 99.96 | `public: bool __thiscall vostok::render::remove_model_if_not_lod_predicate::operator()(struct vostok::render::render_surface_instance *)` |
| 99.97 | `private: void __thiscall vostok::resources::queries_result::translate_request_paths(void)` |
| 99.97 | `private: void __thiscall vostok::resources::queries_result::push_to_grm_cache(void)` |
| 99.97 | `private: void __thiscall vostok::resources::query_result::associate_created_resource_with_fat_or_name_registry(void)` |
| 99.97 | `public: virtual void __thiscall survarium::medkit::action(bool)` |
| 99.97 | `public: void __thiscall vostok::render::renderer_context::set_scene_view(class vostok::resources::resource_ptr<struct vostok::render::base_scene_view, class vostok::resources::unmanaged_intrusive_base>)` |
| 99.97 | `private: enum vostok::resources::allocation_result_enum __thiscall vostok::resources::query_result::allocate_final_unmanaged_resource_if_needed(void)` |
| 99.97 | `private: void __thiscall vostok::resources::query_result::translate_request_path(void)` |
| 99.97 | `private: void __thiscall vostok::resources::resources_manager::save_generated_resources(void)` |
| 99.97 | `protected: virtual void __thiscall vostok::resources::query_result_for_cook::increase_quality_to_target(class vostok::resources::query_result_for_cook *)` |
| 99.97 | `private: void __thiscall vostok::resources::query_result::late_set_fat_it(class vostok::vfs::vfs_iterator)` |
| 99.97 | `public: virtual void __thiscall vostok::render::stage_translucency::execute(void)` |
| 99.97 | `private: void __thiscall vostok::resources::allocate_functionality::prepare_raw_resource_for_inplace_unmanaged_cook(class vostok::resources::query_result *)` |
| 99.97 | `public: virtual void __thiscall vostok::render::stage_sun::execute(void)` |
| 99.97 | `private: void __thiscall vostok::resources::resources_manager::init_query_with_no_fat_it(class vostok::resources::query_result &)` |
| 99.97 | `private: class vostok::const_buffer __thiscall vostok::resources::query_result::pin_raw_buffer(void)` |
| 99.97 | `public: bool __thiscall vostok::resources::hdd_manager_sorting_predicate::operator()(class vostok::resources::query_result *, class vostok::resources::query_result *)` |
| 99.97 | `private: void __thiscall vostok::resources::query_result::on_load_operation_end(class vostok::resources::query_result *)` |
| 99.97 | `private: void __thiscall vostok::resources::resources_manager::decompress_resources(void)` |
| 99.97 | `public: void __thiscall vostok::render::grass_world::process_culling(class vostok::render::renderer_context *, float)` |
| 99.97 | `private: void __thiscall vostok::render::stage_light_propagation_volumes::render_to_rms(class vostok::math::float3const &, float, class vostok::math::float4x4const &, class vostok::math::float4x4const &, class vostok::render::vector<class vostok::math::float4x4>, unsigned int)` |
| 99.97 | `private: bool __thiscall vostok::resources::query_result::check_file_crc(void)` |
| 99.97 | `private: enum vostok::resources::query_result::consider_with_name_registry_result_enum __thiscall vostok::resources::query_result::consider_with_name_registry_impl(char const *, enum vostok::resources::query_result::only_try_to_get_associated_resource_bool)` |
| 99.97 | `private: bool __thiscall vostok::resources::query_result::try_push_created_resource_to_manager_might_destroy_this(void)` |
| 99.97 | `private: class vostok::const_buffer __thiscall vostok::resources::query_result::pin_compressed_file(void)` |
| 99.97 | `private: class vostok::const_buffer __thiscall vostok::resources::query_result::pin_raw_file(void)` |
| 99.97 | `private: bool __thiscall vostok::resources::query_result::process_request_path(bool)` |
| 99.97 | `private: bool __thiscall vostok::resources::device_manager::do_async_operation(void **, class vostok::resources::query_result *, class vostok::fs_new::synchronous_device_interface const &, class vostok::mutable_buffer, unsigned __int64, bool)` |
| 99.97 | `public: virtual void __thiscall vostok::render::renderer_cook::create_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, class vostok::mutable_buffer)` |
| 99.97 | `public: static class vostok::resources::queries_result * __cdecl vostok::resources::resources_manager::create_queries_result(struct vostok::resources::query_resource_params const &)` |
| 99.97 | `public: virtual void __thiscall vostok::render::stage_volume_fog::execute(void)` |
| 99.97 | `private: bool __thiscall vostok::resources::query_result::try_synchronous_cook_from_inline_data(void)` |
| 99.97 | `private: void __thiscall vostok::animation::animation_collection_cook::sub_animations_loaded(class vostok::resources::queries_result &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class vostok::configs::binary_config_value const &)` |
| 99.97 | `private: void __thiscall vostok::render::stage_lights::make_skin_scattering_texture(struct vostok::render::render_surface_instance *, class vostok::render::light *)` |
| 99.97 | `public: void __thiscall vostok::render::renderer_context::set_target_context(class vostok::render::renderer_context_targets const *, bool)` |
| 99.98 | `private: class vostok::math::float4 __thiscall vostok::render::stage_postprocess::compute_luminance_parameters(unsigned int)` |
| 99.98 | `public: virtual void __thiscall vostok::animation::animation_collection_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 99.98 | `private: void __thiscall vostok::render::stage_clouds::fill_cloud_texture(unsigned int)` |
| 99.98 | `private: void __thiscall vostok::resources::device_manager::fill_pre_allocated(void)` |
| 99.98 | `public: virtual void __thiscall vostok::render::skeleton_combined_render_model_instance_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 99.98 | `private: static void __cdecl vostok::animation::bi_spline_skeleton_animation_impl_cook::on_resources_ready(class vostok::resources::queries_result &, class vostok::resources::query_result_for_cook *const)` |
| 99.98 | `public: void __thiscall vostok::resources::resources_manager::cooker_thread_tick(void)` |
| 99.98 | `private: void __thiscall vostok::resources::queries_result::on_fs_iterator_ready(class vostok::vfs::vfs_locked_iterator const &, class vostok::resources::query_result *)` |
| 99.98 | `private: void __thiscall survarium::weapon_cook::on_weapon_subresources_ready(class vostok::resources::queries_result &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class survarium::weapon_core *)` |
| 99.98 | `public: virtual void __thiscall vostok::render::stage_rain::execute(void)` |
| 99.98 | `public: virtual void __thiscall vostok::render::stage_ambient_occlusion::execute(void)` |
| 99.98 | `private: void __thiscall vostok::resources::resources_manager::dispatch_allocated_raw_resources(void)` |
| 99.98 | `private: void __thiscall vostok::resources::resources_manager::dispatch_created_resources(void)` |
| 99.98 | `public: void __thiscall vostok::render::stage_light_propagation_volumes::execute_impl(void)` |
| 99.98 | `private: __thiscall vostok::resources::queries_result::~queries_result(void)` |
| 99.98 | `private: bool __thiscall vostok::resources::device_manager::process_query(class vostok::resources::query_result *, class vostok::fs_new::synchronous_device_interface const &)` |
| 99.98 | `private: bool __thiscall vostok::resources::device_manager::process_read_query(void **, class vostok::resources::query_result *, class vostok::fs_new::synchronous_device_interface const &)` |
| 99.98 | `public: virtual void __thiscall survarium::human_npc_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 99.98 | `public: virtual void __thiscall vostok::render::stage_lights::execute(void)` |
| 99.98 | `private: bool __thiscall vostok::resources::device_manager::process_write_query(void **, class vostok::resources::query_result *, class vostok::fs_new::synchronous_device_interface const &)` |
| 99.98 | `public: class vostok::fs_new::native_path_string __thiscall vostok::resources::query_result::absolute_physical_path(enum assert_on_fail_bool)` |
| 99.98 | `private: void __thiscall vostok::render::stage_light_propagation_volumes::render_to_rms_smoothed2(class vostok::math::float3const &, float, class vostok::math::float4x4const &, class vostok::math::float4x4const &, class vostok::render::vector<class vostok::math::float4x4>, unsigned int, unsigned int, unsigned int)` |
| 99.98 | `public: void __thiscall vostok::render::stage_forward::accumulate_local_reflections(void)` |
| 99.98 | `private: bool __thiscall vostok::resources::query_result::check_fat_for_resource_reusage(void)` |
| 99.98 | `protected: void __thiscall vostok::render::render_model_cook::on_subresources_loaded(class vostok::resources::queries_result &, struct vostok::render::cook_intermediate_data *)` |
| 99.98 | `private: bool __thiscall vostok::resources::query_result::translate_query_if_needed(void)` |
| 99.98 | `public: void __thiscall vostok::render::stage_debug::render_environment_probe_preview(void)` |
| 99.98 | `private: void __thiscall vostok::resources::query_result::do_create_resource(bool *)` |
| 99.98 | `public: void __thiscall vostok::resources::resources_manager::after_resource_deleted(class vostok::resources::cook_base *, bool, class vostok::resources::query_result *const, class vostok::resources::memory_usage_type const &, enum vostok::resources::class_id_enum, char const *)` |
| 99.98 | `private: void __thiscall vostok::render::static_render_model_instance_cook::on_sub_resources_loaded(class vostok::resources::queries_result &)` |
| 99.98 | `private: bool __thiscall vostok::resources::device_manager::open_file(void ***, class vostok::resources::query_result *, class vostok::fs_new::synchronous_device_interface const &)` |
| 99.98 | `private: void __thiscall vostok::resources::query_result::replicate(void)` |
| 99.98 | `private: void __thiscall survarium::player_cook::on_hit_params_loaded(class vostok::resources::queries_result &, struct survarium::player_creation_params *)` |
| 99.98 | `public: virtual void __thiscall vostok::render::stage_clouds::execute(void)` |
| 99.98 | `public: virtual void __thiscall vostok::render::stage_atmosphere::execute(void)` |
| 99.98 | `public: void __thiscall vostok::render::speedtree_forest::get_visible_tree_components(class vostok::render::renderer_context *, class vostok::math::float3const &, bool, class vostok::render::vector<struct vostok::render::speedtree_forest::tree_render_info> &)` |
| 99.98 | `private: void __thiscall vostok::resources::query_result::do_create_resource_end_part(void)` |
| 99.98 | `private: void __thiscall survarium::profile_character::weapon_resources_ready(class vostok::resources::queries_result &)` |
| 99.98 | `private: void __thiscall vostok::resources::device_manager::on_query_processed(class vostok::resources::query_result *, bool)` |
| 99.98 | `public: void __thiscall vostok::animation::skeleton_cook::on_sub_resources_loaded(class vostok::resources::queries_result &)` |
| 99.98 | `public: virtual void __thiscall vostok::render::stage_debug::execute(void)` |
| 99.98 | `protected: void __thiscall vostok::resources::query_result_for_cook::finish_query_impl(enum vostok::resources::cook_base::result_enum, enum assert_on_fail_bool, enum vostok::resources::query_result_for_user::error_type_enum)` |
| 99.98 | `protected: void __thiscall survarium::game_world::on_project_loaded(class vostok::resources::queries_result &, unsigned int, class boost::function<void __cdecl (class vostok::resources::queries_result &)> const &)` |
| 99.98 | `private: void __thiscall survarium::project_cooker_simple::on_collision_and_visuals_loaded(class vostok::resources::queries_result &, class survarium::simple_game_project *)` |
| 99.98 | `public: void __thiscall vostok::render::stage_light_propagation_volumes::execute_smoothed_impl(unsigned int, unsigned int, unsigned int, unsigned int, unsigned int)` |
| 99.98 | `private: void __thiscall survarium::damage_zone_cook::on_sub_resources_loaded(class vostok::resources::queries_result &, class vostok::configs::binary_config_value const &)` |
| 99.98 | `private: void __thiscall vostok::sound::sound_collection_cook::sub_sounds_loaded(class vostok::resources::queries_result &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class vostok::configs::binary_config_value const &)` |
| 99.98 | `public: virtual void __thiscall vostok::render::stage_forward::execute(void)` |
| 99.98 | `public: virtual void __thiscall vostok::render::render_output_window_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 99.98 | `public: void __thiscall vostok::render::stage_forward::render_forward_models(class vostok::render::vector<struct vostok::render::render_surface_instance *> &, unsigned int)` |
| 99.99 | `private: void __thiscall vostok::resources::resources_manager::save_generated_resource(class vostok::resources::query_result *)` |
| 99.99 | `private: void __thiscall survarium::human_npc_cook::on_subresources_loaded(class vostok::resources::queries_result &, class survarium::human_npc *const)` |
| 99.99 | `public: virtual void __thiscall vostok::sound::sound_scene_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 99.99 | `public: virtual void __thiscall vostok::render::stage_pre_rain::execute(void)` |
| 99.99 | `private: void __thiscall vostok::resources::query_result::send_to_create_resource(void)` |
| 99.99 | `private: void __thiscall survarium::sound_player_cook::on_sounds_loaded(class vostok::resources::queries_result &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>)` |
| 99.99 | `private: void __thiscall survarium::booby_trap_cook::on_models_ready(class vostok::resources::queries_result &, class survarium::booby_trap *)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_aimed_fire_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_aimed_fire_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_fire_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_fire_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_reload_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_reload_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_show_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_show_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_aimed_fire_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_aimed_fire_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_fire_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_fire_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_reload_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_reload_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_show_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_show_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_aimed_fire_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_aimed_fire_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_chamber_a_round_aimed_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_chamber_a_round_aimed_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_chamber_a_round_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_chamber_a_round_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_fire_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_fire_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_reload_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_reload_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_finish_substate> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_finish_substate> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_one_round_substate> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_one_round_substate> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_start_substate> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_start_substate> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_show_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_show_state> >::config_params)` |
| 99.99 | `private: void __thiscall vostok::animation::single_animation_cook::on_sub_resources_loaded(class vostok::resources::queries_result &)` |
| 99.99 | `public: virtual void __thiscall vostok::render::stage_resolve_lighting::execute(void)` |
| 99.99 | `private: void __thiscall vostok::render::stage_light_propagation_volumes::render_to_sky_rms(class vostok::render::light *, unsigned int, unsigned int, class vostok::render::vector<class vostok::math::float4x4>)` |
| 99.99 | `public: virtual void __thiscall vostok::render::stage_shadow_direct::execute_disabled(void)` |
| 99.99 | `private: void __thiscall vostok::render::stage_visibility::frustum_culling(void)` |
| 99.99 | `private: void __thiscall vostok::render::stage_gbuffer::z_only_pass(void)` |
| 99.99 | `public: void __thiscall vostok::render::stage_forward::render_opaque_models(void)` |
| 99.99 | `private: void __thiscall vostok::render::effect_manager::on_effects_recompiled(class vostok::vectora<struct vostok::render::effect_manager::effect_to_recompile_struct> *, class vostok::resources::queries_result &)` |
| 99.99 | `public: virtual void __thiscall vostok::render::material_effects_instance_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 99.99 | `public: virtual void __thiscall vostok::render::stage_light_propagation_volumes::execute(void)` |
| 99.99 | `private: void __thiscall survarium::shotgun_weapon_reload_state_cook::on_substates_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *)` |
| 99.99 | `private: void __thiscall survarium::player_cook::on_subresources_loaded(class vostok::resources::queries_result &, struct survarium::player_creation_params *, struct survarium::inventory_cooker_data *, struct survarium::player_parameters_cooker_data *)` |
| 99.99 | `private: void __thiscall survarium::items_cook::create_item_and_finish_query(enum survarium::item_types_enum, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class vostok::resources::query_result_for_cook *)` |
| 99.99 | `private: void __thiscall survarium::main_menu::on_resources_ready(class vostok::resources::queries_result &)` |
| 99.99 | `private: void __thiscall survarium::project_cooker_simple::on_damage_zones_loaded(class survarium::simple_game_project *, class vostok::resources::queries_result &)` |
| 99.99 | `private: void __thiscall survarium::project_cooker_simple::on_ladders_loaded(class survarium::simple_game_project *, class vostok::resources::queries_result &)` |
| 99.99 | `private: void __thiscall vostok::render::stage_visibility::get_results_and_prepare_bounds_portals(class vostok::math::float4*&, unsigned int &)` |
| 99.99 | `protected: void __thiscall vostok::render::render_model_cook::on_materials_loaded(class vostok::resources::queries_result &, struct vostok::render::cook_intermediate_data *)` |
| 99.99 | `private: void __thiscall vostok::sound::ogg_encoded_sound_interface_cook::on_ogg_resources_loaded(class vostok::resources::queries_result &, class vostok::resources::query_result_for_cook *)` |
| 99.99 | `private: void __thiscall vostok::resources::query_result::set_deleter_object_if_needed(bool *)` |
| 99.99 | `public: void __thiscall vostok::resources::allocate_functionality::prepare_final_resource(class vostok::resources::query_result *)` |
| 99.99 | `private: void __thiscall survarium::profile_character::character_animation_ready(class vostok::resources::queries_result &)` |
| 99.99 | `private: void __thiscall vostok::resources::query_result::finish_translated_query(enum vostok::resources::cook_base::result_enum)` |
| 99.99 | `public: void __thiscall vostok::render::batched_geometry<struct vostok::render::lpv_vertex>::for_each_batch_render(class vostok::render::renderer_context *, class boost::function<void __cdecl (struct vostok::render::geometry_batch const &)> const &, class boost::function<void __cdecl (struct vostok::render::geometry_batch const &)> const &)` |
| 99.99 | `private: void __thiscall vostok::render::stage_visibility::get_results_and_prepare_bounds_models(class vostok::math::float4*&, unsigned int &)` |
| 99.99 | `private: void __thiscall vostok::resources::queries_result::query_fs_iterators(void)` |
| 99.99 | `protected: void __thiscall vostok::core::configs::binary_config_cook::on_fs_iterators_ready(class vostok::resources::queries_result &)` |
| 99.99 | `public: void __thiscall vostok::render::stage_shadow_direct::render_models(class vostok::render::vector<struct vostok::render::render_surface_instance *> &, class vostok::math::float4x4const &, unsigned int, unsigned int, class vostok::math::float3const &, unsigned int, unsigned int)` |
| 99.99 | `private: void __thiscall vostok::render::skeleton_combined_model_cook::on_resources_loaded(class vostok::resources::queries_result &, class vostok::resources::query_result_for_cook *, struct vostok::render::skeleton_combined_cook_data *)` |
| 99.99 | `private: void __thiscall vostok::render::stage_visibility::get_results_and_prepare_bounds_particles(class vostok::math::float4*&, unsigned int &)` |
| 99.99 | `private: void __thiscall vostok::render::speedtree_cook::on_speedtree_raw_data_loaded(class vostok::resources::queries_result &, struct vostok::render::speedtree_data *)` |
| 99.99 | `private: void __thiscall vostok::render::stage_visibility::get_results_and_prepare_bounds_lights(class vostok::math::float4*&, unsigned int &)` |
| 99.99 | `private: void __thiscall vostok::resources::resources_manager::init_new_autoselect_quality_queries(void)` |
| 99.99 | `public: void __thiscall vostok::render::speedtree_billboard_parameters::set(class vostok::render::renderer_context *, class vostok::render::speedtree_tree_component *)` |
| 99.99 | `private: void __thiscall vostok::render::stage_visibility::get_results_and_prepare_bounds_grass(class vostok::math::float4*&, unsigned int &)` |
| 99.99 | `private: void __thiscall vostok::resources::allocate_functionality::prepare_raw_resource_for_managed_or_unmanaged_cook(class vostok::resources::query_result *, enum vostok::resources::reallocating_bool)` |
| 99.99 | `private: void __thiscall vostok::render::stage_lights::render_shadowed_light(class vostok::render::light *)` |
| 99.99 | `private: void __thiscall vostok::render::stage_visibility::get_results_and_prepare_bounds_ambient_volumes(class vostok::math::float4*&, unsigned int &)` |
| 99.99 | `private: void __thiscall vostok::render::stage_visibility::get_results_and_prepare_bounds_decals(class vostok::math::float4*&, unsigned int &)` |
| 99.99 | `private: void __thiscall vostok::render::stage_visibility::get_results_and_prepare_bounds_env_probes(class vostok::math::float4*&, unsigned int &)` |
| 99.99 | `public: virtual void __thiscall vostok::render::static_model_instance_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 99.99 | `public: virtual void __thiscall vostok::render::material_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 99.99 | `private: void __thiscall vostok::resources::query_result::do_managed_create_resource(class vostok::resources::managed_cook *)` |
| 99.99 | `private: void __thiscall vostok::sound::composite_sound_cook::on_sub_resources_loaded(class vostok::resources::queries_result &)` |
| 99.99 | `private: void __thiscall survarium::login_menu::on_resources_ready(class vostok::resources::queries_result &)` |
| 99.99 | `public: virtual void __thiscall vostok::render::skeleton_combined_model_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 99.99 | `public: virtual void __thiscall vostok::sound::sound_collection_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 99.99 | `private: void __thiscall vostok::render::stage_gbuffer::render_models(class vostok::render::vector<struct vostok::render::render_surface_instance *> &, unsigned int, unsigned int &, bool)` |
| 99.99 | `private: void __thiscall vostok::render::grass_cook::on_layers_loaded(class vostok::resources::queries_result &, struct vostok::render::grass_cook_data *)` |
| 99.99 | `public: void __thiscall vostok::render::decal_shader_constants_and_geometry::set(class vostok::render::renderer_context *, class vostok::math::float4x4const &, class vostok::math::float4x4const &, float, float, class vostok::math::float3const &, class vostok::math::float4x4const &)` |
| 99.99 | `private: void __thiscall vostok::resources::query_result::do_create_resource_impl(void)` |
| 99.99 | `public: virtual void __thiscall vostok::render::culling::portal_sector_structure_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 99.99 | `private: void __thiscall survarium::lobby_menu::on_render_scenes_ready(class vostok::resources::queries_result &)` |
| 99.99 | `public: void __thiscall vostok::render::stage_resolve_lighting::render_models(class vostok::render::vector<struct vostok::render::render_surface_instance *> &, unsigned int &)` |
| 99.99 | `public: virtual void __thiscall survarium::damage_zone_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 99.99 | `public: virtual void __thiscall vostok::render::stage_postprocess::execute_disabled(void)` |
| 99.99 | `private: void __thiscall vostok::resources::allocate_functionality::prepare_raw_resource_for_inplace_managed_cook(class vostok::resources::query_result *, enum vostok::resources::reallocating_bool)` |
| 99.99 | `public: virtual void __thiscall vostok::render::skeleton_combined_model_instance_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 99.99 | `public: void __thiscall vostok::resources::resources_manager::dispatch_callbacks(bool)` |
| 99.99 | `public: class vostok::render::effect_compiler & __thiscall vostok::render::effect_compiler::set_texture(char const *, char const *, class vostok::intrusive_ptr<class vostok::render::res_texture, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy> *, bool, unsigned int)` |
| 99.99 | `private: void __thiscall survarium::booby_trap_set_cook::on_models_ready(class vostok::resources::queries_result &, class survarium::booby_trap_set *)` |
| 99.99 | `public: virtual void __thiscall vostok::render::stage_gbuffer::execute(void)` |
| 99.99 | `public: virtual void __thiscall vostok::render::stage_ambient_lighting::execute(void)` |
| 99.99 | `private: void __thiscall survarium::empty_hands_cook::on_empty_hands_animations_loaded(class vostok::resources::queries_result &)` |
| 99.99 | `private: void __thiscall vostok::render::speedtree_cook::on_model_materials_loaded(class vostok::resources::queries_result &, struct vostok::render::speedtree_data *)` |
| 99.99 | `private: __thiscall vostok::resources::queries_result::queries_result(unsigned int, class boost::function<void __cdecl (class vostok::resources::queries_result &)>, class vostok::memory::base_allocator *, unsigned int, class vostok::resources::query_result_for_cook *, float *, bool const *, unsigned int const *, enum vostok::resources::query_type_enum, enum vostok::resources::autoselect_quality_bool const *, enum assert_on_fail_bool)` |
| 99.99 | `public: void __thiscall vostok::render::grass_patch::render(struct vostok::render::grass_world *, class vostok::render::renderer_context *, class vostok::math::float3const &, enum vostok::render::enum_render_stage_type, unsigned int, float, class vostok::render::res_effect *, unsigned int)` |
| 99.99 | `private: void __thiscall vostok::sound::composite_sound_cook::on_sounds_loaded(class vostok::resources::queries_result &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class vostok::configs::binary_config_value const &)` |
| 99.99 | `public: void __thiscall vostok::render::speedtree_common_parameters::set(class vostok::render::renderer_context *, class vostok::render::speedtree_tree_component *, class vostok::math::float3const &)` |
| 99.99 | `private: void __thiscall vostok::physics::collision_shape_cook::on_collision_sources_loaded(class vostok::resources::queries_result &, struct vostok::physics::collision_shape_cook::cook_data *)` |
| 99.99 | `private: void __thiscall survarium::weapon_core_state_cook_template<class survarium::double_barreled_weapon_core_aimed_idle_state>::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *)` |
| 99.99 | `private: void __thiscall survarium::weapon_core_state_cook_template<class survarium::double_barreled_weapon_core_idle_state>::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *)` |
| 99.99 | `private: void __thiscall survarium::weapon_core_state_cook_template<class survarium::pistol_weapon_core_aimed_idle_state>::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *)` |
| 99.99 | `private: void __thiscall survarium::weapon_core_state_cook_template<class survarium::pistol_weapon_core_idle_state>::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *)` |
| 99.99 | `private: void __thiscall survarium::weapon_core_state_cook_template<class survarium::weapon_core_aimed_state>::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *)` |
| 99.99 | `private: void __thiscall survarium::weapon_core_state_cook_template<class survarium::weapon_core_idle_state>::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *)` |
| 99.99 | `public: void __thiscall vostok::render::radiance_volume::prepare(class vostok::math::float3const &, class vostok::math::float3const &, float)` |
| 99.99 | `public: virtual void __thiscall survarium::weapon_core_state_cook_template<class survarium::double_barreled_weapon_core_aimed_idle_state>::create_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, class vostok::mutable_buffer)` |
| 99.99 | `public: virtual void __thiscall survarium::weapon_core_state_cook_template<class survarium::double_barreled_weapon_core_idle_state>::create_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, class vostok::mutable_buffer)` |
| 99.99 | `public: virtual void __thiscall survarium::weapon_core_state_cook_template<class survarium::pistol_weapon_core_aimed_idle_state>::create_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, class vostok::mutable_buffer)` |
- _...and 73 more_

### Added (25)

- `private: float __thiscall survarium::medkit::reduce_damage(char const *, char const *, float, float)`
- `private: struct survarium::medkit::damage_protection const * __thiscall survarium::medkit::find_damage_protection(char const *, char const *)`
- `private: void __thiscall survarium::medkit::active_tick(unsigned int)`
- `private: void __thiscall survarium::medkit::on_player_death(void)`
- `private: void __thiscall survarium::medkit::remove_affects(void)`
- `private: void __thiscall survarium::medkit::set_active(bool)`
- `private: void __thiscall vostok::resources::allocate_functionality::allocate_final_resources<class vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 616, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy> >(class vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 616, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy> &, bool)`
- `private: void __thiscall vostok::resources::resources_manager::create_resources<class vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 616, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy> >(class vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 616, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy> const &, class vostok::resources::query_result *, bool)`
- `public: __thiscall survarium::player_death_subscriber::player_death_subscriber(class boost::function<void __cdecl (void)> const &)`
- `public: __thiscall vostok::fs_new::virtual_path_string::ctor<char *>(char *const &)`
- `public: __thiscall vostok::render::speedtree_data::speedtree_data(void)`
- `public: class vostok::resources::query_result * __thiscall vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 608, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::pop_front(void)`
- `public: class vostok::resources::query_result * __thiscall vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 616, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::pop_all_and_clear(unsigned int *)`
- `public: virtual __thiscall vostok::ai::selectors::sound_target_selector::~sound_target_selector(void)`
- `public: virtual void __thiscall survarium::medkit::holder_assigned(void)`
- `public: virtual void __thiscall survarium::medkit::holder_removed(void)`
- `public: virtual void __thiscall survarium::medkit::remove(void)`
- `public: virtual void __thiscall vostok::resources::hdd_manager::grab_sorted_queries(class vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 616, class vostok::threading::single_threading_policy, class vostok::size_policy, class vostok::no_debug_policy> &)`
- `public: void __thiscall vostok::intrusive_double_linked_list<class vostok::resources::query_result, class vostok::resources::query_result *, 624, 620, class vostok::threading::mutex, class vostok::no_size_policy, class vostok::debug_policy>::erase(class vostok::resources::query_result *)`
- `public: void __thiscall vostok::intrusive_double_linked_list<class vostok::resources::query_result, class vostok::resources::query_result *, 624, 620, class vostok::threading::mutex, class vostok::no_size_policy, class vostok::debug_policy>::push_back(class vostok::resources::query_result *, bool *)`
- `public: void __thiscall vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 616, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::push_back(class vostok::resources::query_result *, bool *)`
- `public: void __thiscall vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 616, class vostok::threading::single_threading_policy, class vostok::size_policy, class vostok::no_debug_policy>::push_back(class vostok::resources::query_result *, bool *)`
- `public: void __thiscall vostok::render::renderer::fill_opaque_models(unsigned int, unsigned int)`
- `public: void __thiscall vostok::render::stage_shadow_direct::execute_cascade(unsigned int, unsigned int, unsigned int, unsigned int)`
- `public: void __thiscall vostok::render::stage_shadow_direct::prepare_models(class vostok::render::vector<struct vostok::render::render_surface_instance *> &, class vostok::math::float4x4const &, unsigned int, unsigned int, class vostok::math::float3const &, unsigned int)`

### Deleted (38)

- `private: void __thiscall vostok::render::culling::portal_sector_system::draw_portals(class vostok::render::system_renderer &, unsigned int)`
- `private: void __thiscall vostok::render::culling::portal_sector_system::draw_quads(class vostok::render::system_renderer &)`
- `private: void __thiscall vostok::render::renderer::draw_frame_histogram(void) const`
- `private: void __thiscall vostok::render::renderer::draw_luminance_picker_info(struct vostok::ui::font const *)`
- `private: void __thiscall vostok::render::renderer::draw_stages_stats(struct vostok::ui::font const *)`
- `private: void __thiscall vostok::resources::allocate_functionality::allocate_final_resources<class vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 608, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy> >(class vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 608, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy> &, bool)`
- `private: void __thiscall vostok::resources::resources_manager::create_resources<class vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 608, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy> >(class vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 608, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy> const &, class vostok::resources::query_result *, bool)`
- `protected: float __thiscall survarium::medkit::reduce_damage(char const *, char const *, float, float)`
- `protected: struct survarium::medkit::damage_protection const * __thiscall survarium::medkit::find_damage_protection(char const *, char const *)`
- `protected: void __thiscall survarium::medkit::active_tick(unsigned int)`
- `protected: void __thiscall survarium::medkit::remove_affects(void)`
- `protected: void __thiscall survarium::medkit::set_active(bool)`
- `public: __thiscall vostok::particle::lod_entry::~lod_entry(void)`
- `public: __thiscall vostok::render::render_target_instance::render_target_instance(void)`
- `public: __thiscall vostok::render::sun_cascade::sun_cascade(struct vostok::render::sun_cascade const &)`
- `public: class vostok::resources::query_result * __thiscall vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 600, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::pop_front(void)`
- `public: class vostok::resources::query_result * __thiscall vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 608, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::pop_all_and_clear(unsigned int *)`
- `public: class vostok::variant<32> * __thiscall vostok::resources::query_result_for_cook::user_data(void) const`
- `public: unsigned int __thiscall vostok::render::resource_manager::get_texture_video_memory_size(void)`
- `public: virtual __thiscall survarium::rifle_scope::~rifle_scope(void)`
- `public: virtual __thiscall vostok::particle::particle_system_instance::~particle_system_instance(void)`
- `public: virtual void __thiscall vostok::resources::hdd_manager::grab_sorted_queries(class vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 608, class vostok::threading::single_threading_policy, class vostok::size_policy, class vostok::no_debug_policy> &)`
- `public: void __thiscall vostok::intrusive_double_linked_list<class vostok::resources::query_result, class vostok::resources::query_result *, 616, 612, class vostok::threading::mutex, class vostok::no_size_policy, class vostok::debug_policy>::erase(class vostok::resources::query_result *)`
- `public: void __thiscall vostok::intrusive_double_linked_list<class vostok::resources::query_result, class vostok::resources::query_result *, 616, 612, class vostok::threading::mutex, class vostok::no_size_policy, class vostok::debug_policy>::push_back(class vostok::resources::query_result *, bool *)`
- `public: void __thiscall vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 600, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::push_back(class vostok::resources::query_result *, bool *)`
- `public: void __thiscall vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 608, class vostok::threading::single_threading_policy, class vostok::size_policy, class vostok::no_debug_policy>::push_back(class vostok::resources::query_result *, bool *)`
- `public: void __thiscall vostok::render::culling::portal_sector_system::render(class vostok::render::system_renderer &, class vostok::math::float3const &, class vostok::math::float4x4const &)`
- `public: void __thiscall vostok::render::culling::sector_double_query_preventer::render(class vostok::render::system_renderer &)`
- `public: void __thiscall vostok::render::grass_world::render_debug(class vostok::render::renderer_context *)`
- `public: void __thiscall vostok::render::renderer::draw_debug(class vostok::render::scene *, class vostok::render::scene_view *, float, struct vostok::ui::font const *)`
- `public: void __thiscall vostok::render::renderer::fill_opaque_models(void)`
- `public: void __thiscall vostok::render::scene::draw_portal_system(class vostok::render::system_renderer &, class vostok::math::float3const &, class vostok::math::float4x4const &)`
- `public: void __thiscall vostok::render::stage_shadow_direct::draw_debug(unsigned int)`
- `public: void __thiscall vostok::render::stage_shadow_direct::execute_cascade(unsigned int, unsigned int, unsigned int)`
- `public: void __thiscall vostok::render::stage_shadow_direct::prepare_models(class vostok::render::vector<struct vostok::render::render_surface_instance *> &, class vostok::math::float4x4const &, unsigned int, unsigned int, class vostok::math::float3const &)`
- `vostok::render::draw_text`
- `vostok::render::draw_text_shadowed`
- `vostok::render::make_ui_vertices`

---

## v0.1.1e-build884 → v0.20e-build1916
_2013-05-28 → 2014-03-20 · +4163 / -6812 / ~4526_

### Changed (4526)

| match % | function |
| ---: | --- |
| 0.00 | `CH_ReadProcessMemory` |
| 0.00 | `GetSourceInfoFromAddress` |
| 0.00 | `InitSymInfo` |
| 0.00 | `PCSTR2LPTSTR` |
| 0.00 | `WriteStackTrace` |
| 0.00 | `__calloc_crt` |
| 0.00 | `__malloc_crt` |
| 0.00 | `__msize` |
| 0.00 | `__realloc_crt` |
| 0.00 | `__recalloc_crt` |
| 0.00 | `_munmap` |
| 0.00 | `bool __cdecl survarium::state_prio(struct survarium::anomaly_state *, struct survarium::anomaly_state *)` |
| 0.00 | `bool __cdecl vostok::core::suppress_debug_window_on_crash(void)` |
| 0.00 | `bool __cdecl vostok::fs_new::open_cached_file(class vostok::fs_new::synchronous_device_interface const &, void ***, class vostok::fs_new::native_path_string const &, enum vostok::fs_new::file_mode::mode_enum, enum vostok::fs_new::file_access::access_enum, enum assert_on_fail_bool, enum vostok::fs_new::notify_watcher_bool, enum vostok::fs_new::use_buffering_bool)` |
| 0.00 | `bool __cdecl vostok::fs_new::path_starts_with(char const *, char const *)` |
| 0.00 | `bool __cdecl vostok::network_core::operator>=(struct vostok::network_core::udp_match_stats const &, struct vostok::network_core::udp_match_stats const &)` |
| 0.00 | `bool __cdecl vostok::network_core::operator>=(struct vostok::network_core::udp_match_stream_stats const &, struct vostok::network_core::udp_match_stream_stats const &)` |
| 0.00 | `bool __cdecl vostok::render::reclaim<class vostok::render::res_xs<struct vostok::render::gs_data>, struct vostok::render::resource_manager::compare_shader_predicate<struct vostok::render::gs_data> >(class vostok::render::set<class vostok::render::res_xs<struct vostok::render::gs_data> *, struct vostok::render::resource_manager::compare_shader_predicate<struct vostok::render::gs_data> > &, class vostok::render::res_xs<struct vostok::render::gs_data> const *)` |
| 0.00 | `bool __cdecl vostok::resources::is_associated_with(class vostok::vfs::vfs_iterator, class vostok::resources::resource_base *)` |
| 0.00 | `bool __cdecl vostok::resources::try_clean_associated(class vostok::vfs::vfs_iterator, unsigned int)` |
| 0.00 | `bool __cdecl vostok::strings::ends_with(char const *const, unsigned int, char const *const, unsigned int)` |
| 0.00 | `bool __cdecl vostok::strings::iterate_items<struct vostok::logging::logger_predicate, char *>(char *const, unsigned int, struct vostok::logging::logger_predicate const &, char)` |
| 0.00 | `bool __cdecl vostok::strings::less(char const *, char const *)` |
| 0.00 | `bool __cdecl vostok::testing::run_tests_command_line(void)` |
| 0.00 | `bool __cdecl vostok::vfs::check_is_archive_file(char const *, class vostok::fs_new::synchronous_device_interface &)` |
| 0.00 | `bool __cdecl vostok::vfs::convert_physical_to_virtual_path(class vostok::intrusive_double_linked_list<class vostok::vfs::vfs_mount, class vostok::vfs::vfs_mount *, 16, 12, class vostok::threading::simple_lock, class vostok::no_size_policy, class vostok::debug_policy> &, class vostok::fs_new::virtual_path_string *, class vostok::fs_new::native_path_string const &, unsigned int, class vostok::intrusive_ptr<class vostok::vfs::vfs_mount, class vostok::vfs::vfs_intrusive_mount_base, class vostok::threading::simple_lock> *)` |
| 0.00 | `bool __cdecl vostok::vfs::convert_virtual_to_physical_path(class vostok::intrusive_double_linked_list<class vostok::vfs::vfs_mount, class vostok::vfs::vfs_mount *, 16, 12, class vostok::threading::simple_lock, class vostok::no_size_policy, class vostok::debug_policy> &, class vostok::fs_new::native_path_string *, class vostok::fs_new::virtual_path_string const &, class boost::function<bool __cdecl (char const *, char const *, char const *)> const &, class vostok::intrusive_ptr<class vostok::vfs::vfs_mount, class vostok::vfs::vfs_intrusive_mount_base, class vostok::threading::simple_lock> *)` |
| 0.00 | `bool __cdecl vostok::vfs::convert_virtual_to_physical_path(class vostok::intrusive_double_linked_list<class vostok::vfs::vfs_mount, class vostok::vfs::vfs_mount *, 16, 12, class vostok::threading::simple_lock, class vostok::no_size_policy, class vostok::debug_policy> &, class vostok::fs_new::native_path_string *, class vostok::fs_new::virtual_path_string const &, unsigned int, class vostok::intrusive_ptr<class vostok::vfs::vfs_mount, class vostok::vfs::vfs_intrusive_mount_base, class vostok::threading::simple_lock> *)` |
| 0.00 | `bool __cdecl vostok::vfs::get_inline_data<1>(class vostok::vfs::base_node<1> const *, class vostok::const_buffer *)` |
| 0.00 | `bool __cdecl vostok::vfs::lock_node(class vostok::vfs::base_node<1> *, enum vostok::vfs::lock_type_enum, enum vostok::vfs::lock_operation_enum)` |
| 0.00 | `bool __cdecl vostok::vfs::mount_overlapped_if_needed(struct vostok::vfs::find_environment &)` |
| 0.00 | `bool __cdecl vostok::vfs::need_automatic_archive_mount(bool *, class vostok::vfs::base_node<1> *, class vostok::memory::base_allocator *)` |
| 0.00 | `bool __cdecl vostok::vfs::need_physical_folder_mount(class vostok::vfs::base_node<1> *, enum vostok::vfs::find_enum, enum vostok::vfs::traverse_enum)` |
| 0.00 | `bool __cdecl vostok::vfs::need_physical_mount_or_async(class vostok::vfs::base_node<1> *, enum vostok::vfs::find_enum, enum vostok::vfs::traverse_enum)` |
| 0.00 | `bool __cdecl vostok::vfs::set_inline_data<1>(class vostok::vfs::base_node<1> *, class vostok::const_buffer const &)` |
| 0.00 | `char * __cdecl vostok::strings::copy(char *, unsigned int, char const *)` |
| 0.00 | `char * __cdecl vostok::strings::copy<32>(char (&)[32], char const *)` |
| 0.00 | `char const * __cdecl vostok::fs_new::file_name_from_path<class vostok::fs_new::native_path_string>(class vostok::fs_new::native_path_string const &)` |
| 0.00 | `char const * __cdecl vostok::fs_new::file_name_from_path<class vostok::fs_new::virtual_path_string>(class vostok::fs_new::virtual_path_string const &)` |
| 0.00 | `char const * __cdecl vostok::render::stage_type_to_string(enum vostok::render::enum_render_stage_type)` |
| 0.00 | `char const * __cdecl vostok::strings::get_token(char const *, char *, unsigned int, char)` |
| 0.00 | `class btCompoundShape * __cdecl vostok::physics::new_compound_shape_from_hit_targets_config(class vostok::configs::binary_config_value const &, class vostok::buffer_vector<class vostok::collision::bone_collision_data> &, class vostok::memory::base_allocator *)` |
| 0.00 | `class btQuaternion __cdecl vostok::physics::from_vostok(class vostok::math::quaternion const &)` |
| 0.00 | `class vostok::animation::mixing::addition_lexeme & __cdecl vostok::animation::mixing::operator+<class vostok::animation::mixing::multiplication_lexeme, class vostok::animation::mixing::multiplication_lexeme>(class vostok::animation::mixing::multiplication_lexeme &, class vostok::animation::mixing::multiplication_lexeme &)` |
| 0.00 | `class vostok::animation::mixing::expression __cdecl vostok::animation::mixing::operator+<class vostok::animation::mixing::animation_lexeme>(class vostok::animation::mixing::expression &, class vostok::animation::mixing::animation_lexeme &)` |
| 0.00 | `class vostok::animation::mixing::multiplication_lexeme & __cdecl vostok::animation::mixing::operator*<class vostok::animation::mixing::animation_lexeme, class vostok::animation::mixing::weight_lexeme>(class vostok::animation::mixing::animation_lexeme &, class vostok::animation::mixing::weight_lexeme &)` |
| 0.00 | `class vostok::collision::object * __cdecl vostok::collision::new_aabb_object(class vostok::memory::base_allocator *, unsigned int, class vostok::math::float3const &, class vostok::math::float3const &, void *)` |
| 0.00 | `class vostok::console_commands::console_command * __cdecl vostok::console_commands::find(char const *)` |
| 0.00 | `class vostok::fs_new::native_path_string __cdecl vostok::vfs::get_node_physical_path<class vostok::vfs::base_node, 1>(class vostok::vfs::base_node<1> *)` |
| 0.00 | `class vostok::fs_new::native_path_string __cdecl vostok::vfs::get_node_physical_path<class vostok::vfs::physical_file_node, 1>(class vostok::vfs::physical_file_node<1> *)` |
| 0.00 | `class vostok::intrusive_list<struct vostok::vfs::mount_referer_base, struct vostok::vfs::mount_referer *, 0, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy> * __cdecl vostok::threading::get_or_create_tls_value<class vostok::intrusive_list<struct vostok::vfs::mount_referer_base, struct vostok::vfs::mount_referer *, 0, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy> >(unsigned int, class vostok::memory::base_allocator *const)` |
| 0.00 | `class vostok::intrusive_ptr<class vostok::vfs::vfs_mount, class vostok::vfs::vfs_intrusive_mount_base, class vostok::threading::simple_lock> __cdecl vostok::vfs::find_in_mount_history(class vostok::fs_new::virtual_path_string const &, class vostok::fs_new::native_path_string const &, class vostok::intrusive_double_linked_list<class vostok::vfs::vfs_mount, class vostok::vfs::vfs_mount *, 16, 12, class vostok::threading::simple_lock, class vostok::no_size_policy, class vostok::debug_policy> &)` |
| 0.00 | `class vostok::math::float2 __cdecl vostok::math::normalize_safe(class vostok::math::float2_pod const &, class vostok::math::float2_pod const &)` |
| 0.00 | `class vostok::math::float3 __cdecl vostok::particle::read_config_value<class vostok::math::float3, class vostok::configs::binary_config_value>(class vostok::configs::binary_config_value const &, char const *, class vostok::math::float3const &)` |
| 0.00 | `class vostok::math::float4_pod __cdecl vostok::math::linear_interpolation<class vostok::math::float4_pod>(class vostok::math::float4_pod, class vostok::math::float4_pod, float)` |
| 0.00 | `class vostok::math::float4_pod __cdecl vostok::particle::bilinear_interpolation<class vostok::math::float4_pod>(class vostok::math::float4_pod, class vostok::math::float4_pod, class vostok::math::float4_pod, class vostok::math::float4_pod, float, float)` |
| 0.00 | `class vostok::math::float4x4 __cdecl vostok::math::create_camera_at(class vostok::math::float3const &, class vostok::math::float3const &, class vostok::math::float3const &)` |
| 0.00 | `class vostok::math::float4x4 __cdecl vostok::math::operator*(class vostok::math::float4x4const &, class vostok::math::float4x4const &)` |
| 0.00 | `class vostok::math::quaternion __cdecl vostok::physics::from_bullet(class btQuaternion const &)` |
| 0.00 | `class vostok::physics::bt_collision_shape * __cdecl vostok::physics::create_compound_shape(class vostok::configs::binary_config_value const &, class vostok::math::float3const &, char const *)` |
| 0.00 | `class vostok::render::render_surface * __cdecl vostok::render::model_factory::create_render_surface(unsigned short)` |
| 0.00 | `class vostok::resources::query_result * __cdecl vostok::resources::get_associated_query_result(class vostok::vfs::vfs_iterator)` |
| 0.00 | `class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> __cdecl vostok::resources::get_associated_managed_resource_ptr(class vostok::vfs::vfs_iterator)` |
| 0.00 | `class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> __cdecl vostok::resources::get_associated_unmanaged_resource_ptr(class vostok::vfs::vfs_iterator)` |
| 0.00 | `class vostok::vfs::archive_compressed_file_node<1> * __cdecl vostok::vfs::node_cast<class vostok::vfs::archive_compressed_file_node, class vostok::vfs::base_node, 1>(class vostok::vfs::base_node<1> *)` |
| 0.00 | `class vostok::vfs::archive_folder_mount_root_node<1> * __cdecl vostok::vfs::node_cast<class vostok::vfs::archive_folder_mount_root_node, class vostok::vfs::mount_root_node_base, 1>(class vostok::vfs::mount_root_node_base<1> *)` |
| 0.00 | `class vostok::vfs::archive_inline_compressed_file_node<1> * __cdecl vostok::vfs::node_cast<class vostok::vfs::archive_inline_compressed_file_node, class vostok::vfs::base_node, 1>(class vostok::vfs::base_node<1> *)` |
| 0.00 | `class vostok::vfs::archive_inline_file_node<1> * __cdecl vostok::vfs::node_cast<class vostok::vfs::archive_inline_file_node, class vostok::vfs::base_node, 1>(class vostok::vfs::base_node<1> *)` |
| 0.00 | `class vostok::vfs::base_folder_node<1> * __cdecl vostok::vfs::cast_folder<1>(class vostok::vfs::base_node<1> *)` |
| 0.00 | `class vostok::vfs::base_node<1> * __cdecl vostok::vfs::find_node_of_mount(class vostok::vfs::vfs_hashset &, class vostok::fs_new::virtual_path_string const &, unsigned int, unsigned int)` |
| 0.00 | `class vostok::vfs::base_node<1> * __cdecl vostok::vfs::find_referenced_link_node(class vostok::vfs::base_node<1> const *)` |
| 0.00 | `class vostok::vfs::mount_helper_node<1> * __cdecl vostok::vfs::node_cast<class vostok::vfs::mount_helper_node, class vostok::vfs::base_node, 1>(class vostok::vfs::base_node<1> *)` |
| 0.00 | `class vostok::vfs::mount_root_node_base<1> * __cdecl vostok::vfs::node_cast<class vostok::vfs::mount_root_node_base, class vostok::vfs::base_node, 1>(class vostok::vfs::base_node<1> *)` |
| 0.00 | `class vostok::vfs::physical_file_node<1> * __cdecl vostok::vfs::cast_physical_file<1>(class vostok::vfs::base_node<1> *)` |
| 0.00 | `class vostok::vfs::physical_file_node<1> * __cdecl vostok::vfs::node_cast<class vostok::vfs::physical_file_node, class vostok::vfs::base_node, 1>(class vostok::vfs::base_node<1> *)` |
| 0.00 | `class vostok::vfs::physical_folder_mount_root_node<1> * __cdecl vostok::vfs::node_cast<class vostok::vfs::physical_folder_mount_root_node, class vostok::vfs::base_node, 1>(class vostok::vfs::base_node<1> *)` |
| 0.00 | `class vostok::vfs::physical_folder_node<1> * __cdecl vostok::vfs::node_cast<class vostok::vfs::physical_folder_node, class vostok::vfs::base_node, 1>(class vostok::vfs::base_node<1> *)` |
| 0.00 | `class vostok::vfs::universal_file_node<1> * __cdecl vostok::vfs::node_cast<class vostok::vfs::universal_file_node, class vostok::vfs::base_node, 1>(class vostok::vfs::base_node<1> *)` |
| 0.00 | `class vostok::vfs::vfs_mount * __cdecl vostok::vfs::mount_of_node<1>(class vostok::vfs::base_node<1> *)` |
| 0.00 | `compare_parts` |
| 0.00 | `convert_stick_value` |
| 0.00 | `convert_to_unicode_if_needed` |
| 0.00 | `enum vostok::math::enum_evaluate_type __cdecl vostok::math::string_to_evaluate_type(char const *)` |
| 0.00 | `enum vostok::vfs::result_enum __cdecl vostok::vfs::fill_expand_nodes_and_incref(class vostok::vfs::base_node<1> *, class vostok::vfs::base_node<1> *, class vostok::vfs::base_node<1> *, class vostok::intrusive_list<struct vostok::vfs::node_to_expand, struct vostok::vfs::node_to_expand *, 8, class vostok::threading::single_threading_policy, class vostok::size_policy, class vostok::no_debug_policy> &, struct vostok::vfs::async_callbacks_data *, unsigned int)` |
| 0.00 | `enum vostok::vfs::result_enum __cdecl vostok::vfs::fill_nodes_to_expand_from_overlapped(class vostok::vfs::base_node<1> *, class vostok::vfs::base_node<1> *, class vostok::intrusive_list<struct vostok::vfs::node_to_expand, struct vostok::vfs::node_to_expand *, 8, class vostok::threading::single_threading_policy, class vostok::size_policy, class vostok::no_debug_policy> &, class vostok::memory::base_allocator *, enum vostok::vfs::find_enum, enum vostok::vfs::traverse_enum, unsigned int)` |
| 0.00 | `enum vostok::vfs::result_enum __cdecl vostok::vfs::overlapped_chain_is_expanded(class vostok::vfs::base_node<1> *, struct vostok::vfs::find_environment &)` |
| 0.00 | `enum vostok::vfs::result_enum __cdecl vostok::vfs::try_find_sync(char const *, class vostok::vfs::vfs_locked_iterator *, enum vostok::vfs::find_enum, class vostok::vfs::virtual_file_system *, class vostok::memory::base_allocator *)` |
| 0.00 | `enum vostok::vfs::result_enum __cdecl vostok::vfs::try_pin_tree(class vostok::vfs::base_node<1> *, struct vostok::vfs::find_environment &)` |
| 0.00 | `fill_state` |
| 0.00 | `float __cdecl survarium::computed_shooting_animation_time_scale(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, float)` |
| 0.00 | `float __cdecl vostok::render::calculate_streaming_texture_factor(class vostok::math::float3const *, class vostok::math::float2const *, unsigned int, unsigned int, unsigned short const *, unsigned int)` |
| 0.00 | `float __cdecl vostok::ui::calc_string_length(class vostok::ui::ui_font const &, char const *)` |
| 0.00 | `int __cdecl vostok::debug::unhandled_exception_filter(int, struct _EXCEPTION_POINTERS *const)` |
| 0.00 | `int __cdecl vostok::detail::strcmp_s(char const *, char const *)` |
| 0.00 | `int __cdecl vostok::render::compare(class vostok::render::res_declaration const &, class vostok::render::res_declaration const &)` |
| 0.00 | `int __cdecl vostok::sound::ogg_utils::ov_seek_func(void *, __int64, int)` |
| 0.00 | `int __cdecl vostok::sprintf(char *, unsigned int, char const *const, ...)` |
| 0.00 | `invalid_parameter_handler` |
| 0.00 | `load_function<void __stdcall(unsigned long)>` |
| 0.00 | `load_library` |
| 0.00 | `long __cdecl vostok::sound::ogg_utils::ov_tell_func(void *)` |
| 0.00 | `message_processor` |
| 0.00 | `on_error` |
| 0.00 | `on_mounted_resources` |
| 0.00 | `on_mounted_user_data` |
| 0.00 | `output` |
| 0.00 | `private: __thiscall survarium::double_barreled_weapon_core_idle_state::double_barreled_weapon_core_idle_state(class survarium::weapon_core &, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)` |
| 0.00 | `private: __thiscall survarium::medkit::medkit(void)` |
| 0.00 | `private: __thiscall survarium::pistol_weapon_core_idle_state::pistol_weapon_core_idle_state(class survarium::weapon_core &, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)` |
| 0.00 | `private: __thiscall survarium::weapon_core_idle_state::weapon_core_idle_state(class survarium::weapon_core &, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)` |
| 0.00 | `private: __thiscall vostok::ai::planning::base_lexeme::base_lexeme(enum vostok::ai::planning::base_lexeme::operation_type_enum, class vostok::ai::planning::base_lexeme const &, class vostok::ai::planning::base_lexeme const &, bool)` |
| 0.00 | `private: __thiscall vostok::animation::cubic_spline_skeleton_animation::cubic_spline_skeleton_animation(class vostok::animation::bi_spline_skeleton_animation_baked const &)` |
| 0.00 | `private: __thiscall vostok::render::res_geometry::~res_geometry(void)` |
| 0.00 | `private: bool __thiscall survarium::breath_vibration_calculator::insufficient_breath(void) const` |
| 0.00 | `private: bool __thiscall survarium::bullet::update_bullet_position(float, class vostok::math::float3const &)` |
| 0.00 | `private: bool __thiscall survarium::weapon_core::AE_pred(void) const` |
| 0.00 | `private: bool __thiscall survarium::weapon_core::auto_reload_AE_pred(void) const` |
| 0.00 | `private: bool __thiscall survarium::weapon_core::can_reload(void) const` |
| 0.00 | `private: bool __thiscall survarium::weapon_core::chamber_a_round_AE_pred(void) const` |
| 0.00 | `private: bool __thiscall survarium::weapon_core::fire_AE_pred(void) const` |
| 0.00 | `private: bool __thiscall survarium::weapon_core::fire_pred(void) const` |
| 0.00 | `private: bool __thiscall survarium::weapon_core::hide_AE_pred(void) const` |
| 0.00 | `private: bool __thiscall survarium::weapon_core::hide_break_pred(void) const` |
| 0.00 | `private: bool __thiscall survarium::weapon_core::hide_pred(void) const` |
| 0.00 | `private: bool __thiscall survarium::weapon_core::idle_AE_not_fire_pred(void) const` |
| 0.00 | `private: bool __thiscall survarium::weapon_core::idle_AE_or_reload_break_pred(void) const` |
| 0.00 | `private: bool __thiscall survarium::weapon_core::idle_AE_or_show_break_pred(void) const` |
| 0.00 | `private: bool __thiscall survarium::weapon_core::inactive_pred(void) const` |
| 0.00 | `private: bool __thiscall survarium::weapon_core::is_trying_to_reload(void) const` |
| 0.00 | `private: bool __thiscall survarium::weapon_core::reload_AE_pred(void) const` |
| 0.00 | `private: bool __thiscall survarium::weapon_core::reload_break_pred(void) const` |
| 0.00 | `private: bool __thiscall survarium::weapon_core::show_AE_pred(void) const` |
| 0.00 | `private: bool __thiscall survarium::weapon_core_shotgun_reload_state::finish_reload_predicate(void) const` |
| 0.00 | `private: bool __thiscall survarium::weapon_core_shotgun_reload_state::player_wants_to_fire_predicate(void) const` |
| 0.00 | `private: bool __thiscall survarium::weapon_user_animations_selector::broken_legs_predicate(void) const` |
| 0.00 | `private: bool __thiscall survarium::weapon_user_animations_selector::crouch_predicate(void) const` |
| 0.00 | `private: bool __thiscall survarium::weapon_user_animations_selector::is_trying_to_jump(void) const` |
| 0.00 | `private: bool __thiscall survarium::weapon_user_animations_selector::is_trying_to_sprint(void) const` |
| 0.00 | `private: bool __thiscall vostok::animation::mixing::n_ary_tree_comparer::new_time_scale(class vostok::animation::mixing::n_ary_tree_animation_node &)` |
| 0.00 | `private: bool __thiscall vostok::console_impl::on_text_commit(struct vostok::ui::window *, int, int)` |
| 0.00 | `private: bool __thiscall vostok::network::login_client_impl::verify_ssl_certificate(bool, class boost::asio::ssl::verify_context &)` |
| 0.00 | `private: bool __thiscall vostok::network_core::http_client::add_result_content(void)` |
| 0.00 | `private: bool __thiscall vostok::render::textures_handler<1>::set_overwrite(char const *, class vostok::render::res_texture *)` |
| 0.00 | `private: bool __thiscall vostok::resources::base_of_intrusive_base::is_associated_with_fat(class vostok::resources::managed_resource *const) const` |
| 0.00 | `private: bool __thiscall vostok::resources::base_of_intrusive_base::try_unregister_from_fat_or_from_name_registry<class vostok::resources::managed_resource>(class vostok::resources::managed_resource *const, unsigned int) const` |
| 0.00 | `private: bool __thiscall vostok::resources::device_manager::do_async_operation(void **, class vostok::resources::query_result *, class vostok::fs_new::synchronous_device_interface const &, class vostok::mutable_buffer, unsigned __int64, bool)` |
| 0.00 | `private: bool __thiscall vostok::resources::device_manager::open_file(void ***, class vostok::resources::query_result *, class vostok::fs_new::synchronous_device_interface const &)` |
| 0.00 | `private: bool __thiscall vostok::resources::query_result::is_translate_query(void) const` |
| 0.00 | `private: bool __thiscall vostok::resources::query_result::process_request_path(bool)` |
| 0.00 | `private: bool __thiscall vostok::resources::query_result::retry_action_that_caused_out_of_memory(void)` |
| 0.00 | `private: bool __thiscall vostok::resources::resource_base::try_unregister_from_fat_or_from_name_registry(unsigned int)` |
| 0.00 | `private: bool __thiscall vostok::resources::resource_freeing_functionality::parents_can_be_freed(class vostok::resources::resource_base *, bool *, bool *)` |
| 0.00 | `private: bool __thiscall vostok::resources::resource_freeing_functionality::try_collect_parents_to_free(class vostok::resources::resource_base *)` |
| 0.00 | `private: bool __thiscall vostok::vfs::archive_mounter::read_sub_fat(class vostok::fs_new::synchronous_device_interface &)` |
| 0.00 | `private: bool __thiscall vostok::vfs::virtual_file_system::try_reference_to_pending_mount_unsafe(class vostok::vfs::query_mount_arguments &, bool *)` |
| 0.00 | `private: char __thiscall vostok::logging::log_file::read_next_char(void)` |
| 0.00 | `private: class vostok::ai::planning::base_lexeme_ptr __thiscall vostok::ai::planning::base_lexeme::expand_brackets_as_and(class vostok::memory::stack_allocator &, class vostok::ai::planning::base_lexeme const &) const` |
| 0.00 | `private: class vostok::ai::planning::base_lexeme_ptr __thiscall vostok::ai::planning::base_lexeme::expand_brackets_as_or(class vostok::memory::stack_allocator &) const` |
| 0.00 | `private: class vostok::ai::planning::base_lexeme_ptr __thiscall vostok::ai::planning::base_lexeme::expand_brackets_as_or(class vostok::memory::stack_allocator &, class vostok::ai::planning::base_lexeme const &) const` |
| 0.00 | `private: class vostok::ai::planning::base_lexeme_ptr __thiscall vostok::ai::planning::base_lexeme::generate_permutations_as_and(class vostok::memory::stack_allocator &, class vostok::ai::planning::base_lexeme const &) const` |
| 0.00 | `private: class vostok::ai::planning::base_lexeme_ptr __thiscall vostok::ai::planning::base_lexeme::generate_permutations_as_or(class vostok::memory::stack_allocator &, class vostok::ai::planning::base_lexeme const &) const` |
| 0.00 | `private: class vostok::animation::mixing::n_ary_tree_animation_node * __thiscall vostok::animation::mixing::n_ary_tree_transition_tree_constructor::add_animation(class vostok::animation::mixing::n_ary_tree_animation_node &, class vostok::animation::mixing::n_ary_tree_animation_node *const)` |
| 0.00 | `private: class vostok::animation::mixing::n_ary_tree_animation_node * __thiscall vostok::animation::mixing::n_ary_tree_transition_tree_constructor::new_weight_driving_animation(class vostok::animation::mixing::n_ary_tree_animation_node &)` |
| 0.00 | `private: class vostok::const_buffer __thiscall vostok::resources::query_result::pin_raw_buffer(void)` |
| 0.00 | `private: class vostok::math::float3 __thiscall survarium::bullet::compute_parabolic_position(float, class vostok::math::float3const &)` |
| 0.00 | `private: class vostok::math::float3 __thiscall survarium::bullet::compute_trajectory_position(float, class vostok::math::float3const &)` |
| 0.00 | `private: class vostok::math::float3 __thiscall survarium::bullet::compute_trajectory_velocity(float, class vostok::math::float3const &)` |
| 0.00 | `private: class vostok::math::float3 __thiscall survarium::weapon_core::get_dispersed_buckshot_direction(class vostok::math::float3const &)` |
| 0.00 | `private: class vostok::math::float4x4 __thiscall vostok::animation::bone_matrices_computer::computed_local_bone_matrix(class vostok::animation::skeleton_bone const &, unsigned int) const` |
| 0.00 | `private: class vostok::network_core::tcp_packet * __thiscall vostok::network_core::tcp_packet_socket<class boost::asio::basic_stream_socket<class boost::asio::ip::tcp, class boost::asio::stream_socket_service<class boost::asio::ip::tcp> > >::new_packet(void)` |
| 0.00 | `private: class vostok::network_core::udp_match_packet * __thiscall vostok::network_core::udp_match_connection::new_low_level_packet(unsigned char)` |
| 0.00 | `private: class vostok::sound::sound_collection * __thiscall vostok::sound::sound_collection_cook::create_collection(class vostok::configs::binary_config_value const &)` |
| 0.00 | `private: class vostok::vfs::base_node<1> * __thiscall vostok::vfs::physical_path_mounter::add_physical_node(class vostok::fs_new::virtual_path_string const &, class vostok::fs_new::virtual_path_string const &, unsigned int, class vostok::fs_new::native_path_string const &, class vostok::vfs::base_node<1> *)` |
| 0.00 | `private: enum vostok::animation::callback_return_type_enum __thiscall survarium::jump_logic_state_landing::on_interval_end(struct vostok::animation::animation_callback_params &)` |
| 0.00 | `private: enum vostok::animation::callback_return_type_enum __thiscall survarium::jump_logic_state_start::on_interval_end(struct vostok::animation::animation_callback_params &)` |
| 0.00 | `private: enum vostok::animation::callback_return_type_enum __thiscall survarium::jump_logic_state_start::on_jump_event(struct vostok::animation::animation_callback_params &)` |
| 0.00 | `private: enum vostok::animation::callback_return_type_enum __thiscall survarium::weapon_core_shotgun_reload_finish_substate::on_animation_end(struct vostok::animation::animation_callback_params &)` |
| 0.00 | `private: enum vostok::animation::callback_return_type_enum __thiscall survarium::weapon_core_shotgun_reload_one_round_substate::on_animation_end(struct vostok::animation::animation_callback_params &)` |
| 0.00 | `private: enum vostok::animation::callback_return_type_enum __thiscall survarium::weapon_core_shotgun_reload_start_substate::on_animation_end(struct vostok::animation::animation_callback_params &)` |
| 0.00 | `private: enum vostok::animation::callback_return_type_enum __thiscall survarium::weapon_user_animations_selector::on_interval_ended(struct vostok::animation::animation_callback_params &)` |
| 0.00 | `private: enum vostok::logging::verbosity __thiscall vostok::logging::node::get_verbosity(class vostok::logging::path_parts *, enum vostok::logging::verbosity) const` |
| 0.00 | `private: enum vostok::math::intersection __thiscall vostok::collision::colliders::cuboid_object::intersects_aabb(class vostok::math::float3const &, class vostok::math::float3const &) const` |
| 0.00 | `private: enum vostok::resources::allocation_result_enum __thiscall vostok::resources::query_result::allocate_final_managed_resource_if_needed(void)` |
| 0.00 | `private: enum vostok::resources::decrease_is_possible_bool __thiscall vostok::resources::quality_decreasing_functionality::collect_quality_resources(class vostok::resources::resource_base *, class vostok::intrusive_list<class vostok::resources::resource_base, class vostok::resources::resource_base *, 184, class vostok::threading::single_threading_policy, class vostok::size_policy, class vostok::no_debug_policy> *)` |
| 0.00 | `private: float __thiscall survarium::bullet::compute_max_error(float, float, class vostok::math::float3const &)` |
| 0.00 | `private: float __thiscall survarium::bullet::get_check_time_in_vacuum(float, float, class vostok::math::float3const &)` |
| 0.00 | `private: float __thiscall survarium::bullet::get_parabolic_time(void)` |
| 0.00 | `private: float __thiscall survarium::weapon_core::computed_backward_recoil_time(float, float, unsigned int, unsigned int, unsigned int, float)` |
| 0.00 | `private: float __thiscall survarium::weapon_core::computed_horizontal_recoil_time(float, float, unsigned int, unsigned int, unsigned int, float)` |
| 0.00 | `private: float __thiscall survarium::weapon_core::computed_vertical_recoil_time(float, float, unsigned int, unsigned int, unsigned int, float)` |
| 0.00 | `private: static void __cdecl vostok::animation::skeleton_animation_cook::on_cubic_spline_animation_cooked(class vostok::resources::queries_result &, class vostok::resources::resource_ptr<class vostok::animation::bi_spline_skeleton_animation_baked, class vostok::resources::unmanaged_intrusive_base>)` |
| 0.00 | `private: static void __cdecl vostok::buffer_vector<class vostok::tasks::thread_tls>::destroy(class vostok::tasks::thread_tls *, class vostok::tasks::thread_tls *const &)` |
| 0.00 | `private: struct survarium::game_action_descr * __thiscall survarium::key_binder::action_name_to_ptr(char const *)` |
| 0.00 | `private: struct survarium::keyboard_key_descr * __thiscall survarium::key_binder::keyname_to_ptr(char const *)` |
| 0.00 | `private: struct survarium::scheduler::record & __thiscall survarium::scheduler::register_object(struct survarium::scheduler::identifier *, class boost::function<void __cdecl (unsigned int, unsigned int)> const &, bool)` |
| 0.00 | `private: struct vostok::ai::planning::operands_calculator __thiscall vostok::ai::planning::base_lexeme::count_operands_as_and(void) const` |
| 0.00 | `private: struct vostok::ai::planning::operands_calculator __thiscall vostok::ai::planning::base_lexeme::count_operands_as_or(void) const` |
| 0.00 | `private: struct vostok::ai::planning::operands_calculator __thiscall vostok::ai::planning::base_lexeme::count_operands_as_predicate(void) const` |
| 0.00 | `private: struct vostok::animation::mixing::n_ary_tree_base_node * __thiscall vostok::animation::mixing::n_ary_tree_transition_tree_constructor::new_time_scale_transition(class vostok::animation::mixing::n_ary_tree_animation_node &, class vostok::animation::mixing::n_ary_tree_animation_node &, struct vostok::animation::mixing::n_ary_tree_base_node &, struct vostok::animation::mixing::n_ary_tree_base_node &)` |
| 0.00 | `private: struct vostok::ui::text * __thiscall vostok::console_impl::get_item(void)` |
| 0.00 | `private: unsigned int __thiscall vostok::resources::query_result::allocate_thread_id(void) const` |
| 0.00 | `private: unsigned short __thiscall vostok::ui::ui_text_edit::calc_right_word_position(unsigned short) const` |
| 0.00 | `private: virtual __thiscall survarium::medkit::~medkit(void)` |
| 0.00 | `private: virtual __thiscall survarium::oxygen_tank::~oxygen_tank(void)` |
| 0.00 | `private: virtual bool __thiscall survarium::breath_state_shortbreathing::is_ready_for_transition(void) const` |
| 0.00 | `private: virtual bool __thiscall survarium::jump_logic_state_start::is_ready_for_transition(void) const` |
| 0.00 | `private: virtual bool __thiscall survarium::ladder::ladder_occluder::use_execute(struct survarium::usable_object_user_data *)` |
| 0.00 | `private: virtual bool __thiscall survarium::player_logic_jump_state::is_ready_for_transition(void) const` |
| 0.00 | `private: virtual bool __thiscall survarium::weapon_core_shotgun_reload_start_substate::is_ready_for_transition(void) const` |
| 0.00 | `private: virtual bool __thiscall vostok::sound::encoded_sound_with_qualities::is_increasing_quality(void) const` |
| 0.00 | `private: virtual class vostok::math::aabb __thiscall vostok::collision::aabb_object::update_aabb(class vostok::math::float4x4const &)` |
| 0.00 | `private: virtual class vostok::render::world & __thiscall vostok::engine::engine_world::get_renderer_world(void)` |
| 0.00 | `private: virtual float __thiscall vostok::sound::encoded_sound_with_qualities::satisfaction_with(unsigned int, class vostok::resources::positional_unmanaged_resource const *, unsigned int) const` |
| 0.00 | `private: virtual struct vostok::sound::world & __thiscall vostok::engine::engine_world::get_sound_world(void)` |
| 0.00 | `private: virtual unsigned int __thiscall survarium::booby_trap_core_cook::get_derived_resource_size(void)` |
| 0.00 | `private: virtual unsigned int __thiscall survarium::weapon_core_cook::cooked_object_size(class survarium::weapon_core &) const` |
| 0.00 | `private: virtual unsigned int __thiscall vostok::memory::process_allocator::total_size(void) const` |
| 0.00 | `private: virtual void __stdcall vostok::sound::voice_bridge::OnBufferEnd(void *)` |
| 0.00 | `private: virtual void __stdcall vostok::sound::voice_bridge::OnVoiceError(void *, long)` |
| 0.00 | `private: virtual void __thiscall binary_tree_weight_driving_animation_getter::visit(class vostok::animation::mixing::binary_tree_addition_node &)` |
| 0.00 | `private: virtual void __thiscall survarium::booby_trap_core_cook::query_for_derived_resources(class vostok::resources::query_result_for_cook *, class survarium::booby_trap_core *, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>)` |
| 0.00 | `private: virtual void __thiscall survarium::booby_trap_set_core_cook::query_for_derived_resources(class vostok::resources::query_result_for_cook *, class survarium::booby_trap_set_core *, struct survarium::booby_trap_set_cook_data const &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>)` |
| 0.00 | `private: virtual void __thiscall survarium::jump_logic_state_landing::initialize(void)` |
| 0.00 | `private: virtual void __thiscall survarium::jump_logic_state_start::finalize(void)` |
| 0.00 | `private: virtual void __thiscall survarium::jump_logic_state_start::initialize(void)` |
| 0.00 | `private: virtual void __thiscall survarium::player_input_handler::on_after_processing(struct vostok::input::world *)` |
| 0.00 | `private: virtual void __thiscall survarium::player_input_handler::on_focus(bool)` |
| 0.00 | `private: virtual void __thiscall survarium::player_logic_crouch_state::finalize(void)` |
| 0.00 | `private: virtual void __thiscall survarium::player_logic_crouch_state::initialize(void)` |
| 0.00 | `private: virtual void __thiscall survarium::player_logic_jump_state::execute(void)` |
| 0.00 | `private: virtual void __thiscall survarium::rifle_scope_cook::delete_resource(class vostok::resources::resource_base *)` |
| 0.00 | `private: virtual void __thiscall survarium::weapon::instant_aim_end(void)` |
| 0.00 | `private: virtual void __thiscall survarium::weapon::instant_aim_start(void)` |
| 0.00 | `private: virtual void __thiscall survarium::weapon::set_next_ammo_type(void)` |
| 0.00 | `private: virtual void __thiscall survarium::weapon::set_next_fire_queue_type(void)` |
| 0.00 | `private: virtual void __thiscall survarium::weapon_cook::on_weapon_config_loaded(class vostok::resources::queries_result &)` |
| 0.00 | `private: virtual void __thiscall survarium::weapon_core::on_player_model_added(void)` |
| 0.00 | `private: virtual void __thiscall survarium::weapon_core::on_player_model_removed(void)` |
| 0.00 | `private: virtual void __thiscall survarium::weapon_core_hide_state_base::on_animation_end_impl(bool &)` |
| 0.00 | `private: virtual void __thiscall survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state>::finalize(void)` |
| 0.00 | `private: virtual void __thiscall survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_start_substate>::finalize(void)` |
| 0.00 | `private: virtual void __thiscall vostok::animation::mixing::binary_tree_expression_simplifier::visit(class vostok::animation::mixing::binary_tree_animation_node &)` |
| 0.00 | `private: virtual void __thiscall vostok::animation::mixing::binary_tree_expression_simplifier::visit(class vostok::animation::mixing::binary_tree_multiplication_node &)` |
| 0.00 | `private: virtual void __thiscall vostok::animation::mixing::binary_tree_expression_simplifier::visit(class vostok::animation::mixing::binary_tree_weight_node &)` |
| 0.00 | `private: virtual void __thiscall vostok::animation::mixing::binary_tree_initializer::visit(class vostok::animation::mixing::binary_tree_addition_node &)` |
| 0.00 | `private: virtual void __thiscall vostok::animation::mixing::binary_tree_weight_node::accept(struct vostok::animation::mixing::binary_tree_visitor &)` |
| 0.00 | `private: virtual void __thiscall vostok::animation::mixing::n_ary_tree_animation_time_calculator::visit(class vostok::animation::mixing::n_ary_tree_time_scale_node &)` |
| 0.00 | `private: virtual void __thiscall vostok::animation::mixing::n_ary_tree_destroyer::visit(class vostok::animation::mixing::n_ary_tree_addition_node &)` |
| 0.00 | `private: virtual void __thiscall vostok::animation::mixing::n_ary_tree_destroyer::visit(class vostok::animation::mixing::n_ary_tree_weight_transition_node &)` |
| 0.00 | `private: virtual void __thiscall vostok::animation::mixing::n_ary_tree_multiplication_node::visit(struct vostok::animation::mixing::n_ary_tree_double_dispatcher &, class vostok::animation::mixing::n_ary_tree_multiplication_node &)` |
| 0.00 | `private: virtual void __thiscall vostok::animation::mixing::n_ary_tree_node_comparer::dispatch(class vostok::animation::mixing::n_ary_tree_addition_node &, class vostok::animation::mixing::n_ary_tree_addition_node &)` |
| 0.00 | `private: virtual void __thiscall vostok::animation::mixing::n_ary_tree_node_comparer::dispatch(class vostok::animation::mixing::n_ary_tree_addition_node &, class vostok::animation::mixing::n_ary_tree_weight_node &)` |
| 0.00 | `private: virtual void __thiscall vostok::animation::mixing::n_ary_tree_node_comparer::dispatch(class vostok::animation::mixing::n_ary_tree_time_scale_node &, class vostok::animation::mixing::n_ary_tree_time_scale_node &)` |
| 0.00 | `private: virtual void __thiscall vostok::animation::mixing::n_ary_tree_node_comparer::dispatch(class vostok::animation::mixing::n_ary_tree_weight_node &, class vostok::animation::mixing::n_ary_tree_addition_node &)` |
| 0.00 | `private: virtual void __thiscall vostok::animation::mixing::n_ary_tree_node_comparer::dispatch(class vostok::animation::mixing::n_ary_tree_weight_node &, class vostok::animation::mixing::n_ary_tree_weight_node &)` |
| 0.00 | `private: virtual void __thiscall vostok::animation::mixing::n_ary_tree_node_comparer::dispatch(class vostok::animation::mixing::n_ary_tree_weight_node &, class vostok::animation::mixing::n_ary_tree_weight_transition_node &)` |
| 0.00 | `private: virtual void __thiscall vostok::animation::mixing::n_ary_tree_node_comparer::dispatch(class vostok::animation::mixing::n_ary_tree_weight_transition_node &, class vostok::animation::mixing::n_ary_tree_weight_node &)` |
| 0.00 | `private: virtual void __thiscall vostok::animation::mixing::n_ary_tree_node_comparer::dispatch(class vostok::animation::mixing::n_ary_tree_weight_transition_node &, class vostok::animation::mixing::n_ary_tree_weight_transition_node &)` |
| 0.00 | `private: virtual void __thiscall vostok::animation::mixing::n_ary_tree_size_calculator::visit(class vostok::animation::mixing::binary_tree_addition_node &)` |
| 0.00 | `private: virtual void __thiscall vostok::animation::mixing::n_ary_tree_time_scale_node::visit(struct vostok::animation::mixing::n_ary_tree_double_dispatcher &, class vostok::animation::mixing::n_ary_tree_time_scale_node &)` |
| 0.00 | `private: virtual void __thiscall vostok::animation::mixing::n_ary_tree_weaver::visit(class vostok::animation::mixing::binary_tree_animation_node &)` |
| 0.00 | `private: virtual void __thiscall vostok::animation::mixing::n_ary_tree_weight_node::accept(struct vostok::animation::mixing::n_ary_tree_visitor &)` |
| 0.00 | `private: virtual void __thiscall vostok::animation::skeleton_animation_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 0.00 | `private: virtual void __thiscall vostok::engine::engine_world::load_level(char const *)` |
| 0.00 | `private: virtual void __thiscall vostok::engine::engine_world::unload_level(void)` |
| 0.00 | `private: virtual void __thiscall vostok::memory::doug_lea_mt_allocator::finalize_impl(void)` |
| 0.00 | `private: virtual void __thiscall vostok::memory::doug_lea_mt_allocator::initialize_impl(void *, unsigned __int64, char const *)` |
| 0.00 | `private: virtual void __thiscall vostok::memory::managed_allocator::initialize_impl(void *, unsigned __int64, char const *)` |
| 0.00 | `private: virtual void __thiscall vostok::sound::encoded_sound_with_qualities::decrease_quality(unsigned int)` |
| 0.00 | `private: virtual void __thiscall vostok::sound::encoded_sound_with_qualities::increase_quality_to_target(class vostok::resources::query_result_for_cook *)` |
| 0.00 | `private: void __thiscall survarium::animated_model_instance_cook::on_config_loaded(class vostok::resources::queries_result &)` |
| 0.00 | `private: void __thiscall survarium::application::preinitialize(void)` |
| 0.00 | `private: void __thiscall survarium::body_part_parameters::apply_affects(class survarium::affects_threshold const *, unsigned int)` |
| 0.00 | `private: void __thiscall survarium::body_part_parameters::update_affects(unsigned int)` |
| 0.00 | `private: void __thiscall survarium::booby_trap_cook::on_models_ready(class vostok::resources::queries_result &, class survarium::booby_trap *)` |
| 0.00 | `private: void __thiscall survarium::booby_trap_set_cook::on_models_ready(class vostok::resources::queries_result &, class survarium::booby_trap_set *)` |
| 0.00 | `private: void __thiscall survarium::breath_vibration_calculator::initialize_logic(void)` |
| 0.00 | `private: void __thiscall survarium::bullet::change_trajectory(class vostok::math::float3const &, class vostok::math::float3const &, float)` |
| 0.00 | `private: void __thiscall survarium::bullet_manager::play_sound_impl(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float3const &)` |
| 0.00 | `private: void __thiscall survarium::bullet_manager::tick_bullets(unsigned int, unsigned int, unsigned int)` |
| 0.00 | `private: void __thiscall survarium::damage_model::on_broken_limb_affect(char const *, enum survarium::hit_affects_type_enum, enum survarium::affect_event_type_enum)` |
| 0.00 | `private: void __thiscall survarium::damage_model_cook::on_hit_params_received(class vostok::resources::queries_result &)` |
| 0.00 | `private: void __thiscall survarium::game::set_network_client(class survarium::base_network_client *const, char const *, unsigned short, bool)` |
| 0.00 | `private: void __thiscall survarium::game_material_manager::delete_pairs(void)` |
| 0.00 | `private: void __thiscall survarium::game_options::apply_default_graphic(void)` |
| 0.00 | `private: void __thiscall survarium::game_options::apply_key_bindings(void)` |
| 0.00 | `private: void __thiscall survarium::game_options::assign_binding(enum survarium::game_action_id, char const *)` |
| 0.00 | `private: void __thiscall survarium::game_options::on_resources_ready(class vostok::resources::queries_result &)` |
| 0.00 | `private: void __thiscall survarium::game_options::reset_bindings(bool)` |
| 0.00 | `private: void __thiscall survarium::game_world::switch_to_player_camera(bool)` |
| 0.00 | `private: void __thiscall survarium::game_world_ui::create_slot_value(enum survarium::profile_slot_enum, struct survarium::inventory_item_props &, struct survarium::flash_value &)` |
| 0.00 | `private: void __thiscall survarium::items_cook::create_item_and_finish_query(enum survarium::item_types_enum, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class vostok::resources::query_result_for_cook *)` |
| 0.00 | `private: void __thiscall survarium::jump_logic::initialize_logic(void)` |
| 0.00 | `private: void __thiscall survarium::lobby_menu::request_status_from_server_impl(unsigned int, unsigned int)` |
| 0.00 | `private: void __thiscall survarium::lobby_menu::show_disconnected_message(bool)` |
| 0.00 | `private: void __thiscall survarium::lobby_menu::update_status(void)` |
| 0.00 | `private: void __thiscall survarium::medkit::load(class vostok::configs::binary_config_value)` |
| 0.00 | `private: void __thiscall survarium::messaging_client::on_disconnected(void)` |
| 0.00 | `private: void __thiscall survarium::messaging_client::on_error(enum vostok::network_core::client_error_codes_enum, class boost::system::error_code)` |
| 0.00 | `private: void __thiscall survarium::messaging_client::update_channel_subscriptions(void)` |
| 0.00 | `private: void __thiscall survarium::network_client::on_http_error(class boost::system::error_code)` |
| 0.00 | `private: void __thiscall survarium::network_client::on_match_disconnected(enum vostok::network_core::disconnect_event_types_enum)` |
| 0.00 | `private: void __thiscall survarium::network_client::query_players(void)` |
| 0.00 | `private: void __thiscall survarium::object_vegetation::on_grass_loaded(class vostok::resources::queries_result &, class boost::function<void __cdecl (class survarium::game_object_&)> &)` |
| 0.00 | `private: void __thiscall survarium::oxygen_tank::load(class vostok::configs::binary_config_value)` |
| 0.00 | `private: void __thiscall survarium::player::remove_models_from_scene(void)` |
| 0.00 | `private: void __thiscall survarium::player_cook::on_hit_params_loaded(class vostok::resources::queries_result &, struct survarium::player_creation_params *)` |
| 0.00 | `private: void __thiscall survarium::player_stamina::regenerate(unsigned int)` |
| 0.00 | `private: void __thiscall survarium::project_cooker_simple::on_collision_and_visuals_loaded(class vostok::resources::queries_result &, class survarium::simple_game_project *)` |
| 0.00 | `private: void __thiscall survarium::shotgun_weapon_reload_state_cook::on_substates_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *)` |
| 0.00 | `private: void __thiscall survarium::weapon::load_weapon(class vostok::resources::resource_ptr<class vostok::render::skeleton_model_instance, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::rifle_scope, class vostok::resources::unmanaged_resource> const &)` |
| 0.00 | `private: void __thiscall survarium::weapon::update_pfx_transform(void)` |
| 0.00 | `private: void __thiscall survarium::weapon_cook::on_weapon_subresources_ready(class vostok::resources::queries_result &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class survarium::weapon_core *)` |
| 0.00 | `private: void __thiscall survarium::weapon_core::check_for_no_ammo_message(void)` |
| 0.00 | `private: void __thiscall survarium::weapon_core::check_for_sprint_transition(void)` |
| 0.00 | `private: void __thiscall survarium::weapon_core::load_ammo(void)` |
| 0.00 | `private: void __thiscall survarium::weapon_core_cook::on_weapon_states_ready(class vostok::resources::queries_result &, struct survarium::weapon_state_creation_params const *, class survarium::weapon_core *)` |
| 0.00 | `private: void __thiscall survarium::weapon_core_shotgun_reload_state::initialize_logic(class survarium::weapon_core_shotgun_reload_base_substate *, class survarium::weapon_core_shotgun_reload_base_substate *, class survarium::weapon_core_shotgun_reload_base_substate *)` |
| 0.00 | `private: void __thiscall survarium::weapon_core_state_cook_template<class survarium::double_barreled_weapon_core_idle_state>::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *)` |
| 0.00 | `private: void __thiscall survarium::weapon_core_state_cook_template<class survarium::pistol_weapon_core_idle_state>::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *)` |
| 0.00 | `private: void __thiscall survarium::weapon_core_state_cook_template<class survarium::weapon_core_idle_state>::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *)` |
| 0.00 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_fire_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_fire_state> >::config_params)` |
| 0.00 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_reload_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_reload_state> >::config_params)` |
| 0.00 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_fire_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_fire_state> >::config_params)` |
| 0.00 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_reload_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_reload_state> >::config_params)` |
| 0.00 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_chamber_a_round_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_chamber_a_round_state> >::config_params)` |
| 0.00 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_fire_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_fire_state> >::config_params)` |
| 0.00 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state> >::config_params)` |
| 0.00 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_reload_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_reload_state> >::config_params)` |
| 0.00 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_finish_substate> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_finish_substate> >::config_params)` |
| 0.00 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_one_round_substate> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_one_round_substate> >::config_params)` |
| 0.00 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_start_substate> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_start_substate> >::config_params)` |
| 0.00 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_show_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_show_state> >::config_params)` |
| 0.00 | `private: void __thiscall vostok::ai::planning::base_lexeme::add_to_effects_as_and(class vostok::ai::planning::generalized_action &) const` |
| 0.00 | `private: void __thiscall vostok::ai::planning::base_lexeme::add_to_preconditions_as_and(class vostok::ai::planning::generalized_action &) const` |
| 0.00 | `private: void __thiscall vostok::ai::planning::base_lexeme::add_to_preconditions_as_or(class vostok::ai::planning::generalized_action &) const` |
| 0.00 | `private: void __thiscall vostok::ai::planning::base_lexeme::add_to_target_world_state_as_and(class vostok::ai::planning::specified_problem &, unsigned int &) const` |
| 0.00 | `private: void __thiscall vostok::ai::planning::base_lexeme::invert_value_as_and(void) const` |
| 0.00 | `private: void __thiscall vostok::ai::planning::base_lexeme::invert_value_as_or(void) const` |
| 0.00 | `private: void __thiscall vostok::ai::planning::base_lexeme::invert_value_as_predicate(void) const` |
| 0.00 | `private: void __thiscall vostok::ai::planning::base_lexeme::reset_pointers(void) const` |
| 0.00 | `private: void __thiscall vostok::animation::animation_collection_cook::request_items(class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class vostok::configs::binary_config_value const &, class vostok::resources::query_result_for_cook *const)` |
| 0.00 | `private: void __thiscall vostok::animation::mixing::binary_tree_expression_simplifier::process<class vostok::animation::mixing::binary_tree_addition_node, struct stlp_std::plus<float> >(class vostok::animation::mixing::binary_tree_addition_node &, struct stlp_std::plus<float> const &)` |
| 0.00 | `private: void __thiscall vostok::animation::mixing::binary_tree_expression_simplifier::process<class vostok::animation::mixing::binary_tree_multiplication_node, struct stlp_std::multiplies<float> >(class vostok::animation::mixing::binary_tree_multiplication_node &, struct stlp_std::multiplies<float> const &)` |
| 0.00 | `private: void __thiscall vostok::animation::mixing::binary_tree_expression_simplifier::process<class vostok::animation::mixing::binary_tree_subtraction_node, struct stlp_std::minus<float> >(class vostok::animation::mixing::binary_tree_subtraction_node &, struct stlp_std::minus<float> const &)` |
| 0.00 | `private: void __thiscall vostok::animation::mixing::binary_tree_expression_simplifier::process_null_weight(struct stlp_std::multiplies<float> const &, class vostok::animation::mixing::binary_tree_expression_simplifier const &, class vostok::animation::mixing::binary_tree_expression_simplifier const &)` |
| 0.00 | `private: void __thiscall vostok::animation::mixing::n_ary_tree::accumulate_object_movement(class vostok::animation::mixing::n_ary_tree_animation_node &, float, unsigned int)` |
| 0.00 | `private: void __thiscall vostok::animation::mixing::n_ary_tree::destroy(void)` |
| 0.00 | `private: void __thiscall vostok::animation::mixing::n_ary_tree::remove_animations(unsigned int)` |
| 0.00 | `private: void __thiscall vostok::animation::mixing::n_ary_tree::set_object_transform(class vostok::animation::mixing::n_ary_tree_animation_node &)` |
| 0.00 | `private: void __thiscall vostok::animation::mixing::n_ary_tree::update_event_iterators(unsigned int)` |
| 0.00 | `private: void __thiscall vostok::animation::mixing::n_ary_tree_comparer::new_time_scale_transition(struct vostok::animation::mixing::n_ary_tree_base_node &, struct vostok::animation::mixing::n_ary_tree_base_node &)` |
| 0.00 | `private: void __thiscall vostok::animation::mixing::n_ary_tree_event_iterator::select_state(void)` |
| 0.00 | `private: void __thiscall vostok::animation::mixing::n_ary_tree_size_calculator::propagate(class vostok::animation::mixing::binary_tree_binary_operation_node &)` |
| 0.00 | `private: void __thiscall vostok::collision::colliders::aabb_geometry::add_triangle(unsigned int) const` |
| 0.00 | `private: void __thiscall vostok::collision::colliders::aabb_geometry::test_primitive(unsigned int) const` |
| 0.00 | `private: void __thiscall vostok::collision::colliders::cuboid_geometry::add_triangle(unsigned int) const` |
| 0.00 | `private: void __thiscall vostok::collision::colliders::ray_query_geometry::test_primitive(unsigned int const &)` |
| 0.00 | `private: void __thiscall vostok::collision::collision_cook::on_triangle_mesh_collision_loaded(class vostok::resources::queries_result &, class vostok::resources::query_result_for_cook *)` |
| 0.00 | `private: void __thiscall vostok::collision::collision_cook::query_triangle_mesh(class vostok::resources::query_result_for_cook *)` |
| 0.00 | `private: void __thiscall vostok::engine::engine_world::enable_game_impl(bool)` |
| 0.00 | `private: void __thiscall vostok::engine::engine_world::initialize_logic_thread(void)` |
| 0.00 | `private: void __thiscall vostok::engine::engine_world::initialize_resources(void)` |
| 0.00 | `private: void __thiscall vostok::engine::engine_world::initialize_sound_modules(void)` |
| 0.00 | `private: void __thiscall vostok::engine::engine_world::logic(void)` |
| 0.00 | `private: void __thiscall vostok::engine::engine_world::logic_clear_resources(void)` |
| 0.00 | `private: void __thiscall vostok::engine::engine_world::network(void)` |
| 0.00 | `private: void __thiscall vostok::engine::engine_world::sound(void)` |
| 0.00 | `private: void __thiscall vostok::engine::engine_world::terminate_on_timeout(float)` |
| 0.00 | `private: void __thiscall vostok::fs_new::asynchronous_device_interface::get_synchronous_access(class vostok::fs_new::synchronous_device_interface *, class vostok::memory::base_allocator *)` |
| 0.00 | `private: void __thiscall vostok::fs_new::asynchronous_device_interface::push_query(class vostok::fs_new::asynchronous_device_query *)` |
| 0.00 | `private: void __thiscall vostok::intrusive_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock>::dec(void)` |
| 0.00 | `private: void __thiscall vostok::logging::filter_tree::build_tree(void)` |
| 0.00 | `private: void __thiscall vostok::network::http_client::create_client_impl(void)` |
| 0.00 | `private: void __thiscall vostok::network::http_client::get_impl(char const *, char const *)` |
| 0.00 | `private: void __thiscall vostok::network::http_client::on_error(class boost::system::error_code)` |
| 0.00 | `private: void __thiscall vostok::network::login_client_impl::close_connection(bool)` |
| 0.00 | `private: void __thiscall vostok::network::login_client_impl::connect(enum vostok::resolve_error_types_enum, class boost::asio::ip::basic_resolver_iterator<class boost::asio::ip::tcp>, unsigned int, class boost::function<void __cdecl (enum vostok::connection_error_types_enum)> const &)` |
| 0.00 | `private: void __thiscall vostok::network::login_client_impl::handshake(class boost::function<void __cdecl (enum vostok::handshaking_error_types_enum)> const &, unsigned int, bool)` |
| 0.00 | `private: void __thiscall vostok::network::login_client_impl::on_connected(unsigned int, class boost::function<void __cdecl (enum vostok::connection_error_types_enum)> const &, class boost::asio::ip::basic_resolver_iterator<class boost::asio::ip::tcp>, class boost::system::error_code const &, class boost::asio::ip::basic_resolver_iterator<class boost::asio::ip::tcp>)` |
| 0.00 | `private: void __thiscall vostok::network::login_client_impl::on_handshaked(class boost::system::error_code const &, class boost::function<void __cdecl (enum vostok::handshaking_error_types_enum)> const &, unsigned int, bool)` |
| 0.00 | `private: void __thiscall vostok::network::login_client_impl::ping(unsigned int)` |
| 0.00 | `private: void __thiscall vostok::network::login_client_impl::resolve(class boost::function<void __cdecl (enum vostok::resolve_error_types_enum, class boost::asio::ip::basic_resolver_iterator<class boost::asio::ip::tcp>)> const &, unsigned int)` |
| 0.00 | `private: void __thiscall vostok::network::match_client::create_client(struct vostok::network_core::udp_network_flow_emulator_options const *)` |
| 0.00 | `private: void __thiscall vostok::network::match_client::create_responses_packets_allocator(void)` |
| 0.00 | `private: void __thiscall vostok::network::match_client::on_disconnect(enum vostok::network_core::disconnect_event_types_enum)` |
| 0.00 | `private: void __thiscall vostok::network::match_client::on_disconnect_impl(enum vostok::network_core::disconnect_event_types_enum)` |
| 0.00 | `private: void __thiscall vostok::network::match_client_impl::on_disconnect(enum vostok::network_core::disconnect_event_types_enum)` |
| 0.00 | `private: void __thiscall vostok::network::tcp_packet_client::create_client(void)` |
| 0.00 | `private: void __thiscall vostok::network::tcp_packet_client::on_connected(void)` |
| 0.00 | `private: void __thiscall vostok::network::tcp_packet_client::on_connected_impl(void)` |
| 0.00 | `private: void __thiscall vostok::network::tcp_packet_client::on_disconnected(void)` |
| 0.00 | `private: void __thiscall vostok::network::tcp_packet_client::on_disconnected_impl(void)` |
| 0.00 | `private: void __thiscall vostok::network::tcp_packet_client::on_error(enum vostok::network_core::client_error_codes_enum, class boost::system::error_code)` |
| 0.00 | `private: void __thiscall vostok::network::tcp_packet_client::on_packet_received(class vostok::network_core::tcp_packet const &)` |
| 0.00 | `private: void __thiscall vostok::network_core::http_client::close_connection(void)` |
| 0.00 | `private: void __thiscall vostok::network_core::http_client::handle_connect(class boost::system::error_code const &, class boost::asio::ip::basic_resolver_iterator<class boost::asio::ip::tcp>)` |
| 0.00 | `private: void __thiscall vostok::network_core::http_client::handle_read_content(class boost::system::error_code const &)` |
| 0.00 | `private: void __thiscall vostok::network_core::http_client::handle_read_status_line(class boost::system::error_code const &)` |
| 0.00 | `private: void __thiscall vostok::network_core::http_client::handle_resolve(class boost::system::error_code const &, class boost::asio::ip::basic_resolver_iterator<class boost::asio::ip::tcp>)` |
- _...and 4126 more_

### Added (4163)

- `??__G@YGXPAX0IHP6EPAX00@Z@Z`
- `?set_size@render_output_window@render@vostok@@QAEXII_N_N1@Z`
- `?set_size@res_render_output@render@vostok@@QAEXII_N_N1@Z`
- `_ogg_calloc_impl`
- `_ogg_free_impl`
- `_ogg_malloc_impl`
- `_ogg_realloc_impl`
- ``survarium::hit_animations_selector::selected_animations'::`2'::hit_body_part_greater::operator()`
- ``vostok::particle::particle_world::get_render_emitter_instances'::`2'::emitters_sort_by_priority_pridicate::operator()`
- ``vostok::render::render_particle_emitter_instance::sort_particles'::`4'::particle_sort_predicate::operator()`
- ``vostok::render::scene::process_streaming'::`51'::remove_texture_predicate::operator()`
- ``vostok::render::scene::process_streaming'::`6'::remove_requested_texture_predicate::operator()`
- ``vostok::render::stage_visibility::filter_and_sort_ambient_lights'::`4'::sort_ambient_lights_by_size_predicate::operator()`
- ``vostok::render::stage_visibility::filter_and_sort_env_probes'::`4'::sort_by_size_predicate::operator()`
- `ag_zeroin2`
- `animation_index`
- `bool __cdecl survarium::are_different(struct survarium::player_input const &, struct survarium::player_input const &)`
- `bool __cdecl survarium::load_quest_descriptor(struct survarium::quest_descriptor &, class vostok::configs::binary_config_value)`
- `bool __cdecl survarium::operator==(struct survarium::player_input const &, struct survarium::player_input const &)`
- `bool __cdecl vostok::console_commands::execute_console_commands(class vostok::fs_new::native_path_string, enum vostok::console_commands::execution_filter, unsigned int)`
- `bool __cdecl vostok::platform::is_address_space_or_ram_under_2_gb(void)`
- `bool __cdecl vostok::render::is_material_stages_index(unsigned int)`
- `bool __cdecl vostok::render::operator==(struct vostok::render::hw_buffer_pool_range const &, struct vostok::render::hw_buffer_pool_range const &)`
- `bool __cdecl vostok::render::reclaim<class vostok::render::res_render_output, 64>(class vostok::fixed_vector<class vostok::render::res_render_output *, 64> &, class vostok::render::res_render_output const *)`
- `bool __cdecl vostok::resources::check_queries_result(class vostok::resources::queries_result &)`
- `bool __cdecl vostok::strings::starts_with(char const *const, char const *const)`
- `char * __cdecl vostok::strings::copy<16>(char (&)[16], char const *)`
- `char * __cdecl vostok::strings::copy<260>(char (&)[260], char const *)`
- `char * __cdecl vostok::strings::copy_n(char *const, unsigned int, char const *const, unsigned int)`
- `char * __cdecl vostok::strings::duplicate<class vostok::memory::stack_allocator>(class vostok::memory::stack_allocator &, char const *const)`
- `char const * __cdecl vostok::animation::get_locator_format_string(char const * (&)[2][3], class vostok::render::render_model_instance const &, unsigned int, enum vostok::animation::fingers_to_weapon_corrector::hands_enum, bool)`
- `char const * __cdecl vostok::logging::verbosity_name(enum vostok::logging::verbosity)`
- `char const * __cdecl vostok::render::game::`anonymous namespace'::const_cstr<class vostok::fixed_string<128> >(class vostok::fixed_string<128> const &)`
- `checkMonotonic`
- `class btBvhTriangleMeshShape * __cdecl vostok::physics::create_btBvhTriangleMeshShape(class vostok::math::float3*, unsigned int *, unsigned int, unsigned int, unsigned short const *const, class vostok::math::float3const &, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &)`
- `class btCollisionShape * __cdecl vostok::physics::create_bt_primitive(enum vostok::collision::primitive_type, class vostok::math::float3const &, class vostok::math::float3const &, class vostok::memory::base_allocator *)`
- `class btVector3 __cdecl vostok::physics::capsule_bottom_to_center_position(class btVector3const &, class btCapsuleShape const &, class btVector3const &)`
- `class btVector3 __cdecl vostok::physics::capsule_center_to_bottom_position(class btVector3const &, class btCapsuleShape const &, class btVector3const &)`
- `class btVector3 __cdecl vostok::physics::normalized_safe(class btVector3const &, class btVector3const &)`
- `class vostok::animation::mixing::addition_lexeme & __cdecl vostok::animation::mixing::operator+<class vostok::animation::mixing::animation_lexeme, class vostok::animation::mixing::animation_lexeme>(class vostok::animation::mixing::animation_lexeme &, class vostok::animation::mixing::animation_lexeme &)`
- `class vostok::animation::mixing::expression __cdecl vostok::animation::mixing::operator*(class vostok::animation::mixing::expression &, class vostok::animation::mixing::expression &)`
- `class vostok::animation::mixing::n_ary_tree_animation_node * __cdecl vostok::animation::mixing::find_animation(class boost::function<unsigned char __cdecl (void const *)> const &, class vostok::animation::mixing::n_ary_tree_animation_node *const, class vostok::animation::mixing::n_ary_tree_animation_node *const, class vostok::animation::mixing::n_ary_tree_animation_node &)`
- `class vostok::fixed_string<128> __cdecl vostok::fs_new::file_open_flags_to_string(enum vostok::fs_new::file_mode::mode_enum, enum vostok::fs_new::file_access::access_enum)`
- `class vostok::fixed_string<260> __cdecl vostok::render::make_effect_name(char const *, class vostok::resources::resource_ptr<class vostok::render::material, class vostok::resources::unmanaged_intrusive_base> const &, unsigned int)`
- `class vostok::fixed_string<260> __cdecl vostok::render::make_shader_name(char const *, struct vostok::render::shader_configuration const &, enum vostok::render::enum_shader_type)`
- `class vostok::logging::log_file * __cdecl vostok::logging::new_log_file(class vostok::logging::base_allocator &, class vostok::logging::base_fs_device &, char const *, enum vostok::logging::log_file_usage_enum)`
- `class vostok::math::aabb __cdecl vostok::math::create_identity_aabb(void)`
- `class vostok::math::aabb __cdecl vostok::math::create_invalid_aabb(void)`
- `class vostok::math::aabb __cdecl vostok::math::operator*(class vostok::math::aabb const &, float)`
- `class vostok::math::float3 __cdecl survarium::get_air_control_vector(struct survarium::player_input const &, float, enum survarium::jump_type_enum)`
- `class vostok::math::float3 __cdecl vostok::math::abs(class vostok::math::float3const &)`
- `class vostok::math::float3 __cdecl vostok::math::slerp(class vostok::math::float3const &, class vostok::math::float3const &, float, class vostok::math::float3const &)`
- `class vostok::math::float3 __cdecl vostok::physics::dimensions_from_bullet_shape(class btCollisionShape const *)`
- `class vostok::math::float3 __cdecl vostok::physics::get_box_random_surface_point(class vostok::math::random32&)`
- `class vostok::math::float3 __cdecl vostok::physics::get_capsule_random_surface_point(class vostok::math::random32&, float, float)`
- `class vostok::math::float3 __cdecl vostok::physics::get_cylinder_random_surface_point(class vostok::math::random32&)`
- `class vostok::math::float3 __cdecl vostok::physics::get_sphere_random_surface_point(class vostok::math::random32&)`
- `class vostok::math::float3_pod __cdecl vostok::math::cubic_interpolation<class vostok::math::float3_pod, float>(class vostok::math::float3_pod, class vostok::math::float3_pod, class vostok::math::float3_pod, class vostok::math::float3_pod, float)`
- `class vostok::math::float4 __cdecl vostok::render::convert_to_linear_space(class vostok::math::float4const &)`
- `class vostok::math::float4x4 __cdecl vostok::animation::get_bone_matrix_in_object_space(class vostok::animation::skeleton_bone const &, class vostok::animation::skeleton const &, class vostok::math::float4x4const *)`
- `class vostok::math::float4x4 __cdecl vostok::animation::get_bone_matrix_in_object_space_impl(class vostok::animation::skeleton_bone const &, class vostok::math::float4x4const *, class vostok::animation::skeleton_bone const *)`
- `class vostok::math::float4x4 __cdecl vostok::animation::mix_transformations(class vostok::math::float4x4const &, class vostok::math::float4x4const &, float, float)`
- `class vostok::math::float4x4 __cdecl vostok::math::create_uniform_scale(float const &)`
- `class vostok::math::quaternion __cdecl vostok::math::operator*(class vostok::math::quaternion const &, class vostok::math::quaternion const &)`
- `class vostok::network_core::udp_match_packet * __cdecl vostok::network_core::new_udp_match_packet(class vostok::memory::single_size_buffer_allocator<1364, class vostok::threading::multi_threading_policy> &)`
- `class vostok::physics::bt_dynamic_rigid_body * __cdecl vostok::physics::create_dynamic_rigid_body(struct vostok::physics::bt_rigid_body_construction_info const &, class vostok::physics::bt_collision_shape *)`
- `class vostok::resources::resource_ptr<class survarium::server_game_project, class vostok::resources::unmanaged_intrusive_base> __cdecl vostok::static_cast_resource_ptr<class vostok::resources::resource_ptr<class survarium::server_game_project, class vostok::resources::unmanaged_intrusive_base>, class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `class vostok::resources::resource_ptr<class survarium::weapon_core, class vostok::resources::unmanaged_intrusive_base> __cdecl vostok::static_cast_resource_ptr<class vostok::resources::resource_ptr<class survarium::weapon_core, class vostok::resources::unmanaged_intrusive_base>, class survarium::inventory_item, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::resource_ptr<class survarium::inventory_item, class vostok::resources::unmanaged_intrusive_base> const &)`
- `class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> __cdecl vostok::static_cast_resource_ptr<class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base>, class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `class vostok::resources::resource_ptr<class survarium::weapon_core_shotgun_reload_base_substate, class vostok::resources::unmanaged_intrusive_base> __cdecl vostok::static_cast_resource_ptr<class vostok::resources::resource_ptr<class survarium::weapon_core_shotgun_reload_base_substate, class vostok::resources::unmanaged_intrusive_base>, class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `class vostok::resources::resource_ptr<class vostok::render::grass_render_model, class vostok::resources::unmanaged_intrusive_base> __cdecl vostok::static_cast_resource_ptr<class vostok::resources::resource_ptr<class vostok::render::grass_render_model, class vostok::resources::unmanaged_intrusive_base>, class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `class vostok::resources::resource_ptr<class vostok::render::scene, class vostok::resources::unmanaged_resource> __cdecl vostok::static_cast_resource_ptr<class vostok::resources::resource_ptr<class vostok::render::scene, class vostok::resources::unmanaged_resource>, struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &)`
- `convert_channels_ids`
- `disabled_channel_ids`
- `engineBezierCreate`
- `engineBezierEvaluate`
- `enum survarium::hit_type_enum __cdecl survarium::hit_type(char const *const)`
- `enum survarium::move_direction_enum __cdecl survarium::get_move_direction(struct survarium::player_input const &)`
- `enum vostok::journaling::journal_usage_enum __cdecl vostok::core::journal_usage(void)`
- `evaluateInfinities`
- `find`
- `float __cdecl survarium::read_value_if_exists<float>(class vostok::configs::binary_config_value const &, char const *, float)`
- `float __cdecl vostok::animation::engineAnimEvaluate(struct vostok::animation::EtCurve *, float)`
- `float __cdecl vostok::math::smoothstep(float, float, float)`
- `float __cdecl vostok::particle::fractalsum1(float, float, unsigned int, unsigned int)`
- `float __cdecl vostok::particle::noise1(float, int, unsigned int)`
- `float __cdecl vostok::physics::get_surface_area(class btCollisionShape const *)`
- `float __cdecl vostok::render::fast_log2(float)`
- `int __cdecl CanLaunchMultiplayerGameA(char *)`
- `int __cdecl CanLaunchMultiplayerGameW(wchar_t *)`
- `int __cdecl sprintf_s<4096>(char (&)[4096], char const *, ...)`
- `int __cdecl sprintf_s<512>(char (&)[512], char const *, ...)`
- `int __cdecl vostok::console_commands::bool_from_string(char const *, bool &)`
- `int __cdecl vostok::operator-(class vostok::circular_buffer<class vostok::network_core::sequence_number<unsigned short>, 8>::iterator const &, class vostok::circular_buffer<class vostok::network_core::sequence_number<unsigned short>, 8>::iterator const &)`
- `int __cdecl vostok::operator-(class vostok::circular_buffer<struct stlp_std::pair<enum survarium::game_action_id, enum survarium::action_state_enum>, 64>::const_iterator const &, class vostok::circular_buffer<struct stlp_std::pair<enum survarium::game_action_id, enum survarium::action_state_enum>, 64>::const_iterator const &)`
- `int __cdecl vostok::operator-(class vostok::circular_buffer<struct survarium::fx_history_item, 10>::iterator const &, class vostok::circular_buffer<struct survarium::fx_history_item, 10>::iterator const &)`
- `int __cdecl vostok::particle::initNoise(void)`
- `int __cdecl vostok::particle::read_config_value<int, class vostok::configs::binary_config_value>(class vostok::configs::binary_config_value const &, char const *, int const &)`
- `polyZeroes`
- `private: __thiscall survarium::artefact<class survarium::artefact_lifebone_core>::artefact<class survarium::artefact_lifebone_core>(class vostok::configs::binary_config_value const &, class vostok::resources::resource_ptr<class survarium::game_effect_emitter, class vostok::resources::unmanaged_intrusive_base> const &, class survarium::base_game_scene *)`
- `private: __thiscall survarium::artefact<class survarium::artefact_onyx_core>::artefact<class survarium::artefact_onyx_core>(class vostok::configs::binary_config_value const &, class vostok::resources::resource_ptr<class survarium::game_effect_emitter, class vostok::resources::unmanaged_intrusive_base> const &, class survarium::base_game_scene *)`
- `private: __thiscall survarium::artefact<class survarium::artefact_rattle_core>::artefact<class survarium::artefact_rattle_core>(class vostok::configs::binary_config_value const &, class vostok::resources::resource_ptr<class survarium::game_effect_emitter, class vostok::resources::unmanaged_intrusive_base> const &, class survarium::base_game_scene *)`
- `private: __thiscall survarium::artefact<class survarium::artefact_spring_core>::artefact<class survarium::artefact_spring_core>(class vostok::configs::binary_config_value const &, class vostok::resources::resource_ptr<class survarium::game_effect_emitter, class vostok::resources::unmanaged_intrusive_base> const &, class survarium::base_game_scene *)`
- `private: __thiscall survarium::booby_trap::booby_trap(class survarium::base_game_scene &, struct vostok::physics::world &)`
- `private: __thiscall survarium::booby_trap_set::booby_trap_set(class survarium::base_game_scene &, struct vostok::physics::world &, class vostok::resources::resource_ptr<class survarium::game_material_manager, class vostok::resources::unmanaged_intrusive_base> const &)`
- `private: __thiscall survarium::composite_game_effect::composite_game_effect(class vostok::resources::resource_ptr<class survarium::pure_game_effect_emitter_base, class vostok::resources::unmanaged_intrusive_base>, float)`
- `private: __thiscall survarium::game_effect_emitter::game_effect_emitter(class vostok::resources::resource_ptr<class survarium::pure_game_effect_emitter, class vostok::resources::unmanaged_intrusive_base>)`
- `private: __thiscall survarium::gather_victory_items_rule::gather_victory_items_rule(unsigned int)`
- `private: __thiscall survarium::generic_anomaly::generic_anomaly(class survarium::base_game_scene &, class vostok::resources::resource_ptr<class survarium::artefact_base, class vostok::resources::unmanaged_intrusive_base> const *, unsigned int, unsigned int)`
- `private: __thiscall survarium::grenade::grenade(class survarium::base_game_scene &)`
- `private: __thiscall survarium::hud_game_effect::hud_game_effect(class vostok::resources::resource_ptr<class survarium::pure_game_effect_emitter_base, class vostok::resources::unmanaged_intrusive_base>, enum survarium::hud_effects_enum, unsigned char, class survarium::value_animation<float, class survarium::hud_game_effect_emitter_cook> const *)`
- `private: __thiscall survarium::particle_game_effect::particle_game_effect(class vostok::resources::resource_ptr<class survarium::pure_game_effect_emitter_base, class vostok::resources::unmanaged_intrusive_base>, class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &, float, class survarium::value_animation<float, class survarium::particle_game_effect_emitter_cook> const *)`
- `private: __thiscall survarium::player_respawn_rule::player_respawn_rule(unsigned int, class vostok::configs::binary_config const &, struct vostok::physics::world &)`
- `private: __thiscall survarium::post_process_game_effect::post_process_game_effect(class vostok::resources::resource_ptr<class survarium::pure_game_effect_emitter_base, class vostok::resources::unmanaged_intrusive_base>, class survarium::value_animation<struct vostok::render::environment_properties, class survarium::post_process_game_effect_emitter_cook> const *)`
- `private: __thiscall survarium::pvp_match_core::pvp_match_core(bool, bool, struct survarium::match_options const &, class vostok::resources::resource_ptr<class survarium::server_game_project, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::game_material_manager, class vostok::resources::unmanaged_intrusive_base> const &, class survarium::bullet_manager_engine &, struct vostok::physics::world &, class vostok::resources::resource_ptr<class survarium::base_player, class vostok::resources::unmanaged_intrusive_base> const *, class vostok::resources::resource_ptr<class survarium::base_player, class vostok::resources::unmanaged_intrusive_base> const *, class vostok::resources::resource_ptr<class survarium::game_match_rule_base, class vostok::resources::unmanaged_intrusive_base> const *, class vostok::resources::resource_ptr<class survarium::game_match_rule_base, class vostok::resources::unmanaged_intrusive_base> const *)`
- `private: __thiscall survarium::sound_game_effect::sound_game_effect(class vostok::resources::resource_ptr<class survarium::pure_game_effect_emitter_base, class vostok::resources::unmanaged_intrusive_base>, class vostok::resources::resource_ptr<class vostok::sound::sound_emitter, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::sound::sound_emitter, class vostok::resources::unmanaged_intrusive_base> const &, class survarium::value_animation<struct survarium::sound_game_effect::properties, class survarium::sound_game_effect_emitter_cook> const *)`
- `private: __thiscall survarium::sound_game_effect_emitter::sound_game_effect_emitter(class vostok::resources::resource_ptr<class vostok::sound::sound_emitter, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::sound::sound_emitter, class vostok::resources::unmanaged_intrusive_base> const &, class survarium::value_animation<struct survarium::sound_game_effect::properties, class survarium::sound_game_effect_emitter_cook> const *)`
- `private: __thiscall survarium::victory_item::victory_item(class survarium::game_world &, struct vostok::physics::world &)`
- `private: __thiscall survarium::victory_items_container::victory_items_container(struct vostok::physics::world &, class survarium::gather_victory_items_rule &, class vostok::configs::binary_config_value const &, struct survarium::victory_items_container::victory_item_transform const *, unsigned int)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_fire_state>::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_fire_state>(class survarium::weapon &, enum survarium::weapon_fx_enum, class survarium::base_game_scene &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_reload_state>::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_reload_state>(class survarium::weapon &, enum survarium::weapon_fx_enum, class survarium::base_game_scene &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_fire_state>::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_fire_state>(class survarium::weapon &, enum survarium::weapon_fx_enum, class survarium::base_game_scene &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_reload_state>::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_reload_state>(class survarium::weapon &, enum survarium::weapon_fx_enum, class survarium::base_game_scene &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::weapon_core_chamber_a_round_state>::weapon_sound_events_handler_state<class survarium::weapon_core_chamber_a_round_state>(class survarium::weapon &, enum survarium::weapon_fx_enum, class survarium::base_game_scene &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::weapon_core_fire_state>::weapon_sound_events_handler_state<class survarium::weapon_core_fire_state>(class survarium::weapon &, enum survarium::weapon_fx_enum, class survarium::base_game_scene &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state>::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state>(class survarium::weapon &, enum survarium::weapon_fx_enum, class survarium::base_game_scene &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::weapon_core_reload_state>::weapon_sound_events_handler_state<class survarium::weapon_core_reload_state>(class survarium::weapon &, enum survarium::weapon_fx_enum, class survarium::base_game_scene &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_finish_substate>::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_finish_substate>(class survarium::weapon &, enum survarium::weapon_fx_enum, class survarium::base_game_scene &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_one_round_substate>::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_one_round_substate>(class survarium::weapon &, enum survarium::weapon_fx_enum, class survarium::base_game_scene &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_start_substate>::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_start_substate>(class survarium::weapon &, enum survarium::weapon_fx_enum, class survarium::base_game_scene &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::weapon_core_show_state>::weapon_sound_events_handler_state<class survarium::weapon_core_show_state>(class survarium::weapon &, enum survarium::weapon_fx_enum, class survarium::base_game_scene &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall vostok::resources::pinned_ptr_mutable<struct vostok::render::texture_data_resource>::pinned_ptr_mutable<struct vostok::render::texture_data_resource>(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>)`
- `private: __thiscall vostok::resources::queries_result::queries_result(unsigned int, class boost::function<void __cdecl (class vostok::resources::queries_result &)> const &, class vostok::memory::base_allocator *, unsigned int, class vostok::resources::query_result_for_cook *, float *, bool const *, unsigned int const *, enum vostok::resources::query_type_enum, enum vostok::resources::autoselect_quality_bool const *, enum assert_on_fail_bool)`
- `private: __thiscall vostok::sound::voice_bridge::voice_bridge(struct vostok::sound::voice_bridge::creation_parametrs &, unsigned int)`
- `private: bool __thiscall character_step_down_sweep_test_callback::is_side_contact(class btVector3const &, class btVector3const &) const`
- `private: bool __thiscall survarium::booby_trap_set_core::try_to_place_trap(void)`
- `private: bool __thiscall survarium::breath_vibration_calculator::can_hold_breath(void) const`
- `private: bool __thiscall survarium::breath_vibration_calculator::not_holding_breath(void) const`
- `private: bool __thiscall survarium::bullet::try_pierce(struct vostok::physics::closest_ray_result const &, class vostok::math::float3const &, struct survarium::hit_receiver *const, enum survarium::triangle_orientation)`
- `private: bool __thiscall survarium::bullet::try_reflect(struct vostok::physics::closest_ray_result const &, class vostok::math::float3const &)`
- `private: bool __thiscall survarium::game_world_core::erase_impl(unsigned char, enum survarium::game_event_history_item::events_enum, unsigned int, bool)`
- `private: bool __thiscall survarium::messaging_client::read_found_players(class vostok::network_core::buffer_reader &)`
- `private: bool __thiscall survarium::messaging_client::read_friend_list(class vostok::network_core::buffer_reader &)`
- `private: bool __thiscall survarium::messaging_client::read_friend_status(class vostok::network_core::buffer_reader &)`
- `private: bool __thiscall survarium::messaging_client::read_ignore_list(class vostok::network_core::buffer_reader &)`
- `private: bool __thiscall survarium::player_input_handler::action_present(enum survarium::game_action_id, enum survarium::action_state_enum &) const`
- `private: bool __thiscall survarium::victory_item_core::put_predicate(void) const`
- `private: bool __thiscall survarium::weapon_core::is_going_to_jump(void) const`
- `private: bool __thiscall survarium::weapon_core::is_going_to_sprint(void) const`
- `private: bool __thiscall survarium::weapon_core::melee_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::throw_grenade_pred(void) const`
- `private: bool __thiscall survarium::weapon_user_animations_selector::alive_predicate(void) const`
- `private: bool __thiscall survarium::weapon_user_animations_selector::dead_predicate(void) const`
- `private: bool __thiscall survarium::weapon_user_animations_selector::is_trying_to_aim(void) const`
- `private: bool __thiscall vostok::animation::animation_player::tick_impl(unsigned int, unsigned int, bool)`
- `private: bool __thiscall vostok::animation::mixing::n_ary_tree::process_event(class vostok::animation::mixing::n_ary_tree_animation_node &, unsigned int)`
- `private: bool __thiscall vostok::animation::mixing::n_ary_tree::update_event_iterators_and_dispatch_callbacks(unsigned int, struct vostok::animation::subscribed_channel *&, bool &, unsigned int)`
- `private: bool __thiscall vostok::network_core::udp_match_connection::update_acknowledgements(class vostok::network_core::sequence_number<unsigned short>, class vostok::network_core::sequence_number<unsigned short>, unsigned __int64)`
- `private: bool __thiscall vostok::physics::bullet_character_controller::can_straighten(class btVector3const &, float, class btVector3&) const`
- `private: bool __thiscall vostok::physics::bullet_character_controller::impassable_slope(class btVector3const &, class btVector3const &, class btVector3const &) const`
- `private: bool __thiscall vostok::physics::bullet_character_controller::on_steep_slope(void) const`
- `private: bool __thiscall vostok::physics::bullet_character_controller::side_slide_on_low_ceiling(class btVector3const &, class btVector3const &, class btVector3const &, float, float, class btVector3const &, class btVector3&, float &)`
- `private: bool __thiscall vostok::physics::bullet_character_controller::side_slide_on_slope(class btVector3const &, class btVector3const &, class btVector3const &, float, float, class btVector3&, float &)`
- `private: bool __thiscall vostok::physics::bullet_character_controller::slide_in_impassable_case_impl(class btVector3const &, class btVector3const &, class btVector3const &, float, float, class btVector3&, float &)`
- `private: bool __thiscall vostok::physics::bullet_character_controller::step_down_sweep_test_impl(float, float, class btVector3const &, float, class btVector3const &, class btVector3&, class btVector3&, float &)`
- `private: bool __thiscall vostok::physics::character_controller_move_step_tester::complex_sweep_test(class btVector3const &, class btVector3const &, class btVector3const &, float, class btVector3&, class btVector3&, float &)`
- `private: bool __thiscall vostok::physics::old_bullet_character_controller::convex_sweep_test(class btTransform const &, class btTransform const &, class btVector3const &, float, float, class btVector3&, class btVector3&, float &)`
- `private: bool __thiscall vostok::render::bake_decal_cook::process_baking(struct vostok::render::result_struct &, class vostok::resources::queries_result &, struct vostok::render::render_surface_instance *, struct vostok::render::bake_decal_parameters const &)`
- `private: bool __thiscall vostok::render::buffers_handler<1>::set_overwrite(char const *, class vostok::render::shader_buffer *)`
- `private: bool __thiscall vostok::render::renderer::do_stages_profiling(void)`
- `private: bool __thiscall vostok::render::renderer::is_ready_for_render(class vostok::render::render_output_window *, class vostok::render::scene *const, class boost::function<void __cdecl (bool)> const &)`
- `private: bool __thiscall vostok::render::stage_lights::has_models_for_shadow_pass(class vostok::render::light *, class vostok::buffer_vector<struct vostok::render::render_surface_instance *> const &)`
- `private: bool __thiscall vostok::render::textures_handler<0>::set_overwrite(char const *, class vostok::render::res_texture *)`
- `private: char const * __thiscall survarium::game_world_core::profile_name(unsigned char) const`
- `private: class boost::function<class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> __cdecl (unsigned short)> __thiscall survarium::player::first_third_person_animations_resolver(void) const`
- `private: class boost::function<class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> __cdecl (unsigned short)> __thiscall survarium::player::third_person_animations_resolver(void) const`
- `private: class btVector3 __thiscall character_step_down_sweep_test_callback::get_normal_for_impassable_slope(class btVector3const &)`
- `private: class btVector3 __thiscall character_step_down_sweep_test_callback::get_normal_via_ray_test(struct btCollisionWorld::LocalConvexResult &, class btVector3const &) const`
- `private: class btVector3 __thiscall vostok::physics::bullet_character_controller::get_corrected_walk_vector(void) const`
- `private: class btVector3 __thiscall vostok::physics::bullet_character_controller::get_slide_acceleration(void) const`
- `private: class btVector3 __thiscall vostok::physics::character_move_sweep_callback::get_normal_via_ray_test(struct btCollisionWorld::LocalConvexResult &, class btVector3const &) const`
- `private: class btVector3 __thiscall vostok::physics::character_move_sweep_callback::perform_ray_test(class btVector3const &, struct btCollisionWorld::LocalConvexResult &, class btVector3const &, class btVector3const &) const`
- `private: class btVector3 __thiscall vostok::physics::old_bullet_character_controller::updateTargetPositionBasedOnCollision(class btVector3const &, class btVector3const &, float, float)`
- `private: class survarium::booby_trap_core * __thiscall survarium::booby_trap_set_core::find_disarmed_trap(void)`
- `private: class survarium::booby_trap_core * __thiscall survarium::booby_trap_set_core::find_inactive_trap(void)`
- `private: class survarium::booby_trap_core * __thiscall survarium::booby_trap_set_core::find_oldest_placed_trap(void)`
- `private: class survarium::game_event_history_item * __thiscall survarium::game_world_core::insert_impl(unsigned char, enum survarium::game_event_history_item::events_enum, unsigned int, bool, bool)`
- `private: class survarium::game_event_history_item * __thiscall survarium::game_world_core::new_game_event_history_item(void)`
- `private: class survarium::game_state_history_item & __thiscall survarium::game_world_core::event_horizon_history_item(void)`
- `private: class survarium::game_state_history_item * __thiscall survarium::game_world_core::new_game_state_history_item(void)`
- `private: class survarium::weapon * __thiscall survarium::weapon_cook::allocate_weapon(class survarium::base_game_scene &, unsigned int, unsigned char, unsigned char)`
- `private: class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_fire_state> * __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_fire_state> >::new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_fire_state> >::config_params const &)`
- `private: class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_reload_state> * __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_reload_state> >::new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_reload_state> >::config_params const &)`
- `private: class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_fire_state> * __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_fire_state> >::new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_fire_state> >::config_params const &)`
- `private: class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_reload_state> * __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_reload_state> >::new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_reload_state> >::config_params const &)`
- `private: class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_chamber_a_round_state> * __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_chamber_a_round_state> >::new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_chamber_a_round_state> >::config_params const &)`
- `private: class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_fire_state> * __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_fire_state> >::new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_fire_state> >::config_params const &)`
- `private: class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state> * __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state> >::new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state> >::config_params const &)`
- `private: class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_reload_state> * __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_reload_state> >::new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_reload_state> >::config_params const &)`
- `private: class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_finish_substate> * __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_finish_substate> >::new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_finish_substate> >::config_params const &)`
- `private: class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_one_round_substate> * __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_one_round_substate> >::new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_one_round_substate> >::config_params const &)`
- `private: class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_start_substate> * __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_start_substate> >::new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_start_substate> >::config_params const &)`
- `private: class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_show_state> * __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_show_state> >::new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_show_state> >::config_params const &)`
- `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::double_barreled_weapon_core_reload_state::get_weapon_lexeme(class vostok::mutable_buffer &) const`
- `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::jump_logic_state_landing::get_look_lexeme(class vostok::mutable_buffer &, class fastdelegate::FastDelegate<float __cdecl (float, float, unsigned int, unsigned int, unsigned int, float)> const &, class vostok::animation::mixing::animation_lexeme &)`
- `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::jump_logic_state_prepare::get_look_lexeme(class vostok::mutable_buffer &, class fastdelegate::FastDelegate<float __cdecl (float, float, unsigned int, unsigned int, unsigned int, float)> const &, class vostok::animation::mixing::animation_lexeme &)`
- `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::jump_logic_state_prepare::get_main_lexeme(class vostok::mutable_buffer &, enum vostok::animation::body_part_masks_enum)`
- `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::jump_logic_state_start::get_look_lexeme(class vostok::mutable_buffer &, class fastdelegate::FastDelegate<float __cdecl (float, float, unsigned int, unsigned int, unsigned int, float)> const &, class vostok::animation::mixing::animation_lexeme &)`
- `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::pistol_weapon_core_fire_state::get_weapon_lexeme(class vostok::mutable_buffer &) const`
- `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::pistol_weapon_core_reload_state::get_weapon_lexeme(class vostok::mutable_buffer &) const`
- `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::player_logic_crouch_state::get_look_lexeme(class vostok::mutable_buffer &, unsigned int, bool, class vostok::animation::mixing::animation_lexeme &) const`
- `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::player_logic_crouch_state::movement_lexeme(class vostok::mutable_buffer &, unsigned int, enum vostok::animation::body_part_masks_enum, bool, bool) const`
- `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::player_logic_sprint_state::get_look_lexeme(class vostok::mutable_buffer &, unsigned int, class vostok::animation::mixing::animation_lexeme &) const`
- `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::player_logic_sprint_state::get_movement_lexeme(class vostok::mutable_buffer &, unsigned int, enum vostok::animation::body_part_masks_enum) const`
- `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::player_logic_stand_state::look_lexeme(class vostok::mutable_buffer &, unsigned int, bool, class vostok::animation::mixing::animation_lexeme &) const`
- `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::player_logic_stand_state::movement_lexeme(class vostok::mutable_buffer &, unsigned int, enum vostok::animation::body_part_masks_enum, bool, bool) const`
- `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::short_jump_landing_state::get_look_lexeme(class vostok::mutable_buffer &, class fastdelegate::FastDelegate<float __cdecl (float, float, unsigned int, unsigned int, unsigned int, float)> const &, class vostok::animation::mixing::animation_lexeme &)`
- `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::weapon_core::get_recoil_animation_lexeme(class vostok::mutable_buffer &, enum survarium::recoil_animation_container::recoil_component_enum, bool, float, unsigned int, class fastdelegate::FastDelegate<float __cdecl (float, float, unsigned int, unsigned int, unsigned int, float)> const &, class vostok::animation::mixing::animation_lexeme &) const`
- `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::weapon_core_chamber_a_round_state::get_weapon_lexeme(class vostok::mutable_buffer &) const`
- `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::weapon_core_idle_state::get_user_hands_lexeme(class vostok::mutable_buffer &, enum survarium::weapon_user_state_enum) const`
- `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::weapon_core_reload_state::get_weapon_lexeme(class vostok::mutable_buffer &) const`
- `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::weapon_core_shotgun_reload_base_substate::get_hands_lexeme(class vostok::mutable_buffer &, enum survarium::weapon_user_state_enum, class vostok::animation::mixing::animation_lexeme &) const`
- `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::weapon_core_shotgun_reload_base_substate::get_weapon_lexeme(class vostok::mutable_buffer &, float) const`
- `private: class vostok::animation::mixing::expression __thiscall survarium::weapon_core::get_recoil_expression(class vostok::mutable_buffer &, class vostok::animation::mixing::animation_lexeme &) const`
- `private: class vostok::animation::mixing::n_ary_tree_animation_node * __thiscall vostok::animation::mixing::n_ary_tree_transition_tree_constructor::new_animation(class vostok::animation::mixing::n_ary_tree_animation_node &, class vostok::animation::mixing::n_ary_tree_animation_node &, class vostok::animation::mixing::n_ary_tree_animation_node *, unsigned int, unsigned int &, unsigned int &, unsigned int &, unsigned int &, float &, bool, bool)`
- `private: class vostok::intrusive_ptr<class vostok::render::res_texture, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy> __thiscall vostok::render::bake_decal_cook::occlusion(class vostok::math::float4x4&, struct vostok::render::render_surface_instance *, struct vostok::render::bake_decal_parameters const &, unsigned int, unsigned int, enum DXGI_FORMAT)`
- `private: class vostok::intrusive_ptr<class vostok::sound::sound_instance_proxy, class vostok::sound::sound_instance_proxy, class vostok::threading::single_threading_policy> __thiscall survarium::damage_sound_effect::play_sound_impl(class vostok::resources::resource_ptr<class vostok::sound::sound_emitter, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float3const &, class boost::function<void __cdecl (void)> const &)`
- `private: class vostok::math::float3 __thiscall survarium::weapon_core::get_dispersed_bullet_direction(class vostok::math::float4x4const &)`
- `private: class vostok::math::float4x4 __thiscall survarium::base_player::get_transform_for_animation_player(void const *const) const`
- `private: class vostok::math::float4x4 __thiscall survarium::weapon::calculate_locator(struct vostok::render::model_locator_item const &, class vostok::math::float4x4const &, class vostok::math::float4x4const *, unsigned int)`
- `private: class vostok::math::float4x4 __thiscall vostok::animation::hand_to_weapon_ik_solver::get_hand_target_transform(struct vostok::animation::hand_to_weapon_ik_solver::hand const &, unsigned int, class vostok::math::float4x4const &, class vostok::math::float4x4const *, class vostok::math::float4x4const *, bool) const`
- `private: class vostok::math::float4x4 __thiscall vostok::animation::hand_to_weapon_ik_solver::get_locator_transform_in_item_space(struct vostok::animation::hand_to_weapon_ik_solver::hand const &, enum vostok::animation::hand_to_weapon_ik_solver::ik_locator_id_enum, class vostok::math::float4x4const *, bool) const`
- `private: class vostok::math::float4x4 __thiscall vostok::animation::legs_ik_solver::get_foot_fixed_transform(struct vostok::animation::legs_ik_solver::leg_params const &, class vostok::math::float4x4const &, class vostok::math::float4x4const *, float &) const`
- `private: class vostok::math::float4x4 __thiscall vostok::render::stage_shadow_direct::get_texture_space_transform(void) const`
- `private: class vostok::render::res_shader_technique * __thiscall vostok::render::effect_manager::create_effect_technique(class vostok::render::res_shader_technique const &)`
- `private: class vostok::render::res_xs_hw<struct vostok::render::gs_data> * __thiscall vostok::render::resource_manager::create_xs_hw_impl<struct vostok::render::gs_data>(char const *, struct vostok::render::shader_configuration, struct vostok::render::shader_include_getter *, class vostok::render::map<struct vostok::render::binary_shader_key_type, class vostok::resources::resource_ptr<struct vostok::render::binary_shader_source, class vostok::resources::unmanaged_intrusive_base>, struct stlp_std::less<struct vostok::render::binary_shader_key_type> > *)`
- `private: class vostok::render::res_xs_hw<struct vostok::render::ps_data> * __thiscall vostok::render::resource_manager::create_xs_hw_impl<struct vostok::render::ps_data>(char const *, struct vostok::render::shader_configuration, struct vostok::render::shader_include_getter *, class vostok::render::map<struct vostok::render::binary_shader_key_type, class vostok::resources::resource_ptr<struct vostok::render::binary_shader_source, class vostok::resources::unmanaged_intrusive_base>, struct stlp_std::less<struct vostok::render::binary_shader_key_type> > *)`
- `private: class vostok::render::res_xs_hw<struct vostok::render::vs_data> * __thiscall vostok::render::resource_manager::create_xs_hw_impl<struct vostok::render::vs_data>(char const *, struct vostok::render::shader_configuration, struct vostok::render::shader_include_getter *, class vostok::render::map<struct vostok::render::binary_shader_key_type, class vostok::resources::resource_ptr<struct vostok::render::binary_shader_source, class vostok::resources::unmanaged_intrusive_base>, struct stlp_std::less<struct vostok::render::binary_shader_key_type> > *)`
- `private: class vostok::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base> __thiscall vostok::render::effect_manager::create_new_effect(class vostok::render::effect_descriptor &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &, struct vostok::render::surface_effect_parameters const &)`
- `private: enum survarium::collision_result __thiscall survarium::bullet::check_collision(class vostok::math::float3, float &, float &, float &)`
- `private: enum survarium::game_team_id __thiscall survarium::shared_statistics::team(struct survarium::player_shared_statistics const &) const`
- `private: enum vostok::animation::callback_return_type_enum __thiscall survarium::jump_logic_state_prepare::on_interval_end(struct vostok::animation::animation_callback_params &)`
- `private: enum vostok::animation::callback_return_type_enum __thiscall survarium::player_logic_dead_state::on_animation_end(struct vostok::animation::animation_callback_params &)`
- `private: enum vostok::animation::callback_return_type_enum __thiscall survarium::player_logic_preview_state::on_animation_end(struct vostok::animation::animation_callback_params &)`
- `private: enum vostok::animation::callback_return_type_enum __thiscall survarium::portable_interactive_object_with_finger_correction::on_hand_correction_event(struct vostok::animation::animation_callback_params &, enum vostok::animation::fingers_to_weapon_corrector::hands_enum)`
- `private: enum vostok::animation::callback_return_type_enum __thiscall survarium::short_jump_landing_state::on_landing_event(struct vostok::animation::animation_callback_params &)`
- `private: enum vostok::animation::callback_return_type_enum __thiscall survarium::short_jump_start_state::on_animation_end(struct vostok::animation::animation_callback_params &)`
- `private: enum vostok::animation::callback_return_type_enum __thiscall survarium::victory_item_core_animation_end_aware_state::on_animation_end(struct vostok::animation::animation_callback_params &)`
- `private: enum vostok::animation::callback_return_type_enum __thiscall survarium::weapon_core_melee_state::on_animation_end(struct vostok::animation::animation_callback_params &)`
- `private: enum vostok::animation::callback_return_type_enum __thiscall survarium::weapon_core_melee_state::on_shot_event(struct vostok::animation::animation_callback_params &)`
- `private: enum vostok::input::mouse_button __thiscall vostok::input::platform::mouse::convert_to_binder_mouse_button(int)`
- `private: float __thiscall survarium::damage_zone_core::effect_intensity(class survarium::base_player const &) const`
- `private: float __thiscall survarium::dispersion_calculator::get_character_skill_influence(enum survarium::weapon_user_state_enum, bool, float) const`
- `private: float __thiscall survarium::hit_animations_selector::hit_body_part::hit_time_factor_calculator(float, float, unsigned int, unsigned int, unsigned int, float) const`
- `private: float __thiscall survarium::weapon_core::get_dispersion_amount(float, float)`
- `private: float __thiscall survarium::weapon_core::horizontal_recoil_value(unsigned int) const`
- `private: float __thiscall survarium::weapon_core::vertical_recoil_value(unsigned int) const`
- `private: float __thiscall survarium::weapon_recoil_calculator::get_side_value_impl(unsigned int, float, float) const`
- `private: float __thiscall vostok::math::curve_line_ranged_base::evaluate(float, float, enum vostok::math::enum_evaluate_type, enum vostok::math::enum_evaluate_time_type, unsigned int)`
- `private: float __thiscall vostok::particle::base_particle::get_linear_lifetime_impl(float) const`
- `private: float __thiscall vostok::physics::bullet_character_controller::update_slide_velocity(class btVector3const &, class btVector3const &, float)`
- `private: float __thiscall vostok::physics::old_bullet_character_controller::recover_from_penetration(int)`
- `private: static class vostok::animation::mixing::callback_generator_info * __cdecl vostok::animation::mixing::n_ary_tree::generate_animation_lexeme_end_events(class boost::function<unsigned char __cdecl (void const *)> const &, class vostok::animation::mixing::n_ary_tree const &, class vostok::animation::mixing::n_ary_tree const &, class vostok::animation::mixing::callback_generator_info *, class vostok::animation::mixing::callback_generator_info *, struct vostok::animation::subscribed_channel *)`
- `private: static void __cdecl vostok::buffer_vector<class survarium::fixed_history<struct survarium::player_input_history_item, 27> >::construct(class survarium::fixed_history<struct survarium::player_input_history_item, 27> *, class survarium::fixed_history<struct survarium::player_input_history_item, 27> *const &)`
- `private: static void __cdecl vostok::buffer_vector<class survarium::fixed_history<struct survarium::player_input_history_item, 27> >::destroy(class survarium::fixed_history<struct survarium::player_input_history_item, 27> *, class survarium::fixed_history<struct survarium::player_input_history_item, 27> *const &)`
- `private: static void __cdecl vostok::buffer_vector<class vostok::collision::bone_collision_data>::construct(class vostok::collision::bone_collision_data *, class vostok::collision::bone_collision_data const &)`
- `private: static void __cdecl vostok::buffer_vector<class vostok::fixed_vector<class vostok::math::frustum, 1024> >::construct(class vostok::fixed_vector<class vostok::math::frustum, 1024> *, class vostok::fixed_vector<class vostok::math::frustum, 1024> *const &)`
- `private: static void __cdecl vostok::buffer_vector<class vostok::fixed_vector<class vostok::render::culling::aab_rect, 1024> >::construct(class vostok::fixed_vector<class vostok::render::culling::aab_rect, 1024> *, class vostok::fixed_vector<class vostok::render::culling::aab_rect, 1024> *const &)`
- `private: static void __cdecl vostok::buffer_vector<class vostok::intrusive_ptr<class vostok::render::res_shader_technique, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy> >::destroy(class vostok::intrusive_ptr<class vostok::render::res_shader_technique, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy> *, class vostok::intrusive_ptr<class vostok::render::res_shader_technique, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy> *const &)`
- `private: static void __cdecl vostok::buffer_vector<class vostok::intrusive_ptr<class vostok::render::shader_constant_buffer, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy> >::destroy(class vostok::intrusive_ptr<class vostok::render::shader_constant_buffer, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy> *, class vostok::intrusive_ptr<class vostok::render::shader_constant_buffer, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy> *const &)`
- `private: static void __cdecl vostok::buffer_vector<class vostok::render::buffer_slot>::construct(class vostok::render::buffer_slot *, class vostok::render::buffer_slot *const &)`
- `private: static void __cdecl vostok::buffer_vector<class vostok::render::sampler_slot>::construct(class vostok::render::sampler_slot *, class vostok::render::sampler_slot *const &)`
- `private: static void __cdecl vostok::buffer_vector<class vostok::render::texture_slot>::construct(class vostok::render::texture_slot *, class vostok::render::texture_slot *const &)`
- `private: static void __cdecl vostok::buffer_vector<struct survarium::animations_registry::animations_tuple>::destroy(struct survarium::animations_registry::animations_tuple *, struct survarium::animations_registry::animations_tuple *const &)`
- `private: static void __cdecl vostok::buffer_vector<struct survarium::particle_game_effect_presenter::effect_data>::construct(struct survarium::particle_game_effect_presenter::effect_data *, struct survarium::particle_game_effect_presenter::effect_data *const &)`
- `private: static void __cdecl vostok::buffer_vector<struct survarium::particle_game_effect_presenter::effect_data>::destroy(struct survarium::particle_game_effect_presenter::effect_data *, struct survarium::particle_game_effect_presenter::effect_data *const &)`
- `private: static void __cdecl vostok::buffer_vector<struct survarium::sound_game_effect_presenter::effect_data>::destroy(struct survarium::sound_game_effect_presenter::effect_data *, struct survarium::sound_game_effect_presenter::effect_data *const &)`
- `private: static void __cdecl vostok::buffer_vector<struct vostok::render::effect_compiler::texture_query_desc>::construct(struct vostok::render::effect_compiler::texture_query_desc *, struct vostok::render::effect_compiler::texture_query_desc const &)`
- `private: static void __cdecl vostok::buffer_vector<struct vostok::render::effect_manager::effect_holder_struct>::construct(struct vostok::render::effect_manager::effect_holder_struct *, struct vostok::render::effect_manager::effect_holder_struct const &)`
- `private: static void __cdecl vostok::buffer_vector<struct vostok::render::grass_template>::construct(struct vostok::render::grass_template *, struct vostok::render::grass_template const &)`
- `private: static void __cdecl vostok::buffer_vector<struct vostok::render::light_data>::destroy(struct vostok::render::light_data *, struct vostok::render::light_data *const &)`
- `private: static void __cdecl vostok::buffer_vector<struct vostok::render::requested_streamable_texture>::construct(struct vostok::render::requested_streamable_texture *, struct vostok::render::requested_streamable_texture const &)`
- `private: static void __cdecl vostok::buffer_vector<struct vostok::render::streaming_ready_texture>::destroy(struct vostok::render::streaming_ready_texture *, struct vostok::render::streaming_ready_texture *const &)`
- `private: static void __cdecl vostok::buffer_vector<struct vostok::render::ui::vertex>::construct(struct vostok::render::ui::vertex *, struct vostok::render::ui::vertex const &)`
- `private: struct ID3D11RasterizerState * __thiscall vostok::render::state_cache<struct ID3D11RasterizerState, struct D3D11_RASTERIZER_DESC, 32>::find(struct D3D11_RASTERIZER_DESC const &, unsigned int)`
- `private: struct ID3D11Resource * __thiscall vostok::render::texture_pool::add_texture(struct vostok::render::texture_pool_key const &, bool, bool)`
- `private: struct ID3D11SamplerState * __thiscall vostok::render::state_cache<struct ID3D11SamplerState, struct D3D11_SAMPLER_DESC, 32>::find(struct D3D11_SAMPLER_DESC const &, unsigned int)`
- `private: struct stlp_std::pair<class vostok::animation::mixing::expression, class vostok::animation::mixing::animation_lexeme> __thiscall survarium::jump_logic_state_landing::get_main_expression(class vostok::mutable_buffer &)`
- `private: struct stlp_std::pair<class vostok::animation::mixing::expression, class vostok::animation::mixing::animation_lexeme> __thiscall survarium::jump_logic_state_start::get_main_expression(class vostok::mutable_buffer &, enum vostok::animation::body_part_masks_enum)`
- `private: struct stlp_std::pair<class vostok::animation::mixing::expression, class vostok::animation::mixing::animation_lexeme> __thiscall survarium::short_jump_landing_state::get_main_expression(class vostok::mutable_buffer &)`
- `private: struct stlp_std::pair<class vostok::animation::mixing::expression, class vostok::animation::mixing::animation_lexeme> __thiscall survarium::short_jump_start_state::get_main_expression(class vostok::mutable_buffer &, enum vostok::animation::body_part_masks_enum)`
- `private: struct survarium::anomaly_state * __thiscall survarium::generic_anomaly_core::select_state(void)`
- `private: struct survarium::game_effect_time __thiscall survarium::artefact_base::effect_calculator(struct survarium::game_effect_node const &, unsigned int, unsigned int)`
- `private: struct survarium::game_effect_time __thiscall survarium::body_part_parameters::effect_calculator(struct survarium::game_effect_node const &, unsigned int, unsigned int)`
- `private: struct survarium::game_effect_time __thiscall survarium::body_part_parameters::threshold_effect_calculator(class survarium::affects_threshold *, struct survarium::game_effect_node const &, unsigned int, unsigned int)`
- `private: struct survarium::game_effect_time __thiscall survarium::damage_zone_core::effect_calculator(class survarium::base_player const *, struct survarium::game_effect_node const &, unsigned int, unsigned int) const`
- `private: struct vostok::animation::base_interpolator const & __thiscall vostok::animation::mixing::n_ary_tree_deserializer::get_interpolator(void)`
- `private: struct vostok::animation::mixing::n_ary_tree_base_node & __thiscall vostok::animation::mixing::n_ary_tree_deserializer::get_operand(void)`
- `private: struct vostok::collision::oct_node * __thiscall vostok::collision::loose_oct_tree::new_node(void)`
- `private: struct vostok::render::material_effects * __thiscall vostok::render::material_effects_instance::get_material_effects_or_new(enum vostok::render::enum_vertex_input_type)`
- `private: struct vostok::render::result_struct __thiscall vostok::render::bake_decal_cook::accumulate_decals(struct vostok::render::render_surface_instance *, struct vostok::render::bake_decal_parameters const &, unsigned int, unsigned int, unsigned int, enum DXGI_FORMAT, enum DXGI_FORMAT)`
- `private: struct vostok::render::result_struct __thiscall vostok::render::bake_decal_cook::composition(struct vostok::render::result_struct const &, struct vostok::render::render_surface_instance *, struct vostok::render::bake_decal_parameters const &, unsigned int, unsigned int, enum DXGI_FORMAT)`
- `private: unsigned __int64 __thiscall vostok::timing::floating_timer::get_elapsed_ticks_impl(unsigned __int64&) const`
- `private: unsigned __int64 __thiscall vostok::timing::floating_timer::get_time_with_factor(unsigned __int64, float) const`
- `private: unsigned int __thiscall survarium::network_client::try_send_all(unsigned int, bool)`
- `private: unsigned int __thiscall survarium::player_respawn_rule::get_available_spawn_point(enum survarium::game_team_id)`
- `private: unsigned int __thiscall vostok::animation::mixing::n_ary_tree_deserializer::r(unsigned int)`
- `private: unsigned int __thiscall vostok::math::curve_line_ranged_base::save_binary(class vostok::mutable_buffer &, bool)`
- `private: unsigned int __thiscall vostok::render::res_render_output::select_presentation_interval(bool)`
- `private: virtual __thiscall survarium::artefact<class survarium::artefact_lifebone_core>::~artefact<class survarium::artefact_lifebone_core>(void)`
- `private: virtual __thiscall survarium::artefact<class survarium::artefact_onyx_core>::~artefact<class survarium::artefact_onyx_core>(void)`
- `private: virtual __thiscall survarium::artefact<class survarium::artefact_rattle_core>::~artefact<class survarium::artefact_rattle_core>(void)`
- `private: virtual __thiscall survarium::artefact<class survarium::artefact_spring_core>::~artefact<class survarium::artefact_spring_core>(void)`
- `private: virtual __thiscall survarium::game_effect_emitter::~game_effect_emitter(void)`
- `private: virtual __thiscall survarium::generic_anomaly::~generic_anomaly(void)`
- `private: virtual __thiscall survarium::grenade::~grenade(void)`
- `private: virtual __thiscall survarium::player_respawn_rule::~player_respawn_rule(void)`
- `private: virtual __thiscall survarium::pvp_match_core::~pvp_match_core(void)`
- `private: virtual __thiscall survarium::single_player_respawn_rule::~single_player_respawn_rule(void)`
- `private: virtual __thiscall survarium::weapon_core_melee_state::~weapon_core_melee_state(void)`
- `private: virtual bool __thiscall survarium::artefact_lifebone_core::active_effect_ended(void)`
- `private: virtual bool __thiscall survarium::artefact_onyx_core::active_effect_ended(void)`
- `private: virtual bool __thiscall survarium::artefact_spring_core::active_effect_ended(void)`
- `private: virtual bool __thiscall survarium::jump_logic_state_prepare::is_ready_for_transition(void) const`
- `private: virtual bool __thiscall survarium::match_client::is_connected(void) const`
- `private: virtual bool __thiscall survarium::match_client::is_disconnected(void) const`
- `private: virtual bool __thiscall survarium::victory_item_core::can_use(struct survarium::usable_object_user_data const *) const`
- `private: virtual bool __thiscall survarium::victory_item_core::is_ready_to_be_deactivated(void) const`
- `private: virtual bool __thiscall survarium::victory_item_core::need_to_select_animations(void) const`
- `private: virtual bool __thiscall survarium::victory_item_core_put_state::is_ready_for_transition(void) const`
- `private: virtual bool __thiscall survarium::victory_items_container_core::can_use(struct survarium::usable_object_user_data const *) const`
- `private: virtual bool __thiscall survarium::victory_items_container_core::use_execute(struct survarium::usable_object_user_data *)`
- `private: virtual bool __thiscall survarium::weapon_core::need_to_select_animations(void) const`
- `private: virtual bool __thiscall survarium::weapon_core_throw_grenade_state::is_ready_for_transition(void) const`
- `private: virtual bool __thiscall vostok::engine::engine_world::render_has_been_created(void) const`
- `private: virtual bool __thiscall vostok::input::platform::keyboard::check_modifier(enum vostok::input::enum_modifiers) const`
- `private: virtual bool __thiscall vostok::input::platform::keyboard::get_dik_name(int, char *, int) const`
- `private: virtual bool __thiscall vostok::input::platform::keyboard::is_key_down(enum vostok::input::enum_keyboard) const`
- `private: virtual bool __thiscall vostok::input::platform::keyboard::translate_text(int, wchar_t &)`
- `private: virtual bool __thiscall vostok::journaling::input_handler::on_gamepad_action(struct vostok::input::world *, enum vostok::input::gamepad_button, enum vostok::input::enum_gamepad_action)`
- `private: virtual bool __thiscall vostok::journaling::input_handler::on_keyboard_action(struct vostok::input::world *, enum vostok::input::enum_keyboard, enum vostok::input::enum_keyboard_action)`
- `private: virtual bool __thiscall vostok::journaling::input_handler::on_mouse_key_action(struct vostok::input::world *, enum vostok::input::mouse_button, enum vostok::input::enum_mouse_key_action)`
- `private: virtual bool __thiscall vostok::journaling::input_handler::on_mouse_move(struct vostok::input::world *, int, int, int)`
- `private: virtual bool __thiscall vostok::render::stage_ambient_occlusion::is_effects_ready(void) const`
- `private: virtual bool __thiscall vostok::render::stage_lights::is_effects_ready(void) const`
- `private: virtual bool __thiscall vostok::render::stage_postprocess::is_effects_ready(void) const`
- `private: virtual bool __thiscall vostok::render::stage_pre_rain::is_effects_ready(void) const`
- `private: virtual bool __thiscall vostok::render::stage_rain::is_effects_ready(void) const`
- `private: virtual bool __thiscall vostok::render::stage_shadow_direct::is_effects_ready(void) const`
- `private: virtual bool __thiscall vostok::render::stage_view_mode::is_effects_ready(void) const`
- `private: virtual bool __thiscall vostok::render::stage_volume_fog::is_effects_ready(void) const`
- `private: virtual char const * __thiscall survarium::ladder::ladder_occluder::use_info(struct survarium::usable_object_user_data const *) const`
- `private: virtual char const * __thiscall survarium::victory_item_core::use_info(struct survarium::usable_object_user_data const *) const`
- `private: virtual char const * __thiscall survarium::victory_items_container_core::use_info(struct survarium::usable_object_user_data const *) const`
- `private: virtual class btCollisionObject * __thiscall vostok::physics::bullet_character_controller::get_bt_collision_obect(void)`
- `private: virtual class btCollisionObject * __thiscall vostok::physics::old_bullet_character_controller::get_bt_collision_obect(void)`
- `private: virtual class fastdelegate::FastDelegate<float __cdecl (float, float, unsigned int, unsigned int, unsigned int, float)> __thiscall survarium::victory_item_core::time_calculator(unsigned char)`
- `private: virtual class survarium::booby_trap_core * __thiscall survarium::booby_trap_cook::new_derived_resource(struct vostok::physics::world &, void *const)`
- `private: virtual class survarium::booby_trap_core * __thiscall survarium::booby_trap_core_cook::new_derived_resource(struct vostok::physics::world &, void *const)`
- `private: virtual class survarium::booby_trap_set_core * __thiscall survarium::booby_trap_set_cook::new_derived_resource(struct vostok::physics::world &, class vostok::resources::resource_ptr<class survarium::game_material_manager, class vostok::resources::unmanaged_intrusive_base> const &, void *const)`
- `private: virtual class survarium::booby_trap_set_core * __thiscall survarium::booby_trap_set_core_cook::new_derived_resource(struct vostok::physics::world &, class vostok::resources::resource_ptr<class survarium::game_material_manager, class vostok::resources::unmanaged_intrusive_base> const &, void *const)`
- `private: virtual class survarium::damage_zone_core * __thiscall survarium::damage_zone_cook::construct_resource(class vostok::memory::base_allocator &) const`
- `private: virtual class survarium::damage_zone_core * __thiscall survarium::damage_zone_core_cook::construct_resource(class vostok::memory::base_allocator &) const`
- `private: virtual class survarium::generic_anomaly & __thiscall survarium::generic_anomaly_cook::construct_derived_resource(void *, class vostok::resources::resource_ptr<class survarium::artefact_base, class vostok::resources::unmanaged_intrusive_base> const *, unsigned int) const`
- `private: virtual class survarium::generic_anomaly_core & __thiscall survarium::generic_anomaly_core_cook::construct_derived_resource(void *, class vostok::resources::resource_ptr<class survarium::artefact_base, class vostok::resources::unmanaged_intrusive_base> const *, unsigned int) const`
- `private: virtual class survarium::grenade_core * __thiscall survarium::grenade_cook::new_derived_resource(void *const)`
- `private: virtual class survarium::grenade_core * __thiscall survarium::grenade_core_cook::new_derived_resource(void *const)`
- `private: virtual class survarium::items_dictionary const & __thiscall survarium::generic_anomaly_cook::items_dictionary(void) const`
- `private: virtual class survarium::spottable_object * __thiscall survarium::victory_item_core::cast_to_spottable(void)`
- `private: virtual class survarium::victory_item * __thiscall survarium::victory_item_cook::create_resource(struct vostok::physics::world &)`
- `private: virtual class vostok::animation::mixing::animation_lexeme __thiscall survarium::double_barreled_weapon_core_idle_state::get_weapon_lexeme(class vostok::mutable_buffer &) const`
- `private: virtual class vostok::animation::mixing::animation_lexeme __thiscall survarium::pistol_weapon_core_idle_state::get_weapon_lexeme(class vostok::mutable_buffer &) const`
- `private: virtual class vostok::animation::mixing::animation_lexeme __thiscall survarium::weapon_core_idle_state::get_weapon_lexeme(class vostok::mutable_buffer &) const`
- `private: virtual class vostok::animation::mixing::expression __thiscall survarium::double_barreled_weapon_core_reload_state::weapon_and_hands_expression(class vostok::mutable_buffer &, enum survarium::weapon_user_state_enum, class vostok::animation::mixing::animation_lexeme &) const`
- `private: virtual class vostok::animation::mixing::expression __thiscall survarium::empty_hands::selected_animations(class vostok::mutable_buffer &) const`
- `private: virtual class vostok::animation::mixing::expression __thiscall survarium::pistol_weapon_core_fire_state::weapon_and_hands_expression(class vostok::mutable_buffer &, enum survarium::weapon_user_state_enum, class vostok::animation::mixing::animation_lexeme &) const`
- `private: virtual class vostok::animation::mixing::expression __thiscall survarium::pistol_weapon_core_reload_state::weapon_and_hands_expression(class vostok::mutable_buffer &, enum survarium::weapon_user_state_enum, class vostok::animation::mixing::animation_lexeme &) const`
- `private: virtual class vostok::animation::mixing::expression __thiscall survarium::victory_item_core::selected_animations(class vostok::mutable_buffer &) const`
- `private: virtual class vostok::animation::mixing::expression __thiscall survarium::victory_item_core_carry_state::item_and_hands_expression(class vostok::mutable_buffer &, enum survarium::weapon_user_state_enum, class vostok::animation::mixing::animation_lexeme &) const`
- `private: virtual class vostok::animation::mixing::expression __thiscall survarium::weapon_core_chamber_a_round_state::weapon_and_hands_expression(class vostok::mutable_buffer &, enum survarium::weapon_user_state_enum, class vostok::animation::mixing::animation_lexeme &) const`
- `private: virtual class vostok::animation::mixing::expression __thiscall survarium::weapon_core_hide_state::weapon_and_hands_expression(class vostok::mutable_buffer &, enum survarium::weapon_user_state_enum, class vostok::animation::mixing::animation_lexeme &) const`
- `private: virtual class vostok::animation::mixing::expression __thiscall survarium::weapon_core_idle_state::weapon_and_hands_expression(class vostok::mutable_buffer &, enum survarium::weapon_user_state_enum, class vostok::animation::mixing::animation_lexeme &) const`
- `private: virtual class vostok::animation::mixing::expression __thiscall survarium::weapon_core_melee_state::weapon_and_hands_expression(class vostok::mutable_buffer &, enum survarium::weapon_user_state_enum, class vostok::animation::mixing::animation_lexeme &) const`
- `private: virtual class vostok::animation::mixing::expression __thiscall survarium::weapon_core_reload_state::weapon_and_hands_expression(class vostok::mutable_buffer &, enum survarium::weapon_user_state_enum, class vostok::animation::mixing::animation_lexeme &) const`
- `private: virtual class vostok::animation::mixing::expression __thiscall survarium::weapon_core_shotgun_reload_state::weapon_and_hands_expression(class vostok::mutable_buffer &, enum survarium::weapon_user_state_enum, class vostok::animation::mixing::animation_lexeme &) const`
- `private: virtual class vostok::math::float4x4 __thiscall survarium::empty_hands::get_transform(void) const`
- `private: virtual class vostok::mutable_buffer __thiscall survarium::victory_items_container_cook::allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)`
- `private: virtual class vostok::mutable_buffer __thiscall survarium::weapon_core_melee_state_cook::allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)`
- `private: virtual class vostok::mutable_buffer __thiscall survarium::weapon_core_state_cook_template<class survarium::double_barreled_weapon_core_idle_state>::allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)`
- `private: virtual class vostok::mutable_buffer __thiscall survarium::weapon_core_state_cook_template<class survarium::weapon_core_idle_state>::allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)`
- `private: virtual class vostok::mutable_buffer __thiscall survarium::weapon_core_throw_grenade_state_cook::allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)`
- `private: virtual class vostok::mutable_buffer __thiscall survarium::weapon_preview_state_cook::allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)`
- `private: virtual class vostok::mutable_buffer __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state> >::allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)`
- `private: virtual class vostok::network_core::udp_match_packet * __thiscall survarium::match_client::new_packet(enum vostok::match::client::messages_enum)`
- `private: virtual class vostok::network_core::udp_match_packet * __thiscall vostok::journaling::match_client::new_packet(enum vostok::match::client::messages_enum)`
- `private: virtual class vostok::resources::resource_ptr<class vostok::animation::skeleton, class vostok::resources::unmanaged_intrusive_base> __thiscall survarium::empty_hands::get_skeleton(void) const`
- `private: virtual enum survarium::player_stances_enum __thiscall survarium::victory_item_core::player_stance(void) const`
- `private: virtual float __thiscall vostok::input::platform::gamepad::get_vibration(enum vostok::input::gamepad_vibrators) const`
- `private: virtual struct stlp_std::pair<class vostok::animation::mixing::expression, class vostok::animation::mixing::animation_lexeme> __thiscall survarium::jump_logic_state_landing::selected_animations(class vostok::mutable_buffer &, class fastdelegate::FastDelegate<float __cdecl (float, float, unsigned int, unsigned int, unsigned int, float)> const &, struct survarium::weapon_animation_parameters const &)`
- `private: virtual struct stlp_std::pair<class vostok::animation::mixing::expression, class vostok::animation::mixing::animation_lexeme> __thiscall survarium::jump_logic_state_prepare::selected_animations(class vostok::mutable_buffer &, class fastdelegate::FastDelegate<float __cdecl (float, float, unsigned int, unsigned int, unsigned int, float)> const &, struct survarium::weapon_animation_parameters const &)`
- _...and 3763 more_

### Deleted (6812)

- `??0doug_lea_mt_allocator@memory@vostok@@QAE@_N0_N1@Z`
- `FLoadedAtPreferredAddress`
- `OverlayIAT`
- `PinhFromImageBase`
- `TimeStampOfImage`
- `__aligned_free`
- `__aligned_malloc`
- `__int64 __cdecl vostok::threading::interlocked_compare_exchange(__int64volatile &, __int64, __int64)`
- `__memcpy`
- `_destroy_mspace`
- `_initialize_virtual_alloc_arena`
- `_vostok_mspace_memalign`
- ``vostok::logging::log_file::skip_next_line'::`2'::processor::dummy`
- ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare`
- ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare`
- ``vostok::particle::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare`
- ``vostok::particle::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare`
- ``vostok::physics::bullet_physics_world::object_query'::`2'::object_query_callback::object_query_callback`
- ``vostok::render::res_effect::push_texture_unique'::`2'::find_texture_predicate::find_texture_predicate`
- ``vostok::render::res_effect::push_texture_unique'::`2'::find_texture_predicate::operator()`
- ``vostok::render::scene::dump_scene_statistics'::`2'::sort_predicate::operator()`
- ``vostok::render::scene::gather_streamable_textures'::`2'::find_texture_predicate::find_texture_predicate`
- ``vostok::render::scene::gather_streamable_textures'::`2'::find_texture_predicate::operator()`
- ``vostok::render::scene::process_streaming'::`16'::ready_texture_comparer::operator()`
- ``vostok::render::scene::process_streaming'::`2'::remove_texture_predicate::operator()`
- ``vostok::render::scene::process_streaming'::`3'::remove_requested_texture_predicate::operator()`
- ``vostok::render::shadow_batched_geometry::build'::`9'::sort_predicate::operator()`
- ``vostok::render::sort_by_crc<vostok::configs::binary_config_value>'::`5'::predicate::compare`
- ``vostok::render::sort_by_crc<vostok::render::custom_config_value>'::`5'::predicate::compare`
- ``vostok::render::stage_ambient_lighting::execute'::`5'::sort_by_size_predicate::operator()`
- ``vostok::render::stage_lights::execute'::`15'::sort_by_size_predicate::operator()`
- ``vostok::render::stage_shadow_direct::render_models'::`4'::int4::int4`
- ``vostok::render::static_render_surface::create_shadow_pass_geometry'::`3'::colored_opt_static_vertex::set`
- ``vostok::tasks::task_manager::grab_next_task'::`4'::grabbing_next_task_thread_count_raii_helper::grabbing_next_task_thread_count_raii_helper`
- ``vostok::tasks::task_manager::grab_next_task'::`4'::grabbing_next_task_thread_count_raii_helper::~grabbing_next_task_thread_count_raii_helper`
- `bool __cdecl check_presence_mutex(void)`
- `bool __cdecl show_dialog_for_unhandled_exceptions(void)`
- `bool __cdecl stlp_std::operator!=<unsigned int *>(class stlp_std::reverse_iterator<unsigned int *> const &, class stlp_std::reverse_iterator<unsigned int *> const &)`
- `bool __cdecl survarium::operator!=(struct survarium::animation_space_vertex_id const &, struct survarium::animation_space_vertex_id const &)`
- `bool __cdecl survarium::operator!=(struct survarium::movement_animation_controller_parameters const &, struct survarium::movement_animation_controller_parameters const &)`
- `bool __cdecl survarium::operator!=(struct survarium::simple_animation_controller_parameters const &, struct survarium::simple_animation_controller_parameters const &)`
- `bool __cdecl survarium::operator==(struct survarium::movement_animation_controller_parameters const &, struct survarium::movement_animation_controller_parameters const &)`
- `bool __cdecl survarium::operator==(struct survarium::simple_animation_controller_parameters const &, struct survarium::simple_animation_controller_parameters const &)`
- `bool __cdecl survarium::true_predicate(void)`
- `bool __cdecl vostok::ai::planning::is_block_on_block(struct vostok::ai::planning::block const *const, struct vostok::ai::planning::block const *const)`
- `bool __cdecl vostok::ai::planning::is_clear_predicate(struct vostok::ai::planning::block const *const)`
- `bool __cdecl vostok::ai::planning::is_disk_clear(struct vostok::ai::planning::disk const *const)`
- `bool __cdecl vostok::ai::planning::is_disk_on_disk(struct vostok::ai::planning::disk const *const, struct vostok::ai::planning::disk const *const)`
- `bool __cdecl vostok::ai::planning::is_disk_on_peg(struct vostok::ai::planning::disk const *const, struct vostok::ai::planning::peg const *const)`
- `bool __cdecl vostok::ai::planning::is_disk_smaller(struct vostok::ai::planning::disk const *const, struct vostok::ai::planning::disk const *const)`
- `bool __cdecl vostok::ai::planning::is_hand_empty_predicate(void)`
- `bool __cdecl vostok::ai::planning::is_holding_predicate(struct vostok::ai::planning::block const *const)`
- `bool __cdecl vostok::ai::planning::is_on_table_predicate(struct vostok::ai::planning::block const *const)`
- `bool __cdecl vostok::ai::planning::is_peg_clear(struct vostok::ai::planning::peg const *const)`
- `bool __cdecl vostok::ai::planning::operator<(struct stlp_std::pair<unsigned int const, struct stlp_std::pair<class vostok::ai::planning::pddl_predicate const *, unsigned int> > const &, struct stlp_std::pair<unsigned int const, struct stlp_std::pair<class vostok::ai::planning::pddl_predicate const *, unsigned int> > const &)`
- `bool __cdecl vostok::ai::planning::predicate_binder<class vostok::ai::brain_unit const *, struct vostok::ai::animation_item const *, struct vostok::ai::sound_item const *, class vostok::ai::brain_unit const *, struct vostok::ai::animation_item const *, struct vostok::ai::sound_item const *>(class vostok::ai::planning::pddl_predicate const &, class vostok::fixed_vector<void const *, 4> const &)`
- `bool __cdecl vostok::ai::planning::predicate_binder<class vostok::ai::brain_unit const *, struct vostok::ai::npc const *, class vostok::ai::brain_unit const *, struct vostok::ai::npc const *>(class vostok::ai::planning::pddl_predicate const &, class vostok::fixed_vector<void const *, 4> const &)`
- `bool __cdecl vostok::ai::planning::predicate_binder<struct vostok::ai::npc const *, struct vostok::ai::npc const *>(class vostok::ai::planning::pddl_predicate const &, class vostok::fixed_vector<void const *, 4> const &)`
- `bool __cdecl vostok::animation::mixing::operator<(class vostok::animation::mixing::animation_interval const &, class vostok::animation::mixing::animation_interval const &)`
- `bool __cdecl vostok::animation::mixing::operator>(class vostok::animation::mixing::animation_interval const &, class vostok::animation::mixing::animation_interval const &)`
- `bool __cdecl vostok::apc::is_same_thread(enum vostok::apc::threads_enum)`
- `bool __cdecl vostok::build::print_build_id_command_line(void)`
- `bool __cdecl vostok::collision::bresenham<struct vostok::collision::terrain_data>(struct vostok::collision::terrain_data const &, int, int, int, int, class vostok::math::float3const &, class vostok::math::float3const &, float, float &, bool)`
- `bool __cdecl vostok::collision::get_row_col(float, int, class vostok::math::float3const &, int &, int &)`
- `bool __cdecl vostok::collision::line_line_intersect_non_parallel(class vostok::math::float3const &, class vostok::math::float3const &, class vostok::math::float3const &, class vostok::math::float3const &, class vostok::math::float3&, class vostok::math::float3&, float &, float &)`
- `bool __cdecl vostok::collision::ray_test_quad(class vostok::math::float3const &, class vostok::math::float3const &, class vostok::math::float3const &, class vostok::math::float3const &, class vostok::math::float3const &, class vostok::math::float3const &, float, float &)`
- `bool __cdecl vostok::collision::segment_segment_intersect(class vostok::math::float3const &, class vostok::math::float3const &, class vostok::math::float3const &, class vostok::math::float3const &, float)`
- `bool __cdecl vostok::collision::terrain_ray_test<struct vostok::collision::terrain_data>(struct vostok::collision::terrain_data const &, class vostok::math::float3const &, class vostok::math::float3const &, float, float &)`
- `bool __cdecl vostok::command_line::initialized(void)`
- `bool __cdecl vostok::command_line::key_is_set(char const *)`
- `bool __cdecl vostok::command_line::show_help(void)`
- `bool __cdecl vostok::console_commands::execute_console_commands(class vostok::fs_new::native_path_string, enum vostok::console_commands::execution_filter, bool)`
- `bool __cdecl vostok::core::initialized(void)`
- `bool __cdecl vostok::core::use_console_for_logging(void)`
- `bool __cdecl vostok::debug::bugtrap::initialized(void)`
- `bool __cdecl vostok::debug::platform::error_after_dialog(void)`
- `bool __cdecl vostok::engine::command_line_editor(void)`
- `bool __cdecl vostok::engine::command_line_no_splash_screen(void)`
- `bool __cdecl vostok::fs_new::is_absolute_path<class vostok::fs_new::native_path_string>(class vostok::fs_new::native_path_string const &)`
- `bool __cdecl vostok::math::is_similar(class vostok::math::float3const &, class vostok::math::float3const &, float)`
- `bool __cdecl vostok::math::is_zero<float>(float const &, float const &)`
- `bool __cdecl vostok::math::operator<(class vostok::math::float3_pod const &, class vostok::math::float3_pod const &)`
- `bool __cdecl vostok::math::operator<(class vostok::math::float4_pod const &, class vostok::math::float4_pod const &)`
- `bool __cdecl vostok::math::operator<=(class vostok::math::float3_pod const &, class vostok::math::float3_pod const &)`
- `bool __cdecl vostok::math::operator>(class vostok::math::float3_pod const &, class vostok::math::float3_pod const &)`
- `bool __cdecl vostok::math::operator>(class vostok::math::float4_pod const &, class vostok::math::float4_pod const &)`
- `bool __cdecl vostok::math::operator>=(class vostok::math::float3_pod const &, class vostok::math::float3_pod const &)`
- `bool __cdecl vostok::memory::try_lock_process_heap(void)`
- `bool __cdecl vostok::network_core::get_connection_info_from_string(char const *, char *const, unsigned short &)`
- `bool __cdecl vostok::operator<(class vostok::buffer_string const &, class vostok::buffer_string const &)`
- `bool __cdecl vostok::operator==(class vostok::buffer_string const &, char const *)`
- `bool __cdecl vostok::operator==(class vostok::buffer_string const &, class vostok::buffer_string const &)`
- `bool __cdecl vostok::particle::is_playing(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `bool __cdecl vostok::platform::unload_delay_loaded_library(char const *)`
- `bool __cdecl vostok::render::reclaim<class vostok::render::res_declaration, struct vostok::render::resource_manager::compare_predicate<class vostok::render::res_declaration> >(class vostok::render::set<class vostok::render::res_declaration *, struct vostok::render::resource_manager::compare_predicate<class vostok::render::res_declaration> > &, class vostok::render::res_declaration const *)`
- `bool __cdecl vostok::render::reclaim<class vostok::render::res_geometry, struct vostok::render::resource_manager::compare_member_predicate<class vostok::render::res_geometry> >(class vostok::render::set<class vostok::render::res_geometry *, struct vostok::render::resource_manager::compare_member_predicate<class vostok::render::res_geometry> > &, class vostok::render::res_geometry const *)`
- `bool __cdecl vostok::render::reclaim<class vostok::render::res_input_layout, struct vostok::render::resource_manager::compare_predicate<class vostok::render::res_input_layout> >(class vostok::render::set<class vostok::render::res_input_layout *, struct vostok::render::resource_manager::compare_predicate<class vostok::render::res_input_layout> > &, class vostok::render::res_input_layout const *)`
- `bool __cdecl vostok::render::reclaim<class vostok::render::res_pass, struct vostok::render::effect_manager::compare_predicate<class vostok::render::res_pass> >(class vostok::render::set<class vostok::render::res_pass *, struct vostok::render::effect_manager::compare_predicate<class vostok::render::res_pass> > &, class vostok::render::res_pass const *)`
- `bool __cdecl vostok::render::reclaim<class vostok::render::res_sampler_list, struct vostok::render::resource_manager::compare_member_predicate<class vostok::render::res_sampler_list> >(class vostok::render::set<class vostok::render::res_sampler_list *, struct vostok::render::resource_manager::compare_member_predicate<class vostok::render::res_sampler_list> > &, class vostok::render::res_sampler_list const *)`
- `bool __cdecl vostok::render::reclaim<class vostok::render::res_shader_technique, struct vostok::render::effect_manager::compare_predicate<class vostok::render::res_shader_technique> >(class vostok::render::set<class vostok::render::res_shader_technique *, struct vostok::render::effect_manager::compare_predicate<class vostok::render::res_shader_technique> > &, class vostok::render::res_shader_technique const *)`
- `bool __cdecl vostok::render::reclaim<class vostok::render::res_signature, struct vostok::render::resource_manager::compare_predicate<class vostok::render::res_signature> >(class vostok::render::set<class vostok::render::res_signature *, struct vostok::render::resource_manager::compare_predicate<class vostok::render::res_signature> > &, class vostok::render::res_signature const *)`
- `bool __cdecl vostok::render::reclaim<class vostok::render::res_state>(class vostok::render::vector<class vostok::render::res_state *> &, class vostok::render::res_state const *)`
- `bool __cdecl vostok::render::reclaim<class vostok::render::res_texture_list, struct vostok::render::resource_manager::compare_member_predicate<class vostok::render::res_texture_list> >(class vostok::render::set<class vostok::render::res_texture_list *, struct vostok::render::resource_manager::compare_member_predicate<class vostok::render::res_texture_list> > &, class vostok::render::res_texture_list const *)`
- `bool __cdecl vostok::render::reclaim<class vostok::render::shader_constant_buffer, struct vostok::render::resource_manager::constant_buffer_predicate>(class vostok::render::set<class vostok::render::shader_constant_buffer *, struct vostok::render::resource_manager::constant_buffer_predicate> &, class vostok::render::shader_constant_buffer const *)`
- `bool __cdecl vostok::render::reclaim<class vostok::render::shader_constant_table, struct vostok::render::resource_manager::constant_table_predicate>(class vostok::render::set<class vostok::render::shader_constant_table *, struct vostok::render::resource_manager::constant_table_predicate> &, class vostok::render::shader_constant_table const *)`
- `bool __cdecl vostok::render::set_client_rect(struct HWND__*, int, int, int, int)`
- `bool __cdecl vostok::render::state_utils::operator==(struct D3D11_RASTERIZER_DESC const &, struct D3D11_RASTERIZER_DESC const &)`
- `bool __cdecl vostok::render::state_utils::operator==(struct D3D11_SAMPLER_DESC const &, struct D3D11_SAMPLER_DESC const &)`
- `bool __cdecl vostok::render::utils::calc_lists_diff_range<class vostok::render::res_sampler_list>(class vostok::render::res_sampler_list const &, class vostok::render::res_sampler_list const &, unsigned int &, unsigned int &)`
- `bool __cdecl vostok::render::utils::calc_lists_diff_range<class vostok::render::res_texture_list>(class vostok::render::res_texture_list const &, class vostok::render::res_texture_list const &, unsigned int &, unsigned int &)`
- `bool __cdecl vostok::render::utils::calc_lists_diff_range<class vostok::render::vector<class vostok::intrusive_ptr<class vostok::render::shader_constant_buffer, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy> > >(class vostok::render::vector<class vostok::intrusive_ptr<class vostok::render::shader_constant_buffer, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy> > const &, class vostok::render::vector<class vostok::intrusive_ptr<class vostok::render::shader_constant_buffer, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy> > const &, unsigned int &, unsigned int &)`
- `bool __cdecl vostok::resources::convert_virtual_to_physical_path(class vostok::fs_new::native_path_string *, class vostok::fs_new::virtual_path_string const &, char const *)`
- `bool __cdecl vostok::resources::cook_must_be_registered(enum vostok::resources::class_id_enum)`
- `bool __cdecl vostok::resources::is_fs_iterator_class(enum vostok::resources::class_id_enum)`
- `bool __cdecl vostok::resources::vfs_sub_fat_resource_is_created(class vostok::vfs::vfs_iterator const &)`
- `bool __cdecl vostok::strings::compare_with_wildcards(char const *, char const *)`
- `bool __cdecl vostok::strings::equal(char const *, char const *)`
- `bool __cdecl vostok::strings::mbstowcs(wchar_t *, unsigned int, char const *)`
- `bool __cdecl vostok::strings::set_multibyte(char *, unsigned int, wchar_t const *)`
- `bool __cdecl vostok::tasks::zero_tasks(void)`
- `bool __cdecl vostok::testing::is_testing(void)`
- `bool __cdecl vostok::vfs::folders_connected_by_overlap(class vostok::vfs::base_node<1> *, class vostok::vfs::base_node<1> *)`
- `bool __cdecl vostok::vfs::need_physical_mount(bool *, class vostok::vfs::base_node<1> *, enum vostok::vfs::find_enum, enum vostok::vfs::traverse_enum, class vostok::memory::base_allocator *)`
- `char * __cdecl vostok::strings::append<512>(char (&)[512], char const *)`
- `char __cdecl vostok::math::sign(float)`
- `char const * __cdecl vostok::build::build_date(void)`
- `char const * __cdecl vostok::core::user_data_directory(void)`
- `char const * __cdecl vostok::logging::verbosity_to_string(enum vostok::logging::verbosity)`
- `char const * __cdecl vostok::particle::read_config_value<char const *, class vostok::configs::binary_config_value>(class vostok::configs::binary_config_value const &, char const *, char const *const &)`
- `char const * __cdecl vostok::render::decl_utils::ConvertSemantic(enum _D3DDECLUSAGE)`
- `char const * __cdecl vostok::render::get_textures_path2(void)`
- `char const * __cdecl vostok::resources::test_allocator_name(enum vostok::resources::class_id_enum)`
- `char const * __cdecl vostok::vfs::get_mount_log_type(class vostok::vfs::base_node<1> *, class vostok::vfs::mount_root_node_base<1> *)`
- `class SpeedTree::Mat4x4 __cdecl vostok::render::vostok_to_speedtree(class vostok::math::float4x4const &)`
- `class SpeedTree::Vec3 __cdecl vostok::render::vostok_to_speedtree(class vostok::math::float3const &)`
- `class boost::asio::const_buffers_1 __cdecl vostok::network_core::buffer_to_send(class vostok::network_core::tcp_packet &)`
- `class boost::asio::mutable_buffers_1 __cdecl vostok::network_core::buffer_to_receive_into(class vostok::network_core::tcp_packet &)`
- `class boost::function<void __cdecl (class vostok::resources::query_result *, class vostok::resources::memory_usage_type const &, enum vostok::resources::class_id_enum)> __cdecl vostok::resources::get_resource_freed_callback(void)`
- `class btBvhTriangleMeshShape * __cdecl vostok::physics::create_btBvhTriangleMeshShape(class vostok::math::float3*, unsigned int *, unsigned int, unsigned int, unsigned short *, class vostok::math::float3const &, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &)`
- `class btCollisionShape * __cdecl vostok::physics::create_bt_primitive(enum vostok::collision::primitive_type, class vostok::math::float3const &, class vostok::math::float3const &)`
- `class btVector3 __cdecl vostok::physics::computeReflectionDirection(class btVector3const &, class btVector3const &)`
- `class btVector3 __cdecl vostok::physics::parallelComponent(class btVector3const &, class btVector3const &)`
- `class btVector3 __cdecl vostok::physics::perpindicularComponent(class btVector3const &, class btVector3const &)`
- `class vostok::animation::mixing::expression __cdecl vostok::animation::mixing::operator+(class vostok::animation::mixing::expression &, class vostok::animation::mixing::expression &)`
- `class vostok::animation::mixing::n_ary_tree_animation_node * __cdecl vostok::animation::mixing::find_animation(class vostok::animation::mixing::n_ary_tree_animation_node *const, class vostok::animation::mixing::n_ary_tree_animation_node *const, class vostok::animation::mixing::n_ary_tree_animation_node &)`
- `class vostok::collision::geometry * __cdecl vostok::collision::new_triangle_mesh_geometry(class vostok::memory::base_allocator *, class vostok::math::float3const *, unsigned int, unsigned int const *, unsigned int, unsigned int const *, unsigned int)`
- `class vostok::debug::detail::string_helper __cdecl vostok::debug::detail::make_fail_message<unsigned int, unsigned int>(unsigned int const &, unsigned int const &)`
- `class vostok::fs_new::device_file_system_interface * __cdecl vostok::core::get_core_device_file_system(void)`
- `class vostok::fs_new::physical_path_info __cdecl vostok::resources::get_physical_path_info(class vostok::fs_new::native_path_string const &, bool)`
- `class vostok::fs_new::synchronous_device_interface & __cdecl vostok::core::get_core_synchronous_device(void)`
- `class vostok::intrusive_list<class vostok::tasks::task_type, class vostok::tasks::task_type *, 104, class vostok::threading::mutex_tasks_unaware, class vostok::size_policy, class vostok::no_debug_policy> * __cdecl vostok::tasks::get_task_type_list(void)`
- `class vostok::intrusive_list<struct vostok::vfs::mount_referer_base, struct vostok::vfs::mount_referer *, 0, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy> * __cdecl vostok::vfs::get_ready_referers_list(class vostok::memory::base_allocator *)`
- `class vostok::intrusive_ptr<struct vostok::render::custom_config, struct vostok::render::custom_config, class vostok::threading::simple_lock> __cdecl vostok::render::create_custom_config(class vostok::configs::binary_config_value const &, unsigned int &, bool)`
- `class vostok::intrusive_ptr<struct vostok::render::custom_config, struct vostok::render::custom_config, class vostok::threading::simple_lock> __cdecl vostok::render::create_custom_config(class vostok::render::custom_config_value const &, unsigned int &, bool)`
- `class vostok::intrusive_ptr<struct vostok::render::custom_config, struct vostok::render::custom_config, class vostok::threading::simple_lock> __cdecl vostok::render::create_custom_config(struct vostok::render::effect_options_descriptor const &, class vostok::mutable_buffer &, unsigned int &, bool)`
- `class vostok::intrusive_ptr<struct vostok::render::custom_config, struct vostok::render::custom_config, class vostok::threading::simple_lock> __cdecl vostok::render::create_custom_config(struct vostok::render::effect_options_descriptor const &, unsigned int &, bool)`
- `class vostok::logging::filter_tree * __cdecl vostok::logging::new_filter_tree(class vostok::memory::base_allocator &)`
- `class vostok::logging::log_file * __cdecl vostok::logging::new_log_file(class vostok::memory::base_allocator &, class vostok::fs_new::device_file_system_no_watcher_proxy &, char const *, enum vostok::logging::log_file_usage_enum)`
- `class vostok::math::float2 __cdecl vostok::math::operator-(class vostok::math::float2_pod const &, class vostok::math::float2_pod const &)`
- `class vostok::math::float3 __cdecl vostok::collision::closest_point_on_segment(class vostok::math::float3const &, class vostok::math::float3const &, class vostok::math::float3const &)`
- `class vostok::math::float3 __cdecl vostok::math::cross_product(class vostok::math::float3_pod const &, class vostok::math::float3_pod const &)`
- `class vostok::math::float3 __cdecl vostok::math::normalize(class vostok::math::float3_pod const &)`
- `class vostok::math::float3 __cdecl vostok::math::operator*(class vostok::math::float3_pod const &, float const &)`
- `class vostok::math::float3 __cdecl vostok::math::operator*(float const &, class vostok::math::float3_pod const &)`
- `class vostok::math::float3 __cdecl vostok::math::operator+(class vostok::math::float3_pod const &, class vostok::math::float3_pod const &)`
- `class vostok::math::float3 __cdecl vostok::math::operator-(class vostok::math::float3_pod const &, class vostok::math::float3_pod const &)`
- `class vostok::math::float3 __cdecl vostok::math::operator^(class vostok::math::float3_pod const &, class vostok::math::float3_pod const &)`
- `class vostok::math::float3 __cdecl vostok::math::pow(class vostok::math::float3_pod const &, float)`
- `class vostok::math::float3 __cdecl vostok::particle::linear_interpolation<class vostok::math::float3>(class vostok::math::float3, class vostok::math::float3, float)`
- `class vostok::math::float3 __cdecl vostok::render::speedtree_to_vostok(class SpeedTree::Vec3const &)`
- `class vostok::math::float3_pod __cdecl vostok::particle::cubic_interpolation<class vostok::math::float3_pod, float>(class vostok::math::float3_pod, class vostok::math::float3_pod, class vostok::math::float3_pod, class vostok::math::float3_pod, float)`
- `class vostok::math::float3_pod __cdecl vostok::particle::linear_interpolation<class vostok::math::float3_pod>(class vostok::math::float3_pod, class vostok::math::float3_pod, float)`
- `class vostok::math::float4 __cdecl vostok::math::operator*(class vostok::math::float4_pod const &, float const &)`
- `class vostok::math::float4 __cdecl vostok::math::operator+(class vostok::math::float4_pod const &, class vostok::math::float4_pod const &)`
- `class vostok::math::float4 __cdecl vostok::math::pow(class vostok::math::float4_pod const &, float)`
- `class vostok::math::float4 __cdecl vostok::render::speedtree_to_vostok(class SpeedTree::Vec4const &)`
- `class vostok::math::float4_pod __cdecl vostok::particle::cubic_interpolation<class vostok::math::float4_pod, float>(class vostok::math::float4_pod, class vostok::math::float4_pod, class vostok::math::float4_pod, class vostok::math::float4_pod, float)`
- `class vostok::math::float4_pod __cdecl vostok::particle::linear_interpolation<class vostok::math::float4_pod>(class vostok::math::float4_pod, class vostok::math::float4_pod, float)`
- `class vostok::math::float4x4 __cdecl survarium::get_bone_matrix_in_object_space(class vostok::animation::skeleton_bone const &, class vostok::animation::skeleton const &, class vostok::math::float4x4const *)`
- `class vostok::math::float4x4 __cdecl survarium::get_bone_matrix_in_object_space_impl(class vostok::animation::skeleton_bone const &, class vostok::math::float4x4const *, class vostok::animation::skeleton_bone const *)`
- `class vostok::math::float4x4 __cdecl survarium::mix_transformations(class vostok::math::float4x4const &, class vostok::math::float4x4const &, float)`
- `class vostok::math::float4x4 __cdecl survarium::mix_transformations(class vostok::math::float4x4const &, class vostok::math::float4x4const &, float, float)`
- `class vostok::math::float4x4 __cdecl vostok::math::invert4x4(class vostok::math::float4x4const &)`
- `class vostok::math::float4x4 __cdecl vostok::math::lerp(class vostok::math::float4x4const &, class vostok::math::float4x4const &, float)`
- `class vostok::math::float4x4 __cdecl vostok::render::speedtree_to_vostok(class SpeedTree::Mat4x4const &)`
- `class vostok::math::plane __cdecl vostok::math::create_plane_normalized(class vostok::math::float3const &, class vostok::math::float3const &)`
- `class vostok::math::quaternion __cdecl vostok::math::create_quaternion_from_direction_vector(class vostok::math::float3const &)`
- `class vostok::memory::base_allocator * __cdecl vostok::resources::helper_allocator(void)`
- `class vostok::memory::base_allocator * __cdecl vostok::resources::unmanaged_allocator(void)`
- `class vostok::memory::doug_lea_allocator & __cdecl survarium::game_module::allocator(void)`
- `class vostok::mutable_buffer __cdecl vostok::operator+(class vostok::mutable_buffer const &, unsigned int)`
- `class vostok::network_core::udp_match_packet * __cdecl vostok::network_core::new_udp_match_packet(class vostok::memory::single_size_buffer_allocator<300, class vostok::threading::single_threading_policy> &)`
- `class vostok::physics::bt_character_controller * __cdecl vostok::physics::create_character_controller(class vostok::memory::base_allocator &, struct vostok::physics::world *)`
- `class vostok::physics::bt_collision_shape * __cdecl vostok::physics::create_static_triangle_mesh_shape(class vostok::math::float3*, unsigned int *, unsigned int, unsigned int, unsigned short *, class vostok::math::float3const &, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &)`
- `class vostok::render::culling::aab_rect __cdecl vostok::render::culling::get_intersection_rect(class vostok::render::culling::aab_rect const &, class vostok::render::culling::aab_rect const &)`
- `class vostok::render::engine::world * __cdecl vostok::render::engine::create_world(class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &, bool)`
- `class vostok::render::world * __cdecl vostok::render::create_world(class vostok::memory::base_allocator &, class vostok::memory::base_allocator *, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &, bool)`
- `class vostok::resources::cook_base * __cdecl vostok::resources::unregister_cook(enum vostok::resources::class_id_enum)`
- `class vostok::resources::resource_base * __cdecl vostok::resources::cast_resource_base(struct vostok::vfs::vfs_association *const)`
- `class vostok::resources::resource_ptr<class survarium::artefact_base, class vostok::resources::unmanaged_intrusive_base> __cdecl vostok::static_cast_resource_ptr<class vostok::resources::resource_ptr<class survarium::artefact_base, class vostok::resources::unmanaged_intrusive_base>, class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `class vostok::resources::resource_ptr<class vostok::animation::skeleton, class vostok::resources::unmanaged_intrusive_base> __cdecl vostok::static_cast_resource_ptr<class vostok::resources::resource_ptr<class vostok::animation::skeleton, class vostok::resources::unmanaged_intrusive_base>, class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> __cdecl vostok::configs::create_binary_config(class vostok::mutable_buffer const &, class vostok::memory::base_allocator &)`
- `class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> __cdecl vostok::static_cast_resource_ptr<class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> __cdecl vostok::static_cast_resource_ptr<class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>, class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &)`
- `class vostok::resources::resource_ptr<class vostok::sound::panning_lut, class vostok::resources::unmanaged_intrusive_base> __cdecl vostok::static_cast_resource_ptr<class vostok::resources::resource_ptr<class vostok::sound::panning_lut, class vostok::resources::unmanaged_intrusive_base>, class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `class vostok::resources::resource_ptr<struct vostok::resources::unmanaged_allocation_resource, class vostok::resources::unmanaged_intrusive_base> __cdecl vostok::static_cast_resource_ptr<class vostok::resources::resource_ptr<struct vostok::resources::unmanaged_allocation_resource, class vostok::resources::unmanaged_intrusive_base>, class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `class vostok::resources::vfs_sub_fat_cook * __cdecl vostok::resources::get_vfs_sub_fat_cook(void)`
- `class vostok::tasks::task * __cdecl vostok::tasks::grab_next_task(void)`
- `class vostok::tasks::thread_pool * __cdecl vostok::tasks::get_thread_pool(void)`
- `class vostok::vfs::archive_compressed_file_node<1> * __cdecl vostok::vfs::cast_archive_compressed_file<1>(class vostok::vfs::base_node<1> *)`
- `class vostok::vfs::archive_compressed_file_node<1> const * __cdecl vostok::vfs::cast_archive_compressed_file<1>(class vostok::vfs::base_node<1> const *)`
- `class vostok::vfs::archive_compressed_file_node<1> const * __cdecl vostok::vfs::node_cast<class vostok::vfs::archive_compressed_file_node, class vostok::vfs::base_node, 1>(class vostok::vfs::base_node<1> const *)`
- `class vostok::vfs::archive_file_node<1> * __cdecl vostok::vfs::cast_archive_file<1>(class vostok::vfs::base_node<1> *)`
- `class vostok::vfs::archive_file_node<1> const * __cdecl vostok::vfs::cast_archive_file<1>(class vostok::vfs::base_node<1> const *)`
- `class vostok::vfs::archive_file_node<1> const * __cdecl vostok::vfs::node_cast<class vostok::vfs::archive_file_node, class vostok::vfs::base_node, 1>(class vostok::vfs::base_node<1> const *)`
- `class vostok::vfs::archive_folder_mount_root_node<1> * __cdecl vostok::vfs::cast_archive_folder_mount_root<1>(class vostok::vfs::base_node<1> *)`
- `class vostok::vfs::archive_inline_compressed_file_node<1> * __cdecl vostok::vfs::cast_archive_inline_compressed_file<1>(class vostok::vfs::base_node<1> *)`
- `class vostok::vfs::archive_inline_compressed_file_node<1> const * __cdecl vostok::vfs::cast_archive_inline_compressed_file<1>(class vostok::vfs::base_node<1> const *)`
- `class vostok::vfs::archive_inline_compressed_file_node<1> const * __cdecl vostok::vfs::node_cast<class vostok::vfs::archive_inline_compressed_file_node, class vostok::vfs::base_node, 1>(class vostok::vfs::base_node<1> const *)`
- `class vostok::vfs::archive_inline_file_node<1> * __cdecl vostok::vfs::cast_archive_inline_file<1>(class vostok::vfs::base_node<1> *)`
- `class vostok::vfs::archive_inline_file_node<1> const * __cdecl vostok::vfs::cast_archive_inline_file<1>(class vostok::vfs::base_node<1> const *)`
- `class vostok::vfs::archive_inline_file_node<1> const * __cdecl vostok::vfs::node_cast<class vostok::vfs::archive_inline_file_node, class vostok::vfs::base_node, 1>(class vostok::vfs::base_node<1> const *)`
- `class vostok::vfs::base_folder_node<1> * __cdecl vostok::vfs::cast_folder<1>(class vostok::vfs::physical_folder_mount_root_node<1> *)`
- `class vostok::vfs::base_folder_node<1> * __cdecl vostok::vfs::node_cast<class vostok::vfs::base_folder_node, class vostok::vfs::archive_folder_mount_root_node, 1>(class vostok::vfs::archive_folder_mount_root_node<1> *)`
- `class vostok::vfs::base_folder_node<1> * __cdecl vostok::vfs::node_cast<class vostok::vfs::base_folder_node, class vostok::vfs::base_node, 1>(class vostok::vfs::base_node<1> *)`
- `class vostok::vfs::base_folder_node<1> * __cdecl vostok::vfs::node_cast<class vostok::vfs::base_folder_node, class vostok::vfs::mount_helper_node, 1>(class vostok::vfs::mount_helper_node<1> *)`
- `class vostok::vfs::base_folder_node<1> * __cdecl vostok::vfs::node_cast<class vostok::vfs::base_folder_node, class vostok::vfs::physical_folder_mount_root_node, 1>(class vostok::vfs::physical_folder_mount_root_node<1> *)`
- `class vostok::vfs::base_folder_node<1> const * __cdecl vostok::vfs::cast_folder<1>(class vostok::vfs::base_node<1> const *)`
- `class vostok::vfs::base_folder_node<1> const * __cdecl vostok::vfs::node_cast<class vostok::vfs::base_folder_node, class vostok::vfs::base_node, 1>(class vostok::vfs::base_node<1> const *)`
- `class vostok::vfs::base_node<1> * __cdecl vostok::vfs::cast_node<1>(class vostok::vfs::base_node<1> *)`
- `class vostok::vfs::base_node<1> * __cdecl vostok::vfs::cast_node<1>(class vostok::vfs::hard_link_node<1> *)`
- `class vostok::vfs::base_node<1> * __cdecl vostok::vfs::cast_node<1>(class vostok::vfs::physical_file_mount_root_node<1> *)`
- `class vostok::vfs::base_node<1> * __cdecl vostok::vfs::cast_node<1>(class vostok::vfs::physical_folder_mount_root_node<1> *)`
- `class vostok::vfs::base_node<1> * __cdecl vostok::vfs::find_overlapped_by_mount_id(class vostok::vfs::base_node<1> *, unsigned int)`
- `class vostok::vfs::base_node<1> * __cdecl vostok::vfs::get_attach_node(class vostok::vfs::mount_root_node_base<1> *)`
- `class vostok::vfs::base_node<1> * __cdecl vostok::vfs::node_cast<class vostok::vfs::base_node, class vostok::vfs::archive_folder_mount_root_node, 1>(class vostok::vfs::archive_folder_mount_root_node<1> *)`
- `class vostok::vfs::base_node<1> * __cdecl vostok::vfs::node_cast<class vostok::vfs::base_node, class vostok::vfs::base_folder_node, 1>(class vostok::vfs::base_folder_node<1> *)`
- `class vostok::vfs::base_node<1> * __cdecl vostok::vfs::node_cast<class vostok::vfs::base_node, class vostok::vfs::base_node, 1>(class vostok::vfs::base_node<1> *)`
- `class vostok::vfs::base_node<1> * __cdecl vostok::vfs::node_cast<class vostok::vfs::base_node, class vostok::vfs::hard_link_node, 1>(class vostok::vfs::hard_link_node<1> *)`
- `class vostok::vfs::base_node<1> * __cdecl vostok::vfs::node_cast<class vostok::vfs::base_node, class vostok::vfs::mount_helper_node, 1>(class vostok::vfs::mount_helper_node<1> *)`
- `class vostok::vfs::base_node<1> * __cdecl vostok::vfs::node_cast<class vostok::vfs::base_node, class vostok::vfs::mount_root_node_base, 1>(class vostok::vfs::mount_root_node_base<1> *)`
- `class vostok::vfs::base_node<1> * __cdecl vostok::vfs::node_cast<class vostok::vfs::base_node, class vostok::vfs::physical_file_mount_root_node, 1>(class vostok::vfs::physical_file_mount_root_node<1> *)`
- `class vostok::vfs::base_node<1> * __cdecl vostok::vfs::node_cast<class vostok::vfs::base_node, class vostok::vfs::physical_folder_mount_root_node, 1>(class vostok::vfs::physical_folder_mount_root_node<1> *)`
- `class vostok::vfs::base_node<1> * __cdecl vostok::vfs::node_cast<class vostok::vfs::base_node, class vostok::vfs::physical_folder_node, 1>(class vostok::vfs::physical_folder_node<1> *)`
- `class vostok::vfs::erased_node<1> * __cdecl vostok::vfs::node_cast<class vostok::vfs::erased_node, class vostok::vfs::base_node, 1>(class vostok::vfs::base_node<1> *)`
- `class vostok::vfs::external_subfat_node<1> * __cdecl vostok::vfs::cast_external_node<1>(class vostok::vfs::base_node<1> *)`
- `class vostok::vfs::external_subfat_node<1> * __cdecl vostok::vfs::node_cast<class vostok::vfs::external_subfat_node, class vostok::vfs::base_node, 1>(class vostok::vfs::base_node<1> *)`
- `class vostok::vfs::external_subfat_node<1> const * __cdecl vostok::vfs::cast_external_node<1>(class vostok::vfs::base_node<1> const *)`
- `class vostok::vfs::external_subfat_node<1> const * __cdecl vostok::vfs::node_cast<class vostok::vfs::external_subfat_node, class vostok::vfs::base_node, 1>(class vostok::vfs::base_node<1> const *)`
- `class vostok::vfs::hard_link_node<1> * __cdecl vostok::vfs::cast_hard_link<1>(class vostok::vfs::base_node<1> *)`
- `class vostok::vfs::hard_link_node<1> * __cdecl vostok::vfs::node_cast<class vostok::vfs::hard_link_node, class vostok::vfs::base_node, 1>(class vostok::vfs::base_node<1> *)`
- `class vostok::vfs::hard_link_node<1> const * __cdecl vostok::vfs::cast_hard_link<1>(class vostok::vfs::base_node<1> const *)`
- `class vostok::vfs::hard_link_node<1> const * __cdecl vostok::vfs::node_cast<class vostok::vfs::hard_link_node, class vostok::vfs::base_node, 1>(class vostok::vfs::base_node<1> const *)`
- `class vostok::vfs::mount_helper_node<1> * __cdecl vostok::vfs::cast_mount_helper_node<1>(class vostok::vfs::base_node<1> *)`
- `class vostok::vfs::mount_root_node_base<1> * __cdecl vostok::vfs::cast_mount_root_node_base<1>(class vostok::vfs::base_node<1> *)`
- `class vostok::vfs::physical_file_mount_root_node<1> * __cdecl vostok::vfs::cast_physical_file_mount_root<1>(class vostok::vfs::base_node<1> *)`
- `class vostok::vfs::physical_file_mount_root_node<1> * __cdecl vostok::vfs::node_cast<class vostok::vfs::physical_file_mount_root_node, class vostok::vfs::mount_root_node_base, 1>(class vostok::vfs::mount_root_node_base<1> *)`
- `class vostok::vfs::physical_file_node<1> const * __cdecl vostok::vfs::cast_physical_file<1>(class vostok::vfs::base_node<1> const *)`
- `class vostok::vfs::physical_file_node<1> const * __cdecl vostok::vfs::node_cast<class vostok::vfs::physical_file_node, class vostok::vfs::base_node, 1>(class vostok::vfs::base_node<1> const *)`
- `class vostok::vfs::physical_folder_mount_root_node<1> * __cdecl vostok::vfs::cast_physical_folder_mount_root<1>(class vostok::vfs::base_node<1> *)`
- `class vostok::vfs::physical_folder_mount_root_node<1> * __cdecl vostok::vfs::node_cast<class vostok::vfs::physical_folder_mount_root_node, class vostok::vfs::mount_root_node_base, 1>(class vostok::vfs::mount_root_node_base<1> *)`
- `class vostok::vfs::physical_folder_node<1> * __cdecl vostok::vfs::cast_physical_folder<1>(class vostok::vfs::base_node<1> *)`
- `class vostok::vfs::physical_folder_node<1> * __cdecl vostok::vfs::cast_physical_folder<1>(class vostok::vfs::physical_folder_mount_root_node<1> *)`
- `class vostok::vfs::physical_folder_node<1> * __cdecl vostok::vfs::node_cast<class vostok::vfs::physical_folder_node, class vostok::vfs::physical_folder_mount_root_node, 1>(class vostok::vfs::physical_folder_mount_root_node<1> *)`
- `class vostok::vfs::universal_file_node<1> * __cdecl vostok::vfs::cast_universal_file_node<1>(class vostok::vfs::base_node<1> *)`
- `class vostok::vfs::universal_file_node<1> const * __cdecl vostok::vfs::cast_universal_file_node<1>(class vostok::vfs::base_node<1> const *)`
- `class vostok::vfs::universal_file_node<1> const * __cdecl vostok::vfs::node_cast<class vostok::vfs::universal_file_node, class vostok::vfs::base_node, 1>(class vostok::vfs::base_node<1> const *)`
- `clean<vostok::animation::mixing::binary_tree_addition_node>`
- `clean<vostok::animation::mixing::binary_tree_animation_node>`
- `clean<vostok::animation::mixing::binary_tree_multiplication_node>`
- `clean<vostok::animation::mixing::binary_tree_subtraction_node>`
- `closest_point_on_segment`
- `compute_gaussian_value`
- `convert_stick_values`
- `convert_to_unicode_if_needed<214>`
- `convert_to_unicode_if_needed<260>`
- `convert_to_unicode_if_needed<64>`
- `destroy<vostok::animation::mixing::n_ary_tree_addition_node>`
- `destroy<vostok::animation::mixing::n_ary_tree_animation_node>`
- `destroy<vostok::animation::mixing::n_ary_tree_multiplication_node>`
- `destroy<vostok::animation::mixing::n_ary_tree_subtraction_node>`
- `destroy<vostok::animation::mixing::n_ary_tree_time_scale_node>`
- `destroy<vostok::animation::mixing::n_ary_tree_time_scale_transition_node>`
- `destroy<vostok::animation::mixing::n_ary_tree_weight_node>`
- `destroy<vostok::animation::mixing::n_ary_tree_weight_transition_node>`
- `empty_function`
- `enqueue_impl`
- `enum DXGI_FORMAT __cdecl vostok::render::decl_utils::ConvertVertexFormat(enum _D3DDECLTYPE)`
- `enum vostok::particle::enum_evaluate_type __cdecl vostok::particle::string_to_evaluate_type(char const *)`
- `enum vostok::threading::lock_type_enum __cdecl vostok::vfs::to_threading_lock_type(enum vostok::vfs::lock_type_enum)`
- `enum vostok::vfs::result_enum __cdecl vostok::vfs::find_async_and_wait(class vostok::vfs::virtual_file_system &, class vostok::fs_new::virtual_path_string const &, class vostok::vfs::vfs_locked_iterator *, enum vostok::vfs::find_enum, class vostok::memory::base_allocator *, class boost::function<void __cdecl (void)> const &)`
- `enum vostok::vfs::vfs_iterator::type_enum __cdecl vostok::vfs::iterator_type(enum vostok::vfs::find_enum)`
- `execute_handler_filter`
- `extrapolated_slerp`
- `float __cdecl sqrt_safe(float)`
- `float __cdecl survarium::always_unit_timescale_calculator(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, struct survarium::weapon_state_creation_params const &)`
- `float __cdecl survarium::get_additional_length(class vostok::math::float3const &, class vostok::math::float3const &, float)`
- `float __cdecl survarium::get_angle(float, float, float)`
- `float __cdecl survarium::get_booster_value(enum survarium::boosters_enum, struct survarium::player_profile const &)`
- `float __cdecl vostok::math::abs(float)`
- `float __cdecl vostok::math::acos(float)`
- `float __cdecl vostok::math::atan2(float, float)`
- `float __cdecl vostok::math::clamp_r<float>(float, float, float)`
- `float __cdecl vostok::math::cos(float)`
- `float __cdecl vostok::math::cubic_interpolation<float, float>(float, float, float, float, float)`
- `float __cdecl vostok::math::deg2rad(float)`
- `float __cdecl vostok::math::get_tangent_from_2d_vector(class vostok::math::float2const &)`
- `float __cdecl vostok::math::length(class vostok::math::float3const &)`
- `float __cdecl vostok::math::lerp<float>(float const &, float const &, float)`
- `float __cdecl vostok::math::max(float, float)`
- `float __cdecl vostok::math::min(float, float)`
- `float __cdecl vostok::math::operator|(class vostok::math::float3_pod const &, class vostok::math::float3_pod const &)`
- `float __cdecl vostok::math::pow(float, float)`
- `float __cdecl vostok::math::pow_impl(float, unsigned int)`
- `float __cdecl vostok::math::segment_to_segment_distance(class vostok::math::float3const &, class vostok::math::float3const &, class vostok::math::float3const &, class vostok::math::float3const &)`
- `float __cdecl vostok::math::sin(float)`
- `float __cdecl vostok::math::sqr<float>(float const &)`
- `float __cdecl vostok::math::sqrt(float)`
- `float __cdecl vostok::math::tan(float)`
- `float __cdecl vostok::memory::uninitialized_value<float>(void)`
- `float __cdecl vostok::particle::cubic_interpolation<float, float>(float, float, float, float, float)`
- `float __cdecl vostok::particle::get_tangent_from_2d_vector(class vostok::math::float2const &)`
- `float __cdecl vostok::particle::linear_interpolation<float>(float, float, float)`
- `float __cdecl vostok::render::select_model_orientation(void)`
- `float __cdecl vostok::render::select_model_scale(float, float)`
- `float __cdecl vostok::resources::max_satisfaction_of_unreferenced_resource(void)`
- `float __cdecl vostok::resources::min_satisfaction_of_unreferenced_resource(void)`
- `free_region_impl`
- `get_current_process`
- `guess_exact_memory_size`
- `has_segment_link`
- `init_bins`
- `int __cdecl vostok::engine::get_exit_code(void)`
- `int __cdecl vostok::math::abs(int)`
- `int __cdecl vostok::math::max(int, int)`
- `int __cdecl vostok::math::min(int, int)`
- `int __cdecl vostok::memory::compare(class vostok::const_buffer const &, class vostok::const_buffer const &)`
- `int __cdecl vostok::render::calculate_needed_texture_mip_levels(class vostok::math::float4x4const &, class vostok::math::float3const &, class vostok::math::sphere const &, unsigned int, unsigned int, float, float &)`
- `int __cdecl vostok::render::compare(class vostok::render::res_xs<struct vostok::render::gs_data> const &, class vostok::render::res_xs<struct vostok::render::gs_data> const &)`
- `int __cdecl vostok::render::compare(class vostok::render::shader_constant_host const &, class vostok::render::shader_constant_host const &)`
- `int __cdecl vostok::sound::ogg_utils::ov_close_func(void *)`
- `int __cdecl vostok::sprintf<256>(char (&)[256], char const *const, ...)`
- `int __cdecl vostok::sprintf<4096>(char (&)[4096], char const *const, ...)`
- `int __cdecl vostok::sprintf<512>(char (&)[512], char const *const, ...)`
- `int __cdecl vostok::sprintf<64>(char (&)[64], char const *const, ...)`
- `int __cdecl vostok::strings::compare_insensitive(char const *, char const *)`
- `int __cdecl vostok::vsnprintf(char *const, unsigned int, unsigned int, char const *const, char *const)`
- `int __cdecl vostok::vsprintf(char *const, unsigned int, char const *const, char *const)`
- `interlockedexchange`
- `is_terminal_character`
- `is_unique_animation_lexeme`
- `line_line_intersect_non_parallel`
- `load_function<long (__stdcall*__stdcall(void))(_EXCEPTION_POINTERS *)>`
- `load_function<void __cdecl(void)>`
- `load_function<void __stdcall(char const *)>`
- `load_function<void __stdcall(enum BUGTRAP_ACTIVITY_tag)>`
- `load_function<void __stdcall(enum BUGTRAP_DIALOGMESSAGE_tag,char const *)>`
- `load_function<void __stdcall(enum BUGTRAP_REPORTFORMAT_tag)>`
- `long __cdecl vostok::debug::interlocked_compare_exchange(long &, long, long)`
- `long __cdecl vostok::debug::interlocked_decrement(long &)`
- `long __cdecl vostok::debug::interlocked_exchange(long &, long)`
- `long __cdecl vostok::debug::interlocked_increment(long &)`
- `long __cdecl vostok::threading::interlocked_and(long volatile &, long)`
- `long __cdecl vostok::threading::interlocked_compare_exchange(long volatile &, long, long)`
- `long __cdecl vostok::threading::interlocked_decrement(long volatile &)`
- `long __cdecl vostok::threading::interlocked_exchange(long volatile &, long)`
- `long __cdecl vostok::threading::interlocked_exchange_add(long volatile &, long)`
- `long __cdecl vostok::threading::interlocked_increment(long volatile &)`
- `long __cdecl vostok::threading::interlocked_or(long volatile &, long)`
- `lut_id`
- `mix_scales`
- `mmap_resize`
- `network_flow_emulator_options`
- `private: __thiscall survarium::booby_trap::booby_trap(class survarium::game_world &)`
- `private: __thiscall survarium::booby_trap_set::booby_trap_set(class survarium::game_world &)`
- `private: __thiscall survarium::double_barreled_weapon_core_aimed_idle_state::double_barreled_weapon_core_aimed_idle_state(class survarium::weapon_core &, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)`
- `private: __thiscall survarium::empty_hands::empty_hands(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> *, unsigned int)`
- `private: __thiscall survarium::pistol_weapon_core_aimed_idle_state::pistol_weapon_core_aimed_idle_state(class survarium::weapon_core &, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)`
- `private: __thiscall survarium::weapon_core_aimed_state::weapon_core_aimed_state(class survarium::weapon_core &, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_aimed_fire_state>::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_aimed_fire_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_fire_state>::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_fire_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state>::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_reload_state>::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_reload_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_show_state>::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_show_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_aimed_fire_state>::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_aimed_fire_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_fire_state>::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_fire_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state>::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_reload_state>::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_reload_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_show_state>::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_show_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::weapon_core_aimed_fire_state>::weapon_sound_events_handler_state<class survarium::weapon_core_aimed_fire_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::weapon_core_chamber_a_round_aimed_state>::weapon_sound_events_handler_state<class survarium::weapon_core_chamber_a_round_aimed_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::weapon_core_chamber_a_round_state>::weapon_sound_events_handler_state<class survarium::weapon_core_chamber_a_round_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::weapon_core_fire_state>::weapon_sound_events_handler_state<class survarium::weapon_core_fire_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state>::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::weapon_core_reload_state>::weapon_sound_events_handler_state<class survarium::weapon_core_reload_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_finish_substate>::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_finish_substate>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_one_round_substate>::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_one_round_substate>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_start_substate>::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_start_substate>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::weapon_core_show_state>::weapon_sound_events_handler_state<class survarium::weapon_core_show_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall vostok::render::debug::renderer::renderer(class vostok::render::one_way_render_channel &, class vostok::memory::base_allocator &, class vostok::render::engine::world &)`
- _...and 6412 more_

---

## v0.20e-build1916 → v0.20f-build1923
_2014-03-20 → 2014-04-01 · +1 / -3 / ~11_

### Changed (11)

| match % | function |
| ---: | --- |
| 0.00 | `private: virtual void __thiscall survarium::weapon_preview_state_cook::deallocate_resource(void *)` |
| 0.00 | `protected: virtual void __thiscall vostok::particle::particle_system::add_action_to_guid_list(char const *, class vostok::particle::particle_action *)` |
| 0.00 | `public: __thiscall boost::_bi::bind_t<void, class boost::_mfi::mf1<void, class vostok::engine::engine_world, class boost::function<void __cdecl (void)> >, class boost::_bi::list2<class boost::_bi::value<class vostok::engine::engine_world *>, class boost::_bi::value<class boost::function<void __cdecl (void)> > > >::bind_t<void, class boost::_mfi::mf1<void, class vostok::engine::engine_world, class boost::function<void __cdecl (void)> >, class boost::_bi::list2<class boost::_bi::value<class vostok::engine::engine_world *>, class boost::_bi::value<class boost::function<void __cdecl (void)> > > >(class boost::_bi::bind_t<void, class boost::_mfi::mf1<void, class vostok::engine::engine_world, class boost::function<void __cdecl (void)> >, class boost::_bi::list2<class boost::_bi::value<class vostok::engine::engine_world *>, class boost::_bi::value<class boost::function<void __cdecl (void)> > > > const &)` |
| 0.00 | `public: __thiscall survarium::affect_subscriber::~affect_subscriber(void)` |
| 0.00 | `public: __thiscall vostok::intrusive_list<struct survarium::affect_subscriber, struct survarium::affect_subscriber *, 32, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::~intrusive_list<struct survarium::affect_subscriber, struct survarium::affect_subscriber *, 32, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>(void)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base>::~resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base>(void)` |
| 0.00 | `public: virtual int __thiscall btConvexHullShape::getNumPlanes(void) const` |
| 0.00 | `public: virtual struct vostok::ui::window * __thiscall vostok::ui::ui_image::w(void)` |
| 0.00 | `public: virtual void __thiscall survarium::game_camera::on_focus(bool)` |
| 99.97 | `public: virtual void __thiscall vostok::network::network_world::dispatch_callbacks(void)` |
| 99.97 | `public: void __thiscall vostok::render::stage_shadow_direct::prepare_visibile_objects(class vostok::fixed_vector<struct vostok::render::caster_model, 2048> *, class vostok::memory::base_allocator *, class vostok::math::float3const &, unsigned int, unsigned int, unsigned int)` |

### Added (1)

- ``vostok::render::stage_lights::accumulate_particle_lighting'::`6'::sort_probes_by_size_predicate::operator()`

### Deleted (3)

- ``vostok::render::stage_visibility::filter_and_sort_env_probes'::`4'::sort_by_size_predicate::operator()`
- `public: __thiscall boost::_bi::bind_t<void, class boost::_mfi::mf3<void, class survarium::game_world, class vostok::resources::queries_result &, unsigned int, class boost::function<void __cdecl (class vostok::resources::queries_result &)> const &>, class boost::_bi::list4<class boost::_bi::value<class survarium::game_world *>, struct boost::arg<1>, class boost::_bi::value<unsigned int>, class boost::_bi::value<class boost::function<void __cdecl (class vostok::resources::queries_result &)> > > >::bind_t<void, class boost::_mfi::mf3<void, class survarium::game_world, class vostok::resources::queries_result &, unsigned int, class boost::function<void __cdecl (class vostok::resources::queries_result &)> const &>, class boost::_bi::list4<class boost::_bi::value<class survarium::game_world *>, struct boost::arg<1>, class boost::_bi::value<unsigned int>, class boost::_bi::value<class boost::function<void __cdecl (class vostok::resources::queries_result &)> > > >(class boost::_bi::bind_t<void, class boost::_mfi::mf3<void, class survarium::game_world, class vostok::resources::queries_result &, unsigned int, class boost::function<void __cdecl (class vostok::resources::queries_result &)> const &>, class boost::_bi::list4<class boost::_bi::value<class survarium::game_world *>, struct boost::arg<1>, class boost::_bi::value<unsigned int>, class boost::_bi::value<class boost::function<void __cdecl (class vostok::resources::queries_result &)> > > > const &)`
- `public: __thiscall vostok::fixed_vector<class vostok::intrusive_ptr<class vostok::render::shader_buffer, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, 32>::~fixed_vector<class vostok::intrusive_ptr<class vostok::render::shader_buffer, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, 32>(void)`

---

## v0.20f-build1923 → v0.21d-build2010
_2014-04-01 → 2014-04-24 · +605 / -383 / ~2566_

### Changed (2566)

| match % | function |
| ---: | --- |
| 0.00 | `class vostok::math::float3 __cdecl survarium::get_air_control_vector(struct survarium::player_input const &, float, enum survarium::jump_type_enum)` |
| 0.00 | `float __cdecl survarium::computed_hide_animation_time_scale(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, float)` |
| 0.00 | `private: class vostok::network_core::udp_match_packet * __thiscall vostok::network_core::udp_match_connection::new_low_level_packet(unsigned char)` |
| 0.00 | `private: enum vostok::animation::callback_return_type_enum __thiscall survarium::jump_logic_state_start::on_jump_event(struct vostok::animation::animation_callback_params &)` |
| 0.00 | `private: virtual bool __thiscall survarium::ladder::ladder_occluder::use_execute(struct survarium::usable_object_user_data *)` |
| 0.00 | `private: virtual struct vostok::engine_user::world * __thiscall survarium::game_module_proxy::create_world(struct vostok::engine_user::engine &, class vostok::render::world &, struct vostok::sound::world &, struct vostok::network::world &)` |
| 0.00 | `private: virtual unsigned int __thiscall survarium::grenade_core_cook::get_derived_resource_size(void)` |
| 0.00 | `private: virtual void __thiscall survarium::game::on_alttab(bool)` |
| 0.00 | `private: void __thiscall survarium::lobby_client::clear_profile_info(void)` |
| 0.00 | `private: void __thiscall vostok::network::login_client_impl::on_ping_sent(unsigned int, class boost::system::error_code const &, unsigned int)` |
| 0.00 | `private: void __thiscall vostok::render::device::create(void)` |
| 0.00 | `private: void __thiscall vostok::render::device::create_d3d(void)` |
| 0.00 | `protected: virtual void __thiscall vostok::memory::stack_allocator::call_free(void *, char const *const, char const *const, unsigned int)` |
| 0.00 | `protected: virtual void __thiscall vostok::particle::particle_system::add_action_to_guid_list(char const *, class vostok::particle::particle_action *)` |
| 0.00 | `protected: void __thiscall survarium::base_player::deactivate_physics(void)` |
| 0.00 | `protected: void __thiscall survarium::lobby_menu::create_player_params(struct survarium::flash_value &, class survarium::player_params_modifiers_container const &)` |
| 0.00 | `public: __thiscall boost::_bi::bind_t<void, class boost::_mfi::mf1<void, class vostok::engine::engine_world, class boost::function<void __cdecl (void)> >, class boost::_bi::list2<class boost::_bi::value<class vostok::engine::engine_world *>, class boost::_bi::value<class boost::function<void __cdecl (void)> > > >::bind_t<void, class boost::_mfi::mf1<void, class vostok::engine::engine_world, class boost::function<void __cdecl (void)> >, class boost::_bi::list2<class boost::_bi::value<class vostok::engine::engine_world *>, class boost::_bi::value<class boost::function<void __cdecl (void)> > > >(class boost::_bi::bind_t<void, class boost::_mfi::mf1<void, class vostok::engine::engine_world, class boost::function<void __cdecl (void)> >, class boost::_bi::list2<class boost::_bi::value<class vostok::engine::engine_world *>, class boost::_bi::value<class boost::function<void __cdecl (void)> > > > const &)` |
| 0.00 | `public: __thiscall survarium::artefact_lifebone_core::config::~config(void)` |
| 0.00 | `public: __thiscall survarium::lobby_player_profile::lobby_player_profile(void)` |
| 0.00 | `public: __thiscall survarium::player_creation_params::~player_creation_params(void)` |
| 0.00 | `public: __thiscall survarium::portable_interactive_object_core::~portable_interactive_object_core(void)` |
| 0.00 | `public: __thiscall vostok::buffer_vector<unsigned int>::buffer_vector<unsigned int>(void *, unsigned int, class vostok::buffer_vector<unsigned int> const &)` |
| 0.00 | `public: __thiscall vostok::intrusive_list<struct survarium::affect_subscriber, struct survarium::affect_subscriber *, 32, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::~intrusive_list<struct survarium::affect_subscriber, struct survarium::affect_subscriber *, 32, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>(void)` |
| 0.00 | `public: __thiscall vostok::network_core::udp_match_client::~udp_match_client(void)` |
| 0.00 | `public: __thiscall vostok::physics::bt_character_controller::bt_character_controller(struct vostok::physics::world *, unsigned short, unsigned short, class vostok::math::float2const &, class vostok::math::float2const &)` |
| 0.00 | `public: __thiscall vostok::render::sun_cascade::sun_cascade(struct vostok::render::sun_cascade const &)` |
| 0.00 | `public: __thiscall vostok::resources::pinned_ptr_const<unsigned char>::pinned_ptr_const<unsigned char>(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>)` |
| 0.00 | `public: __thiscall vostok::resources::pinned_ptr_const<unsigned char>::~pinned_ptr_const<unsigned char>(void)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base>::~resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base>(void)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>::~resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>(void)` |
| 0.00 | `public: bool __thiscall survarium::lobby_client::read_player_match_stats(class vostok::network_core::buffer_reader &)` |
| 0.00 | `public: bool __thiscall survarium::lobby_client::read_squad_info(class vostok::network_core::buffer_reader &)` |
| 0.00 | `public: bool __thiscall vostok::physics::character_controller_sweep_test_cache_template<struct vostok::physics::character_controller_move_step_tester::key_type, struct vostok::physics::character_controller_move_step_tester::value_type>::cache_predicate::operator()(struct stlp_std::pair<struct vostok::physics::character_controller_move_step_tester::key_type, struct vostok::physics::character_controller_move_step_tester::value_type> const &) const` |
| 0.00 | `public: char const * __thiscall vostok::fs_new::path_string_impl::c_str(void) const` |
| 0.00 | `public: class vostok::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base> & __thiscall vostok::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base>::operator=(class vostok::render::res_effect *)` |
| 0.00 | `public: virtual __thiscall survarium::items_dictionary::~items_dictionary(void)` |
| 0.00 | `public: virtual __thiscall survarium::jump_logic_state_start::~jump_logic_state_start(void)` |
| 0.00 | `public: virtual __thiscall vostok::network::send_queued_order::~send_queued_order(void)` |
| 0.00 | `public: virtual bool __thiscall vostok::collision::object::touch(void) const` |
| 0.00 | `public: virtual bool __thiscall vostok::render::stage_debug::is_effects_ready(void) const` |
| 0.00 | `public: virtual bool __thiscall vostok::ui::ui_window::get_visible(void) const` |
| 0.00 | `public: virtual int __thiscall btConvexHullShape::getNumPlanes(void) const` |
| 0.00 | `public: virtual struct vostok::ui::font const * __thiscall vostok::ui::ui_world::default_font(void)` |
| 0.00 | `public: virtual unsigned int __thiscall vostok::particle::particle_action_light::get_class_size(void) const` |
| 0.00 | `public: virtual void __thiscall survarium::effect_zone_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 0.00 | `public: virtual void __thiscall survarium::game_camera::on_focus(bool)` |
| 0.00 | `public: virtual void __thiscall survarium::weapon_core::set_next_ammo_type(void)` |
| 0.00 | `public: virtual void __thiscall vostok::detail::concrete_type_helper<struct survarium::weapon_cook_data>::copy(class vostok::mutable_buffer, class vostok::const_buffer)` |
| 0.00 | `public: virtual void __thiscall vostok::detail::concrete_type_helper<struct vostok::physics::world *>::copy(class vostok::mutable_buffer, class vostok::const_buffer)` |
| 0.00 | `public: virtual void __thiscall vostok::input::input_world::remove_handler(struct vostok::input::handler &)` |
| 0.00 | `public: virtual void __thiscall vostok::network::enqueue_order::execute(void)` |
| 0.00 | `public: virtual void __thiscall vostok::network::functor_order::execute(void)` |
| 0.00 | `public: virtual void __thiscall vostok::render::stage_rain::execute(void)` |
| 0.00 | `public: virtual void __thiscall vostok::render::texture_cook::destroy_resource(class vostok::resources::managed_resource *)` |
| 0.00 | `public: virtual void __thiscall vostok::render::ui::draw_vertices_command::defer_execution(void)` |
| 0.00 | `public: void __thiscall survarium::base_player::stand_up(void)` |
| 0.00 | `public: void __thiscall survarium::lobby_menu::add_quest(struct survarium::quest_instance const &)` |
| 0.00 | `public: void __thiscall survarium::lobby_menu::on_client_status_received(enum vostok::lobby::query_info_types)` |
| 0.00 | `public: void __thiscall vostok::animation::fingers_to_weapon_corrector::activate_hand(enum vostok::animation::fingers_to_weapon_corrector::hands_enum, enum vostok::animation::finger_corrector_animation_events_type_enum, unsigned int)` |
| 0.00 | `public: void __thiscall vostok::animation::hand_to_weapon_ik_solver::activate_hand(enum vostok::animation::hand_to_weapon_ik_solver::hands_enum, enum vostok::animation::ik_animation_events_type, unsigned int)` |
| 0.00 | `public: void __thiscall vostok::buffer_vector<class vostok::render::scene *>::erase(class vostok::render::scene **const &)` |
| 0.00 | `public: void __thiscall vostok::network_core::udp_match_client::connect(char const *, unsigned short, class vostok::network_core::udp_match_packet *, unsigned int)` |
| 0.00 | `public: void __thiscall vostok::network_core::udp_match_client::send_queued_packets(unsigned int)` |
| 0.00 | `unsigned int __cdecl survarium::get_jump_animation_index(enum survarium::jump_type_enum, bool, enum survarium::jump_animation_parts)` |
| 0.00 | `void __cdecl `public: void __thiscall vostok::render::effect_manager::create_effect<class vostok::render::effect_blur<13> >(class render::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base> *)'::`2'::descriptor_object::`dynamic atexit destructor'(void)` |
| 0.00 | `void __cdecl `public: void __thiscall vostok::render::effect_manager::create_effect<class vostok::render::effect_blur<17> >(class render::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base> *)'::`2'::descriptor_object::`dynamic atexit destructor'(void)` |
| 0.00 | `void __cdecl `public: void __thiscall vostok::render::effect_manager::create_effect<class vostok::render::effect_blur<21> >(class render::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base> *)'::`2'::descriptor_object::`dynamic atexit destructor'(void)` |
| 0.00 | `void __cdecl `public: void __thiscall vostok::render::effect_manager::create_effect<class vostok::render::effect_blur<25> >(class render::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base> *)'::`2'::descriptor_object::`dynamic atexit destructor'(void)` |
| 0.00 | `void __cdecl `public: void __thiscall vostok::render::effect_manager::create_effect<class vostok::render::effect_blur<3> >(class render::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base> *)'::`2'::descriptor_object::`dynamic atexit destructor'(void)` |
| 0.00 | `void __cdecl `public: void __thiscall vostok::render::effect_manager::create_effect<class vostok::render::effect_blur<5> >(class render::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base> *)'::`2'::descriptor_object::`dynamic atexit destructor'(void)` |
| 0.00 | `void __cdecl `public: void __thiscall vostok::render::effect_manager::create_effect<class vostok::render::effect_blur<7> >(class render::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base> *)'::`2'::descriptor_object::`dynamic atexit destructor'(void)` |
| 0.00 | `void __cdecl `public: void __thiscall vostok::render::effect_manager::create_effect<class vostok::render::effect_blur<9> >(class render::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base> *)'::`2'::descriptor_object::`dynamic atexit destructor'(void)` |
| 0.00 | `void __cdecl `public: void __thiscall vostok::render::effect_manager::create_effect<class vostok::render::effect_hiz_occlusion>(class render::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base> *)'::`2'::descriptor_object::`dynamic atexit destructor'(void)` |
| 0.00 | `void __cdecl `public: void __thiscall vostok::render::effect_manager::create_effect<class vostok::render::effect_mask_far_plane>(class render::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base> *)'::`2'::descriptor_object::`dynamic atexit destructor'(void)` |
| 0.00 | `vostok::render::draw_text` |
| 0.00 | `vostok::render::draw_text_shadowed` |
| 0.00 | `vostok::render::get_gaussain_weights_offsets` |
| 2.22 | `public: virtual void __thiscall survarium::player::tick(unsigned int)` |
| 3.22 | `public: void __thiscall vostok::network::match_client_impl::set_connection_ports(unsigned char, unsigned int, unsigned short, unsigned short)` |
| 3.49 | `private: virtual void __thiscall survarium::jump_logic_state_landing::initialize(void)` |
| 4.60 | `private: virtual void __thiscall survarium::player_logic_sprint_state::finalize(void)` |
| 5.71 | `private: virtual void __thiscall survarium::artefact_core_cook::query_for_derived_resources(class vostok::resources::query_result_for_cook &, class survarium::artefact_base &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 7.77 | `public: void __thiscall survarium::base_player::end_jump(void)` |
| 8.44 | `private: virtual void __thiscall survarium::game_statistics_handler::on_victory_item_event(unsigned char, enum survarium::victory_item_event_type, class survarium::victory_item_core const &)` |
| 9.05 | `public: virtual void __thiscall vostok::render::texture_cook_wrapper::translate_query(class vostok::resources::query_result_for_cook &)` |
| 9.79 | `public: void __thiscall vostok::render::resource_manager::initialize_texture_pools(void)` |
| 11.11 | `public: virtual void __thiscall vostok::render::stage_decals_accumulate::execute(void)` |
| 11.46 | `public: __thiscall vostok::render::stage_rain::stage_rain(class vostok::render::renderer *, class vostok::render::renderer_context *)` |
| 11.76 | `public: virtual void __thiscall survarium::items_dictionary_cook::delete_resource(class vostok::resources::resource_base *)` |
| 12.01 | `public: virtual void __thiscall vostok::input::input_world::add_handler(struct vostok::input::handler &)` |
| 14.48 | `public: float __thiscall survarium::weapon_user_animations_selector::look_time_factor(void) const` |
| 15.05 | `public: void __thiscall vostok::render::backend::flush_rt_views(void)` |
| 15.15 | `private: virtual void __thiscall survarium::player_logic_jump_state::initialize(void)` |
| 16.00 | `private: virtual class vostok::network_core::udp_match_packet * __thiscall survarium::match_client::new_packet(enum vostok::match::client::messages_enum)` |
| 16.75 | `public: virtual void __thiscall survarium::player::serialize(class vostok::network_core::buffer_writer const &, class vostok::network_core::buffer_writer const *, unsigned char (&)[32768], class vostok::intrusive_ptr<class vostok::animation::mixing::n_ary_tree_intrusive_base, class vostok::animation::mixing::n_ary_tree_intrusive_base, class vostok::threading::single_threading_policy> &, unsigned int)` |
| 17.35 | `public: virtual void __thiscall survarium::portable_interactive_object::deserialize(class vostok::network_core::buffer_reader &, class vostok::network_core::buffer_reader *, unsigned int)` |
| 17.37 | `private: void __thiscall survarium::profile_skin_visual_cook::on_configs_loaded(class vostok::resources::queries_result &, class vostok::resources::query_result_for_cook *, struct survarium::player_profile const *)` |
| 18.33 | `private: void __thiscall vostok::network_core::udp_match_connection::add_ordered_packet<class vostok::network_core::process_packet_predicate>(struct vostok::network_core::udp_match_connection::channel &, class vostok::network_core::udp_match_packet &, class vostok::network_core::process_packet_predicate const &)` |
| 18.38 | `private: void __thiscall vostok::network_core::udp_match_connection::call_predicate<class vostok::network_core::process_packet_predicate>(class vostok::network_core::process_packet_predicate const &, class vostok::network_core::buffer_reader &)` |
| 18.85 | `public: void __thiscall survarium::lobby_menu::on_stats_message_arrived(char const *, char const *, enum vostok::messaging::message_channel_enum)` |
| 19.61 | `private: void __thiscall survarium::network_client::process_static_match_info(class vostok::network_core::buffer_reader &)` |
| 20.47 | `private: void __thiscall vostok::network_core::udp_match_connection::process_low_level_message(class vostok::network_core::buffer_reader &, unsigned int)` |
| 22.14 | `public: bool __thiscall sequence_id_predicate::operator()(class vostok::network_core::udp_match_packet *) const` |
| 22.40 | `public: void __thiscall vostok::buffer_vector<struct vostok::render::ray>::assign<struct vostok::render::ray const *>(struct vostok::render::ray const *, struct vostok::render::ray const *const &)` |
| 22.70 | `private: float __thiscall survarium::weapon_core::vertical_recoil_value(unsigned int) const` |
| 22.81 | `public: virtual class vostok::math::aabb __thiscall vostok::render::skeleton_render_model_instance::get_aabb(void)` |
| 22.83 | `public: __thiscall survarium::game_world_ui::game_world_ui(class survarium::game_world &)` |
| 23.28 | `protected: virtual class survarium::artefact_base & __thiscall survarium::artefact_core_cook::construct_derived_resource(void *, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::game_effect_emitter, class vostok::resources::unmanaged_intrusive_base> const &, void *const) const` |
| 23.28 | `private: void __thiscall survarium::items_dictionary_cook::on_subresources_loaded(class vostok::resources::queries_result &, class survarium::items_dictionary *)` |
| 23.93 | `public: __thiscall vostok::network_core::udp_network_flow_emulator::~udp_network_flow_emulator(void)` |
| 24.35 | `public: void __thiscall vostok::buffer_vector<class vostok::render::shader_constant>::assign<class vostok::render::shader_constant const *>(class vostok::render::shader_constant const *, class vostok::render::shader_constant const *const &)` |
| 24.44 | `private: void __thiscall vostok::network_core::udp_match_connection::fill_packet_header(class vostok::network_core::udp_match_packet &)` |
| 24.44 | `public: virtual void __thiscall vostok::render::stage_screen_space_reflections::execute(void)` |
| 24.59 | `private: __thiscall survarium::artefact<class survarium::artefact_lifebone_core>::artefact<class survarium::artefact_lifebone_core>(class vostok::configs::binary_config_value const &, class vostok::resources::resource_ptr<class survarium::game_effect_emitter, class vostok::resources::unmanaged_intrusive_base> const &, class survarium::base_game_scene *)` |
| 24.59 | `private: __thiscall survarium::artefact<class survarium::artefact_spring_core>::artefact<class survarium::artefact_spring_core>(class vostok::configs::binary_config_value const &, class vostok::resources::resource_ptr<class survarium::game_effect_emitter, class vostok::resources::unmanaged_intrusive_base> const &, class survarium::base_game_scene *)` |
| 24.90 | `public: virtual void __thiscall survarium::inventory_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 25.71 | `public: void __thiscall vostok::render::effect_material_base::compile_end(class vostok::render::effect_compiler &)` |
| 26.54 | `public: static void __cdecl vostok::network_core::udp_match_connection::construct_packet(struct vostok::network_core::udp_match_packets_orderer &, class vostok::network_core::udp_match_packet &, unsigned char, char const *const)` |
| 26.83 | `message_processor` |
| 27.04 | `protected: void __thiscall survarium::base_player::activate_physics(void)` |
| 28.12 | `public: virtual void __thiscall vostok::engine::engine_world::on_alttab(bool)` |
| 28.25 | `private: void __thiscall vostok::network_core::udp_match_connection::process_multipacket_message<class vostok::network_core::process_packet_predicate>(class vostok::network_core::process_packet_predicate const &, class vostok::network_core::buffer_reader &)` |
| 28.31 | `public: virtual void __thiscall survarium::oxygen_tank::get_item_props(struct survarium::inventory_item_props &) const` |
| 28.67 | `private: void __thiscall vostok::network_core::udp_match_client::process_incoming_packet(class vostok::network_core::buffer_reader &, class boost::asio::ip::basic_endpoint<class boost::asio::ip::udp> const &, struct vostok::network_core::socket_handler *)` |
| 28.76 | `protected: void __thiscall survarium::base_player::tick_animations(unsigned int, unsigned int)` |
| 28.76 | `private: virtual void __thiscall survarium::player_logic_jump_state::serialize(class vostok::network_core::buffer_writer const &, class vostok::network_core::buffer_writer const *) const` |
| 29.86 | `private: bool __thiscall vostok::physics::bullet_character_controller::impassable_slope(class btVector3const &, class btVector3const &, class btVector3const &) const` |
| 30.00 | `private: virtual void __thiscall survarium::match_client::enqueue(class vostok::network_core::udp_match_packet *)` |
| 30.19 | `public: class vostok::fixed_vector<class vostok::render::sampler_slot, 16> & __thiscall vostok::fixed_vector<class vostok::render::sampler_slot, 16>::operator=(class vostok::fixed_vector<class vostok::render::sampler_slot, 16> const &)` |
| 30.43 | `private: void __thiscall survarium::player_profile::deserialize_slots(class vostok::network_core::buffer_reader &)` |
| 30.74 | `public: void __thiscall survarium::lobby_menu::fill_inventory_contents(void)` |
| 31.40 | `private: virtual bool __thiscall survarium::weapon_core_throw_grenade_state::is_ready_for_transition(void) const` |
| 31.96 | `public: void __thiscall survarium::intermediate_shared_statistics::clear(void)` |
| 32.29 | `public: virtual void __thiscall survarium::weapon_core::tick(unsigned int)` |
| 32.34 | `private: virtual void __thiscall survarium::weapon_core_throw_grenade_state::deserialize(class vostok::network_core::buffer_reader &, class vostok::network_core::buffer_reader *)` |
| 32.67 | `private: virtual void __thiscall survarium::breath_state_holding::tick(float, float)` |
| 33.41 | `private: __thiscall survarium::artefact<class survarium::artefact_rattle_core>::artefact<class survarium::artefact_rattle_core>(class vostok::configs::binary_config_value const &, class vostok::resources::resource_ptr<class survarium::game_effect_emitter, class vostok::resources::unmanaged_intrusive_base> const &, class survarium::base_game_scene *)` |
| 33.66 | `private: void __thiscall vostok::network::login_client_impl::ping(unsigned int)` |
| 33.69 | `public: class vostok::fixed_vector<struct vostok::render::effect_compiler::shader_cache_info, 32> const __thiscall vostok::render::effect_compiler::get_cached_shaders_info(void) const` |
| 33.71 | `private: void __thiscall vostok::render::texture_options_binary_cooker::on_lua_options_loaded(class vostok::resources::queries_result &)` |
| 34.22 | `public: __thiscall survarium::options_item_bool::options_item_bool(class survarium::options_tab &, char const *, unsigned char)` |
| 34.62 | `private: void __thiscall vostok::network_core::udp_match_connection::acknowledge_packets(class vostok::network_core::sequence_number<unsigned short>, unsigned __int64)` |
| 35.00 | `public: __thiscall survarium::artefact_spring_core::config::config(struct survarium::artefact_spring_core::config const &)` |
| 35.76 | `private: __thiscall survarium::artefact<class survarium::artefact_onyx_core>::artefact<class survarium::artefact_onyx_core>(class vostok::configs::binary_config_value const &, class vostok::resources::resource_ptr<class survarium::game_effect_emitter, class vostok::resources::unmanaged_intrusive_base> const &, class survarium::base_game_scene *)` |
| 36.00 | `class vostok::resources::resource_ptr<class survarium::weapon_core, class vostok::resources::unmanaged_intrusive_base> __cdecl vostok::static_cast_resource_ptr<class vostok::resources::resource_ptr<class survarium::weapon_core, class vostok::resources::unmanaged_intrusive_base>, class survarium::inventory_item, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::resource_ptr<class survarium::inventory_item, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 36.44 | `void __cdecl survarium::get_profile_faction_affinity(class survarium::items_dictionary const &, struct survarium::player_profile const &, enum survarium::factions_enum &, float &)` |
| 36.67 | `private: float __thiscall survarium::weapon_core::computed_backward_recoil_time(float, float, unsigned int, unsigned int, unsigned int, float)` |
| 36.68 | `private: virtual void __thiscall survarium::pvp_match_core_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 36.98 | `public: void __thiscall survarium::shared_statistics::deserialize(class vostok::network_core::buffer_reader &, unsigned int)` |
| 37.14 | `private: virtual void __thiscall survarium::player_logic_jump_state::deserialize(class vostok::network_core::buffer_reader &, class vostok::network_core::buffer_reader *)` |
| 38.24 | `public: void __thiscall survarium::shared_statistics::serialize(class vostok::network_core::buffer_writer const &, unsigned int) const` |
| 38.29 | `public: void __thiscall vostok::render::res_render_output::on_alttab(bool)` |
| 39.36 | `public: bool __thiscall survarium::lobby_client::read_enumerate_inventory_info(class vostok::network_core::buffer_reader &)` |
| 39.50 | `private: virtual void __thiscall survarium::weapon_core_throw_grenade_state::serialize(class vostok::network_core::buffer_writer const &, class vostok::network_core::buffer_writer const *) const` |
| 39.94 | `private: bool __thiscall vostok::network_core::udp_match_connection::update_acknowledgements(class vostok::network_core::sequence_number<unsigned short>, class vostok::network_core::sequence_number<unsigned short>, unsigned __int64)` |
| 40.00 | `public: virtual void __thiscall vostok::core::core_debug_engine::on_terminate(void) const` |
| 40.26 | `vostok::network_core::construct_multipacket_part` |
| 40.26 | `public: void __thiscall vostok::render::resource_manager::reload_modified_textures(void)` |
| 40.60 | `public: class vostok::network_core::udp_match_packet * __thiscall vostok::network::match_client::new_packet(unsigned char)` |
| 40.68 | `private: virtual void __thiscall survarium::breath_state_holding::initialize(void)` |
| 40.85 | `public: void __thiscall vostok::network_core::udp_match_connection::enqueue(class vostok::network_core::udp_match_packet *)` |
| 41.04 | `public: __thiscall vostok::render::res_declaration::res_declaration(struct D3D11_INPUT_ELEMENT_DESC const *, unsigned int)` |
| 41.16 | `private: struct survarium::anomaly_state * __thiscall survarium::generic_anomaly_core::select_state(void)` |
| 41.22 | `private: void __thiscall vostok::network_core::udp_match_connection::enqueue_impl(class vostok::network_core::udp_match_packet *)` |
| 41.27 | `private: virtual void __thiscall survarium::player_logic_sprint_state::initialize(void)` |
| 41.79 | `public: void __thiscall vostok::buffer_vector<struct survarium::hud_game_effect_presenter::effect_data>::assign<struct survarium::hud_game_effect_presenter::effect_data const *>(struct survarium::hud_game_effect_presenter::effect_data const *, struct survarium::hud_game_effect_presenter::effect_data const *const &)` |
| 41.92 | `private: virtual void __thiscall survarium::weapon_core_throw_grenade_state::initialize(void)` |
| 42.38 | `public: __thiscall survarium::player_profile::~player_profile(void)` |
| 42.51 | `private: void __thiscall vostok::render::res_render_output::initialize_swap_chain(struct IDXGISwapChain *)` |
| 42.80 | `public: virtual void __thiscall vostok::render::effect_downsample::compile(class vostok::render::effect_compiler &, class vostok::configs::binary_config_value const &, struct vostok::render::surface_effect_parameters const &)` |
| 43.07 | `private: void __thiscall vostok::animation::legs_ik_solver::process_leg(struct vostok::animation::legs_ik_solver::leg_params &, class vostok::math::float4x4const &, class vostok::math::float4x4const &, class vostok::math::float4x4*, class vostok::math::float4x4const &)` |
| 43.18 | `private: enum vostok::animation::callback_return_type_enum __thiscall survarium::portable_interactive_object_with_finger_correction::on_hand_correction_event(struct vostok::animation::animation_callback_params &, enum vostok::animation::fingers_to_weapon_corrector::hands_enum)` |
| 43.18 | `protected: enum vostok::animation::callback_return_type_enum __thiscall survarium::object_skeleton_visual::on_fingers_event(struct vostok::animation::animation_callback_params &, enum vostok::animation::fingers_to_weapon_corrector::hands_enum)` |
| 43.30 | `public: __thiscall survarium::lobby_character::lobby_character(class survarium::lobby_menu &, struct vostok::physics::world &, class vostok::math::float3const &, float)` |
| 43.36 | `private: virtual struct stlp_std::pair<class vostok::animation::mixing::expression, class vostok::animation::mixing::animation_lexeme> __thiscall survarium::player_logic_jump_state::selected_animations(class vostok::mutable_buffer &, struct survarium::weapon_animation_parameters const &) const` |
| 43.43 | `private: void __thiscall survarium::chat_handler::initialize_tabs(class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &, bool)` |
| 43.59 | `public: void __thiscall vostok::buffer_vector<struct survarium::particle_game_effect_presenter::effect_data>::assign<struct survarium::particle_game_effect_presenter::effect_data const *>(struct survarium::particle_game_effect_presenter::effect_data const *, struct survarium::particle_game_effect_presenter::effect_data const *const &)` |
| 44.00 | `public: virtual void __thiscall survarium::artefact_container_core::use_finalize(struct survarium::usable_object_user_data *)` |
| 44.02 | `private: virtual void __thiscall survarium::jump_logic_state_prepare::initialize(void)` |
| 44.28 | `public: virtual void __thiscall vostok::render::stage_ambient_lighting::execute(void)` |
| 44.44 | `public: void __thiscall survarium::players_checker::serialize(class vostok::network_core::buffer_writer const &) const` |
| 44.73 | `vostok::network::enqueue_impl` |
| 44.84 | `private: bool __thiscall survarium::weapon_user_animations_selector::is_trying_to_jump(void) const` |
| 45.00 | `public: __thiscall vostok::intrusive_ptr<class vostok::render::res_state, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>::~intrusive_ptr<class vostok::render::res_state, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>(void)` |
| 45.09 | `private: void __thiscall survarium::network_client::process_profiles_action(class vostok::network_core::buffer_reader &)` |
| 45.32 | `public: __thiscall vostok::render::event_query::event_query(void)` |
| 46.08 | `private: bool __thiscall survarium::breath_vibration_calculator::not_holding_breath(void) const` |
| 46.39 | `private: void __thiscall vostok::network::login_client_impl::on_sign_in_answer_received(class boost::function<void __cdecl (enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::login::server::messages_enum)> const &, class boost::system::error_code const &, unsigned int)` |
| 46.75 | `public: virtual bool __thiscall survarium::game_world::on_keyboard_action(struct vostok::input::world *, enum vostok::input::enum_keyboard, enum vostok::input::enum_keyboard_action)` |
| 47.00 | `protected: enum vostok::animation::callback_return_type_enum __thiscall survarium::object_skeleton_visual::on_hand_ik_event(struct vostok::animation::animation_callback_params &, enum vostok::animation::hand_to_weapon_ik_solver::hands_enum)` |
| 47.00 | `public: enum vostok::animation::callback_return_type_enum __thiscall survarium::portable_interactive_object::on_hand_ik_event(struct vostok::animation::animation_callback_params &, enum vostok::animation::hand_to_weapon_ik_solver::hands_enum)` |
| 47.06 | `private: void __thiscall vostok::network_core::udp_match_client::handle_receive(class boost::system::error_code const &, unsigned int)` |
| 47.44 | `public: void __thiscall survarium::game_world_ui::clear_player(void)` |
| 47.49 | `public: __thiscall survarium::dictionary_item::dictionary_item(struct survarium::dictionary_item const &)` |
| 47.78 | `public: virtual void __thiscall survarium::weapon_core_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 48.30 | `private: void __thiscall survarium::items_dictionary_cook::on_configs_loaded(class vostok::resources::queries_result &)` |
| 48.58 | `public: __thiscall survarium::player_shared_statistics::player_shared_statistics(void)` |
| 48.68 | `private: class btVector3 __thiscall character_step_down_sweep_test_callback::get_normal_via_ray_test(struct btCollisionWorld::LocalConvexResult &, class btVector3const &) const` |
| 48.76 | `public: virtual void __thiscall survarium::weapon_core_throw_grenade_pull_substate::initialize(void)` |
| 48.79 | `public: void __thiscall vostok::network_core::udp_match_client::set_connection_ports(unsigned char, unsigned int, unsigned short, unsigned short)` |
| 49.00 | `public: __thiscall vostok::buffer_vector<float>::buffer_vector<float>(void *, unsigned int, class vostok::buffer_vector<float> const &)` |
| 49.17 | `private: virtual void __thiscall survarium::match_client::set_on_disconnect(class boost::function<void __cdecl (enum vostok::network_core::disconnect_event_types_enum)> const &)` |
| 49.69 | `private: virtual void __thiscall vostok::engine::engine_world::on_crash(void)` |
| 49.70 | `private: void __thiscall survarium::network_client::process_player_entered_match(class vostok::network_core::buffer_reader &)` |
| 49.83 | `public: void __thiscall vostok::console_commands::console_command::on_invalid_syntax(char const *)` |
| 49.94 | `public: virtual void __thiscall vostok::render::effect_apply_decal::compile(class vostok::render::effect_compiler &, class vostok::configs::binary_config_value const &, struct vostok::render::surface_effect_parameters const &)` |
| 50.61 | `public: virtual void __thiscall survarium::network_client::on_idle(unsigned int)` |
| 50.80 | `public: void __thiscall survarium::inventory::setup_from_profile(struct survarium::player_profile &)` |
| 50.95 | `vostok::physics::get_wall_slide_vector` |
| 51.43 | `public: void __thiscall vostok::buffer_vector<struct survarium::sound_game_effect_presenter::effect_data>::assign<struct survarium::sound_game_effect_presenter::effect_data const *>(struct survarium::sound_game_effect_presenter::effect_data const *, struct survarium::sound_game_effect_presenter::effect_data const *const &)` |
| 51.64 | `public: virtual __thiscall vostok::render::res_effect::~res_effect(void)` |
| 51.65 | `public: bool __thiscall survarium::inventory::update_weight(void)` |
| 51.76 | `private: void __thiscall vostok::render::hw_hiz_occlusion_manager::copy_scene_depth(void)` |
| 52.36 | `public: void __thiscall vostok::render::renderer::render(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct vostok::render::base_scene_view, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct vostok::render::base_output_window, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::rectangle<class vostok::math::float2> const &, class boost::function<void __cdecl (bool)> const &, bool, struct vostok::ui::font const *)` |
| 52.38 | `public: void __thiscall vostok::physics::bt_character_controller::set_transform(class vostok::math::float4x4const &, unsigned int)` |
| 52.43 | `public: virtual void __thiscall vostok::render::stage_ambient_lighting::clear_surfaces(void)` |
| 52.53 | `private: float __thiscall survarium::weapon_core::computed_vertical_recoil_time(float, float, unsigned int, unsigned int, unsigned int, float)` |
| 52.70 | `public: void __thiscall survarium::base_player::assign_physics_transform(void)` |
| 53.18 | `private: virtual void __thiscall survarium::player_input_handler::on_after_processing(struct vostok::input::world *)` |
| 53.33 | `private: bool __thiscall vostok::render::stage_lights::has_models_for_shadow_pass(class vostok::render::light *, class vostok::buffer_vector<struct vostok::render::render_surface_instance *> const &)` |
| 53.33 | `public: class vostok::render::res_pass * __thiscall vostok::render::effect_manager::create_pass(class vostok::render::res_pass const &)` |
| 53.65 | `public: void __thiscall survarium::lobby_menu::switch_to_level_loading(unsigned char)` |
| 53.73 | `public: class vostok::network_core::udp_match_packet * __thiscall vostok::intrusive_list<class vostok::network_core::udp_match_packet, class vostok::network_core::udp_match_packet *, 60, class vostok::threading::single_threading_policy, class vostok::size_policy, class vostok::no_debug_policy>::remove_if<class vostok::network_core::move_to_list_predicate>(class vostok::network_core::move_to_list_predicate const &)` |
| 54.00 | `public: virtual void __thiscall vostok::detail::concrete_type_helper<struct survarium::booby_trap_set_cook_data>::copy(class vostok::mutable_buffer, class vostok::const_buffer)` |
| 54.05 | `public: void __thiscall vostok::render::res_render_output::resize(bool, unsigned int, unsigned int, bool)` |
| 54.12 | `public: void __thiscall vostok::network::match_client_impl::send_queued_packets(unsigned int)` |
| 54.15 | `private: void __thiscall vostok::render::res_render_output::update_targets(void)` |
| 54.96 | `private: void __thiscall vostok::render::stage_lights::render_to_hw_shadowmap(class vostok::render::light *, unsigned int, float, unsigned int, unsigned int, class vostok::math::float4x4const &, class vostok::math::float4x4const &, unsigned int, unsigned int)` |
| 54.96 | `public: __thiscall vostok::fixed_vector<class fastdelegate::FastDelegate<bool __cdecl (struct vostok::ui::window *, int, int)>, 16>::fixed_vector<class fastdelegate::FastDelegate<bool __cdecl (struct vostok::ui::window *, int, int)>, 16>(class vostok::fixed_vector<class fastdelegate::FastDelegate<bool __cdecl (struct vostok::ui::window *, int, int)>, 16> const &)` |
| 55.39 | `public: virtual void __thiscall survarium::object_volume_fog::insert(void)` |
| 55.41 | `public: float __thiscall survarium::base_player::look_time_factor_calculator(float, float, unsigned int, unsigned int, unsigned int, float)` |
| 55.42 | `public: void __thiscall vostok::animation::fingers_to_weapon_corrector::serialize(class vostok::network_core::buffer_writer const &, unsigned int) const` |
| 55.42 | `public: void __thiscall vostok::animation::hand_to_weapon_ik_solver::serialize(class vostok::network_core::buffer_writer const &, unsigned int) const` |
| 56.17 | `public: virtual void __thiscall vostok::resources::unknown_data_class_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 56.18 | `public: void __thiscall vostok::physics::bt_character_controller::set_air_control_vector(class vostok::math::float3const &)` |
| 56.34 | `public: __thiscall vostok::render::res_render_output::res_render_output(struct HWND__*, bool)` |
| 56.55 | `public: class vostok::buffer_vector<struct survarium::animations_registry::animations_tuple> & __thiscall vostok::buffer_vector<struct survarium::animations_registry::animations_tuple>::operator=(class vostok::buffer_vector<struct survarium::animations_registry::animations_tuple> const &)` |
| 56.83 | `public: virtual void __thiscall survarium::profile_skin_visual_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 56.84 | `private: virtual void __thiscall survarium::breath_state_holding::finalize(void)` |
| 56.85 | `private: void __thiscall survarium::network_client::process_local_player_input_discard(class vostok::network_core::buffer_reader &)` |
| 57.32 | `private: void __thiscall survarium::shared_statistics::on_event(struct survarium::player_shared_statistics &, enum survarium::match_stats_events_dict_enum, unsigned short)` |
| 57.73 | `public: virtual void __thiscall survarium::base_player::apply_new_input(unsigned int, struct survarium::player_input const &)` |
| 58.05 | `public: virtual void __thiscall survarium::network_client::unload(void)` |
| 58.21 | `public: __thiscall vostok::fixed_vector<class vostok::resources::resource_ptr<class survarium::game_match_rule_base, class vostok::resources::unmanaged_intrusive_base>, 4>::ctor<class vostok::resources::resource_ptr<class survarium::game_match_rule_base, class vostok::resources::unmanaged_intrusive_base> const *>(class vostok::resources::resource_ptr<class survarium::game_match_rule_base, class vostok::resources::unmanaged_intrusive_base> const *const &, class vostok::resources::resource_ptr<class survarium::game_match_rule_base, class vostok::resources::unmanaged_intrusive_base> const *const &)` |
| 58.42 | `private: void __thiscall vostok::render::effect_manager::on_effects_recompiled(class vostok::fixed_vector<struct vostok::render::effect_manager::effect_to_recompile_struct, 2048> *, class vostok::resources::queries_result &)` |
| 59.09 | `private: virtual void __thiscall survarium::match_client::connect(char const *, unsigned short, unsigned int, unsigned int, class boost::function<void __cdecl (enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::lobby::server::messages_enum)> const &)` |
| 59.23 | `protected: virtual void __thiscall survarium::weapon_core::serialize(class vostok::network_core::buffer_writer const &, class vostok::network_core::buffer_writer const *, unsigned int) const` |
| 59.29 | `public: void __thiscall survarium::lobby_menu::show_match_making(bool)` |
| 59.35 | `public: float __thiscall survarium::player_params_modifiers_container::apply_modifier(enum survarium::player_params_modifiers_enum, float, float) const` |
| 59.51 | `public: void __thiscall vostok::render::resource_manager::release(class vostok::render::shader_constant_buffer const *)` |
| 59.59 | `public: void __thiscall vostok::render::backend::reset(void)` |
| 59.66 | `private: void __thiscall survarium::inventory_cook::on_subresources_loaded(class vostok::resources::queries_result &, struct survarium::inventory_cooker_data *)` |
| 59.75 | `private: void __thiscall survarium::game_world_core::atomic_tick(unsigned int, unsigned int)` |
| 59.89 | `public: virtual void __thiscall survarium::weapon_core_base_state::serialize(class vostok::network_core::buffer_writer const &, class vostok::network_core::buffer_writer const *) const` |
| 60.00 | `private: virtual void __thiscall survarium::player_logic_dead_state::serialize(class vostok::network_core::buffer_writer const &, class vostok::network_core::buffer_writer const *) const` |
| 60.00 | `public: virtual void __thiscall survarium::victory_item_core_base_state::serialize(class vostok::network_core::buffer_writer const &, class vostok::network_core::buffer_writer const *) const` |
| 60.40 | `public: bool __thiscall survarium::items_dictionary::can_move_item_to_slot(unsigned int, unsigned int) const` |
| 60.44 | `vostok::physics::get_slope_slide_vector` |
| 61.00 | `public: void __thiscall vostok::render::xs_descriptor<struct vostok::render::vs_data>::reset(class vostok::render::res_xs_hw<struct vostok::render::vs_data> *)` |
| 61.09 | `void __cdecl vostok::render::register_texture_cook(void)` |
| 61.64 | `public: void __thiscall survarium::inventory_item_descr::deserialize(class vostok::network_core::buffer_reader &, enum survarium::slot_serialize_mode_enum)` |
| 61.79 | `public: __thiscall survarium::lobby_client::lobby_client(class survarium::game &)` |
| 61.80 | `public: void __thiscall survarium::breath_vibration_calculator::serialize(class vostok::network_core::buffer_writer const &, class vostok::network_core::buffer_writer const *, unsigned int) const` |
| 61.80 | `private: void __thiscall survarium::game_world_ui::update_quick_slot(class vostok::resources::resource_ptr<class survarium::inventory_item, class vostok::resources::unmanaged_intrusive_base> const &, enum survarium::profile_slot_enum)` |
| 61.84 | `private: float __thiscall survarium::weapon_core::computed_horizontal_recoil_time(float, float, unsigned int, unsigned int, unsigned int, float)` |
| 62.11 | `private: void __thiscall vostok::physics::bullet_character_controller::step_down(float, bool, class btVector3const &, class btVector3const &, class btVector3const &, class btVector3const &)` |
| 62.27 | `private: void __thiscall survarium::game::on_base_resources_created(class vostok::resources::queries_result &)` |
| 62.33 | `private: void __thiscall survarium::collision_sensor::notify_objects_inside(unsigned int, unsigned int)` |
| 62.44 | `public: virtual __thiscall survarium::game::~game(void)` |
| 62.76 | `public: void __thiscall survarium::lobby_menu::player_parameters_ready(struct survarium::lobby_player_profile const &)` |
| 62.80 | `private: virtual void __thiscall survarium::player_logic_crouch_state::initialize(void)` |
| 62.81 | `public: __thiscall vostok::animation::fingers_to_weapon_corrector::fingers_to_weapon_corrector(void)` |
| 62.98 | `public: void __thiscall survarium::shared_statistics::on_player_killed(unsigned int, unsigned char, unsigned char, bool, bool, unsigned int)` |
| 63.18 | `private: void __thiscall vostok::render::res_render_output::update_depth_stencil_buffer(void)` |
| 63.33 | `private: void __thiscall vostok::network_core::http_client::handle_resolve(class boost::system::error_code const &, class boost::asio::ip::basic_resolver_iterator<class boost::asio::ip::tcp>)` |
| 63.70 | `public: void __thiscall survarium::dispersion_calculator::serialize(class vostok::network_core::buffer_writer const &, unsigned int) const` |
| 63.88 | `public: void __thiscall vostok::network_core::udp_match_connection::disconnect(void)` |
| 63.91 | `public: __thiscall vostok::render::ui::draw_vertices_command::draw_vertices_command(class vostok::render::engine::world &, class vostok::resources::resource_ptr<struct vostok::render::base_scene_view, class vostok::resources::unmanaged_intrusive_base> const &, struct vostok::render::ui::vertex const *, struct vostok::render::ui::vertex const *, class vostok::memory::base_allocator &, unsigned int, unsigned int)` |
| 64.00 | `public: virtual void __thiscall survarium::timelimit_rule_core::on_player_entered_match(class survarium::base_player &, unsigned int)` |
| 65.21 | `public: void __thiscall vostok::render::effect_manager::delete_pass(class vostok::render::res_pass const *)` |
| 65.30 | `public: static void __cdecl vostok::animation::mixing::n_ary_tree::update_animation_time(struct vostok::animation::mixing::animation_state &)` |
| 65.33 | `private: virtual struct stlp_std::pair<class vostok::animation::mixing::expression, class vostok::animation::mixing::animation_lexeme> __thiscall survarium::player_logic_sprint_state::selected_animations(class vostok::mutable_buffer &, struct survarium::weapon_animation_parameters const &) const` |
| 65.41 | `private: struct stlp_std::pair<class vostok::animation::mixing::expression, class vostok::animation::mixing::animation_lexeme> __thiscall survarium::short_jump_landing_state::get_main_expression(class vostok::mutable_buffer &)` |
| 65.66 | `private: void __thiscall survarium::lobby_client::on_connected(void)` |
| 66.20 | `public: void __thiscall vostok::render::resource_manager::release(class vostok::render::res_texture_list const *)` |
| 66.20 | `public: void __thiscall vostok::render::resource_manager::release(class vostok::render::shader_constant_table const *)` |
| 66.20 | `private: void __thiscall survarium::network_client::process_set_time_request(class vostok::network_core::buffer_reader &)` |
| 66.33 | `public: virtual void __thiscall survarium::grenade_set_core::set_inventory(class survarium::inventory *, enum survarium::profile_slot_enum)` |
| 66.36 | `public: virtual void __thiscall survarium::timelimit_rule_core::tick(unsigned int, unsigned int)` |
| 66.44 | `private: virtual void __thiscall survarium::victory_item_core::load(class vostok::configs::binary_config_value const &)` |
| 66.44 | `public: void __thiscall vostok::render::resource_manager::release(class vostok::render::res_xs<struct vostok::render::gs_data> const *)` |
| 66.44 | `public: void __thiscall vostok::render::resource_manager::release(class vostok::render::res_xs<struct vostok::render::vs_data> const *)` |
| 66.58 | `public: virtual void __thiscall survarium::timelimit_rule_core::on_player_left_match(class survarium::base_player &, unsigned int)` |
| 66.82 | `private: void __thiscall survarium::network_client::process_player_input_change(class vostok::network_core::buffer_reader &)` |
| 66.87 | `private: void __thiscall survarium::network_client::process_player_left_match(class vostok::network_core::buffer_reader &)` |
| 66.88 | `public: void __thiscall survarium::game_world_ui::update_minimap_players(void)` |
| 66.91 | `protected: static struct survarium::artefact_spring_core::config __cdecl survarium::artefact_spring_core::load_config(class vostok::configs::binary_config_value const &)` |
| 66.92 | `public: __thiscall vostok::render::res_pass::~res_pass(void)` |
| 66.95 | `public: __thiscall survarium::lobby_client::~lobby_client(void)` |
| 67.07 | `public: __thiscall survarium::player_profile::player_profile(void)` |
| 67.22 | `private: void __thiscall survarium::base_player::apply_rotation(class vostok::math::float2const &)` |
| 67.22 | `void __cdecl vostok::render::register_samplers(void)` |
| 67.31 | `public: void __thiscall vostok::render::resource_manager::release(class vostok::render::res_geometry const *)` |
| 67.31 | `public: void __thiscall vostok::render::resource_manager::release(class vostok::render::res_input_layout const *)` |
| 67.31 | `public: void __thiscall vostok::render::resource_manager::release(class vostok::render::res_xs<struct vostok::render::ps_data> const *)` |
| 67.33 | `public: void * __thiscall vostok::render::shader_buffer::lock_write_discard(void)` |
| 67.41 | `public: void __thiscall vostok::render::resource_manager::release(class vostok::render::res_sampler_list const *)` |
| 67.48 | `public: void __thiscall vostok::render::resource_manager::release(class vostok::render::res_declaration const *)` |
| 67.68 | `protected: void __thiscall survarium::lobby_menu::on_render_scenes_ready(class vostok::resources::queries_result &)` |
| 67.76 | `public: void __thiscall survarium::shared_statistics::clear(void)` |
| 67.84 | `public: virtual void __thiscall survarium::particle_game_effect_presenter::present(class survarium::base_player *)` |
| 67.96 | `private: void __thiscall survarium::network_client::on_match_ready(class vostok::resources::queries_result &)` |
| 67.98 | `private: void __thiscall vostok::sound::sound_collection_cook::sub_sounds_loaded(class vostok::resources::queries_result &, class vostok::sound::sound_collection *, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>)` |
| 68.12 | `public: __thiscall vostok::physics::bullet_character_controller::bullet_character_controller(class vostok::math::float2const &, class vostok::math::float2const &, short, short, class vostok::memory::base_allocator &)` |
| 68.24 | `private: virtual void __thiscall survarium::player_logic_jump_state::finalize(void)` |
| 68.27 | `public: virtual class survarium::artefact_base & __thiscall survarium::artefact_cook::construct_derived_resource(void *, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::game_effect_emitter, class vostok::resources::unmanaged_intrusive_base> const &, void *const) const` |
| 68.30 | `private: struct stlp_std::pair<class vostok::animation::mixing::expression, class vostok::animation::mixing::animation_lexeme> __thiscall survarium::short_jump_start_state::get_main_expression(class vostok::mutable_buffer &, enum vostok::animation::body_part_masks_enum)` |
| 68.43 | `public: void __thiscall survarium::usable_object::serialize_usable_object(class vostok::network_core::buffer_writer const &, unsigned int) const` |
| 68.65 | `private: void __thiscall vostok::render::bake_decal_cook::on_textures_loaded(class vostok::resources::queries_result &, struct vostok::render::decal_texture_slot *, struct vostok::render::bake_decal_cook_parameters *, struct vostok::render::render_surface_instance *)` |
| 68.68 | `public: virtual void __thiscall vostok::render::effect_post_process_terrain_debug_materials::compile(class vostok::render::effect_compiler &, class vostok::configs::binary_config_value const &, struct vostok::render::surface_effect_parameters const &)` |
| 68.80 | `public: void __thiscall vostok::render::resource_manager::release(class vostok::render::res_signature const *)` |
| 68.84 | `private: void __thiscall survarium::game_world_ui::update_current_object(void)` |
| 68.97 | `private: bool __thiscall vostok::render::renderer::is_effects_ready(void) const` |
| 68.98 | `public: void __thiscall vostok::physics::bullet_character_controller::serialize(class vostok::network_core::buffer_writer const &, unsigned int) const` |
| 70.00 | `private: void __thiscall survarium::game_world_ui::update_current_player(void)` |
| 70.05 | `public: void __thiscall survarium::bullet::serialize(class vostok::network_core::buffer_writer const &, unsigned int) const` |
| 70.07 | `private: void __thiscall survarium::player_stamina::spend(float)` |
| 70.10 | `public: void __thiscall vostok::buffer_vector<class vostok::intrusive_ptr<class vostok::render::shader_constant_buffer, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy> >::assign<class vostok::intrusive_ptr<class vostok::render::shader_constant_buffer, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy> const *>(class vostok::intrusive_ptr<class vostok::render::shader_constant_buffer, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy> const *, class vostok::intrusive_ptr<class vostok::render::shader_constant_buffer, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy> const *const &)` |
| 70.24 | `private: virtual void __thiscall survarium::booby_trap_core::serialize(class vostok::network_core::buffer_writer const &, unsigned int) const` |
| 70.72 | `private: void __thiscall vostok::network::login_client_impl::on_connected(unsigned int, class boost::function<void __cdecl (enum vostok::connection_error_types_enum)> const &, class boost::asio::ip::basic_resolver_iterator<class boost::asio::ip::tcp>, class boost::system::error_code const &, class boost::asio::ip::basic_resolver_iterator<class boost::asio::ip::tcp>)` |
| 70.94 | `public: virtual void __thiscall survarium::lobby_menu::clear_resources(void)` |
| 71.06 | `public: __thiscall vostok::network_core::udp_match_connection::~udp_match_connection(void)` |
| 71.13 | `public: __thiscall vostok::render::shader_constant_table::shader_constant_table(class vostok::render::shader_constant_table const &)` |
| 71.20 | `public: virtual void __thiscall vostok::network::receive_udp_response::execute(void)` |
| 71.22 | `public: __thiscall vostok::render::singletons_on_preinitialize::singletons_on_preinitialize(class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &, unsigned __int64, bool)` |
| 71.52 | `public: virtual void __thiscall vostok::render::effect_rain::compile(class vostok::render::effect_compiler &, class vostok::configs::binary_config_value const &, struct vostok::render::surface_effect_parameters const &)` |
| 71.87 | `public: bool __thiscall survarium::base_player::can_sprint(void) const` |
| 72.00 | `public: void __thiscall survarium::player_stamina::serialize(class vostok::network_core::buffer_writer const &, unsigned int) const` |
| 72.15 | `private: void __thiscall survarium::network_client::on_lobby_packet_received(class vostok::network_core::buffer_reader &)` |
| 72.31 | `public: __thiscall vostok::network_core::async_connector::~async_connector(void)` |
| 72.31 | `public: unsigned int __thiscall vostok::resources::query_result_for_cook::get_raw_file_size(void) const` |
| 72.34 | `public: void __thiscall vostok::render::resource_manager::release(class vostok::render::res_render_output const *)` |
| 72.76 | `public: void __thiscall vostok::buffer_vector<class vostok::intrusive_ptr<class vostok::render::res_shader_technique, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy> >::push_back(class vostok::intrusive_ptr<class vostok::render::res_shader_technique, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy> const &)` |
| 72.80 | `public: void __thiscall survarium::player_input::serialize(class vostok::network_core::buffer_writer const &) const` |
| 73.16 | `private: enum survarium::collision_result __thiscall survarium::bullet::check_collision(class vostok::math::float3, float &, float &, float &)` |
| 73.31 | `public: void __thiscall survarium::lobby_menu::fill_items_dictionary(void)` |
| 73.65 | `private: virtual class vostok::network_core::udp_match_packet * __thiscall vostok::journaling::match_client::new_packet(enum vostok::match::client::messages_enum)` |
| 73.66 | `private: bool __thiscall survarium::messaging_client::read_friend_status(class vostok::network_core::buffer_reader &)` |
| 73.77 | `public: void __thiscall survarium::weapon_recoil_calculator::serialize(class vostok::network_core::buffer_writer const &, unsigned int) const` |
| 73.78 | `public: virtual void __thiscall survarium::lobby_menu::scaleform_call(struct survarium::flash_function_handler_params &)` |
| 73.90 | `public: virtual void __thiscall survarium::base_player::serialize(class vostok::network_core::buffer_writer const &, class vostok::network_core::buffer_writer const *, unsigned char (&)[32768], class vostok::intrusive_ptr<class vostok::animation::mixing::n_ary_tree_intrusive_base, class vostok::animation::mixing::n_ary_tree_intrusive_base, class vostok::threading::single_threading_policy> &, unsigned int)` |
| 73.95 | `private: void __thiscall survarium::game_world_ui::update_minimap_objects(void)` |
| 74.04 | `convert_channels_ids` |
| 74.12 | `public: __thiscall vostok::render::shader_buffer::shader_buffer(unsigned int, unsigned int, enum DXGI_FORMAT)` |
| 74.13 | `private: __thiscall vostok::render::game::renderer::renderer(class vostok::render::world &, class vostok::render::engine::world &)` |
| 74.29 | `private: virtual void __thiscall vostok::animation::mixing::n_ary_tree_serializer::visit(class vostok::animation::instant_interpolator const &)` |
| 74.30 | `public: void __thiscall survarium::victory_item_event_manager::serialize(class vostok::network_core::buffer_writer const &, unsigned int) const` |
| 74.38 | `public: void __thiscall vostok::animation::fingers_to_weapon_corrector::deserialize(class vostok::network_core::buffer_reader &, unsigned int)` |
| 74.38 | `public: void __thiscall vostok::animation::hand_to_weapon_ik_solver::deserialize(class vostok::network_core::buffer_reader &, unsigned int)` |
| 74.50 | `class vostok::logging::log_file * __cdecl vostok::logging::new_log_file(class vostok::logging::base_allocator &, class vostok::logging::base_fs_device &, char const *, enum vostok::logging::log_file_usage_enum)` |
| 74.77 | `public: void __thiscall survarium::bullet_manager::serialize(class vostok::network_core::buffer_writer const &, unsigned int) const` |
| 74.82 | `private: void __thiscall vostok::physics::bullet_character_controller::player_step(float)` |
| 74.83 | `public: void __thiscall vostok::render::effect_compiler::end_technique(void)` |
| 74.88 | `public: struct vostok::render::vs_data & __thiscall vostok::render::vs_data::operator=(struct vostok::render::vs_data const &)` |
| 74.88 | `private: void __thiscall survarium::network_client::query_players(void)` |
| 74.90 | `public: virtual void __thiscall survarium::jump_logic_state_landing::serialize(class vostok::network_core::buffer_writer const &, class vostok::network_core::buffer_writer const *) const` |
| 75.07 | `public: virtual void __thiscall survarium::portable_interactive_object::initialize(void)` |
| 75.13 | `protected: void __thiscall survarium::base_player::set_physics_controller_walk_vector(unsigned int)` |
| 75.32 | `public: virtual void __thiscall vostok::render::texture_cook::create_resource(class vostok::resources::query_result_for_cook &, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>, unsigned int, unsigned int &)` |
| 75.34 | `private: class vostok::math::float4x4 __thiscall vostok::animation::legs_ik_solver::get_foot_fixed_transform(struct vostok::animation::legs_ik_solver::leg_params const &, class vostok::math::float4x4const &, class vostok::math::float4x4const *, float &) const` |
| 75.38 | `private: void __thiscall vostok::network_core::udp_match_connection::call_predicate_and_destroy_packet<class vostok::network_core::process_packet_predicate>(class vostok::network_core::udp_match_packet *&, class vostok::network_core::process_packet_predicate const &)` |
| 75.43 | `public: void __thiscall survarium::game_world_ui::process_statistic_event(class survarium::game_statistic_event_history_item *, bool)` |
| 75.47 | `public: virtual void __thiscall survarium::jump_logic_base_state::serialize(class vostok::network_core::buffer_writer const &, class vostok::network_core::buffer_writer const *) const` |
| 75.47 | `public: virtual void __thiscall survarium::weapon_core_throw_grenade_base_substate::serialize(class vostok::network_core::buffer_writer const &, class vostok::network_core::buffer_writer const *) const` |
| 75.53 | `private: void __thiscall vostok::network_core::http_client::handle_connect(class boost::system::error_code const &, class boost::asio::ip::basic_resolver_iterator<class boost::asio::ip::tcp>)` |
| 75.60 | `private: virtual class vostok::fixed_string<512> __thiscall vostok::resources::managed_resource::log_string(void) const` |
| 75.65 | `private: virtual bool __thiscall vostok::render::stage_postprocess::is_effects_ready(void) const` |
| 75.80 | `public: __thiscall survarium::login_menu::login_menu(class survarium::game &)` |
| 75.88 | `public: void __thiscall vostok::threading::reader_writer_lock::unlock_write(void) const` |
| 75.93 | `protected: virtual void __thiscall survarium::double_barreled_weapon_core_fire_state::serialize(class vostok::network_core::buffer_writer const &, class vostok::network_core::buffer_writer const *) const` |
| 75.93 | `protected: virtual void __thiscall survarium::pistol_weapon_core_fire_state::serialize(class vostok::network_core::buffer_writer const &, class vostok::network_core::buffer_writer const *) const` |
| 75.93 | `public: virtual void __thiscall survarium::short_jump_start_state::serialize(class vostok::network_core::buffer_writer const &, class vostok::network_core::buffer_writer const *) const` |
| 76.00 | `protected: virtual void __thiscall survarium::victory_item_core_animation_end_aware_state::serialize(class vostok::network_core::buffer_writer const &, class vostok::network_core::buffer_writer const *) const` |
| 76.00 | `protected: virtual void __thiscall survarium::weapon_core_animation_end_aware_state::serialize(class vostok::network_core::buffer_writer const &, class vostok::network_core::buffer_writer const *) const` |
| 76.00 | `protected: virtual void __thiscall survarium::weapon_core_fire_state_base::serialize(class vostok::network_core::buffer_writer const &, class vostok::network_core::buffer_writer const *) const` |
| 76.01 | `private: void __thiscall vostok::network_core::udp_match_connection::handle_send(class vostok::network_core::udp_match_packet &, class boost::system::error_code const &, unsigned int)` |
| 76.09 | `public: void __thiscall survarium::recoil_calculator::serialize(class vostok::network_core::buffer_writer const &, unsigned int) const` |
| 76.12 | `public: void __thiscall survarium::intermediate_shared_statistics::serialize(class vostok::network_core::buffer_writer const &, unsigned int) const` |
| 76.33 | `public: void * __thiscall vostok::memory::stack_allocator::realloc_impl(void *, unsigned int, char const *const, char const *const, char const *const, unsigned int)` |
| 76.44 | `public: struct vostok::render::gs_data & __thiscall vostok::render::gs_data::operator=(struct vostok::render::gs_data const &)` |
| 76.52 | `private: virtual struct vostok::network_core::udp_match_message_type_info __thiscall survarium::network_packets_orderer<enum vostok::match::client::messages_enum, enum vostok::match::server::messages_enum>::get_sending_message_info(unsigned char)` |
| 76.61 | `private: virtual void __thiscall vostok::render::point_light_effect<0, 0>::compile(class vostok::render::effect_compiler &, class vostok::configs::binary_config_value const &, struct vostok::render::surface_effect_parameters const &)` |
| 76.61 | `private: virtual void __thiscall vostok::render::point_light_effect<0, 1>::compile(class vostok::render::effect_compiler &, class vostok::configs::binary_config_value const &, struct vostok::render::surface_effect_parameters const &)` |
| 76.62 | `public: void __thiscall vostok::render::renderer_context_targets::resize(class vostok::math::uint2, bool)` |
| 76.77 | `public: __thiscall survarium::object_skeleton_visual::object_skeleton_visual(class survarium::base_game_scene &, class survarium::simple_game_project &)` |
| 76.80 | `public: void __thiscall survarium::hit_animations_selector::serialize(class vostok::network_core::buffer_writer const &, unsigned int) const` |
| 76.80 | `private: bool __thiscall vostok::threading::reader_writer_lock::lock_write_impl(bool) const` |
| 76.90 | `public: __thiscall survarium::fwd_animation_interval_end_time_calculator::fwd_animation_interval_end_time_calculator(class survarium::weapon_user_animations_container const &, void const *)` |
| 76.90 | `public: class vostok::render::shader_constant_table & __thiscall vostok::render::shader_constant_table::operator=(class vostok::render::shader_constant_table const &)` |
| 76.91 | `private: void __thiscall vostok::network::match_client::create_responses_packets_allocator(void)` |
- _...and 2166 more_

### Added (605)

- `?set_size@render_output_window@render@vostok@@QAEXII_N_N11@Z`
- `?set_size@res_render_output@render@vostok@@QAEXII_N_N11@Z`
- ``vostok::configs::create_binary_config_buffer_impl'::`3'::remap_disposer::operator()`
- ``vostok::configs::sort'::`5'::predicate::compare`
- ``vostok::render::renderer::draw_top_dip_models_list'::`4'::sort_predicate::operator()`
- `add_bit_cell`
- `add_cells`
- `bool __cdecl survarium::disable_game_statistics_gathering(void)`
- `bool __cdecl vostok::render::read_file_chunk(class vostok::fs_new::native_path_string const &, unsigned char *, unsigned __int64, unsigned __int64, unsigned __int64, class vostok::fs_new::synchronous_device_interface const &)`
- `char * __cdecl vostok::strings::copy<256>(char (&)[256], char const *)`
- `char const * __cdecl survarium::message_id_to_string(unsigned char)`
- `class btQuaternion __cdecl get_shape_rotation(struct btCollisionWorld::LocalConvexResult &)`
- `class btVector3 __cdecl vostok::physics::perpindicularComponent(class btVector3const &, class btVector3const &)`
- `class vostok::animation::mixing::addition_lexeme & __cdecl vostok::animation::mixing::operator+<class vostok::animation::mixing::addition_lexeme, class vostok::animation::mixing::animation_lexeme>(class vostok::animation::mixing::addition_lexeme &, class vostok::animation::mixing::animation_lexeme &)`
- `class vostok::network_core::custom_alloc_handler<class boost::_bi::bind_t<void, class boost::_mfi::mf3<void, class vostok::network_core::udp_match_client, class boost::system::error_code const &, unsigned int, class boost::function<void __cdecl (class boost::system::error_code const &, unsigned int)> const &>, class boost::_bi::list4<class boost::_bi::value<class vostok::network_core::udp_match_client *>, struct boost::arg<1>, struct boost::arg<2>, class boost::_bi::value<class boost::function<void __cdecl (class boost::system::error_code const &, unsigned int)> > > >, class vostok::network_core::handler_allocator<1024, 96, 1> > __cdecl vostok::network_core::make_custom_alloc_handler<class boost::_bi::bind_t<void, class boost::_mfi::mf3<void, class vostok::network_core::udp_match_client, class boost::system::error_code const &, unsigned int, class boost::function<void __cdecl (class boost::system::error_code const &, unsigned int)> const &>, class boost::_bi::list4<class boost::_bi::value<class vostok::network_core::udp_match_client *>, struct boost::arg<1>, struct boost::arg<2>, class boost::_bi::value<class boost::function<void __cdecl (class boost::system::error_code const &, unsigned int)> > > >, class vostok::network_core::handler_allocator<1024, 96, 1> >(class vostok::network_core::handler_allocator<1024, 96, 1> &, class boost::_bi::bind_t<void, class boost::_mfi::mf3<void, class vostok::network_core::udp_match_client, class boost::system::error_code const &, unsigned int, class boost::function<void __cdecl (class boost::system::error_code const &, unsigned int)> const &>, class boost::_bi::list4<class boost::_bi::value<class vostok::network_core::udp_match_client *>, struct boost::arg<1>, struct boost::arg<2>, class boost::_bi::value<class boost::function<void __cdecl (class boost::system::error_code const &, unsigned int)> > > >)`
- `class vostok::network_core::udp_match_packet * __cdecl vostok::network_core::new_udp_match_packet(class vostok::memory::single_size_buffer_allocator<684, class vostok::threading::multi_threading_policy> &)`
- `class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> __cdecl vostok::configs::create_binary_config(class vostok::mutable_buffer const &, class vostok::memory::base_allocator &)`
- `class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> __cdecl vostok::configs::modify_binary_config(class vostok::configs::binary_config_value const &, class boost::intrusive::set<struct vostok::configs::modifier, struct boost::intrusive::member_hook<struct vostok::configs::modifier, class boost::intrusive::set_member_hook<struct boost::intrusive::none, struct boost::intrusive::none, struct boost::intrusive::none, struct boost::intrusive::none>, 32>, struct boost::intrusive::compare<struct vostok::configs::modifier::comparer>, struct boost::intrusive::none, struct boost::intrusive::none> const &, class vostok::memory::base_allocator &)`
- `enum survarium::factions_enum __cdecl survarium::item_faction(class survarium::items_dictionary const &, struct survarium::inventory_item_descr const &)`
- `float __cdecl survarium::apply_modifier(enum survarium::player_params_modifiers_enum, float, struct survarium::player_profile const &, class survarium::items_dictionary const &)`
- `float __cdecl survarium::get_modifier_value(enum survarium::player_params_modifiers_enum, struct survarium::inventory_item_descr const &, class survarium::items_dictionary const &)`
- `float __cdecl survarium::item_weight(struct survarium::inventory_item_descr const &, class survarium::items_dictionary const &)`
- `float __cdecl survarium::shotgun_reload_end_timescale_calculator(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, struct survarium::weapon_state_creation_params const &)`
- `float __cdecl survarium::shotgun_reload_start_timescale_calculator(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, struct survarium::weapon_state_creation_params const &)`
- `int __cdecl sprintf_s<256>(char (&)[256], char const *, ...)`
- `int __cdecl sprintf_s<32>(char (&)[32], char const *, ...)`
- `message_length`
- `messages<vostok::network_core::udp_match_messages_stats_template<vostok::network_core::udp_match_received_message_stats> >`
- `messages<vostok::network_core::udp_match_messages_stats_template<vostok::network_core::udp_match_sent_message_stats> >`
- `private: __thiscall survarium::armor::armor(class vostok::configs::binary_config_value const &)`
- `private: __thiscall survarium::booby_trap_set::booby_trap_set(class vostok::configs::binary_config_value const &, unsigned char, class survarium::base_game_scene &, struct vostok::physics::world &, class vostok::resources::resource_ptr<class survarium::game_material_manager, class vostok::resources::unmanaged_intrusive_base> const &)`
- `private: __thiscall survarium::match_time_vi_spawn_rule::match_time_vi_spawn_rule(unsigned int)`
- `private: __thiscall survarium::medkit::medkit(class vostok::configs::binary_config_value const &)`
- `private: __thiscall survarium::oxygen_tank::oxygen_tank(class vostok::configs::binary_config_value const &)`
- `private: __thiscall vostok::resources::pinned_ptr_mutable<class vostok::animation::cubic_spline_skeleton_animation>::pinned_ptr_mutable<class vostok::animation::cubic_spline_skeleton_animation>(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>)`
- `private: bool __thiscall vostok::physics::bullet_character_controller::can_skeep_player_step(void) const`
- `private: bool __thiscall vostok::physics::bullet_character_controller::impassable_slope_down_slide(class btVector3const &, class btVector3const &, class btVector3const &, float, class btVector3&)`
- `private: bool __thiscall vostok::physics::bullet_character_controller::need_slide_on_supporting_surface(void) const`
- `private: bool __thiscall vostok::physics::bullet_character_controller::on_ground(float) const`
- `private: bool __thiscall vostok::physics::bullet_character_controller::on_steep_slope(float) const`
- `private: bool __thiscall vostok::physics::bullet_character_controller::side_slide_on_low_ceiling(class btVector3const &, class btVector3const &, class btVector3const &, float, float, class btVector3const &, class btVector3&)`
- `private: bool __thiscall vostok::physics::bullet_character_controller::side_slide_on_slope(class btVector3const &, class btVector3const &, class btVector3const &, float, float, class btVector3&)`
- `private: bool __thiscall vostok::physics::bullet_character_controller::slide_in_impassable_case_impl(class btVector3const &, class btVector3const &, class btVector3const &, float, float, class btVector3&)`
- `private: bool __thiscall vostok::physics::bullet_character_controller::step_down_sweep_test_impl(float, class btVector3const &, float, class btVector3const &, class btVector3&, class btVector3&)`
- `private: bool __thiscall vostok::render::statistics::is_visible_group(struct vostok::render::statistics_group *) const`
- `private: class btVector3 __thiscall character_step_down_sweep_test_callback::get_normal_for_impassable_slope(class btVector3const &) const`
- `private: class btVector3 __thiscall character_step_down_sweep_test_callback::get_normal_for_terminal_passable_slope(class btVector3const &) const`
- `private: class survarium::weapon * __thiscall survarium::weapon_cook::allocate_weapon(class vostok::configs::binary_config_value const &, class survarium::base_game_scene &, unsigned int, unsigned char, unsigned char)`
- `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::jump_logic_state_landing::get_look_lexeme(class vostok::mutable_buffer &, class fastdelegate::FastDelegate<float __cdecl (float, float, unsigned int, unsigned int, unsigned int, float)> const &, float, class vostok::animation::mixing::animation_lexeme &) const`
- `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::jump_logic_state_prepare::get_look_lexeme(class vostok::mutable_buffer &, class fastdelegate::FastDelegate<float __cdecl (float, float, unsigned int, unsigned int, unsigned int, float)> const &, float, class vostok::animation::mixing::animation_lexeme &)`
- `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::jump_logic_state_start::get_look_lexeme(class vostok::mutable_buffer &, class fastdelegate::FastDelegate<float __cdecl (float, float, unsigned int, unsigned int, unsigned int, float)> const &, float, class vostok::animation::mixing::animation_lexeme &)`
- `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::player_logic_sprint_state::get_hands_idle_lexeme(class vostok::mutable_buffer &, class vostok::animation::mixing::animation_lexeme &) const`
- `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::short_jump_landing_state::get_look_lexeme(class vostok::mutable_buffer &, class fastdelegate::FastDelegate<float __cdecl (float, float, unsigned int, unsigned int, unsigned int, float)> const &, float, class vostok::animation::mixing::animation_lexeme &)`
- `private: class vostok::network_core::udp_match_packet * __thiscall vostok::network::match_client::new_packet_impl(unsigned char)`
- `private: float __thiscall vostok::physics::bullet_character_controller::update_slide_velocity(class btVector3const &, class btVector3const &)`
- `private: struct stlp_std::pair<class vostok::math::float4x4, class vostok::math::float3> __thiscall vostok::animation::bone_matrices_computer::computed_local_bone_matrix(class vostok::animation::skeleton_bone const &, unsigned int, bool) const`
- `private: struct vostok::animation::bone_transform __thiscall vostok::animation::bone_matrices_computer::computed_local_bone_transform(class vostok::animation::skeleton_bone const &, unsigned int, unsigned int, bool) const`
- `private: unsigned int __thiscall survarium::lobby_menu::get_next_number_from_message(class vostok::fixed_string<256> &)`
- `private: unsigned int __thiscall survarium::swear_filter_cook::count_buffer_size(class vostok::configs::binary_config_value &, wchar_t *)`
- `private: virtual bool __thiscall survarium::short_jump_start_state::is_ready_for_transition(void) const`
- `private: virtual class survarium::booby_trap_set_core * __thiscall survarium::booby_trap_set_cook::new_derived_resource(class vostok::configs::binary_config_value const &, unsigned char, struct vostok::physics::world &, class vostok::resources::resource_ptr<class survarium::game_material_manager, class vostok::resources::unmanaged_intrusive_base> const &, void *const)`
- `private: virtual class survarium::booby_trap_set_core * __thiscall survarium::booby_trap_set_core_cook::new_derived_resource(class vostok::configs::binary_config_value const &, unsigned char, struct vostok::physics::world &, class vostok::resources::resource_ptr<class survarium::game_material_manager, class vostok::resources::unmanaged_intrusive_base> const &, void *const)`
- `private: virtual class survarium::gather_victory_items_rule * __thiscall survarium::gather_victory_items_rule_cook::create_resource(unsigned int)`
- `private: virtual class survarium::grenade_set_core * __thiscall survarium::grenade_set_core_cook::new_derived_resource(void *const, class vostok::configs::binary_config_value const &, unsigned char)`
- `private: virtual class survarium::match_time_vi_spawn_rule * __thiscall survarium::match_time_vi_spawn_rule_cook::create_resource(unsigned int)`
- `private: virtual class vostok::network_core::udp_match_stats & __thiscall survarium::match_client::stats(void) const`
- `private: virtual float __thiscall survarium::weapon_core::look_pitch(void) const`
- `private: virtual struct stlp_std::pair<class vostok::animation::mixing::expression, class vostok::animation::mixing::animation_lexeme> __thiscall survarium::jump_logic_state_landing::selected_animations(class vostok::mutable_buffer &, class fastdelegate::FastDelegate<float __cdecl (float, float, unsigned int, unsigned int, unsigned int, float)> const &, float, struct survarium::weapon_animation_parameters const &)`
- `private: virtual struct stlp_std::pair<class vostok::animation::mixing::expression, class vostok::animation::mixing::animation_lexeme> __thiscall survarium::jump_logic_state_prepare::selected_animations(class vostok::mutable_buffer &, class fastdelegate::FastDelegate<float __cdecl (float, float, unsigned int, unsigned int, unsigned int, float)> const &, float, struct survarium::weapon_animation_parameters const &)`
- `private: virtual struct stlp_std::pair<class vostok::animation::mixing::expression, class vostok::animation::mixing::animation_lexeme> __thiscall survarium::jump_logic_state_start::selected_animations(class vostok::mutable_buffer &, class fastdelegate::FastDelegate<float __cdecl (float, float, unsigned int, unsigned int, unsigned int, float)> const &, float, struct survarium::weapon_animation_parameters const &)`
- `private: virtual struct stlp_std::pair<class vostok::animation::mixing::expression, class vostok::animation::mixing::animation_lexeme> __thiscall survarium::short_jump_landing_state::selected_animations(class vostok::mutable_buffer &, class fastdelegate::FastDelegate<float __cdecl (float, float, unsigned int, unsigned int, unsigned int, float)> const &, float, struct survarium::weapon_animation_parameters const &)`
- `private: virtual struct stlp_std::pair<class vostok::animation::mixing::expression, class vostok::animation::mixing::animation_lexeme> __thiscall survarium::short_jump_start_state::selected_animations(class vostok::mutable_buffer &, class fastdelegate::FastDelegate<float __cdecl (float, float, unsigned int, unsigned int, unsigned int, float)> const &, float, struct survarium::weapon_animation_parameters const &)`
- `private: virtual unsigned int __thiscall survarium::gather_victory_items_rule_cook::get_derived_resource_size(void)`
- `private: virtual unsigned int __thiscall survarium::match_time_vi_spawn_rule_cook::get_derived_resource_size(void)`
- `private: virtual void __thiscall survarium::armor::on_holder_assigned(void)`
- `private: virtual void __thiscall survarium::booby_trap_core::fixed_tick(unsigned int, unsigned int)`
- `private: virtual void __thiscall survarium::booby_trap_core::hit(unsigned int, struct survarium::hit_initiator const *const, class vostok::collision::bone_collision_data const &, enum survarium::hit_type_enum, float, float, class survarium::bullet *const, class survarium::inventory_item const *const)`
- `private: virtual void __thiscall survarium::booby_trap_core::hit(unsigned int, struct survarium::hit_initiator const *const, unsigned int, enum survarium::hit_type_enum, float, float, class survarium::bullet *const, class vostok::math::float3const &, enum survarium::triangle_orientation, class survarium::inventory_item const *const)`
- `private: virtual void __thiscall survarium::booby_trap_set_core_cook::translate_query(class vostok::resources::query_result_for_cook &)`
- `private: virtual void __thiscall survarium::game_statistics_handler::on_event(unsigned char, enum survarium::match_stats_events_dict_enum, unsigned short)`
- `private: virtual void __thiscall survarium::grenade_set_core_cook::query_for_derived_resources(class vostok::resources::query_result_for_cook *, class survarium::grenade_set_core *, struct survarium::grenade_set_cook_data const &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>)`
- `private: virtual void __thiscall survarium::grenade_set_core_cook::translate_query(class vostok::resources::query_result_for_cook &)`
- `private: virtual void __thiscall survarium::item_config_cook::translate_query(class vostok::resources::query_result_for_cook &)`
- `private: virtual void __thiscall survarium::items_cook::translate_query(class vostok::resources::query_result_for_cook &)`
- `private: virtual void __thiscall survarium::player::generate_hit_event(unsigned int, unsigned char, unsigned char, float, float, class survarium::bullet const *, bool, unsigned short)`
- `private: virtual void __thiscall survarium::swear_filter_config_cook::translate_query(class vostok::resources::query_result_for_cook &)`
- `private: virtual void __thiscall survarium::swear_filter_cook::delete_resource(class vostok::resources::resource_base *)`
- `private: virtual void __thiscall survarium::swear_filter_cook::translate_query(class vostok::resources::query_result_for_cook &)`
- `private: virtual void __thiscall survarium::victory_item_core_put_state::on_animation_end_impl(bool &)`
- `private: virtual void __thiscall survarium::weapon_cook::on_weapon_config_loaded(class vostok::resources::queries_result &, void *, bool)`
- `private: virtual void __thiscall survarium::weapon_cook::query_weapon_states(class vostok::resources::query_result_for_cook *const, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class survarium::weapon_core *, void *, bool)`
- `private: virtual void __thiscall survarium::weapon_core::apply_look_pitch(float)`
- `private: void __thiscall survarium::base_player::generate_killed_event(unsigned int, unsigned char, char const *, class survarium::inventory_item const *, class survarium::bullet const *)`
- `private: void __thiscall survarium::chat_handler::on_message_typed(char const (&)[256], enum vostok::messaging::message_channel_enum)`
- `private: void __thiscall survarium::effect_zone_cook::create_resource(class vostok::resources::query_result_for_cook &, struct survarium::effect_zone_construct_params const &, class vostok::configs::binary_config_value const &)`
- `private: void __thiscall survarium::game::on_match_stats_movies_loaded(class vostok::resources::queries_result &)`
- `private: void __thiscall survarium::game_world_core::tick_game_objects(unsigned int, unsigned int)`
- `private: void __thiscall survarium::items_cook::create_item_and_finish_query(class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class vostok::resources::query_result_for_cook *)`
- `private: void __thiscall survarium::items_cook::on_config_ready(class vostok::resources::queries_result &)`
- `private: void __thiscall survarium::lobby_menu::create_quest_ui_message(char const *, unsigned char)`
- `private: void __thiscall survarium::lobby_menu::prepare_quest_object(struct survarium::flash_value &, struct survarium::quest_instance const &, struct survarium::quest_descriptor const &)`
- `private: void __thiscall survarium::login_menu::update_online_queue(unsigned int)`
- `private: void __thiscall survarium::network_client::register_message_in_stats(enum survarium::input_action_enum, enum vostok::match::server::messages_enum) const`
- `private: void __thiscall survarium::network_client::try_send_all(unsigned int, bool)`
- `private: void __thiscall survarium::network_stats_orders_channel::add_row(struct survarium::flash_value &, unsigned int, char const *const, class vostok::network_core::sequence_number<unsigned short> const &)`
- `private: void __thiscall survarium::network_stats_orders_channel::fill_header(void)`
- `private: void __thiscall survarium::network_stats_orders_channel::initialize_header(void)`
- `private: void __thiscall survarium::network_stats_orders_channel::on_enabled_changed(char const *)`
- `private: void __thiscall survarium::network_stats_orders_channel::update_position(unsigned int, unsigned int)`
- `private: void __thiscall survarium::network_stats_packets::add_row(struct survarium::flash_value &, unsigned int, char const *const, struct vostok::network_core::udp_match_bytes_count_stats &, unsigned int)`
- `private: void __thiscall survarium::network_stats_packets::fill_header(void)`
- `private: void __thiscall survarium::network_stats_packets::initialize_header(void)`
- `private: void __thiscall survarium::network_stats_packets::on_enabled_changed(char const *)`
- `private: void __thiscall survarium::network_stats_packets::update_position(unsigned int, unsigned int)`
- `private: void __thiscall survarium::network_stats_packets_sequence::add_row(struct survarium::flash_value &, unsigned int, char const *const, struct vostok::network_core::udp_match_raw_stats &, unsigned int)`
- `private: void __thiscall survarium::network_stats_packets_sequence::fill_header(void)`
- `private: void __thiscall survarium::network_stats_packets_sequence::initialize_header(void)`
- `private: void __thiscall survarium::network_stats_packets_sequence::on_enabled_changed(char const *)`
- `private: void __thiscall survarium::network_stats_packets_sequence::update_position(unsigned int, unsigned int)`
- `private: void __thiscall survarium::network_stats_ports::add_column(struct survarium::flash_value (&)[8], unsigned int, struct vostok::network_core::udp_match_port_sent_received_stats &, unsigned int)`
- `private: void __thiscall survarium::network_stats_ports::fill_header(void)`
- `private: void __thiscall survarium::network_stats_ports::initialize_header_impl(unsigned short, unsigned short)`
- `private: void __thiscall survarium::network_stats_ports::on_enabled_changed(char const *)`
- `private: void __thiscall survarium::network_stats_ports::update_position(unsigned int, unsigned int)`
- `private: void __thiscall survarium::network_stats_received_messages::add_row(struct survarium::flash_value &, unsigned int, char const *const, struct vostok::network_core::udp_match_received_message_stats &, struct vostok::network_core::udp_match_raw_stats const &, unsigned int)`
- `private: void __thiscall survarium::network_stats_received_messages::fill_header(void)`
- `private: void __thiscall survarium::network_stats_received_messages::initialize_header(void)`
- `private: void __thiscall survarium::network_stats_received_messages::on_enabled_changed(char const *)`
- `private: void __thiscall survarium::network_stats_received_messages::update_position(unsigned int, unsigned int)`
- `private: void __thiscall survarium::network_stats_rejected_messages::add_row(struct survarium::flash_value &, unsigned int, struct vostok::network_core::udp_match_received_message_stats &, unsigned int)`
- `private: void __thiscall survarium::network_stats_rejected_messages::initialize_header(void)`
- `private: void __thiscall survarium::network_stats_rejected_messages::on_enabled_changed(char const *)`
- `private: void __thiscall survarium::network_stats_rejected_messages::update_position(unsigned int, unsigned int)`
- `private: void __thiscall survarium::network_stats_seconds::add_row(struct survarium::flash_value &, unsigned int, char const *const, struct vostok::network_core::udp_match_raw_stats &, unsigned int)`
- `private: void __thiscall survarium::network_stats_seconds::fill_header(void)`
- `private: void __thiscall survarium::network_stats_seconds::initialize_header(void)`
- `private: void __thiscall survarium::network_stats_seconds::on_enabled_changed(char const *)`
- `private: void __thiscall survarium::network_stats_seconds::update_position(unsigned int, unsigned int)`
- `private: void __thiscall survarium::network_stats_sent_messages::add_row(struct survarium::flash_value &, unsigned int, char const *const, struct vostok::network_core::udp_match_sent_message_stats &, struct vostok::network_core::udp_match_raw_stats const &, unsigned int)`
- `private: void __thiscall survarium::network_stats_sent_messages::fill_header(void)`
- `private: void __thiscall survarium::network_stats_sent_messages::initialize_header(void)`
- `private: void __thiscall survarium::network_stats_sent_messages::on_enabled_changed(char const *)`
- `private: void __thiscall survarium::network_stats_sent_messages::update_position(unsigned int, unsigned int)`
- `private: void __thiscall survarium::player_input_handler::process_third_person_mode(void)`
- `private: void __thiscall survarium::player_logic_jump_state::initialize_logic(void)`
- `private: void __thiscall survarium::player_logic_jump_state::initialize_weight_for_on_site_animation(void)`
- `private: void __thiscall survarium::player_stamina::sprint(unsigned int)`
- `private: void __thiscall survarium::replay_network_client::on_match_replay_ready(class vostok::resources::queries_result &, class vostok::replay_match_reader *const)`
- `private: void __thiscall survarium::swear_filter_config_cook::on_binary_config_loaded(class vostok::resources::queries_result &, class vostok::resources::query_result_for_cook *)`
- `private: void __thiscall survarium::swear_filter_cook::fill_buffers(unsigned int, class vostok::configs::binary_config_value, wchar_t *, unsigned char *const, wchar_t **)`
- `private: void __thiscall survarium::swear_filter_cook::on_resources_loaded(class vostok::resources::queries_result &)`
- `private: void __thiscall survarium::weapon_cook::on_weapon_subresources_ready(class vostok::resources::queries_result &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class survarium::weapon_core *, void *, bool)`
- `private: void __thiscall survarium::weapon_core_cook::on_core_subresources_ready(class vostok::resources::queries_result &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class survarium::weapon_core *, void *, bool)`
- `private: void __thiscall vostok::animation::bone_matrices_computer::compute_skeleton_branch(class vostok::animation::skeleton_bone const &, class vostok::math::float4x4*, class vostok::math::float4x4const &, unsigned int const *, unsigned int const *, unsigned char, bool) const`
- `private: void __thiscall vostok::animation::bone_matrices_computer::compute_skeleton_branch_local(class vostok::animation::skeleton_bone const &, class vostok::math::float4x4*, unsigned int const *, unsigned int const *, unsigned char, bool) const`
- `private: void __thiscall vostok::intrusive_ptr<class vostok::render::res_shader_technique, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>::dec(void)`
- `private: void __thiscall vostok::network::login_client_impl::process_ping_answer(class boost::system::error_code const &, unsigned int)`
- `private: void __thiscall vostok::network::login_client_impl::schedule_ping(unsigned int)`
- `private: void __thiscall vostok::network::login_client_impl::start_ping_answer_acception(void)`
- `private: void __thiscall vostok::network::match_client::on_packet_received(unsigned char, class vostok::network_core::buffer_reader &, unsigned int)`
- `private: void __thiscall vostok::network::match_client::send_heart_beat(void)`
- `private: void __thiscall vostok::network::match_client_impl::on_packet_received(unsigned char, class vostok::network_core::buffer_reader &, unsigned int)`
- `private: void __thiscall vostok::network_core::async_connector::connect(class boost::asio::ip::basic_resolver_iterator<class boost::asio::ip::tcp> const &)`
- `private: void __thiscall vostok::network_core::udp_match_client::connect_impl(class vostok::network_core::udp_match_packet *const, unsigned int)`
- `private: void __thiscall vostok::network_core::udp_match_client::destroy_packet(class vostok::network_core::udp_match_packet &)`
- `private: void __thiscall vostok::network_core::udp_match_client::duplicate_packet_send_handler(class boost::system::error_code const &, unsigned int)`
- `private: void __thiscall vostok::network_core::udp_match_client::on_delayed_packet_received(class vostok::network_core::udp_match_packet &, class boost::asio::ip::basic_endpoint<class boost::asio::ip::udp> const &)`
- `private: void __thiscall vostok::network_core::udp_match_client::on_error(enum vostok::network_core::client_error_codes_enum, class boost::system::error_code)`
- `private: void __thiscall vostok::network_core::udp_match_client::original_packet_send_handler(class boost::system::error_code const &, unsigned int, class boost::function<void __cdecl (class boost::system::error_code const &, unsigned int)> const &)`
- `private: void __thiscall vostok::network_core::udp_match_client::send_packet(class vostok::network_core::udp_match_packet &, class boost::function<void __cdecl (class vostok::network_core::udp_match_packet &, class boost::system::error_code const &, unsigned int)> const &, class boost::function<void __cdecl (class vostok::network_core::udp_match_packet &)> const &)`
- `private: void __thiscall vostok::network_core::udp_match_client::send_packet_impl(class vostok::network_core::udp_match_packet &, bool, class boost::asio::ip::basic_endpoint<class boost::asio::ip::udp> const &, class boost::function<void __cdecl (class vostok::network_core::udp_match_packet &, class boost::system::error_code const &, unsigned int)> const &)`
- `private: void __thiscall vostok::network_core::udp_match_connection::send(class vostok::network_core::udp_match_packet *, class boost::function<void __cdecl (class vostok::network_core::udp_match_packet &, class boost::function<void __cdecl (class vostok::network_core::udp_match_packet &, class boost::system::error_code const &, unsigned int)> const &, class boost::function<void __cdecl (class vostok::network_core::udp_match_packet &)> const &)> const &)`
- `private: void __thiscall vostok::network_core::udp_match_connection::send_packets_list(class vostok::network_core::udp_match_packet *, unsigned int, class boost::function<void __cdecl (class vostok::network_core::udp_match_packet &, class boost::function<void __cdecl (class vostok::network_core::udp_match_packet &, class boost::system::error_code const &, unsigned int)> const &, class boost::function<void __cdecl (class vostok::network_core::udp_match_packet &)> const &)> const &)`
- `private: void __thiscall vostok::network_core::udp_match_stats::register_packet(enum vostok::network_core::udp_match_raw_stats::packets_types_enum, unsigned int, unsigned int)`
- `private: void __thiscall vostok::network_core::udp_network_flow_emulator::append_received_packet(class vostok::network_core::udp_match_packet &, class boost::function<void __cdecl (class vostok::network_core::udp_match_packet &)> const &, unsigned int, unsigned int)`
- `private: void __thiscall vostok::network_core::udp_network_flow_emulator::append_sent_packet(class vostok::network_core::udp_match_packet &, class boost::function<void __cdecl (class vostok::network_core::udp_match_packet &, bool)> const &, unsigned int, unsigned int)`
- `private: void __thiscall vostok::network_core::udp_network_flow_emulator::process_received_packets(class vostok::buffer_vector<struct stlp_std::pair<class vostok::network_core::udp_match_packet *, class boost::function<void __cdecl (class vostok::network_core::udp_match_packet &)> > > &)`
- `private: void __thiscall vostok::network_core::udp_network_flow_emulator::process_sent_packets(class vostok::buffer_vector<struct stlp_std::pair<class vostok::network_core::udp_match_packet *, class boost::function<void __cdecl (class vostok::network_core::udp_match_packet &, bool)> > > &)`
- `private: void __thiscall vostok::render::buffers_handler<2>::apply(void)`
- `private: void __thiscall vostok::render::device::find_outputs(void)`
- `private: void __thiscall vostok::render::effect_manager::delete_effect_technique(class vostok::render::res_shader_technique const *)`
- `private: void __thiscall vostok::render::scene::render_lines(bool, bool)`
- `private: void __thiscall vostok::render::scene::render_triangles(bool, bool)`
- `private: void __thiscall vostok::render::texture_cook_wrapper::on_dds_header_ready(class vostok::resources::query_result_for_cook *, class vostok::fs_new::asynchronous_device_interface *, class vostok::fs_new::native_path_string *, unsigned __int64, unsigned char *, unsigned __int64, unsigned __int64, bool)`
- `private: void __thiscall vostok::render::texture_cook_wrapper::on_fs_iterators_ready_converted(class vostok::resources::queries_result &)`
- `private: void __thiscall vostok::render::texture_cook_wrapper::query_converted_texture(class vostok::vfs::vfs_iterator, class vostok::resources::query_result_for_cook *)`
- `private: void __thiscall vostok::render::texture_cook_wrapper::query_converted_texture_mip(class vostok::vfs::vfs_iterator, class vostok::resources::query_result_for_cook *)`
- `private: void __thiscall vostok::render::texture_mip_cook::on_dds_body_ready(class vostok::resources::query_result_for_cook *, struct vostok::render::texture_mip_cook_data const *, bool)`
- `private: void __thiscall vostok::render::textures_handler<1>::reset(void)`
- `protected: __thiscall survarium::artefact_base::artefact_base(class vostok::configs::binary_config_value const &, class vostok::resources::resource_ptr<class survarium::game_effect_emitter, class vostok::resources::unmanaged_intrusive_base> const &)`
- `protected: __thiscall survarium::artefact_lifebone_core::artefact_lifebone_core(class vostok::configs::binary_config_value const &, class vostok::resources::resource_ptr<class survarium::game_effect_emitter, class vostok::resources::unmanaged_intrusive_base> const &)`
- `protected: __thiscall survarium::artefact_onyx_core::artefact_onyx_core(class vostok::configs::binary_config_value const &, class vostok::resources::resource_ptr<class survarium::game_effect_emitter, class vostok::resources::unmanaged_intrusive_base> const &)`
- `protected: __thiscall survarium::artefact_spring_core::artefact_spring_core(class vostok::configs::binary_config_value const &, class vostok::resources::resource_ptr<class survarium::game_effect_emitter, class vostok::resources::unmanaged_intrusive_base> const &)`
- `protected: __thiscall survarium::booby_trap_set_core::booby_trap_set_core(class vostok::configs::binary_config_value const &, unsigned char, struct vostok::physics::world &, class vostok::resources::resource_ptr<class survarium::game_material_manager, class vostok::resources::unmanaged_intrusive_base> const &)`
- `protected: __thiscall survarium::gather_victory_items_rule::gather_victory_items_rule(unsigned int)`
- `protected: __thiscall survarium::jump_logic_base_state::jump_logic_base_state(class survarium::player_logic_jump_state &)`
- `protected: class vostok::resources::pinned_ptr_mutable<class vostok::animation::cubic_spline_skeleton_animation> __thiscall vostok::resources::cook_base::pin_for_write<class vostok::animation::cubic_spline_skeleton_animation>(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>)`
- `protected: virtual void __thiscall survarium::base_game_statistics_handler::deserialize(class vostok::network_core::buffer_reader &, unsigned int)`
- `protected: virtual void __thiscall survarium::base_game_statistics_handler::on_artefact_took(unsigned char)`
- `protected: virtual void __thiscall survarium::base_game_statistics_handler::on_event(unsigned char, enum survarium::match_stats_events_dict_enum, unsigned short)`
- `protected: virtual void __thiscall survarium::base_game_statistics_handler::on_limb_affect(unsigned int, unsigned char, enum survarium::affect_event_type_enum)`
- `protected: virtual void __thiscall survarium::base_game_statistics_handler::on_medkit_action(class survarium::medkit const &, bool, unsigned char)`
- `protected: virtual void __thiscall survarium::base_game_statistics_handler::on_pain_body_part_damage_received(unsigned char, unsigned char, float)`
- `protected: virtual void __thiscall survarium::base_game_statistics_handler::on_pain_body_part_regenerated(unsigned char)`
- `protected: virtual void __thiscall survarium::base_game_statistics_handler::on_player_damaged(unsigned int, unsigned char, enum survarium::player_stances_enum, unsigned char, float, enum survarium::profile_slot_enum, bool, unsigned int, unsigned short)`
- `protected: virtual void __thiscall survarium::base_game_statistics_handler::on_player_killed(unsigned int, unsigned char, enum survarium::player_stances_enum, unsigned short, class vostok::math::float3const &, bool, unsigned char, class vostok::math::float3const &, bool, enum survarium::profile_slot_enum, bool, bool)`
- `protected: virtual void __thiscall survarium::base_game_statistics_handler::on_player_weapon_firing(unsigned char, enum survarium::profile_slot_enum, enum survarium::player_stances_enum, unsigned short)`
- `protected: virtual void __thiscall survarium::base_game_statistics_handler::on_victory_item_event(unsigned char, enum survarium::victory_item_event_type, class survarium::victory_item_core const &)`
- `protected: virtual void __thiscall survarium::base_game_statistics_handler::serialize(class vostok::network_core::buffer_writer const &, unsigned int) const`
- `protected: virtual void __thiscall survarium::base_player::generate_hit_event(unsigned int, unsigned char, unsigned char, float, float, class survarium::bullet const *, bool, unsigned short)`
- `protected: virtual void __thiscall survarium::base_player::hit(unsigned int, struct survarium::hit_initiator const *const, class vostok::collision::bone_collision_data const &, enum survarium::hit_type_enum, float, float, class survarium::bullet *const, class survarium::inventory_item const *const)`
- `protected: virtual void __thiscall survarium::base_player::hit(unsigned int, struct survarium::hit_initiator const *const, unsigned int, enum survarium::hit_type_enum, float, float, class survarium::bullet *const, class vostok::math::float3const &, enum survarium::triangle_orientation, class survarium::inventory_item const *const)`
- `protected: virtual void __thiscall survarium::weapon_core_cook::on_weapon_config_loaded(class vostok::resources::queries_result &, void *, bool)`
- `protected: virtual void __thiscall survarium::weapon_core_cook::query_weapon_states(class vostok::resources::query_result_for_cook *const, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class survarium::weapon_core *, void *, bool)`
- `protected: void __thiscall survarium::base_game_statistics_handler::emit_score_changed_event(unsigned char, short)`
- `protected: void __thiscall survarium::base_game_statistics_handler::recalculate_scores(void)`
- `protected: void __thiscall survarium::grenade_set_core_cook::finish_query(class vostok::resources::query_result_for_cook *, class survarium::grenade_set_core *)`
- `protected: void __thiscall survarium::weapon_core_cook::process_loading_weapon_core(class vostok::resources::query_result_for_cook *const, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class survarium::weapon_core *, void *, bool)`
- `public: __thiscall boost::_bi::storage4<class boost::_bi::value<class vostok::network::login_client_impl *>, class boost::_bi::value<unsigned int>, class boost::_bi::value<class boost::function<void __cdecl (enum vostok::connection_error_types_enum)> >, class boost::_bi::value<class boost::asio::ip::basic_resolver_iterator<class boost::asio::ip::tcp> > >::~storage4<class boost::_bi::value<class vostok::network::login_client_impl *>, class boost::_bi::value<unsigned int>, class boost::_bi::value<class boost::function<void __cdecl (enum vostok::connection_error_types_enum)> >, class boost::_bi::value<class boost::asio::ip::basic_resolver_iterator<class boost::asio::ip::tcp> > >(void)`
- `public: __thiscall character_step_down_sweep_test_callback::character_step_down_sweep_test_callback(class btCollisionWorld &, class btCollisionObject &, class btVector3const &, float, class btVector3const &, float, float, float)`
- `public: __thiscall survarium::base_game_statistics_handler::base_game_statistics_handler(void)`
- `public: __thiscall survarium::dictionary_item::~dictionary_item(void)`
- `public: __thiscall survarium::grenade_set_core::grenade_set_core(class vostok::configs::binary_config_value const &, unsigned char)`
- `public: __thiscall survarium::hit_info::hit_info(unsigned int, unsigned char, unsigned char, char const *const, enum survarium::hit_type_enum, float, float, class survarium::bullet *const, class vostok::math::float3const &, enum survarium::triangle_orientation, class survarium::inventory_item const *const)`
- `public: __thiscall survarium::inventory_item::inventory_item(class vostok::configs::binary_config_value const &, enum survarium::inventory_item::action_behaviour_type, bool)`
- `public: __thiscall survarium::inventory_item_descr::inventory_item_descr(void)`
- `public: __thiscall survarium::inventory_item_descr::~inventory_item_descr(void)`
- `public: __thiscall survarium::items_dictionary::items_dictionary(class vostok::memory::base_allocator *, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: __thiscall survarium::match_client::match_client(struct vostok::network::world &, class vostok::timing::timer const &)`
- `public: __thiscall survarium::match_options::~match_options(void)`
- `public: __thiscall survarium::match_stats::match_stats(void)`
- `public: __thiscall survarium::network_stats_orders_channel::network_stats_orders_channel(class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: __thiscall survarium::network_stats_packets::network_stats_packets(class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: __thiscall survarium::network_stats_packets_sequence::network_stats_packets_sequence(class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: __thiscall survarium::network_stats_ports::network_stats_ports(class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: __thiscall survarium::network_stats_received_messages::network_stats_received_messages(class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: __thiscall survarium::network_stats_rejected_messages::network_stats_rejected_messages(class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: __thiscall survarium::network_stats_seconds::network_stats_seconds(class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: __thiscall survarium::network_stats_sent_messages::network_stats_sent_messages(class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: __thiscall survarium::player_logic_jump_state::player_logic_jump_state(class survarium::weapon_user_animations_selector &)`
- `public: __thiscall survarium::player_result_brief::player_result_brief(void)`
- `public: __thiscall survarium::player_result_full::player_result_full(void)`
- `public: __thiscall survarium::portable_interactive_object::portable_interactive_object(class survarium::base_game_scene &)`
- `public: __thiscall survarium::replay_network_client::replay_network_client(class survarium::game &)`
- `public: __thiscall survarium::swear_filter::swear_filter(wchar_t **const, unsigned int, wchar_t *const, unsigned int, wchar_t **const, unsigned int, wchar_t *const, unsigned int, char *)`
- `public: __thiscall survarium::weapon::weapon(class vostok::configs::binary_config_value const &, class survarium::base_game_scene &, unsigned int)`
- `public: __thiscall survarium::weapon_ammunition::weapon_ammunition(class vostok::configs::binary_config_value const &)`
- `public: __thiscall survarium::weapon_core::weapon_core(class vostok::configs::binary_config_value const &)`
- `public: __thiscall vostok::animation::animation_player::animation_player(unsigned int)`
- `public: __thiscall vostok::buffer_vector<class boost::basic_regex<wchar_t, struct boost::regex_traits<wchar_t, class boost::w32_regex_traits<wchar_t> > > >::~buffer_vector<class boost::basic_regex<wchar_t, struct boost::regex_traits<wchar_t, class boost::w32_regex_traits<wchar_t> > > >(void)`
- `public: __thiscall vostok::buffer_vector<struct stlp_std::pair<class vostok::network_core::udp_match_packet *, class boost::function<void __cdecl (class vostok::network_core::udp_match_packet &)> > >::~buffer_vector<struct stlp_std::pair<class vostok::network_core::udp_match_packet *, class boost::function<void __cdecl (class vostok::network_core::udp_match_packet &)> > >(void)`
- `public: __thiscall vostok::circular_buffer<struct stlp_std::pair<unsigned int, unsigned int>, 128>::~circular_buffer<struct stlp_std::pair<unsigned int, unsigned int>, 128>(void)`
- `public: __thiscall vostok::console_commands::logging_filters_console_command::logging_filters_console_command(class vostok::logging::filter_tree &, char const *const, bool, enum vostok::console_commands::command_type, enum vostok::console_commands::execution_filter)`
- `public: __thiscall vostok::fixed_vector<struct vostok::particle::render_particle_emitter_instance *, 2048>::fixed_vector<struct vostok::particle::render_particle_emitter_instance *, 2048>(class vostok::fixed_vector<struct vostok::particle::render_particle_emitter_instance *, 2048> const &)`
- `public: __thiscall vostok::intrusive_ptr<class vostok::render::skin, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock>::~intrusive_ptr<class vostok::render::skin, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock>(void)`
- `public: __thiscall vostok::math::float4x4::float4x4(void)`
- `public: __thiscall vostok::math::half2::half2(class vostok::math::float2const &)`
- `public: __thiscall vostok::memory::single_size_buffer_allocator<684, class vostok::threading::multi_threading_policy>::single_size_buffer_allocator<684, class vostok::threading::multi_threading_policy>(void *, unsigned int, class boost::function<void __cdecl (class vostok::memory::single_size_buffer_allocator<684, class vostok::threading::multi_threading_policy> const &)> const &)`
- `public: __thiscall vostok::memory::single_size_buffer_allocator<80, class vostok::threading::single_threading_policy>::single_size_buffer_allocator<80, class vostok::threading::single_threading_policy>(void *, unsigned int, class boost::function<void __cdecl (class vostok::memory::single_size_buffer_allocator<80, class vostok::threading::single_threading_policy> const &)> const &)`
- `public: __thiscall vostok::network::connect_order::connect_order(class vostok::memory::base_allocator &, class vostok::memory::base_allocator &, char const *const, class vostok::intrusive_ptr<class vostok::network_core::udp_match_packets_allocator, class vostok::network_core::udp_match_packets_allocator, class vostok::threading::multi_threading_policy> const &, class vostok::network_core::udp_match_packet const *, class boost::function<void __cdecl (char const *, class vostok::network_core::udp_match_packet const *)> const &, class vostok::network_core::udp_match_stats &)`
- `public: __thiscall vostok::network::match_client::match_client(struct vostok::network::world &, struct vostok::network_core::udp_match_packets_orderer &, struct vostok::network_core::udp_network_flow_emulator_options const *, class vostok::timing::timer const &)`
- `public: __thiscall vostok::network::udp_match_fixed_packets_allocator<4096>::udp_match_fixed_packets_allocator<4096>(class vostok::memory::base_allocator &)`
- `public: __thiscall vostok::network_core::udp_match_bytes_count_stats::udp_match_bytes_count_stats(struct vostok::network_core::udp_match_bytes_count_stats const &)`
- `public: __thiscall vostok::network_core::udp_match_bytes_count_stats::udp_match_bytes_count_stats(void)`
- `public: __thiscall vostok::network_core::udp_match_bytes_count_stats::~udp_match_bytes_count_stats(void)`
- `public: __thiscall vostok::network_core::udp_match_client::udp_match_client(class boost::asio::io_service &, class vostok::memory::single_size_buffer_allocator<684, class vostok::threading::multi_threading_policy> &, struct vostok::network_core::udp_match_packets_orderer &, class vostok::network_core::udp_network_flow_emulator *)`
- `public: __thiscall vostok::network_core::udp_match_connection::udp_match_connection(class vostok::memory::single_size_buffer_allocator<684, class vostok::threading::multi_threading_policy> &, struct vostok::network_core::udp_match_packets_orderer &, unsigned int, unsigned int, char const *const, unsigned char, unsigned char)`
- `public: __thiscall vostok::network_core::udp_match_max_value_stats::udp_match_max_value_stats(struct vostok::network_core::udp_match_max_value_stats const &)`
- `public: __thiscall vostok::network_core::udp_match_message_item_duplicates_stats::udp_match_message_item_duplicates_stats(struct vostok::network_core::udp_match_message_item_duplicates_stats const &)`
- `public: __thiscall vostok::network_core::udp_match_message_item_flow_stats::udp_match_message_item_flow_stats(struct vostok::network_core::udp_match_message_item_flow_stats const &)`
- `public: __thiscall vostok::network_core::udp_match_message_item_flow_stats::udp_match_message_item_flow_stats(void)`
- `public: __thiscall vostok::network_core::udp_match_message_item_flow_stats::~udp_match_message_item_flow_stats(void)`
- `public: __thiscall vostok::network_core::udp_match_messages_stats::udp_match_messages_stats(void)`
- `public: __thiscall vostok::network_core::udp_match_messages_stats_cumulative_template<struct vostok::network_core::udp_match_received_message_stats, 10>::~udp_match_messages_stats_cumulative_template<struct vostok::network_core::udp_match_received_message_stats, 10>(void)`
- `public: __thiscall vostok::network_core::udp_match_messages_stats_cumulative_template<struct vostok::network_core::udp_match_received_message_stats, 3>::~udp_match_messages_stats_cumulative_template<struct vostok::network_core::udp_match_received_message_stats, 3>(void)`
- `public: __thiscall vostok::network_core::udp_match_messages_stats_cumulative_template<struct vostok::network_core::udp_match_sent_message_stats, 10>::~udp_match_messages_stats_cumulative_template<struct vostok::network_core::udp_match_sent_message_stats, 10>(void)`
- `public: __thiscall vostok::network_core::udp_match_messages_stats_cumulative_template<struct vostok::network_core::udp_match_sent_message_stats, 3>::~udp_match_messages_stats_cumulative_template<struct vostok::network_core::udp_match_sent_message_stats, 3>(void)`
- `public: __thiscall vostok::network_core::udp_match_messages_stats_template<struct vostok::network_core::udp_match_received_message_stats>::udp_match_messages_stats_template<struct vostok::network_core::udp_match_received_message_stats>(struct vostok::network_core::udp_match_messages_stats_template<struct vostok::network_core::udp_match_received_message_stats> const &)`
- `public: __thiscall vostok::network_core::udp_match_messages_stats_template<struct vostok::network_core::udp_match_received_message_stats>::~udp_match_messages_stats_template<struct vostok::network_core::udp_match_received_message_stats>(void)`
- `public: __thiscall vostok::network_core::udp_match_messages_stats_template<struct vostok::network_core::udp_match_sent_message_stats>::udp_match_messages_stats_template<struct vostok::network_core::udp_match_sent_message_stats>(struct vostok::network_core::udp_match_messages_stats_template<struct vostok::network_core::udp_match_sent_message_stats> const &)`
- `public: __thiscall vostok::network_core::udp_match_messages_stats_template<struct vostok::network_core::udp_match_sent_message_stats>::~udp_match_messages_stats_template<struct vostok::network_core::udp_match_sent_message_stats>(void)`
- `public: __thiscall vostok::network_core::udp_match_raw_stats::udp_match_raw_stats(struct vostok::network_core::udp_match_raw_stats const &)`
- `public: __thiscall vostok::network_core::udp_match_raw_stats::udp_match_raw_stats(void)`
- `public: __thiscall vostok::network_core::udp_match_raw_stats::~udp_match_raw_stats(void)`
- `public: __thiscall vostok::network_core::udp_match_received_message_stats::udp_match_received_message_stats(struct vostok::network_core::udp_match_received_message_stats const &)`
- `public: __thiscall vostok::network_core::udp_match_received_message_stats::udp_match_received_message_stats(void)`
- `public: __thiscall vostok::network_core::udp_match_received_message_stats::~udp_match_received_message_stats(void)`
- `public: __thiscall vostok::network_core::udp_match_sent_message_stats::udp_match_sent_message_stats(struct vostok::network_core::udp_match_sent_message_stats const &)`
- `public: __thiscall vostok::network_core::udp_match_sent_message_stats::udp_match_sent_message_stats(void)`
- `public: __thiscall vostok::network_core::udp_match_sent_message_stats::~udp_match_sent_message_stats(void)`
- `public: __thiscall vostok::network_core::udp_match_stats::udp_match_stats(struct vostok::network_core::udp_match_packets_orderer &, unsigned char, unsigned char)`
- `public: __thiscall vostok::network_core::udp_network_flow_emulator::udp_network_flow_emulator(class vostok::memory::base_allocator &, struct vostok::network_core::udp_network_flow_emulator_options const &, unsigned int)`
- `public: __thiscall vostok::render::device::device(unsigned __int64, bool)`
- `public: __thiscall vostok::render::device::~device(void)`
- `public: __thiscall vostok::render::particle_rain_drops_geometry::particle_rain_drops_geometry(unsigned int)`
- `public: __thiscall vostok::render::particle_rain_drops_geometry::~particle_rain_drops_geometry(void)`
- `public: __thiscall vostok::resources::managed_cook::managed_cook(enum vostok::resources::class_id_enum, enum vostok::resources::cook_base::reuse_enum, unsigned int, class vostok::enum_flags<enum vostok::resources::cook_base::flags_enum>)`
- `public: __thiscall vostok::variant<32>::~variant<32>(void)`
- `public: bool __thiscall delayed_received_packets_predicate::operator()(struct stlp_std::pair<class vostok::network_core::udp_match_packet *, class boost::function<void __cdecl (class vostok::network_core::udp_match_packet &)> > const &) const`
- `public: bool __thiscall delayed_sent_packets_predicate::operator()(struct stlp_std::pair<class vostok::network_core::udp_match_packet *, class boost::function<void __cdecl (class vostok::network_core::udp_match_packet &, bool)> > const &) const`
- `public: bool __thiscall survarium::lobby_client::read_match_stats(class vostok::network_core::buffer_reader &)`
- `public: bool __thiscall survarium::packet_sender::on_player_input_changed(struct survarium::player_update &) const`
- `public: bool __thiscall survarium::player_logic_jump_state::is_short_jump(void) const`
- `public: bool __thiscall survarium::player_stamina::tick(unsigned int, bool, bool)`
- `public: bool __thiscall vostok::network_core::move_to_list_predicate::operator()(class vostok::network_core::udp_match_packet *const) const`
- `public: bool __thiscall vostok::physics::bt_character_controller::can_jump(void) const`
- `public: bool __thiscall vostok::physics::character_controller_impassable_slide_down_tester::convex_sweep_test(class btVector3const &, class btVector3const &, class btVector3&, class btVector3&, float &)`
- `public: bool __thiscall vostok::render::options::use_ssr(void) const`
- `public: bool __thiscall vostok::render::remove_texture_predicate::operator()(struct vostok::render::streamable_texture_info const &)`
- `public: bool __thiscall vostok::variant<32>::try_get<struct survarium::item_config_cook_data>(struct survarium::item_config_cook_data &)`
- `public: bool __thiscall vostok::variant<32>::try_get<struct survarium::item_cook_data>(struct survarium::item_cook_data &)`
- `public: bool __thiscall vostok::variant<32>::try_get<unsigned int>(unsigned int &)`
- `public: class vostok::buffer_vector<class vostok::render::buffer_slot> & __thiscall vostok::buffer_vector<class vostok::render::buffer_slot>::operator=(class vostok::buffer_vector<class vostok::render::buffer_slot> const &)`
- `public: class vostok::buffer_vector<class vostok::render::texture_slot> & __thiscall vostok::buffer_vector<class vostok::render::texture_slot>::operator=(class vostok::buffer_vector<class vostok::render::texture_slot> const &)`
- `public: class vostok::buffer_vector<unsigned int> & __thiscall vostok::buffer_vector<unsigned int>::operator=(class vostok::buffer_vector<unsigned int> const &)`
- `public: class vostok::fs_new::virtual_path_string const & __thiscall vostok::fs_new::virtual_path_string::operator=<class vostok::configs::binary_config_value>(class vostok::configs::binary_config_value const &)`
- `public: class vostok::math::float4x4 __thiscall vostok::animation::animation_player::computed_bone_matrix(class vostok::animation::skeleton const &, class vostok::animation::skeleton_bone const &, void const *const, unsigned int const *const, class boost::function<class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> __cdecl (unsigned short)> const &, bool) const`
- `public: class vostok::math::float4x4 __thiscall vostok::animation::bone_matrices_computer::computed_bone_matrix(class vostok::animation::skeleton_bone const &, unsigned int const *, bool) const`
- `public: class vostok::math::float4x4 __thiscall vostok::physics::bt_character_controller::get_transform(void) const`
- `public: class vostok::math::int2 __thiscall vostok::render::device::get_max_supported_resolution(void) const`
- `public: class vostok::network_core::udp_match_stats & __thiscall vostok::network::match_client::stats(void) const`
- `public: class vostok::render::res_texture * __thiscall vostok::render::resource_manager::on_texture_loaded_res_impl(unsigned char const *, unsigned int, unsigned int, unsigned int, unsigned int, unsigned int, char const *, unsigned int, bool)`
- `public: class vostok::resources::resource_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base> __thiscall survarium::base_network_client::get_last_current_player(void)`
- `public: enum assert_on_fail_bool __thiscall vostok::resources::query_result_for_cook::assert_on_fail(void) const`
- `public: enum survarium::input_action_enum __thiscall survarium::game_world_core::discard_input(unsigned char, unsigned int)`
- `public: enum survarium::input_action_enum __thiscall survarium::game_world_core::enter_match(unsigned char, unsigned int)`
- `public: enum survarium::input_action_enum __thiscall survarium::game_world_core::leave_match(unsigned char, unsigned int)`
- `public: static struct survarium::price_item * __cdecl vostok::memory::new_array_helper<struct survarium::price_item>::call<class vostok::memory::doug_lea_allocator>(class vostok::memory::doug_lea_allocator &, unsigned int, char const *const, char const *const, unsigned int)`
- `public: static union vostok::memory::single_size_buffer_allocator<684, class vostok::threading::multi_threading_policy>::node * __cdecl vostok::memory::multi_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<684, class vostok::threading::multi_threading_policy>::node>::allocate(union vostok::memory::multi_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<684, class vostok::threading::multi_threading_policy>::node>::free_list_type &)`
- `public: static union vostok::memory::single_size_buffer_allocator<80, class vostok::threading::single_threading_policy>::node * __cdecl vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<80, class vostok::threading::single_threading_policy>::node>::allocate(class vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<80, class vostok::threading::single_threading_policy>::node>::free_list_type &)`
- `public: static unsigned int __cdecl vostok::detail::type_to_int<struct survarium::item_config_cook_data>::get(void)`
- `public: static unsigned int __cdecl vostok::detail::type_to_int<struct survarium::item_cook_data>::get(void)`
- `public: static unsigned int __cdecl vostok::detail::type_to_int<unsigned int>::get(void)`
- `public: static void __cdecl survarium::item_config_cook::create_request(struct survarium::item_config_cook_data const &, class vostok::fs_new::virtual_path_string &, enum vostok::resources::class_id_enum &)`
- `public: static void __cdecl vostok::memory::detail::call_constructor_helper<struct survarium::dictionary_item, 0>::call(struct survarium::dictionary_item *const, struct survarium::dictionary_item *const)`
- `public: static void __cdecl vostok::network_core::lost_packets_detector::call_predicate_on_every_bit<struct vostok::network_core::not_received_packets_predicate>(unsigned __int64const &, unsigned int, class vostok::network_core::sequence_number<unsigned short> const &, struct vostok::network_core::not_received_packets_predicate const &)`
- `public: static void __cdecl vostok::network_core::lost_packets_detector::call_predicate_on_every_bit<struct vostok::network_core::sent_lost_packets_predicate>(unsigned __int64const &, unsigned int, class vostok::network_core::sequence_number<unsigned short> const &, struct vostok::network_core::sent_lost_packets_predicate const &)`
- `public: static void __cdecl vostok::render::resource_intrusive_base::destroy<class vostok::render::res_state>(class vostok::render::res_state const *const)`
- `public: struct IDXGIOutput * __thiscall vostok::render::device::get_output(unsigned int) const`
- `public: struct stlp_std::pair<class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> > __thiscall survarium::player_logic_jump_state::get_animation(enum survarium::jump_animation_parts) const`
- `public: struct stlp_std::pair<class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> > __thiscall survarium::player_logic_jump_state::get_animation(enum survarium::jump_type_enum, enum survarium::jump_animation_parts) const`
- `public: struct stlp_std::pair<class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> > __thiscall survarium::player_logic_jump_state::get_move_animation(void) const`
- `public: struct survarium::dictionary_item const * __thiscall survarium::items_dictionary::item_by_id(unsigned int) const`
- `public: struct survarium::item_modification * __thiscall survarium::items_dictionary::item_modification_by_id(unsigned int) const`
- `public: struct survarium::lobby_player_profile & __thiscall survarium::lobby_player_profile::operator=(struct survarium::lobby_player_profile const &)`
- `public: struct survarium::player_profile & __thiscall survarium::player_profile::operator=(struct survarium::player_profile const &)`
- `public: unsigned __int64 __thiscall vostok::render::hw_buffer_pool::total_allocated_memory(void) const`
- `public: unsigned char __thiscall survarium::lobby_client::squad_ready_count(void) const`
- `public: unsigned char __thiscall survarium::swear_filter::filter_text(wchar_t *, unsigned short, wchar_t const *) const`
- `public: unsigned int __thiscall vostok::network_core::udp_match_stats::register_received_message(class vostok::network_core::buffer_reader const &, unsigned char)`
- `public: unsigned int __thiscall vostok::render::resource_manager::get_texture_video_memory_size(void)`
- `public: unsigned int __thiscall vostok::render::statistics_group::render_column(struct vostok::ui::world &, unsigned int, unsigned int, enum vostok::render::statistics_group::enum_item_column)`
- `public: unsigned int __thiscall vostok::render::texture_storage::occupied_memory(void) const`
- `public: unsigned int __thiscall vostok::vfs::vfs_iterator::get_file_size(void) const`
- `public: virtual __thiscall survarium::base_game_statistics_handler::~base_game_statistics_handler(void)`
- `public: virtual __thiscall survarium::base_local_network_client::~base_local_network_client(void)`
- `public: virtual __thiscall survarium::gather_victory_items_rule::~gather_victory_items_rule(void)`
- `public: virtual __thiscall survarium::player_logic_jump_state::~player_logic_jump_state(void)`
- `public: virtual bool __thiscall survarium::game_world::on_mouse_key_action(struct vostok::input::world *, enum vostok::input::mouse_button, enum vostok::input::enum_mouse_key_action)`
- `public: virtual class survarium::grenade_set_core * __thiscall survarium::grenade_set_cook::new_derived_resource(void *const, class vostok::configs::binary_config_value const &, unsigned char)`
- `public: virtual class vostok::detail::abstract_type_helper * __thiscall vostok::detail::concrete_type_helper<struct survarium::item_config_cook_data>::copy_helper(class vostok::mutable_buffer)`
- `public: virtual class vostok::detail::abstract_type_helper * __thiscall vostok::detail::concrete_type_helper<struct survarium::item_cook_data>::copy_helper(class vostok::mutable_buffer)`
- `public: virtual class vostok::detail::abstract_type_helper * __thiscall vostok::detail::concrete_type_helper<unsigned int>::copy_helper(class vostok::mutable_buffer)`
- `public: virtual class vostok::math::float4x4const & __thiscall vostok::render::render_model_instance_impl::transform(void) const`
- `public: virtual class vostok::resources::resource_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base> __thiscall survarium::base_local_network_client::get_active_player(unsigned char) const`
- `public: virtual class vostok::resources::resource_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base> __thiscall survarium::base_local_network_client::get_player(unsigned char) const`
- `public: virtual float __thiscall closest_convex_not_me_result_callback::addSingleResult(struct btCollisionWorld::LocalConvexResult &, bool)`
- `public: virtual float __thiscall survarium::interactive_object::look_pitch(void) const`
- `public: virtual int __thiscall btRigidBody::calculateSerializeBufferSize(void) const`
- `public: virtual unsigned int __thiscall vostok::render::texture_mip_cook::calculate_resource_size(class vostok::const_buffer, bool)`
- `public: virtual void __thiscall survarium::base_game_statistics_handler::finish_match(void)`
- `public: virtual void __thiscall survarium::base_game_statistics_handler::start_match(class survarium::game_world_core &, struct survarium::match_options const &)`
- `public: virtual void __thiscall survarium::base_local_network_client::attach_to_next_player(void)`
- `public: virtual void __thiscall survarium::base_local_network_client::attach_to_player(class vostok::resources::resource_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base>)`
- `public: virtual void __thiscall survarium::base_local_network_client::attach_to_prev_player(void)`
- `public: virtual void __thiscall survarium::base_local_network_client::attach_to_target_player(void)`
- `public: virtual void __thiscall survarium::base_local_network_client::detach_from_player(void)`
- `public: virtual void __thiscall survarium::base_view_network_client::to_first_view_mode(class survarium::game_world &)`
- `public: virtual void __thiscall survarium::base_view_network_client::to_free_fly_mode(class survarium::game_world &)`
- `public: virtual void __thiscall survarium::base_view_network_client::to_third_view_mode(class survarium::game_world &)`
- `public: virtual void __thiscall survarium::game::on_clipboard_changed(wchar_t const *)`
- `public: virtual void __thiscall survarium::game_statistics_handler::start_match(class survarium::game_world_core &, struct survarium::match_options const &)`
- `public: virtual void __thiscall survarium::interactive_object::apply_look_pitch(float)`
- `public: virtual void __thiscall survarium::match_time_vi_spawn_rule::deserialize(class vostok::network_core::buffer_reader &, unsigned int)`
- `public: virtual void __thiscall survarium::match_time_vi_spawn_rule::on_match_ready(unsigned int)`
- `public: virtual void __thiscall survarium::match_time_vi_spawn_rule::serialize(class vostok::network_core::buffer_writer const &, unsigned int) const`
- `public: virtual void __thiscall survarium::match_time_vi_spawn_rule::tick(unsigned int, unsigned int)`
- `public: virtual void __thiscall survarium::network_client::draw_match_stats(unsigned int)`
- `public: virtual void __thiscall survarium::player_logic_base_state::set_user(class survarium::base_player &)`
- `public: virtual void __thiscall survarium::portable_interactive_object_with_finger_correction::on_weapon_user_sprint(bool, bool)`
- `public: virtual void __thiscall survarium::replay_network_client::close_current_match(enum vostok::network_core::disconnect_event_types_enum)`
- `public: virtual void __thiscall survarium::replay_network_client::load_replay(class vostok::replay_match_reader *const)`
- `public: virtual void __thiscall survarium::replay_network_client::set_player_score_changed_callback(class boost::function<void __cdecl (unsigned char, short)> const &)`
- `public: virtual void __thiscall survarium::replay_network_client::unload(void)`
- `public: virtual void __thiscall survarium::text_clipboard::OnTextStore(wchar_t const *, unsigned int)`
- `public: virtual void __thiscall vostok::animation::cubic_spline_skeleton_animation_cook::destroy_resource(class vostok::resources::managed_resource *)`
- `public: virtual void __thiscall vostok::detail::concrete_type_helper<struct survarium::item_cook_data>::copy(class vostok::mutable_buffer, class vostok::const_buffer)`
- `public: virtual void __thiscall vostok::particle::particle_world::get_render_emitter_instances(class vostok::math::float4x4const &, class vostok::fixed_vector<struct vostok::particle::render_particle_emitter_instance *, 2048> &)`
- `public: virtual void __thiscall vostok::render::effect_probe_brdf::compile(class vostok::render::effect_compiler &, class vostok::configs::binary_config_value const &, struct vostok::render::surface_effect_parameters const &)`
- `public: virtual void __thiscall vostok::render::effect_ssr::compile(class vostok::render::effect_compiler &, class vostok::configs::binary_config_value const &, struct vostok::render::surface_effect_parameters const &)`
- _...and 205 more_

### Deleted (383)

- `?set_size@render_output_window@render@vostok@@QAEXII_N_N1@Z`
- `?set_size@res_render_output@render@vostok@@QAEXII_N_N1@Z`
- ``vostok::render::scene::process_streaming'::`51'::remove_texture_predicate::operator()`
- `bool __cdecl vostok::network_core::operator>=(struct vostok::network_core::udp_match_stats const &, struct vostok::network_core::udp_match_stats const &)`
- `bool __cdecl vostok::network_core::operator>=(struct vostok::network_core::udp_match_stream_stats const &, struct vostok::network_core::udp_match_stream_stats const &)`
- `bool __cdecl vostok::render::reclaim<class vostok::render::res_render_output, 64>(class vostok::fixed_vector<class vostok::render::res_render_output *, 64> &, class vostok::render::res_render_output const *)`
- `bool __cdecl vostok::render::reclaim<class vostok::render::res_xs<struct vostok::render::gs_data>, struct vostok::render::resource_manager::compare_shader_predicate<struct vostok::render::gs_data> >(class vostok::render::set<class vostok::render::res_xs<struct vostok::render::gs_data> *, struct vostok::render::resource_manager::compare_shader_predicate<struct vostok::render::gs_data> > &, class vostok::render::res_xs<struct vostok::render::gs_data> const *)`
- `class vostok::math::aabb __cdecl vostok::math::operator*(class vostok::math::aabb const &, float)`
- `class vostok::math::float2 __cdecl vostok::math::normalize_safe(class vostok::math::float2_pod const &, class vostok::math::float2_pod const &)`
- `class vostok::math::float4x4 __cdecl vostok::math::operator*(class vostok::math::float4x4const &, class vostok::math::float4x4const &)`
- `class vostok::network_core::udp_match_packet * __cdecl vostok::network_core::new_udp_match_packet(class vostok::memory::single_size_buffer_allocator<1364, class vostok::threading::multi_threading_policy> &)`
- `class vostok::resources::resource_ptr<class vostok::render::scene, class vostok::resources::unmanaged_resource> __cdecl vostok::static_cast_resource_ptr<class vostok::resources::resource_ptr<class vostok::render::scene, class vostok::resources::unmanaged_resource>, struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &)`
- `private: __thiscall survarium::booby_trap_set::booby_trap_set(class survarium::base_game_scene &, struct vostok::physics::world &, class vostok::resources::resource_ptr<class survarium::game_material_manager, class vostok::resources::unmanaged_intrusive_base> const &)`
- `private: __thiscall survarium::gather_victory_items_rule::gather_victory_items_rule(unsigned int)`
- `private: __thiscall survarium::medkit::medkit(void)`
- `private: __thiscall survarium::oxygen_tank::oxygen_tank(void)`
- `private: __thiscall vostok::resources::pinned_ptr_mutable<struct vostok::render::texture_data_resource>::pinned_ptr_mutable<struct vostok::render::texture_data_resource>(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>)`
- `private: bool __thiscall vostok::physics::bullet_character_controller::on_steep_slope(void) const`
- `private: bool __thiscall vostok::physics::bullet_character_controller::side_slide_on_low_ceiling(class btVector3const &, class btVector3const &, class btVector3const &, float, float, class btVector3const &, class btVector3&, float &)`
- `private: bool __thiscall vostok::physics::bullet_character_controller::side_slide_on_slope(class btVector3const &, class btVector3const &, class btVector3const &, float, float, class btVector3&, float &)`
- `private: bool __thiscall vostok::physics::bullet_character_controller::slide_in_impassable_case_impl(class btVector3const &, class btVector3const &, class btVector3const &, float, float, class btVector3&, float &)`
- `private: bool __thiscall vostok::physics::bullet_character_controller::step_down_sweep_test_impl(float, float, class btVector3const &, float, class btVector3const &, class btVector3&, class btVector3&, float &)`
- `private: bool __thiscall vostok::physics::old_bullet_character_controller::convex_sweep_test(class btTransform const &, class btTransform const &, class btVector3const &, float, float, class btVector3&, class btVector3&, float &)`
- `private: class btVector3 __thiscall character_step_down_sweep_test_callback::get_normal_for_impassable_slope(class btVector3const &)`
- `private: class btVector3 __thiscall vostok::physics::old_bullet_character_controller::updateTargetPositionBasedOnCollision(class btVector3const &, class btVector3const &, float, float)`
- `private: class survarium::weapon * __thiscall survarium::weapon_cook::allocate_weapon(class survarium::base_game_scene &, unsigned int, unsigned char, unsigned char)`
- `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::jump_logic_state_landing::get_look_lexeme(class vostok::mutable_buffer &, class fastdelegate::FastDelegate<float __cdecl (float, float, unsigned int, unsigned int, unsigned int, float)> const &, class vostok::animation::mixing::animation_lexeme &)`
- `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::jump_logic_state_prepare::get_look_lexeme(class vostok::mutable_buffer &, class fastdelegate::FastDelegate<float __cdecl (float, float, unsigned int, unsigned int, unsigned int, float)> const &, class vostok::animation::mixing::animation_lexeme &)`
- `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::jump_logic_state_start::get_look_lexeme(class vostok::mutable_buffer &, class fastdelegate::FastDelegate<float __cdecl (float, float, unsigned int, unsigned int, unsigned int, float)> const &, class vostok::animation::mixing::animation_lexeme &)`
- `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::short_jump_landing_state::get_look_lexeme(class vostok::mutable_buffer &, class fastdelegate::FastDelegate<float __cdecl (float, float, unsigned int, unsigned int, unsigned int, float)> const &, class vostok::animation::mixing::animation_lexeme &)`
- `private: class vostok::math::float4x4 __thiscall vostok::animation::bone_matrices_computer::computed_local_bone_matrix(class vostok::animation::skeleton_bone const &, unsigned int) const`
- `private: class vostok::math::float4x4 __thiscall vostok::render::stage_shadow_direct::get_texture_space_transform(void) const`
- `private: float __thiscall vostok::physics::bullet_character_controller::update_slide_velocity(class btVector3const &, class btVector3const &, float)`
- `private: float __thiscall vostok::physics::old_bullet_character_controller::recover_from_penetration(int)`
- `private: static void __cdecl vostok::buffer_vector<class vostok::intrusive_ptr<class vostok::render::res_shader_technique, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy> >::destroy(class vostok::intrusive_ptr<class vostok::render::res_shader_technique, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy> *, class vostok::intrusive_ptr<class vostok::render::res_shader_technique, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy> *const &)`
- `private: struct vostok::animation::bone_transform __thiscall vostok::animation::bone_matrices_computer::computed_local_bone_transform(class vostok::animation::skeleton_bone const &, unsigned int, unsigned int) const`
- `private: unsigned int __thiscall survarium::network_client::try_send_all(unsigned int, bool)`
- `private: virtual bool __thiscall survarium::jump_logic_state_prepare::is_ready_for_transition(void) const`
- `private: virtual bool __thiscall survarium::victory_item_core_put_state::is_ready_for_transition(void) const`
- `private: virtual bool __thiscall vostok::render::stage_rain::is_effects_ready(void) const`
- `private: virtual class btCollisionObject * __thiscall vostok::physics::old_bullet_character_controller::get_bt_collision_obect(void)`
- `private: virtual class survarium::booby_trap_set_core * __thiscall survarium::booby_trap_set_cook::new_derived_resource(struct vostok::physics::world &, class vostok::resources::resource_ptr<class survarium::game_material_manager, class vostok::resources::unmanaged_intrusive_base> const &, void *const)`
- `private: virtual class survarium::booby_trap_set_core * __thiscall survarium::booby_trap_set_core_cook::new_derived_resource(struct vostok::physics::world &, class vostok::resources::resource_ptr<class survarium::game_material_manager, class vostok::resources::unmanaged_intrusive_base> const &, void *const)`
- `private: virtual struct stlp_std::pair<class vostok::animation::mixing::expression, class vostok::animation::mixing::animation_lexeme> __thiscall survarium::jump_logic_state_landing::selected_animations(class vostok::mutable_buffer &, class fastdelegate::FastDelegate<float __cdecl (float, float, unsigned int, unsigned int, unsigned int, float)> const &, struct survarium::weapon_animation_parameters const &)`
- `private: virtual struct stlp_std::pair<class vostok::animation::mixing::expression, class vostok::animation::mixing::animation_lexeme> __thiscall survarium::jump_logic_state_prepare::selected_animations(class vostok::mutable_buffer &, class fastdelegate::FastDelegate<float __cdecl (float, float, unsigned int, unsigned int, unsigned int, float)> const &, struct survarium::weapon_animation_parameters const &)`
- `private: virtual struct stlp_std::pair<class vostok::animation::mixing::expression, class vostok::animation::mixing::animation_lexeme> __thiscall survarium::jump_logic_state_start::selected_animations(class vostok::mutable_buffer &, class fastdelegate::FastDelegate<float __cdecl (float, float, unsigned int, unsigned int, unsigned int, float)> const &, struct survarium::weapon_animation_parameters const &)`
- `private: virtual struct stlp_std::pair<class vostok::animation::mixing::expression, class vostok::animation::mixing::animation_lexeme> __thiscall survarium::short_jump_landing_state::selected_animations(class vostok::mutable_buffer &, class fastdelegate::FastDelegate<float __cdecl (float, float, unsigned int, unsigned int, unsigned int, float)> const &, struct survarium::weapon_animation_parameters const &)`
- `private: virtual struct stlp_std::pair<class vostok::animation::mixing::expression, class vostok::animation::mixing::animation_lexeme> __thiscall survarium::short_jump_start_state::selected_animations(class vostok::mutable_buffer &, class fastdelegate::FastDelegate<float __cdecl (float, float, unsigned int, unsigned int, unsigned int, float)> const &, struct survarium::weapon_animation_parameters const &)`
- `private: virtual struct vostok::network_core::udp_match_stats const & __thiscall survarium::match_client::get_stats(void) const`
- `private: virtual unsigned int __thiscall survarium::booby_trap_set_core_cook::get_derived_resource_size(void)`
- `private: virtual unsigned short __thiscall vostok::physics::old_bullet_character_controller::get_collision_group(void) const`
- `private: virtual void __thiscall survarium::booby_trap_core::hit(unsigned int, struct survarium::hit_initiator const *const, class vostok::collision::bone_collision_data const &, enum survarium::hit_type_enum, float, float, class survarium::bullet *const, unsigned short)`
- `private: virtual void __thiscall survarium::booby_trap_core::hit(unsigned int, struct survarium::hit_initiator const *const, unsigned int, enum survarium::hit_type_enum, float, float, class survarium::bullet *const, class vostok::math::float3const &, enum survarium::triangle_orientation, unsigned short)`
- `private: virtual void __thiscall survarium::booby_trap_core::tick(unsigned int, unsigned int)`
- `private: virtual void __thiscall survarium::booby_trap_set_core_cook::query_for_derived_resources(class vostok::resources::query_result_for_cook *, class survarium::booby_trap_set_core *, struct survarium::booby_trap_set_cook_data const &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>)`
- `private: virtual void __thiscall survarium::game_statistics_handler::deserialize(class vostok::network_core::buffer_reader &, unsigned int)`
- `private: virtual void __thiscall survarium::game_statistics_handler::on_artefact_took(unsigned char)`
- `private: virtual void __thiscall survarium::game_statistics_handler::on_limb_affect(unsigned int, unsigned char, enum survarium::affect_event_type_enum)`
- `private: virtual void __thiscall survarium::game_statistics_handler::on_medkit_action(class survarium::medkit const &, bool, unsigned char)`
- `private: virtual void __thiscall survarium::game_statistics_handler::on_pain_body_part_damage_received(unsigned char, unsigned char, float)`
- `private: virtual void __thiscall survarium::game_statistics_handler::on_pain_body_part_regenerated(unsigned char)`
- `private: virtual void __thiscall survarium::game_statistics_handler::on_player_damaged(unsigned int, unsigned char, enum survarium::player_stances_enum, unsigned char, float, enum survarium::profile_slot_enum, bool)`
- `private: virtual void __thiscall survarium::game_statistics_handler::on_player_killed(unsigned int, unsigned char, enum survarium::player_stances_enum, unsigned short, class vostok::math::float3const &, bool, unsigned char, class vostok::math::float3const &, bool, enum survarium::profile_slot_enum, bool, bool)`
- `private: virtual void __thiscall survarium::game_statistics_handler::serialize(class vostok::network_core::buffer_writer const &, unsigned int) const`
- `private: virtual void __thiscall survarium::medkit::set_inventory(class survarium::inventory *, enum survarium::profile_slot_enum)`
- `private: virtual void __thiscall survarium::player_logic_jump_state::set_user(class survarium::base_player &)`
- `private: virtual void __thiscall survarium::player_logic_sprint_state::deserialize(class vostok::network_core::buffer_reader &, class vostok::network_core::buffer_reader *)`
- `private: virtual void __thiscall survarium::portable_interactive_object_with_finger_correction::on_weapon_user_sprint(bool, bool)`
- `private: virtual void __thiscall survarium::weapon_cook::on_weapon_config_loaded(class vostok::resources::queries_result &)`
- `private: virtual void __thiscall survarium::weapon_cook::query_weapon_states(class vostok::resources::query_result_for_cook *const, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class survarium::weapon_core *)`
- `private: void * __thiscall vostok::memory::single_size_buffer_allocator<1364, class vostok::threading::multi_threading_policy>::allocate_impl(void)`
- `private: void __thiscall survarium::base_player::generate_hit_event(unsigned int, unsigned char, unsigned char, float, float, class survarium::bullet const *, bool)`
- `private: void __thiscall survarium::base_player::generate_killed_event(unsigned int, unsigned char, char const *, unsigned short, class survarium::bullet const *)`
- `private: void __thiscall survarium::chat_handler::on_message_typed(char const *, enum vostok::messaging::message_channel_enum)`
- `private: void __thiscall survarium::game_statistics_handler::emit_score_changed_event(unsigned char, short)`
- `private: void __thiscall survarium::game_statistics_handler::on_event(unsigned char, enum survarium::match_stats_events_dict_enum, unsigned short)`
- `private: void __thiscall survarium::game_statistics_handler::recalculate_scores(void)`
- `private: void __thiscall survarium::game_world_ui::initialize_quick_slots(void)`
- `private: void __thiscall survarium::game_world_ui::show_oxygene(bool)`
- `private: void __thiscall survarium::game_world_ui::update_back_slot(class vostok::resources::resource_ptr<class survarium::inventory_item, class vostok::resources::unmanaged_intrusive_base> const &)`
- `private: void __thiscall survarium::items_cook::create_item_and_finish_query(enum survarium::item_types_enum, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class vostok::resources::query_result_for_cook *)`
- `private: void __thiscall survarium::items_cook::on_config_ready(class vostok::resources::queries_result &, class vostok::resources::query_result_for_cook *)`
- `private: void __thiscall survarium::jump_logic::initialize_logic(void)`
- `private: void __thiscall survarium::jump_logic::initialize_weight_for_on_site_move_animation(void)`
- `private: void __thiscall survarium::lobby_menu::request_squad_status_from_server_impl(unsigned int, unsigned int)`
- `private: void __thiscall survarium::lobby_menu::request_status_from_server_impl(unsigned int, unsigned int)`
- `private: void __thiscall survarium::lobby_menu::update_status(void)`
- `private: void __thiscall survarium::medkit::load(class vostok::configs::binary_config_value)`
- `private: void __thiscall survarium::oxygen_tank::load(class vostok::configs::binary_config_value)`
- `private: void __thiscall survarium::player_logic_sprint_state::on_stamina_depleted(bool &)`
- `private: void __thiscall survarium::weapon_ammunition_cook::on_config_ready(class vostok::resources::queries_result &, class vostok::resources::query_result_for_cook *)`
- `private: void __thiscall survarium::weapon_cook::on_weapon_subresources_ready(class vostok::resources::queries_result &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class survarium::weapon_core *)`
- `private: void __thiscall survarium::weapon_core::update_recoil(unsigned int)`
- `private: void __thiscall survarium::weapon_core_cook::on_core_subresources_ready(class vostok::resources::queries_result &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class survarium::weapon_core *)`
- `private: void __thiscall vostok::animation::bone_matrices_computer::compute_skeleton_branch(class vostok::animation::skeleton_bone const &, class vostok::math::float4x4*, class vostok::math::float4x4const &, unsigned int const *, unsigned int const *, unsigned char) const`
- `private: void __thiscall vostok::animation::bone_matrices_computer::compute_skeleton_branch_local(class vostok::animation::skeleton_bone const &, class vostok::math::float4x4*, unsigned int const *, unsigned int const *, unsigned char) const`
- `private: void __thiscall vostok::animation::mixing::n_ary_tree_serializer::save_bits(unsigned char *const)`
- `private: void __thiscall vostok::collision::loose_oct_tree::render_iterate(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::debug::renderer &, struct vostok::collision::oct_node const *const, class vostok::math::float3const &, float)`
- `private: void __thiscall vostok::intrusive_ptr<class vostok::render::scene, class vostok::resources::unmanaged_resource, class vostok::threading::simple_lock>::dec(void)`
- `private: void __thiscall vostok::network::match_client::on_packet_received(unsigned char, class vostok::network_core::buffer_reader &)`
- `private: void __thiscall vostok::network::match_client_impl::on_packet_received(unsigned char, class vostok::network_core::buffer_reader &)`
- `private: void __thiscall vostok::network_core::udp_match_client::send_packet(class vostok::network_core::udp_match_packet &, class boost::function<void __cdecl (class vostok::network_core::udp_match_packet &, class boost::system::error_code const &, unsigned int)> const &)`
- `private: void __thiscall vostok::network_core::udp_match_connection::send(class vostok::network_core::udp_match_packet *, class boost::function<void __cdecl (class vostok::network_core::udp_match_packet &, class boost::function<void __cdecl (class vostok::network_core::udp_match_packet &, class boost::system::error_code const &, unsigned int)> const &)> const &)`
- `private: void __thiscall vostok::network_core::udp_match_connection::send_packets_list(class vostok::network_core::udp_match_packet *, unsigned int, class boost::function<void __cdecl (class vostok::network_core::udp_match_packet &, class boost::function<void __cdecl (class vostok::network_core::udp_match_packet &, class boost::system::error_code const &, unsigned int)> const &)> const &)`
- `private: void __thiscall vostok::network_core::udp_network_flow_emulator::add_packet(unsigned char *, unsigned int, class boost::asio::ip::basic_endpoint<class boost::asio::ip::udp> const &, unsigned int, unsigned int, struct vostok::network_core::socket_handler *const)`
- `private: void __thiscall vostok::physics::old_bullet_character_controller::player_step(float, class btVector3const &)`
- `private: void __thiscall vostok::physics::old_bullet_character_controller::setup_crouch_state(bool, bool)`
- `private: void __thiscall vostok::physics::old_bullet_character_controller::setup_shape_dim(class vostok::math::float2const &)`
- `private: void __thiscall vostok::physics::old_bullet_character_controller::step_down(float, bool, class btVector3const &, bool, class btVector3const &, float)`
- `private: void __thiscall vostok::physics::old_bullet_character_controller::step_forward_and_strafe(class btVector3const &)`
- `private: void __thiscall vostok::physics::old_bullet_character_controller::step_up(bool, class btVector3&)`
- `private: void __thiscall vostok::render::debug::renderer::draw_lines(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float4x4const &, class vostok::math::float3const &, float const *, unsigned int, unsigned short const *, unsigned int, class vostok::math::color const &, bool)`
- `private: void __thiscall vostok::render::debug::renderer::draw_primitive_solid(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float4x4const &, class vostok::math::float3const &, float const *, unsigned int, unsigned short const *, unsigned int, class vostok::math::color const &, bool)`
- `private: void __thiscall vostok::render::scene::render_lines(bool)`
- `private: void __thiscall vostok::render::scene::render_triangles(bool)`
- `private: void __thiscall vostok::render::stage_postprocess::process_blur(enum vostok::render::enum_render_target_index, enum vostok::render::enum_render_target_index, unsigned int)`
- `private: void __thiscall vostok::render::texture_cook_wrapper::query_converted_texture(class vostok::resources::query_result_for_cook *)`
- `protected: __thiscall survarium::artefact_base::artefact_base(struct survarium::artefact_base::config const &, class vostok::resources::resource_ptr<class survarium::game_effect_emitter, class vostok::resources::unmanaged_intrusive_base> const &)`
- `protected: __thiscall survarium::artefact_lifebone_core::artefact_lifebone_core(struct survarium::artefact_lifebone_core::config const &, class vostok::resources::resource_ptr<class survarium::game_effect_emitter, class vostok::resources::unmanaged_intrusive_base> const &)`
- `protected: __thiscall survarium::artefact_onyx_core::artefact_onyx_core(struct survarium::artefact_onyx_core::config const &, class vostok::resources::resource_ptr<class survarium::game_effect_emitter, class vostok::resources::unmanaged_intrusive_base> const &)`
- `protected: __thiscall survarium::artefact_spring_core::artefact_spring_core(struct survarium::artefact_spring_core::config const &, class vostok::resources::resource_ptr<class survarium::game_effect_emitter, class vostok::resources::unmanaged_intrusive_base> const &)`
- `protected: __thiscall survarium::booby_trap_set_core::booby_trap_set_core(struct vostok::physics::world &, class vostok::resources::resource_ptr<class survarium::game_material_manager, class vostok::resources::unmanaged_intrusive_base> const &)`
- `protected: __thiscall survarium::jump_logic_base_state::jump_logic_base_state(class survarium::jump_logic &)`
- `protected: static struct survarium::artefact_base::config __cdecl survarium::artefact_base::load_config(class vostok::configs::binary_config_value const &)`
- `protected: static struct survarium::artefact_rattle_core::config __cdecl survarium::artefact_rattle_core::load_config(class vostok::configs::binary_config_value const &)`
- `protected: virtual void __thiscall survarium::base_player::hit(unsigned int, struct survarium::hit_initiator const *const, class vostok::collision::bone_collision_data const &, enum survarium::hit_type_enum, float, float, class survarium::bullet *const, unsigned short)`
- `protected: virtual void __thiscall survarium::base_player::hit(unsigned int, struct survarium::hit_initiator const *const, unsigned int, enum survarium::hit_type_enum, float, float, class survarium::bullet *const, class vostok::math::float3const &, enum survarium::triangle_orientation, unsigned short)`
- `protected: virtual void __thiscall survarium::weapon_core_cook::on_weapon_config_loaded(class vostok::resources::queries_result &)`
- `protected: virtual void __thiscall survarium::weapon_core_cook::query_weapon_states(class vostok::resources::query_result_for_cook *const, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class survarium::weapon_core *)`
- `protected: void __thiscall survarium::booby_trap_set_core::load(class vostok::configs::binary_config_value const &, unsigned char)`
- `protected: void __thiscall survarium::lobby_menu::query_account_data(void)`
- `protected: void __thiscall survarium::lobby_menu::query_lobby_info(void)`
- `protected: void __thiscall survarium::weapon_core_cook::process_loading_weapon_core(class vostok::resources::query_result_for_cook *const, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class survarium::weapon_core *)`
- `public: __thiscall boost::_bi::bind_t<void, class boost::_mfi::mf5<void, class vostok::network::login_client_impl, unsigned int, class boost::function<void __cdecl (enum vostok::connection_error_types_enum)> const &, class boost::asio::ip::basic_resolver_iterator<class boost::asio::ip::tcp>, class boost::system::error_code const &, class boost::asio::ip::basic_resolver_iterator<class boost::asio::ip::tcp> >, class boost::_bi::list6<class boost::_bi::value<class vostok::network::login_client_impl *>, class boost::_bi::value<unsigned int>, class boost::_bi::value<class boost::function<void __cdecl (enum vostok::connection_error_types_enum)> >, class boost::_bi::value<class boost::asio::ip::basic_resolver_iterator<class boost::asio::ip::tcp> >, struct boost::arg<1>, struct boost::arg<2> > >::~bind_t<void, class boost::_mfi::mf5<void, class vostok::network::login_client_impl, unsigned int, class boost::function<void __cdecl (enum vostok::connection_error_types_enum)> const &, class boost::asio::ip::basic_resolver_iterator<class boost::asio::ip::tcp>, class boost::system::error_code const &, class boost::asio::ip::basic_resolver_iterator<class boost::asio::ip::tcp> >, class boost::_bi::list6<class boost::_bi::value<class vostok::network::login_client_impl *>, class boost::_bi::value<unsigned int>, class boost::_bi::value<class boost::function<void __cdecl (enum vostok::connection_error_types_enum)> >, class boost::_bi::value<class boost::asio::ip::basic_resolver_iterator<class boost::asio::ip::tcp> >, struct boost::arg<1>, struct boost::arg<2> > >(void)`
- `public: __thiscall character_step_down_sweep_test_callback::character_step_down_sweep_test_callback(class btCollisionWorld &, class btCollisionObject &, class btVector3const &, float, class btVector3const &, float, float)`
- `public: __thiscall survarium::artefact_lifebone_core::config::config(struct survarium::artefact_lifebone_core::config const &)`
- `public: __thiscall survarium::artefact_onyx_core::config::config(struct survarium::artefact_onyx_core::config const &)`
- `public: __thiscall survarium::game_statistics_handler::game_statistics_handler(void)`
- `public: __thiscall survarium::grenade_set_core::grenade_set_core(void)`
- `public: __thiscall survarium::hit_info::hit_info(unsigned int, unsigned char, unsigned char, char const *const, enum survarium::hit_type_enum, float, float, class survarium::bullet *const, class vostok::math::float3const &, enum survarium::triangle_orientation, unsigned short)`
- `public: __thiscall survarium::inventory_item::inventory_item(enum survarium::inventory_item::action_behaviour_type, bool)`
- `public: __thiscall survarium::items_dictionary::items_dictionary(class vostok::memory::base_allocator *, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: __thiscall survarium::jump_logic::jump_logic(class survarium::weapon_user_animations_selector &, class survarium::player_logic_jump_state &)`
- `public: __thiscall survarium::jump_logic::~jump_logic(void)`
- `public: __thiscall survarium::match_client::match_client(struct vostok::network::world &)`
- `public: __thiscall survarium::match_total_stats::match_total_stats(void)`
- `public: __thiscall survarium::player_stamina::player_stamina(struct survarium::stamina_base_parameters const &, class survarium::player_params_modifiers_container &)`
- `public: __thiscall survarium::player_stamina::~player_stamina(void)`
- `public: __thiscall survarium::portable_interactive_object::portable_interactive_object(class survarium::base_game_scene &, enum vostok::animation::hand_to_weapon_ik_solver::ik_locator_id_enum)`
- `public: __thiscall survarium::shared_statistics::~shared_statistics(void)`
- `public: __thiscall survarium::weapon::weapon(class survarium::base_game_scene &, unsigned int)`
- `public: __thiscall survarium::weapon_core::weapon_core(void)`
- `public: __thiscall survarium::weapon_sound_effect::sounds::~sounds(void)`
- `public: __thiscall vostok::animation::animation_player::animation_player(void)`
- `public: __thiscall vostok::animation::fingers_to_weapon_corrector::hand::hand(void)`
- `public: __thiscall vostok::buffer_vector<struct vostok::render::render_surface_instance *>::buffer_vector<struct vostok::render::render_surface_instance *>(void *, unsigned int, class vostok::buffer_vector<struct vostok::render::render_surface_instance *> const &)`
- `public: __thiscall vostok::buffer_vector<struct vostok::render::vertex_colored>::ctor<struct vostok::render::vertex_colored const *>(void *const, unsigned int, struct vostok::render::vertex_colored const *const &, struct vostok::render::vertex_colored const *const &)`
- `public: __thiscall vostok::fixed_vector<struct vostok::particle::render_particle_emitter_instance *, 1024>::fixed_vector<struct vostok::particle::render_particle_emitter_instance *, 1024>(class vostok::fixed_vector<struct vostok::particle::render_particle_emitter_instance *, 1024> const &)`
- `public: __thiscall vostok::fixed_vector<struct vostok::render::caster_model, 2048>::~fixed_vector<struct vostok::render::caster_model, 2048>(void)`
- `public: __thiscall vostok::fixed_vector<struct vostok::render::geometry_batch, 32>::~fixed_vector<struct vostok::render::geometry_batch, 32>(void)`
- `public: __thiscall vostok::fixed_vector<unsigned short, 1024>::ctor<unsigned short const *>(unsigned short const *const &, unsigned short const *const &)`
- `public: __thiscall vostok::intrusive_ptr<class vostok::render::res_pass, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>::intrusive_ptr<class vostok::render::res_pass, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>(class vostok::intrusive_ptr<class vostok::render::res_pass, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy> const &)`
- `public: __thiscall vostok::intrusive_ptr<class vostok::render::res_shader_technique, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>::~intrusive_ptr<class vostok::render::res_shader_technique, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>(void)`
- `public: __thiscall vostok::math::aabb_plane::aabb_plane(void)`
- `public: __thiscall vostok::memory::single_size_buffer_allocator<1364, class vostok::threading::multi_threading_policy>::single_size_buffer_allocator<1364, class vostok::threading::multi_threading_policy>(void *, unsigned int, class boost::function<void __cdecl (class vostok::memory::single_size_buffer_allocator<1364, class vostok::threading::multi_threading_policy> const &)> const &)`
- `public: __thiscall vostok::memory::single_size_buffer_allocator<76, class vostok::threading::single_threading_policy>::single_size_buffer_allocator<76, class vostok::threading::single_threading_policy>(void *, unsigned int, class boost::function<void __cdecl (class vostok::memory::single_size_buffer_allocator<76, class vostok::threading::single_threading_policy> const &)> const &)`
- `public: __thiscall vostok::network::connect_order::connect_order(class vostok::memory::base_allocator &, class vostok::memory::base_allocator &, char const *const, class vostok::intrusive_ptr<class vostok::network_core::udp_match_packets_allocator, class vostok::network_core::udp_match_packets_allocator, class vostok::threading::multi_threading_policy> const &, class vostok::network_core::udp_match_packet const *, class boost::function<void __cdecl (char const *, class vostok::network_core::udp_match_packet const *)> const &)`
- `public: __thiscall vostok::network::enqueue_order::enqueue_order(class vostok::memory::base_allocator &, class boost::function<void __cdecl (class vostok::network_core::udp_match_packet &)> const &, class vostok::network_core::udp_match_packet &, class vostok::intrusive_ptr<class vostok::network_core::udp_match_packets_allocator, class vostok::network_core::udp_match_packets_allocator, class vostok::threading::multi_threading_policy> const &, struct vostok::network_core::udp_match_stats const &, struct vostok::network_core::udp_match_stats &)`
- `public: __thiscall vostok::network::match_client::match_client(struct vostok::network::world &, struct vostok::network_core::udp_match_packets_orderer &, struct vostok::network_core::udp_network_flow_emulator_options const *)`
- `public: __thiscall vostok::network::receive_udp_response::receive_udp_response(class vostok::memory::base_allocator &, class boost::function<void __cdecl (class vostok::network_core::buffer_reader &)> const &, class vostok::intrusive_ptr<class vostok::network_core::udp_match_packets_allocator, class vostok::network_core::udp_match_packets_allocator, class vostok::threading::multi_threading_policy> const &, class vostok::network_core::udp_match_packet &, struct vostok::network_core::udp_match_stats const &, struct vostok::network_core::udp_match_stats &)`
- `public: __thiscall vostok::network_core::udp_match_client::udp_match_client(class boost::asio::io_service &, class vostok::memory::single_size_buffer_allocator<1364, class vostok::threading::multi_threading_policy> &, struct vostok::network_core::udp_match_packets_orderer &, class vostok::network_core::udp_network_flow_emulator *)`
- `public: __thiscall vostok::network_core::udp_match_connection::udp_match_connection(class vostok::memory::single_size_buffer_allocator<1364, class vostok::threading::multi_threading_policy> &, struct vostok::network_core::udp_match_packets_orderer &, unsigned int, unsigned int, char const *const)`
- `public: __thiscall vostok::network_core::udp_match_packets_allocator::udp_match_packets_allocator(class vostok::memory::base_allocator &, void *, unsigned int)`
- `public: __thiscall vostok::network_core::udp_match_stats::udp_match_stats(void)`
- `public: __thiscall vostok::network_core::udp_network_flow_emulator::udp_network_flow_emulator(class vostok::memory::base_allocator &, class vostok::memory::single_size_buffer_allocator<1364, class vostok::threading::multi_threading_policy> &, struct vostok::network_core::udp_network_flow_emulator_options const &)`
- `public: __thiscall vostok::physics::bt_character_controller::~bt_character_controller(void)`
- `public: __thiscall vostok::physics::character_controller_can_stand_tester::character_controller_can_stand_tester(class btVector3const &, class btCollisionObject &, class btCapsuleShape &, float)`
- `public: __thiscall vostok::physics::character_move_test_callback::character_move_test_callback(class btCollisionObject *, class btVector3const &, float)`
- `public: __thiscall vostok::physics::old_bullet_character_controller::old_bullet_character_controller(class vostok::math::float2const &, class vostok::math::float2const &, short, short, class vostok::memory::base_allocator &)`
- `public: __thiscall vostok::render::batched_vertex_source::batched_vertex_source(struct vostok::render::batched_vertex_source const &)`
- `public: __thiscall vostok::render::debug::draw_lines_command::ctor<2, 2>(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::engine::world &, class vostok::memory::base_allocator &, struct vostok::render::vertex_colored const (&)[2], unsigned short const (&)[2], bool)`
- `public: __thiscall vostok::render::debug::draw_lines_command::ctor<6, 6>(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::engine::world &, class vostok::memory::base_allocator &, struct vostok::render::vertex_colored const (&)[6], unsigned short const (&)[6], bool)`
- `public: __thiscall vostok::render::debug::draw_lines_command::ctor<class vostok::buffer_vector>(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::engine::world &, class vostok::memory::base_allocator &, class vostok::buffer_vector<struct vostok::render::vertex_colored> const &, class vostok::buffer_vector<unsigned short> const &, bool)`
- `public: __thiscall vostok::render::debug::draw_triangles_command::ctor<3, 3>(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::engine::world &, class vostok::memory::base_allocator &, struct vostok::render::vertex_colored const (&)[3], unsigned short const (&)[3], bool)`
- `public: __thiscall vostok::render::debug::draw_triangles_command::draw_triangles_command(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::engine::world &, class vostok::memory::base_allocator &, class vostok::buffer_vector<struct vostok::render::vertex_colored> const &, class vostok::buffer_vector<unsigned short> const &, bool)`
- `public: __thiscall vostok::render::game::renderer::~renderer(void)`
- `public: __thiscall vostok::resources::resource_ptr<class survarium::weapon_core, class vostok::resources::unmanaged_intrusive_base>::resource_ptr<class survarium::weapon_core, class vostok::resources::unmanaged_intrusive_base>(class survarium::weapon_core *)`
- `public: bool __thiscall delayed_packets_predicate::operator()(struct stlp_std::pair<class vostok::network_core::udp_match_packet *, struct stlp_std::pair<class boost::asio::ip::basic_endpoint<class boost::asio::ip::udp>, struct vostok::network_core::socket_handler *> > const &) const`
- `public: bool __thiscall survarium::dictionary_item::is_ammo(void) const`
- `public: bool __thiscall survarium::game_world_core::enter_match(unsigned char, unsigned int)`
- `public: bool __thiscall survarium::game_world_core::leave_match(unsigned char, unsigned int)`
- `public: bool __thiscall survarium::lobby_client::read_account_money(class vostok::network_core::buffer_reader &)`
- `public: bool __thiscall survarium::lobby_client::read_last_played_match_stats(class vostok::network_core::buffer_reader &)`
- `public: bool __thiscall survarium::lobby_client::read_new_profile(class vostok::network_core::buffer_reader &)`
- `public: bool __thiscall survarium::player_stamina::deplete(bool)`
- `public: bool __thiscall vostok::intrusive_list<struct survarium::player_stamina_subscriber, struct survarium::player_stamina_subscriber *, 32, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::contains_object(struct survarium::player_stamina_subscriber *)`
- `public: bool __thiscall vostok::intrusive_list<struct survarium::player_stamina_subscriber, struct survarium::player_stamina_subscriber *, 32, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::erase(struct survarium::player_stamina_subscriber *)`
- `public: bool __thiscall vostok::physics::bt_character_controller::can_stand(void) const`
- `public: bool __thiscall vostok::physics::bt_character_controller::is_activated(void) const`
- `public: bool __thiscall vostok::physics::bt_character_controller::is_in_jump(void) const`
- `public: bool __thiscall vostok::physics::bullet_character_controller::can_jump(void) const`
- `public: bool __thiscall vostok::physics::bullet_character_controller::on_ground(void) const`
- `public: bool __thiscall vostok::physics::old_bullet_character_controller::can_stand(void)`
- `public: bool __thiscall vostok::physics::old_bullet_character_controller::on_ground(void) const`
- `public: bool __thiscall vostok::physics::old_bullet_character_controller::sweep_test_key::operator==(struct vostok::physics::old_bullet_character_controller::sweep_test_key const &) const`
- `public: bool __thiscall vostok::variant<32>::try_get<unsigned short>(unsigned short &)`
- `public: class btTransform __thiscall vostok::physics::bullet_character_controller::get_transform(void)`
- `public: class btTransform __thiscall vostok::physics::old_bullet_character_controller::get_transform(void)`
- `public: class vostok::buffer_vector<float> & __thiscall vostok::buffer_vector<float>::operator=(class vostok::buffer_vector<float> const &)`
- `public: class vostok::fixed_vector<class vostok::render::buffer_slot, 128> & __thiscall vostok::fixed_vector<class vostok::render::buffer_slot, 128>::operator=(class vostok::fixed_vector<class vostok::render::buffer_slot, 128> const &)`
- `public: class vostok::fixed_vector<class vostok::render::texture_slot, 128> & __thiscall vostok::fixed_vector<class vostok::render::texture_slot, 128>::operator=(class vostok::fixed_vector<class vostok::render::texture_slot, 128> const &)`
- `public: class vostok::math::float4x4 __thiscall vostok::animation::animation_player::computed_bone_matrix(class vostok::animation::skeleton const &, class vostok::animation::skeleton_bone const &, void const *const, unsigned int const *const, class boost::function<class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> __cdecl (unsigned short)> const &) const`
- `public: class vostok::math::float4x4 __thiscall vostok::animation::bone_matrices_computer::computed_bone_matrix(class vostok::animation::skeleton_bone const &, unsigned int const *) const`
- `public: class vostok::render::res_texture * __thiscall vostok::render::resource_manager::on_texture_loaded_res_impl(unsigned char const *, unsigned int, char const *, unsigned int, bool)`
- `public: enum vostok::math::intersection __thiscall vostok::math::cuboid::test(class vostok::math::sphere const &) const`
- `public: float __thiscall survarium::jump_logic::get_preface_animation_timescale(float) const`
- `public: float __thiscall survarium::player_params_modifiers_container::get_modifier_value(enum survarium::player_params_modifiers_enum) const`
- `public: static struct survarium::dictionary_item * __cdecl vostok::memory::new_array_helper<struct survarium::dictionary_item>::call<class vostok::memory::base_allocator>(class vostok::memory::base_allocator &, unsigned int, char const *const, char const *const, unsigned int)`
- `public: static union vostok::memory::single_size_buffer_allocator<1364, class vostok::threading::multi_threading_policy>::node * __cdecl vostok::memory::multi_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<1364, class vostok::threading::multi_threading_policy>::node>::allocate(union vostok::memory::multi_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<1364, class vostok::threading::multi_threading_policy>::node>::free_list_type &)`
- `public: static union vostok::memory::single_size_buffer_allocator<76, class vostok::threading::single_threading_policy>::node * __cdecl vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<76, class vostok::threading::single_threading_policy>::node>::allocate(class vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<76, class vostok::threading::single_threading_policy>::node>::free_list_type &)`
- `public: static unsigned int __cdecl vostok::detail::type_to_int<unsigned short>::get(void)`
- `public: static void * __cdecl vostok::memory::new_helper<class vostok::render::debug::draw_lines_command>::call<class vostok::memory::base_allocator>(class vostok::memory::base_allocator &, char const *const, char const *const, unsigned int)`
- `public: static void * __cdecl vostok::memory::new_helper<class vostok::render::debug::draw_triangles_command>::call<class vostok::memory::base_allocator>(class vostok::memory::base_allocator &, char const *const, char const *const, unsigned int)`
- `public: static void __cdecl vostok::render::resource_intrusive_base::destroy<class vostok::render::res_shader_technique>(class vostok::render::res_shader_technique const *const)`
- `public: struct stlp_std::pair<class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> > __thiscall survarium::jump_logic::get_animation(enum survarium::jump_animation_parts) const`
- `public: struct stlp_std::pair<class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> > __thiscall survarium::jump_logic::get_animation(enum survarium::jump_type_enum, enum survarium::jump_animation_parts) const`
- `public: struct stlp_std::pair<class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> > __thiscall survarium::jump_logic::get_move_animation(void) const`
- `public: struct survarium::dictionary_item * __thiscall survarium::items_dictionary::item_by_id(unsigned int) const`
- `public: unsigned char __thiscall survarium::lobby_client::read_price_items(class vostok::network_core::buffer_reader &)`
- `public: unsigned int __thiscall survarium::lobby_client::squad_ready_count(void) const`
- `public: virtual __thiscall survarium::base_match_client::~base_match_client(void)`
- `public: virtual __thiscall survarium::game_statistics_handler::~game_statistics_handler(void)`
- `public: virtual __thiscall survarium::pistol_weapon_core_fire_state::~pistol_weapon_core_fire_state(void)`
- `public: virtual __thiscall survarium::weapon_core_fire_state::~weapon_core_fire_state(void)`
- `public: virtual __thiscall survarium::weapon_core_hide_state::~weapon_core_hide_state(void)`
- `public: virtual __thiscall survarium::weapon_core_reload_state::~weapon_core_reload_state(void)`
- `public: virtual __thiscall survarium::weapon_core_shotgun_reload_base_substate::~weapon_core_shotgun_reload_base_substate(void)`
- `public: virtual __thiscall vostok::render::debug::draw_triangles_command::~draw_triangles_command(void)`
- `public: virtual bool __thiscall vostok::render::stage_particles::is_effects_ready(void) const`
- `public: virtual class survarium::grenade_set_core * __thiscall survarium::grenade_set_cook::new_derived_resource(void *const)`
- `public: virtual class survarium::grenade_set_core * __thiscall survarium::grenade_set_core_cook::new_derived_resource(void *const)`
- `public: virtual float __thiscall vostok::physics::character_move_test_callback::addSingleResult(struct btCollisionWorld::LocalConvexResult &, bool)`
- `public: virtual unsigned int __thiscall survarium::grenade_set_cook::get_derived_resource_size(void)`
- `public: virtual unsigned int __thiscall survarium::grenade_set_core_cook::get_derived_resource_size(void)`
- `public: virtual void __thiscall survarium::booby_trap_set_core_cook::translate_query(class vostok::resources::query_result_for_cook &)`
- `public: virtual void __thiscall survarium::grenade_set_core_cook::query_for_derived_resources(class vostok::resources::query_result_for_cook *, class survarium::grenade_set_core *, struct survarium::grenade_set_cook_data const &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>)`
- `public: virtual void __thiscall survarium::grenade_set_core_cook::translate_query(class vostok::resources::query_result_for_cook &)`
- `public: virtual void __thiscall survarium::items_cook::translate_query(class vostok::resources::query_result_for_cook &)`
- `public: virtual void __thiscall survarium::jump_logic_base_state::set_user(class survarium::base_player &)`
- `public: virtual void __thiscall survarium::network_client::on_new_input(unsigned int)`
- `public: virtual void __thiscall survarium::weapon_ammunition_cook::translate_query(class vostok::resources::query_result_for_cook &)`
- `public: virtual void __thiscall survarium::weapon_core::set_inventory(class survarium::inventory *, enum survarium::profile_slot_enum)`
- `public: virtual void __thiscall vostok::collision::aabb_object::render(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::debug::renderer &) const`
- `public: virtual void __thiscall vostok::collision::box_geometry_instance::render(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::debug::renderer &) const`
- `public: virtual void __thiscall vostok::collision::box_geometry_instance::render(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::debug::renderer &, class vostok::math::float4x4const &) const`
- `public: virtual void __thiscall vostok::collision::box_geometry_instance::render(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::debug::renderer &, class vostok::math::float4x4const &, class vostok::math::color const &) const`
- `public: virtual void __thiscall vostok::collision::collision_object::render(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::debug::renderer &) const`
- `public: virtual void __thiscall vostok::collision::loose_oct_tree::render(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::debug::renderer &)`
- `public: virtual void __thiscall vostok::collision::sphere_geometry_instance::render(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::debug::renderer &, class vostok::math::float4x4const &) const`
- `public: virtual void __thiscall vostok::collision::sphere_geometry_instance::render(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::debug::renderer &, class vostok::math::float4x4const &, class vostok::math::color const &) const`
- `public: virtual void __thiscall vostok::collision::triangle_mesh_geometry::render(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::render::debug::renderer &, class vostok::math::float4x4const &) const`
- `public: virtual void __thiscall vostok::detail::concrete_type_helper<struct survarium::pvp_match_core_query_user_data>::copy(class vostok::mutable_buffer, class vostok::const_buffer)`
- `public: virtual void __thiscall vostok::network::send_queued_order::execute(void)`
- `public: virtual void __thiscall vostok::particle::particle_world::get_render_emitter_instances(class vostok::math::float4x4const &, class vostok::fixed_vector<struct vostok::particle::render_particle_emitter_instance *, 1024> &)`
- `public: virtual void __thiscall vostok::physics::old_bullet_character_controller::updateAction(class btCollisionWorld *, float)`
- `public: virtual void __thiscall vostok::render::debug::draw_lines_command::defer_execution(void)`
- `public: virtual void __thiscall vostok::render::debug::draw_lines_command::execute(void)`
- `public: virtual void __thiscall vostok::render::debug::draw_triangles_command::defer_execution(void)`
- `public: virtual void __thiscall vostok::render::debug::draw_triangles_command::execute(void)`
- `public: virtual void __thiscall vostok::render::stage_decals_accumulate::clear_surfaces(void)`
- `public: virtual void __thiscall vostok::sound::composite_sound::emit_sound_propagators(class vostok::sound::sound_instance_proxy_internal &, unsigned int, unsigned int) const`
- `public: virtual void __thiscall vostok::sound::single_sound::emit_sound_propagators(class vostok::sound::sound_instance_proxy_internal &, unsigned int, unsigned int) const`
- `public: virtual void __thiscall vostok::sound::sound_collection::emit_sound_propagators(class vostok::sound::sound_instance_proxy_internal &, unsigned int, unsigned int) const`
- `public: void __thiscall survarium::base_game_scene::hide_movie(class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> &)`
- `public: void __thiscall survarium::base_game_scene::show_movie(class vostok::resources::resource_ptr<struct survarium::flash_movie_resource, class vostok::resources::unmanaged_intrusive_base> &)`
- `public: void __thiscall survarium::base_player::jump(enum survarium::jump_type_enum)`
- `public: void __thiscall survarium::flash_value::SetElement(unsigned int, char const *)`
- `public: void __thiscall survarium::game_statistics_handler::clear(void)`
- `public: void __thiscall survarium::game_statistics_handler::finish_match(void)`
- `public: void __thiscall survarium::game_statistics_handler::start_match(class survarium::game_world_core &, struct survarium::match_options const &)`
- `public: void __thiscall survarium::game_world_core::discard_input(unsigned char, unsigned int)`
- `public: void __thiscall survarium::game_world_ui::on_enemy_hitted(unsigned int, bool, unsigned int, float)`
- `public: void __thiscall survarium::game_world_ui::on_player_killed(unsigned char, unsigned char, bool, unsigned short)`
- `public: void __thiscall survarium::grenade_set_core::load(class vostok::configs::binary_config_value const &, unsigned char)`
- `public: void __thiscall survarium::grenade_set_core_cook::finish_query(class vostok::resources::query_result_for_cook *, class survarium::grenade_set_core *)`
- `public: void __thiscall survarium::jump_logic::initialize(void)`
- `public: void __thiscall survarium::jump_logic::serialize(class vostok::network_core::buffer_writer const &, class vostok::network_core::buffer_writer const *) const`
- `public: void __thiscall survarium::lobby_client::buy_item(unsigned short, unsigned int, unsigned char, bool)`
- `public: void __thiscall survarium::lobby_client::ping_server(void)`
- `public: void __thiscall survarium::lobby_client::query_client_status(enum vostok::lobby::query_info_types)`
- `public: void __thiscall survarium::lobby_client::query_prices(unsigned int)`
- `public: void __thiscall survarium::lobby_client::query_profile_leveling(unsigned int)`
- `public: void __thiscall survarium::lobby_client::query_squad_info(void)`
- `public: void __thiscall survarium::lobby_menu::fill_match_statistic(struct survarium::match_total_stats const &, class vostok::vectora<struct survarium::player_results_item> const &)`
- `public: void __thiscall survarium::lobby_menu::fill_player_statistic(struct survarium::match_player_stats const &)`
- `public: void __thiscall survarium::lobby_menu::fill_squad_info(class vostok::fixed_vector<struct survarium::squad_member_item, 3> const &, bool)`
- `public: void __thiscall survarium::lobby_menu::on_operation_permitted_received(enum vostok::lobby::client::messages_enum)`
- `public: void __thiscall survarium::lobby_menu::on_price_items_arrived(unsigned char)`
- `public: void __thiscall survarium::lobby_menu::on_profile_arrived(unsigned char)`
- `public: void __thiscall survarium::lobby_menu::request_squad_status_from_server(unsigned int)`
- `public: void __thiscall survarium::lobby_menu::request_status_from_server(unsigned int)`
- `public: void __thiscall survarium::match_player_stats::deserialize(class vostok::network_core::buffer_reader &)`
- `public: void __thiscall survarium::match_total_stats::deserialize(class vostok::network_core::buffer_reader &)`
- `public: void __thiscall survarium::messaging_client::on_message_typed(char const *, char const *, enum vostok::messaging::message_channel_enum)`
- `public: void __thiscall survarium::packet_sender::on_player_input_changed(struct survarium::player_update &) const`
- `public: void __thiscall survarium::player_results_item::deserialize(class vostok::network_core::buffer_reader &)`
- `public: void __thiscall survarium::player_stamina::clear_subscribers(void)`
- `public: void __thiscall survarium::player_stamina::jump(void)`
- `public: void __thiscall survarium::player_stamina::subscribe_on_depletion(struct survarium::player_stamina_subscriber *const)`
- `public: void __thiscall survarium::portable_interactive_object::on_weapon_user_sprint(bool, bool)`
- `public: void __thiscall survarium::scheduler::register_for_update(struct survarium::scheduler::identifier *, class boost::function<void __cdecl (unsigned int, unsigned int)> const &, bool, unsigned int, unsigned int, unsigned int)`
- `public: void __thiscall survarium::teammate_cure_event_manager::serialize(class vostok::network_core::buffer_writer const &, unsigned int) const`
- `public: void __thiscall survarium::weapon_ammunition::load(class vostok::configs::binary_config_value const &)`
- `public: void __thiscall survarium::weapon_user_animations_selector::remove_animation_callback(char const *, void const *)`
- `public: void __thiscall survarium::weapon_user_animations_selector::remove_animation_callback(enum vostok::animation::reserved_channel_ids_enum, void const *)`
- `public: void __thiscall survarium::weapon_user_animations_selector::set_animation_callback(char const *, void const *, class boost::function<enum vostok::animation::callback_return_type_enum __cdecl (struct vostok::animation::animation_callback_params &)> const &)`
- `public: void __thiscall vostok::animation::animation_player::compute_bones_local_matrices(class vostok::animation::skeleton const &, class vostok::math::float4x4*, class vostok::math::float4x4*, void const *const, unsigned int *, class boost::function<class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> __cdecl (unsigned short)> const &, unsigned char) const`
- `public: void __thiscall vostok::animation::animation_player::compute_bones_matrices(class vostok::animation::skeleton const &, class vostok::math::float4x4*, class vostok::math::float4x4*, void const *const, unsigned int *, class boost::function<class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> __cdecl (unsigned short)> const &, unsigned char) const`
- `public: void __thiscall vostok::animation::bone_matrices_computer::compute_bones_local_matrices(class vostok::math::float4x4*, class vostok::math::float4x4*, unsigned int const *, unsigned char) const`
- `public: void __thiscall vostok::animation::bone_matrices_computer::compute_bones_matrices(class vostok::math::float4x4*, class vostok::math::float4x4*, unsigned int const *, unsigned char) const`
- `public: void __thiscall vostok::animation::fingers_to_weapon_corrector::activate_hand(enum vostok::animation::fingers_to_weapon_corrector::hands_enum, bool, bool, enum vostok::animation::fingers_to_weapon_corrector::fingers_locator_set_id_enum, unsigned int)`
- `public: void __thiscall vostok::animation::hand_to_weapon_ik_solver::activate_hand(enum vostok::animation::hand_to_weapon_ik_solver::hands_enum, bool, bool, enum vostok::animation::hand_to_weapon_ik_solver::ik_locator_id_enum, unsigned int)`
- `public: void __thiscall vostok::animation::legs_ik_drawer::draw_leg(class vostok::math::float4x4const &, class vostok::math::float4x4const &, class vostok::math::float4x4const &, class vostok::math::float4x4const &, class vostok::math::color const &, class vostok::math::color const &, class vostok::math::color const &, class vostok::math::color const &, float)`
- `public: void __thiscall vostok::animation::mixing::n_ary_tree::compute_bones_local_matrices(void const *, class vostok::animation::skeleton const &, class vostok::math::float4x4*const, class vostok::math::float4x4*const, unsigned int *, class boost::function<class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> __cdecl (unsigned short)> const &, unsigned char) const`
- `public: void __thiscall vostok::animation::mixing::n_ary_tree::compute_bones_matrices(void const *, class vostok::animation::skeleton const &, class vostok::math::float4x4*const, class vostok::math::float4x4*const, unsigned int *, class boost::function<class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> __cdecl (unsigned short)> const &, unsigned char) const`
- `public: void __thiscall vostok::buffer_vector<class vostok::physics::loose_ptr<class vostok::physics::base_physics_object, class vostok::physics::loose_ptr_data, class vostok::threading::multi_threading_policy> >::assign<class vostok::physics::loose_ptr<class vostok::physics::base_physics_object, class vostok::physics::loose_ptr_data, class vostok::threading::multi_threading_policy> *>(class vostok::physics::loose_ptr<class vostok::physics::base_physics_object, class vostok::physics::loose_ptr_data, class vostok::threading::multi_threading_policy> *, class vostok::physics::loose_ptr<class vostok::physics::base_physics_object, class vostok::physics::loose_ptr_data, class vostok::threading::multi_threading_policy> *const &)`
- `public: void __thiscall vostok::buffer_vector<class vostok::render::buffer_slot>::assign<class vostok::render::buffer_slot const *>(class vostok::render::buffer_slot const *, class vostok::render::buffer_slot const *const &)`
- `public: void __thiscall vostok::buffer_vector<class vostok::render::texture_slot>::assign<class vostok::render::texture_slot const *>(class vostok::render::texture_slot const *, class vostok::render::texture_slot const *const &)`
- `public: void __thiscall vostok::buffer_vector<struct stlp_std::pair<class vostok::network_core::udp_match_packet *, struct stlp_std::pair<class boost::asio::ip::basic_endpoint<class boost::asio::ip::udp>, struct vostok::network_core::socket_handler *> > >::push_back(struct stlp_std::pair<class vostok::network_core::udp_match_packet *, struct stlp_std::pair<class boost::asio::ip::basic_endpoint<class boost::asio::ip::udp>, struct vostok::network_core::socket_handler *> > const &)`
- `public: void __thiscall vostok::buffer_vector<struct survarium::squad_member_item>::resize(unsigned int)`
- `public: void __thiscall vostok::buffer_vector<struct vostok::physics::old_bullet_character_controller::sweep_test_cache_item *>::resize(unsigned int)`
- `public: void __thiscall vostok::buffer_vector<struct vostok::render::vertex_colored>::insert<struct vostok::render::vertex_colored const *>(struct vostok::render::vertex_colored *const &, struct vostok::render::vertex_colored const *, struct vostok::render::vertex_colored const *const &)`
- `public: void __thiscall vostok::buffer_vector<unsigned int>::assign<unsigned int const *>(unsigned int const *, unsigned int const *const &)`
- `public: void __thiscall vostok::buffer_vector<unsigned short>::assign<unsigned short const *>(unsigned short const *, unsigned short const *const &)`
- `public: void __thiscall vostok::network_core::process_packet_predicate::operator()(unsigned char, class vostok::network_core::buffer_reader &) const`
- `public: void __thiscall vostok::network_core::udp_match_client::enqueue(unsigned char, class vostok::network_core::buffer_reader &)`
- `public: void __thiscall vostok::network_core::udp_match_connection::connect(class vostok::network_core::udp_match_packet *)`
- `public: void __thiscall vostok::network_core::udp_match_connection::enqueue(unsigned char, class vostok::network_core::buffer_reader &)`
- `public: void __thiscall vostok::network_core::udp_match_connection::process_incoming_packet<class vostok::network_core::process_packet_predicate>(class vostok::network_core::buffer_reader &, class vostok::network_core::process_packet_predicate const &)`
- `public: void __thiscall vostok::network_core::udp_match_connection::send_queued_packets(unsigned int, class boost::function<void __cdecl (class vostok::network_core::udp_match_packet &, class boost::function<void __cdecl (class vostok::network_core::udp_match_packet &, class boost::system::error_code const &, unsigned int)> const &)> const &)`
- `public: void __thiscall vostok::network_core::udp_network_flow_emulator::tick(unsigned int, class boost::function<void __cdecl (class vostok::network_core::buffer_reader &, class boost::asio::ip::basic_endpoint<class boost::asio::ip::udp> const &, struct vostok::network_core::socket_handler *)> const &)`
- `public: void __thiscall vostok::physics::bt_character_controller::initialize(class vostok::math::float4x4const &, unsigned int, unsigned char)`
- `public: void __thiscall vostok::physics::bt_character_controller::set_crouch(bool)`
- `public: void __thiscall vostok::physics::bt_character_controller::set_landing_callback(class boost::function<void __cdecl (float)> const &, float)`
- `public: void __thiscall vostok::physics::bullet_character_controller::end_jump(void)`
- `public: void __thiscall vostok::physics::old_bullet_character_controller::deserialize(class vostok::network_core::buffer_reader &, unsigned int)`
- `public: void __thiscall vostok::physics::old_bullet_character_controller::insert(class btDynamicsWorld *)`
- `public: void __thiscall vostok::physics::old_bullet_character_controller::remove(class btDynamicsWorld *)`
- `public: void __thiscall vostok::physics::old_bullet_character_controller::serialize(class vostok::network_core::buffer_writer const &, unsigned int) const`
- `public: void __thiscall vostok::physics::old_bullet_character_controller::set_desired_walk_vector(class btVector3const &)`
- `public: void __thiscall vostok::physics::old_bullet_character_controller::set_transform(class btTransform const &)`
- `public: void __thiscall vostok::render::backend::flush_rt_shader_resources(void)`
- `public: void __thiscall vostok::render::debug::renderer::draw_aabb(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float3const &, class vostok::math::float3const &, class vostok::math::color const &, bool)`
- `public: void __thiscall vostok::render::debug::renderer::draw_cross(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float3const &, float, class vostok::math::color const &, bool)`
- `public: void __thiscall vostok::render::debug::renderer::draw_cube(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float4x4const &, class vostok::math::float3const &, class vostok::math::color const &, bool)`
- `public: void __thiscall vostok::render::debug::renderer::draw_cube_solid(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float4x4const &, class vostok::math::float3const &, class vostok::math::color const &, bool)`
- `public: void __thiscall vostok::render::debug::renderer::draw_cylinder(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float4x4const &, class vostok::math::float3const &, class vostok::math::color const &, bool)`
- `public: void __thiscall vostok::render::debug::renderer::draw_line(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float3const &, class vostok::math::float3const &, class vostok::math::color const &, bool)`
- `public: void __thiscall vostok::render::debug::renderer::draw_line_capsule(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float4x4const &, class vostok::math::float3const &, class vostok::math::color const &, bool)`
- `public: void __thiscall vostok::render::debug::renderer::draw_line_hemisphere(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float4x4const &, class vostok::math::float3const &, bool, class vostok::math::color const &, bool)`
- `public: void __thiscall vostok::render::debug::renderer::draw_lines(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float4x4const &, float const *, unsigned int, unsigned short const *, unsigned int, class vostok::math::color const &, bool)`
- `public: void __thiscall vostok::render::debug::renderer::draw_origin(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float4x4const &, float, bool)`
- `public: void __thiscall vostok::render::debug::renderer::draw_solid_capsule(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float4x4const &, class vostok::math::float3const &, class vostok::math::color const &, bool)`
- `public: void __thiscall vostok::render::debug::renderer::draw_sphere(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float4x4const &, float const &, class vostok::math::color const &, bool)`
- `public: void __thiscall vostok::render::debug::renderer::draw_sphere_solid(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float3const &, float const &, class vostok::math::color const &, bool)`
- `public: void __thiscall vostok::render::debug::renderer::draw_triangle(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, struct vostok::render::vertex_colored const (&)[3], bool)`
- `public: void __thiscall vostok::render::hw_hiz_point_list::render(unsigned int)`
- `public: void __thiscall vostok::render::renderer::downsample(class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, class vostok::intrusive_ptr<class vostok::render::res_texture, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>)`
- `public: void __thiscall vostok::render::scene::draw_lines(class vostok::buffer_vector<struct vostok::render::vertex_colored> const &, class vostok::buffer_vector<unsigned short> const &)`
- `public: void __thiscall vostok::render::scene::draw_triangles(class vostok::buffer_vector<struct vostok::render::vertex_colored> const &, class vostok::buffer_vector<unsigned short> const &)`
- `public: void __thiscall vostok::render::scene::flush(class boost::function<void __cdecl (bool)> const &, bool, bool)`
- `public: void __thiscall vostok::render::stage_screen_space_reflections::render_models_with_reflections(class vostok::buffer_vector<struct vostok::render::render_surface_instance *> const &, bool)`
- `public: void __thiscall vostok::render::stage_shadow_direct::prepare_visibile_objects(class vostok::fixed_vector<struct vostok::render::caster_model, 2048> *, class vostok::memory::base_allocator *, class vostok::math::float3const &, unsigned int, unsigned int, unsigned int)`
- `public: void __thiscall vostok::render::stage_shadow_direct::render_models(class vostok::fixed_vector<struct vostok::render::caster_model, 2048> &, class vostok::math::float3const &, unsigned int, bool)`
- `unsigned char __cdecl survarium::calculate_profile_icon(struct survarium::player_profile const &, class survarium::items_dictionary const &)`
- `void __cdecl survarium::setup_damage_model_from_profile(class survarium::damage_model &, struct survarium::player_profile const &, class survarium::items_dictionary const &)`
- `void __cdecl vostok::memory::delete_helper<class vostok::memory::base_allocator, class vostok::animation::legs_ik_drawer>(class vostok::memory::base_allocator &, class vostok::animation::legs_ik_drawer *&, char const *const, char const *const, unsigned int)`
- `void __cdecl vostok::memory::zero(void *, unsigned int)`
- `void __cdecl vostok::network_core::delete_udp_match_packet(class vostok::memory::single_size_buffer_allocator<1364, class vostok::threading::multi_threading_policy> &, class vostok::network_core::udp_match_packet *&)`
- `void __cdecl vostok::render::defer_execution(class vostok::render::base_command &, class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &)`
- `vostok::physics::getNormalizedVector`
- `vostok::physics::set_max_slope_angle`
- `vostok::render::parse_resolution`
