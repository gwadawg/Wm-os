---
title: RM Quiz Funnel V2 Blueprint
domain: client-fulfillment
owner: media-buying-lead
status: draft
last_updated: 2026-06-24
review_cycle: monthly
artifact_type: blueprint
supersedes: null
companion: rm-funnel-form-spec.md
---

# RM Quiz Funnel V2 — Blueprint

> **Purpose:** Redesign the reverse-mortgage lead funnel as a **qualification quiz** that preserves
> Waiz qualify-first doctrine, `form_intent` nurture routing, and speed-to-lead thank-you cadence —
> while applying quiz-funnel psychology (progress, categories, scoring tiers, personalized insight)
> to lift completion and lead quality from cold Meta traffic.
>
> **Template rule:** Client-agnostic. Use `{placeholders}` from
> [RM Funnel Form Spec](rm-funnel-form-spec.md). Do not embed live client copy in this blueprint.

## Funnel overview

| Field | Value |
|-------|-------|
| **Audience** | Homeowners 62+ (or approaching), primary residence, equity-rich, cold/warm Meta |
| **Goal** | Qualify for LO/SDR conversation; tag `form_intent` + `fit_tier` for downstream nurture |
| **Traffic temperature** | Cold default (8–11 quiz steps); warm retargeting may add 1–2 education steps |
| **Routing tiers** | `qualified` · `nurture` · `not_a_fit` |
| **Platform** | Perspective (quiz UI) → GHL → existing SMS/iMessage/SDR stack |
| **Naming (external)** | *Retirement Equity Assessment* or *Home Equity Readiness Check* — avoid leading with "reverse mortgage" on landing |

**Relationship to V1:** [RM Funnel Form Spec](rm-funnel-form-spec.md) remains the shipped baseline.
This doc is the **V2 target architecture** for net-new builds and template upgrades.

---

## Part 1 — Audit of current funnel (quiz-funnel scorecard)

Audited against the 10-criterion checklist (0–2 each; **10 = perfect**).

| # | Criterion | Score | Current state | Gap |
|---|-----------|-------|---------------|-----|
| 1 | Hook targets real desire + specific promise | **2** | Strong outcome-first hero; equity + no monthly payment | Keep; move hook to **landing-only** (not combined with Q1) |
| 2 | Single CTA, mobile-first, time expectation | **1** | "60 seconds" on subhead; lander doubles as Q1 | Split landing CTA from quiz; show *~3 minutes · 10 questions* |
| 3 | Questions qualify without interrogation feel | **1** | Logical qualifiers but free numeric fields feel like forms | Use **range chips** + progress bar + category labels |
| 4 | Fit scoring + weighted routing defined | **0** | No `fit_tier`; only implicit age/state DQ | Add scored tiers → thank-you variants + GHL tags |
| 5 | 8–15 questions, categories, progress shown | **1** | ~9 steps, no visible progress or grouping | 10 questions in 3 categories + progress UI |
| 6 | Opt-in immediately post-quiz | **2** | Opt-in follows last question | Keep; improve bridge copy |
| 7 | Minimum fields, privacy, quiz→form bridge | **1** | Fields OK; headline weak vs quiz payoff | Bridge: *"Where should we send your personalized assessment?"* |
| 8 | Thank-you personalized insight | **0** | Same page for everyone; no answer callbacks | Tier + `form_intent` dynamic insight block |
| 9 | Expectations: timeframe + channel | **2** | 15-minute call promise is excellent | Keep for **qualified**; soften for nurture/not-fit |
| 10 | Trust elements; no hard sales CTA on TY | **1** | Strong FAQ/timeline; repeat *Start Valuation* CTAs | Remove hard re-entry CTAs; **Save Our Number** + soft links only |

**Current score: 6 / 10**

**Path to 10/10:** Implement sections below — unified landing, categorized quiz with scoring, tier-routed thank-you, quiz-native UX, design system applied in Perspective.

---

## Part 2 — Stage architecture (4-stage quiz funnel)

