#!/usr/bin/env python3
"""Downsize portrait originals so the repo stays small.

Hugo never renders a portrait larger than 256px, so originals above 800px on
the long edge only add weight to every clone. Run from VRS2026/:

    python3 tools/shrink-portraits.py assets/img/people/*.jpg

Requires Pillow (pip install pillow). Files already within the limit are left
untouched; WebP/AVIF files are skipped (already small).
"""
import sys
from pathlib import Path
from PIL import Image, ImageOps

MAX_EDGE = 800

for arg in sys.argv[1:]:
    path = Path(arg)
    if not path.is_file() or path.suffix.lower() not in {".jpg", ".jpeg", ".png"}:
        continue
    with Image.open(path) as im:
        im = ImageOps.exif_transpose(im)
        if max(im.size) <= MAX_EDGE:
            print(f"ok      {path} ({im.width}x{im.height})")
            continue
        before = path.stat().st_size
        im.thumbnail((MAX_EDGE, MAX_EDGE), Image.LANCZOS)
        if path.suffix.lower() == ".png":
            im.save(path, optimize=True)
        else:
            im = im.convert("RGB")
            im.save(path, "JPEG", quality=88, optimize=True, progressive=True)
        print(f"shrunk  {path} -> {im.width}x{im.height}, {before//1024} KB -> {path.stat().st_size//1024} KB")
