#!/usr/bin/env python3
"""Render site/ for Hala Tours Agadir — every page, EN at the root and FR under /fr/ (stdlib only).

    python3 tools/images.py   # only when tools/images.json changes
    python3 tools/build.py

Data:     tools/content/days.json      one record per day out (structure + EN/FR strings)
          tools/content/catalogue.json contact constant, moods, lengths, map geometry
          tools/content/en.json, fr.json  site chrome + page copy, same keys in both
Images:   tools/content/images.gen.json (written by tools/images.py; Commons files carry a credit block)
Map data: tools/data/osm-hamilton.json (OSM extract for the desk locator)
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
LANGS = ("en", "fr")


def load(*p):
    with open(os.path.join(TOOLS, *p), encoding="utf-8") as f:
        return json.load(f)


CAT = load("content", "catalogue.json")
DAYS = load("content", "days.json")["days"]
IMG = load("content", "images.gen.json")
OSM = load("data", "osm-hamilton.json")
T = {lang: load("content", f"{lang}.json") for lang in LANGS}
C = CAT["contact"]
WA_BASE = "https://wa.me/" + C["wa"]
TEL = "tel:" + C["phone_tel"]
MOOD = {m["id"]: m for m in CAT["moods"]}
DAY = {d["id"]: d for d in DAYS}

# page key -> URL per language
PAGES = {
    "home": {"en": "/", "fr": "/fr/"},
    "days": {"en": "/days/", "fr": "/fr/sorties/"},
    "where": {"en": "/where-we-go/", "fr": "/fr/ou-nous-allons/"},
    "visit": {"en": "/visit/", "fr": "/fr/nous-trouver/"},
    "reviews": {"en": "/reviews/", "fr": "/fr/avis/"},
    "transfers": {"en": "/transfers/", "fr": "/fr/transferts/"},
    "plan": {"en": "/plan/", "fr": "/fr/organiser/"},
    "credits": {"en": "/credits/", "fr": "/fr/credits/"},
}
for _m in CAT["moods"]:
    PAGES["mood:" + _m["id"]] = {"en": "/moods/" + T["en"]["moods"][_m["id"]]["slug"] + "/",
                                 "fr": "/fr/envies/" + T["fr"]["moods"][_m["id"]]["slug"] + "/"}
for _d in DAYS:
    PAGES["day:" + _d["id"]] = {"en": "/days/" + _d["slug"]["en"] + "/", "fr": "/fr/sorties/" + _d["slug"]["fr"] + "/"}


def e(s):
    return html.escape(str(s), quote=True)


def ver(rel):
    with open(os.path.join(SITE, "assets", rel), "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8]


def url(page, lang, frag=""):
    return PAGES[page][lang] + frag


def wa(text):
    return WA_BASE + "?text=" + quote(text)


def mood_days(mid):
    return [d for d in DAYS if d["mood"] == mid]


def color(d):
    return MOOD[d["mood"]]["color"]


def rating(t):
    v = C["rating"]["value"]
    return v.replace(".", ",") if t["lang"] == "fr" else v


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


def credit_line(t, name):
    """Visible credit under a Commons place photo (short; full details on /credits/)."""
    c = IMG[name].get("credit")
    if not c: return ""
    lang = t["lang"]
    return (f'<figcaption class="cap"><span class="cap__place">{e(c["place"][lang])}</span> '
            f'<span class="cap__by">{e(t["ui"]["photo_by"])}: <a href="{e(c["source"])}" rel="noopener">{e(c["author"])}</a>, '
            f'<a href="{e(c["license_url"])}" rel="noopener license">{e(c["license"])}</a> · {e(t["ui"]["context_photo"])}</span></figcaption>')


def hero_picture():
    d, m = IMG["hero-horses"], IMG["hero-horses-m"]
    ms = ", ".join(f"/assets/img/{x['file']} {x['w']}w" for x in m["variants"])
    ds = ", ".join(f"/assets/img/{x['file']} {x['w']}w" for x in d["variants"])
    return (f'<picture class="hero__pic">'
            f'<source media="(max-width: 47.99em)" srcset="{ms}" sizes="100vw" width="{m["w"]}" height="{m["h"]}">'
            f'<img src="/assets/img/{d["variants"][1]["file"]}" srcset="{ds}" sizes="(min-width: 48em) 52vw, 100vw" '
            f'width="{d["w"]}" height="{d["h"]}" alt="{e(d["alt"])}" fetchpriority="high" decoding="async" '
            f'style="background:{d["color"]} url({d["lqip"]}) center/cover"></picture>')


def stack(words, cls="stack"):
    return f'<div class="{cls}" aria-hidden="true">' + "".join(f"<span>{e(w)}</span>" for w in words) + "</div>"


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
def day_map_svg(t, big=False):
    """Sketch map of Agadir and the day-trip destinations (equirectangular, cos-lat scaled)."""
    lang = t["lang"]
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
    tid = "daymap-t2" if big else "daymap-t"
    out = [f'<svg class="daymap__svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="{tid}">',
           f'<title id="{tid}">{e(t["map"]["title"])}</title>',
           f'<polygon class="dm-ocean" points="{ocean}"/>',
           '<polyline class="dm-coast" points="' + " ".join(f"{x},{y}" for x, y in coast) + '"/>',
           f'<text class="dm-ocean-l" x="44" y="{H * 0.6:.0f}" transform="rotate(-80 44 {H * 0.6:.0f})">{e(t["map"]["ocean"])}</text>']
    pts = [d for d in DAYS if d.get("map") and d["id"] != "zagora"]
    for d in pts:
        x, y = P(*d["map"])
        mx, my = (ax + x) / 2, (ay + y) / 2
        dx, dy = x - ax, y - ay
        cx, cy = mx - dy * 0.18, my + dx * 0.18
        out.append(f'<path class="dm-route c-{color(d)}" d="M{ax},{ay} Q{cx:.1f},{cy:.1f} {x},{y}"/>')
    # Zagora: off the map to the east
    zx, zy = P(30.33, -7.75)
    out.append(f'<path class="dm-route c-cobalt" d="M{ax},{ay} Q{(ax + zx) / 2:.1f},{zy + 40:.1f} {zx - 6},{zy}"/>')
    out.append(f'<a href="{url("day:zagora", lang)}" class="dm-place"><path class="dm-arrow" d="M{zx - 14},{zy - 8} {zx},{zy} {zx - 14},{zy + 8}"/>'
               f'<text x="{zx - 6}" y="{zy - 14}" text-anchor="end">{e(t["map"]["zagora_arrow"])} →</text></a>')
    for nm, key in (("Tiznit", "tiznit"), ("Tiout", "tiout")):
        x, y = P(*CAT["map_extra"][key])
        out.append(f'<g class="dm-minor"><circle cx="{x}" cy="{y}" r="3.5"/><text x="{x + 8}" y="{y + 4}">{nm}</text></g>')
    for d in pts:
        x, y = P(*d["map"])
        dx, dy, anc = lab.get(d["id"], (10, 4, "start"))
        out.append(f'<a href="{url("day:" + d["id"], lang)}" class="dm-place" aria-label="{e(d[lang]["name"])}"><circle class="dm-dot c-{color(d)}" cx="{x}" cy="{y}" r="8"/>'
                   f'<text x="{x + dx}" y="{y + dy}" text-anchor="{anc}">{e(t["map"]["labels"][d["id"]])}</text></a>')
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


# ---------------------------------------------------------------- structured data
def org(t):
    lang = t["lang"]
    days = {"Mo": "Monday", "Tu": "Tuesday", "We": "Wednesday", "Th": "Thursday", "Fr": "Friday", "Sa": "Saturday", "Su": "Sunday"}
    return {
        "@type": "TravelAgency", "@id": ORIGIN + "/#agency", "name": "Hala Tours Agadir",
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


def crumbs_ld(lang, trail):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": name, "item": ORIGIN + href} for i, (name, href) in enumerate(trail)]}


def ld(*items):
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": list(items)}, ensure_ascii=False).replace("</", "<\\/") + "</script>"


# ---------------------------------------------------------------- partials
def head(t, page, title, desc):
    lang = t["lang"]
    canon = ORIGIN + PAGES[page][lang]
    full = title if page == "home" else title + t["meta"]["suffix"]
    alts = "".join(f'<link rel="alternate" hreflang="{l2}" href="{ORIGIN}{PAGES[page][l2]}">' for l2 in LANGS)
    alts += f'<link rel="alternate" hreflang="x-default" href="{ORIGIN}{PAGES[page]["en"]}">'
    og = IMG["_og"]
    ogt = t["meta"]["og_title"] if page == "home" else full
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canon}">{alts}
<meta name="theme-color" content="#1b2390">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Hala Tours Agadir">
<meta property="og:title" content="{e(ogt)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{ORIGIN}/assets/img/{og['file']}">
<meta property="og:image:width" content="{og['w']}">
<meta property="og:image:height" content="{og['h']}">
<meta property="og:image:alt" content="{e(IMG['hero-horses']['alt'])}">
<meta property="og:locale" content="{t['locale']}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(ogt)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{ORIGIN}/assets/img/{og['file']}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/bricolage-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/site.css?v={ver('css/site.css')}">
<script src="/assets/js/site.js?v={ver('js/site.js')}" defer></script>
"""


