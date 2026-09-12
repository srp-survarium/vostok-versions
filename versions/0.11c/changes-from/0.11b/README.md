# 0.11b → 0.11c: HDR sound landed with broad gameplay and rendering changes

Binary builds **826 → 870**. Catalog dates: 2013-05-14 → 2013-05-24.

Function accounting: **142 added, 160 deleted, 1465 changed, and 9916 identical** demangled names.

This is the largest May 2013 function interval: **142 names added, 160 deleted,
and 1,465 changed**. The sound symbols show a structural replacement. Removed
scopes include `ogg_file_contents_cook`, `ogg_sound_cook`, `ogg_source_cook`,
`wav_encoded_sound_interface_cook`, `sound_environment_cook`, `ogg_sound`, and
`effect_cross_fader`. At the same time:

- `sound_scene` gains `calculate_hdr_audio_frame`, `calculate_channel_matrix`,
  `x3daudio_calculate`, `process_fade`, and listener notification methods;
- `new_sound_propagator` changes its voice attachment, detachment, SPL, RMS, and
  timing interfaces;
- `sound_voice` changes buffer refill, muting, filtering, callback, and quality
  handling;
- allocator specializations change from 28/108/136-byte objects to
  32/84/96-byte objects, consistent with changed sound-object layouts.

That is direct evidence for the public [0.11c notes](../../update-note.wiki)
about HDR audio and sound-direction fixes. The file checksums across 816 -> 870
find **45 changed sound files, six sound files present only at 870, and twenty
sound files present only at 816**. Since that checksum interval also contains
build 826, the exact file changes cannot be assigned between the two steps, but
the consecutive symbol diff locates the sound rearchitecture at 826 -> 870.

The gameplay symbols likewise match several independent areas from the notes:
`booby_trap_set_core::load`, trap state/timer/defuse functions, and network trap
messages changed; `player_logic_stand_state` and `player_logic_crouch_state`
animation selection changed; `damage_model`, hit processing, and
`game_world_ui::on_hit_from_pos` changed; reload-break and shotgun reload
functions changed; and the UI gains or changes player-list, quick-slot, ammo,
health, victory-point, and match-state methods.

Rendering changed at the same time. `stage_ambient_occlusion::execute`, shader
macro registration, and shader-cache interfaces changed. The shader registry
shrinks from 81 to 68 slots; six shader names are added and two removed. Motion
blur splits into low/medium/high variants and `ssao_accumulation_hq.ps` appears.
These symbols and shader deltas support HDAO/quality-tier and graphics work,
although they do not map each internal name to a particular public option.

The broad source count is therefore expected rather than a checksum accident.
Across the combined 816 -> 870 file interval, 222 of the 258 changed engine files
sit in `game_core` (71), `render` (58), `game` (48), and `sound` (45), while all
1,921 recorded third-party files remain identical. See the
[870 build report](symbols-by-scope.md) and
[directional diff](object-summary.md).

## Canonical evidence

- [Complete function accounting](functions.json)
- [Object-level summary](object-summary.md) and [machine-readable form](object-summary.json)
- [Added and deleted symbols grouped by scope](symbols-by-scope.md)

Shader cross-check: [vostok-shader-evolution at the recorded evidence commit](https://github.com/srp-survarium/vostok-shader-evolution/blob/3c95be0e19d8e809b223d419d074c94d22b97f0f/EVOLUTION.md).
