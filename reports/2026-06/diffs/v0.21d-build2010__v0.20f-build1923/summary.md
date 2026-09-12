# v0.21d-build2010 -> v0.20f-build1923

Lists below: **hand-written engine** (`vostok/*`, compiler-generated excluded). Full breakdown:

| bucket | engine | generated | third-party |
| --- | ---: | ---: | ---: |
| identical | **6942** | 1526 | 6216 |
| changed | **2487** | 12 | 201 |
| new / rewritten | **598** | 225 | 580 |
| units removed | **49** | - | 16 |

## Most-changed engine functions (50 shown)

| match % | unit | function |
| ---: | --- | --- |
| 0.68 | vostok/game_core/sources/items_dictionary_cook.cpp | `private: void __thiscall survarium::items_dictionary_cook::on_configs_loaded(class vostok::resources::queries_result &)` |
| 2.60 | vostok/game_core/sources/grenade_set_core_cook.cpp | `private: void __thiscall survarium::grenade_set_core_cook::on_config_ready(class vostok::resources::queries_result &, struct survarium::grenade_set_cook_data)` |
| 2.76 | vostok/game/sources/game_world_input.cpp | `public: virtual bool __thiscall survarium::game_world::on_keyboard_action(struct vostok::input::world *, enum vostok::input::enum_keyboard, enum vostok::input::enum_keyboard_action)` |
| 4.21 | vostok/network/sources/login_client_impl_ping.cpp | `private: void __thiscall vostok::network::login_client_impl::on_ping_sent(unsigned int, class boost::system::error_code const &, unsigned int)` |
| 4.53 | vostok/render/core/dx11/sources/res_render_output.cpp | `public: __thiscall vostok::render::res_render_output::res_render_output(struct HWND__*, bool)` |
| 8.14 | vostok/physics/sources/character_controller_step_down_tester.cpp | `private: class btVector3 __thiscall character_step_down_sweep_test_callback::get_normal_via_ray_test(struct btCollisionWorld::LocalConvexResult &, class btVector3const &) const` |
| 8.19 | vostok/render/engine/sources/renderer.cpp | `public: virtual void __thiscall vostok::render::effect_downsample::compile(class vostok::render::effect_compiler &, class vostok::configs::binary_config_value const &, struct vostok::render::surface_effect_parameters const &)` |
| 8.68 | vostok/game/sources/game_world_ui.cpp | `public: void __thiscall survarium::game_world_ui::clear_player(void)` |
| 8.92 | vostok/network/sources/enqueue_order.h | `public: virtual void __thiscall vostok::network::enqueue_order::execute(void)` |
| 9.64 | vostok/game/sources/lobby_client.cpp | `public: bool __thiscall survarium::lobby_client::read_player_match_stats(class vostok::network_core::buffer_reader &)` |
| 10.68 | vostok/game_core/sources/player_shared_statistics.cpp | `public: __thiscall survarium::player_shared_statistics::player_shared_statistics(void)` |
| 11.04 | vostok/game/sources/lobby_menu_ui.cpp | `public: void __thiscall survarium::lobby_menu::add_quest(struct survarium::quest_instance const &)` |
| 11.38 | vostok/game/sources/network_client_processing.cpp | `private: void __thiscall survarium::network_client::process_player_entered_match(class vostok::network_core::buffer_reader &)` |
| 12.45 | vostok/render/engine/sources/stage_ambient_lighting.cpp | `public: virtual void __thiscall vostok::render::stage_ambient_lighting::clear_surfaces(void)` |
| 13.88 | vostok/animation/sources/fingers_to_weapon_corrector.cpp | `public: void __thiscall vostok::animation::fingers_to_weapon_corrector::activate_hand(enum vostok::animation::fingers_to_weapon_corrector::hands_enum, enum vostok::animation::finger_corrector_animation_events_type_enum, unsigned int)` |
| 15.25 | vostok/input/sources/input_world.cpp | `public: virtual void __thiscall vostok::input::input_world::add_handler(struct vostok::input::handler &)` |
| 15.63 | vostok/network/sources/login_client_impl_sign_in.cpp | `private: void __thiscall vostok::network::login_client_impl::on_sign_in_answer_received(class boost::function<void __cdecl (enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::login::server::messages_enum)> const &, class boost::system::error_code const &, unsigned int)` |
| 16.08 | vostok/game_core/sources/weapon_core.cpp | `public: virtual void __thiscall survarium::weapon_core::set_next_ammo_type(void)` |
| 16.94 | vostok/network_core/sources/udp_match_client.cpp | `private: void __thiscall vostok::network_core::udp_match_client::handle_receive(class boost::system::error_code const &, unsigned int)` |
| 17.85 | vostok/game_core/sources/weapon_core.cpp | `private: float __thiscall survarium::weapon_core::vertical_recoil_value(unsigned int) const` |
| 19.38 | vostok/game_core/sources/weapon_core_throw_grenade_substate.cpp | `public: virtual void __thiscall survarium::weapon_core_throw_grenade_pull_substate::initialize(void)` |
| 20.00 | vostok/game_core/sources/artefact_container_core.cpp | `public: virtual void __thiscall survarium::artefact_container_core::use_finalize(struct survarium::usable_object_user_data *)` |
| 20.72 | vostok/survarium/game_module_proxy.cpp | `private: virtual struct vostok::engine_user::world * __thiscall survarium::game_module_proxy::create_world(struct vostok::engine_user::engine &, class vostok::render::world &, struct vostok::sound::world &, struct vostok::network::world &)` |
| 21.09 | vostok/game/sources/lobby_menu.cpp | `public: void __thiscall survarium::lobby_menu::on_client_status_received(enum vostok::lobby::query_info_types)` |
| 23.65 | vostok/game_core/sources/player_logic_jump_state.cpp | `private: virtual struct stlp_std::pair<class vostok::animation::mixing::expression, class vostok::animation::mixing::animation_lexeme> __thiscall survarium::player_logic_jump_state::selected_animations(class vostok::mutable_buffer &, struct survarium::weapon_animation_parameters const &) const` |
| 24.25 | vostok/network_core/sources/udp_match_client.cpp | `public: void __thiscall vostok::network_core::udp_match_client::set_connection_ports(unsigned char, unsigned int, unsigned short, unsigned short)` |
| 24.72 | vostok/game_core/sources/base_player.cpp | `protected: void __thiscall survarium::base_player::deactivate_physics(void)` |
| 26.27 | vostok/game_core/sources/shared_statistics.cpp | `private: void __thiscall survarium::shared_statistics::on_event(struct survarium::player_shared_statistics &, enum survarium::match_stats_events_dict_enum, unsigned short)` |
| 26.33 | vostok/game_core/sources/weapon_core_cook.cpp | `public: virtual void __thiscall survarium::weapon_core_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 26.55 | vostok/game_core/sources/shared_statistics.cpp | `public: void __thiscall survarium::shared_statistics::serialize(class vostok::network_core::buffer_writer const &, unsigned int) const` |
| 26.73 | vostok/render/engine/sources/stage_rain.cpp | `public: virtual void __thiscall vostok::render::stage_rain::execute(void)` |
| 27.21 | vostok/game/sources/object_volume_fog.cpp | `public: virtual void __thiscall survarium::object_volume_fog::insert(void)` |
| 27.33 | vostok/game_core/sources/player_profile.cpp | `private: void __thiscall survarium::player_profile::deserialize_slots(class vostok::network_core::buffer_reader &)` |
| 27.64 | vostok/network_core/sources/udp_match_client.cpp | `public: void __thiscall vostok::network_core::udp_match_client::connect(char const *, unsigned short, class vostok::network_core::udp_match_packet *, unsigned int)` |
| 27.67 | vostok/render/engine/sources/stage_lights.cpp | `private: bool __thiscall vostok::render::stage_lights::has_models_for_shadow_pass(class vostok::render::light *, class vostok::buffer_vector<struct vostok::render::render_surface_instance *> const &)` |
| 28.12 | vostok/resources_resource_ptr_inline.h | `class vostok::resources::resource_ptr<class survarium::weapon_core, class vostok::resources::unmanaged_intrusive_base> __cdecl vostok::static_cast_resource_ptr<class vostok::resources::resource_ptr<class survarium::weapon_core, class vostok::resources::unmanaged_intrusive_base>, class survarium::inventory_item, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::resource_ptr<class survarium::inventory_item, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 28.58 | vostok/render/core/sources/event_query.cpp | `public: __thiscall vostok::render::event_query::event_query(void)` |
| 29.13 | vostok/game_core/sources/items_dictionary_cook.cpp | `public: virtual __thiscall survarium::items_dictionary::~items_dictionary(void)` |
| 29.82 | vostok/network_core/sources/udp_match_connection.cpp | `public: void __thiscall vostok::network_core::udp_match_connection::enqueue(class vostok::network_core::udp_match_packet *)` |
| 30.00 | vostok/game/sources/match_client.h | `private: virtual class vostok::network_core::udp_match_packet * __thiscall survarium::match_client::new_packet(enum vostok::match::client::messages_enum)` |
| 30.96 | vostok/game_core/sources/oxygen_tank.cpp | `public: virtual void __thiscall survarium::oxygen_tank::get_item_props(struct survarium::inventory_item_props &) const` |
| 31.54 | vostok/game_core/sources/base_player.cpp | `public: void __thiscall survarium::base_player::stand_up(void)` |
| 32.55 | vostok/game/sources/lobby_menu_ui.cpp | `protected: void __thiscall survarium::lobby_menu::create_player_params(struct survarium::flash_value &, class survarium::player_params_modifiers_container const &)` |
| 33.00 | vostok/render/core/dx11/sources/device.cpp | `private: void __thiscall vostok::render::device::create_d3d(void)` |
| 33.35 | vostok/game_core/sources/items_dictionary_cook.cpp | `private: void __thiscall survarium::items_dictionary_cook::on_subresources_loaded(class vostok::resources::queries_result &, class survarium::items_dictionary *)` |
| 33.43 | vostok/game/sources/game.cpp | `private: virtual void __thiscall survarium::game::on_alttab(bool)` |
| 34.33 | vostok/game_core/sources/player_params_modifiers_container.cpp | `public: float __thiscall survarium::player_params_modifiers_container::apply_modifier(enum survarium::player_params_modifiers_enum, float, float) const` |
| 35.61 | vostok/network_core/sources/udp_match_client.cpp | `private: void __thiscall vostok::network_core::udp_match_client::process_incoming_packet(class vostok::network_core::buffer_reader &, class boost::asio::ip::basic_endpoint<class boost::asio::ip::udp> const &, struct vostok::network_core::socket_handler *)` |
| 35.90 | vostok/render/core/dx11/effect_compiler.h | `public: class vostok::fixed_vector<struct vostok::render::effect_compiler::shader_cache_info, 32> const __thiscall vostok::render::effect_compiler::get_cached_shaders_info(void) const` |
| 35.96 | vostok/network/sources/send_queued_order.h | `public: virtual __thiscall vostok::network::send_queued_order::~send_queued_order(void)` |