def wordmark():
    return ('<span class="wm"><svg class="wm__sun" viewBox="0 0 40 40" aria-hidden="true" focusable="false">'
            '<circle cx="20" cy="20" r="13"/><path d="M20 1v5M20 34v5M1 20h5M34 20h5M6.6 6.6l3.5 3.5M29.9 29.9l3.5 3.5M6.6 33.4l3.5-3.5M29.9 10.1l3.5-3.5"/></svg>'
            '<span class="wm__name">Hala<span class="wm__rest"> Tours Agadir</span></span></span>')


def lang_switch(t, page, cls):
    u = t["ui"]
    o = u["other_lang"]
    return (f'<p class="{cls}" aria-label="{e(u["lang_label"])}"><span aria-current="true">{e(u["this_lang"])}</span>'
            f'<a href="{url(page, o["code"])}" hreflang="{o["code"]}" lang="{o["code"]}" title="{e(o["label"])}">{e(o["short"])}</a></p>')


def header(t, page):
    u, lang = t["ui"], t["lang"]
    cur = ' aria-current="page"'
    links = "".join(f'<li><a href="{url(p, lang)}"{cur if p == page else ""}>{e(label)}</a></li>' for p, label in u["nav"])
    return f"""<a class="skip" href="#main">{e(u['skip'])}</a>
<header class="top" id="top">
  <div class="top__in">
    <a class="top__brand" href="{url('home', lang)}" aria-label="{e(u['home_label'])}">{wordmark()}<span class="top__sub">{e(u['brand_sub'])}</span></a>
    <nav class="top__nav" aria-label="{e(u['nav_label'])}"><ul>{links}</ul></nav>
    <div class="top__act">
      {lang_switch(t, page, 'top__lang')}
      <a class="top__call" href="{TEL}">{icon('i-phone')}<span>{e(C['phone_display'])}</span></a>
      <a class="btn btn--sun top__plan" href="{url('plan', lang)}">{icon('i-wa')}<span>{e(u['cta_plan'])}</span></a>
      <button class="top__menu" type="button" aria-expanded="false" aria-controls="sheet">{icon('i-menu')}<span>{e(u['menu'])}</span></button>
    </div>
  </div>
</header>"""


def sheet(t, page):
    """Mobile menu: the mood tabs, big, plus the practical links."""
    u, lang = t["ui"], t["lang"]
    tabs = "".join(f'<li><a class="tab tab--{m["color"]}" href="{url("mood:" + m["id"], lang)}">{e(t["moods"][m["id"]]["name"])}</a></li>' for m in CAT["moods"])
    links = "".join(f'<li><a href="{url(p, lang)}">{e(label)}</a></li>' for p, label in u["nav"] + u["more_links"][:2])
    return f"""<div class="sheet" id="sheet" hidden>
  <div class="sheet__in" role="dialog" aria-modal="true" aria-label="{e(u['menu'])}">
    <div class="sheet__top">{wordmark()}<button class="sheet__close" type="button">{icon('i-close')}<span>{e(u['close'])}</span></button></div>
    <p class="sheet__label">{e(t['hero']['moods_label'])}</p>
    <ul class="sheet__tabs">{tabs}</ul>
    <ul class="sheet__links">{links}</ul>
    {lang_switch(t, page, 'sheet__lang')}
    <div class="sheet__contact"><a class="btn btn--sun" href="{wa(t['plan']['wa_simple'])}">{icon('i-wa')}{e(u['whatsapp'])}</a><a class="btn btn--line" href="{TEL}">{icon('i-phone')}{e(u['call'])}</a></div>
  </div>
</div>"""


def crumbs(t, trail):
    """trail: [(label, href or None), …] after Home."""
    u, lang = t["ui"], t["lang"]
    items = [f'<li><a href="{url("home", lang)}">{e(u["home"])}</a></li>']
    for label, href in trail:
        items.append(f'<li><a href="{href}">{e(label)}</a></li>' if href else f'<li><span aria-current="page">{e(label)}</span></li>')
    return f'<nav class="crumbs" aria-label="{e(u["crumb_label"])}"><ol>{"".join(items)}</ol></nav>'


def hero(t):
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
    <a class="proof" href="#reviews"><span class="proof__stars">{icon('i-star')*5}</span><strong>{rating(t)}</strong> {e(h['rating'])} · {e(h['rating_count'])}</a>
    <a class="status" href="#desk" data-status>{icon('i-pin')}<span data-status-text>{e(t['desk']['address'])}</span></a>
  </div>
