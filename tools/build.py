#!/usr/bin/env python3
"""Render site/ for Hala Tours Agadir from per-language content + partials (stdlib only).

    python3 tools/images.py   # only when tools/images.json changes
    python3 tools/build.py

Content:  tools/content/catalogue.json (structure, language-neutral)
          tools/content/en.json (+ fr.json with the same keys in phase 3)
Images:   tools/content/images.gen.json (written by tools/images.py)
Map data: tools/data/osm-hamilton.json (OSM extract for the desk locator)
Pages:    PAGES below. A page renders only if its renderer is in RENDER and its language file
          exists; links to pages that are not built yet fall back to a homepage anchor, so
          nothing ever points at a missing file.
"""
import hashlib
import html
import json
import math
import os
from urllib.parse import quote

TOOLS = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(TOOLS)
SITE = os.path.join(REPO, "site")
ORIGIN = "https://hala-tours.peashoot.io"

CAT = json.load(open(os.path.join(TOOLS, "content", "catalogue.json")))
IMG = json.load(open(os.path.join(TOOLS, "content", "images.gen.json")))
OSM = json.load(open(os.path.join(TOOLS, "data", "osm-hamilton.json")))
C = CAT["contact"]
WA_BASE = "https://wa.me/" + C["wa"]
TEL = "tel:" + C["phone_tel"]
MOOD = {m["id"]: m for m in CAT["moods"]}
PRODUCTS = CAT["products"]

# page key -> URL per language; anchor = homepage fallback while the page is not built.
PAGES = {
    "home": {"en": "/", "fr": "/fr/", "anchor": ""},
    "days": {"en": "/days/", "fr": "/fr/sorties/", "anchor": "#guide"},
    "visit": {"en": "/visit/", "fr": "/fr/nous-trouver/", "anchor": "#desk"},
    "transfers": {"en": "/transfers/", "fr": "/fr/transferts/", "anchor": "#transfers"},
    "plan": {"en": "/plan/", "fr": "/fr/organiser/", "anchor": "#plan"},
    "credits": {"en": "/credits/", "fr": "/fr/credits/", "anchor": ""},
}
BUILT = set()  # (page, lang) pairs rendered this run — filled before rendering


def e(s):
    return html.escape(str(s), quote=True)