```
Landing ──start──→ Quiz (3 categories) ──score──→ Opt-in ──tier──→ Thank You (3 variants)
                         │                      │                    │
                         ├─ form_intent         ├─ lead + tags       ├─ qualified → 15-min call TY
                         ├─ fit_score           └─ fit_tier          ├─ nurture → resource TY
                         └─ equity_band                              └─ not_a_fit → honest exit TY
```

Post-thank-you **unchanged** from V1: GHL ingest → SMS +5m → intent drip → AI bot → SDR (tier-dependent). See [RM Funnel Form Spec § Post-submit journey](rm-funnel-form-spec.md).

---

## Part 3 — Stage 1: Landing page

**Job:** One action — start the quiz. No questions on this screen.

### Hook–Story–Offer

| Element | Copy pattern |
|---------|--------------|
| **Hook** (readiness + moving-toward) | Could Your Home Equity Help You Live More Comfortably in Retirement? |
| **Story** (2 sentences) | Many homeowners your age are sitting on significant equity — but aren't sure what options actually fit their situation. This short assessment helps you see where you stand — without a credit pull or obligation. |
| **Offer** | Answer **10 quick questions** → get a personalized **Retirement Equity Assessment** and clear next steps. |
| **CTA** | **Check My Equity Options** |
| **Time** | Takes less than **3 minutes** |
| **Credibility** | `{company_name}` · NMLS `{nmls}` · Equal Housing Lender · Licensed in `{licensed_states}` |

### CRO rules

- No nav menu, no external links above fold except required compliance footer
- Single button; thumb-zone placement on mobile
- Optional: muted loop of `{mlo_name}` 15-sec credibility clip below fold (warm traffic only)
- Ad scent match: landing headline must echo the ad outcome (payment removal vs cash-out vs debt)

### Design (landing)