</section>"""


def add_button(t, d):
    u = t["ui"]
    return (f'<button class="day__add" type="button" data-pick="{d["id"]}" aria-pressed="false">'
            f'<span class="day__add-off">{icon("i-plus")}{e(u["add"])}</span><span class="day__add-on">{icon("i-check")}{e(u["added"])}</span></button>')


def len_tags(t, d):
    u = t["ui"]
    return "".join(f'<span class="len-tag">{len_glyph(l)}{e(u["length_short"][l])}</span>' for l in d["lengths"])


def day_row(t, d, more=False, tag="h3"):
    u, lang = t["ui"], t["lang"]
    s = d[lang]
    req = f'<span class="badge">{e(u["on_request"])}</span>' if d["status"] == "on_request" else ""
    cls = f"day c-{color(d)}" + (" day--more" if more else "")
    return (f'<li class="{cls}" id="day-{d["id"]}" data-lengths="{" ".join(d["lengths"])}">'
            f'<div class="day__len">{len_tags(t, d)}</div>'
            f'<{tag} class="day__name"><a href="{url("day:" + d["id"], lang)}">{e(s["name"])}</a>{req}</{tag}>'
            f'<p class="day__line">{e(s["line"])}</p>'
            f'{add_button(t, d)}</li>')


def lenbar(t):
    g, u = t["guide"], t["ui"]
    chips = f'<button type="button" class="chip" data-len="" aria-pressed="true">{e(g["filter_all"])}</button>' + "".join(
        f'<button type="button" class="chip" data-len="{l}" aria-pressed="false">{len_glyph(l)}{e(u["lengths"][l])}</button>' for l in CAT["lengths"])
    return f'<div class="lenbar" role="group" aria-label="{e(g["filter_label"])}"><p class="lenbar__l">{e(g["filter_label"])}</p><div class="lenbar__chips">{chips}</div></div>'


def mood_media(t, m, lazy=True):
    mt = t["moods"][m["id"]]
    if m["img"]:
        return f'<figure class="ch__fig">{img(m["img"], "(min-width: 64em) 40vw, 92vw", cls="ch__img", lazy=lazy, priority=not lazy)}</figure>'
    return stack(mt.get("places", []), "ch__places")


def chapter(t, m, i, mode="home"):
    """mode: home (first rows + 'all N days' link), index (all rows), page (the mood page: h1, all rows)."""
    lang = t["lang"]
    mt = t["moods"][m["id"]]
    items = mood_days(m["id"])
    n = CAT["home_rows"]
    rows = "".join(day_row(t, d, more=(mode == "home" and j >= n)) for j, d in enumerate(items))
    note_txt = mt.get("note") or (mt.get("page_note") if mode == "page" else None)
    note = f'<p class="note note--ch">{icon("i-scribble", "note__arrow")}{e(note_txt)}</p>' if note_txt else ""
    side = " ch--flip" if (i % 2 and mode != "page") else ""
    hid = f"mood-{m['id']}-h"
    if mode == "page":
        num = f'<a class="ch__num" href="{url("days", lang)}">{e(t["mood_page"]["kicker"].format(n=i + 1))}</a>'
        h = f'<h1 class="ch__h" id="{hid}">{e(mt["name"])}</h1>'
    else:
        num = f'<p class="ch__num">{e(t["guide"]["chapter"].format(n=i + 1))}</p>'
        h = f'<h2 class="ch__h" id="{hid}"><a href="{url("mood:" + m["id"], lang)}">{e(mt["name"])}</a></h2>'
    more = ""
    if mode == "home":
        more = (f'<a class="ch__more" href="{url("mood:" + m["id"], lang)}">{e(t["ui"]["more_days"].format(n=len(items), mood=mt["name"]))}{icon("i-arrow")}</a>')
    tag = "div" if mode == "page" else "section"
    return f"""<{tag} class="ch ch--{m['color']}{side}" id="mood-{m['id']}" aria-labelledby="{hid}" data-mood="{m['id']}">
  <header class="ch__band">
    {num}
    {h}
    <p class="ch__intro">{e(mt['intro'])}</p>
  </header>
  <div class="ch__body">
    <div class="ch__media">{mood_media(t, m, lazy=(mode != "page"))}{note}</div>
    <div class="ch__list">{lenbar(t) if mode == "page" else ""}<ul class="ch__days">{rows}</ul>
    <p class="ch__none" hidden>{e(t['guide']['none_here'])}</p>{more}</div>
  </div>
</{tag}>"""


def thumbs(t):
    return '<nav class="thumbs" aria-label="' + e(t["hero"]["moods_label"]) + '"><ul>' + "".join(
        f'<li><a class="thumb thumb--{m["color"]}" href="#mood-{m["id"]}" data-thumb="{m["id"]}" aria-label="{e(t["moods"][m["id"]]["name"])}"><span>{e(t["moods"][m["id"]]["short"])}</span></a></li>'
        for m in CAT["moods"]) + "</ul></nav>"


def guide(t, mode="home"):
    g, lang = t["guide"], t["lang"]
    chapters = "\n".join(chapter(t, m, i, mode) for i, m in enumerate(CAT["moods"]))
    if mode == "home":
        headh = f'<p class="kicker">{e(g["kicker"])}</p><h2 class="guide__h" id="guide-h">{e(g["title"])}</h2>'
        tail = f'<p class="guide__all"><a class="btn btn--ink" href="{url("days", lang)}">{e(g["all_link"])}{icon("i-arrow")}</a></p>'
    else:
        p = t["days_page"]
        headh = f'<p class="kicker">{e(p["kicker"])}</p><h1 class="guide__h guide__h--page" id="guide-h">{e(p["h1"])}</h1><p class="guide__lede">{e(p["lede"])}</p>'
        tail = ""
    return f"""<section class="guide guide--{mode}" id="guide" aria-labelledby="guide-h">
  <div class="guide__head">{headh}{lenbar(t)}</div>
  {thumbs(t)}
{chapters}
{tail}
</section>"""


def daymap(t, mode="home"):
    m, lang = t["map"], t["lang"]
    link = f'<p class="daymap__link"><a class="link" href="{url("where", lang)}">{e(m["page_link"])}{icon("i-arrow")}</a></p>' if mode == "home" else ""
    return f"""<section class="daymap" id="map" aria-labelledby="map-h">
  <div class="daymap__text">
    <p class="kicker">{e(m['kicker'])}</p>
    <h2 id="map-h" class="sec-h">{e(m['title'])}</h2>
    <p>{e(m['text'])}</p>
    <p class="daymap__cap">{e(m['caption'])}</p>{link}
  </div>
  <div class="daymap__map">{day_map_svg(t)}</div>
</section>"""


def quote_items(t, idxs):
    r = t["reviews"]
    return "".join(f'<li class="rv rv--{n % 5}"><blockquote><p>“{e(r["items"][i]["q"])}”</p></blockquote><p class="rv__by">{e(r["items"][i]["by"])} · {e(r["platform"])}</p></li>'
                   for n, i in enumerate(idxs))


def reviews(t):
    r, lang = t["reviews"], t["lang"]
    note = f'<p class="reviews__note">{e(r["lang_note"])}</p>' if r["lang_note"] else ""
    return f"""<section class="reviews" id="reviews" aria-labelledby="rv-h">
  <div class="reviews__head">
    <p class="kicker">{e(r['kicker'])}</p>
    <h2 id="rv-h" class="sec-h"><span class="reviews__big">{icon('i-star')}{rating(t)}</span> {e(r['title'])}</h2>{note}
    <p class="reviews__links"><a class="link" href="{url('reviews', lang)}">{e(r['more'])}{icon('i-arrow')}</a>
    <a class="link" href="{C['maps_url']}" rel="noopener">{e(r['link'])}{icon('i-arrow')}</a></p>
  </div>
  <ul class="reviews__list">{quote_items(t, r['home_pick'])}</ul>
