# 0.11a → 0.11b: a same-day renderer drop and command filtering

Binary builds **816 → 826**. Catalog dates: 2013-05-14 → 2013-05-14.

Function accounting: **19 added, 26 deleted, 254 changed, and 11268 identical** demangled names.

This is a smaller function diff, but its shader change is disproportionate. The
shader evidence records **23 code-changing names**, while the permutation count
rises from 3,408 to 4,569. `gbuffer_pass.ps` doubles its permutations, and the
forward-lighting family changes together. In the function symbols,
`render::backend`, `shader_constant_buffer`, and `constants_handler<0/1>` gain and
lose typed constant-setting overloads. That combination points to a coordinated
lighting/material and shader-binding change.

Several renderer types introduced at 816 disappear immediately:
`streaming_ready_texture`, `requested_streamable_texture`,
`streamable_texture_info`, `speedtree_data`, `animated_model_instance`, and
`render_target_instance`. Because both binaries carry the same catalog date,
this is most safely described as code being folded, renamed, or backed out during
a same-day integration pass. The symbols do not prove that texture streaming or
SpeedTree support vanished from the product.

The non-rendering additions are unusually specific. `console_commands::execute`,
`execute_console_commands`, and `load` all gain an extra boolean parameter while
retaining `execution_filter`; `survarium::game::load_cc_script`,
`load_config_query`, and `on_config_loaded` change in parallel. This directly
supports a new command/config filtering path and aligns with the public
[0.11b note](../../update-note.wiki) that internal
console commands were prohibited. `weapon_core` also gains `reload_break_pred`
and `idle_AE_or_chamber_a_round_break_pred`, a focused continuation of the prior
weapon-state work.

The evidence supports renderer/shader integration and command filtering. The
public level addition is content and need not leave new client function names.
See the [826 build report](symbols-by-scope.md) and
[directional diff](object-summary.md).

## Canonical evidence

- [Complete function accounting](functions.json)
- [Object-level summary](object-summary.md) and [machine-readable form](object-summary.json)
- [Added and deleted symbols grouped by scope](symbols-by-scope.md)

Shader cross-check: [vostok-shader-evolution at the recorded evidence commit](https://github.com/srp-survarium/vostok-shader-evolution/blob/3c95be0e19d8e809b223d419d074c94d22b97f0f/EVOLUTION.md).
