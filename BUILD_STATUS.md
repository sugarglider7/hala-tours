# BUILD STATUS — hala-tours

_Last updated: 2026-10-02 05:50 UTC by ResearchHala (Phase 1 research done)_

## Recovered state (resume of crashed run "agadir-batch2")
- Prior run left ONLY raw material (no repo, no status files, no code, no deployment):
  raw page dumps + downloaded images, now in `research/raw/` (gitignored; on disk at /home/agent/agadir-pilot/sites/hala-tours/research/raw/). Original copy still at /tmp/sites2/hala-tours/.
- Confirmed on 2026-10-02: no GitHub repo, no Cloudflare Pages project, no live hala-tours.peashoot.io before this run.

## Research
- DONE 2026-10-02 (ResearchHala): SOURCE_OF_TRUTH.md · CONTENT_INVENTORY.md · ASSET_INVENTORY.md · LEGACY_CONTENT_INVENTORY.md · research/notes-{catalogue,provenance,reviews,contact-location}.md.
- Live site re-crawled (raw: research/raw/crawl2/, index.json maps URL→file; products_live.txt). All 390 Google reviews captured (research/raw/google_reviews_2026-10-02.json). 8 Google "By owner" photos downloaded (research/raw/images/google-owner/). Contact sheets: /home/agent/agadir-pilot/qa/hala-tours/sheets/.
- Catalogue: 26 live product pages (FR+EN) = every BRIEF baseline item; boat trip duplicated (ids 94/99). Sold per reviews: quad (no.1), camel, horse, buggy, jet ski, Paradise Valley, Marrakech, Essaouira, Petit Désert 4x4, hammam, Crocoparc, boat, Legzira, Taroudant, city tour, transfers. No evidence: balloon, Zagora 2d, El Borj 2d, Essaouira+Marrakech 2d, Tafraout.
- Ratings: Google 5.0 (390). No Tripadvisor/Viator/GYG listing for Hala.

## Design
- BRAND_NOTES.md — not started

## Pages implemented
- none

## Pages remaining
- all

## Factual uncertainties
- PHONE CONFLICT: site +212 660 732 477 (also its WhatsApp button) vs Google +212 660 732 177. Unresolvable online → owner must confirm. Build with ONE constant (working value …477).
- All site prices STALE (2022) → show none.
- Legacy product text is copied from other operators; 13 product photos shared with other agencies; remaining product photos stock → only ~18 unique first-party photos usable (gallery + Google owner). No photo of the Hamilton desk.
- People: Ayoub (130 reviews; site links to his personal FB/IG) safe as "the person you meet at the desk", no title. Mustafa (5 reviews) only with owner OK. Others: do not publish.
- Desk location inside Hotel Hamilton (main reception/entrance per reviews) — exact spot, walk-in policy, payment/cancellation, pickup zones beyond Agadir, guide languages: unknown.
- Multi-day tours + balloon: listed but unconfirmed.

## QA status
- not started (see QA_CHECKLIST.md)

## Deployment URL
- target: https://hala-tours.peashoot.io/ (Cloudflare Pages project "hala-tours", output dir `site/`, no build command) — not yet created

## Outstanding problems
- Orphan Google Maps tabs may remain in shared Chromium from ResearchHala's timed-out tab.run (not closable from its kernel) — orchestrator informed.

## Log
- 05:08 recovery: workspace created from prior raw research; brief + standard written.
- 05:20 ResearchHala: live re-crawl, Google listing + 390 reviews captured, provenance check vs sibling template sites.
- 05:35 partial commit (SOURCE_OF_TRUTH, LEGACY inventory, notes).
- 05:50 research complete: CONTENT + ASSET inventories, BUILD_STATUS updated.