</section>"""


def hours_table(t):
    return "<table>" + "".join(f"<tr><th scope=\"row\">{e(a)}</th><td>{e(b)}</td></tr>" for a, b in t["ui"]["days_range"]) + "</table>"


def desk(t):
    """Homepage version: compact; the full story lives on /visit/."""
    d, lang = t["desk"], t["lang"]
    return f"""<section class="desk" id="desk" aria-labelledby="desk-h">
  <div class="desk__text">
    <p class="kicker">{e(d['kicker'])}</p>
    <h2 id="desk-h" class="sec-h">{e(d['title'])}</h2>
    <p class="desk__p">{e(d['text'])}</p>
    <address class="desk__addr">{icon('i-pin')}<span>{e(d['address'])}</span></address>
    <div class="desk__hours"><p class="desk__ht">{e(d['hours_title'])} <span class="desk__now" data-status-badge hidden></span></p>{hours_table(t)}</div>
    <div class="desk__btns">
      <a class="btn btn--sun" href="{url('visit', lang)}">{e(d['more'])}{icon('i-arrow')}</a>
      <a class="btn btn--line" href="{C['maps_url']}" rel="noopener">{icon('i-pin')}{e(d['maps'])}</a>
    </div>
  </div>
  <figure class="desk__map">{locator_svg(t)}<p class="note note--desk">{e(d['note'])}</p></figure>
  <p class="desk__tr"><a class="link" href="{url('transfers', lang)}">{e(d['transfers_line'])}{icon('i-arrow')}</a></p>
</section>"""


def ok_box(t):
    p = t["plan"]
    return f"""<div class="planner__ok" data-ok hidden tabindex="-1">
      <p class="planner__ok-h">{e(p['ok_title'])}</p><p>{e(p['ok_text'])}</p>
      <p class="planner__ok-links"><a class="btn btn--sun" data-retry href="{wa(p['wa_simple'])}">{icon('i-wa')}{e(p['retry'])}</a>
      <a class="link" href="{TEL}">{icon('i-phone')}{e(p['or_call'])} {e(C['phone_display'])}</a>
      <a class="link" data-mail href="mailto:{C['email']}">{icon('i-mail')}{e(p['or_mail'])} {e(C['email'])}</a></p>
    </div>"""


def people_fields(t, prefix):
    p = t["plan"]
    return (f'<div class="fld fld--num"><label for="{prefix}-adults">{e(p["adults_label"])}</label><input id="{prefix}-adults" name="adults" type="number" inputmode="numeric" min="1" max="60" value="2" required><p class="err" data-err="adults" hidden>{e(p["err_adults"])}</p></div>'
            f'<div class="fld fld--num"><label for="{prefix}-kids">{e(p["kids_label"])}</label><input id="{prefix}-kids" name="kids" type="number" inputmode="numeric" min="0" max="40" value="0"></div>'
            f'<div class="fld" data-ages hidden><label for="{prefix}-ages">{e(p["ages_label"])}</label><input id="{prefix}-ages" name="ages" type="text" placeholder="{e(p["ages_ph"])}" autocomplete="off"></div>')


def planner(t, level="h2", compact=False):
    p, u = t["plan"], t["ui"]
    moods = "".join(f'<label class="mchip mchip--{m["color"]}"><input type="checkbox" name="mood" value="{m["id"]}"><span>{e(t["moods"][m["id"]]["name"])}</span></label>' for m in CAT["moods"])
    lens = "".join(f'<label class="lchip"><input type="radio" name="length" value="{l}"><span>{len_glyph(l)}{e(u["lengths"][l])}</span></label>' for l in CAT["lengths"])
    lens += f'<label class="lchip"><input type="radio" name="length" value="" checked><span>{e(p["length_any"])}</span></label>'
    hcls = "sec-h sec-h--page" if level == "h1" else "sec-h"
    open_d, close_d = (f'<details class="more"><summary>{e(p["more_summary"])}</summary><div class="more__in">', "</div></details>") if compact else ("", "")
    return f"""<section class="plan" id="plan" aria-labelledby="plan-h" data-dock-hide>
  <div class="plan__head">
    <p class="kicker">{e(p['kicker'])}</p>
    <{level} id="plan-h" class="{hcls}">{e(p['title'])}</{level}>
    <p>{e(p['text'])}</p>
  </div>
  <form class="planner" id="planner" data-wa="plan" novalidate>
    <fieldset class="f f--moods"><legend>{e(p['moods_label'])}</legend><div class="mchips">{moods}</div></fieldset>
    <div class="f f--picked"><p class="f__l">{e(p['picked_label'])}</p><ul class="picked" data-picked></ul><p class="picked__empty" data-picked-empty>{e(p['picked_empty'])}</p></div>
    <p class="err" data-err="what" hidden>{e(p['err_what'])}</p>
    {open_d}<fieldset class="f f--len"><legend>{e(p['length_label'])}</legend><div class="lchips">{lens}</div></fieldset>
    <div class="f f--row">
      <div class="fld"><label for="f-date">{e(p['date_label'])}</label><input id="f-date" name="date" type="date" aria-describedby="f-date-h"><p class="hint" id="f-date-h">{e(p['date_hint'])}</p><p class="err" data-err="date" hidden>{e(p['err_date'])}</p></div>
      {people_fields(t, 'f')}
    </div>
    <div class="f f--row">
      <div class="fld"><label for="f-stay">{e(p['stay_label'])}</label><input id="f-stay" name="stay" type="text" placeholder="{e(p['stay_ph'])}" autocomplete="off"></div>
      <div class="fld"><label for="f-name">{e(p['name_label'])}</label><input id="f-name" name="name" type="text" autocomplete="given-name"></div>
    </div>{close_d}
    <div class="fld"><label for="f-msg">{e(p['msg_label'])}</label><textarea id="f-msg" name="msg" rows="3" placeholder="{e(p['msg_ph'])}"></textarea></div>
    <div class="planner__go"><button class="btn btn--sun btn--big" type="submit">{icon('i-wa')}{e(p['submit'])}</button>
      <noscript><a class="link" href="{wa(p['wa_simple'])}">{e(p['nojs'])}</a></noscript></div>
    {ok_box(t)}
  </form>
</section>"""


def footer(t, page):
    f, u, lang = t["footer"], t["ui"], t["lang"]
    hours = " · ".join(f"{a} {b}" for a, b in u["days_range"])
    links = "".join(f'<li><a href="{url(p, lang)}">{e(label)}</a></li>' for p, label in u["nav"] + u["more_links"])
    return f"""<footer class="foot" id="foot" data-dock-hide>
  <div class="foot__in">
    <div class="foot__brand">{wordmark()}<p>{e(f['line'])}</p>{lang_switch(t, page, 'foot__lang')}</div>
    <div class="foot__col"><p class="foot__h">{e(f['visit'])}</p><p>{e(t['desk']['address'])}</p><p>{e(hours)}</p><p><a href="{C['maps_url']}" rel="noopener">{icon('i-pin')}{e(t['desk']['maps'])}</a></p></div>
    <div class="foot__col"><p class="foot__h">{e(f['contact'])}</p>
      <p><a href="{wa(t['plan']['wa_simple'])}">{icon('i-wa')}WhatsApp {e(C['phone_display'])}</a></p>
      <p><a href="{TEL}">{icon('i-phone')}{e(C['phone_display'])}</a></p>
      <p><a href="mailto:{C['email']}">{icon('i-mail')}{e(C['email'])}</a></p></div>
    <nav class="foot__col" aria-label="{e(f['pages'])}"><p class="foot__h">{e(f['pages'])}</p><ul class="foot__links">{links}</ul></nav>
  </div>
  <p class="foot__small">{e(f['small'])}</p>
