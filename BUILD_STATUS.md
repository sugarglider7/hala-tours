# BUILD STATUS — hala-tours

_Last updated: 2026-10-02 06:40 UTC by DesignHala (Phase 2 design + EN homepage done)_

## Recovered state (resume of crashed run "agadir-batch2")
- Prior run left ONLY raw material (no repo, no status files, no code, no deployment):
  raw page dumps + downloaded images, now in `research/raw/` (gitignored; on disk at /home/agent/agadir-pilot/sites/hala-tours/research/raw/). Original copy still at /tmp/sites2/hala-tours/.
- Confirmed on 2026-10-02: no GitHub repo, no Cloudflare Pages project, no live hala-tours.peashoot.io before this run.

## Orchestrator decisions (binding, 2026-10-02)
1. Phone/WhatsApp: use **+212 660 732 477** everywhere (tel + wa.me/212660732477) — it is what the official site and its own WhatsApp button publish. Never show the Google variant …177. One constant in the build; owner to confirm.
2. Catalogue: show all distinct live products (boat 94/99 merged). Review-evidenced products get full pages. Listed-but-unconfirmed (balloon, Zagora 2 days, El Borj 2 days, Essaouira+Marrakech 2 days, Tafraout/Tiznit) stay, framed "on request — ask us for dates", content limited to route facts that are still true today (no collapsed Legzira arch, no demolished Tifnit village), no promised times/meals unless the live site states them and they are plausible today.
3. Prices: none anywhere (all 2022 / stale) — including transfers. "Ask for today's price" via WhatsApp.
4. People: Ayoub may be named by first name (130 reviews + official site links his socials) as part of "Ayoub and the team" — no title, no bio. Mustafa only inside real quotes.
5. Images: DO-NOT-USE the cross-agency duplicates and the generic web product photos (unknown copyright). Use Hala's own photos (WhatsApp gallery + Google owner photos). Destination context imagery: Wikimedia Commons files with free licences (CC0/PD/CC BY/CC BY-SA), CONTEXT-ONLY (places, never vehicles/guides/groups implying Hala), credited on a /credits/ page (+ FR) with author, licence, link.
6. Visit Hala: lightweight self-drawn SVG locator map from OSM geometry around Hotel Hamilton + "Open in Google Maps" link; hours as on the Google listing (Mon–Sat 08:00–23:00, Sun 09:00–22:00).

## Orchestrator review (phase 2 → phase 3, binding)
- Homepage proof approved: "the desk's own guidebook" — seven colour-coded mood chapters, thumb-index tabs, Kalam desk notes, sketch map, duration rings, WhatsApp day planner. Keep it.
- SHORTEN THE HOMEPAGE: at 390 px it is ~17,000 CSS px. Each mood chapter on the homepage shows its photo + intro + the first 3 days, then "All N days in <mood> →" linking to that mood's own page (which lists every day of the mood). Length filter keeps working across what's shown (and on mood pages). Target ≤ ~11,000 CSS px at 390.
- Planner: keep the homepage planner AND build `/plan/` (+ `/fr/plan/`) from the same partial; "Add to my day" persists across pages (localStorage) and inner pages link to /plan/. Every experience page also has a one-tap "Ask about this day on WhatsApp" with a prefilled message naming the day.
- Pages to build: one page per day (24) + transfers; one page per mood (7); where we go (map); visit the desk (OSM map, hours, how to find it in the Hamilton, phone/WhatsApp, Google Maps link); reviews; plan; credits (Commons licences); 404 — all EN + FR.
- Phone/WhatsApp stays +212 660 732 477 (single constant) — owner to confirm vs Google's …177.
- Experience pages render only verified fields (no "N/A"); "On request" badge kept for the 5 unconfirmed days; no prices anywhere.
- Live: https://hala-tours.peashoot.io/ (Cloudflare Pages project hala-tours, output dir site/, auto-deploys on push to main).

