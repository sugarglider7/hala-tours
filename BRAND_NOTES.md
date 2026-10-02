# BRAND_NOTES — Hala Tours Agadir

_Phase 2 (DesignHala, 2026-10-02). Binding for phase 3. Facts only from SOURCE_OF_TRUTH.md; orchestrator decisions in BUILD_STATUS.md override everything._

## 1. What Hala sells, to whom, and the one action
- **Emotionally:** relief and appetite. "I'm in Agadir for a week — what do I actually do?" answered by locals who know two dozen kinds of day and will tell you honestly which one suits you (and your kids), then collect you from your hotel.
- **Customer:** holidaymakers already in Agadir (often staying in the Hotel Hamilton area / city hotels), families with kids, couples, groups of friends; English and French speakers; browsing on a phone between beach and dinner. Many walk past or into the Hamilton.
- **Primary conversion:** a WhatsApp message to +212 660 732 477 composed by the day planner ("Tell us what sort of day you want"). Secondary: walk to the desk (Hotel Hamilton, Bd Mohammed V; Mon–Sat 08:00–23:00, Sun 09:00–22:00), call.
- **Proof points we may use:** 5.0 on Google from 390 reviews; a physical desk in a real hotel; hotel pickup on almost every trip; English and French; "Ayoub and the team" (first name only, no title).

## 2. Visual thesis + the one creative concept
**The desk's own guidebook.** The site reads like a joyful printed travel guide to the days around Agadir, marked up by the people at the Hala desk. Three devices carry it — none of them needs photos Hala doesn't have:
1. **Mood chapters with thumb-index tabs.** The catalogue is seven colour-coded chapters ("Sand & engines", "Salt water", "Hooves, humps & crocodiles", "Medinas & markets", "Palms, gorges & mountain villages", "Go slow", "Two days, one night away"). Each chapter opens with a big colour band whose number sits on a folder tab; on desktop the same colours stand as a thumb index on the right edge of the screen, like the tabs cut into a guidebook's pages. Breadth becomes a set of choices, not a wall of cards.
2. **Handwritten desk notes** (Kalam) — short, true, local advice in the margin: "In summer we go to Paradise Valley in the morning. The afternoons are scorching." / "Ask for the sunset ride." Max one per chapter, never decorative filler.
3. **Agadir in the middle** — a sketch map with the desk at the centre and dotted routes out to every day trip in its mood colour; plus the day-length glyph: a ring that fills (quarter = a couple of hours, half = half a day, full = all day, two rings = two days).

The colour is the joy; typography is the confidence; Hala's own phone photos are the proof.

## 3. Typography (registered in /home/agent/agadir-pilot/FONTS.md)
- **Bricolage Grotesque** (variable opsz 12–96, wght 200–800), self-hosted woff2 latin + latin-ext (`site/assets/fonts/bricolage-*.woff2`, 77 KB + 31 KB; latin preloaded). Display at wght 800 + `opsz 96` with tight tracking (−0.035em) — warm, ink-trapped, a little cheeky, loud enough for "What kind of day do you want?". Body at 400–600 (auto optical size) stays readable on phones. Fits Hala: energetic and friendly, not a luxury serif, not a corporate sans.
- **Kalam 700** (latin + latin-ext, 22 KB + 12 KB) — the desk's handwriting; used only for notes, "Pick a mood", captions. It is a hand, not a label/mono face.
- 4 font files total; `font-display: swap`; `font-synthesis: none` (no fake bold/italic). No italics anywhere.
- Self-hosted (not Google link) to avoid a third-party connection and to preload the one critical file. Source: Google Fonts CSS2 API fetched with a modern Chrome UA via curl (2026-10-02), files copied verbatim, unicode-ranges copied into `site.css`.

| role | 390 px | 1440 px | weight / settings |
|---|---|---|---|
| H1 (hero question) | 44 px / 0.94 | 102 px / 0.94 | 800, opsz 96, −0.035em, `text-wrap: balance` |
| Chapter title (h2) | 40 px / 0.92 | 88 px / 0.92 | 800, opsz 96 |
| Section title (`.sec-h`) | 34 px / 1.0 | 58 px / 1.0 | 800, opsz 96 |
| Day name (h3) | 21 px / 1.12 | 26 px | 700, opsz 32 |
| Review quote | 21 px / 1.18 | 32 px | 600, opsz 48 |
| Body | 17 px / 1.5 | 18 px / 1.5 | 400 |
| Lede / chapter intro | 18–19 px | 19–20 px | 400 |
| Kicker | 13 px caps, +0.08em | same | 700 |
| Desk note (Kalam) | 19–22 px / 1.12, rotated −3° | 22 px | 700 |
(all sizes are `clamp()` between these points — see `site.css`.)

