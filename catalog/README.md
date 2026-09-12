# Build catalog

- `versions.json`: nine installer builds with download URLs and hashes. Eight
  carry PDBs; `v0.23h-build2285` explicitly has `symbols: false`.
- `extra_builds.json`: four executable-only builds, with archive member URLs,
  executable SHA-256 hashes, architecture, and optional local paths under `work/`.
- `chain.json`: the exact ordered sequence and base for function/flag comparisons.
  Ingestion does not silently add entries or skip absent intermediate builds.
- `dependency-markers.json`: scanner marker definitions and separately labeled
  source-snapshot version declarations. A declared version is not a measurement
  of every binary.

Keep labels stable: metadata, reports, and external research refer to them. Add
new builds here after identifying their source and hash. PDB capability is
independent of installer format; an executable-only build can still be scanned.

The root `versions.json` links here for existing consumers. The Nix flake and
Python scripts read this directory directly. Published wiki update names are
kept separately in `sources/`; no automatic version-name equivalence is assumed.