## Research
- DONE 2026-10-02 (ResearchHala): SOURCE_OF_TRUTH.md · CONTENT_INVENTORY.md · ASSET_INVENTORY.md · LEGACY_CONTENT_INVENTORY.md · research/notes-{catalogue,provenance,reviews,contact-location}.md.
- Live site re-crawled (raw: research/raw/crawl2/, index.json maps URL→file; products_live.txt). All 390 Google reviews captured (research/raw/google_reviews_2026-10-02.json). 8 Google "By owner" photos downloaded (research/raw/images/google-owner/). Contact sheets: /home/agent/agadir-pilot/qa/hala-tours/sheets/.
- Catalogue: 26 live product pages (FR+EN) = every BRIEF baseline item; boat trip duplicated (ids 94/99). Sold per reviews: quad (no.1), camel, horse, buggy, jet ski, Paradise Valley, Marrakech, Essaouira, Petit Désert 4x4, hammam, Crocoparc, boat, Legzira, Taroudant, city tour, transfers. No evidence: balloon, Zagora 2d, El Borj 2d, Essaouira+Marrakech 2d, Tafraout.
- Ratings: Google 5.0 (390). No Tripadvisor/Viator/GYG listing for Hala.

## Design
- DONE 2026-10-02 (DesignHala) — `BRAND_NOTES.md` (concept, palette, type scale, nav, CTA, forms, conversion spec EN+FR, experience-page template, page map + homepage section plan, must-not-look-like).
- Concept: **the desk's own guidebook** — seven colour-coded mood chapters with thumb-index tabs, handwritten desk notes, Agadir-at-the-centre sketch map, day-length rings; WhatsApp day planner.
- Fonts: Bricolage Grotesque (display + text) + Kalam 700 (desk notes only), self-hosted, 4 woff2 files; registered in /home/agent/agadir-pilot/FONTS.md.
- Palette from Hala's logo (sun #f39800, saffron #f9b700, wave #0d6fb8, sky #28a7e1) and own photos (robe cobalt #1b2390, dune #e8a773, jet-ski chili #b8262c, argan #55702f), ink #10143f on paper #fffcf6.
- Tooling: `tools/build.py` (stdlib; renders site/ from `tools/content/catalogue.json` + `en.json`, FR = parallel `fr.json`; unbuilt pages fall back to homepage anchors so check_site never sees a missing target), `tools/images.py` + `tools/images.json` (Pillow, sequential, WebP + LQIP + favicons), `tools/data/osm-hamilton.json` (OSM extract for the locator SVG, © OSM contributors). Run: `python3 tools/images.py` (only when images.json changes), then `python3 tools/build.py`.
- Assets: `site/assets/css/site.css` (28 KB), `site/assets/js/site.js` (10 KB, deferred), favicon.svg + favicon-32.png + apple-touch-icon.png, `_headers`, robots.txt, sitemap.xml, 404.html.

## Pages implemented
- `/` (EN homepage, final quality): header · hero · length filter + 7 mood chapters (24 days) · day-trip map · reviews · Visit the desk (+ OSM locator, hours, live open/closed, airport transfers) · WhatsApp planner · footer · mobile dock + menu sheet.
- `/404.html` (self-contained).

## Pages remaining (phase 3; URLs in BRAND_NOTES §13)
- FR mirror of everything: `fr.json` with the same keys (+ language switch, hreflang — build already emits hreflang pairs once a page exists in both languages).
- `/days/` guide index + 24 experience pages `/days/<slug>/` (template BRAND_NOTES §12) — then turn day names into links (`url()` helper).
- `/transfers/`, `/visit/` (full Visit Hala page: bigger locator, directions from airport/bus, "Ayoub and the team"), `/plan/` (planner page; dock + header CTA already point to `url('plan')`, now `/#plan`), `/credits/` (needed as soon as Commons place images are used).
- Commons CONTEXT-ONLY place imagery for destination pages (Paradise Valley, Marrakech, Taroudant/Tiout, Tafraout, Legzira, Tiznit) + credits.

