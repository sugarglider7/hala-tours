# BUILD STATUS — hala-tours

_Last updated: 2026-10-02 by FixHala (Phase 4 fix pass — Audit A + B findings applied, see QA_CHECKLIST "Fix log")_

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

## Pages implemented (phase 3, generated by `tools/build.py` — 39 page keys × EN/FR = 78 pages + 404)
- Data: `tools/content/days.json` (one record per day: slug EN/FR, mood, lengths, status, image, related days, EN+FR fields: name/line/title/desc/lede/facts/steps/tips/note/suits), `catalogue.json` (contact constant, moods, map), `en.json`/`fr.json` (chrome + page copy, identical keys).
- `/` + `/fr/` home (3 days per mood with their one-line description; "See all N days" only where a mood has more; chapters 4–7 compact on phones; map teaser card → /where-we-go/; filter collapses empty chapters + live count; compact planner with optional details) · `/days/` + `/fr/sorties/` (all 24 by mood + length filter) · 7 mood pages `/moods/<slug>/` + `/fr/envies/<slug>/` · 24 day pages `/days/<slug>/` + `/fr/sorties/<slug>/` (band, photo or route card (stops + length ring + desk note) for the 7 photo-less days, facts, steps, good to know, on-request block, WhatsApp ask form + one-tap link, related days, TouristTrip JSON-LD) · `/where-we-go/` `/fr/ou-nous-allons/` (full sketch map incl. El Borj/Tighmert, minor places, Souss river) · `/visit/` `/fr/nous-trouver/` · `/reviews/` `/fr/avis/` · `/transfers/` `/fr/transferts/` (transfer WhatsApp form) · `/plan/` `/fr/organiser/` · `/credits/` `/fr/credits/` · `/404.html` (EN+FR text, brand font + wordmark).
- Commons CONTEXT-ONLY place photos (8: Paradise Valley, Koutoubia, Taroudant ramparts, Tafraout painted rocks, Legzira 2018 surviving arch, Agadir port from Oufella, Agadir marina, Draa palm grove at Agdz) credited under each photo + on /credits/. Own photos added: dune-ocean (#7), essaouira-lane (#6), transfer-van (#27).
- "Add to my day" picks persist in localStorage across pages/languages; dock shows count; day pages dock → "Today's price" / on-request "Ask about dates" (#ask), with a "N days picked · Plan" chip above it when picks exist.

## Pages remaining
- None. All BRAND_NOTES page-map pages built EN + FR.

## Factual uncertainties
- PHONE CONFLICT: site +212 660 732 477 (also its WhatsApp button) vs Google +212 660 732 177. Unresolvable online → owner must confirm. Build with ONE constant (working value …477).
- All site prices STALE (2022) → show none.
- Legacy product text is copied from other operators; 13 product photos shared with other agencies; remaining product photos stock → only ~18 unique first-party photos usable (gallery + Google owner). No photo of the Hamilton desk.
- People: Ayoub (130 reviews; site links to his personal FB/IG) safe as "the person you meet at the desk", no title. Mustafa (5 reviews) only with owner OK. Others: do not publish.
- Desk location inside Hotel Hamilton (main reception/entrance per reviews) — exact spot, walk-in policy, payment/cancellation, pickup zones beyond Agadir, guide languages: unknown.
- Multi-day tours + balloon + Tafraout: listed but unconfirmed → shown with an "On request" badge and route facts only.
- Homepage lengths per day ("Couple of hours / Half day / All day / Two days") are approximate groupings from the live site's stated times; Paradise Valley shown as half or full day (owner question 11); Crocoparc "half day" is our grouping (30 min drive each way + park).
- Live "desk open now" status uses the Google hours in Africa/Casablanca time (Ramadan hours unknown).
- Legzira photo is the surviving arch (Commons, dated 2018); captioned as such — copy promises no arches.
- Sandboarding: legacy text (copied) vs reviews disagree on where it runs → page names no dunes/lunch, "ask us".

## QA status
- Phase 3 QA done: 3 screenshot rounds (qa/hala-tours/p3/r1-*, r2-*, r3-*, live-home-390), 360 px overflow sweep over all 79 pages, forms EN/FR decoded, perf per template, check_site OK (2 WARN justified: real quote "Paradise city"). Details + per-page claim tables in QA_CHECKLIST.md.
- Phase 4: Audit A (facts & copy, A1–A26) + Audit B (visual/mobile/conversion, B1–B27) applied — 51 fixed, B25 partly (inner band padding kept by design), A14 = owner decision (phone). Fix log with verification per ID in QA_CHECKLIST.md; screenshots qa/hala-tours/p4-fix/. check_site OK; 360 sweep of 79 pages clean; EN/FR day, on-request, transfer and planner messages decoded.

## Deployment URL
- https://hala-tours.peashoot.io/ — Cloudflare Pages project "hala-tours" (output dir `site/`). Push does NOT auto-deploy: run `/home/agent/agadir-pilot/tools/cf-static-deploy.sh hala-tours deploy` after pushing.
- Live check 2026-10-02 (deploy 9f4f269): `/`, `/days/marrakech/`, `/fr/`, `/fr/sorties/vallee-du-paradis/` → 200, canonical correct, no broken images, no overflow at 390, mailto links intact (no Cloudflare email-protection rewrite), `/does-not-exist/` → 404 page; no failed requests/console errors after allowing the Cloudflare Insights beacon in CSP.
- Live check 2026-10-02 after phase 4 (deploy 3aafb61, CSS ?v=de8413ae): at 390 `/`, `/fr/`, `/days/`, `/days/hot-air-balloon/`, `/days/buggy/`, `/where-we-go/`, `/transfers/`, `/visit/`, `/fr/sorties/desert-de-zagora/`, valleys mood page → no overflow, no broken images, no aggregateRating, no console errors/failed requests; header FR pill → `/fr/`; "Two days" filter → 1 chapter + "3 days fit “Two days”"; balloon form → "Could it run on my dates…" decoded. Shots `qa/hala-tours/p4-fix/live-*`.

## Outstanding problems
- Orphan Google Maps tabs may remain in shared Chromium from ResearchHala's timed-out tab.run (not closable from its kernel) — orchestrator informed.
- No photo of the desk/Hamilton entrance (biggest image gap; Fadwa could take one). Visit section uses the OSM locator + minibus photo instead.
- Guests' faces in Hala's own photos (hero riders, minibus selfie) — owner should confirm reuse consent.
- Homepage at 390 is 11.8k CSS px (11,763; was 11,871) although every home row now carries its one-line description; chapters 4–7 are compact on phones. With a length filter on, it drops to 6.9–9.1k.
- JSON-LD carries no aggregateRating (orchestrator decision); "5.0 on Google · 390 reviews" stays visible on the page.
- Visit page has no photo of the desk itself (none exists).

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
- 07:00 BuildHala: days.json (24 records EN+FR, fresh copy), 8 Commons place photos (API metadata in research/raw/commons/chosen.json) + 3 more own photos, multi-page build (39 page keys × 2), inner-page CSS, generic WhatsApp forms (plan/day/transfer), localStorage picks. Commit c55a93b.
- 07:10 round 1 screenshots; homepage 16.6k → 11.8k px; EN+FR pages commit 88d082b, deployed (orchestrator: deploy via cf-static-deploy.sh; email_off wrapping added).
- 07:25 round 2: FR, menu, forms filled/success, 404, desktop; fixes (mood filter placement, dock labels, valleys note overlap). Perf + functional checks recorded. Commits f545524, 9e2c507.
- 07:45 live verification; CSP allowed Cloudflare Insights beacon (was blocked). Commit 9f4f269 deployed. Tab closed, preview stopped.
- Phase 4 FixHala: facts/copy fixes in days/en/fr.json (on-request framing, "at the Hamilton", flamingo hedges, sandboarding/hammam specifics removed, transfers wording, FR typography pass in build.py, FR alts via images.json alt_fr, mobile hero re-cut), UI fixes (filter collapse + aria-live, whole-row links, mobile EN/FR pill, 44 px hero tabs, compact chapters 4–7, map teaser + full where map, route cards, dock picks chip, success box, 404 font, thumb index on the book edge, desktop h1 on two lines). Commit 3794b38 + follow-ups.
- Phase 4 deploy 3aafb61 (cf-static-deploy) + live verification at 390; tab closed, preview stopped.