- Full-viewport **warm cream** canvas (`#FAF7F2`), centered content max-width 420px mobile
- Hero **display headline** in deep navy (`#1B2A4A`) — see [Design system](#part-7-design-system-frontend)
- One **terracotta** CTA (`#C4653A`) with subtle lift shadow; no gradient buttons
- Soft **architectural line illustration** (home + equity abstract) at 12% opacity — not stock photos of seniors pointing at laptops

---

## Part 4 — Stage 2: Quiz (qualification engine)

**Job:** Qualify silently; visitor feels insight, not interrogation.

### UX requirements (Perspective build)

| Element | Spec |
|---------|------|
| Progress | `Question {n} of 10` + thin bar fill (category color shift per section) |
| Momentum | At Q6: *"Almost done — two more sections"* |
| Transitions | 300ms slide; optional 800ms micro-insight card between categories |
| Input pattern | **Large tap cards** (single-select) or **range chips** — avoid keyboard on mobile |
| Back | Allow one step back; preserve answers |
| Loading | After Q1 only: *Personalizing your assessment…* (800ms) — not after every step |

### Categories (3)

| Category | Questions | Purpose |
|----------|-----------|---------|
| **Your Goal** | Q1 | `form_intent` + nurture segment |
| **Your Home** | Q2–Q6 | Equity, occupancy, geography |
| **You & Eligibility** | Q7–Q10 | Age, household, program fit |

### Questions, scoring, routing

| # | Cat | Question | Type | Options | Weight | Signals / routing |
|---|-----|----------|------|---------|--------|-------------------|
| 1 | Goal | If you could improve one thing about your housing costs or equity, what would it be? | Single select | Same 4 intents as V1 spec | — | Maps to `form_intent` (see V1 table) |
| 2 | Home | Is this your **primary residence** — where you live most of the year? | Yes / No | Yes · No | **3** | No → `not_a_fit` (investment/second home path) |
| 3 | Home | Do you currently have a mortgage on the property? | Yes / No | Yes · No | 2 | No → skip Q4 |
| 4 | Home | About how much do you still owe? | Range chips | $0 · Under $100k · $100k–250k · $250k–500k · $500k+ | **3** | With Q5 → `equity_band` |
| 5 | Home | What do you think your home is worth today? | Range chips | Under $200k · $200k–400k · $400k–700k · $700k–1M · $1M+ | **3** | Low band → nurture flag |
| 6 | Home | Which state is the property in? | Dropdown | `{licensed_states}` + Other | **3** | Other / unlicensed → `not_a_fit` |
| 7 | You | What is your age? | Range chips | Under 55 · 55–61 · **62–69** · 70–79 · 80+ | **3** | Under 62 → `not_a_fit` |
| 8 | You | Are you currently married? | Yes / No | Yes · No | 1 | No → skip Q9 |
| 9 | You | How old is your spouse? | Range chips | Under 62 · 62+ | 2 | Conditional; NBS rules internal |
| 10 | You | How soon would you want to explore your options if you qualify? | Single select | Ready now · Within 30 days · Just researching | 2 | `timeline_urgency`; boosts score |

### Scoring logic → `fit_tier`

Compute **`fit_score`** (internal) and persist **`fit_tier`** to GHL.

| Tier | Rule (all must be considered) |
|------|-------------------------------|
| **qualified** | Age 62+ · primary residence Yes · licensed state · equity band not "weak" (value >> balance or free-and-clear) · timeline ≠ *Just researching* only |
| **nurture** | Age 62+ · primary Yes · licensed state · but weak equity band OR timeline *Just researching* OR value range at low end |
| **not_a_fit** | Age under 62 · non-primary · unlicensed state · or explicit opt-out paths |

**Weighting:** Q2, Q5, Q6, Q7 at 3×; Q4, Q9, Q10 at 2×; Q1, Q3, Q8 at 1× for tie-breaks only.

**GHL tags (add to V1 mapping):**

| Field | Values |
|-------|--------|
| `fit_tier` | `qualified` \| `nurture` \| `not_a_fit` |
| `equity_band` | `strong` \| `moderate` \| `weak` \| `unknown` |
| `timeline_urgency` | `ready_now` \| `30_days` \| `researching` |

### Micro-insights (optional, between categories)

One line only — reduces drop-off, increases quiz feel:

| After category | Pattern |
|----------------|---------|
| Your Goal | *Got it — we'll tailor your assessment around **[intent label]**.* |
| Your Home | *Thanks — equity looks like a meaningful part of your picture.* (if bands allow) |

Do not promise approval or specific dollar amounts.

---

## Part 5 — Stage 3: Opt-in (post-quiz)

**Job:** Capture lead at peak intent — immediately after Q10, no extra click.

| Element | Copy pattern |
|---------|--------------|
| **Headline** | Where should we send your **personalized Retirement Equity Assessment**? |
| **Subhead** | Enter your details to see your results and what happens next. |
| **Fields** | First name · Last name · Phone · Email · SMS consent (required) |
| **Submit CTA** | **See My Results** |
| **Privacy** | We respect your privacy. Your information is used only to provide your assessment and connect you with a licensed advisor. [{privacy_policy_url}] |
| **Meta Pixel** | `lead` event on submit click |

**Consent line:** Same TCPA pattern as V1 — `{mlo_name}` placeholder.

**Do not** ask for info already collected in quiz. ZIP optional only if state dropdown insufficient for routing.

---

## Part 6 — Stage 4: Thank-you page (tier-routed)

**Job:** Personalized insight + expectation + trust. **No booking calendar, no "Apply now."**

Soft actions only: **Save Our Number**, FAQ, privacy, optional educational link.

### Variant A — `qualified` (default for SDR tier)

Use when `fit_tier = qualified`. **Preserves V1 speed-to-lead cadence.**

| Block | Content pattern |
|-------|-----------------|
| **Insight** | Thank you, `{first_name}`. Based on your answers — especially your goal to **[intent plain language]** and your timeline — you're in a **strong position to explore your options** with a licensed advisor. |
| **Expectation (hero)** | We're preparing your assessment now. **Expect a call from `{company_name}` within 15 minutes.** Watch for a **`{area_code}`** number. |
| **Timeline (3 steps)** | Same as V1: review → call → 15–20 min walkthrough, no pressure |
| **Trust** | Process transparency + 3 testimonial slots + FAQ accordion (call length, no pressure, nothing to prepare) |
| **Soft CTA** | **Save Our Number** (vCard / tel link) |
| **Downstream** | Full SMS +5m, intent drip, SDR ≤5m — per V1 |

### Variant B — `nurture`

| Block | Content pattern |
|-------|-----------------|
| **Insight** | Thank you, `{first_name}`. You're **on the right track**, but a few details suggest it's worth **clarifying your equity picture** before a full conversation — we'll help with that first. |
| **Expectation** | You'll receive a **summary by email within the hour**. A specialist **may** reach out within **1–2 business days** if your answers suggest a fit — **no pressure**. |
| **Trust** | Educational soft link (HECM basics FAQ) · no 15-minute call promise |
| **Downstream** | Lighter SMS cadence; intent drip; no aggressive SDR dial for 24h |

### Variant C — `not_a_fit`

| Block | Content pattern |
|-------|-----------------|
| **Insight** | Thank you, `{first_name}`. Based on your answers — **[honest reason: age, occupancy, or state]** — this particular program **may not be the right fit today**. |
| **Expectation** | **We won't put you on a sales call list.** We've sent a **free resource** to your email with general guidance for homeowners in your situation. |
| **Trust** | FAQ link · invitation to re-take assessment later when circumstances change |
| **Downstream** | Suppress SDR; tag `dq_funnel`; no speed-to-lead |

### Intent-aware insight snippets (merge into Variant A/B)

| `form_intent` | Plain-language insert |
|---------------|----------------------|
| `remove_mortgage_payment` | eliminate your monthly mortgage payment |
| `pay_off_debt` | reduce debt that's weighing on your retirement |
| `cash_out` / `tax_free_cash_out` | access equity without adding a new monthly bill |

### Thank-you design

- **Qualified:** warm celebratory tone — soft green check animation, confetti restrained (single pulse, not gamified casino)
- **Nurture:** calm blue-gray reassurance
- **Not fit:** neutral, respectful — no red error styling (avoid shame)

Remove V1 **Start your Free Valuation** repeat CTAs on thank-you (quiz-funnel violation + confuses post-submit).

---

## Part 7 — Design system (frontend)

**Aesthetic direction:** *Refined retirement editorial* — trustworthy, warm, magazine-quality. Not fintech neon, not generic SaaS purple, not clip-art seniors.

### Typography (web fonts in Perspective custom CSS if available)

| Role | Font | Fallback |
|------|------|----------|
| Display / questions | [Fraunces](https://fonts.google.com/specimen/Fraunces) | Georgia, serif |
| Body / options | [DM Sans](https://fonts.google.com/specimen/DM+Sans) | system-ui |
| Labels / progress | DM Sans 500, 12px, letter-spacing 0.06em uppercase |

### Color tokens

```css
:root {
  --bg-canvas: #FAF7F2;
  --bg-card: #FFFFFF;
  --text-primary: #1B2A4A;
  --text-muted: #5C6478;
  --accent: #C4653A;        /* terracotta — CTA, progress fill */
  --accent-hover: #A8522E;
  --trust: #2D6A6A;         /* category "Your Home" accent */
  --success: #3D6B4F;
  --border: #E8E2D9;
  --shadow: 0 8px 32px rgba(27, 42, 74, 0.08);
}
```

### Components

| Component | Spec |
|-----------|------|
| **Option card** | White card, 16px radius, 1px `--border`, 16px padding; selected = 2px `--accent` + soft shadow |
| **Progress bar** | 4px height, full width; fill `--accent`; label above right-aligned |
| **Primary button** | Full-width mobile, 52px height, `--accent` bg, white text, Fraunces 18px |
| **Footer** | 11px muted legal; sticky on quiz steps only |

### Motion

- Page enter: fade + 8px translateY, 400ms ease-out
- Option select: scale 0.98 → 1, 150ms
- Progress bar: width transition 500ms ease
- Thank-you check: SVG stroke draw 600ms once

### Spatial layout

- Mobile-first single column; max-width 480px centered
- Question text **left-aligned** (editorial), not centered corporate
- Generous vertical rhythm: 24px between question and options; 40px section padding

---

## Part 8 — Ad → funnel scent matrix

Match landing hook to ad angle ([RM Ad Playbook](../client-marketing/rm-ad-playbook.md)):

| Ad angle | Landing headline variant | Q1 first option emphasized |
|----------|-------------------------|---------------------------|
| Remove payment | …Live More Comfortably **Without a Monthly Mortgage Payment**? | Eliminate my mortgage payment |
| Cash out | …Access **Equity Without a New Monthly Bill**? | Get extra cash… |
| Debt | …**Reduce Retirement Debt** Using Home Equity? | Eliminate debt… |
| Safety net | …Build a **Financial Cushion** for Unexpected Costs? | Protect myself from rising costs… |

Use UTM → dynamic headline swap in Perspective if supported; else duplicate funnel entry pages sharing same quiz core.

---

## Part 9 — Data flow summary

| Stage output | GHL / CRM |
|--------------|-----------|
| Q1 | `form_intent` |
| Q2–Q6, Q7–Q10 | custom fields + `equity_band`, `timeline_urgency` |
| Score engine | `fit_tier`, tag `quiz_qualified` / `quiz_nurture` / `quiz_dq` |
| Opt-in | contact fields, SMS consent, `external form` |
| Thank-you route | workflow branch on `fit_tier` |

**Perspective limitation:** If tier-routing requires separate thank-you URLs, build 3 TY pages and branch in funnel logic; map all three in manifest notes.

---

## Part 10 — Implementation checklist

> **Build path:** Use native Perspective pages (duplicate Reverse Template). Do **not** use
> Perspective AI funnel generation (`create_funnel` MCP) — JS-routed single-page funnels break
> editor preview and conditional routing. See
> [rm-quiz-funnel-v2-perspective-manual-build.md](rm-quiz-funnel-v2-perspective-manual-build.md).

1. [ ] Duplicate Reverse Template → rename `{client_slug}-quiz-v2`
2. [ ] Build landing (hook-only) + 10-step quiz per question table
3. [ ] Implement scoring rules in Perspective logic (or GHL workflow calculator on ingest)
4. [ ] Create 3 thank-you variants; wire branches
5. [ ] Apply design tokens (CSS / Perspective theme)
6. [ ] Map all fields + new tags in GHL; test lead for each tier
7. [ ] Fire Meta `lead` on opt-in submit; verify Events Manager
8. [ ] Run 50-click soft test; compare step drop-off vs V1 via Perspective MCP
9. [ ] Update [perspective-client-manifest.yaml](../media-buying/perspective-client-manifest.yaml) when live

---

## Part 11 — What we intentionally keep from V1

| Element | Why |
|---------|-----|
| Post-quiz opt-in (not pre-gate) | Commitment + quality per doctrine |
| 4 `form_intent` values | Existing iMessage segments |
| 15-minute call promise (qualified) | Speed-to-lead performance variable |
| SMS + intent drip + AI bot stack | Full-funnel ownership |
| Compliance footer every step | RM guardrails |
| Range-based qualification (not quotes) | Marketing number-free |

---

## Related docs

- [RM Funnel Form Spec](rm-funnel-form-spec.md) — V1 baseline
- [Doctrine Reverse Mortgage](doctrine-reverse-mortgage.md)
- [RM Compliance Guardrails](rm-compliance-guardrails.md)
- [RM iMessage Intent Drip](../client-marketing/rm-imessage-intent-drip-7day.md)
- [Perspective Funnel Setup SOP](../media-buying/perspective-funnel-setup-sop.md)
- Quiz funnel skill: `quiz-funnel` (Cursor) — audit checklist source
