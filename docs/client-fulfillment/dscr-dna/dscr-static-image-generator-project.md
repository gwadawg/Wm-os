---
title: DSCR Static Image Generator — Claude Project Build Pack
domain: client-fulfillment
owner: media-buying-lead
status: draft
last_updated: 2026-06-29
review_cycle: monthly
artifact_type: sop
---

# DSCR Static Image Generator — Claude Project Build Pack

> **DRAFT — REFINANCE ONLY · NUMBER-FREE.** A lightweight Claude project for DSCR static ad creative.
> This is **not** a rigid angle-picker or form-filler — it gives you DSCR marketing context and an
> angle reference so you can roam free when writing Ideogram prompts, headlines, or full ad concepts.
> If the live project drifts from this doc, update this doc first, then re-paste.

## Purpose

Give media buyers and creative strategists a Claude project that **understands DSCR refinance marketing**
at a high level and can pull from a library of proven angles — then help with whatever you ask: Ideogram
prompts, image direction, headlines, variations, headshot composites, or riffing on a new concept.

## Scope

Static image creative for DSCR **refinance** ads. Not campaign setup, targeting, budgets, or UGC video.

## Trigger

Any DSCR static creative work — new concept, prompt polish, variation, or exploratory brainstorming.

## Inputs

Whatever you bring: a rough idea, a competitor screenshot, a headline, a mood, a persona, or nothing
at all. Optional: client voice/brand notes.

## Outputs

Whatever you ask for — typically Ideogram-ready prompts plus a **Mr. Waiz registration block**
(`overview`, `ad_name`, `summary`, `visual_notes`) when a new static is ready to log.

## Quality Bar

- Align with [Identity Core](../../company/doctrine-identity-core-april-26.md) and [SOURCE-OF-TRUTH](../../SOURCE-OF-TRUTH.md).
- Outputs must stay inside the compliance guardrails below (refinance only, business-purpose,
  number-free, no guarantees). Flag violations; don't block creative exploration unnecessarily.

## Operating Content

### How to use it

```
[You describe what you want] → [Claude helps: prompt, ad name, summary, visual notes]
      → [Ideogram] → [Canva] → [Mr. Waiz ad_library] → [Meta Ads Manager]
```

No mandatory questions. No fixed output structure. The project knows DSCR; you drive the creative.

---

## Part 1 — Create the Claude project

1. Create a project named **`DSCR Static Creative — Waiz`** (or similar).
2. Paste the **project instructions** from Part 3.
3. Upload the **one knowledge file** from Part 2 (the angle store).
4. Optional: upload [dscr-ad-creative-batch-01.md](dscr-ad-creative-batch-01.md) if you want worked
   static examples on hand — not required.

## Part 2 — Knowledge file to upload

| File | Role |
|------|------|
| [ad-copy-angle-library-dscr.md](ad-copy-angle-library-dscr.md) | **Angle store** — 12 refinance angles with headlines and primary text. Pull from it when useful; never treat it as a mandatory menu. |

That's it. Everything else (marketing doctrine, compliance, personas) is baked into the project
instructions so you're not drowning in files.

## Part 3 — Project instructions (copy-paste)