</footer>"""


def dock(t, href=None, label=None):
    u, lang = t["ui"], t["lang"]
    static = ' data-static' if label else ""
    return f"""<div class="dock" data-dock>
  <button class="dock__menu" type="button" aria-expanded="false" aria-controls="sheet">{icon('i-menu')}<span class="vh">{e(u['menu'])}</span></button>
  <a class="dock__plan" href="{href or url('plan', lang)}"{static}><span class="dock__count" data-count hidden>0</span>{icon('i-wa')}<span data-dock-label>{e(label or u['sticky_idle'])}</span></a>
  <a class="dock__call" href="{TEL}">{icon('i-phone')}<span class="vh">{e(u['call'])} {e(C['phone_display'])}</span></a>
</div>"""


def page_data(t):
    """Strings + facts the script needs (keeps site.js language-agnostic)."""
    p, u, lang = t["plan"], t["ui"], t["lang"]
    s = {k: v for k, v in p.items() if k.startswith(("wa_", "mail_", "remove"))}
    s.update({"d_intro": t["day"]["wa_intro"], "d_outro": t["day"]["wa_outro"]})
    s.update({"t_" + k[3:]: v for k, v in t["transfers_page"].items() if k.startswith("wa_")})
    data = {
        "wa": WA_BASE, "email": C["email"], "hours": C["hours"], "tz": "Africa/Casablanca", "lang": lang,
        "products": {d["id"]: d[lang]["name"] for d in DAYS},
        "pc": {d["id"]: color(d) for d in DAYS},
        "moods": {m["id"]: t["moods"][m["id"]]["name"] for m in CAT["moods"]},
        "lengths": u["lengths"], "s": s,
        "ui": {k: u[k] for k in ("open_now", "closed_now", "sticky_idle", "sticky_go")},
    }
    return '<script type="application/json" id="hala-data">' + json.dumps(data, ensure_ascii=False).replace("</", "<\\/") + "</script>"


def page(t, key, title, desc, main, ldata, dock_html=None):
    return (head(t, key, title, desc) + "</head>\n<body>\n<!--email_off-->\n" + "\n".join([
        header(t, key), sheet(t, key), f'<main id="main">{main}</main>', footer(t, key),
        dock_html or dock(t), SPRITE, page_data(t), ld(*ldata)]) + "\n<!--/email_off-->\n</body>\n</html>\n")


def cta_band(t, title, text, href=None, label=None):
    lang = t["lang"]
    return (f'<aside class="band-cta"><div class="band-cta__in"><p class="band-cta__h">{e(title)}</p><p>{e(text)}</p>'
            f'<a class="btn btn--sun btn--big" href="{href or url("plan", lang)}">{icon("i-wa")}{e(label or t["mood_page"]["plan_cta"])}</a></div></aside>')


# ---------------------------------------------------------------- pages
def render_home(t):
    lang = t["lang"]
    main = "\n".join([hero(t), guide(t, "home"), daymap(t), reviews(t), desk(t), planner(t, compact=True)])
    data = dict(org(t), **{"@context": "https://schema.org"})
    return (head(t, "home", t["meta"]["title"], t["meta"]["description"]) + "</head>\n<body>\n<!--email_off-->\n" + "\n".join([
        header(t, "home"), sheet(t, "home"), f'<main id="main">{main}</main>', footer(t, "home"), dock(t), SPRITE, page_data(t),
        '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"]) + "\n<!--/email_off-->\n</body>\n</html>\n")


def render_days(t):
    lang, p = t["lang"], t["days_page"]
    main = crumbs(t, [(t["guide"]["kicker"], None)]) + guide(t, "index") + cta_band(t, t["mood_page"]["plan_title"], t["mood_page"]["plan_text"])
    items = [{"@type": "ListItem", "position": i + 1, "url": ORIGIN + url("day:" + d["id"], lang), "name": d[lang]["name"]} for i, d in enumerate(DAYS)]
    return page(t, "days", p["title"], p["desc"], main,
                [{"@type": "ItemList", "name": p["h1"], "itemListElement": items}, crumbs_ld(lang, [(t["ui"]["home"], url("home", lang)), (t["guide"]["kicker"], url("days", lang))])])


def render_mood(t, mid):
    lang = t["lang"]
    i = [m["id"] for m in CAT["moods"]].index(mid)
    m, mt, mp = MOOD[mid], t["moods"][mid], t["mood_page"]
    others = "".join(f'<li><a class="tab tab--{o["color"]}" href="{url("mood:" + o["id"], lang)}">{e(t["moods"][o["id"]]["name"])}</a></li>' for o in CAT["moods"] if o["id"] != mid)
    main = (crumbs(t, [(t["guide"]["kicker"], url("days", lang)), (mt["name"], None)])
            + f'<div class="moodpage">{chapter(t, m, i, "page")}</div>'
            + f'<nav class="others" aria-labelledby="others-h"><p class="others__h" id="others-h">{e(mp["other"])}</p><ul class="tabs">{others}</ul></nav>'
            + cta_band(t, mp["plan_title"], mp["plan_text"]))
    items = [{"@type": "ListItem", "position": j + 1, "url": ORIGIN + url("day:" + d["id"], lang), "name": d[lang]["name"]} for j, d in enumerate(mood_days(mid))]
    trail = [(t["ui"]["home"], url("home", lang)), (t["guide"]["kicker"], url("days", lang)), (mt["name"], url("mood:" + mid, lang))]
    return page(t, "mood:" + mid, mt["title"], mt["desc"], main, [{"@type": "ItemList", "name": mt["name"], "itemListElement": items}, crumbs_ld(lang, trail)])


def day_media(t, d):
    lang = t["lang"]
    if d["img"]:
        return (f'<figure class="dp__fig">{img(d["img"], "(min-width: 64em) 42vw, 100vw", cls="dp__img", lazy=False, priority=True)}'
                f'{credit_line(t, d["img"])}</figure>')
    return f'<div class="dp__fig dp__fig--stack">{stack(d["stack"][lang], "dp__stack")}</div>'


def ask_block(t, d):
    lang, dd, p = t["lang"], t["day"], t["plan"]
    name = d[lang]["name"]
    simple = wa(dd["wa_intro"].format(day=name) + "\n\n" + dd["wa_outro"])
    return f"""<section class="ask" id="ask" aria-labelledby="ask-h" data-dock-hide>
  <div class="ask__head">
    <p class="kicker">{e(dd['ask_kicker'])}</p>
    <h2 class="sec-h" id="ask-h">{e(dd['ask_title'])}</h2>
    <p>{e(dd['ask_text'])}</p>
  </div>
  <form class="planner ask__form" data-wa="day" data-day="{d['id']}" novalidate>
    <div class="f f--row">
      <div class="fld"><label for="a-date">{e(p['date_label'])}</label><input id="a-date" name="date" type="date" aria-describedby="a-date-h"><p class="hint" id="a-date-h">{e(p['date_hint'])}</p><p class="err" data-err="date" hidden>{e(p['err_date'])}</p></div>
      {people_fields(t, 'a')}
    </div>
    <div class="fld"><label for="a-stay">{e(p['stay_label'])}</label><input id="a-stay" name="stay" type="text" placeholder="{e(p['stay_ph'])}" autocomplete="off"></div>
    <div class="planner__go"><button class="btn btn--sun btn--big" type="submit">{icon('i-wa')}{e(dd['submit'])}</button>
      <a class="link" href="{simple}">{e(dd['one_tap'])}{icon('i-arrow')}</a></div>
    {ok_box(t)}
  </form>
  <ul class="ask__more">
    <li><a class="link" href="{TEL}">{icon('i-phone')}{e(p['or_call'])} {e(C['phone_display'])}</a></li>
    <li><a class="link" href="{url('visit', lang)}">{icon('i-pin')}{e(dd['or_desk'])}</a></li>
    <li><a class="link" href="{url('plan', lang)}">{e(dd['or_plan'])} {e(t['ui']['cta_plan'])}{icon('i-arrow')}</a></li>
  </ul>