def ver(rel):
    with open(os.path.join(SITE, "assets", rel), "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8]


def url(page, lang, frag=""):
    if (page, lang) in BUILT:
        return PAGES[page][lang] + frag
    return PAGES["home"][lang] + (frag or PAGES[page]["anchor"])


def wa(text):
    return WA_BASE + "?text=" + quote(text)


# ---------------------------------------------------------------- images
def img(name, sizes, alt=None, cls="", lazy=True, priority=False):
    m = IMG[name]
    v = m["variants"]
    big = v[0]
    srcset = ", ".join(f"/assets/img/{x['file']} {x['w']}w" for x in v)
    src = v[-1]["file"] if lazy else v[min(1, len(v) - 1)]["file"]
    attrs = [f'src="/assets/img/{src}"', f'srcset="{srcset}"', f'sizes="{sizes}"',
             f'width="{big["w"]}" height="{big["h"]}"', f'alt="{e(alt if alt is not None else m["alt"])}"',
             f'style="background:{m["color"]} url({m["lqip"]}) center/cover"']
    if cls: attrs.append(f'class="{cls}"')
    attrs.append('loading="lazy" decoding="async"' if lazy else 'decoding="async"')
    if priority: attrs.append('fetchpriority="high"')
    return "<img " + " ".join(attrs) + ">"


def hero_picture():
    d, m = IMG["hero-horses"], IMG["hero-horses-m"]
    ms = ", ".join(f"/assets/img/{x['file']} {x['w']}w" for x in m["variants"])
    ds = ", ".join(f"/assets/img/{x['file']} {x['w']}w" for x in d["variants"])
    return (f'<picture class="hero__pic">'
            f'<source media="(max-width: 47.99em)" srcset="{ms}" sizes="100vw" width="{m["w"]}" height="{m["h"]}">'
            f'<img src="/assets/img/{d["variants"][1]["file"]}" srcset="{ds}" sizes="(min-width: 48em) 52vw, 100vw" '
            f'width="{d["w"]}" height="{d["h"]}" alt="{e(d["alt"])}" fetchpriority="high" decoding="async" '
            f'style="background:{d["color"]} url({d["lqip"]}) center/cover"></picture>')


# ---------------------------------------------------------------- icons (inline sprite)
SPRITE = """<svg xmlns="http://www.w3.org/2000/svg" class="sprite" aria-hidden="true" focusable="false">
<symbol id="i-wa" viewBox="0 0 24 24"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2c-1.5 0-3-.4-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2c0 1.3.9 2.5 1.1 2.7.1.2 1.8 2.8 4.4 3.9 1.6.7 2.3.8 3.1.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3Z"/></symbol>
<symbol id="i-phone" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M5 3h3.5l1.7 4.3-2.3 1.5a11 11 0 0 0 7.3 7.3l1.5-2.3L21 15.5V19a2 2 0 0 1-2 2A17 17 0 0 1 3 5a2 2 0 0 1 2-2Z"/></symbol>
<symbol id="i-plus" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" d="M12 5v14M5 12h14"/></symbol>
<symbol id="i-check" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" d="m5 12.5 4.5 4.5L19 7.5"/></symbol>
<symbol id="i-star" viewBox="0 0 24 24"><path fill="currentColor" d="m12 2.8 2.8 5.9 6.4.8-4.7 4.4 1.2 6.4L12 17.2l-5.7 3.1 1.2-6.4-4.7-4.4 6.4-.8Z"/></symbol>
<symbol id="i-arrow" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" d="M5 12h14m-6-6 6 6-6 6"/></symbol>
<symbol id="i-pin" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2" d="M12 21s7-6.2 7-11.5a7 7 0 1 0-14 0C5 14.8 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.5" fill="currentColor"/></symbol>
<symbol id="i-mail" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" d="M3 6h18v12H3zM3 6l9 7 9-7"/></symbol>
<symbol id="i-menu" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" d="M4 7h16M4 12h16M4 17h10"/></symbol>
<symbol id="i-close" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" d="m6 6 12 12M18 6 6 18"/></symbol>
<symbol id="len-hours" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-opacity=".28" stroke-width="3"/><path d="M12 3a9 9 0 0 1 9 9" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></symbol>
<symbol id="len-half" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-opacity=".28" stroke-width="3"/><path d="M12 3a9 9 0 0 1 0 18" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></symbol>
<symbol id="len-full" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="3"/><circle cx="12" cy="12" r="4" fill="currentColor"/></symbol>
<symbol id="len-two" viewBox="0 0 32 24"><circle cx="10" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="3"/><circle cx="22" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="3"/></symbol>
<symbol id="i-scribble" viewBox="0 0 60 40"><path fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" d="M4 6c14 2 30 9 40 24m0 0-9-2m9 2 1-9"/></symbol>
</svg>"""


def icon(name, cls="ico"):
    return f'<svg class="{cls}" aria-hidden="true" focusable="false"><use href="#{name}"/></svg>'


def len_glyph(length):
    w = 32 if length == "two" else 24
    return f'<svg class="len" width="{w}" height="24" aria-hidden="true" focusable="false"><use href="#len-{length}"/></svg>'


# ---------------------------------------------------------------- maps
def day_map_svg(t):
    """Sketch map of Agadir and the day-trip destinations (equirectangular, cos-lat scaled)."""
    lon0, lon1, lat0, lat1 = -10.7, -7.7, 29.25, 31.85
    k = math.cos(math.radians(30.5))
    W = 520
    H = round(W * (lat1 - lat0) / ((lon1 - lon0) * k))

    def P(lat, lon):
        return (round((lon - lon0) / (lon1 - lon0) * W, 1), round((lat1 - lat) / (lat1 - lat0) * H, 1))

    coast = [P(a, b) for a, b in CAT["map_extra"]["coast"]]
    ocean = " ".join(f"{x},{y}" for x, y in coast) + f" -20,{coast[-1][1] + 60} -20,-20 {coast[0][0]},-20"
    ax, ay = P(*CAT["map_extra"]["agadir"])
    # label offsets (dx, dy, anchor) chosen by eye to avoid collisions
    lab = {"paradise-valley": (-12, -10, "end"), "essaouira": (12, 6, "start"), "marrakech": (-14, 6, "end"),
           "taroudant": (0, -16, "middle"), "tafraout": (13, 6, "start"), "legzira": (13, 6, "start"),
           "little-desert": (13, 6, "start")}
    out = [f'<svg class="daymap__svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="daymap-t">',
           f'<title id="daymap-t">{e(t["map"]["title"])}</title>',
           f'<polygon class="dm-ocean" points="{ocean}"/>',
           '<polyline class="dm-coast" points="' + " ".join(f"{x},{y}" for x, y in coast) + '"/>',
           f'<text class="dm-ocean-l" x="44" y="{H * 0.6:.0f}" transform="rotate(-80 44 {H * 0.6:.0f})">{e(t["map"]["ocean"])}</text>']
    pts = []
    for p in PRODUCTS:
        if p.get("map") and p["id"] != "zagora":
            pts.append(p)
    for p in pts:
        x, y = P(*p["map"])
        mx, my = (ax + x) / 2, (ay + y) / 2
        dx, dy = x - ax, y - ay
        cx, cy = mx - dy * 0.18, my + dx * 0.18
        out.append(f'<path class="dm-route c-{MOOD[p["mood"]]["color"]}" d="M{ax},{ay} Q{cx:.1f},{cy:.1f} {x},{y}"/>')
    # Zagora: off the map to the east
    zx, zy = P(30.33, -7.75)
    out.append(f'<path class="dm-route c-cobalt" d="M{ax},{ay} Q{(ax + zx) / 2:.1f},{zy + 40:.1f} {zx - 6},{zy}"/>')
    out.append(f'<a href="#day-zagora" class="dm-place"><path class="dm-arrow" d="M{zx - 14},{zy - 8} {zx},{zy} {zx - 14},{zy + 8}"/>'
               f'<text x="{zx - 6}" y="{zy - 14}" text-anchor="end">{e(t["map"]["zagora_arrow"])} →</text></a>')
    for nm, key in (("Tiznit", "tiznit"), ("Tiout", "tiout")):
        x, y = P(*CAT["map_extra"][key])
        out.append(f'<g class="dm-minor"><circle cx="{x}" cy="{y}" r="3.5"/><text x="{x + 8}" y="{y + 4}">{nm}</text></g>')
    for p in pts:
        x, y = P(*p["map"])
        dx, dy, anc = lab.get(p["id"], (10, 4, "start"))
        name = t["map"]["labels"][p["id"]]
        out.append(f'<a href="#day-{p["id"]}" class="dm-place" aria-label="{e(t["products"][p["id"]]["name"])}"><circle class="dm-dot c-{MOOD[p["mood"]]["color"]}" cx="{x}" cy="{y}" r="8"/>'
                   f'<text x="{x + dx}" y="{y + dy}" text-anchor="{anc}">{e(name)}</text></a>')
    out.append(f'<g class="dm-home"><circle cx="{ax}" cy="{ay}" r="15"/><circle class="dm-home-c" cx="{ax}" cy="{ay}" r="5"/>'
               f'<text x="{ax + 22}" y="{ay + 2}" class="dm-home-l">{e(t["map"]["agadir"])}</text>'
               f'<text x="{ax + 22}" y="{ay + 22}" class="dm-home-s">{e(t["map"]["desk"])}</text></g>')
    out.append("</svg>")
    return "".join(out)


def locator_svg(t):
    """Street locator around the Hotel Hamilton from the OSM extract."""
    lat0, lat1, lon0, lon1 = 30.4096, 30.4160, -9.6036, -9.5936
    k = math.cos(math.radians(30.41))
    W = 600
    H = round(W * (lat1 - lat0) / ((lon1 - lon0) * k))

    def XY(lat, lon):
        return (lon - lon0) / (lon1 - lon0) * W, (lat1 - lat) / (lat1 - lat0) * H

    def P(lat, lon):
        x, y = XY(lat, lon)
        return f"{x:.0f},{y:.0f}"

    def visible(pts, m=0.0006):
        return any(lat0 - m < a < lat1 + m and lon0 - m < b < lon1 + m for a, b in pts)

    def simplify(xy, tol=1.6):
        """Ramer–Douglas–Peucker in pixel space (keeps the inline SVG small)."""
        if len(xy) < 3: return xy
        (x1, y1), (x2, y2) = xy[0], xy[-1]
        dx, dy = x2 - x1, y2 - y1
        n = math.hypot(dx, dy)
        dmax, idx = 0, 0
        for i in range(1, len(xy) - 1):
            dd = abs(dy * xy[i][0] - dx * xy[i][1] + x2 * y1 - y2 * x1) / n if n > 1e-6 else math.hypot(xy[i][0] - x1, xy[i][1] - y1)
            if dd > dmax: dmax, idx = dd, i
        if dmax <= tol: return [xy[0], xy[-1]]
        return simplify(xy[:idx + 1], tol)[:-1] + simplify(xy[idx:], tol)

    def area(xy):
        return abs(sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in zip(xy, xy[1:] + xy[:1]))) / 2

    cls = {"hw:primary": "lm-primary", "hw:primary_link": "lm-primary", "hw:secondary": "lm-primary", "hw:tertiary": "lm-tertiary",
           "hw:residential": "lm-minor", "hw:living_street": "lm-minor", "hw:service": "lm-service", "hw:pedestrian": "lm-ped",
           "hw:footway": "lm-foot", "leis:park": "lm-green", "land:grass": "lm-green", "leis:pitch": "lm-green",
           "leis:swimming_pool": "lm-pool", "nat:beach": "lm-beach", "nat:coastline": "lm-coast", "bld": "lm-bld"}
    areas = ("leis:park", "land:grass", "leis:pitch", "leis:swimming_pool", "nat:beach", "bld")
    order = ["nat:beach", "leis:park", "land:grass", "leis:pitch", "leis:swimming_pool", "bld", "hw:pedestrian", "hw:service",
             "hw:living_street", "hw:residential", "hw:tertiary", "hw:primary_link", "hw:secondary", "hw:primary", "nat:coastline"]
    out = [f'<svg class="locator__svg" viewBox="0 0 {W} {H}" role="img" aria-label="{e(t["desk"]["map_alt"])}">',
           f'<rect width="{W}" height="{H}" class="lm-bg"/>']
    for kind in order:
        group = []
        for w in OSM["ways"]:
            if w["k"] != kind or not visible(w["pts"]): continue
            closed = kind in areas and w["pts"][0] == w["pts"][-1]
            xy = simplify([XY(a, b) for a, b in w["pts"]])
            if closed and (len(xy) < 4 or area(xy) < 40): continue
            pts = " ".join(dict.fromkeys(f"{x:.0f},{y:.0f}" for x, y in xy))
            group.append(f'<{"polygon" if closed else "polyline"} points="{pts}"/>')
        if group: out.append(f'<g class="{cls[kind]}">' + "".join(group) + "</g>")

    def street_label(prefix, text, kinds=("hw:primary",), dy=-12):
        best = None
        for w in OSM["ways"]:
            if w["k"] in kinds and (w["name"] or "").startswith(prefix):
                for (a1, b1), (a2, b2) in zip(w["pts"], w["pts"][1:]):
                    if all(lat0 + .0004 < a < lat1 - .0004 and lon0 + .0004 < b < lon1 - .0004 for a, b in ((a1, b1), (a2, b2))):
                        L = math.hypot(a2 - a1, (b2 - b1) * k)
                        if not best or L > best[0]: best = (L, a1, b1, a2, b2)
        if not best: return
        _, a1, b1, a2, b2 = best
        (x1, y1), (x2, y2) = XY(a1, b1), XY(a2, b2)
        if x2 < x1: x1, y1, x2, y2 = x2, y2, x1, y1
        ang = math.degrees(math.atan2(y2 - y1, x2 - x1))
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        out.append(f'<text class="lm-street" x="{mx:.0f}" y="{my:.0f}" dy="{dy}" text-anchor="middle" transform="rotate({ang:.1f} {mx:.0f} {my:.0f})">{e(text)}</text>')

    street_label("Avenue Mohammed V", "Avenue Mohammed V")
    street_label("Boulevard du 20 Août", "Bd du 20 Août", ("hw:tertiary", "hw:residential"), dy=-8)
    beach = [XY(a, b) for w in OSM["ways"] if w["k"] == "nat:beach" for a, b in w["pts"] if lat0 < a < lat1 and lon0 < b < lon1]
    if beach:
        bx = max(56, sum(x for x, _ in beach) / len(beach)); by = sum(y for _, y in beach) / len(beach)
        out.append(f'<text class="lm-beachl" x="{bx:.0f}" y="{by:.0f}" text-anchor="middle">{e(t["desk"]["beach"])}</text>')
    out.append('<polygon class="lm-hotel" points="' + " ".join(P(a, c) for a, c in OSM["pin_building"]) + '"/>')
    px, py = XY(*C["geo"])
    out.append(f'<g class="lm-pin"><circle cx="{px:.0f}" cy="{py:.0f}" r="22"/><circle cx="{px:.0f}" cy="{py:.0f}" r="7" class="lm-pin-c"/></g>')
    lx = px - 254 if px > 280 else px + 30
    out.append(f'<g class="lm-label"><rect x="{lx:.0f}" y="{py - 64:.0f}" width="224" height="56" rx="10"/>'
               f'<text x="{lx + 16:.0f}" y="{py - 40:.0f}" class="lm-l1">Hala Tours Agadir</text>'
               f'<text x="{lx + 16:.0f}" y="{py - 18:.0f}" class="lm-l2">Hotel Hamilton</text></g>')
    out.append(f'<text x="{W - 10}" y="{H - 10}" text-anchor="end" class="lm-osm">{e(t["desk"]["osm"])}</text></svg>')
    return "".join(out)


