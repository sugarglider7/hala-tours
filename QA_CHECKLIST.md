# QA_CHECKLIST — hala-tours (phase 3, BuildHala, 2026-10-02)

Tags refer to `SOURCE_OF_TRUTH.md` (S# = Sources table). FR pages carry the same claims as their EN pair (same data record / same keys), so each row covers both languages.

## 1. Global chrome (every page)
| claim | tag | phrasing |
|---|---|---|
| Name "Hala Tours Agadir" | [VERIFIED: S1,S3] | as written |
| "at the Hotel Hamilton", address "Hotel Hamilton, Boulevard Mohammed V, Agadir 80000" | [VERIFIED: S1,S12] | as written |
| Phone/WhatsApp +212 660 732 477 (tel + wa.me/212660732477) | [CONFLICT: S1,S3] → orchestrator decision 1 | ONE constant in `catalogue.json`; owner to confirm vs Google …177 |
| Email halatoursagadir@gmail.com | [VERIFIED: S1] | footer + form fallback; wrapped in `<!--email_off-->` for Cloudflare |
| Hours Mon–Sat 08:00–23:00, Sun 09:00–22:00 + live "open now" | [VERIFIED: S3] | Africa/Casablanca time; Ramadan hours unknown |
| "Prices on request" / no prices anywhere | [STALE] all prices | "Ask for today's price on WhatsApp" |
| Footer "photos by Hala Tours Agadir; place photos credited" | ASSET_INVENTORY + /credits/ | — |

## 2. Home `/` · `/fr/`
| claim | tag | phrasing |
|---|---|---|
| Day trips, activities & transfers from Agadir | [VERIFIED: S1,S2] | eyebrow |
| Pickup from your hotel on almost every trip | [VERIFIED: S1; PROBABLE: S4] | "almost every trip" |
| 5.0 on Google · 390 reviews | [VERIFIED: S3] (count will drift) | no date |
| "Twenty-odd kinds of day. One desk." / 24 days in 7 moods | [VERIFIED: S1] 26 pages − duplicate boat − transfers | — |
| Mood intros (Tifnit dunes, Souss river flamingos, Nile crocodiles, Imouzzer road, Taroudant walls, Tafraout granite) | [VERIFIED: S1] place facts | rewritten |
| Desk notes: combine quads/sandboard/camel; sunset ride; Marrakech out 7 home ~9; Paradise Valley in the morning in summer | [PROBABLE: S4]; [VERIFIED: S1] times | as notes, "ask us" |
| Two-day trips "run on request" | [UNVERIFIED as sold] | "message us for dates" |
| Sketch map: destinations + "our desk" | geography; [VERIFIED: S1] places | caption "places roughly where they are" |
| 3 quotes: Noor, Meem, Mariam Alastall (desktop) — 2 on phones | [VERIFIED: S4] SOT §f 1,3,9 | exact text, "Name · Google review", no dates |
| "Come and talk it through with Ayoub and the team" | [PROBABLE: S4] 130 reviews; tie S1 | first name only, no title (orchestrator decision 4) |
| OSM locator, pin on the hotel | [VERIFIED: S3,S5,S13] | "Map data © OpenStreetMap contributors" |
| "We do airport transfers too" | [VERIFIED: S1] | link to /transfers/ |
| Planner → WhatsApp | [VERIFIED: S1] channel | composed message, no prices |
| Hero photo: riders on a cliff path | own Google "by owner" photo #25 [VERIFIED: S3] | no place caption; guests' consent = owner question |

## 3. All days `/days/` · `/fr/sorties/` and 7 mood pages `/moods/*` · `/fr/envies/*`
| claim | tag | phrasing |
|---|---|---|
| Every row = one record in `days.json` (see §6) | per-day tags | name + one line + length rings |
| "On request" badge on Tafraout, balloon, Zagora, El Borj, Marrakech+Essaouira | [UNVERIFIED as sold] | badge + page block (orchestrator decision 2) |
| Mood-page-only notes: "Calm mornings are the best for anything on the water", "Hammam the day after Marrakech", "Tell us your dates first…" | generic advice | no facts claimed |
| Chapter photos | own photos #13, #11, #24, #9, #5, #15; valleys = place-name stack | no place captions on own photos |

## 4. Other pages
| page | claim | tag | phrasing |
|---|---|---|---|
| Where we go | destinations on the sketch map; "Around Agadir … a short drive from your hotel" | geography; [VERIFIED: S1] (Crocoparc 30 min) | no distances/times printed |
| Visit | "inside the Hotel Hamilton … centre of Agadir" | [VERIFIED: S1,S12] ("0 km to city centre") | — |
| Visit | "Come in through the main entrance … ask at reception" | [PROBABLE: S4] desk at main reception/entrance | advice, not a claim about the exact spot |
| Visit | Airport ~23 km / ~30 min; city bus stop ~200 m | [VERIFIED: S12] | "about/around" |
| Visit | Plus Code CC73+32W | [VERIFIED: S3] | — |
| Visit | "Most people meet Ayoub at the desk … honest answer, incl. which days aren't worth it for small children" | [PROBABLE: S4] (130 reviews, honesty/kids themes) | guest-experience phrasing, no title/bio |
| Visit | Quotes daniel oconnell, Erin Grace-Woodrow, Carly Hughes | [VERIFIED: S4] SOT §f 4,5,7 | exact |
| Visit | "We speak English and French" | [PROBABLE: S4,S1] | as BRAND_NOTES; other languages not claimed |
| Visit | Photo: minibus selfie #29 | own photo | caption "On the way out for the day" |
| Reviews | 5.0 on Google from 390 reviews; 11 quotes (SOT §f 1–7, 9–12) | [VERIFIED: S3,S4] | exact text incl. original spelling ("a absolute", "Paradise city"); FR page notes quotes are in English; quote 8 skipped (typo) |
| Transfers | Agadir airport ↔ hotels; Marrakech, Casablanca, Essaouira airports → Agadir | [VERIFIED: S1] | route list + form options ("Something else" for other routes) |
| Transfers | Priced per vehicle, 1–3 / 4–7 people | [VERIFIED: S1] (prices [STALE]) | no amounts |
| Transfers | "Late arrivals are fine — just ask us first" | [PROBABLE: S4] (2 AM airport run) | softened with "ask us first" |
| Transfers | Quote Zoltán Tóth (vans clean, on time) | [VERIFIED: S4] SOT §f 6 | exact |
| Transfers | Photo: guests by a silver minivan #27 | own Google photo | no vehicle-type claim |
| Plan | "We reply with ideas, times and today's price … we collect you from your hotel on the day" | [VERIFIED: S1] pickup; [PROBABLE: S4] WhatsApp use | — |
| Credits | 8 Commons files: author, licence, source link, "cropped and resized"; OSM ODbL; fonts OFL | file pages checked via Commons API 2026-10-02 (`research/raw/commons/chosen.json`) | — |
| 404 | EN + FR text, links home + WhatsApp | — | self-contained |

## 5. Owner-embarrassment self-test (done; removed/softened)
- Removed: "the Atlantic on your left" (wrong direction), "rods and bait" (bait not stated), "Kids talk about it for the rest of the week", "dates are limited" (balloon), "the desert closest to the coast" (El Borj), "you don't need to be a hotel guest" (unstated policy), "where the river meets the ocean" (cliché + vague), "the port grills fish all day".
- Never stated: prices, payment/cancellation, guide languages per tour, Taghazout/Tamraght pickup, entry fees, vehicle models, team titles, Mustafa or any other name, founding year, Tripadvisor.
- Softened with "around/about/usually/ask us": all times (2022 copy), surf age, Paradise Valley length, Taroudant lunch, Crocoparc hours, Souk El Had days, balloon take-off place.
- Legzira: no arches promised in copy; the only arch shown is the surviving one, photo dated 2018 and captioned. Tifnit: only the beach dunes (still there), never the demolished village.

## 6. Claim tables per day page (EN + FR from the same record in `tools/content/days.json`)
Tag shorthand: times are from the live site's 2022 copy → always "around/about"; place names = [VERIFIED: S1] rewritten in our voice (the legacy prose is copied from other operators and was not reused).

#### /days/quad/ · /fr/sorties/quad/ — Quad biking (legacy id 84)

| claim | tag | phrasing |
|---|---|---|
| Offered by Hala | [PROBABLE: S4] reviews + [VERIFIED: S1] listed | normal |
| Timing: About 90 minutes of riding, plus the drive there and back | [VERIFIED: S1] (2022 copy) | softened (around/about) |
| Pickup: From your hotel in Agadir, and back again | [VERIFIED: S1] | verified |
| Route: We collect you from your hotel and drive south of the city to the quads → A briefing before anyone starts an engine → Tracks through a Berber village and the open country around it → Out onto the dunes by Tifnit beach → Back to th | [VERIFIED: S1] place names | rewritten in our voice |
| Lengths: hours | [VERIFIED: S1] times → our grouping | approximate rings |
| Combine quad + sandboard + camel | [PROBABLE: S4] | softened: 'Ask us — we combine' |
| Photo `quad-dunes` | Hala own photo (ASSET_INVENTORY USE) | no place/person caption |
| Good to know tips | generic common sense | no policies invented |

#### /days/buggy/ · /fr/sorties/buggy/ — Buggy ride (legacy id 85)

| claim | tag | phrasing |
|---|---|---|
| Offered by Hala | [PROBABLE: S4] reviews + [VERIFIED: S1] listed | normal |
| Timing: Morning: out around 08:30, back around 12:00. Afternoon: around 14:00 to 17:30. About 1½ hours of driving. | [VERIFIED: S1] (2022 copy) | softened (around/about) |
| Pickup: From your hotel, about 20 minutes' drive to the buggies | [VERIFIED: S1] | verified |
| Food: Mint tea on the way | [VERIFIED: S1] | verified |
| Route: We pick you up at your hotel; the buggies are about 20 minutes away → Your guide shows you the controls and leads the way → Forest tracks first, then out onto the dunes → A stop for mint tea → Back on the tracks to the base, then  | [VERIFIED: S1] place names | rewritten in our voice |
| Lengths: half | [VERIFIED: S1] times → our grouping | approximate rings |
| Two-seaters suit families with children | [VERIFIED: S1] | 'one adult drives, one child alongside' |
| No photo | — | place-name stack (no borrowed imagery) |
| Good to know tips | generic common sense | no policies invented |

#### /days/sandboarding/ · /fr/sorties/sandboard/ — Sandboarding (legacy id 93)

| claim | tag | phrasing |
|---|---|---|
| Offered by Hala | [PROBABLE: S4] reviews + [VERIFIED: S1] listed | normal |
| Timing: A couple of hours on its own, or half a day combined with quads | [VERIFIED: S1] (2022 copy) | softened (around/about) |
| Route: Tell us whether you want the boards on their own or with quads and a camel → We drive you out to the dunes → Boards on: down the face, back up on foot, again → Back to Agadir and your hotel | [VERIFIED: S1] place names | rewritten in our voice |
| Lengths: hours, half | [VERIFIED: S1] times → our grouping | approximate rings |
| Where/how sandboarding runs | [CONFLICT: S1 copied text (S15) vs S4 (with quads south)] | neutralised: no place/lunch named; 'tell us… we put the afternoon together' |
| Photo `dune-ocean` | Hala own photo (ASSET_INVENTORY USE) | no place/person caption |
| Good to know tips | generic common sense | no policies invented |

#### /days/little-desert/ · /fr/sorties/petit-desert/ — The Little Desert by 4x4 (legacy id 76)

| claim | tag | phrasing |
|---|---|---|
| Offered by Hala | [PROBABLE: S4] reviews + [VERIFIED: S1] listed | normal |
| Timing: Out around 08:30, back around 17:30 | [VERIFIED: S1] (2022 copy) | softened (around/about) |
| Pickup: From your hotel in Agadir | [VERIFIED: S1] | verified |
| Food: Lunch in a Berber family's home | [VERIFIED: S1] | verified |
| Route: Pickup at your hotel around 08:30, then south in the 4x4 → The Souss-Massa national park, along the coast where the birds gather → The dunes, and a short ride on a camel → Lunch in a Berber family's home → Tiznit: the old medina a | [VERIFIED: S1] place names | rewritten in our voice |
| Lengths: full | [VERIFIED: S1] times → our grouping | approximate rings |
| 4x4 vehicle | [PROBABLE: S4] | stated as 'by 4x4' (reviews + owner 4x4 photo #21) |
| Tifnit fishing village | [STALE: S18] | omitted |
| Photo `group-4x4` | Hala own photo (ASSET_INVENTORY USE) | no place/person caption |
| Good to know tips | generic common sense | no policies invented |

#### /days/jet-ski/ · /fr/sorties/jet-ski/ — Jet ski (legacy id 88)

| claim | tag | phrasing |
|---|---|---|
| Offered by Hala | [PROBABLE: S4] reviews + [VERIFIED: S1] listed | normal |
| Timing: 20 minutes, 30 minutes or 1 hour on the water | [VERIFIED: S1] (2022 copy) | softened (around/about) |
| Route: Pick your time on the water: 20, 30 or 60 minutes → Tell us the day and how many of you are riding → Out on Agadir bay → Dry off, done — the rest of the day is yours | [VERIFIED: S1] place names | rewritten in our voice |
| Lengths: hours | [VERIFIED: S1] times → our grouping | approximate rings |
| Photo `jetski-spray` | Hala own photo (ASSET_INVENTORY USE) | no place/person caption |
| Good to know tips | generic common sense | no policies invented |

#### /days/boat-trip/ · /fr/sorties/sortie-en-bateau/ — Boat trip: fish, swim, lunch (legacy id 94)

| claim | tag | phrasing |
|---|---|---|
| Offered by Hala | [PROBABLE: S4] reviews + [VERIFIED: S1] listed | normal |
| Timing: Back at the marina around 14:00 and at your hotel around 14:30 | [VERIFIED: S1] (2022 copy) | softened (around/about) |
| Pickup: From your hotel | [VERIFIED: S1] | verified |
| Food: Fish barbecue with Moroccan salad, on board | [VERIFIED: S1] | verified |
| Included: Fishing gear and drinks on board | [VERIFIED: S1] | verified |
| Route: We take you from your hotel to Agadir marina → Out along the coast → A fishing stop — the gear is on board → A swim stop → Fish grilled on deck, with Moroccan salad → Back at the marina around 14:00, at your hotel around 14:30 | [VERIFIED: S1] place names | rewritten in our voice |
| Lengths: half | [VERIFIED: S1] times → our grouping | approximate rings |
| Duplicate products 94/99 merged | [VERIFIED: S1] | one page |
| Drinks on board | [VERIFIED: S1 id 99 'refreshments'] | verified |
| Photo `marina` | Commons CC BY-SA 4.0 by Abdeaitali — CONTEXT-ONLY place | credited under photo + /credits/; caption ‘the place, not our trip’ |
| Good to know tips | generic common sense | no policies invented |

#### /days/surf/ · /fr/sorties/surf/ — Surf lessons (legacy id 92)

| claim | tag | phrasing |
|---|---|---|
| Offered by Hala | [PROBABLE: S4] reviews + [VERIFIED: S1] listed | normal |
| Pickup: From your hotel in Agadir, included | [VERIFIED: S1] | verified |
| Children: From about 7 years old — ask us | [VERIFIED: S1, stale] | verified |
| Route: Tell us your level and how many of you want a lesson → We collect you from your hotel → A lesson matched to your level → Back to your hotel | [VERIFIED: S1] place names | rewritten in our voice |
| Lengths: half | [VERIFIED: S1] times → our grouping | approximate rings |
| Kids from 7 | [VERIFIED: S1, stale copy] | softened 'from about 7 — ask us' |
| '5 hours of surfing a day' | [STALE/implausible] | omitted; 'ask us when you book' |
| No photo | — | place-name stack (no borrowed imagery) |
| Good to know tips | generic common sense | no policies invented |

#### /days/legzira/ · /fr/sorties/legzira/ — Legzira & Massa, with lunch (legacy id 97)

| claim | tag | phrasing |
|---|---|---|
| Offered by Hala | [PROBABLE: S4] reviews + [VERIFIED: S1] listed | normal |
| Timing: Out around 08:00, back around 18:00 — roughly 300 km there and back | [VERIFIED: S1] (2022 copy) | softened (around/about) |
| Pickup: From your hotel in Agadir | [VERIFIED: S1] | verified |
| Food: Fish lunch by the ocean, included | [VERIFIED: S1] | verified |
| Route: Pickup around 08:00 and south out of Agadir → A stop at the Youssef Ben Tachfine dam → Aglou beach → Free time on Legzira beach, under the red cliffs → Fish lunch by the ocean → Home via Tiznit and the dunes, back around 18:00 | [VERIFIED: S1] place names | rewritten in our voice |
| Lengths: full | [VERIFIED: S1] times → our grouping | approximate rings |
| Main arch collapsed 2016 | [STALE] | no arches promised; photo is the surviving arch dated 2018, captioned so |
| May need more people | [PROBABLE: S4 Hugo Vieira] | desk note 'runs best with a few more people' |
| Photo `legzira` | Commons CC BY-SA 4.0 by Roy Egloff — CONTEXT-ONLY place | credited under photo + /credits/; caption ‘the place, not our trip’ |
| Good to know tips | generic common sense | no policies invented |

#### /days/camel/ · /fr/sorties/balade-a-dos-de-chameau/ — Camel ride by the Souss river (legacy id 95)

| claim | tag | phrasing |
|---|---|---|
| Offered by Hala | [PROBABLE: S4] reviews + [VERIFIED: S1] listed | normal |
| Timing: A few hours, including the drive | [VERIFIED: S1] (2022 copy) | softened (around/about) |
| Pickup: From your hotel to the ranch, and back | [VERIFIED: S1] | verified |
| Route: We drive you from your hotel to the ranch → Up onto your camel, with a guide leading → Through the eucalyptus towards the Souss river → Flamingos in the shallows, and a glimpse of the royal palace → Back to the ranch and to your h | [VERIFIED: S1] place names | rewritten in our voice |
| Lengths: hours | [VERIFIED: S1] times → our grouping | approximate rings |
| Sunset ride | [PROBABLE: S4] | 'Ask for the sunset ride' |
| Photo `camel-sand` | Hala own photo (ASSET_INVENTORY USE) | no place/person caption |
| Good to know tips | generic common sense | no policies invented |

#### /days/camel-bbq/ · /fr/sorties/chameau-et-barbecue/ — Camel ride & barbecue dinner (legacy id 87)

| claim | tag | phrasing |
|---|---|---|
| Offered by Hala | [PROBABLE: S4] reviews + [VERIFIED: S1] listed | normal |
| Timing: About 2 hours on the camel, then dinner | [VERIFIED: S1] (2022 copy) | softened (around/about) |
| Food: Dinner: barbecue, tagine or vegetarian | [VERIFIED: S1] | verified |
| Route: Meet your camel at the base, where the horses live too → About two hours out through the countryside → The mouth of the Souss river, and its flamingos → Back for dinner: barbecue, tagine or vegetarian | [VERIFIED: S1] place names | rewritten in our voice |
| Lengths: hours | [VERIFIED: S1] times → our grouping | approximate rings |
| Photo `camel-sand` | Hala own photo (ASSET_INVENTORY USE) | no place/person caption |
| Good to know tips | generic common sense | no policies invented |

#### /days/horse-riding/ · /fr/sorties/balade-a-cheval/ — Horse riding (legacy id 86)

| claim | tag | phrasing |
|---|---|---|
| Offered by Hala | [PROBABLE: S4] reviews + [VERIFIED: S1] listed | normal |
| Timing: A few hours, including the drive | [VERIFIED: S1] (2022 copy) | softened (around/about) |
| Pickup: From your hotel to the ranch, and back | [VERIFIED: S1] | verified |
| Route: We drive you from your hotel to the ranch → Horses matched to the riders, with a guide → Along the Souss river and past the flamingos → Through the eucalyptus woods and along the royal palace → Back to the ranch and to your hotel | [VERIFIED: S1] place names | rewritten in our voice |
| Lengths: hours | [VERIFIED: S1] times → our grouping | approximate rings |
| Sunset ride | [PROBABLE: S4] | 'Ask about a sunset ride' |
| Hero photo = own Google 'by owner' riders on a cliff path | [VERIFIED: S3 photo] | no place caption |
| Photo `hero-horses` | Hala own photo (ASSET_INVENTORY USE) | no place/person caption |
| Good to know tips | generic common sense | no policies invented |

#### /days/crocoparc/ · /fr/sorties/crocoparc/ — Crocoparc (legacy id 83)

| claim | tag | phrasing |
|---|---|---|
| Offered by Hala | [PROBABLE: S4] reviews + [VERIFIED: S1] listed | normal |
| Timing: Half a day, with about 30 minutes' drive each way | [VERIFIED: S1] (2022 copy) | softened (around/about) |
| Pickup: From your hotel reception, and back | [VERIFIED: S1] | verified |
| Route: We collect you from your hotel reception → About half an hour's drive to the park → Crocodiles, gardens, and time to wander at your own pace → We drive you back to your hotel | [VERIFIED: S1] place names | rewritten in our voice |
| Lengths: half | [VERIFIED: S1] times → our grouping | approximate rings |
| Park hours / '300+ crocodiles' | [STALE] third-party | omitted; 'ask us about opening times' |
| No photo | — | place-name stack (no borrowed imagery) |
| Good to know tips | generic common sense | no policies invented |

#### /days/marrakech/ · /fr/sorties/marrakech/ — Marrakech for the day (legacy id 77)

| claim | tag | phrasing |
|---|---|---|
| Offered by Hala | [PROBABLE: S4] reviews + [VERIFIED: S1] listed | normal |
| Timing: Out around 07:00, in Marrakech around 10:30, home around 21:00 | [VERIFIED: S1] (2022 copy) | softened (around/about) |
| Pickup: From your hotel | [VERIFIED: S1] | verified |
| Food: Lunch stop in a riad — not included, you pay there | [VERIFIED: S1] | verified |
| Route: Pickup around 07:00; in Marrakech around 10:30 → The Bahia Palace and the Koutoubia gardens → The Saadian Tombs → Lunch in a riad (pay on the spot), then time in the souks → Meet at Jemaa el-Fna around 17:30 → Back at your hotel a | [VERIFIED: S1] place names | rewritten in our voice |
| Lengths: full | [VERIFIED: S1] times → our grouping | approximate rings |
| Lunch not included | [VERIFIED: S1] | verified; no amount printed |
| Photo `koutoubia` | Commons CC BY-SA 4.0 by Baca12 — CONTEXT-ONLY place | credited under photo + /credits/; caption ‘the place, not our trip’ |
| Good to know tips | generic common sense | no policies invented |

#### /days/essaouira/ · /fr/sorties/essaouira/ — Essaouira for the day (legacy id 82)

| claim | tag | phrasing |
|---|---|---|
| Offered by Hala | [PROBABLE: S4] reviews + [VERIFIED: S1] listed | normal |
| Pickup: From your hotel | [VERIFIED: S1] | verified |
| Food: Lunch is up to you — grilled fish at the port is the classic | [VERIFIED: S1] | verified |
| Included: A guided walk through the town | [VERIFIED: S1] | verified |
| Route: Pickup at your hotel and north up the coast → Goats in the argan trees, if they're up there that day → A coffee stop in a Berber village → A guided walk: the souk, the Skala ramparts, the port and the market → Free time for lunch  | [VERIFIED: S1] place names | rewritten in our voice |
| Lengths: full | [VERIFIED: S1] times → our grouping | approximate rings |
| 'An hour drive' | [STALE/wrong] | no drive time printed |
| Lunch on your own | [VERIFIED: S1] | verified |
| Photo `essaouira-cannon` | Hala own photo (ASSET_INVENTORY USE) | no place/person caption |
| Good to know tips | generic common sense | no policies invented |

#### /days/agadir-city-tour/ · /fr/sorties/visite-d-agadir/ — Agadir city tour (legacy id 90)

| claim | tag | phrasing |
|---|---|---|
| Offered by Hala | [PROBABLE: S4] reviews + [VERIFIED: S1] listed | normal |
| Timing: About 3 hours, morning or afternoon | [VERIFIED: S1] (2022 copy) | softened (around/about) |
| Pickup: From your hotel | [VERIFIED: S1] | verified |
| Route: Pickup at your hotel → Along the seafront to the Marina → The fishing port → Up to Agadir Oufella for the view over the bay → An argan oil cooperative → An hour of free time in Souk El Had, then back to your hotel | [VERIFIED: S1] place names | rewritten in our voice |
| Lengths: half | [VERIFIED: S1] times → our grouping | approximate rings |
| Souk El Had opening days | general knowledge (closed Mondays) | 'Ask us which days Souk El Had is open' |
| Photo `oufella` | Commons CC BY-SA 4.0 by Abdeaitali — CONTEXT-ONLY place | credited under photo + /credits/; caption ‘the place, not our trip’ |
| Good to know tips | generic common sense | no policies invented |

#### /days/paradise-valley/ · /fr/sorties/vallee-du-paradis/ — Paradise Valley (legacy id 78)

| claim | tag | phrasing |
|---|---|---|
| Offered by Hala | [PROBABLE: S4] reviews + [VERIFIED: S1] listed | normal |
| Pickup: From outside your hotel | [VERIFIED: S1] | verified |
| Route: Pickup outside your hotel → Up the Imouzzer road into the hills → Paradise Valley: the palm-lined gorge and its river → Argan, almond and olive trees along the way → Free time in Imouzzer village → Back down to Agadir | [VERIFIED: S1] place names | rewritten in our voice |
| Lengths: half, full | [VERIFIED: S1] times → our grouping | approximate rings |
| Morning in summer (heat) | [PROBABLE: S4 3★ review] | desk note |
| Half vs full day | [CONFLICT: S1 'day' vs S11 half-day] | both rings + 'ask us' |
| Turquoise pools | [S4: absent in summer] | not promised ('in case the water's up') |
| Photo `paradise` | Commons CC BY-SA 4.0 by Younes GOUSSYRA — CONTEXT-ONLY place | credited under photo + /credits/; caption ‘the place, not our trip’ |
| Good to know tips | generic common sense | no policies invented |

#### /days/taroudant/ · /fr/sorties/taroudant/ — Taroudant & Tiout (legacy id 75)

| claim | tag | phrasing |
|---|---|---|
| Offered by Hala | [PROBABLE: S4] reviews + [VERIFIED: S1] listed | normal |
| Timing: Out around 08:30–09:00, back in the evening | [VERIFIED: S1] (2022 copy) | softened (around/about) |
| Pickup: From your hotel | [VERIFIED: S1] | verified |
| Food: Lunch out there — ask us what's included | [VERIFIED: S1] | verified |
| Route: Pickup around 08:30–09:00 and east up the Souss valley → Taroudant: the ramparts that circle the town → Time in Taroudant's souks → Tiout: the palm grove and the old kasbah — on foot, or by donkey if you like → Home to Agadir by a | [VERIFIED: S1] place names | rewritten in our voice |
| Lengths: full | [VERIFIED: S1] times → our grouping | approximate rings |
| Lunch included? | [VERIFIED: S1 'lunch on site'] unclear if included | 'ask us what's included' |
| Photo `taroudant` | Commons CC BY-SA 3.0 by Bjørn Christian Tørrissen — CONTEXT-ONLY place | credited under photo + /credits/; caption ‘the place, not our trip’ |
| Good to know tips | generic common sense | no policies invented |

#### /days/tafraout/ · /fr/sorties/tafraout/ — Tafraout & Tiznit (legacy id 96)

| claim | tag | phrasing |
|---|---|---|
| Offered by Hala | [VERIFIED: S1] listed; sold [UNVERIFIED] | "On request" badge + block |
| Timing: A full day — out around 07:30 | [VERIFIED: S1] (2022 copy) | softened (around/about) |
| Route: Out of Agadir across the Souss plain → Up into the Ameln valley and its villages under the granite → Tafraout, about 1,000 m up → The painted rocks near Aguerd Oudad → Mint tea, then Tiznit and its silver medina → Home to Agadir | [VERIFIED: S1] place names | rewritten in our voice |
| Lengths: full | [VERIFIED: S1] times → our grouping | approximate rings |
| Still sold | [UNVERIFIED: 0 reviews] | 'On request' badge + block |
| Souk weekday, almond blossom | [UNVERIFIED] | omitted |
| Photo `tafraout` | Commons CC BY-SA 4.0 by Simohnt — CONTEXT-ONLY place | credited under photo + /credits/; caption ‘the place, not our trip’ |
| Good to know tips | generic common sense | no policies invented |

#### /days/hammam/ · /fr/sorties/hammam/ — Hammam & massage (legacy id 100)

| claim | tag | phrasing |
|---|---|---|
| Offered by Hala | [PROBABLE: S4] reviews + [VERIFIED: S1] listed | normal |
| Timing: The hammam, then a 60-minute massage | [VERIFIED: S1] (2022 copy) | softened (around/about) |
| Pickup: From your hotel to the spa in the centre, and back | [VERIFIED: S1] | verified |
| Included: Transport both ways | [VERIFIED: S1] | verified |
| Route: We collect you from your hotel → A traditional hammam: steam and a scrub → A 60-minute massage with argan oil → We drive you back to your hotel | [VERIFIED: S1] place names | rewritten in our voice |
| Lengths: hours | [VERIFIED: S1] times → our grouping | approximate rings |
| Female therapist on request | not stated | phrased 'tell us and we'll ask' (no promise) |
| No photo | — | place-name stack (no borrowed imagery) |
| Good to know tips | generic common sense | no policies invented |

#### /days/berber-evening/ · /fr/sorties/soiree-berbere/ — Berber evening & dinner (legacy id 98)

| claim | tag | phrasing |
|---|---|---|
| Offered by Hala | [PROBABLE: S4] reviews + [VERIFIED: S1] listed | normal |
| Timing: An evening | [VERIFIED: S1] (2022 copy) | softened (around/about) |
| Food: Dinner: pastilla, briouates, couscous, fruit, mint tea and pastries | [VERIFIED: S1] | verified |
| Route: Arrive in the evening and take your place under the tents → Dinner, course after course → Ahwach and Gnaoua music, dancers and acrobats → The fantasia: riders charging in a line and firing together → Mint tea and pastries to finis | [VERIFIED: S1] place names | rewritten in our voice |
| Lengths: hours | [VERIFIED: S1] times → our grouping | approximate rings |
| Sold | [PROBABLE: S4, 1 review] | shown normally |
| Transport | [UNVERIFIED] | 'ask us about getting there and back' |
| No photo | — | place-name stack (no borrowed imagery) |
| Good to know tips | generic common sense | no policies invented |

#### /days/hot-air-balloon/ · /fr/sorties/montgolfiere/ — Hot-air balloon (legacy id 101)

| claim | tag | phrasing |
|---|---|---|
| Offered by Hala | [VERIFIED: S1] listed; sold [UNVERIFIED] | "On request" badge + block |
| Timing: Sunrise — an early start | [VERIFIED: S1] (2022 copy) | softened (around/about) |
| Food: Mint tea before, breakfast after landing | [VERIFIED: S1] | verified |
| Route: Message us with the dates you have → We tell you where it flies from and confirm a morning → Mint tea while the balloon is prepared → The flight over plains and villages at sunrise → Breakfast after landing | [VERIFIED: S1] place names | rewritten in our voice |
| Lengths: half | [VERIFIED: S1] times → our grouping | approximate rings |
| Still sold / take-off location | [UNVERIFIED] | 'On request'; 'we tell you where it flies from' |
| No photo | — | place-name stack (no borrowed imagery) |
| Good to know tips | generic common sense | no policies invented |

#### /days/zagora-desert/ · /fr/sorties/desert-de-zagora/ — Zagora desert, 2 days (legacy id 79)

| claim | tag | phrasing |
|---|---|---|
| Offered by Hala | [VERIFIED: S1] listed; sold [UNVERIFIED] | "On request" badge + block |
| Timing: 2 days, 1 night — back in Agadir on the evening of day 2 | [VERIFIED: S1] (2022 copy) | softened (around/about) |
| Pickup: From your accommodation in Agadir | [VERIFIED: S1] | verified |
| Route: Day 1: Taroudant, then Taliouine and its saffron fields → Taznakht, Agdz and down the Draa valley to Zagora → A camel ride to camp, sunset over the dunes, a night in the desert → Day 2: sunrise on the dunes, breakfast at camp → Ba | [VERIFIED: S1] place names | rewritten in our voice |
| Lengths: two | [VERIFIED: S1] times → our grouping | approximate rings |
| Still sold | [UNVERIFIED] | 'On request'; meals only 'breakfast at camp' (stated, plausible) + 'we'll confirm what's included' |
| Photo `zagora` | Commons CC BY-SA 4.0 by Sylvestre BOCCO — CONTEXT-ONLY place | credited under photo + /credits/; caption ‘the place, not our trip’ |
| Good to know tips | generic common sense | no policies invented |

#### /days/el-borj-desert/ · /fr/sorties/desert-d-el-borj/ — El Borj desert, 2 days (legacy id 81)

| claim | tag | phrasing |
|---|---|---|
| Offered by Hala | [VERIFIED: S1] listed; sold [UNVERIFIED] | "On request" badge + block |
| Timing: 2 days, 1 night — back in Agadir around 18:00 on day 2 | [VERIFIED: S1] (2022 copy) | softened (around/about) |
| Route: Day 1: south to Tiznit → Lunch at Legzira, by the ocean → On to the El Borj dunes for sunset, and a night in tents → Day 2: a camel ride and the rock carvings → Lunch in the Tighmert palm grove, then home, around 18:00 | [VERIFIED: S1] place names | rewritten in our voice |
| Lengths: two | [VERIFIED: S1] times → our grouping | approximate rings |
| Still sold | [UNVERIFIED] | 'On request' |
| No photo | — | place-name stack (no borrowed imagery) |
| Good to know tips | generic common sense | no policies invented |

#### /days/marrakech-essaouira/ · /fr/sorties/marrakech-essaouira/ — Marrakech & Essaouira, 2 days (legacy id 80)

| claim | tag | phrasing |
|---|---|---|
| Offered by Hala | [VERIFIED: S1] listed; sold [UNVERIFIED] | "On request" badge + block |
| Timing: 2 days, 1 night in a hotel — back in Agadir around 18:00 on day 2 | [VERIFIED: S1] (2022 copy) | softened (around/about) |
| Route: Day 1: Marrakech — the palaces and the souks → Jemaa el-Fna in the evening, and a night in a hotel → Day 2: across to Essaouira and its medina → Lunch by the sea → Home to Agadir along the coast road, around 18:00 | [VERIFIED: S1] place names | rewritten in our voice |
| Lengths: two | [VERIFIED: S1] times → our grouping | approximate rings |
| Still sold | [UNVERIFIED] | 'On request'; 'we'll confirm the hotel and what's included' |
| Photo `essaouira-lane` | Hala own photo (ASSET_INVENTORY USE) | no place/person caption |
| Good to know tips | generic common sense | no policies invented |
## 7. Functional checklist (STANDARD §10) — run 2026-10-02 on the local preview (python http.server :8701), one tab
| check | result |
|---|---|
| `check_site.py` | OK (79 pages), 0 ERROR. 2 WARN = "Paradise city trip was out of this world…" — a real Google quote (Stephanie McDougal, SOT §f 12), kept verbatim on /reviews/ + /fr/avis/; "paradise" is her word, not our copy |
| Contact targets | only wa.me/212660732477, tel:+212660732477, mailto:halatoursagadir@gmail.com (the verified/decided constants) |
| Horizontal overflow at 360 px | all 79 pages: scrollWidth = 360, no element past the right edge |
| One h1 per page, title, description, canonical, hreflang en/fr/x-default | all pages (checked programmatically + `/fr/sorties/vallee-du-paradis/`: canonical own URL, alternates both, language switch → `/days/paradise-valley/`) |
| JSON-LD | home + visit: TravelAgency (5.0 / 390 Google — verified figure); day pages: TouristTrip + BreadcrumbList; transfers: Service; lists: ItemList; no prices/offers |
| Console errors / failed requests | none across all 79 pages (pageerror, console.error, requestfailed, HTTP ≥ 400) |
| Menu sheet | aria-expanded true, focus moves to Close, Esc closes, focus returns to the Menu button, link tap closes, Tab trapped |
| Length filter | home: "All day" reveals the hidden 4th row of a mood (little-desert) and every full-day trip; reset shows 21 rows (3 × 7); mood + /days/ pages filter all rows |
| Add to my day | picks persist in localStorage across pages and languages; dock count + "Plan on WhatsApp"; chips on /plan/ removable |
| Planner validation | empty → "Pick a mood, a day, or tell us…"; adults < 1 → error; past date → error; focus to first problem (details opened if needed) |
| Planner message EN | `Hello Hala Tours! I'd like to plan a day.` / `• Kind of day: Salt water` / `• Ideas: Quad biking; Camel ride by the Souss river` / `• Date: Wed, 7 Oct 2026` / `• People: 2 adults, 2 children (ages: 6 & 9)` / `• Staying at: Hôtel Hamilton` / `• Name: Zoé` / `• Notes: Line one⏎Line two & more` / outro — accents, line breaks and `&` intact, no empty/undefined lines |
| Planner message FR | `Bonjour Hala Tours ! J'aimerais organiser une journée.` / `• Envie de : Palmiers, gorges & villages de montagne` / `• Idées : Quad ; Balade à dos de chameau au bord du Souss` / `• Personnes : 2 adultes` / outro |
| Day form FR | `Bonjour Hala Tours ! Je suis intéressé(e) par : Vallée du Paradis.` / `• Date : dim. 4 oct. 2026` / `• Personnes : 1 adulte` / outro; past date blocked |
| Transfer form FR | route + date required; `• Trajet : Aéroport de Marrakech → Agadir` / `• Date : lun. 5 oct. 2026` / `• Heure du vol : 23:40` / `• Vol : AT 410` / `• Personnes : 2` / `• Hôtel : Riad & Spa Agadir` |
| Success state | box gets focus: "Didn't open? Tap here" (same wa.me URL), call link, mailto with the same body |
| Sticky dock vs submit | dock hides while planner / ask form / transfer form / footer is on screen (`data-dock-hide`); verified hidden at the day ask form |
| No-JS fallback | every day page has a plain "Ask about this day on WhatsApp" link; planner has a `<noscript>` WhatsApp link; footer always shows WhatsApp/tel/mail |
| Inputs | ≥ 52 px tall, 17 px text (no iOS zoom), number inputs `inputmode=numeric`, date `min=today` |
| Cloudflare email obfuscation | body wrapped in `<!--email_off-->…<!--/email_off-->` (verified live, see BUILD_STATUS) |

## 8. Performance (390 × 844, cache disabled, before scrolling; uncompressed local server — live is brotli, so HTML is smaller live)
| template | KB transferred | requests | LCP element | CLS |
|---|---|---|---|---|
| Home `/` | 344 (HTML 95) | 7 | hero-horses-m-560.webp (58 KB), 636 ms | 0.001 |
| Home `/fr/` | 347 | 7 | same | 0.002 |
| All days `/days/` | 242 | 6 | lede paragraph | 0 |
| Mood page | 216 | 6 | chapter photo quad-dunes-600.webp (39 KB) | 0 |
| Day page, own photo (quad) | 219 | 6 | dp__img quad-dunes-600.webp (39 KB) | 0 |
| Day page, Commons photo (Paradise Valley) | 226 | 6 | paradise-560.webp (46 KB) | 0 |
| Day page, no photo (hammam) | 157 | 4 | lede paragraph | 0 |
| Where we go | 182 | 5 | lede | 0 |
| Visit | 206 | 5 | h1 | 0 |
| Reviews | 151 | 4 | lede | 0 |
| Transfers | 183 | 5 | transfer-van-560.webp (29 KB) | 0 |
| Plan | 153 | 4 | text | 0 |
| Credits | 384 | 12 | lede (8 small thumbnails) | 0 |
CSS 43 KB, JS 13 KB (deferred), 4 font files (Bricolage latin preloaded). Largest image file: hero-horses-1440.webp 252 KB (desktop only). All `<img>` have width/height + dominant-colour/LQIP background; below-the-fold images lazy; LCP images `fetchpriority=high`, not lazy.
Homepage length at 390: 11.8k CSS px (was 16.9k in phase 2; target "≈11,000").

## 9. Screenshots — `/home/agent/agadir-pilot/qa/hala-tours/p3/`
Round 1 (`r1-*`): home 390/1440, day quad 390/1440, Paradise Valley 390, balloon (on request) 390, mood Salt water 390/1440, all days 390, where 390/1440, visit 390/1440, transfers 390/1440, reviews 390, plan 390, credits 390, FR home 390; `r1b-home-390` after shortening.
Round 2 (`r2-*`): menu open 390, day ask form filled + success 390, planner error + success (filled) 390, 404 390, FR home 390/1440, FR Zagora 1440, FR Legzira 390, all days 1440, FR mood at 360 (+ `r2b-fr-dock-360` after dock fix).
Round 3 (`r3-*`): home 390/1440 final, Marrakech day 390, FR Paradise Valley 1440, 404 1440.
Fixed between rounds: homepage 16.6k → 11.8k px (3 rows per mood, line hidden on phones, 2:1 photos with the desk note hanging off the photo, compact desk, 2–3 quotes, optional planner details), "All 3 days in Two days, one night away" wording, mood-page filter moved under the band, desktop mood tab stretching, FR dock label wrapping at 360, valleys stack note overlap, 404 WhatsApp label.

## Audit A — facts & copy

_Phase 4, AuditFactsHala, 2026-10-02. Scope: `tools/content/{days,catalogue,en,fr}.json`, `tools/images.json`, `tools/build.py` templates, all 79 generated `site/**/*.html` (text, meta, JSON-LD). Rendered spot checks: `/`, `/moods/sand-and-engines/`, `/days/little-desert/`, `/days/crocoparc/` (no photo), `/days/marrakech/`, `/days/hot-air-balloon/` (on request, no photo), `/days/zagora-desert/` (on request), `/visit/`, `/transfers/`, `/reviews/`, `/credits/`, `/fr/`, `/fr/nous-trouver/`, `/fr/sorties/montgolfiere/`, `/fr/transferts/`. Live checked with curl: same copy as the repo (deploy 9f4f269). Copy findings apply at every viewport. Base URL: https://hala-tours.peashoot.io._

**Checked and passing (no action needed):**
- Phone: only +212 660 732 477 / `tel:+212660732477` / `wa.me/212660732477` (470 / 416 / 394 occurrences). The Google variant …177 never appears, and neither does any other number.
- Prices: no €, MAD, DH, dirham or euro figures anywhere, transfers included.
- People: Ayoub is named by first name only, with no title, as "Ayoub and the team". Mustafa, Larcen, Hassan, Jamal and the other names never appear, not even inside quotes.
- Quotes: all 11 match `research/raw/google_reviews_2026-10-02.json` word for word. All 11 reviews were originally written in English (not Google translations). Names appear as Google shows them ("daniel oconnell"), with no dates. The excerpts keep the original meaning.
- Reuse of old-site wording: I compared 7-word sequences across EN and FR against `research/raw/crawl*/` and `products_live.txt`, which includes the copied competitor text. The only matches were the address and phone/email block, "prise en charge à votre hôtel à Agadir", "to the mouth of the Souss river", "at the Youssef Ben Tachfine dam, Aglou beach" and "20 min, 30 min ou une heure". None of the copied paragraphs were reused.
- Out-of-date place facts: the site never mentions the Tifnit fishing or cave village, never promises Legzira arches, gives no Crocoparc opening hours, gives no Essaouira drive time, and does not mention the Tafraout Wednesday souk or almond blossom.
- Commons photos (8 files): author, licence and licence link match `research/raw/commons/chosen.json`. Each is captioned "the place, not our trip" on every page that uses it (10 pages) and listed on `/credits/`. None of them shows a vehicle, guide or group.
- Language claim: "We speak English and French" / "On parle anglais et français", plus `knowsLanguage` en and fr. This matches the SOT.
- Opening hours (Mon–Sat 08:00–23:00, Sun 09:00–22:00) and the address match on every page and in both languages. The EN and FR numbers (times, km, minutes, ages) match for all 24 days.
- Every page has exactly one h1, a correct self-canonical, and en/fr/x-default hreflang pointing to pages that exist. Titles and meta descriptions are unique. STANDARD §3 banned words: none found in EN or FR.

### P1 — must fix

**A1 · P1 · every on-request day page, EN + FR: `/days/hot-air-balloon/`, `/days/tafraout/`, `/days/zagora-desert/`, `/days/el-borj-desert/`, `/days/marrakech-essaouira/` and the `/fr/sorties/…` mirrors**
- **What's wrong:** The "On request" box says "This one doesn't run every week." (FR "Cette sortie ne part pas toutes les semaines."), from `en.json`/`fr.json` `day.request_text`. Directly under it, the CTA says "Check today's price on WhatsApp" (`day.ask_title`), and "Times are usual times — we confirm yours when you book." (`day.times_note`) is printed too.
- **Why it matters:** These five products have no evidence they are still sold. SOT says "UNVERIFIED as currently sold", and orchestrator decision 2 says frame them as "on request — ask us for dates". "Doesn't run every week", "today's price" and "usual times" all tell the reader the trip does run, with a price and a timetable. That is exactly the owner-embarrassment case from the brief ("We don't sell this anymore").
- **Fix:**
  - `request_text` → "We arrange this one on request. Message us with your dates and we'll tell you honestly whether we can do it." / FR "On l'organise sur demande. Écrivez-nous vos dates : on vous dira franchement si c'est possible."
  - When `status == on_request`: set `ask_title` → "Ask us about dates on WhatsApp" / "Demandez-nous les dates sur WhatsApp".
  - When `status == on_request`: hide `times_note`.

**A2 · P1 · footer of all 39 FR pages, e.g. `/fr/`**
- **What's wrong:** "Le comptoir d'excursions de l'hôtel Hamilton, à Agadir." (`fr.json` `footer.line`). In French this means "the Hotel Hamilton's excursion desk", i.e. the hotel's own desk. The EN line says "The local travel desk at the Hotel Hamilton".
- **Why it matters:** It claims Hala is affiliated with, or run by, the hotel. Nothing supports that (SOT §b: "at/inside", not "of"). Both the Hamilton and the owner could object.
- **Fix:** "Le comptoir d'excursions installé à l'hôtel Hamilton, à Agadir." or "Votre comptoir d'excursions à l'hôtel Hamilton, Agadir."

### P2 — should fix

**A3 · P2 · `/visit/`, `/` (#desk), `/fr/nous-trouver/`, `/fr/`, visit meta descriptions**
- **What's wrong:** The site states as fact that the desk is "inside the Hotel Hamilton" (`desk.text`, `visit_page.find[0]`, `visit_page.desc`), and FR "dans l'hôtel Hamilton" / "Nous sommes dans l'hôtel Hamilton".
- **Why it matters:** The business itself only writes "(Hotel Hamilton) Boulevard Mohamed V" (S1). "Inside / main reception" is PROBABLE, from reviews only, and the exact spot is still owner question 3. The brief says "at/around".
- **Fix:** Use "at the Hotel Hamilton" / "à l'hôtel Hamilton" everywhere. Keep the reception hint as soft advice, which is already done well: "Can't see us straight away? Ask at reception."

**A4 · P2 · `/visit/` lede + `/fr/nous-trouver/`**
- **What's wrong:** "A real desk in a real hotel. Walk in, sit down, tell us what you fancy" / "Entrez, asseyez-vous".
- **Why it matters:** Nothing establishes seating, and walk-ins are only PROBABLE (SOT §b "Walk-ins"). The owner may have a counter, not chairs.
- **Fix:** "Come by the desk during opening hours and tell us what you fancy — or message us first and we'll have ideas ready." / "Passez au comptoir aux heures d'ouverture et dites-nous ce qui vous tente — ou écrivez-nous d'abord…"

**A5 · P2 · `/where-we-go/` + `/fr/ou-nous-allons/`**
- **What's wrong:**
  - Tafraout, Zagora, El Borj, Marrakech & Essaouira and the balloon are listed with no "On request" badge (0 badges on the page, versus 5 on `/days/`).
  - The "Further out" intro promises "Day trips and longer trips, with pickup from your hotel." (`where_page.away_text`).
- **Why it matters:**
  - It is the only list of days that drops the on-request framing.
  - Hotel pickup is not stated for El Borj, Marrakech & Essaouira, Tafraout or the balloon.
- **Fix:**
  - Render `u.on_request` in `render_where` `lst()` when `status == on_request`.
  - `away_text` → "Day trips and longer trips — most with pickup from your hotel; the longer ones on request." / FR "…la plupart avec prise en charge à l'hôtel ; les plus longues sur demande."

**A6 · P2 · `/days/sandboarding/` + `/fr/sorties/sandboard/` (also the home and Sand mood rows)**
- **What's wrong:**
  - Timing "A couple of hours on its own, or half a day combined with quads" (`days.json` sandboarding `facts.time`), plus lengths `hours`/`half`.
  - The lede says "Most people do it as part of a bigger afternoon".
- **Why it matters:** No source gives a sandboarding duration. The old page (copied from a Tripadvisor listing) describes a day trip north to Taboga with lunch at Tamri. Two reviews describe a roughly 4-hour quad + sandboard combo in the south. "A couple of hours" and "most people" are invented.
- **Fix:**
  - Drop `facts.time`, or use "Ask us — on its own or as part of a quad afternoon".
  - Lede → "A board, a tall dune and the walk back up. It's at its best as part of a bigger afternoon — quads first, then the boards, sometimes a camel at the end."
  - Lengths: keep `half` only, or let the tip "ask us" cover it.

**A7 · P2 · `/days/hammam/` + `/fr/sorties/hammam/` (including the day page's place-name stack "Black soap")**
- **What's wrong:** The lede says "Steam, a proper scrub, then an hour's massage", step 2 says "A traditional hammam: steam and a scrub", the FR says "un vrai gommage" / "vapeur et gommage", and the place-name stack shows "Black soap / Savon noir".
- **Why it matters:** The source only says "take advantage of the hammam" plus a 60-minute argan massage. A scrub (gommage) or black soap is not stated, and spas often charge extra for it. Promising it is an inclusion claim.
- **Fix:**
  - Lede → "Time in a traditional hammam, then an hour's massage with argan oil."
  - Step → "A traditional hammam."
  - Stack: "Black soap" → "Hammam".
  - Optional tip: "Want a gommage (scrub)? Ask us when you book."

**A8 · P2 · `/days/camel/`, `/days/camel-bbq/`, `/days/horse-riding/`, Animals mood (`moods.hooves.intro`), `/moods/hooves-humps-and-crocodiles/`, FR mirrors**
- **What's wrong:** Flamingos are promised as a certainty: "where flamingos feed in the shallows", "The mouth of the Souss river, and its flamingos", "Flamingos in the shallows".
- **Why it matters:** The Hala source for camel + BBQ (id 87) itself says "If you are lucky, you may see migratory birds (flamingos…)". Flamingos are seasonal, so a guest who sees none has a fair complaint.
- **Fix:** Add a hedge once per page, e.g. "the Souss river, where flamingos often feed in the shallows" / "…et, souvent, ses flamants roses". Keep the step as "The mouth of the Souss river — flamingos, if they're about."

**A9 · P2 · `/days/hot-air-balloon/`, `/moods/go-slow/`, `/fr/sorties/montgolfiere/`, `/fr/envies/au-ralenti/`**
- **What's wrong:**
  - The balloon is labelled "Half a day".
  - The Go slow mood title says "Hammam, Berber evening & sunrise balloon — slow days in Agadir".
- **Why it matters:** The launch site is unknown (SOT notes: "location not stated; photos are Marrakech/other"). The page body honestly says "We tell you where it flies from", but the length label and "in Agadir" claim a local half-day.
- **Fix:**
  - Drop the length, or use a neutral "Ask us" length label.
  - Mood title → "Hammam, Berber evening & a sunrise balloon on request — slow days from Agadir" (FR "…au départ d'Agadir").

**A10 · P2 · all FR pages, e.g. `/fr/` ("Quelle journée vous fait envie ?")**
- **What's wrong:** French high punctuation uses an ordinary breaking space: 175× before "?", 108× before ":", 82× before ";" (FR "!" lines too, e.g. "Passez nous dire bonjour !"). "« Ajouter à ma journée »" has ordinary spaces inside the guillemets. Template strings have no space at all: "Photo: Baca12" and "Utilisée sur:" (8+8×, `build.py` caption and credits rows).
- **Why it matters:**
  - On a 360–390 px phone, "?" or ":" can wrap alone onto the next line. Example: the h1 "Quelle journée vous fait envie ?" at 44 px.
  - The missing spaces are plain French typography errors.
- **Fix:**
  - In `build.py`, post-process FR text nodes: replace `" ([?!;:»])"` with `"\u202f\1"` (and `"\u00a0"` before ":"), and `"« "` with `"«\u202f"`.
  - Make the FR caption/credits strings "Photo : " and "Utilisée sur : " (move them into `fr.json`).

**A11 · P2 · about 27 of 28 FR pages that have images, e.g. `/fr/`, `/fr/sorties/marrakech/`, `/fr/nous-trouver/`**
- **What's wrong:** Every `alt` is in English: "A line of riders on horseback along a cliff-top path above the Atlantic surf", "The Koutoubia minaret rising above palm trees…", "A minibus full of smiling, waving passengers…".
- **Why it matters:** Screen-reader users and image search get English on `lang="fr"` pages, which breaks the "full FR mirror" rule (STANDARD §3).
- **Fix:**
  - Add `alt_fr` to every entry in `tools/images.json`, e.g. "Une file de cavaliers sur un sentier de falaise au-dessus de l'Atlantique". Make `img()` pick the alt by language.
  - While there, change `group-4x4` "and their guide" → "and a man in a blue robe". It isn't established that he is the guide.

**A12 · P2 · `/fr/` (#reviews) and `/fr/avis/` title + description**
- **What's wrong:** "5,0 sur Google, sur 390 avis" and "Avis — 5,0 sur Google, sur 390 avis" (`fr.json` `reviews.title`, `reviews_page.title/desc`).
- **Why it matters:** The doubled "sur… sur" reads like a literal translation.
- **Fix:** "5,0 sur Google · 390 avis" (title: "Avis — 5,0 sur Google (390 avis)"). Desc: "…: 5,0 sur Google pour 390 avis."

**A13 · P2 · JSON-LD on `/`, `/visit/`, `/fr/`, `/fr/nous-trouver/` (`build.py` `org()`)**
- **What's wrong:** The TravelAgency `aggregateRating` (5.0 / 390) is copied from Google Maps reviews.
- **Why it matters:** The figures are verified, but Google's review-snippet rules exclude self-serving LocalBusiness ratings and ratings collected on a third-party platform. That risks a structured-data manual action. The 390 count will also go stale silently.
- **Fix:** Remove `aggregateRating` from `org()`. Keep the visible "5.0 on Google" text, which is fine.

**A14 · P2 · Google listing linked from every page ("Open in Google Maps" / "Read them all on Google")**
- **What's wrong:** The Google listing shows +212 6 60 73 21 77. The site shows …477 (orchestrator decision 1).
- **Why it matters:** A guest who taps through sees two different numbers. This doesn't block the owner meeting, but it is the first thing to settle there.
- **Fix:** Fadwa asks the owner which number is live on WhatsApp. If it is …177, change the one constant `catalogue.json` `contact` and rebuild. If it is …477, the owner should correct the Google listing.

### P3 — polish

**A15 · P3 · day lengths, every guide row + `/fr/organiser/`**
- **What's wrong:** Jet ski (20 min–1 h) is labelled "Couple of hours" / FR "Quelques heures". The FR long label for `hours` is "Deux ou trois heures" (`fr.json` `ui.lengths.hours`), which contradicts both the jet ski and EN "A couple of hours".
- **Fix:** EN "An hour or two" / FR "Une heure ou deux" for `hours`, in both `lengths` and `length_short`.

**A16 · P3 · `/days/legzira/`, `/fr/sorties/legzira/`**
- **What's wrong:** The name is "Legzira & Massa, with lunch", but no step goes to Massa (the old-site title says "Legzira+Massa", but the itinerary is the dam, Aglou, Legzira, Tiznit and the dunes).
- **Fix:** Either rename to "Legzira & Aglou, with lunch" / "Legzira & Aglou, déjeuner compris", or ask the owner where Massa fits.

**A17 · P3 · Legzira photo caption on `/days/legzira/` and `/credits/` (EN + FR)**
- **What's wrong:** "Legzira beach, 2018 — the arch that still stands" uses the present tense for a 2018 photo. Legzira's arches have been collapsing (2016).
- **Fix:** "Legzira beach in 2018, after the big arch fell" / FR "La plage de Legzira en 2018, après la chute de la grande arche".

**A18 · P3 · invented specifics in day records (`days.json`)**
- **What's wrong** (none of these is in any source):
  - Little Desert: "an hour in Tiznit's old walled town" (EN lede).
  - Taroudant: "back in the evening" (facts.time).
  - Horse riding: "Horses matched to the riders" / "Un cheval pour chaque cavalier".
  - Boat trip: "the catch of the day grilled on deck" (the source says fresh fish, not your catch).
  - Marrakech & Essaouira: "Two cities without rushing either", "Jemaa el-Fna at night / le soir" and "Lunch by the sea" (the source says "a seafood meal", Jemaa el-Fna by day).
- **Fix:**
  - Little Desert: "time in Tiznit's old walled town".
  - Taroudant: "Out around 08:30–09:00; ask us the return time".
  - Horse riding: "Horses and a guide" / "Des chevaux et un guide".
  - Boat trip: "fresh fish grilled on deck".
  - Marrakech & Essaouira: "Two cities in two days", "Jemaa el-Fna before the night in a hotel", "A seafood lunch".

**A19 · P3 · `/transfers/` + `/fr/transferts/`**
- **What's wrong:**
  - "Someone waiting when you land" / "Quelqu'un qui vous attend à l'arrivée" (a meet-and-greet promise that isn't stated).
  - "Late arrivals are fine" (a policy; reviews only show a 2 AM run *to* the airport).
  - "one size for 1–3 people, one for 4–7" (vehicle types are UNVERIFIED; the source has price tiers, not sizes).
  - Zoltán Tóth's quote is about the vans on day trips, not transfers.
- **Fix:**
  - Lede → "A lift from the airport to your hotel, and back when it's time to go."
  - Late: "Landing late? Tell us your flight and we'll tell you what's possible."
  - Vehicle: "one rate for 1–3 people, one for 4–7".
  - Swap the quote for Meem's ("transport is included to and from your hotel"), or drop it.

**A20 · P3 · pickup stated as absolute**
- **What's wrong:** `/plan/` "Say yes, and we collect you from your hotel on the day." / FR "on vient vous chercher à l'hôtel le jour J". Jet ski, camel + BBQ, the Berber evening and the balloon have no stated pickup.
- **Fix:** "…and, for most days, we collect you from your hotel."

**A21 · P3 · `/visit/` "Ayoub and the team" + FR**
- **What's wrong:** "Most people meet Ayoub at the desk." / "La plupart des gens rencontrent Ayoub au comptoir." This is a statistic-style claim taken from review counts (130 of 390).
- **Fix:** "At the desk you'll usually find Ayoub." / "Au comptoir, c'est souvent Ayoub qui vous accueille."

**A22 · P3 · street name inconsistency**
- **What's wrong:** The address, map text and JSON-LD say "Boulevard Mohammed V", but the locator alt says "Avenue Mohammed V" (`desk.map_alt`, EN + FR). Hala writes "Boulevard Mohamed V".
- **Fix:** Use "Boulevard Mohammed V" in `map_alt` too.

**A23 · P3 · copy that reads like a template, or odd phrasing**
  - `/days/agadir-city-tour/`: "Your own city in three hours" → "Agadir in three hours". FR "Votre ville en trois heures" → "Agadir en trois heures".
  - Every day page has the kicker "No prices printed — ever" / "Aucun prix affiché — jamais", which sounds defensive in front of the owner → "Prices change with the season" / "Les prix changent selon la saison".
  - FR hero: "on sait sûrement quoi faire" is a literal rendering → "on a sûrement une idée".
  - FR uses filler adjectives: "idéal avec un enfant à côté de vous" (buggy line; it also over-claims) → "pratique avec un enfant à côté de vous". "Parfait le lendemain d'une grosse journée" (hammam) → "Bien pratique le lendemain d'une grosse journée". "Parfait pour une matinée…" (Crocoparc) → "Bien pour une matinée…". "Idéal le premier jour" (city tour) → "À faire dès le premier jour".
  - FR Little Desert step "là où l'oued rejoint l'océan": this cliché was removed from EN in phase 3 → "le long de la côte, là où se posent les oiseaux".

**A24 · P3 · FR time format**
- **What's wrong:** Day copy uses "8 h 30" and the visit description "de 8 h à 23 h", but the hours block and footer render "08:00 – 23:00" (`fr.json` `ui.days_range`).
- **Fix:** FR `days_range` → "8 h – 23 h" / "9 h – 22 h", and format `{open}`/`{close}` the same way.

**A25 · P3 · hygiene**
- **What's wrong:**
  - The h1 on on-request days runs into the badge: the accessible name reads "Hot-air balloonOn request" (`<h1>Hot-air balloon<span class="badge">`).
  - TouristTrip `touristType` holds the mood name ("Sand & engines"), which is not an audience type.
  - 67 of 79 titles are over 70 characters with the " | Hala Tours Agadir" suffix, e.g. FR Vallée du Paradis at 98, so they get cut off in search results.
- **Fix:**
  - Add a space or visually hidden separator before the badge (`' <span…'`).
  - Remove `touristType`.
  - Drop the suffix on day and mood titles, which already say "from Agadir".

**A26 · P3 · gaps against the brief**
- **What's wrong:**
  - The brief lists "minibuses/buses/transport". The site only offers airport transfers.
  - Day combinations reviewers booked are missing: Taghazout + Paradise Valley, and Paradise Valley + Timlaline dunes (SOT: PROBABLE, "ask us / we combine"). They do not appear, although the brief says "do not accidentally omit it".
- **Fix:**
  - On `/transfers/` add: "Need a minibus for a group, or a ride somewhere else? Ask us." / FR "Un minibus pour un groupe, ou un autre trajet ? Demandez-nous."
  - Paradise Valley tip: "Ask about combining it with Taghazout or the Timlaline dunes." / FR "Demandez-nous pour la combiner avec Taghazout ou les dunes de Timlaline."
