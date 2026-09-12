# Preserved reports

[Expanded September 2026 source-file checksum comparisons](2026-09-12-source-files-expanded/README.md)
record exact file-level changes, including headers, after additional PDB-bearing
builds were fetched through the flake. The index records precisely which builds
and intervals were analyzed.

The [initial two-build comparison](2026-09-12-source-files/README.md) retains the
earlier `v0.10b-build802` → `v0.20e-build1916` result from before additional
archive downloads succeeded.

[June 2026](2026-06/README.md) contains the original binary-analysis reports and
supporting metadata. The snapshot has a hash manifest and is not an output target
of the maintained scripts.

New analysis writes to `work/reports/` and `work/diffs/`. Review its evidence and
coverage before publishing a new dated snapshot; keep older snapshots intact.

`builds` is a link to the June snapshot for existing shader-research references.