# ---------------------------------------------------------------- partials
def head(t, page, lang, title, desc):
    canon = ORIGIN + PAGES[page][lang]
    alts = ""
    for l2 in ("en", "fr"):
        if (page, l2) in BUILT:
            alts += f'<link rel="alternate" hreflang="{l2}" href="{ORIGIN}{PAGES[page][l2]}">'
    if alts and ("fr" in [l for p, l in BUILT if p == page]):
        alts += f'<link rel="alternate" hreflang="x-default" href="{ORIGIN}{PAGES[page]["en"]}">'
    og = IMG["_og"]
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canon}">{alts}
<meta name="theme-color" content="#1b2390">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Hala Tours Agadir">
<meta property="og:title" content="{e(t['meta']['og_title'])}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{ORIGIN}/assets/img/{og['file']}">
<meta property="og:image:width" content="{og['w']}">
<meta property="og:image:height" content="{og['h']}">
<meta property="og:locale" content="{t['locale']}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/bricolage-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/site.css?v={ver('css/site.css')}">
<script src="/assets/js/site.js?v={ver('js/site.js')}" defer></script>
"""


def jsonld(t, lang):
    days = {"Mo": "Monday", "Tu": "Tuesday", "We": "Wednesday", "Th": "Thursday", "Fr": "Friday", "Sa": "Saturday", "Su": "Sunday"}
    data = {
        "@context": "https://schema.org", "@type": "TravelAgency", "name": "Hala Tours Agadir",
        "url": ORIGIN + PAGES["home"][lang], "image": f"{ORIGIN}/assets/img/{IMG['_og']['file']}",
        "telephone": C["phone_display"], "email": C["email"],
        "address": {"@type": "PostalAddress", "streetAddress": "Hotel Hamilton, Boulevard Mohammed V",
                    "addressLocality": "Agadir", "postalCode": "80000", "addressCountry": "MA"},
        "geo": {"@type": "GeoCoordinates", "latitude": C["geo"][0], "longitude": C["geo"][1]},
        "hasMap": C["maps_url"],
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": days[d], "opens": o, "closes": c}
                                      for d, o, c in C["hours"]],
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": C["rating"]["value"], "reviewCount": C["rating"]["count"], "bestRating": "5"},
        "areaServed": "Agadir", "knowsLanguage": ["en", "fr"],
    }
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"


def wordmark():
    return ('<span class="wm"><svg class="wm__sun" viewBox="0 0 40 40" aria-hidden="true" focusable="false">'
            '<circle cx="20" cy="20" r="13"/><path d="M20 1v5M20 34v5M1 20h5M34 20h5M6.6 6.6l3.5 3.5M29.9 29.9l3.5 3.5M6.6 33.4l3.5-3.5M29.9 10.1l3.5-3.5"/></svg>'
            '<span class="wm__name">Hala<span class="wm__rest"> Tours Agadir</span></span></span>')


def header(t, page, lang):
    u = t["ui"]
    home = url("home", lang)
    links = "".join(f'<li><a href="{e(h if page == "home" else home + h)}">{e(label)}</a></li>' for h, label in u["nav"])
    return f"""<a class="skip" href="#main">{e(u['skip'])}</a>
