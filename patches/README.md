# PDB checksum export

`pdb-diff-all-files.patch` backports the `pdb_diff` changes through upstream
commit `2151189477de0b08eb6152cabdd77e092892add8` onto the parser revision already
pinned by this repository (`95e462d9d49a18ab0a0e24542d4a8c54d27d7c0a`).

It adds `--all-files` and `--list-checksums`: enumerate every source checksum
record, including headers, export algorithm/digest/path TSV, and reject conflicting
hashes for the same normalized path. The Python report classifies missing and
incomparable hashes as unknown rather than using `pdb_diff`'s older diff summary.

The patched Nix package was built and its checksum export for build 802 matched
the previously available newer parser's export byte for byte.
