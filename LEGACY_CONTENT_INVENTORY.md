# LEGACY CONTENT INVENTORY — halatoursagadir.com

_Live crawl 2026-10-02 (108 URLs + 2 manual) → `research/raw/crawl2/index.json` (URL → saved file). The crashed run's `research/raw/crawl/*.html` (unnamed hashes) are mostly the same pages; its many identical 19,715-byte / 16,034-byte files are **empty product-template probes** (ids with no product), its 10,588 / 11,149-byte files are the empty junk categories, 12,440 / 11,933-byte files are the broken apostrophe URLs below._

Platform: Maroc Annuaire multi-tenant PHP template (tenant slug `agadirridertours`), Bootstrap + Revolution slider, © 2022. Languages: FR at root, EN under `/en/`; Arabic flag → 404. No robots.txt, no sitemap.xml, no canonical/hreflang, every `<title>` = "HALA TOURS Agadir", `<html lang="zxx">`.

Classification key: **VERIFIED/PRESERVE** · **POSSIBLY STALE/VERIFY** · **DUPLICATE/CONSOLIDATE** · **BROKEN** · **TEMPLATE GARBAGE** · **UNCERTAIN**.

## 1. Global elements (every page)
| Element | Content | Class | New-site mapping |
|---|---|---|---|
| Top bar / footer phone | +212 660 732 477 | UNCERTAIN (conflicts with Google …177) | single config constant after owner check |
| Emails | halatoursagadir@gmail.com (all); contact@halatoursagadir.com (FR footer only) | VERIFIED/PRESERVE (gmail primary) | Contact, footer |
| Address | "(Hotel Hamilton) Boulevard Mohamed V Agadir, 80000, Maroc" | VERIFIED/PRESERVE | Visit Hala, footer, JSON-LD |
| Tagline | "agence de tourisme basée à Agadir, spécialisée dans les Excursions et Tours depuis Agadir" | VERIFIED/PRESERVE (rewrite) | About, meta description |
| Nav | Accueil · Qui somme nous · Nos Services (Circuits, Excursions, Activités, Transfert) · Galerie · Contact | DUPLICATE/CONSOLIDATE (EN labels "Tours" for both circuits and the category title) | new IA |
| Social icons | Facebook → personal profile elmouden.ayoub; Instagram → ayoub_el_mouden; Tripadvisor → tripadvisor.fr home; YouTube → youtube.com home | TEMPLATE GARBAGE (TA/YouTube placeholders); personal links UNCERTAIN (consent) | omit unless owner provides business accounts |
| WhatsApp float | api.whatsapp.com/send?phone=212660732477 | UNCERTAIN (number) | wa.me CTA |
| "Réalisé par : Maroc Annuaire" + marocannuaire favicon | agency credit | TEMPLATE GARBAGE | drop |
| Language switch | fr / en / al(→404) | BROKEN (al) | EN root + /fr/ |

