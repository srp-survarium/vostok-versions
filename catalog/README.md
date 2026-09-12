# Catalog

Machine-readable inputs for the version record and analysis tools:

- `releases.json` accounts for every public version directory, its reported
  date and stage, update-note revision, mapped binaries, and historical leads.
- `versions.json` describes nine archived builds: eight with EXE/PDB pairs and
  one marked `symbols: false`. It records original URLs and hashes, binary
  spellings, candidate release associations, and exact file identities.
- `extra_builds.json` describes four executable-only dependency-scan builds.
- `chain.json` is the exact eight-build function-comparison sequence.
- `binary-release.json` records compact bundles for five verified EXE/PDB pairs,
  including compressed and contained-file hashes.
- `dependency-markers.json` defines executable strings and RTTI markers. Declared
  library versions remain separate from observed markers.

The label is the stable binary identity used by scripts and Nix. `release`
associates it with a directory under `versions/`. `binary_version` preserves the
file or archive spelling. Associations are marked `candidate` when spelling and
date support the mapping but no authoritative release manifest is available.

For entries with `bundle_url`, `nix build .#version-<label>` fetches the compact
EXE/PDB bundle. `nix build .#version-<label>-archive` extracts the original
installer. Entries without a bundle use the original archive. Both are
fixed-output downloads; the bundle manifest ties compressed bytes to the exact
EXE and PDB hashes in `versions.json`.

Generated local executable paths live under `.generated/downloads/`. Browse the
public record through [versions/README.md](../versions/README.md).