</section>"""


def render_day(t, did):
    lang, dd, u = t["lang"], t["day"], t["ui"]
    d = DAY[did]
    s, m = d[lang], MOOD[d["mood"]]
    mt = t["moods"][d["mood"]]
    simple = wa(dd["wa_intro"].format(day=s["name"]) + "\n\n" + dd["wa_outro"])
    badge = f'<span class="badge badge--band">{e(u["on_request"])}</span>' if d["status"] == "on_request" else ""
    facts = "".join(f'<div class="fact"><dt>{e(dd["facts"][k])}</dt><dd>{e(s["facts"][k])}</dd></div>' for k in ("time", "pickup", "food", "incl", "kids") if s["facts"].get(k))
    facts_html = (f'<section class="dp__facts" aria-labelledby="facts-h"><h2 class="vh" id="facts-h">{e(dd["facts_label"])}</h2><dl>{facts}</dl>'
                  + (f'<p class="dp__small">{e(dd["times_note"])}</p>' if s["facts"].get("time") and d["lengths"] != ["two"] else "") + "</section>") if facts else ""
    req = (f'<section class="dp__req"><h2>{e(dd["request_title"])}</h2><p>{e(dd["request_text"])}</p></section>') if d["status"] == "on_request" else ""
    steps = "".join(f"<li>{e(x)}</li>" for x in s["steps"])
    tips = "".join(f"<li>{e(x)}</li>" for x in s.get("tips", []))
    note = f'<p class="note note--dp">{icon("i-scribble", "note__arrow")}{e(s["note"])}</p>' if s.get("note") else ""
    suits = f'<section class="dp__sec"><h2 class="dp__h2">{e(dd["suits"])}</h2><p>{e(s["suits"])}</p></section>' if s.get("suits") else ""
    good = f'<section class="dp__sec dp__good"><h2 class="dp__h2">{e(dd["good"])}</h2><ul>{tips}</ul>{note}</section>' if tips else ""
    rel = "".join(day_row(t, DAY[r]) for r in d["related"])
    lens = "".join(f'<span class="len-tag">{len_glyph(l)}{e(u["lengths"][l])}</span>' for l in d["lengths"])
    main = f"""{crumbs(t, [(t['guide']['kicker'], url('days', lang)), (mt['name'], url('mood:' + d['mood'], lang)), (s['name'], None)])}
<article class="dp c-{m['color']}" aria-labelledby="dp-h">
  <header class="dp__band">
    <a class="dp__mood" href="{url('mood:' + d['mood'], lang)}">{e(mt['name'])}</a>
    <h1 class="dp__h" id="dp-h">{e(s['name'])}{badge}</h1>
    <p class="dp__len">{lens}</p>
    <p class="dp__lede">{e(s['lede'])}</p>
    <div class="dp__cta"><a class="btn btn--sun" href="{simple}">{icon('i-wa')}{e(dd['one_tap'])}</a>{add_button(t, d)}</div>
  </header>
  <div class="dp__body">
    <div class="dp__side">{day_media(t, d)}{facts_html}</div>
    <div class="dp__main">
      {req}
      <section class="dp__sec"><h2 class="dp__h2">{e(dd['what'])}</h2><ol class="steps">{steps}</ol></section>
      {good}{suits}
    </div>
  </div>
</article>
{ask_block(t, d)}
<section class="rel" aria-labelledby="rel-h"><h2 class="rel__h" id="rel-h">{e(dd['related'])}</h2><ul class="rel__list">{rel}</ul></section>"""
    trip = {"@type": "TouristTrip", "name": s["name"], "description": s["desc"], "url": ORIGIN + url("day:" + did, lang),
            "touristType": mt["name"], "provider": {"@id": ORIGIN + "/#agency"}, "inLanguage": lang,
            "itinerary": {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": x} for i, x in enumerate(s["steps"])]}}
    if d["img"]: trip["image"] = f"{ORIGIN}/assets/img/{IMG[d['img']]['variants'][0]['file']}"
    agency = {"@type": "TravelAgency", "@id": ORIGIN + "/#agency", "name": "Hala Tours Agadir", "url": ORIGIN + "/", "telephone": C["phone_display"]}
    trail = [(u["home"], url("home", lang)), (t["guide"]["kicker"], url("days", lang)), (mt["name"], url("mood:" + d["mood"], lang)), (s["name"], url("day:" + did, lang))]
    return page(t, "day:" + did, s["title"], s["desc"], main, [trip, agency, crumbs_ld(lang, trail)],
                dock(t, "#ask", dd["dock"]))


def render_where(t):
    lang, w = t["lang"], t["where_page"]
    far = [d for d in DAYS if d.get("map")]
    near = [d for d in DAYS if not d.get("map")]

    def lst(ds):
        return "".join(f'<li class="c-{color(d)}"><a href="{url("day:" + d["id"], lang)}"><span class="pl__dot" aria-hidden="true"></span><span class="pl__n">{e(d[lang]["name"])}</span>'
                       f'<span class="pl__l">{len_tags(t, d)}</span></a></li>' for d in ds)
    main = f"""{crumbs(t, [(w['h1'], None)])}
<section class="where" aria-labelledby="where-h">
  <div class="where__head"><p class="kicker">{e(t['map']['kicker'])}</p><h1 class="sec-h sec-h--page" id="where-h">{e(w['h1'])}</h1><p class="where__lede">{e(w['lede'])}</p></div>
  <div class="where__map">{day_map_svg(t, big=True)}<p class="daymap__cap">{e(t['map']['caption'])}</p></div>
  <div class="where__lists">
    <section class="pl"><h2 class="pl__h">{e(w['away_h'])}</h2><p>{e(w['away_text'])}</p><ul>{lst(far)}</ul></section>
    <section class="pl"><h2 class="pl__h">{e(w['near_h'])}</h2><p>{e(w['near_text'])}</p><ul>{lst(near)}</ul></section>
  </div>
</section>
{cta_band(t, t['mood_page']['plan_title'], t['mood_page']['plan_text'])}"""
    return page(t, "where", w["title"], w["desc"], main, [crumbs_ld(lang, [(t["ui"]["home"], url("home", lang)), (w["h1"], url("where", lang))])])


def render_reviews(t):
    lang, rp, r = t["lang"], t["reviews_page"], t["reviews"]
    note = f'<p class="reviews__note">{e(r["lang_note"])}</p>' if r["lang_note"] else ""
    main = f"""{crumbs(t, [(r['kicker'], None)])}
<section class="reviews reviews--page" aria-labelledby="rv-h">
  <div class="reviews__head">
    <p class="kicker">{e(r['kicker'])}</p>
    <h1 id="rv-h" class="sec-h sec-h--page"><span class="reviews__big">{icon('i-star')}{rating(t)}</span> {e(rp['h1'])}</h1>
    <p class="reviews__lede">{e(rp['lede'])}</p>{note}
    <a class="link" href="{C['maps_url']}" rel="noopener">{e(r['link'])}{icon('i-arrow')}</a>
  </div>
  <ul class="reviews__list">{quote_items(t, range(len(r['items'])))}</ul>
