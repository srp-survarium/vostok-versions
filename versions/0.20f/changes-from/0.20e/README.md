# 0.20e → 0.20f: a true maintenance-sized binary change

Binary builds **1916 → 1923**. Catalog dates: 2014-03-20 → 2014-04-01.

Function accounting: **1 added, 3 deleted, 11 changed, and 8847 identical** demangled names.

This interval has **8,847 identical names** and only one added, three deleted,
and eleven changed. The directional object summary identifies just two cleanly
matched changed engine functions, both at 99.97% similarity:
`network_world::dispatch_callbacks` and
`stage_shadow_direct::prepare_visibile_objects`. The other name-set differences
are a renderer sort predicate, a shader-buffer `fixed_vector` destructor, a bind
template instance, and several zero-match symbols that are consistent with
folding/alignment noise.

The public [0.20f notes](../../update-note.wiki)
describe synchronization improvements for high ping, low-end computers, and
heavy player activity. The near-identical change to
`network_world::dispatch_callbacks` is compatible with a small synchronization
fix, but the binary evidence is too thin to derive all three claims or their
mechanism. What the symbols firmly establish is that 0.20f was a very small
client maintenance build with no build-flag change.

See the [1923 build report](symbols-by-scope.md) and
[directional diff](object-summary.md).

## Canonical evidence

- [Complete function accounting](functions.json)
- [Object-level summary](object-summary.md) and [machine-readable form](object-summary.json)
- [Added and deleted symbols grouped by scope](symbols-by-scope.md)