## 2. Pages
| URL (FR · EN) | What it contains | Class | Maps to / SEO keywords |
|---|---|---|---|
| `/` = `/index.php` · `/en/` = `/en/index.php` (exact duplicates) | Slider (Agadir cable car, Essaouira, Marrakech Menara stock banners; "S'inscrire" buttons → inscription.php), welcome blurb, 4 featured products (Petit Désert, Paradise Valley, Marrakech, Camel ride), hidden education counters "7096 ÉTUDIANTS ACTIFS / 508 COURS EN LIGNE / 167 ANNÉE D'HISTOIRE / 70" | DUPLICATE (index/root); slider buttons + counters TEMPLATE GARBAGE; featured products POSSIBLY STALE | Home ("excursions Agadir", "tours from Agadir", "activités Agadir") |
| `/about.php` · `/en/about.php` | "QUI SOMME NOUS": agency based in Agadir, excursions & circuits from Agadir "en 4x4"; generic 2 sentences | VERIFIED/PRESERVE (facts only) | About / Visit Hala |
| `/contact.php` · `/en/contact.php` | GSM, email, address, contact form (nom, email, tel, objet, message → mails halatoursagadir@gmail.com). EN h1 still "Nous contacter". No map, no hours | VERIFIED (email/address) · UNCERTAIN (phone) | Contact + Visit Hala (add hours from Google, map, WhatsApp form) |
| `/galerie.php` · `/en/galerie.php` | 23 photos: 3 numbered + 20 WhatsApp images 2022-11-30 (staff/guests selfies, jet ski, quad, Essaouira, coast, group by 4x4) | VERIFIED/PRESERVE (first-party; consent check) | Gallery strip / About / product heroes |
| `/inscription.php` · `/en/inscription.php` | "Pré-inscription" education form: Nom, Prénom, **date de naissance, nationalité, "Formation"** select listing the products | TEMPLATE GARBAGE | replace by WhatsApp inquiry form |
| `/p.php?c=circuits` · `/en/p.php?c=circuits` | List: Legzira+Massa, El Borj (title missing in list), Essaouira & Marrakech 2 j, Zagora 2 j | POSSIBLY STALE/VERIFY | Multi-day ("circuit désert Agadir", "Zagora 2 jours", "désert El Borj") |
| `/p.php?c=excursions` · `/en/…` | Tafraout Tiznit, Balade en bateau, Essaouira, Paradise Valley, Marrakech, Petit Désert, Taroudant & Tiout | POSSIBLY STALE/VERIFY | Day trips ("excursion Essaouira depuis Agadir", "Paradise Valley Agadir", "Marrakech day trip from Agadir") |
| `/p.php?c=activites` · `/en/…` | 14 activities (see §3) | POSSIBLY STALE/VERIFY | Activities ("quad Agadir", "balade chameau Agadir", "buggy Agadir", "jet ski Agadir") |
| `/p.php?c=transfert` · `/en/…` | 1 item → Transfer page | POSSIBLY STALE | Transfers ("transfert aéroport Agadir") |
| `/p.php?c=bachelor`, `c=masters-europeen`, `c=le-mba-europeen`, `/en/p.php?c=licence-professionnelle`, `c=master-specialise`, `c=le-mba-europeen`, `p.php?c=` | Empty category shells from an education template (linked in hidden nav) | TEMPLATE GARBAGE | drop (404/redirect home) |
| `/al/`, `/al/index.php` | 404 | BROKEN | — |
| `/robots.txt`, `/sitemap.xml` | 404 | BROKEN/missing | new robots + sitemap |
| `de_sv.php?n=Excursion dans le désert d` (FR El Borj) · `n=Tour d` (FR city tour) and EN equivalents · `de_sv.php?n=&i=&p=&c=` | Links truncated at the apostrophe → empty page | BROKEN (correct URLs with %27 work) | — |

## 3. Product pages (`de_sv.php?…&i=<id>&p=agadirridertours&c=<cat>`; FR at root, EN under /en/; each EN page reachable under 2 `n=` values = DUPLICATE URLs)
All: price [STALE]; copy COPIED/TEMPLATE (rewrite, never reuse verbatim); main photo mostly shared/stock (see ASSET_INVENTORY). "Réservation/Booking" button → contact.php (a commented-out button points to agadirbesttours.com).