## Factual uncertainties
- PHONE CONFLICT: site +212 660 732 477 (also its WhatsApp button) vs Google +212 660 732 177. Unresolvable online → owner must confirm. Build with ONE constant (working value …477).
- All site prices STALE (2022) → show none.
- Legacy product text is copied from other operators; 13 product photos shared with other agencies; remaining product photos stock → only ~18 unique first-party photos usable (gallery + Google owner). No photo of the Hamilton desk.
- People: Ayoub (130 reviews; site links to his personal FB/IG) safe as "the person you meet at the desk", no title. Mustafa (5 reviews) only with owner OK. Others: do not publish.
- Desk location inside Hotel Hamilton (main reception/entrance per reviews) — exact spot, walk-in policy, payment/cancellation, pickup zones beyond Agadir, guide languages: unknown.
- Multi-day tours + balloon + Tafraout: listed but unconfirmed → shown with an "On request" badge and route facts only.
- Homepage lengths per day ("Couple of hours / Half day / All day / Two days") are approximate groupings from the live site's stated times; Paradise Valley shown as half or full day (owner question 11); Crocoparc "half day" is our grouping (30 min drive each way + park).
- Live "desk open now" status uses the Google hours in Africa/Casablanca time (Ramadan hours unknown).

## QA status
- Phase 2 self-checks done (see Log 06:32). Full QA pending (phase 4; QA_CHECKLIST.md).

## Deployment URL
- target: https://hala-tours.peashoot.io/ (Cloudflare Pages project "hala-tours", output dir `site/`, no build command) — not yet created

## Outstanding problems
- Orphan Google Maps tabs may remain in shared Chromium from ResearchHala's timed-out tab.run (not closable from its kernel) — orchestrator informed.
- No photo of the desk/Hamilton entrance (biggest image gap; Fadwa could take one). Visit section uses the OSM locator + minibus photo instead.
- Guests' faces in Hala's own photos (hero riders, minibus selfie) — owner should confirm reuse consent.

## Log
- 05:08 recovery: workspace created from prior raw research; brief + standard written.
- 05:20 ResearchHala: live re-crawl, Google listing + 390 reviews captured, provenance check vs sibling template sites.
- 05:35 partial commit (SOURCE_OF_TRUTH, LEGACY inventory, notes).
- 05:50 research complete: CONTENT + ASSET inventories, BUILD_STATUS updated.
- 05:52 DesignHala: read contracts/inventories, looked at full-size first-party photos, sampled palette (logo + robe/dune/jet-ski/argan), registered fonts.
- 05:58 tooling: images.json/images.py (hero 1600 w was 310 KB → capped at 1440 w = 251 KB; mobile crop 560/800 w 57/108 KB), OSM extract via api.openstreetmap.org (Overpass returned 406), build.py, site.css, site.js.
- 06:10 round 1 (qa/hala-tours/p2/round1-*): mobile fold strong but eyebrow repeated the header ("at the Hotel Hamilton" twice), rating below the fold; rows 150 px tall because "Add to my day" had its own line (page 17.9k px); locator map showed mostly grass (only primary/tertiary roads, no buildings/service roads) and its label covered the pin; day map labels unreadable at 390 (product names, 15 px at 0.75 scale) and Paradise Valley/Taroudant collided; desktop flipped chapters squeezed the list into the 5/12 column; thumb index visible over the hero with ellipsised labels; reviews heading read "5.0 5.0 on Google". → eyebrow now states what Hala sells, proof moved directly under the photo, add-button moved to the length row, locator rebuilt with buildings/service roads/pools/beach (RDP-simplified, 92 KB HTML / 26 KB gz), short map labels at 19 px, flip grid 7/5, thumbs use short names and appear only when the guide crosses mid-screen, heading fixed; adults/children pluralised properly in the WhatsApp text.
- 06:25 round 2 (round2-*): desktop rhythm right, all chapters balanced; mobile 16.9k px (was 17.9k). Remaining: proof rows loose on phone, cobalt "Two days" tab invisible on the cobalt menu sheet → tightened, sheet tab inverted to paper.
- 06:32 round 3 (round3-390-fold/full/menu, round3-1440-fold/full/guide): final. Functional checks at 360/390: no horizontal overflow (scrollWidth 360), menu aria-expanded/Esc/focus return/closes on link tap, length filter (Two days → 3 rows, 6 chapters collapse), Add to my day → dock count + planner chips, validation errors (adults 0), composed wa.me text decoded correctly (no empty/undefined lines), mailto fallback body, no console errors, no failed requests on fresh loads. check_site OK, 0 WARN. Tab closed, preview stopped.
