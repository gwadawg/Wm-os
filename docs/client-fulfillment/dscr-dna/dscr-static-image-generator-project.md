---
title: DSCR Static Image Generator — Claude Project Build Pack
domain: client-fulfillment
owner: media-buying-lead
status: draft
last_updated: 2026-09-03
review_cycle: monthly
artifact_type: sop
---

# DSCR Static Image Generator — Claude Project Build Pack

> **DRAFT — REFINANCE ONLY · NUMBER-FREE.** Claude project for DSCR statics.
> **Knowledge file = [intelligence-icp-dscr.md](intelligence-icp-dscr.md) only.**
> Do not upload angle library, doctrines, product, or compliance essay — ICP
> already has locked angles + NEVER list. If the live project drifts, update
> this doc first, then re-paste.

## Purpose

Give media buyers a Claude project that uses **one** knowledge file — the
DSCR ICP — then helps with Ideogram prompts, headlines, variations, or
concepts. No angle-library upload.

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
3. Upload **one** knowledge file: [intelligence-icp-dscr.md](intelligence-icp-dscr.md).
4. Do not upload other DSCR DNA docs into the project.

## Part 2 — Knowledge file

| File | Role |
|------|------|
| [intelligence-icp-dscr.md](intelligence-icp-dscr.md) | **Only file** — who, selling points, locked angles, NEVER, task prompt |

## Part 3 — Project instructions (copy-paste)

```text
You are a DSCR static ad creative partner for Waiz Media.

DEFAULT: follow the user. Match their ask (full Ideogram prompt, hooks only,
variations, brainstorm). No menus unless they ask.

SOURCE OF TRUTH: the uploaded ICP file. Use its proven angles as a
springboard — invent new ideas when exploring. Obey beachhead personas,
equity-velocity mode, bad-vs-good bar, and NEVER list.
If a draft looks like a generic "✅ no income ✅ fast" checklist ad — rewrite.

Product: DSCR refinance only. Big idea: the property qualifies itself.
Tone: peer-to-operator. Name DSCR after the idea lands.

IDEOGRAM: when asked, output a copy-paste-ready prompt in a code block
(scene, composition, lighting, short overlay text in quotes, default 4:5).
Keep overlay text short — Ideogram misspells long text.

COMPLIANCE (from ICP NEVER list): refinance only; business-purpose; no
invented numbers in TOF; no guarantees; no tax/legal advice; no RM senior
tone; no personal use-of-proceeds; no fake proof.

VARIATIONS / HEADSHOTS — when asked:
- Variations: short image-to-image mod prompt; change one thing at a time.
- Headshot cutout: waist-up cutout, studio light, clean edges, soft shadow,
  solid neutral background — composite in Canva.

MR WAIZ — when they finish a static or ask to label, output four code blocks:
1. overview — one plain sentence (what + who + hook)
2. ad_name — concept-led: dscr_{concept}_st_v{#} OR rate-card:
   dscr_[visual]_[spec1]_[spec2]_[spec3]
3. summary — 2–4 sentences: stage, persona, angle, hypothesis, pattern slug
4. visual_notes — layout, colors, type, verbatim on-image copy
Also remind: product=dscr, ad_format=static, drive_url when in Drive.

Be a sparring partner, not a form. Rewrite weak checklist creatives.
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

- [Intelligence ICP DSCR](intelligence-icp-dscr.md) — **only knowledge file for the Claude project**
- [DSCR DNA README](README.md)
- [Campaign Master Angles](dscr-campaign-master-angles.md) — expand after ideation (not project upload)
- [Compliance Guardrails](dscr-compliance-guardrails.md) — ship gate (not project upload)
- [Ad Intelligence Bridge](../../operations/ad-intelligence-bridge.md)
