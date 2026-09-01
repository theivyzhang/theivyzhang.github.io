#!/usr/bin/env python3
"""Resize + re-encode the photos under images/misc/ so they are web-sized.

Phone photos are 3-17 MB each, which is far too heavy to ship in a GitHub Pages
repo. This walks images/misc/, applies the EXIF orientation, caps the long edge
at MAX_EDGE px, strips metadata, and rewrites the file as a progressive JPEG
with a lowercase, space-free name.

Re-run it after dropping new photos into images/misc/ -- it skips anything that
is already small enough.

Needs Pillow:  /opt/homebrew/bin/python3.11 scripts/optimize_misc_photos.py
"""

import sys
from pathlib import Path

from PIL import Image, ImageOps

MAX_EDGE = 1600
QUALITY = 78
ROOT = Path(__file__).resolve().parent.parent / "images" / "misc"
SUFFIXES = {".jpg", ".jpeg", ".png", ".heic", ".webp"}


def clean_name(stem: str) -> str:
    return stem.lower().replace(" ", "-").replace("_", "-")


def optimize(path: Path) -> None:
    target = path.with_name(clean_name(path.stem) + ".jpg")
    # macOS is case-insensitive, so IMG_1.JPG and img-1.jpg can be the same file.
    # Encode to a scratch file first, then swap it in.
    scratch = path.with_name(target.stem + ".optimizing.tmp")

    with Image.open(path) as im:
        im = ImageOps.exif_transpose(im)
        if max(im.size) <= MAX_EDGE and path.stat().st_size < 900_000 and path.name == target.name:
            print(f"  skip  {path.relative_to(ROOT)}")
            return
        im.thumbnail((MAX_EDGE, MAX_EDGE), Image.LANCZOS)
        im.convert("RGB").save(
            scratch, "JPEG", quality=QUALITY, optimize=True, progressive=True
        )

    path.unlink()
    scratch.rename(target)
    kb = target.stat().st_size // 1024
    print(f"  wrote {target.relative_to(ROOT)}  ({kb} KB)")


def main() -> int:
    if not ROOT.is_dir():
        print(f"no such directory: {ROOT}", file=sys.stderr)
        return 1
    for path in sorted(ROOT.rglob("*")):
        if path.is_file() and path.suffix.lower() in SUFFIXES:
            optimize(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
