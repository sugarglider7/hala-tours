#!/usr/bin/env python3
"""Turn selected research/raw/images/* into site/assets/img/*.webp (sequential, Pillow).

Reads tools/images.json (declarative list), writes:
  site/assets/img/<name>-<w>.webp      one per width (never upscaled)
  site/assets/img/<og>.jpg             1200x630 social image
  site/apple-touch-icon.png, site/favicon-32.png  (brand sun mark)
  tools/content/images.gen.json        sizes, dominant colour, LQIP data URI -> read by build.py
Run: python3 tools/images.py
"""
import base64, io, json, os
from PIL import Image, ImageDraw, ImageOps

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(REPO, "research", "raw", "images")
OUT = os.path.join(REPO, "site", "assets", "img")
GEN = os.path.join(REPO, "tools", "content", "images.gen.json")

SUN, COBALT, PAPER = (243, 152, 0), (27, 35, 144), (255, 252, 246)


def open_src(rel):
    im = Image.open(os.path.join(RAW, rel))
    im.draft("RGB", (4000, 4000))
    return ImageOps.exif_transpose(im).convert("RGB")


def dominant(im):
    small = im.copy(); small.thumbnail((64, 64))
    q = small.quantize(colors=5, method=Image.Quantize.MEDIANCUT)
    pal = q.getpalette(); counts = sorted(q.getcolors(), reverse=True)
    i = counts[0][1]
    return "#%02x%02x%02x" % tuple(pal[i * 3:i * 3 + 3])


def lqip(im):
    t = im.copy(); t.thumbnail((20, 20))
    buf = io.BytesIO(); t.save(buf, "WEBP", quality=40)
    return "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode()


def favicons():
    for size, name in ((180, "apple-touch-icon.png"), (32, "favicon-32.png")):
        s = size * 4
        im = Image.new("RGB", (s, s), COBALT)
        d = ImageDraw.Draw(im)
        r = s * 0.34; cx, cy = s / 2, s * 0.56
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=SUN)
        # the "h" of Hala, drawn as strokes so no font file is needed
        w = s * 0.085
        d.rounded_rectangle((s * 0.36, s * 0.22, s * 0.36 + w, s * 0.74), radius=w / 2, fill=PAPER)
        d.rounded_rectangle((s * 0.56, s * 0.47, s * 0.56 + w, s * 0.74), radius=w / 2, fill=PAPER)
        d.arc((s * 0.36, s * 0.40, s * 0.56 + w, s * 0.62), 180, 360, fill=PAPER, width=int(w))
        im.resize((size, size), Image.LANCZOS).save(os.path.join(REPO, "site", name), optimize=True)


def main():
    spec = json.load(open(os.path.join(REPO, "tools", "images.json")))
    q = spec.get("quality", 75)
    os.makedirs(OUT, exist_ok=True)
    gen = {}
    for item in spec["images"]:                      # one image at a time
        im = open_src(item["src"])
        if item.get("crop"): im = im.crop(tuple(item["crop"]))
        entry = {"w": im.width, "h": im.height, "color": dominant(im), "lqip": lqip(im),
                 "alt": item.get("alt", ""), "variants": []}
        if item.get("credit"): entry["credit"] = item["credit"]
        for w in sorted(item["widths"], reverse=True):
            if w > im.width: continue
            h = round(im.height * w / im.width)
            v = im.resize((w, h), Image.LANCZOS)
            fn = f"{item['name']}-{w}.webp"
            v.save(os.path.join(OUT, fn), "WEBP", quality=q, method=6)
            entry["variants"].append({"w": w, "h": h, "file": fn, "kb": os.path.getsize(os.path.join(OUT, fn)) // 1024})
            v.close()
        im.close()
        gen[item["name"]] = entry
        print(item["name"], [(v["w"], v["kb"]) for v in entry["variants"]], entry["color"])
    og = spec.get("og")
    if og:
        im = open_src(og["src"])
        if og.get("crop"): im = im.crop(tuple(og["crop"]))
        im = im.resize(tuple(og["size"]), Image.LANCZOS)
        im.save(os.path.join(OUT, og["name"] + ".jpg"), "JPEG", quality=80, optimize=True, progressive=True)
        gen["_og"] = {"file": og["name"] + ".jpg", "w": og["size"][0], "h": og["size"][1]}
        im.close()
    favicons()
    os.makedirs(os.path.dirname(GEN), exist_ok=True)
    json.dump(gen, open(GEN, "w"), indent=1)
    print("wrote", os.path.relpath(GEN, REPO))


if __name__ == "__main__":
    main()
