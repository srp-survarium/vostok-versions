# Preserved reports

[September 2026 source-file checksum comparison](2026-09-12-source-files/README.md)
records exact file-level changes between `v0.10b-build802` and `v0.20e-build1916`,
including headers. The six other configured PDB builds were unavailable locally;
Archive.org downloads failed during this run. The report explicitly marks its subset.

[June 2026](2026-06/README.md) contains the original binary-analysis reports and
supporting metadata. The snapshot has a hash manifest and is not an output target
of the maintained scripts.

New analysis writes to `work/reports/` and `work/diffs/`. Review its evidence and
coverage before publishing a new dated snapshot; keep older snapshots intact.

`builds` is a link to the June snapshot for existing shader-research references.
