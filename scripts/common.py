#!/usr/bin/env python3
"""
common.py - shared helpers for the Survarium cross-version diff project.

Every version is an *internal* Survarium build that shipped with both
survarium.exe and survarium.pdb. The PDB is what makes a build tractable:
vostok-delinker uses it to split the EXE into per-function COFF .obj files, and
objdiff then diffs one version's objects against another's. No PDB -> no symbols,
no clean per-function objects, and this whole approach does not apply.

The toolchain (vostok-delinker, pdb_parser, objdiff-cli, innoextract) is provided
by this repo's Nix devShell. Run these scripts inside `nix develop`, or point the
*_BIN env vars at the binaries.
"""

from __future__ import annotations

import datetime
import hashlib
import json
import os
import shutil
import struct
import subprocess
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
REPO_DIR = SCRIPTS_DIR.parent
CATALOG_DIR = REPO_DIR / "catalog"
GENERATED_DIR = REPO_DIR / ".generated"
VERSIONS_DIR = GENERATED_DIR / "builds"
DIFFS_DIR = GENERATED_DIR / "comparisons"
REPORTS_DIR = GENERATED_DIR / "analysis"
CACHE_DIR = GENERATED_DIR / "downloads"
CONFIG_PATH = CATALOG_DIR / "chain.json"

# Real shipped Survarium PDBs record source paths under this prefix; the delinker
# and pdb-parser strip it to recover engine-relative unit names. Override per
# version with --engine-path if a build used a different root.
ENGINE_PATH_DEFAULT = "c:/survarium/sources"


def log(tag: str, msg: str) -> None:
    print(f"[{tag}] {msg}", flush=True)


# --- tool resolution -------------------------------------------------------

def _tool(env_var: str, default: str) -> str:
    return os.environ.get(env_var, default)


def delinker() -> str:
    return _tool("VOSTOK_DELINKER", "vostok-delinker")


def pdb_parser() -> str:
    return _tool("PDB_PARSER", "pdb_parser")


def objdiff_cli() -> str:
    return _tool("OBJDIFF_CLI", "objdiff-cli")


def innoextract() -> str:
    return _tool("INNOEXTRACT", "innoextract")


def require_tool(binary: str) -> str:
    """Return `binary` if on PATH, else exit with a devShell hint."""
    if shutil.which(binary) is None:
        sys.exit(
            f"error: {binary!r} not found on PATH.\n"
            "  Run inside this repo's `nix develop` (it provides "
            "vostok-delinker, pdb_parser, objdiff-cli, innoextract),\n"
            "  or set the matching *_BIN / VOSTOK_DELINKER env var."
        )
    return binary


def delinker_supports(flag: str) -> bool:
    """Whether the delinker advertises `flag` in --help (newer flags may be absent)."""
    try:
        out = subprocess.run(
            [delinker(), "--help"], capture_output=True, text=True, check=False
        )
        return flag in (out.stdout + out.stderr)
    except OSError:
        return False


# --- assets ----------------------------------------------------------------

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def tool_identity(binary: str) -> dict:
    """Resolve the executable actually used, including overrides outside Nix."""
    require_tool(binary)
    path = Path(shutil.which(binary)).resolve()
    return {"path": str(path), "sha256": sha256_file(path)}


def object_fingerprint(label: str) -> dict:
    root = VERSIONS_DIR / label
    objects = sorted((root / "objects").rglob("*.obj"))
    if not objects or not (root / "meta.json").is_file():
        sys.exit(f"error: {label} has no complete local ingestion; run add_version.py {label}")
    h = hashlib.sha256()
    for path in objects:
        h.update(path.relative_to(root).as_posix().encode() + b"\0")
        h.update(bytes.fromhex(sha256_file(path)))
    return {"label": label, "objects_sha256": h.hexdigest(), "n_objects": len(objects),
            "metadata_sha256": sha256_file(root / "meta.json")}


def comparison_inputs(base: str, target: str) -> dict:
    return {"base": object_fingerprint(base), "target": object_fingerprint(target),
            "objdiff": tool_identity(objdiff_cli()),
            "flake_lock_sha256": sha256_file(REPO_DIR / "flake.lock"),
            "scripts": {name: sha256_file(SCRIPTS_DIR / name)
                        for name in ("common.py", "diff_versions.py")}}


