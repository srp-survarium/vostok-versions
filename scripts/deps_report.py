#!/usr/bin/env python3
"""Report dependency markers into .generated/analysis/.

String/RTTI matches are observations, not proof of linked libraries or parsed
imports. Version-looking atoms are candidates; declared source versions remain
separate. Published cross-version evidence lives in versions/dependencies.md.
"""
from __future__ import annotations

import argparse
import base64
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as c  # noqa: E402

REPORTS_DIR = c.REPORTS_DIR
EXTRA_PATH = c.CATALOG_DIR / "extra_builds.json"
MARKER_PATH = c.CATALOG_DIR / "dependency-markers.json"


def extra_registry() -> list[dict]:
    return json.loads(EXTRA_PATH.read_text())


def fetch_exe_via_flake(token: str) -> Path:
    out = subprocess.run(
        ["nix", "build", f'.#"{token}"', "--no-link", "--print-out-paths"],
        cwd=c.REPO_DIR, stdout=subprocess.PIPE, text=True, check=True,
    )
    return Path(out.stdout.strip().splitlines()[-1]) / f"{token}.exe"


BARE_VER = re.compile(r"^\d+\.\d+\.\d+(?:\.\d+)?[a-z]?$")
IPV4 = re.compile(r"^(\d{1,3}\.){3}\d{1,3}$")


def is_version_atom(s: str) -> bool:
    return bool(BARE_VER.match(s)) and not IPV4.match(s)


def exe_strings(exe: Path) -> list[str]:
    """ASCII + UTF-16LE strings of the image (markers seen are all ASCII, but
    pull both so nothing is missed)."""
    out = []
    for args in (["strings", "-n", "4", str(exe)],
                 ["strings", "-n", "4", "-e", "l", str(exe)]):
        out.append(subprocess.run(args, capture_output=True, text=True,
                                  errors="replace", check=True).stdout)
    return "\n".join(out).splitlines()


# --- version banners and candidate hints ---------------------------------

def v_zlib(blob: str):
    m = re.search(r"(?:inflate|deflate) (\d+\.\d+\.\d+) Copyright", blob)
    if m:
        return m.group(1)
    # Wrapper names can remain even when the library's banner is unavailable.
    if re.search(r"bio_zlib_new|zlib compression", blob, re.I):
        return "zlib wrapper marker (no version banner)"
    return None


def v_openssl(blob: str):
    m = re.search(r"OpenSSL (\d+\.\d+\.\d+[a-z]*) (\d+ \w+ \d+)", blob)
    if m:
        return f"{m.group(1)} ({m.group(2)})"
    # A path can hint at a branch without identifying the linked version.
    if re.search(r"engines-1_1|/lib/engines-1_1", blob):
        return "1.1.x path marker (no version banner)"
    if "CRYPTOGAMS" in blob or "@openssl.org" in blob or "ssleay" in blob.lower():
        return "OpenSSL-related marker (no version banner)"
    return None


def v_scaleform(lines: list[str], blob: str):
    # Co-occurring version atoms are candidates, not an attributed version.
    if "@Scaleform@@" in blob:
        cands = sorted({s for s in lines if re.match(r"^4\.\d+\.\d+$", s)})
        return ", ".join(cands) if cands else "RTTI marker (version not isolated)"
    if "vostok_scaleform.dll" in blob.lower():
        return "vostok_scaleform.dll name marker (version unknown)"
    return None


def v_stl(blob: str):
    """Which C++ standard library: STLport (early) vs the MSVC std:: (later)."""
    if "@stlp_std@@" in blob:
        return "STLport namespace"
    if "@std@@" in blob or "char_traits@D@std@@" in blob:
        return "MSVC std::"
    return None


def pe_arch(exe: Path):
    """PE Machine field: 0x14c = x86, 0x8664 = x64."""
    try:
        with exe.open("rb") as f:
            f.seek(0x3C)
            pe = int.from_bytes(f.read(4), "little")
            f.seek(pe + 4)
            m = int.from_bytes(f.read(2), "little")
        return {0x14C: "x86", 0x8664: "x64", 0xAA64: "arm64"}.get(m, hex(m))
    except OSError:
        return "?"


def v_bugtrap(build_dir: Path):
    """Collect a version-looking UTF-16 string from an adjacent BugTrap DLL."""
    dlls = list(build_dir.glob("bugtrap*.dll")) + list(build_dir.glob("BugTrap*.dll"))
    if not dlls:
        return None
    txt = subprocess.run(["strings", "-e", "l", "-n", "4", str(dlls[0])],
                         capture_output=True, text=True, errors="replace", check=True).stdout
    vers = sorted({s for s in txt.splitlines()
                   if re.match(r"^\d+\.\d+\.\d+\.\d+$", s)})
    return vers[0] if vers else None