## Engine units in base but gone in target

- vostok/core/engine.h
- vostok/core/sources/configs_binary_config_creation.cpp
- vostok/core/sources/configs_binary_config_modification.cpp
- vostok/core/sources/memory_stream.cpp
- vostok/core/sources/string_functions_win.cpp
- vostok/debug/macros_inline.h
- vostok/game/game_quest_progress_calculator.cpp
- vostok/game/sources/base_game_statistics_handler.cpp
- vostok/game/sources/base_local_network_client.cpp
- vostok/game/sources/base_local_network_client.h
- vostok/game/sources/base_view_network_client.cpp
- vostok/game/sources/base_view_network_client.h
- vostok/game/sources/network_client_draw_match_stats.cpp
- vostok/game/sources/network_stats.h
- vostok/game/sources/network_stats_orders_channel.cpp
- vostok/game/sources/network_stats_packets.cpp
- vostok/game/sources/network_stats_packets_sequence.cpp
- vostok/game/sources/network_stats_ports.cpp
- vostok/game/sources/network_stats_received_messages.cpp
- vostok/game/sources/network_stats_rejected_messages.cpp
- vostok/game/sources/network_stats_seconds.cpp
- vostok/game/sources/network_stats_sent_messages.cpp
- vostok/game/sources/replay_network_client.cpp
- vostok/game/sources/replay_network_client.h
- vostok/game/sources/swear_filter.cpp
- vostok/game/sources/swear_filter_config_cook.cpp
- vostok/game/sources/swear_filter_cook.cpp
- vostok/game_core/gather_victory_items_rule_cook.h
- vostok/game_core/new_player_damage_protector.cpp
- vostok/game_core/sources/armor.cpp
- vostok/game_core/sources/game_core_entry_point.cpp
- vostok/game_core/sources/interactive_object.cpp
- vostok/game_core/sources/item_affinities.cpp
- vostok/game_core/sources/item_config_cook.cpp
- vostok/game_core/sources/lobby_player_profile.cpp
- vostok/game_core/sources/match_time_vi_spawn_rule.cpp
- vostok/game_core/sources/match_time_vi_spawn_rule_cook.cpp
- vostok/game_core/sources/match_time_vi_spawn_rule_cook.h
- vostok/game_core/sources/player_logic_jump_state.h
- vostok/game_core/tickable_object.h
- vostok/network_core/sources/udp_match_stats.cpp
- vostok/physics/sources/character_controller_impassable_slide_down_tester.cpp
- vostok/render/engine/sources/effect_probe_brdf.cpp
- vostok/render/engine/sources/effect_ssr.cpp
- vostok/render/engine/sources/effect_ssr_mask.cpp
- vostok/render/engine/sources/particle_rain_drops_geometry.cpp
- vostok/render/engine/sources/stage_shadow_direct.h
- vostok/render/facade/base_command.h
- vostok/render/facade/sources/defer_execution.cpp