</section>
{cta_band(t, rp['cta_title'], rp['cta_text'])}"""
    return page(t, "reviews", rp["title"], rp["desc"], main, [crumbs_ld(lang, [(t["ui"]["home"], url("home", lang)), (r["kicker"], url("reviews", lang))])])


def render_visit(t):
    lang, d, v = t["lang"], t["desk"], t["visit_page"]
    facts = "".join(f"<li><strong>{e(a)}</strong> {e(b)}</li>" for a, b in d["facts"])
    find = "".join(f"<li>{e(x)}</li>" for x in v["find"])
    get = "".join(f"<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>" for a, b in v["getting"])
    main = f"""{crumbs(t, [(d['kicker'], None)])}
<section class="desk desk--page" aria-labelledby="desk-h">
  <div class="desk__text">
    <p class="kicker">{e(d['kicker'])}</p>
    <h1 id="desk-h" class="sec-h sec-h--page">{e(v['h1'])}</h1>
    <p class="desk__p">{e(v['lede'])}</p>
    <address class="desk__addr">{icon('i-pin')}<span>{e(d['address'])}<br><small>{e(v['plus_code'])} {e(C['plus_code'])}</small></span></address>
    <div class="desk__hours"><p class="desk__ht">{e(d['hours_title'])} <span class="desk__now" data-status-badge hidden></span></p>{hours_table(t)}</div>
    <div class="desk__btns">
      <a class="btn btn--sun" href="{wa(t['plan']['wa_simple'])}">{icon('i-wa')}{e(v['wa_cta'])}</a>
      <a class="btn btn--line" href="{C['maps_url']}" rel="noopener">{icon('i-pin')}{e(d['maps'])}</a>
      <a class="btn btn--line" href="{TEL}">{icon('i-phone')}{e(C['phone_display'])}</a>
    </div>
  </div>
  <figure class="desk__map">{locator_svg(t)}<p class="note note--desk">{e(d['note'])}</p></figure>
</section>
<div class="visit">
  <section class="visit__sec"><h2 class="dp__h2">{e(v['find_h'])}</h2><ol class="steps">{find}</ol></section>
  <section class="visit__sec"><h2 class="dp__h2">{e(v['getting_h'])}</h2><dl class="getting">{get}</dl>
    <p><a class="link" href="{url('transfers', lang)}">{e(d['transfers_line'])}{icon('i-arrow')}</a></p></section>
  <section class="visit__sec visit__team"><h2 class="dp__h2">{e(v['team_h'])}</h2><p>{e(v['team'])}</p>
    <ul class="desk__facts desk__facts--paper">{facts}</ul></section>
  <figure class="visit__photo">{img('minibus-smiles', '(min-width: 64em) 30vw, 90vw', cls='visit__img')}<figcaption>{e(d['photo_caption'])}</figcaption></figure>
  <section class="reviews reviews--inline" aria-label="{e(t['reviews']['kicker'])}"><ul class="reviews__list">{quote_items(t, v['quotes'])}</ul></section>
</div>"""
    return page(t, "visit", v["title"], v["desc"], main, [org(t), crumbs_ld(lang, [(t["ui"]["home"], url("home", lang)), (d["kicker"], url("visit", lang))])])


def render_transfers(t):
    lang, tp, p = t["lang"], t["transfers_page"], t["plan"]
    routes = "".join(f"<li>{e(label)}</li>" for k, label in tp["routes"] if k != "other")
    opts = f'<option value="">{e(tp["route_choose"])}</option>' + "".join(f'<option value="{k}">{e(label)}</option>' for k, label in tp["routes"])
    simple = wa(t["transfers"]["wa"])
    main = f"""{crumbs(t, [(tp['h1'], None)])}
<article class="dp c-atlantic tp" aria-labelledby="tp-h">
  <header class="dp__band">
    <p class="dp__mood">{e(t['transfers']['kicker'])}</p>
    <h1 class="dp__h" id="tp-h">{e(tp['h1'])}</h1>
    <p class="dp__lede">{e(tp['lede'])}</p>
    <div class="dp__cta"><a class="btn btn--sun" href="#transfer">{icon('i-wa')}{e(tp['form_title'])}</a></div>
  </header>
  <div class="dp__body">
    <div class="dp__side"><figure class="dp__fig">{img('transfer-van', '(min-width: 64em) 42vw, 100vw', cls='dp__img', lazy=False, priority=True)}</figure></div>
    <div class="dp__main">
      <section class="dp__sec"><h2 class="dp__h2">{e(tp['routes_h'])}</h2><ul class="routes">{routes}</ul></section>
      <section class="dp__sec"><h2 class="dp__h2">{e(tp['vehicle_h'])}</h2><p>{e(tp['vehicle'])}</p></section>
      <section class="dp__sec"><h2 class="dp__h2">{e(tp['late_h'])}</h2><p>{e(tp['late'])}</p></section>
      <section class="reviews reviews--inline" aria-label="{e(t['reviews']['kicker'])}"><ul class="reviews__list">{quote_items(t, [tp['quote']])}</ul></section>
    </div>
  </div>
</article>
<section class="ask" id="transfer" aria-labelledby="tf-h" data-dock-hide>
  <div class="ask__head"><p class="kicker">{e(t['day']['ask_kicker'])}</p><h2 class="sec-h" id="tf-h">{e(tp['form_title'])}</h2><p>{e(tp['form_text'])}</p></div>
  <form class="planner ask__form" data-wa="transfer" novalidate>
    <div class="fld"><label for="t-route">{e(tp['route_label'])}</label><select id="t-route" name="route" required>{opts}</select><p class="err" data-err="route" hidden>{e(tp['err_route'])}</p></div>
    <div class="f f--row">
      <div class="fld"><label for="t-date">{e(tp['date_label'])}</label><input id="t-date" name="date" type="date" required><p class="err" data-err="date" hidden>{e(tp['err_date'])}</p></div>
      <div class="fld"><label for="t-time">{e(tp['time_label'])}</label><input id="t-time" name="time" type="time"></div>
      <div class="fld"><label for="t-flight">{e(tp['flight_label'])}</label><input id="t-flight" name="flight" type="text" placeholder="{e(tp['flight_ph'])}" autocomplete="off"></div>
    </div>
    <div class="f f--row">
      <div class="fld fld--num"><label for="t-people">{e(tp['people_label'])}</label><input id="t-people" name="people" type="number" inputmode="numeric" min="1" max="60" value="2" required><p class="err" data-err="people" hidden>{e(tp['err_people'])}</p></div>
      <div class="fld fld--num"><label for="t-bags">{e(tp['bags_label'])}</label><input id="t-bags" name="bags" type="number" inputmode="numeric" min="0" max="60"></div>
      <div class="fld"><label for="t-stay">{e(tp['stay_label'])}</label><input id="t-stay" name="stay" type="text" autocomplete="off"></div>
      <div class="fld"><label for="t-name">{e(tp['name_label'])}</label><input id="t-name" name="name" type="text" autocomplete="given-name"></div>
    </div>
    <div class="planner__go"><button class="btn btn--sun btn--big" type="submit">{icon('i-wa')}{e(tp['submit'])}</button>
      <a class="link" href="{simple}">{e(t['transfers']['cta'])}{icon('i-arrow')}</a></div>
    {ok_box(t)}
  </form>
