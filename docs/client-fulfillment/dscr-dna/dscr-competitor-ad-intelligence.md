---
title: DSCR Competitor Ad Intelligence (Meta Ad Library)
domain: client-fulfillment
owner: media-buying-lead
status: draft
last_updated: 2026-06-02
review_cycle: monthly
artifact_type: intelligence
---

# DSCR Competitor Ad Intelligence (Meta Ad Library)

> **DRAFT — market research.** Snapshot of the live DSCR ad landscape on Meta, scraped from the
> Meta Ad Library on **2026-06-02** via Apify (`apify/facebook-ads-scraper`). Purpose: see which
> competitor ads are *clearly working*, name the bottlenecks in the category, and turn that into a
> DSCR creative edge. Read alongside the [GTM & Positioning Brief](dscr-gtm-positioning-brief.md)
> and the [Ad Copy & Angle Library (DSCR)](ad-copy-angle-library-dscr.md). Evidence file:
> [`_research/dscr-meta-ads-2026-06-02.json`](_research/dscr-meta-ads-2026-06-02.json).

## Purpose

Reverse-engineer what's working in competitor DSCR ads on Meta and convert the gaps into a
differentiated creative plan for the Waiz DSCR launch.

## Scope

US, Meta Ad Library, keyword `DSCR`, `ad_type=all` (commercial), images + video + carousel + DCO.
291 unique ads analyzed (**200 active**, **91 inactive**). Not a census — a representative pull;
refresh monthly.

## Method (so it's reproducible)

- **Tool:** Apify actor `apify/facebook-ads-scraper` (10.8M runs), fed Meta Ad Library *search URLs*.
- **Why not the "official API" actors:** Meta's Ad Library **API only returns political/issue ads** for
  the US, and unauthenticated web-scraper fallbacks get **403-challenged**. The working path is an actor
  that reads the Ad Library web app's internal GraphQL via a search URL.
- **Search URL pattern:**
  `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=DSCR&search_type=keyword_unordered&media_type=all`
- **"Working" proxy = longevity.** Advertisers kill losers fast and keep winners. Days-running (start
  date → today for active; start → end for inactive) is the strongest public signal of a converting ad.

## Headline Findings

### 1. The category churns hard — most ads die in ~2 weeks

| Cohort | Median lifespan | Mean | Max |
|--------|-----------------|------|-----|
| **Active** ads | 66 days | 100 days | 856 days |
| **Inactive** ads | 2 days | 22 days | 171 days |

**76% of inactive ads were dead within 14 days.** The space has a brutal hook bottleneck: the
overwhelming majority of DSCR creatives fail fast. A small set of durable winners (200–850+ days)
carries each advertiser. → *Survivorship bias warning: don't copy the visible winners without
remembering the 76% graveyard you can't see.*

### 2. A few committed advertisers own the space