<header class="top" id="top">
  <div class="top__in">
    <a class="top__brand" href="{home}" aria-label="Hala Tours Agadir — home">{wordmark()}<span class="top__sub">{e(u['brand_sub'])}</span></a>
    <nav class="top__nav" aria-label="{e(u['nav_label'])}"><ul>{links}</ul></nav>
    <div class="top__act">
      <a class="top__call" href="{TEL}">{icon('i-phone')}<span>{e(C['phone_display'])}</span></a>
      <a class="btn btn--sun top__plan" href="{url('plan', lang)}">{icon('i-wa')}<span>{e(u['cta_plan'])}</span></a>
      <button class="top__menu" type="button" aria-expanded="false" aria-controls="sheet">{icon('i-menu')}<span>{e(u['menu'])}</span></button>
    </div>
  </div>
</header>"""


def sheet(t, page, lang):
    """Mobile menu: the mood tabs, big, plus the practical links."""
    u = t["ui"]
    home = url("home", lang)
    pre = "" if page == "home" else home
    tabs = "".join(f'<li><a class="tab tab--{m["color"]}" href="{pre}#mood-{m["id"]}">{e(t["moods"][m["id"]]["name"])}</a></li>' for m in CAT["moods"])
    links = "".join(f'<li><a href="{e(pre + h)}">{e(label)}</a></li>' for h, label in u["nav"][1:])
    return f"""<div class="sheet" id="sheet" hidden>
  <div class="sheet__in" role="dialog" aria-modal="true" aria-label="{e(u['menu'])}">
    <div class="sheet__top">{wordmark()}<button class="sheet__close" type="button">{icon('i-close')}<span>{e(u['close'])}</span></button></div>
    <p class="sheet__label">{e(t['hero']['moods_label'])}</p>
    <ul class="sheet__tabs">{tabs}</ul>
    <ul class="sheet__links">{links}<li><a href="{url('plan', lang)}">{e(t['plan']['kicker'])}</a></li></ul>
    <div class="sheet__contact"><a class="btn btn--sun" href="{wa(t['plan']['wa_simple'])}">{icon('i-wa')}{e(u['whatsapp'])}</a><a class="btn btn--line" href="{TEL}">{icon('i-phone')}{e(u['call'])}</a></div>
  </div>