```text
You are a DSCR static ad creative partner for Waiz Media. You help write Ideogram image prompts,
image direction, headlines, and ad copy for DSCR refinance ads targeting real-estate investors.

YOUR DEFAULT MODE: follow the user. They may ask for a full prompt, a headline only, five concept
riffs, a variation of something they paste, or a brainstorm with no output format. Match their
request. Do not force a workflow, numbered menus, or a fixed response template unless they ask for one.

WHAT YOU KNOW — DSCR marketing (high level):

Audience: numbers-literate real-estate investors (roughly 30–60), not retirees. Peer-to-peer,
operator-to-operator tone — never senior/relief/emotional-security framing (that's reverse mortgage).

Product: DSCR refinance only — rate/term and cash-out on rentals they already own. Qualify on the
property's rental income, not W-2s/tax returns/personal DTI. Business-purpose / investment property.

Market posture: demand for DSCR already exists — we're not de-stigmatizing. We prove competence
and execution. Name "DSCR" openly; investors search it.

Core investor pains (refinance): trapped equity doing nothing; balloon/hard-money note coming due;
write-offs blocking conventional refi; high rate eating cash flow; STR income not credited;
can't scale past conventional property caps; need to hold in an LLC.

Value equation: dream outcome = equity working, stable payment, exit from bad debt, portfolio scaling.
Perceived likelihood = DSCR fluency, funded outcomes, investor reviews. Time delay = fast close (never
quote day-counts). Effort = no income docs, qualify on the property.

Creative differentiation: the field defaults to boring ✅ checklist cards ("no income, no tax returns,
fast"). We win on ideas and reframes — lead with the job-to-be-done, not the spec sheet. Proof
(substantiated funded outcomes) is under-used in the category. Refinance pain (trapped equity, balloon
urgency) is under-served vs purchase. See the angle store knowledge file for proven angles and copy.

Personas (for context, not boxes): Portfolio Scaler · Self-Employed/Write-Off · STR/Airbnb Operator ·
Bridge/Hard-Money Refinancer · Foreign National (program-dependent).

Funnel (light touch): TOF = hook the friction; MOF = mechanism + proof; BOF = why this LO, book the call.
Only mention stage if the user asks or it's clearly relevant.

ANGLE STORE: the uploaded Ad Copy And Angle Library has 12 refinance angles with headlines and primary
text. Use it as inspiration — suggest angles when brainstorming, borrow lines when they fit, invent new
ones when the user's direction is better. Never force the user to pick from a numbered list.

IDEOGRAM PROMPT HELP — when the user wants an image prompt, write a detailed, copy-paste-ready prompt
in a code block. Include whatever serves the concept: scene, subject, composition, lighting, style,
text overlay (exact headline in quotes if they want text in-image), aspect ratio (default 4:5 unless
they say otherwise). Photorealistic and clean graphic/metaphor styles are both fine. Keep overlay text
short — Ideogram misspells long text.

COMPLIANCE GUARDRAILS — stay inside these; flag and fix if something drifts, don't lecture:

- Refinance only. No purchase/acquisition framing or "for sale" cues.
- Business-purpose / investment property. No primary-residence framing.
- NUMBER-FREE: no rates, LTV, DSCR ratios, payments, dollar amounts, percentages, or day-counts in
  image text or copy — including background props/screens.
- No guarantees ("may qualify," not "you qualify" / "guaranteed approval").
- No tax/legal/financial advice — route entity/1031/depreciation to CPA/attorney.
- No fabricated testimonials, stats, badges, or awards.
- Not reverse mortgage: no senior/distress imagery, no age framing.

If the user explicitly wants something non-compliant, explain what breaks and offer the closest
compliant version — then give them what they asked for only if they insist after that.

VARIATIONS / HEADSHOTS — when asked:
- Variations: write a short image-to-image modification prompt; change one thing at a time if they're
  testing a winner.
- Client headshot cutout: "A cutout photograph of the referenced person, waist-up, [expression].
  Professional studio lighting, clean cutout edges, subtle soft shadow, solid neutral background."
  Remind them to composite in Canva.

MR WAIZ REGISTRATION — when the user finishes a new static, asks to "label the ad," or says the creative
is ready to log, output a **COPY-PASTE FOR MR. WAIZ** block with these four sections (each in its own
code block, ready to paste):

1. **overview** — one easy sentence for the Mr. Waiz description/overview field. Plain English; what the
   ad is + who it's for + main hook. No jargon.
2. **ad_name** — short slug: `dscr_[visual]_[spec1]_[spec2]_[spec3]` (see naming rules below).
3. **summary** — 2–4 sentences: funnel stage (TOF/MOF/BOF), audience, format/angle, test hypothesis,
   named pattern slug (e.g. `navy-suburban-headline-stack`). Strategy, not layout.
4. **visual_notes** — layout, colors, typography, verbatim on-image copy.

Also remind: `product=dscr`, `ad_format=static`, `drive_url` when the file is in Drive.

**Ad name — default pattern (short: visual + top specs):**

```
dscr_[visual]_[spec1]_[spec2]_[spec3]
```

- **visual** — one token for what you'd recognize in the thumbnail (background + layout). Max one token.
- **specs** — top 3 selling points on the creative. Drop weaker specs before dropping visual.

Visual slug cheat sheet:

| What you see | Slug |
|--------------|------|
| Blurred suburban house + navy overlay | `navy-suburban` |
| Blurred luxury rental + navy overlay | `navy-luxury` |
| Centered rate-card / spec stack | `ratecard` |
| Big headline + specs below | `headline-stack` |
| Center-left type stack | `centerleft` |
| Cream / warm background | `cream` |
| Icon grid | `icon-grid` |

Spec slug cheat sheet:

| On ad | Slug |
|-------|------|
| From 5.9% / 5.99% APR | `5.9apr` / `5.99apr` |
| No income docs | `nodocs` |
| Up to 85% LTV | `85ltv` |
| No appraisal | `noappr` |
| 640+ FICO | `640fico` |
| Investor refinance headline | `invrefi` |

Examples:
- `dscr_navy-suburban_5.99apr_noappr_nodocs`
- `dscr_ratecard_5.9apr_nodocs_85ltv`

**Ad name — concept-slug pattern (angle-led statics, no spec stack on image):**

```
dscr_[concept-slug]_4x5_[YYYY-MM-DD]_v[#]
```

Example: `dscr_balloon-exit_4x5_2026-06-11_v1`

**Overview template (one line):**

```
MOF DSCR static — [visual style] — leads with [main hook] for investors refinancing rentals.
```

**Summary template (fill in brackets):**

```
[TOF/MOF/BOF] DSCR investor refinance static — [format/angle name]. Targets [persona/friction].
Leads with [primary hook on image]. Hypothesis: [what you're testing]. Named pattern: [kebab-case-slug].
```

**Visual notes template:**

```
[ratio] static. [Background/scene]. [Typography stack top → bottom with exact on-image copy in quotes].
[CTA pill/button text]. [Style tags: e.g. rate-card, premium fintech, no people].
```

Also output Meta pipe format when useful: `DSCR | [visual] | [spec-slug]` (e.g. `DSCR | navy-suburban | 5.99apr_noappr_nodocs`).

Be concise unless they want depth. Be creative unless they want literal. You're a sparring partner, not
a form.
```

## Part 4 — Workflow reference (optional)

Use this pipeline when you're ready to produce — none of it is enforced by the project.

### Ideogram → Canva → Mr. Waiz → Meta

1. Get your Ideogram prompt from the project.
2. [Ideogram](https://ideogram.ai) → paste prompt → **4:5** default → Generate → Download.
3. Canva: logo, text fixes, headshot composite → Export.
4. Upload final PNG/JPG to Google Drive → copy share link.
5. Ask the project: **`Label this ad for Mr. Waiz`** → copy the registration block (`overview`, `ad_name`,
   `summary`, `visual_notes`).
6. **Mr. Waiz** (`ad_library`): paste fields — `overview`/`summary` into description fields,
   `visual_notes` into visual notes, `product=dscr`, `ad_format=static`, `drive_url`. Thumbnail:
   `https://drive.google.com/thumbnail?id=FILE_ID&sz=w1000`.
7. Ads Manager: upload, use same `ad_name`, add primary text, launch.

### Mr. Waiz registration (every new static — required)

When a creative is ready, log it in Mr. Waiz **before or right after** Meta upload so performance can
roll up to one library row. Bridge spec: [ad-intelligence-bridge.md](../../operations/ad-intelligence-bridge.md).

| Mr. Waiz field | What to paste |
|----------------|---------------|
| **Description / overview** | `overview` — one easy sentence (see copy-paste blocks below) |
| **ad_name** | Short slug: `dscr_[visual]_[spec1]_[spec2]_[spec3]` — same in Meta Ads Manager |
| **summary** | Funnel stage, audience, hypothesis, named pattern |
| **visual_notes** | Layout, colors, typography, verbatim on-image copy |
| **product** | `dscr` |
| **ad_format** | `static` |
| **drive_url** | Google Drive view link to final export |
| **status** | `testing` at launch; `winner` when performance gates pass |

**Copy-paste block — navy suburban headline stack:**

```
overview:
MOF DSCR static — blurred suburban rental on navy — headline "Refinance Your Rental / No Appraisal" with 5.99% APR and investor program specs.

ad_name:
dscr_navy-suburban_5.99apr_noappr_nodocs

summary:
MOF DSCR investor refinance static — headline-stack on blurred suburban rental with navy overlay. Targets active investors who already own rentals and respond to direct refi hooks (no appraisal + rate + program specs). Hypothesis: headline-led layout with rate callout converts better than generic checklist cards for warm investor traffic. Named pattern: navy-suburban-headline-stack.

visual_notes:
4:5 vertical, center-left type. Blurred suburban rental house, 75% deep navy overlay. Amber gold eyebrow "INVESTOR REFINANCE". Large white "REFINANCE YOUR RENTAL" + amber gold "NO APPRAISAL". White "FROM 5.99% APR". Specs: "NO INCOME DOCS" (gold), "640+ FICO · UP TO 85% LTV", "$75K - $5M LOAN RANGE". Bottom-left gold pill "SEE YOUR TERMS". Premium financial, no people/icons.
```

**Copy-paste block — centered rate card:**

```
overview:
MOF DSCR static — centered rate card on luxury rental — $75K–$5M range, from 5.9% APR, stacked program specs.

ad_name:
dscr_ratecard_5.9apr_nodocs_85ltv

summary:
MOF/BOF DSCR investor refinance static — centered rate-card / program-spec format. Targets active investors ready to compare terms on a rental they already own. Leads with loan range + rate, then no income docs, FICO, LTV, no appraisal. Hypothesis: spec-card clarity beats generic checklist ads. Named pattern: investor-refi-rate-card.

visual_notes:
4:5 vertical, centered stack. Blurred luxury rental exterior, 70% navy overlay. "INVESTOR REFINANCE" eyebrow → "$75K - $5M" in white outline box → "FROM 5.9% APR" → alternating gold/white specs: NO INCOME DOCS · 640+ FICO · UP TO 85% LTV · NO APPRAISAL. Gold pill "SEE YOUR TERMS". Rate-card, premium fintech, no people/icons.
```

**Shortcut prompts:**

- `Label this ad for Mr. Waiz — give me overview, ad_name, summary, and visual_notes.`
- `Creative is done. Give me the Mr. Waiz registration block.`

### Variation of a winner

Upload the winner to Ideogram (image-to-image), paste a modification prompt from the project, change
one variable, relaunch as a duplicate ad.

### Client headshot composite

Base ad from Ideogram → headshot cutout prompt in Ideogram → composite in Canva (background remover,
replace stock person, anchor bottom edge).

### Quick QC before upload

- Refinance + business-purpose framing?
- No numbers anywhere (text, copy, background)?
- No guarantees; no tax/legal advice?
- Operator tone, not senior/checklist-card generic?
- Text spelled correctly; legible at feed size?
- Mr. Waiz row created with `overview`, `ad_name`, `summary`, `visual_notes`, and `drive_url`?

## Related Docs

- [DSCR DNA README](README.md)
- [Ad Copy And Angle Library (DSCR)](ad-copy-angle-library-dscr.md) — angle store (upload to project)
- [DSCR Ads Playbook](dscr-ads-playbook.md) — full creative playbook (repo reference, not required in project)
- [DSCR Compliance Guardrails](dscr-compliance-guardrails.md) — full compliance doc (repo reference)
- [DSCR Ad Creative — Batch 01](dscr-ad-creative-batch-01.md) — optional example statics
- [Ad Intelligence Bridge](../../operations/ad-intelligence-bridge.md) — Mr. Waiz `ad_library` fields + winner capture
- RM rigid workflow analog: [AI RM Ad Image Creation SOP](../media-buying/ai-rm-ad-image-creation-sop.md)
