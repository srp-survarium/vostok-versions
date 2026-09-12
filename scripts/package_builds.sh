#!/usr/bin/env bash
# Repackage every game-tree build inside a Survarium archive into upload-ready
# <identifier>.zip files, named from the engine's own version + compile date:
#     vostok_engine_v<ver>_<mon>_<d>_<year>.zip
# build# / internal id are NOT in the exe (the Steam depot supplies them at
# launch) — add them in the archive.org upload form if you have them.
#
#   nix develop -c scripts/package_builds.sh <source.zip|.7z> [out-dir]
#
# Needs 7z (p7zip) + strings (binutils) — both on the devShell PATH. Extracts one
# build at a time and deletes it after zipping, so peak disk ≈ output + one build.
set -euo pipefail
SRC=$(realpath -- "${1:?usage: package_builds.sh <source-archive> [out-dir]}")
OUT=${2:-./.generated/packages}
WORK=$(mktemp -d)
trap 'rm -rf "$WORK"' EXIT
mkdir -p "$OUT"
OUT=$(realpath -- "$OUT")

# Discover build roots: every folder holding game/binaries/<arch>/survarium.exe.
7z l -slt "$SRC" > "$WORK/listing.txt"
mapfile -t exepaths < <(sed -n 's/^Path = //p' "$WORK/listing.txt" \
  | grep -iE 'binaries/(x86|x64)/survarium\.exe$' | sort -u)
total=${#exepaths[@]}
echo "found $total game-tree build(s) in $(basename "$SRC")"

n=0
for exe in "${exepaths[@]}"; do
  n=$((n + 1))
  root=${exe%%/game/*}                      # e.g. Survarium_archives/Survarium31e
  # 1) lift just the exe to read the authoritative version + compile date
  7z e "$SRC" "$exe" "-o$WORK/exe" -y >/dev/null 2>&1
  E="$WORK/exe/survarium.exe"
  strings -n8 "$E" > "$WORK/exe/strings.txt"
  ver=$(grep -oE 'Vostok Engine v0\.[0-9]+[a-z][0-9]' "$WORK/exe/strings.txt" | sort -u | head -1 || true)
  ver=${ver#Vostok Engine }
  dt=$(grep -oE '^[A-Z][a-z][a-z] [ 0-9][0-9] [0-9]{4}$' "$WORK/exe/strings.txt" | sort -u | head -1 || true)
  rm -rf "$WORK/exe"
  if [ -z "$ver" ] || [ -z "$dt" ]; then echo "[$n/$total] SKIP $root (no version/date)"; continue; fi
  did=$(echo "$dt" | tr 'A-Z' 'a-z' | tr -s ' ' | tr ' ' '_')   # "Apr  1 2015" -> apr_1_2015
  ident="vostok_engine_${ver}_${did}"
  dest="$OUT/$ident.zip"
  if [ -f "$dest" ]; then echo "[$n/$total] skip (exists): $ident.zip"; continue; fi
  # 2) extract the full build tree and zip it (fast deflate), then clean up
  echo "[$n/$total] $(date +%H:%M:%S) $ident  ($root) ..."
  7z x "$SRC" "$root/*" "-o$WORK/x" -y >/dev/null 2>&1
  ( cd "$WORK/x/$(dirname "$root")" && 7z a -tzip -mx=1 -mmt=on "$dest" "${root##*/}" >/dev/null 2>&1 )
  test -s "$dest"
  rm -rf "$WORK/x"
  echo "[$n/$total] $(date +%H:%M:%S) DONE $ident.zip -> $(du -h "$dest" 2>/dev/null | cut -f1)"
done

# name map for the archive.org upload form (build#/id left to fill in)
{ echo "# identifier (archive.org) — title = 'Vostok Engine v<ver>, <date>'"
  echo "# build# / internal id: from the Steam depot or your records, not the exe"
  for z in "$OUT"/vostok_engine_*.zip; do
    if [ -e "$z" ]; then basename "$z" .zip; fi
  done
} > "$OUT/names.txt"
count=$(sed '/^#/d' "$OUT/names.txt" | wc -l)
echo "DONE: $count zips in $OUT (see names.txt)"