</div>"""


def hero(t, lang):
    h = t["hero"]
    tabs = "".join(f'<li><a class="tab tab--{m["color"]}" href="#mood-{m["id"]}">{e(t["moods"][m["id"]]["name"])}</a></li>' for m in CAT["moods"])
    r = C["rating"]
    return f"""<section class="hero" aria-labelledby="hero-h">
  <div class="hero__text">
    <p class="hero__eyebrow">{e(h['eyebrow'])}</p>
    <h1 id="hero-h" class="hero__h">{e(h['h1'])}</h1>
  </div>
  <p class="hero__lede">{e(h['lede'])}</p>
  <div class="hero__media">{hero_picture()}<p class="note note--hero" aria-hidden="true">{e(h['note'])}</p></div>
  <nav class="hero__moods" aria-label="{e(h['moods_label'])}"><p class="hero__moods-l">{e(h['moods_label'])}</p><ul class="tabs">{tabs}</ul></nav>
  <div class="hero__proof">
    <a class="proof" href="#reviews"><span class="proof__stars">{icon('i-star')*5}</span><strong>{r['value']}</strong> {e(h['rating'])} · {e(h['rating_count'])}</a>
    <a class="status" href="#desk" data-status>{icon('i-pin')}<span data-status-text>{e(t['desk']['address'])}</span></a>
  </div>
</section>"""


def product_row(t, p, n):
    u = t["ui"]
    s = t["products"][p["id"]]
    lens = "".join(f'<span class="len-tag">{len_glyph(l)}{e(u["length_short"][l])}</span>' for l in p["lengths"])
    req = f'<span class="badge">{e(u["on_request"])}</span>' if p["status"] == "on_request" else ""
    return (f'<li class="day" id="day-{p["id"]}" data-lengths="{" ".join(p["lengths"])}">'
            f'<div class="day__len">{lens}</div>'
            f'<h3 class="day__name">{e(s["name"])}{req}</h3>'
            f'<p class="day__line">{e(s["line"])}</p>'
            f'<button class="day__add" type="button" data-pick="{p["id"]}" aria-pressed="false">'
            f'<span class="day__add-off">{icon("i-plus")}{e(u["add"])}</span><span class="day__add-on">{icon("i-check")}{e(u["added"])}</span></button></li>')


def chapter(t, m, i):
    mt = t["moods"][m["id"]]
    items = [p for p in PRODUCTS if p["mood"] == m["id"]]
    rows = "".join(product_row(t, p, n) for n, p in enumerate(items))
    if m["img"]:
        media = f'<figure class="ch__fig">{img(m["img"], "(min-width: 64em) 40vw, 92vw", cls="ch__img")}</figure>'
    else:
        places = ["Imouzzer", "Paradise Valley", "Taroudant", "Tiout", "Tafraout", "Ameln"] if m["id"] == "valleys" else []
        media = '<div class="ch__places" aria-hidden="true">' + "".join(f"<span>{e(x)}</span>" for x in places) + "</div>"
    note = f'<p class="note note--ch">{icon("i-scribble", "note__arrow")}{e(mt["note"])}</p>' if mt.get("note") else ""
    side = " ch--flip" if i % 2 else ""
    return f"""<section class="ch ch--{m['color']}{side}" id="mood-{m['id']}" aria-labelledby="mood-{m['id']}-h" data-mood="{m['id']}">
  <header class="ch__band">
    <p class="ch__num">{e(t['guide']['chapter'].format(n=i + 1))}</p>
    <h2 class="ch__h" id="mood-{m['id']}-h">{e(mt['name'])}</h2>
    <p class="ch__intro">{e(mt['intro'])}</p>
  </header>
  <div class="ch__body">
    <div class="ch__media">{media}{note}</div>
    <ul class="ch__days">{rows}</ul>
    <p class="ch__none" hidden>{e(t['guide']['none_here'])}</p>
  </div>
