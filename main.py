#!/usr/bin/env python3
"""Entry point for the news-image-20261122 make.fun competition.

The repository ships its poster as a sealed base64 asset
(``assets/entry.png.b64``).  This program -- Python standard library only --
decodes that asset, checks the PNG signature, and writes the image
atomically to ``$MAKEFUN_OUTPUT_DIR/entry.png`` (default ``/output``).
It needs no network and writes identical bytes on every run.
"""

import base64
import os
import struct
import sys
import tempfile

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_IMAGE_BYTES = 1_048_576  # 1 MiB competition cap
MAX_DIMENSION = 1024  # competition cap on width and height, in pixels


def load_poster_bytes() -> bytes:
    """Decode the sealed poster asset that ships with this repository."""
    here = os.path.dirname(os.path.abspath(__file__))
    asset_path = os.path.join(here, "assets", "entry.png.b64")
    with open(asset_path, "r", encoding="ascii") as handle:
        encoded = handle.read().strip()
    return base64.b64decode(encoded, validate=True)


def check_dimensions(data: bytes) -> None:
    """Enforce the 1024x1024 cap using the PNG IHDR chunk.

    The IHDR chunk always follows the 8-byte signature: a 4-byte length, the
    ``IHDR`` type, then width and height as big-endian uint32 values.
    """
    if len(data) < 24 or data[12:16] != b"IHDR":
        raise SystemExit("sealed asset has no PNG IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        raise SystemExit(
            f"poster is {width}x{height}, over the {MAX_DIMENSION}x{MAX_DIMENSION} cap"
        )


def main() -> int:
    data = load_poster_bytes()
    if not data.startswith(PNG_SIGNATURE):
        raise SystemExit("sealed asset is not a PNG image")
    if len(data) > MAX_IMAGE_BYTES:
        raise SystemExit("sealed asset exceeds the 1 MiB size cap")
    check_dimensions(data)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")

    # Write atomically: fill a temp file in the same directory, then rename,
    # so a reader never sees a half-written entry.png.
    fd, tmp_path = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
        os.replace(tmp_path, target)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    return 0


if __name__ == "__main__":
    sys.exit(main())