def find_exe_pdb(root: Path) -> tuple[Path, Path]:
    """Locate the game survarium.exe + survarium.pdb under `root`.

    Picks the largest non-uninstaller survarium.exe (mirrors the flake's
    extraction heuristic), then the .pdb sitting beside it.
    """
    exes = sorted(
        (p for p in root.rglob("*.exe")
         if p.name.lower() == "survarium.exe" and "uninstall" not in str(p).lower()),
        key=lambda p: p.stat().st_size, reverse=True,
    )
    if not exes:
        sys.exit(f"error: no survarium.exe found under {root}")
    exe = exes[0]
    pdb = exe.with_suffix(".pdb")
    if not pdb.exists():
        cand = list(exe.parent.glob("*.pdb"))
        if not cand:
            sys.exit(f"error: no .pdb beside {exe} (a symbol-less build is not usable here)")
        pdb = cand[0]
    return exe, pdb


# --- repo config (which label is the base) ---------------------------------

def load_config() -> dict:
    if CONFIG_PATH.exists():
        return json.loads(CONFIG_PATH.read_text())
    return {}


def save_config(cfg: dict) -> None:
    CONFIG_PATH.write_text(json.dumps(cfg, indent=2) + "\n")


def now_iso() -> str:
    return datetime.datetime.now().replace(microsecond=0).isoformat()


# --- engine vs third-party classification ----------------------------------
# First-party engine/game code lives under sources/vostok/, so its delinked
# units are "vostok/...". Everything else (boost, bullet, stlport, scaleform,
# vorbis, opcode, speedtree, zlib, ogg, wildmagic, _msvc_internal, ...) is
# third-party and is the main source of cross-version diff noise.

def is_engine_unit(unit: str) -> bool:
    return unit.startswith("vostok/")


# Compiler-synthesized / non-source functions (MSVC demangled names). These are
# not hand-written - vtable thunks, deleting destructors, static init/teardown,
# EH/RTTI iterators, delinker stubs - and they churn with layout/codegen changes
# rather than source edits, so a source-level diff drops them by default.
_GENERATED_SUBSTRINGS = (
    "[thunk]:",                       # adjustor / vcall thunks
    "vcall'",
    "vtordisp",
    "vector deleting destructor",     # synthesized array/scalar deleting dtors
    "scalar deleting destructor",
    "vbase destructor'",
    "dynamic initializer for",        # static init / teardown
    "dynamic atexit destructor for",
    "eh vector",                      # EH array ctor/dtor iterators
    "vector constructor iterator",
    "vector destructor iterator",
    "copy constructor closure",
    "default constructor closure",
    "`RTTI",                          # RTTI descriptors
    "local static guard",             # function-static init guards
    "local static thread guard",
    "__autoclassinit",
)


def is_compiler_generated(name: str) -> bool:
    return name == "empty_stub" or any(s in name for s in _GENERATED_SUBSTRINGS)


# Third-party libraries whose templates get instantiated *inside* engine (vostok/)
# translation units - their owning namespace is third-party even though the unit
# path is vostok/*. Matched against the owning qualified name (the token right
# after the calling convention), so library types in *parameters* don't trip it.
_CALLING_CONVENTIONS = (" __thiscall ", " __cdecl ", " __stdcall ", " __fastcall ", " __vectorcall ")
_THIRDPARTY_NAMESPACES = (
    "boost::", "std::", "stlport::", "Scaleform::", "Wm4::", "eastl::",
    "fastdelegate::", "OpenSSL::", "Opcode::",
)


def _owning_namespace_thirdparty(name: str) -> bool:
    # The owning class/function begins after the last calling convention; the
    # return type (which may mention a library type) sits before it and is ignored.
    cut = -1
    for cc in _CALLING_CONVENTIONS:
        p = name.rfind(cc)
        if p > cut:
            cut = p + len(cc)
    owner = (name[cut:] if cut >= 0 else name).lstrip("&* ")
    return owner.startswith(_THIRDPARTY_NAMESPACES)