</section>"""


def guide(t, lang):
    g, u = t["guide"], t["ui"]
    chips = f'<button type="button" class="chip" data-len="" aria-pressed="true">{e(g["filter_all"])}</button>' + "".join(
        f'<button type="button" class="chip" data-len="{l}" aria-pressed="false">{len_glyph(l)}{e(u["lengths"][l])}</button>' for l in CAT["lengths"])
    chapters = "\n".join(chapter(t, m, i) for i, m in enumerate(CAT["moods"]))
    index = "".join(f'<li><a class="thumb thumb--{m["color"]}" href="#mood-{m["id"]}" data-thumb="{m["id"]}" aria-label="{e(t["moods"][m["id"]]["name"])}"><span>{e(t["moods"][m["id"]]["short"])}</span></a></li>' for m in CAT["moods"])
    return f"""<section class="guide" id="guide" aria-labelledby="guide-h">
  <div class="guide__head">
    <p class="kicker">{e(g['kicker'])}</p>
    <h2 class="guide__h" id="guide-h">{e(g['title'])}</h2>
    <div class="lenbar" role="group" aria-label="{e(g['filter_label'])}"><p class="lenbar__l">{e(g['filter_label'])}</p><div class="lenbar__chips">{chips}</div></div>
  </div>
  <nav class="thumbs" aria-label="{e(t['hero']['moods_label'])}"><ul>{index}</ul></nav>
{chapters}
</section>"""


def daymap(t):
    m = t["map"]
    return f"""<section class="daymap" id="map" aria-labelledby="map-h">
  <div class="daymap__text">
    <p class="kicker">{e(m['kicker'])}</p>
    <h2 id="map-h" class="sec-h">{e(m['title'])}</h2>
    <p>{e(m['text'])}</p>
    <p class="daymap__cap">{e(m['caption'])}</p>
  </div>
  <div class="daymap__map">{day_map_svg(t)}</div>
</section>"""


def reviews(t):
    r = t["reviews"]
    items = "".join(f'<li class="rv rv--{i}"><blockquote><p>“{e(x["q"])}”</p></blockquote><p class="rv__by">{e(x["by"])} · {e(r["platform"])}</p></li>'
                    for i, x in enumerate(r["items"]))
    return f"""<section class="reviews" id="reviews" aria-labelledby="rv-h">
  <div class="reviews__head">
    <p class="kicker">{e(r['kicker'])}</p>
    <h2 id="rv-h" class="sec-h"><span class="reviews__big">{icon('i-star')}{C['rating']['value']}</span> {e(r['title'])}</h2>
    <a class="link" href="{C['maps_url']}" rel="noopener">{e(r['link'])}{icon('i-arrow')}</a>
  </div>
  <ul class="reviews__list">{items}</ul>
</section>"""


def desk(t, lang):
    d, u = t["desk"], t["ui"]
    hours = "".join(f"<tr><th scope=\"row\">{e(a)}</th><td>{e(b)}</td></tr>" for a, b in u["days_range"])
    facts = "".join(f"<li><strong>{e(a)}</strong> {e(b)}</li>" for a, b in d["facts"])
    tr = t["transfers"]
    return f"""<section class="desk" id="desk" aria-labelledby="desk-h">
  <div class="desk__text">
    <p class="kicker">{e(d['kicker'])}</p>
    <h2 id="desk-h" class="sec-h">{e(d['title'])}</h2>
    <p class="desk__p">{e(d['text'])}</p>
    <address class="desk__addr">{icon('i-pin')}<span>{e(d['address'])}</span></address>
    <div class="desk__hours"><p class="desk__ht">{e(d['hours_title'])} <span class="desk__now" data-status-badge hidden></span></p><table>{hours}</table></div>
    <div class="desk__btns">
      <a class="btn btn--ink" href="{C['maps_url']}" rel="noopener">{icon('i-pin')}{e(d['maps'])}</a>
      <a class="btn btn--line" href="{TEL}">{icon('i-phone')}{e(C['phone_display'])}</a>
    </div>
  </div>
  <figure class="desk__map">{locator_svg(t)}<p class="note note--desk">{e(d['note'])}</p></figure>
  <ul class="desk__facts">{facts}</ul>
  <figure class="desk__photo">{img('minibus-smiles', '(min-width: 64em) 30vw, 80vw', cls='desk__img')}<figcaption>{e(d['photo_caption'])}</figcaption></figure>
  <div class="transfers" id="transfers">
    <p class="kicker">{e(tr['kicker'])}</p>
    <h3 class="transfers__h">{e(tr['title'])}</h3>
    <p>{e(tr['text'])}</p>
    <a class="link" href="{wa(tr['wa'])}">{icon('i-wa')}{e(tr['cta'])}</a>
  </div>
