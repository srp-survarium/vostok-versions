# Build catalog

- `versions.json`: nine installer builds with download URLs and hashes. Eight
  carry PDBs; `v0.23h-build2285` explicitly has `symbols: false`. Five entries
  also point to small, verified GitHub release bundles containing the exact
  EXE/PDB pairs used by the reports.
- `binary-release.json`: release tag, asset URLs, compressed hashes and sizes,
  and hashes and sizes for both files inside every published bundle.
- `extra_builds.json`: four executable-only builds, with archive member URLs,
  executable SHA-256 hashes, architecture, and optional local paths under `work/`.
- `chain.json`: the exact ordered sequence and base for function/flag comparisons.
  Ingestion does not silently add entries or skip absent intermediate builds.
- `dependency-markers.json`: scanner marker definitions and separately labeled
  source-snapshot version declarations. A declared version is not a measurement
  of every binary.

Build 802 uses the canonical label **`v0.10b-build802`**, consistent with the
reconstruction project's naming. The June snapshot and source wiki call it
`v0.100b-build802` / `0.100b`; those are historical names for the same cataloged
build. Download URLs, hashes, archived paths, and original source text retain
their recorded values. New commands and generated outputs use `v0.10b-build802`.

Keep labels stable: metadata, reports, and external research refer to them. Add
new builds here after identifying their source and hash. PDB capability is
independent of installer format; an executable-only build can still be scanned.

The root `versions.json` links here for existing consumers. The Nix flake and
Python scripts read this directory directly. Published wiki update names are
kept separately in `sources/`; no automatic version-name equivalence is assumed.

For a catalog entry with `bundle_url`, `nix build .#version-<label>` downloads
the compact evidence bundle. `nix build .#version-<label>-archive` uses the
original installer URL instead. Entries without a bundle continue to use their
original archives. Both inputs are fixed-output downloads, and the release
manifest ties each compressed asset back to the original EXE and PDB hashes.
