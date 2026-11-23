#!/usr/bin/env python3
"""Render the poster and seal it into ``assets/entry.png.b64``.

Build-time only (uses Pillow via :mod:`build_image`).  Run from anywhere:

    python3 tools/render.py

Writes ``entry.png`` at the repository root (a build artifact, ignored by
git) and the single-line base64 asset that ``main.py`` ships.
"""

import base64
import hashlib
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import build_image  # noqa: E402


def main() -> int:
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    png_path = os.path.join(repo_root, "entry.png")
    build_image.build(png_path)

    with open(png_path, "rb") as handle:
        data = handle.read()

    asset_dir = os.path.join(repo_root, "assets")
    os.makedirs(asset_dir, exist_ok=True)
    asset_path = os.path.join(asset_dir, "entry.png.b64")
    with open(asset_path, "w", encoding="ascii") as handle:
        handle.write(base64.b64encode(data).decode("ascii"))

    print(f"poster: {png_path} ({len(data)} bytes)")
    print(f"sha256: {hashlib.sha256(data).hexdigest()}")
    print(f"asset:  {asset_path} (single line, {os.path.getsize(asset_path)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