</section>"""


def planner(t, lang):
    p, u = t["plan"], t["ui"]
    moods = "".join(f'<label class="mchip mchip--{m["color"]}"><input type="checkbox" name="mood" value="{m["id"]}"><span>{e(t["moods"][m["id"]]["name"])}</span></label>' for m in CAT["moods"])
    lens = "".join(f'<label class="lchip"><input type="radio" name="length" value="{l}"><span>{len_glyph(l)}{e(u["lengths"][l])}</span></label>' for l in CAT["lengths"])
    lens += f'<label class="lchip"><input type="radio" name="length" value="" checked><span>{e(p["length_any"])}</span></label>'
    return f"""<section class="plan" id="plan" aria-labelledby="plan-h">
  <div class="plan__head">
    <p class="kicker">{e(p['kicker'])}</p>
    <h2 id="plan-h" class="sec-h">{e(p['title'])}</h2>
    <p>{e(p['text'])}</p>
  </div>
  <form class="planner" id="planner" novalidate>
    <fieldset class="f f--moods"><legend>{e(p['moods_label'])}</legend><div class="mchips">{moods}</div></fieldset>
    <div class="f f--picked"><p class="f__l">{e(p['picked_label'])}</p><ul class="picked" data-picked></ul><p class="picked__empty" data-picked-empty>{e(p['picked_empty'])}</p></div>
    <p class="err" id="err-what" data-err="what" hidden>{e(p['err_what'])}</p>
    <fieldset class="f f--len"><legend>{e(p['length_label'])}</legend><div class="lchips">{lens}</div></fieldset>
    <div class="f f--row">
      <div class="fld"><label for="f-date">{e(p['date_label'])}</label><input id="f-date" name="date" type="date" aria-describedby="f-date-h"><p class="hint" id="f-date-h">{e(p['date_hint'])}</p><p class="err" data-err="date" hidden>{e(p['err_date'])}</p></div>
      <div class="fld fld--num"><label for="f-adults">{e(p['adults_label'])}</label><input id="f-adults" name="adults" type="number" inputmode="numeric" min="1" max="60" value="2" required><p class="err" data-err="adults" hidden>{e(p['err_adults'])}</p></div>
      <div class="fld fld--num"><label for="f-kids">{e(p['kids_label'])}</label><input id="f-kids" name="kids" type="number" inputmode="numeric" min="0" max="40" value="0"></div>
      <div class="fld" data-ages hidden><label for="f-ages">{e(p['ages_label'])}</label><input id="f-ages" name="ages" type="text" placeholder="{e(p['ages_ph'])}" autocomplete="off"></div>
    </div>
    <div class="f f--row">
      <div class="fld"><label for="f-stay">{e(p['stay_label'])}</label><input id="f-stay" name="stay" type="text" placeholder="{e(p['stay_ph'])}" autocomplete="off"></div>
      <div class="fld"><label for="f-name">{e(p['name_label'])}</label><input id="f-name" name="name" type="text" autocomplete="given-name"></div>
    </div>
    <div class="fld"><label for="f-msg">{e(p['msg_label'])}</label><textarea id="f-msg" name="msg" rows="3" placeholder="{e(p['msg_ph'])}"></textarea></div>
    <div class="planner__go"><button class="btn btn--sun btn--big" type="submit">{icon('i-wa')}{e(p['submit'])}</button>
      <noscript><a class="link" href="{wa(p['wa_simple'])}">{e(p['nojs'])}</a></noscript></div>
    <div class="planner__ok" data-ok hidden tabindex="-1">
      <p class="planner__ok-h">{e(p['ok_title'])}</p><p>{e(p['ok_text'])}</p>
      <p class="planner__ok-links"><a class="btn btn--sun" data-retry href="{wa(p['wa_simple'])}">{icon('i-wa')}{e(p['retry'])}</a>
      <a class="link" href="{TEL}">{icon('i-phone')}{e(p['or_call'])} {e(C['phone_display'])}</a>
      <a class="link" data-mail href="mailto:{C['email']}">{icon('i-mail')}{e(p['or_mail'])} {e(C['email'])}</a></p>
    </div>
  </form>
