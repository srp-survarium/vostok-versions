# v0.20f-build1923 -> v0.21d-build2010

Lists below: **hand-written engine** (`vostok/*`, compiler-generated excluded). Full breakdown:

| bucket | engine | generated | third-party |
| --- | ---: | ---: | ---: |
| identical | **6941** | 1526 | 6216 |
| changed | **2516** | 12 | 202 |
| new / rewritten | **815** | 299 | 890 |
| units removed | **19** | - | 2 |

## Most-changed engine functions (50 shown)

| match % | unit | function |
| ---: | --- | --- |
| 2.22 | vostok/game/sources/player_tick.cpp | `public: virtual void __thiscall survarium::player::tick(unsigned int)` |
| 3.22 | vostok/network/sources/match_client_impl.h | `public: void __thiscall vostok::network::match_client_impl::set_connection_ports(unsigned char, unsigned int, unsigned short, unsigned short)` |
| 3.49 | vostok/game_core/sources/jump_logic_state_landing.cpp | `private: virtual void __thiscall survarium::jump_logic_state_landing::initialize(void)` |
| 4.60 | vostok/game_core/sources/player_logic_sprint_state.cpp | `private: virtual void __thiscall survarium::player_logic_sprint_state::finalize(void)` |
| 5.71 | vostok/game_core/artefact_core_cook.h | `private: virtual void __thiscall survarium::artefact_core_cook::query_for_derived_resources(class vostok::resources::query_result_for_cook &, class survarium::artefact_base &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 7.77 | vostok/game_core/sources/base_player.cpp | `public: void __thiscall survarium::base_player::end_jump(void)` |
| 8.44 | vostok/game/sources/game_statistics_handler.cpp | `private: virtual void __thiscall survarium::game_statistics_handler::on_victory_item_event(unsigned char, enum survarium::victory_item_event_type, class survarium::victory_item_core const &)` |
| 9.05 | vostok/render/core/dx11/sources/texture_cook_wrapper.cpp | `public: virtual void __thiscall vostok::render::texture_cook_wrapper::translate_query(class vostok::resources::query_result_for_cook &)` |
| 9.79 | vostok/render/core/dx11/sources/resource_manager.cpp | `public: void __thiscall vostok::render::resource_manager::initialize_texture_pools(void)` |
| 11.11 | vostok/render/engine/sources/stage_decals_accumulate.cpp | `public: virtual void __thiscall vostok::render::stage_decals_accumulate::execute(void)` |
| 11.46 | vostok/render/engine/sources/stage_rain.cpp | `public: __thiscall vostok::render::stage_rain::stage_rain(class vostok::render::renderer *, class vostok::render::renderer_context *)` |
| 11.76 | vostok/game_core/sources/items_dictionary_cook.cpp | `public: virtual void __thiscall survarium::items_dictionary_cook::delete_resource(class vostok::resources::resource_base *)` |
| 12.01 | vostok/input/sources/input_world.cpp | `public: virtual void __thiscall vostok::input::input_world::add_handler(struct vostok::input::handler &)` |
| 14.48 | vostok/game_core/sources/weapon_user_animations_selector.cpp | `public: float __thiscall survarium::weapon_user_animations_selector::look_time_factor(void) const` |
| 15.05 | vostok/render/core/dx11/backend_inline.h | `public: void __thiscall vostok::render::backend::flush_rt_views(void)` |
| 15.15 | vostok/game_core/sources/player_logic_jump_state.cpp | `private: virtual void __thiscall survarium::player_logic_jump_state::initialize(void)` |
| 16.00 | vostok/game/sources/match_client.h | `private: virtual class vostok::network_core::udp_match_packet * __thiscall survarium::match_client::new_packet(enum vostok::match::client::messages_enum)` |
| 16.75 | vostok/game/sources/player.cpp | `public: virtual void __thiscall survarium::player::serialize(class vostok::network_core::buffer_writer const &, class vostok::network_core::buffer_writer const *, unsigned char (&)[32768], class vostok::intrusive_ptr<class vostok::animation::mixing::n_ary_tree_intrusive_base, class vostok::animation::mixing::n_ary_tree_intrusive_base, class vostok::threading::single_threading_policy> &, unsigned int)` |
| 17.35 | vostok/game/sources/portable_interactive_object.cpp | `public: virtual void __thiscall survarium::portable_interactive_object::deserialize(class vostok::network_core::buffer_reader &, class vostok::network_core::buffer_reader *, unsigned int)` |
| 17.37 | vostok/game/sources/player_cook.cpp | `private: void __thiscall survarium::profile_skin_visual_cook::on_configs_loaded(class vostok::resources::queries_result &, class vostok::resources::query_result_for_cook *, struct survarium::player_profile const *)` |
| 18.33 | vostok/network_core/udp_match_connection_inline.h | `private: void __thiscall vostok::network_core::udp_match_connection::add_ordered_packet<class vostok::network_core::process_packet_predicate>(struct vostok::network_core::udp_match_connection::channel &, class vostok::network_core::udp_match_packet &, class vostok::network_core::process_packet_predicate const &)` |
| 18.38 | vostok/network_core/udp_match_connection_inline.h | `private: void __thiscall vostok::network_core::udp_match_connection::call_predicate<class vostok::network_core::process_packet_predicate>(class vostok::network_core::process_packet_predicate const &, class vostok::network_core::buffer_reader &)` |
| 18.85 | vostok/game/sources/lobby_menu_ui.cpp | `public: void __thiscall survarium::lobby_menu::on_stats_message_arrived(char const *, char const *, enum vostok::messaging::message_channel_enum)` |
| 19.61 | vostok/game/sources/network_client_processing.cpp | `private: void __thiscall survarium::network_client::process_static_match_info(class vostok::network_core::buffer_reader &)` |
| 20.47 | vostok/network_core/sources/udp_match_connection.cpp | `private: void __thiscall vostok::network_core::udp_match_connection::process_low_level_message(class vostok::network_core::buffer_reader &, unsigned int)` |
| 22.14 | vostok/network_core/sources/udp_match_connection.cpp | `public: bool __thiscall sequence_id_predicate::operator()(class vostok::network_core::udp_match_packet *) const` |
| 22.40 | vostok/buffer_vector_inline.h | `public: void __thiscall vostok::buffer_vector<struct vostok::render::ray>::assign<struct vostok::render::ray const *>(struct vostok::render::ray const *, struct vostok::render::ray const *const &)` |
| 22.70 | vostok/game_core/sources/weapon_core.cpp | `private: float __thiscall survarium::weapon_core::vertical_recoil_value(unsigned int) const` |
| 22.81 | vostok/render/engine/sources/render_model_skeleton.h | `public: virtual class vostok::math::aabb __thiscall vostok::render::skeleton_render_model_instance::get_aabb(void)` |
| 22.83 | vostok/game/sources/game_world_ui.cpp | `public: __thiscall survarium::game_world_ui::game_world_ui(class survarium::game_world &)` |
| 23.28 | vostok/game_core/sources/artefact_core_cook.cpp | `protected: virtual class survarium::artefact_base & __thiscall survarium::artefact_core_cook::construct_derived_resource(void *, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::game_effect_emitter, class vostok::resources::unmanaged_intrusive_base> const &, void *const) const` |
| 23.28 | vostok/game_core/sources/items_dictionary_cook.cpp | `private: void __thiscall survarium::items_dictionary_cook::on_subresources_loaded(class vostok::resources::queries_result &, class survarium::items_dictionary *)` |
| 23.93 | vostok/network_core/sources/udp_network_flow_emulator.cpp | `public: __thiscall vostok::network_core::udp_network_flow_emulator::~udp_network_flow_emulator(void)` |
| 24.35 | vostok/buffer_vector_inline.h | `public: void __thiscall vostok::buffer_vector<class vostok::render::shader_constant>::assign<class vostok::render::shader_constant const *>(class vostok::render::shader_constant const *, class vostok::render::shader_constant const *const &)` |
| 24.44 | vostok/network_core/sources/udp_match_connection.cpp | `private: void __thiscall vostok::network_core::udp_match_connection::fill_packet_header(class vostok::network_core::udp_match_packet &)` |
| 24.44 | vostok/render/engine/sources/stage_screen_space_reflections.cpp | `public: virtual void __thiscall vostok::render::stage_screen_space_reflections::execute(void)` |
| 24.59 | vostok/game/sources/artefact_inline.h | `private: __thiscall survarium::artefact<class survarium::artefact_lifebone_core>::artefact<class survarium::artefact_lifebone_core>(class vostok::configs::binary_config_value const &, class vostok::resources::resource_ptr<class survarium::game_effect_emitter, class vostok::resources::unmanaged_intrusive_base> const &, class survarium::base_game_scene *)` |
| 24.59 | vostok/game/sources/artefact_inline.h | `private: __thiscall survarium::artefact<class survarium::artefact_spring_core>::artefact<class survarium::artefact_spring_core>(class vostok::configs::binary_config_value const &, class vostok::resources::resource_ptr<class survarium::game_effect_emitter, class vostok::resources::unmanaged_intrusive_base> const &, class survarium::base_game_scene *)` |
| 24.90 | vostok/game_core/sources/inventory_cook.cpp | `public: virtual void __thiscall survarium::inventory_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 25.71 | vostok/render/engine/sources/effect_material_base.cpp | `public: void __thiscall vostok::render::effect_material_base::compile_end(class vostok::render::effect_compiler &)` |
| 26.54 | vostok/network_core/udp_match_connection_inline.h | `public: static void __cdecl vostok::network_core::udp_match_connection::construct_packet(struct vostok::network_core::udp_match_packets_orderer &, class vostok::network_core::udp_match_packet &, unsigned char, char const *const)` |
| 26.83 | vostok/engine/sources/engine_world_win.cpp | `message_processor` |
| 27.04 | vostok/game_core/sources/base_player.cpp | `protected: void __thiscall survarium::base_player::activate_physics(void)` |
| 28.12 | vostok/engine/sources/engine_world.cpp | `public: virtual void __thiscall vostok::engine::engine_world::on_alttab(bool)` |
| 28.25 | vostok/network_core/udp_match_connection_inline.h | `private: void __thiscall vostok::network_core::udp_match_connection::process_multipacket_message<class vostok::network_core::process_packet_predicate>(class vostok::network_core::process_packet_predicate const &, class vostok::network_core::buffer_reader &)` |
| 28.31 | vostok/game_core/sources/oxygen_tank.cpp | `public: virtual void __thiscall survarium::oxygen_tank::get_item_props(struct survarium::inventory_item_props &) const` |
| 28.67 | vostok/network_core/sources/udp_match_client.cpp | `private: void __thiscall vostok::network_core::udp_match_client::process_incoming_packet(class vostok::network_core::buffer_reader &, class boost::asio::ip::basic_endpoint<class boost::asio::ip::udp> const &, struct vostok::network_core::socket_handler *)` |
| 28.76 | vostok/game_core/sources/base_player.cpp | `protected: void __thiscall survarium::base_player::tick_animations(unsigned int, unsigned int)` |
| 28.76 | vostok/game_core/sources/player_logic_jump_state.cpp | `private: virtual void __thiscall survarium::player_logic_jump_state::serialize(class vostok::network_core::buffer_writer const &, class vostok::network_core::buffer_writer const *) const` |
| 29.86 | vostok/physics/sources/bullet_character_controller.cpp | `private: bool __thiscall vostok::physics::bullet_character_controller::impassable_slope(class btVector3const &, class btVector3const &, class btVector3const &) const` |

## Engine units in base but gone in target

- vostok/animation/fingers_to_weapon_corrector.h
- vostok/animation/sources/legs_ik_drawer.cpp
- vostok/core_debug_engine.h
- vostok/game/sources/base_match_client.h
- vostok/game_core/sources/artefact_base_config.cpp
- vostok/game_core/sources/artefact_rattle_core_config.cpp
- vostok/game_core/sources/jump_logic.cpp
- vostok/game_core/sources/weapon_ammunition_cook.cpp
- vostok/network_core/udp_match_packets_allocator.h
- vostok/physics/sources/old_bullet_character_controller.cpp
- vostok/physics/sources/old_bullet_character_controller.h
- vostok/render/core/dx11/sources/manager_common_inline.h
- vostok/render/facade/one_way_render_channel.h
- vostok/render/facade/sources/debug_draw_lines_command.cpp
- vostok/render/facade/sources/debug_draw_lines_command_inline.h
- vostok/render/facade/sources/debug_draw_triangles_command.cpp
- vostok/render/facade/sources/debug_draw_triangles_command_inline.h
- vostok/render/facade/sources/debug_renderer.cpp
- vostok/scaleform/sources/d3d1x_events.h