## 4. Palette (hex, sampled with Pillow from Hala's own logo and photos)
| token | hex | source | use |
|---|---|---|---|
| `--ink` | #10143f | darkest shadow of the blue robe (#15 gallery, sampled #0C156B, deepened) | text, borders, footer |
| `--paper` | #fffcf6 | — (near white, deliberately NOT beige) | page ground |
| `--cobalt` | #1b2390 | the blue robe, gallery photo #15 (sampled #0C156B–#2F2D6B) | "Two days" mood, desk band, menu sheet |
| `--atlantic` | #0d6fb8 | logo wave (dominant logo pixel #0D6FB8) | "Salt water", sea on maps |
| `--sky` | #28a7e1 | logo sky (#28A7E1) | "Go slow" |
| `--sun` | #f39800 | logo sun (#F39800) | primary CTA, map home, stars, favicon |
| `--saffron` | #f9b700 | logo sun rim (#F9B700) | "Hooves…", kickers on cobalt |
| `--dune` | #e8a773 | sand in the quad photo #13 (sampled #E8A773) | "Sand & engines" |
| `--chili` | #b8262c | red jet-ski hull, photo #11 (median red #B8262C) | "Medinas & markets", pin |
| `--argan` | #55702f | argan foliage in photo #13 (sampled #504E28, saturated) | "Palms, gorges…" |
Each mood also has `--cd`, a deeper version for text/lines on paper (dune → #9a4f1c, saffron → #865c00, sky → #0a6690; dark moods use themselves). Text contrast: ink on dune/saffron/sky/sun ≥ 6:1; paper on atlantic/chili/argan/cobalt ≥ 5:1.

## 5. Grid, spacing, shape
- Max width 1320 px; side padding 20 / 40 / 56 px (390 / ≥768 / ≥1280). Desktop chapters: 5/7 columns (photo / list), alternating sides (`.ch--flip`); hero 1.05fr / 1fr.
- Vertical rhythm: sections 56–96 px; chapters 44 px (mobile) / 72 px (desktop) apart.
- Shapes: tabs and mood chips have one squared corner (`12px 12px 12px 3px`) like a cut index tab; photos radius 14 px with a soft shadow; pills for buttons. Dotted rules between days (guidebook), solid 2 px ink rules between sections.

## 6. Image treatment
- Only Hala's own photos (ASSET_INVENTORY status USE); never captioned with a person's name; no place names on photos whose place isn't known.
- Declarative list `tools/images.json` → `tools/images.py` (Pillow, sequential) → WebP q74, widths per role, dominant colour + 20 px LQIP baked into `style` so nothing flashes white; art-directed hero crop for phones (`hero-horses-m`, 560/800 w ≤ 108 KB) and desktop (`hero-horses`, 800/1100/1440 w ≤ 251 KB).
- Photos sit straight (no polaroid tilt); they overlap the bottom of their chapter band by 52–72 px so band + photo read as one spread.
- Chapters without an owned photo (Palms, gorges & mountain villages) get a **place-name stack** (big alternating heavy/light names in the mood colour) instead of borrowed imagery. Phase 3 may add Wikimedia Commons place imagery on destination pages only, CONTEXT-ONLY, credited on /credits/ (author, licence, link), never next to vehicles/people implying Hala.
- OG image: 1200×630 JPEG crop of the cliff-top horse ride.

## 7. Motion
- CSS only + IntersectionObserver: chapter photos and review rows rise 22 px and fade in once; tabs lift/tilt 1.5° on hover; thumb-index tab slides out for the chapter in view; dock slides away near the planner/footer. Durations 0.2–0.6 s, one easing (`cubic-bezier(.2,.7,.2,1)`).
- `prefers-reduced-motion: reduce` kills all transitions/smooth scroll. Content is visible without JS (hidden states only apply under `.js`).

## 8. Navigation
- **Desktop (≥1024):** slim sticky top bar: wordmark (sun + "Hala Tours Agadir", "at the Hotel Hamilton" underneath) · The days · Where we go · Visit the desk · Reviews · phone · "Plan my day" (sun pill). Plus the **thumb index** on the right edge (≥1152 px), visible only while the guide is mid-screen.
- **Mobile:** non-sticky header (wordmark + Menu). Menu opens a full-screen cobalt sheet whose main content is the seven mood tabs, big; then practical links and WhatsApp/Call. `aria-expanded`, focus moves in, Tab is trapped, Esc and link taps close, focus returns.
- **Sticky mobile action = "the dock":** a floating three-part bar at the bottom — Menu · "Tell us your day" (sun, WhatsApp glyph; shows a count and switches to "Plan on WhatsApp" once days are picked) · Call. Hidden while the planner or footer is on screen, so it never covers the submit button or footer contacts. Body has 84 px bottom padding on mobile.
- Language switch: not shown until FR exists (phase 3: `EN · FR` text links in the top bar + sheet, keeping the current page via the PAGES map).

## 9. CTA treatment
- One primary colour for action: `--sun` pill with ink text and the WhatsApp glyph. Secondary: ink pill, outline pill. Text links with arrow.
- Every product row has "+ Add to my day" (toggle, `aria-pressed`) → picks are kept in sessionStorage (shared across pages in phase 3) and appear as removable coloured chips in the planner.
- Experience pages (phase 3): primary button **"Check today's price on WhatsApp"** with the trip name prefilled. Prices are never printed anywhere (orchestrator decision 3).

## 10. Form styling
- Inputs ≥ 52 px tall, 17 px text (no iOS zoom), 2 px ink border, radius 12, white fill on paper; focus = 3 px sun outline; errors in chili under the field with `aria-invalid` + `aria-describedby`.
- Moods as colour-coded checkbox tabs; length as radio pills with the day-ring glyph; adults/children as numeric inputs (`inputmode="numeric"`); children's ages field appears only when children > 0; date `type=date` with `min=today`.

## 11. Conversion flow spec (verified channels only)
Channels: WhatsApp/phone **+212 660 732 477** (one constant `contact` in `tools/content/catalogue.json`; owner to confirm vs Google's …177), email **halatoursagadir@gmail.com**. Nothing else.
1. Fields: kind of day (mood checkboxes, optional) · days picked (from "Add to my day", optional) · length (radio, default "Not sure") · date (optional, not in the past) · adults (required, 1–60, default 2) · children (0–40) · children's ages (optional, shown if children > 0) · where you're staying (optional) · name (optional) · anything else (optional).
2. Validation: need at least one of mood / picked day / free text ("Pick a mood, a day, or tell us below what you'd like."); adults ≥ 1; date not before today. Focus jumps to the first problem.
3. Compose → `https://wa.me/212660732477?text=<urlencoded>`, opened in a new tab; success box appears (focus moved) with **"Didn't open? Tap here"** (same URL), **call** link and **mailto** with the same body.
4. Template EN (lines only appear when filled — never "undefined"/empty):
```
Hello Hala Tours! I'd like to plan a day.

• Kind of day: Salt water
• Ideas: Quad biking; Paradise Valley
• Length: Half a day
• Date: Mon, 12 Oct 2026
• People: 2 adults, 1 child (ages: 6)
• Staying at: Hotel Hamilton
• Name: Sam
• Notes: …

What would you suggest, and what's today's price?
```
   Template FR (phase 3, `fr.json` same keys):
```
Bonjour Hala Tours ! J'aimerais organiser une journée.

• Envie de : Côté mer
• Idées : Quad ; Vallée du Paradis
• Durée : Une demi-journée
• Date : lun. 12 oct. 2026
• Personnes : 2 adultes, 1 enfant (âges : 6)
• Hébergement : Hôtel Hamilton
• Prénom : Sam
• Remarques : …

Que nous conseillez-vous, et quel est le prix aujourd'hui ?
```
5. Fallbacks: no-JS → plain wa.me link with a short greeting; footer + desk section always show tel/WhatsApp/mail; transfers have their own prefilled WhatsApp template (From / To / Date and flight time / Number of people).

## 12. Experience-page template (phase 3, `/days/<slug>/`, FR `/fr/sorties/<slug-fr>/`)
Only verified fields render; a missing field simply doesn't appear (no "N/A", no empty headings). Data per product goes into `catalogue.json` (structure) + `en.json`/`fr.json` (strings), keyed by product id.
1. **Band header** in the mood colour: breadcrumb ("Sand & engines" tab), h1 name, "On request" badge if `status: on_request`, day-ring + length.
2. **Photo** (Hala-owned) or, for destinations, a credited Commons place photo; else the place-name stack.
3. **Fact strip** (only filled ones): Duration / times ("Out 08:30, back around 17:30" — always "around") · Pickup ("From your hotel in Agadir") · Food ("Lunch in a Berber family's home" / "Lunch isn't included") · Included as stated (e.g. fishing gear, transport to the hammam).
4. **What happens** — 3–6 short steps from the verified itinerary (place names), in our voice; stale facts banned (Tifnit village, Legzira arch, "an hour" to Essaouira, third-party opening hours).
5. **Good to know** — desk notes (heat in summer, combine with…, kids' ages) in Kalam.
6. **Who it suits** — only when grounded (buggy two-seaters suit families; surf from about 7 — "ask us").
7. **CTA block:** "Check today's price on WhatsApp" (prefilled: trip name + date + people + hotel mini-form, same planner component) · call · "or come to the desk at the Hamilton".
8. **Related days** — same mood + same length, 3 rows in the guide-row style (not cards).
Multi-day + balloon + Tafraout pages: route facts only, "On request — ask us for dates", no promised meals/times beyond what the live site states and is plausible.

## 13. Page map (EN root + FR mirror)
| page | EN | FR | status |
|---|---|---|---|
| Home | `/` | `/fr/` | EN built (phase 2) |
| All days (guide + filters, by mood/length) | `/days/` | `/fr/sorties/` | phase 3 (homepage `#guide` until then) |
| 24 experience pages | `/days/<slug>/` (quad, buggy, sandboarding, little-desert, jet-ski, boat-trip, surf, legzira, camel, camel-bbq, horse, crocoparc, marrakech, essaouira, city-tour, paradise-valley, taroudant, tafraout, hammam, berber-evening, balloon, zagora, el-borj, marrakech-essaouira) | `/fr/sorties/<slug-fr>/` | phase 3 |
| Transfers | `/transfers/` | `/fr/transferts/` | phase 3 (`#transfers`) |
| Visit the desk (map, hours, directions, Ayoub and the team) | `/visit/` | `/fr/nous-trouver/` | phase 3 (`#desk`) |
| Plan / contact (planner) | `/plan/` | `/fr/organiser/` | phase 3 (`#plan`) |
| Photo & map credits | `/credits/` | `/fr/credits/` | phase 3 (needed once Commons images appear) |
| 404 | `/404.html` | — | built |
No separate About/Team (team story beyond "Ayoub and the team" unverified) and no separate Reviews page (reviews live on Home + Visit).

### Homepage section plan (built)
| # | section | facts (SOT) | images |
|---|---|---|---|
| 1 | Header: wordmark, "at the Hotel Hamilton", nav, phone, Plan my day | name, address [VERIFIED S1,S2]; phone [CONFLICT S1,S3 → constant] | — |
| 2 | Hero: "Day trips, activities & transfers from Agadir", H1 "What kind of day do you want?", lede, rating, live desk status, mood tabs | catalogue breadth [S1]; hotel pickup [S1, S4]; 5.0 (390) [S3]; hours [S3] | `hero-horses` (#25, own Google photo) |
| 3 | The days: length filter + 7 mood chapters, 24 rows | per-product facts from notes-catalogue (S1), combos/sunset/heat as "ask us" notes [PROBABLE S4] | quad (#13), jet ski (#11), camel (#24), Essaouira cannon (#9), deckchair bay (#5), blue robe (#15); valleys = place-name stack |
| 4 | Where we go: sketch map, desk at centre | destination places [S1]; geography | SVG |
| 5 | Reviews: ★5.0 on Google, 5 exact quotes (name · Google review, no dates) | SOT §f quotes 1,2,3,9,10 [S4] | — |
| 6 | Visit the desk (cobalt): address, hours + live status, OSM locator, Maps link, phone; facts (pickup, families, languages, prices) ; photo; Airport transfers | [S1,S3,S12]; languages [PROBABLE S4]; transfers routes [S1] | `minibus-smiles` (#29); OSM SVG (© OSM contributors) |
| 7 | Tell us your day: WhatsApp planner | channels [S1] | — |
| 8 | Footer: visit, hours, contacts | [S1,S3] | — |

## 14. Must NOT look like
- GetYourGuide / Viator / Expedia / any marketplace: no price tags, star-rated product cards, "bestseller" badges, carts, availability calendars, "free cancellation".
- Identical white card grids; stock icon grids; carousels of the same card.
- Generic beige/terracotta Morocco: no arches-and-lanterns pattern, no zellige backgrounds, no beige paper.
- **agadir-trip.peashoot.io / agadir-camel-horse.peashoot.io** (Fraunces + Inter, dark full-bleed hero photo with serif headline over it, green WhatsApp + "Book now" bottom bar): Hala uses no serif, no text over a darkened photo, a sun-orange three-part dock with the menu in it, and colour-coded mood chapters.
- **hyle-surfhouse.peashoot.io:** warm host-centred surf house — no host portrait storytelling, no surf imagery as identity.
- **Hôtel Lynx (this batch):** wayfinding/signage language, monospace labels, room-key numerals, sign-plate headings — none here (Kalam is a hand, not a label face; no mono anywhere).
- **Line Up Surf House (this batch):** horizon lines, line-up geometry, surf-magazine width-stretched type, "a day by the break" timelines — none here (our day glyph is a closed ring, our structure is chapters + map, not horizons).
- SaaS gradients, glassmorphism, black-luxury, gradient text, generic wave/palm SVGs.

## 15. Copy voice
"We", short sentences, real place names and times, a little humour ("Bring sunglasses; you'll get sand everywhere."). Honest advice is the brand ("Lunch isn't included", "The afternoons are scorching"). Banned list per STANDARD §3; never expose research method; never print prices; Ayoub only as "Ayoub and the team".