</section>"""


def footer(t, lang):
    f, u = t["footer"], t["ui"]
    hours = " · ".join(f"{a} {b}" for a, b in u["days_range"])
    return f"""<footer class="foot" id="foot">
  <div class="foot__in">
    <div class="foot__brand">{wordmark()}<p>{e(f['line'])}</p></div>
    <div class="foot__col"><p class="foot__h">{e(f['visit'])}</p><p>{e(t['desk']['address'])}</p><p>{e(hours)}</p><p><a href="{C['maps_url']}" rel="noopener">{e(t['desk']['maps'])}</a></p></div>
    <div class="foot__col"><p class="foot__h">{e(f['contact'])}</p>
      <p><a href="{wa(t['plan']['wa_simple'])}">{icon('i-wa')}WhatsApp {e(C['phone_display'])}</a></p>
      <p><a href="{TEL}">{icon('i-phone')}{e(C['phone_display'])}</a></p>
      <p><a href="mailto:{C['email']}">{icon('i-mail')}{e(C['email'])}</a></p></div>
  </div>
  <p class="foot__small">{e(f['small'])}</p>
</footer>"""


def sticky(t, lang):
    u = t["ui"]
    return f"""<div class="dock" data-dock>
  <button class="dock__menu" type="button" aria-expanded="false" aria-controls="sheet">{icon('i-menu')}<span class="vh">{e(u['menu'])}</span></button>
  <a class="dock__plan" href="{url('plan', lang)}"><span class="dock__count" data-count hidden>0</span>{icon('i-wa')}<span data-dock-label>{e(u['sticky_idle'])}</span></a>
  <a class="dock__call" href="{TEL}">{icon('i-phone')}<span class="vh">{e(u['call'])} {e(C['phone_display'])}</span></a>
</div>"""


def page_data(t, lang):
    """Strings + facts the script needs (keeps site.js language-agnostic)."""
    p, u = t["plan"], t["ui"]
    data = {
        "wa": WA_BASE, "email": C["email"], "hours": C["hours"], "tz": "Africa/Casablanca",
        "lang": lang,
        "products": {x["id"]: t["products"][x["id"]]["name"] for x in PRODUCTS},
        "moods": {m["id"]: t["moods"][m["id"]]["name"] for m in CAT["moods"]},
        "lengths": u["lengths"],
        "s": {k: v for k, v in p.items() if k.startswith(("wa_", "mail_", "remove"))},
        "ui": {k: u[k] for k in ("open_now", "closed_now", "sticky_idle", "sticky_go")},
    }
    return '<script type="application/json" id="hala-data">' + json.dumps(data, ensure_ascii=False).replace("</", "<\\/") + "</script>"


# ---------------------------------------------------------------- pages
def render_home(t, lang):
    body = [header(t, "home", lang), sheet(t, "home", lang),
            '<main id="main">', hero(t, lang), guide(t, lang), daymap(t), reviews(t), desk(t, lang), planner(t, lang), "</main>",
            footer(t, lang), sticky(t, lang), SPRITE, page_data(t, lang), jsonld(t, lang)]
    return head(t, "home", lang, t["meta"]["title"], t["meta"]["description"]) + "</head>\n<body>\n" + "\n".join(body) + "\n</body>\n</html>\n"


def render_404(t, lang):
    n = t["notfound"]
    return f"""<!doctype html>
<html lang="{lang}">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(n['title'])}</title><meta name="robots" content="noindex">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<style>
body{{margin:0;min-height:100vh;display:grid;place-items:center;background:#1b2390;color:#fffcf6;font:18px/1.5 system-ui,sans-serif;padding:24px;box-sizing:border-box}}
main{{max-width:34rem}}h1{{font-size:clamp(2.2rem,8vw,3.6rem);line-height:1.02;margin:.2em 0 .4em;letter-spacing:-.02em}}
.sun{{width:72px;height:72px;border-radius:50%;background:#f39800}}a{{display:inline-block;margin:.4em 1em .4em 0;padding:.8em 1.2em;border-radius:999px;background:#f39800;color:#10143f;font-weight:700;text-decoration:none}}
a.alt{{background:transparent;color:#fffcf6;box-shadow:inset 0 0 0 2px #fffcf6}}
</style></head>
<body><main><div class="sun" aria-hidden="true"></div><h1>{e(n['h1'])}</h1><p>{e(n['text'])}</p>
<p><a href="{PAGES['home'][lang]}">{e(n['home'])}</a><a class="alt" href="{wa(t['plan']['wa_simple'])}">WhatsApp {e(C['phone_display'])}</a></p></main></body></html>
"""


RENDER = {"home": render_home}


def write(rel, text):
    path = os.path.join(SITE, rel.lstrip("/"))
    if rel.endswith("/"): path = os.path.join(path, "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return os.path.relpath(path, SITE)


def main():
    langs = {}
    for lang in ("en", "fr"):
        p = os.path.join(TOOLS, "content", f"{lang}.json")
        if os.path.exists(p): langs[lang] = json.load(open(p, encoding="utf-8"))
    for lang in langs:
        for page in RENDER:
            BUILT.add((page, lang))
    written = []
    for lang, t in langs.items():
        for page, fn in RENDER.items():
            written.append(write(PAGES[page][lang], fn(t, lang)))
    written.append(write("/404.html", render_404(langs["en"], "en")))
    # sitemap + robots + headers
    urls = "".join(f"<url><loc>{ORIGIN}{PAGES[p][l]}</loc></url>" for p, l in sorted(BUILT))
    write("/sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    write("/robots.txt", f"User-agent: *\nAllow: /\nSitemap: {ORIGIN}/sitemap.xml\n")
    write("/_headers", "/assets/*\n  Cache-Control: public, max-age=31536000, immutable\n/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n")
    print("built:", ", ".join(written))


if __name__ == "__main__":
    main()