def split_qualified(name: str) -> tuple[str, str]:
    """Split a demangled function name into (owning scope, leaf).

    The owner is the class/namespace that encloses the function -
    `survarium::weapon_core::aimed_fire_pred(void) const` -> ('survarium::weapon_core',
    'aimed_fire_pred(void) const'). '::' inside template args or parameters is
    ignored (angle-depth tracked; the parameter list is cut before scoping).
    """
    cut = -1
    for cc in _CALLING_CONVENTIONS:
        p = name.rfind(cc)
        if p > cut:
            cut = p + len(cc)
    s = (name[cut:] if cut >= 0 else name).lstrip("&* ")

    # body = signature without its parameter list (first top-level '(')
    depth, body = 0, s
    for i, ch in enumerate(s):
        if ch == "<":
            depth += 1
        elif ch == ">":
            depth -= 1
        elif ch == "(" and depth == 0:
            body = s[:i]
            break

    depth, last, i = 0, -1, 0
    while i < len(body) - 1:
        ch = body[i]
        if ch == "<":
            depth += 1
        elif ch == ">":
            depth -= 1
        elif ch == ":" and depth == 0 and body[i + 1] == ":":
            last = i
            i += 2
            continue
        i += 1
    if last < 0:
        return ("", s)
    return (body[:last], s[last + 2:])


def owning_scope(name: str) -> str:
    return split_qualified(name)[0]


def classify(unit: str, name: str) -> str:
    """One of: 'third_party', 'generated' (compiler-synthesized engine), or
    'engine' (hand-written first-party). Third-party is detected by both unit
    path and owning namespace (library templates inlined into engine units)."""
    if not is_engine_unit(unit):
        return "third_party"
    if is_compiler_generated(name):
        return "generated"
    if _owning_namespace_thirdparty(name):
        return "third_party"
    return "engine"


# --- version registry (versions.json) + flake fetch ------------------------
# versions.json is the single source of truth, read by BOTH this script (json)
# and flake.nix (builtins.fromJSON). Each entry: label, url, sha256, and
# optionally base (bool) + engine_path. The flake turns each into a
# `version-<label>` package: the archive.org installer, innoextracted to a dir
# holding survarium.{exe,pdb}.

REGISTRY_PATH = CATALOG_DIR / "versions.json"


def registry() -> list[dict]:
    if REGISTRY_PATH.exists():
        return json.loads(REGISTRY_PATH.read_text())
    return []


def registry_entry(label: str) -> dict | None:
    return next((v for v in registry() if v.get("label") == label), None)


def chain_versions() -> list[dict]:
    """Return exactly the configured sequence; never derive it from local caches."""
    labels = load_config().get("versions", [])
    if len(labels) != len(set(labels)):
        sys.exit("error: duplicate labels in catalog/chain.json")
    by_label = {v["label"]: v for v in registry()}
    for label in labels:
        if label not in by_label or not by_label[label].get("symbols", True):
            sys.exit(f"error: {label} is not a PDB-bearing catalog entry")
    return [by_label[label] for label in labels]


def flake_attr(label: str) -> str:
    """Package attribute for a label: dots -> underscores so the `nix build .#attr`
    CLI path isn't split on '.' (the flake applies the same transform)."""
    return "version-" + label.replace(".", "_")


def fetch_from_flake(label: str) -> Path:
    """`nix build .#version-<label>` and return the extracted-build out path.
    stderr streams through so flake build errors are visible, not swallowed."""
    require_tool("nix")
    out = subprocess.run(
        ["nix", "build", f".#{flake_attr(label)}", "--no-link", "--print-out-paths"],
        cwd=REPO_DIR, stdout=subprocess.PIPE, text=True, check=True,
    )
    return Path(out.stdout.strip().splitlines()[-1])


# --- objdiff config emission ------------------------------------------------

def write_dummy_obj(path: Path) -> None:
    """A minimal valid empty COFF .obj, used as the base side for a unit that
    exists in the target version but not the base (i.e. an added unit)."""
    symbol_table_offset = 20 + 40
    header = struct.pack("<HHIIIHH", 0x14C, 1, 0, symbol_table_offset, 0, 0, 0)
    section = struct.pack("<8sIIIIIIHHI", b".text\0\0\0",
                          0, 0, 0, 0, 0, 0, 0, 0, 0x60000020)
    string_table = struct.pack("<I", 4)
    with path.open("wb") as f:
        f.write(header)
        f.write(section)
        f.write(string_table)
