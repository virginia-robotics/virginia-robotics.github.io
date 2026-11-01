#!/usr/bin/env python3
"""Render the 1200x630 link-preview image (Open Graph / Twitter card).

Reads the hero image, date, venue and location from hugo.toml and writes
static/img/social-card.jpg. Run from VRS2026/ whenever those change:

    python3 tools/make-social-card.py

For an archived year, override the text and output path, e.g.:

    python3 tools/make-social-card.py --line2 "November 14, 2025" \
        --line3 "Link Lab · Charlottesville, VA" \
        --out static/2025/assets/img/social-card.jpg

Requires Pillow (pip install pillow). The text is set in Lato Bold if the
system has it (sudo apt install fonts-lato), otherwise DejaVu Sans Bold.
"""
import argparse
import tomllib
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

W, H = 1200, 630
cfg = tomllib.loads(Path("hugo.toml").read_text())
p = cfg["params"]
ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("--title", default="Virginia Robotics Symposium")
ap.add_argument("--line2", help="second line (default: dateline · timeRange from hugo.toml)")
ap.add_argument("--line3", help="third line (default: venue · location from hugo.toml)")
ap.add_argument("--out", default="static/img/social-card.jpg", type=Path)
args = ap.parse_args()
title = args.title
line2 = args.line2 or p["dateline"] + ((" · " + p["timeRange"]) if p.get("timeRange") else "")
line3 = args.line3 or f'{p["venue"]} · {p["location"]}'
accent = tuple(int(p["colors"]["accentLight"].lstrip("#")[i:i+2], 16) for i in (0, 2, 4))

def font(size):
    for f in ("/usr/share/fonts/truetype/lato/Lato-Bold.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"):
        if Path(f).exists():
            return ImageFont.truetype(f, size)
    return ImageFont.load_default(size)

# Background: hero photo, cover-cropped, with the same dark gradient as the hero section.
bg = Image.open(Path("assets") / p["heroImage"]).convert("RGB")
bg = ImageOps.fit(bg, (W, H), Image.LANCZOS)
overlay = Image.new("RGB", (W, H))
top, bottom = (40, 0, 20), (0, 0, 0)
for y in range(H):
    t = y / (H - 1)
    overlay.paste(tuple(int(top[i] * (1 - t) + bottom[i] * t) for i in range(3)), (0, y, W, y + 1))
alpha = Image.linear_gradient("L").resize((W, H))          # 0 at top -> 255 at bottom
alpha = alpha.point(lambda v: int(255 * (0.68 + 0.14 * v / 255)))
bg = Image.composite(overlay, bg, alpha)

d = ImageDraw.Draw(bg)
def centered(text, y, size, fill):
    f = font(size)
    w = d.textlength(text, font=f)
    d.text(((W - w) / 2 + 2, y + 2), text, font=f, fill=(0, 0, 0))   # soft shadow
    d.text(((W - w) / 2, y), text, font=f, fill=fill)
    return f.size

centered(title, 215, 78, (255, 255, 255))
centered(line2, 330, 42, accent)
centered(line3, 400, 30, (235, 235, 235))

out = args.out
bg.save(out, "JPEG", quality=85, optimize=True, progressive=True)
print(f"wrote {out} ({out.stat().st_size // 1024} KB)")
