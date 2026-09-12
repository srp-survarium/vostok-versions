# 0.11c → 0.11e: resource layouts moved while shadows and medkits changed

Binary builds **870 → 884**. Catalog dates: 2013-05-24 → 2013-05-28.

Function accounting: **25 added, 38 deleted, 473 changed, and 11012 identical** demangled names.

Most added/deleted names here are template-layout evidence. Resource-query
intrusive lists move among offsets 600, 608, and 616; a double-linked query list
moves from offsets 616/612 to 624/620. `resources_manager::create_resources`,
`allocate_functionality::allocate_final_resources`, and
`hdd_manager::grab_sorted_queries` acquire the corresponding new template
specializations. Many apparent additions and deletions therefore express a
changed `query_result` layout rather than separate new behavior.

The durable behavioral clusters are smaller:

- `stage_shadow_direct::execute_cascade` and `prepare_models` change signatures,
  `sun_cascade` disappears, and renderer/portal-sector culling functions change;
- `medkit` gains `on_player_death`, `holder_assigned`, `holder_removed`, and
  `remove`, while several methods move from protected to private signatures;
- `fs_new::virtual_path_string` gains a constructor specialization;
- `network_client::close_current_match`, post-processing, render options, and
  collision-contact code change.

Shader evidence calls this a settling pass: 259 of 265 shader names are
byte-identical, two change only their permutation matrices, and four change code.
That supports a focused renderer/resource maintenance build rather than another
broad graphics rewrite.

Build 884 is dated May 28, while the public [0.11d](../../../0.11d/update-note.wiki)
and [0.11e](../../update-note.wiki) pages are dated
May 30. The interval may include work associated with 0.11d, whereas 0.11e is
described only as an installer repair. The executable symbols cannot establish
that mapping, and the observed client changes should not be attributed to the
installer hotfix. See the [884 build report](symbols-by-scope.md)
and [directional diff](object-summary.md).

## Canonical evidence

- [Complete function accounting](functions.json)
- [Object-level summary](object-summary.md) and [machine-readable form](object-summary.json)
- [Added and deleted symbols grouped by scope](symbols-by-scope.md)

Shader cross-check: [vostok-shader-evolution at the recorded evidence commit](https://github.com/srp-survarium/vostok-shader-evolution/blob/3c95be0e19d8e809b223d419d074c94d22b97f0f/EVOLUTION.md).
