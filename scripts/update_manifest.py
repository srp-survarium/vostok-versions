#!/usr/bin/env python3
"""Rewrite the integrity manifest for the canonical versions tree."""

from __future__ import annotations

import datetime
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1] / "versions"
MANIFEST = ROOT / "manifest.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    files = {
        path.relative_to(ROOT).as_posix(): sha256(path)
        for path in sorted(ROOT.rglob("*"))
        if path.is_file() and path != MANIFEST
    }
    manifest = {
        "schema": 1,
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "description": "Integrity manifest for the canonical version evidence tree.",
        "source_lineage": {
            "original_evidence_commit": "4621fd37df9db5d778be9cbf982d51b4ae252d7e"
        },
        "files": files,
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Recorded {len(files)} files in {MANIFEST}")


if __name__ == "__main__":
    main()