</section>"""
    return page(t, "transfers", tp["title"], tp["desc"], main,
                [{"@type": "Service", "name": tp["h1"], "serviceType": "Airport transfer", "areaServed": ["Agadir", "Marrakech", "Casablanca", "Essaouira"],
                  "provider": {"@id": ORIGIN + "/#agency"}, "description": tp["desc"]},
                 {"@type": "TravelAgency", "@id": ORIGIN + "/#agency", "name": "Hala Tours Agadir", "url": ORIGIN + "/", "telephone": C["phone_display"]},
                 crumbs_ld(lang, [(t["ui"]["home"], url("home", lang)), (tp["h1"], url("transfers", lang))])],
                dock(t, "#transfer", tp["form_title"]))


def render_plan(t):
    lang, pp = t["lang"], t["plan_page"]
    steps = "".join(f"<li>{e(x)}</li>" for x in pp["aside"])
    main = (crumbs(t, [(t["ui"]["cta_plan"], None)]) + planner(t, "h1")
            + f'<aside class="plan__next"><h2 class="dp__h2">{e(pp["aside_h"])}</h2><ol class="steps">{steps}</ol>'
            + f'<p><a class="link" href="{url("days", lang)}">{e(pp["browse"])}{icon("i-arrow")}</a></p></aside>')
    return page(t, "plan", pp["title"], pp["desc"], main, [crumbs_ld(lang, [(t["ui"]["home"], url("home", lang)), (t["ui"]["cta_plan"], url("plan", lang))])])


def render_credits(t):
    lang, cp = t["lang"], t["credits_page"]
    used = {}
    for d in DAYS:
        if d["img"] and IMG[d["img"]].get("credit"): used.setdefault(d["img"], []).append(d)
    rows = []
    for name, m in IMG.items():
        c = m.get("credit") if not name.startswith("_") else None
        if not c: continue
        on = ", ".join(f'<a href="{url("day:" + d["id"], lang)}">{e(d[lang]["name"])}</a>' for d in used.get(name, []))
        rows.append(f'<li class="cr">{img(name, "160px", cls="cr__img")}<div><p class="cr__place">{e(c["place"][lang])}</p>'
                    f'<p>{e(cp["by"])} {e(c["author"])} · {e(cp["licence"])} <a href="{e(c["license_url"])}" rel="noopener license">{e(c["license"])}</a> · '
                    f'<a href="{e(c["source"])}" rel="noopener">{e(cp["source"])}</a></p><p class="cr__small">{e(cp["changes"])} {e(cp["used_on"])}: {on}</p></div></li>')
    main = f"""{crumbs(t, [(cp['h1'], None)])}
<section class="credits" aria-labelledby="cr-h">
  <h1 class="sec-h sec-h--page" id="cr-h">{e(cp['h1'])}</h1>
  <p class="credits__lede">{e(cp['lede'])}</p>
  <h2 class="dp__h2">{e(cp['own_h'])}</h2><p>{e(cp['own'])}</p>
  <h2 class="dp__h2">{e(cp['commons_h'])}</h2><ul class="cr__list">{''.join(rows)}</ul>
  <h2 class="dp__h2">{e(cp['map_h'])}</h2><p>{e(cp['map'])} <a href="{cp['odbl']}" rel="noopener">openstreetmap.org/copyright</a></p>
  <h2 class="dp__h2">{e(cp['fonts_h'])}</h2><p>{e(cp['fonts'])}</p>
</section>"""
    return page(t, "credits", cp["title"], cp["desc"], main, [crumbs_ld(lang, [(t["ui"]["home"], url("home", lang)), (cp["h1"], url("credits", lang))])])


def render_404():
    n, f = T["en"]["notfound"], T["fr"]["notfound"]
    return f"""<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(n['title'])}</title><meta name="description" content="{e(n['text'])}"><meta name="robots" content="noindex">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<style>
body{{margin:0;min-height:100vh;display:grid;place-items:center;background:#1b2390;color:#fffcf6;font:18px/1.5 system-ui,sans-serif;padding:24px;box-sizing:border-box}}
main{{max-width:34rem}}h1{{font-size:clamp(2.2rem,8vw,3.6rem);line-height:1.02;margin:.2em 0 .4em;letter-spacing:-.02em}}
.fr{{margin-top:2.2em;padding-top:1.4em;border-top:2px solid rgba(255,252,246,.3)}}.fr .h{{font-size:1.6rem;font-weight:700;line-height:1.1;margin:0 0 .3em}}
.sun{{width:72px;height:72px;border-radius:50%;background:#f39800}}a{{display:inline-block;margin:.4em 1em .4em 0;padding:.8em 1.2em;border-radius:999px;background:#f39800;color:#10143f;font-weight:700;text-decoration:none}}
a.alt{{background:transparent;color:#fffcf6;box-shadow:inset 0 0 0 2px #fffcf6}}
</style></head>
<body><main><div class="sun" aria-hidden="true"></div><h1>{e(n['h1'])}</h1><p>{e(n['text'])}</p>
<p><a href="/">{e(n['home'])}</a><a class="alt" href="{wa(T['en']['plan']['wa_simple'])}">WhatsApp</a></p>
<div class="fr" lang="fr"><p class="h">{e(f['h1'])}</p><p>{e(f['text'])}</p><p><a href="/fr/">{e(f['home'])}</a><a class="alt" href="{wa(T['fr']['plan']['wa_simple'])}">WhatsApp</a></p></div>
</main></body></html>
"""


def write(rel, text):
    path = os.path.join(SITE, rel.lstrip("/"))
    if rel.endswith("/"): path = os.path.join(path, "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return os.path.relpath(path, SITE)


def renderers():
    yield "home", render_home
    yield "days", render_days
    for m in CAT["moods"]:
        yield "mood:" + m["id"], lambda t, mid=m["id"]: render_mood(t, mid)
    for d in DAYS:
        yield "day:" + d["id"], lambda t, did=d["id"]: render_day(t, did)
    yield "where", render_where
    yield "reviews", render_reviews
    yield "visit", render_visit
    yield "transfers", render_transfers
    yield "plan", render_plan
    yield "credits", render_credits


def main():
    written = []
    keys = []
    for key, fn in renderers():
        keys.append(key)
        for lang in LANGS:
            written.append(write(PAGES[key][lang], fn(T[lang])))
    written.append(write("/404.html", render_404()))
    # sitemap with hreflang pairs
    urls = []
    for key in keys:
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{l2}" href="{ORIGIN}{PAGES[key][l2]}"/>' for l2 in LANGS)
        alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{ORIGIN}{PAGES[key]["en"]}"/>'
        for lang in LANGS:
            urls.append(f"<url><loc>{ORIGIN}{PAGES[key][lang]}</loc>{alts}</url>")
    write("/sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
          + "\n".join(urls) + "\n</urlset>\n")
    write("/robots.txt", f"User-agent: *\nAllow: /\nSitemap: {ORIGIN}/sitemap.xml\n")
    write("/_headers", "/assets/*\n  Cache-Control: public, max-age=31536000, immutable\n"
          "/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: SAMEORIGIN\n"
          "  Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=()\n"
          "  Content-Security-Policy: default-src 'self'; img-src 'self' data:; style-src 'self' 'unsafe-inline'; "
          "script-src 'self' https://static.cloudflareinsights.com; font-src 'self'; connect-src 'self' https://cloudflareinsights.com; "
          "object-src 'none'; base-uri 'self'; frame-ancestors 'self'; form-action 'self'\n")
    print(f"built {len(written)} files ({len(keys)} pages × {len(LANGS)} languages + 404)")


if __name__ == "__main__":
    main()