def v_libpng(lines: list[str], blob: str):
    if "libpng" not in blob:
        return None
    # PNG_LIBPNG_VER_STRING is a bare "1.5.x"/"1.6.x" atom in .rdata.
    cands = sorted({s for s in lines if is_version_atom(s)
                    and re.match(r"1\.[5-9]\.", s)})
    return ", ".join(cands) if cands else "libpng marker (version string not isolated)"



def scan(exe: Path, build_dir: Path) -> dict:
    lines = exe_strings(exe)
    blob = "\n".join(lines)
    definitions = json.loads(MARKER_PATH.read_text())
    versions = {"zlib": v_zlib(blob), "openssl": v_openssl(blob),
                "scaleform": v_scaleform(lines, blob), "libpng": v_libpng(lines, blob),
                "bugtrap": v_bugtrap(build_dir)}
    dependencies = {}
    for rule in definitions["rules"]:
        key = rule["key"]
        matches = [marker for marker in rule["markers"] if marker in blob]
        value = versions.get(key)
        basis = None
        if value:
            basis = "version candidate or marker hint"
            if key == "zlib" and re.match(r"^\d+\.\d+\.\d+$", value):
                basis = "zlib copyright banner"
            elif key == "openssl" and re.match(r"^\d+\.\d+\.\d+[a-z]* ", value):
                basis = "OpenSSL version banner"
            elif key == "bugtrap":
                basis = "version-looking string in adjacent BugTrap DLL"
        dependencies[key] = {"display": rule["display"], "marker_matches": matches,
                             "version_observation": value, "version_basis": basis,
                             "declared_reference_version": rule["declared_version"]}
    dlls = sorted({p for p in build_dir.iterdir() if p.is_file()
                   and p.name.lower().startswith("bugtrap") and p.suffix.lower() == ".dll"})
    return {"exe": {"path": str(exe), "sha256": c.sha256_file(exe),
                    "size": exe.stat().st_size, "arch": pe_arch(exe)},
            "adjacent_bugtrap_dlls": [{"name": p.name, "sha256": c.sha256_file(p)} for p in dlls],
            "dependencies": dependencies,
            "version_atoms": sorted({s for s in lines if is_version_atom(s)}),
            "dll_name_markers": [dll for dll in definitions["dll_names"] if dll.lower() in blob.lower()],
            "standard_library_marker": v_stl(blob)}


def cell(info: dict) -> str:
    if info["version_observation"]:
        return info["version_observation"].replace("|", "\\|")
    return "marker observed" if info["marker_matches"] else "not observed"


def main() -> None:
    argparse.ArgumentParser(description=__doc__).parse_args()
    c.require_tool("strings")
    entries = c.registry() + extra_registry()
    scans = {}
    for entry in entries:
        label = entry["label"]
        if "exe_url" in entry:
            exe = c.REPO_DIR / entry["exe"]
            if not exe.exists():
                exe = fetch_exe_via_flake(label.split("-")[0].removeprefix("v"))
            expected = base64.b64decode(entry["exe_sha256"].removeprefix("sha256-")).hex()
            if c.sha256_file(exe) != expected:
                sys.exit(f"error: cached executable hash mismatch for {label}: {exe}")
        else:
            exe = c.fetch_from_flake(label) / "survarium.exe"
        c.log("deps", f"scanning {label}")
        scans[label] = scan(exe, exe.parent)
    result = {"generated_at": c.now_iso(), "strings_tool": c.tool_identity("strings"),
              "flake_lock_sha256": c.sha256_file(c.REPO_DIR / "flake.lock"),
              "marker_definitions_sha256": c.sha256_file(MARKER_PATH),
              "script_sha256": c.sha256_file(Path(__file__)),
              "catalog_entries": entries, "builds": scans}
    md = ["# Dependency marker observations", "",
          "Version banners, candidate version strings, RTTI names, and DLL-name strings "
          "observed in the selected files. A missing marker is not proof of absence. "
          "DLL-name strings are not a parsed PE import table.", "",
          "Declared source versions are recorded separately in the JSON evidence. "
          "Published interpretations and the manually recorded 25-build sweep are in versions/dependencies.md.", "",
          "| Dependency | " + " | ".join(scans) + " |",
          "| --- | " + " | ".join("---" for _ in scans) + " |"]
    rules = json.loads(MARKER_PATH.read_text())["rules"]
    for rule in rules:
        md.append("| " + rule["display"] + " | " + " | ".join(
            cell(scan["dependencies"][rule["key"]]) for scan in scans.values()) + " |")
    for label, scan_result in scans.items():
        md += ["", f"## {label}", "", f"Executable SHA-256: `{scan_result['exe']['sha256']}`.",
               "", "DLL-name markers: " + (", ".join(scan_result["dll_name_markers"]) or "none observed") + "."]
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    (REPORTS_DIR / "DEPENDENCY_MARKERS.json").write_text(json.dumps(result, indent=2) + "\n")
    (REPORTS_DIR / "DEPENDENCY_MARKERS.md").write_text("\n".join(md) + "\n")
    c.log("deps", f"{len(scans)} builds -> {REPORTS_DIR}")


if __name__ == "__main__":
    main()