| id | FR title · EN title | Class | New-site mapping / keywords |
|---|---|---|---|
| 97 | Legzira+Massa Avec repas · Legzira+Massa lunch included | POSSIBLY STALE/VERIFY (reviews: sold; "arches" stale; filed under Circuits though a day trip) | Day trip "Legzira beach day trip from Agadir" |
| 81 | Excursion dans le désert d'El Borj… – 2 jours · El Borj Desert Tour from Agadir – 2 Days | UNCERTAIN (0 reviews) | Multi-day, only if confirmed |
| 80 | Essaouira & Marrakech – 2 Jours · – 2 Days | UNCERTAIN (0 reviews) | Multi-day, only if confirmed |
| 79 | Circuit dans le désert de Zagora 2 jours · Zagora desert tour 2 days (EN slug still French) | UNCERTAIN (0 reviews) | Multi-day "Zagora desert 2 days from Agadir" |
| 96 | Excursion Tafraout Tiznit (same FR/EN) | UNCERTAIN (0 reviews) | Day trip "Tafraout day trip" |
| 94 | Balade en bateau à Agadir · Boat trip in Agadir | DUPLICATE/CONSOLIDATE with 99 (price conflict) | one "Boat trip: fishing, swim & fish BBQ" |
| 99 | Excursion Bateau Agadir · Agadir Boat Trip | DUPLICATE/CONSOLIDATE with 94 | → merge |
| 82 | Excursion à Essaouira · excursion to Essaouira | POSSIBLY STALE/VERIFY (sold; "an hour drive" wrong) | Day trip "Essaouira day trip from Agadir" |
| 78 | Excursion à vallée du Paradis · Paradise Valley Excursion From Agadir | POSSIBLY STALE/VERIFY (sold, top) | Day trip "Paradise Valley Agadir" |
| 77 | Excursion à Marrakech · Excursion to Marrakech | POSSIBLY STALE/VERIFY (sold) | Day trip "Marrakech day trip from Agadir" |
| 76 | Agadir Excursion au Petit Désert · …to the Petit Desert | POSSIBLY STALE/VERIFY (sold; Tifnit village part stale; copied text) | Day trip "mini Sahara / petit désert Agadir 4x4" |
| 75 | Excursion Taroudant et Tiout · …Taroudant and Tiout | POSSIBLY STALE/VERIFY (sold) | Day trip "Taroudant Tiout" |
| 101 | Montgolfière · Hot-air balloon | UNCERTAIN (0 reviews, location unstated) | only if confirmed |
| 100 | Hammam & massage | POSSIBLY STALE/VERIFY (sold) | Activity "hammam Agadir" |
| 98 | Soirée berbère & Dîner · Berber evening & Dinner | POSSIBLY STALE/VERIFY | Evening "fantasia dinner show Agadir" |
| 95 | Balade à dos de chameau à Agadir · Camel ride in Agadir | VERIFIED-by-reviews/PRESERVE (rewrite) | Activity "camel ride Agadir Souss river sunset" |
| 93 | Sandboarding à Agadir · Sandboarding in Agadir | UNCERTAIN (text copied from another operator's Tamri trip; reviews describe sandboarding with quad in the south) | Activity, wording to confirm |
| 92 | Cours de surf à Agadir · Surf lessons in Agadir | POSSIBLY STALE/VERIFY | Activity "surf lessons Agadir" |
| 90 | Tour d'Agadir · Agadir city tour | POSSIBLY STALE/VERIFY (FR list link BROKEN) | Activity "Agadir city tour Oufella" |
| 88 | Jet-ski à Agadir · Jetski in Agadir | VERIFIED-by-reviews + own photos/PRESERVE | Activity "jet ski Agadir" |
| 87 | Balade à dos de chameau et barbecue · Camel ride and barbecue | VERIFIED-by-reviews/PRESERVE | Activity "camel ride BBQ Agadir" |
| 86 | Balade à cheval · Horse Riding Agadir | VERIFIED-by-reviews/PRESERVE | Activity "horse riding Agadir" |
| 85 | Ballade en Buggy à Agadir · Buggy ride in Agadir | VERIFIED-by-reviews/PRESERVE (FR typo "Ballade") | Activity "buggy Agadir" |
| 84 | Agadir Quad Tours · Agadir Quad Biking | VERIFIED-by-reviews/PRESERVE (no.1 product) | Activity "quad Agadir dunes" |
| 83 | Excursion Crocoparc · Crocopark Excursion | POSSIBLY STALE/VERIFY (park hours 3rd party) | Activity/family "Crocoparc Agadir" |
| 89 | Transfert · Transfer (table in MAD) | POSSIBLY STALE/VERIFY (routes keep; prices stale) | Transfers page "Agadir airport transfer", "Marrakech airport to Agadir" |

## 4. Useful legacy SEO URLs (for redirects if the domain is ever moved)
Keep a 301 map from: `/p.php?c=excursions|activites|circuits|transfert` (+ `/en/` versions), `/contact.php`, `/about.php`, `/galerie.php` and each `de_sv.php?…&i=<id>` (match on `i`, ignore `n`) to the new page of the same product. (Peashoot build lives on hala-tours.peashoot.io, so this is advisory only.)

## 5. Summary
Preserve: business name, Hamilton/Bd Mohammed V location, gmail, the breadth of the catalogue (as facts, rewritten), first-party gallery photos. Verify: phone, every product's current availability, all prices (show none), multi-day tours, balloon. Drop: education-template remnants, placeholder socials, Maroc Annuaire credit, shared/stock product photos as "ours", copied product prose, duplicate URLs, broken `/al/`.