By total active-days (commitment = it's working):

| Advertiser | Active ads | Total active-day-units | Read |
|------------|-----------|------------------------|------|
| **DSCR Loan Team** | 13 | 2,807 | The replicable model — human/brand-led, long runners |
| **The DSCR Lender** | 23 | 1,230 | Volume player; cash-out refi angle |
| The Mortgage Calculator | 1 | 856 | Aggregator DCO/catalog ad |
| Torus Capital | 4 | 854 | Carousel, "no monthly payments / high leverage" |
| Black Label Capital | 1 | 845 | Hard-money carousel, 2+ years running |
| The Lending Market | 5 | 723 | — |

~38% of active ads are **DCO/catalog** (`{{product.brand}}` templated, big aggregators like The
Mortgage Calculator / Longleaf). Those are hard for a single LO/brand to replicate. **The replicable
winners are the human/brand-led ones** (DSCR Loan Team, Torus, Gwen Wachowski, Truehold video).

### 3. Format & CTA mix (active)

- **Format:** DCO 77 · Image 75 · Video 28 · Carousel 19 · Text 1. Video is *under-represented* (14%)
  yet several video ads are long-runners → underexploited.
- **CTA:** "Get quote" 75 · "Learn more" 51 · "Apply now" 32. The category leans on **high-friction
  asks** (quote/apply). Low-friction "see if you qualify" framing is rare.
- **Landing:** `fb.me` instant lead forms (68) dominate, then advertiser quote pages
  (`thedscrlender.com` 23, `go.dscrloanteam.com` 13). On-platform instant forms are the norm.

### 4. Angle frequency — the category has collapsed to one claim

| Angle | # of 200 active ads |
|-------|---------------------|
| Fast / close quickly | 69 |
| **No income / no tax returns** | 61 |
| Portfolio / scale | 48 |
| Cash-out / equity | 39 |
| Rental income qualifies | 31 |
| LTV / leverage figure (e.g. "85% LTV") | 29 |
| Rate / low rate | 21 |
| Foreign national | 19 |
| **Hard-money / bridge / balloon** | 16 |
| STR / Airbnb | 8 |
| LLC / entity | 6 |

Everyone is shouting the same two things — **"no income / no tax returns"** and **"fast."** It's a
sea of sameness.

## What "clearly working" looks like (proven winners, verbatim)

- **DSCR Loan Team** (245d, image) — *"Why let your personal income hold you back? DSCR loans make it
  easy to fund investment properties based on rental income—not pay stubs or tax returns. ✅ No income
  verification ✅ Close fast ✅ Up to 85% LTV ... Stop waiting on banks to say 'yes.'"* Reframe + clean
  feature stack + soft "no credit impact."
- **The DSCR Lender** (cash-out, image) — *"[Real Estate Investors] Sitting on equity but not using it?
  ... A DSCR cash-out refinance lets you pull equity from your property based on its cash flow — not
  your personal income ... You keep the asset. You unlock the capital."* The strongest **loss-aversion**
  framing in the set, and **refinance-led**.
- **Torus Capital** (279d, carousel) — *"Don't let financing slow you down ... high leverage, no
  monthly payments (on select programs), nationwide ... Ready to scale your deals?"*
- **Gwen Wachowski** (332d, image) — quotes specific rates ("as low as 7.5% / 7.875% APR") — a
  number-heavy approach you **can't and shouldn't** copy (compliance).

## Bottlenecks in the category (the openings) — marketing-psychology lens

1. **Sea of sameness → no differentiation (First Principles / Contrast Effect).** ~60% of ads make the
   identical "no income / no tax returns" claim. When everyone says the same thing, nobody is heard.
   The category is differentiated only by *who shouts the feature list*, not by idea. **Opening:** lead
   with the reframe — **"the property qualifies itself"** — *then* name DSCR, so the idea (not the
   feature) is the hook.
2. **Feature-listing, not Jobs-to-be-Done.** Most ads are spec stacks ("✅ 85% LTV ✅ no W-2 ✅ fast").
   They sell the drill, not the hole. Investors don't want "85% LTV" — they want to *stop being told no
   by a bank looking at the wrong number* and *free trapped equity*. **Opening:** write to the job/outcome.
3. **The 76%-die-in-2-weeks hook problem (Pattern Interrupt / Peak-End).** Weak, undifferentiated hooks
   = fast death. **Opening:** invest in a few strong, idea-led hooks and **more concepts, not recolors**
   (Andromeda) — winners reveal the next batch.
4. **Almost no proof (Social Proof / Availability Heuristic).** The set is nearly devoid of funded
   examples, testimonials, or "investors like you do this all the time." **Opening:** proof-led creative
   (a real exit/cash-out story) is wide open and high-trust.
5. **High-friction asks (Activation Energy / Foot-in-the-Door).** "Get quote / Apply now" everywhere —
   a big first step. **Opening:** a low-friction step ("See if your property qualifies — 60 seconds, no
   credit pull") lowers activation energy and earns the micro-commitment first.
6. **Refinance + cash-out + urgency are under-served (Loss Aversion / Scarcity).** Cash-out/equity is
   only 39/200, hard-money/balloon just 16/200, STR 8/200 — yet these map directly to your beachhead
   (#1 Self-Employed/Write-Off, #2 Hard-Money) and carry the strongest emotional drivers: *trapped
   equity is dead money* (loss aversion) and *the balloon doesn't wait* (urgency). The field is loud on
   **purchase** and quiet on **refinance pain**. This is your lane — and it's where your compliance
   posture (refinance-only) is an advantage, not a constraint.
7. **Number-dependence (your compliance edge).** Several winners lean on figures ("85% LTV", "7.5%").
   Waiz copy is **number-free** by policy. The top *human* winner (DSCR Loan Team) succeeds largely on
   outcome framing → **you are not disadvantaged**; reframe + proof beats spec-listing.

## How we make it better (DSCR launch implications)

1. **Idea-first hook, every ad:** open with the reframe ("Your tax returns say you're broke. Your
   rentals say otherwise."), then name DSCR. Differentiate on *idea*, not feature list.
2. **Own the refinance/cash-out/urgency lanes** the field under-serves — straight to beachhead #1 + #2.
   Lead with *trapped equity / dead money* (loss aversion) and *balloon coming due* (urgency).
3. **Proof-led concepts** (compliant funded examples / investor stories) — the biggest unworked angle.
4. **Lower the first step:** "See if your property qualifies" (soft, no-credit) before "Get a quote."
5. **Lean into video + creator/UGC** — under-used (14%) and several long-runners; cheaper differentiation
   than another static feature card.
6. **Stay number-free and win on reframe + proof** — it's a feature, not a handicap, vs. the LTV/rate crowd.
7. **Plan for the graveyard:** expect ~3 in 4 creatives to die fast; budget for concept volume and judge
   on refi-ready CPL → booked → showed (per [KPI scorecard](dscr-kpi-and-test-scorecard.md)), not CTR.

## Limitations

- Longevity ≈ "working" but isn't conversion data; Meta hides impressions/spend for commercial ads.
- Keyword `DSCR` only (one pull); brand-name and adjacent terms ("rental loan," "investor loan,"
  "no-doc mortgage") not yet captured. Single snapshot — trends need repeat pulls.
- DCO/catalog template bodies (`{{product.brand}}`) carry no readable copy and are excluded from angle text.

## Next pulls (to deepen)

- Adjacent keywords: `no income mortgage`, `rental property loan`, `investor loan no tax returns`, `hard money refinance`.
- Per-advertiser deep dives on DSCR Loan Team + The DSCR Lender (full creative libraries via page URL).
- Re-run monthly; track which winners persist (durable = truly converting) vs. churn.

## Related Docs

- [DSCR GTM And Positioning Brief](dscr-gtm-positioning-brief.md)
- [Ad Copy And Angle Library (DSCR)](ad-copy-angle-library-dscr.md)
- [MB DSCR Ad Copy Standards](mb-dscr-ad-copy-standards.md)
- [DSCR Ads Playbook](dscr-ads-playbook.md)
- [DSCR KPI And Test Scorecard](dscr-kpi-and-test-scorecard.md)
- Evidence: [`_research/dscr-meta-ads-2026-06-02.json`](_research/dscr-meta-ads-2026-06-02.json)
