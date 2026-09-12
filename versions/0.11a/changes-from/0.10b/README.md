# 0.10b → 0.11a: weapon behavior was rebuilt around explicit states

Binary builds **802 → 816**. Catalog dates: 2013-05-09 → 2013-05-14.

Function accounting: **88 added, 56 deleted, 400 changed, and 11060 identical** demangled names.

The strongest evidence is the `survarium::weapon_core` symbol set: **44 functions
were added and 20 deleted**. New predicates include `aimed_fire_pred`,
`chamber_a_round_pred`, `chamber_a_round_on_reload_break_pred`, `can_reload`,
`can_jump`, `can_sprint`, and `ready_to_fire`. Existing implementations such as
`weapon_core::tick`, `weapon_core_aimed_fire_state_base::initialize`,
`weapon_core_fire_state_base::finalize`, and the shotgun reload substates also
changed substantially. This is evidence of a state-machine redesign rather than
a few weapon constants changing.

Accuracy work is visible independently. The new
`character_dispersion_skill_influence` scope supplies a constructor and `load`,
while `character_dispersion_calculator` gains `get_skill_coef` and
`set_character_dispersion_skill_influence`; its `tick` implementation changes.
`damage_model::reset` changes signature and `damage_model::hit_body_part` changes
code. These symbols directly support work on skill-dependent accuracy and damage.
The public [0.11a notes](../../update-note.wiki)
describe recoil, hip-fire accuracy, weapon-skill influence, shotgun behavior,
and damage-model changes, which is a close thematic match.

There is a smaller rendering thread. `weapon` gains `add_weapon_fire_light` and
`remove_weapon_fire_light`, matching the public firing-light change. Shader
evidence records five code-changing shader names, led by `gbuffer_pass.ps`, with
changes to environment-probe lighting, terrain G-buffer, post-processing, and
God rays. The renderer also gains several streaming-texture and SpeedTree-related
types. Those types disappear in the next same-day build, so they are better read
as an in-flight renderer refactor than as durable features.

Finally, the `sound_rms`, `sound_rms_cook`, and `sound_rms_pinned` scopes and their
source units disappear. That is direct evidence that an RMS resource path was
removed, although the symbols alone do not establish what replaced it.

The PDB checksums independently find **44 changed engine sources and 29 changed
headers**, with only two target-only and two base-only records. That shape agrees
with concentrated edits to existing weapon code rather than a wholesale source
tree replacement. Full symbol evidence is in the
[816 build report](symbols-by-scope.md) and the
[directional diff](object-summary.md).

## Canonical evidence

- [Complete function accounting](functions.json)
- [Object-level summary](object-summary.md) and [machine-readable form](object-summary.json)
- [Added and deleted symbols grouped by scope](symbols-by-scope.md)

Shader cross-check: [vostok-shader-evolution at the recorded evidence commit](https://github.com/srp-survarium/vostok-shader-evolution/blob/3c95be0e19d8e809b223d419d074c94d22b97f0f/EVOLUTION.md).
