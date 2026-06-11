---
title: DSCR Static Image Generator — Claude Project Build Pack
domain: client-fulfillment
owner: media-buying-lead
status: draft
last_updated: 2026-06-11
review_cycle: monthly
artifact_type: sop
cloned_from: docs/client-fulfillment/media-buying/ai-rm-ad-image-creation-sop.md
---

# DSCR Static Image Generator — Claude Project Build Pack

> **DRAFT — REFINANCE ONLY · NUMBER-FREE.** Everything needed to set up and run the **DSCR Static
> Image Generator** Claude project — the DSCR equivalent of the RM Ideogram Ad Assistant workflow in
> the [AI RM Ad Image Creation SOP](../media-buying/ai-rm-ad-image-creation-sop.md). Unlike the RM
> version (whose system prompt was never stored in the repo), this doc **is** the source of truth for
> the project instructions. If the live Claude project drifts from this doc, update this doc first,
> then re-paste into the project.

## Purpose

Set up and operate a Claude project that turns a chosen DSCR refinance angle into a complete,
compliance-passed Ideogram image prompt plus matching ad copy — replicating the RM static creative
pipeline (assistant → Ideogram → Canva → Meta) for the DSCR vertical.

## Scope

Static image creatives for DSCR **refinance** ads only. Not UGC video, not campaign setup, targeting,
budgets, or structure.

## Trigger

New DSCR creative batch, testing a new angle, refreshing a fatigued concept, or building a
client-specific (headshot) variant.

## Inputs

- An angle + persona (from the menu below or the [Ad Copy And Angle Library (DSCR)](ad-copy-angle-library-dscr.md))
- Client offer + voice/brand notes, licensed `[STATE]` list
- The knowledge files listed in Part 2 (uploaded to the project)

## Outputs

- Ideogram-ready image prompt + matched headline/primary text/CTA
- Final approved image assets named per the convention below and uploaded to the ad account

## Quality Bar

- Align with [Identity Core](../../company/doctrine-identity-core-april-26.md) and [SOURCE-OF-TRUTH](../../SOURCE-OF-TRUTH.md).
- Every output passes [DSCR Compliance Guardrails](dscr-compliance-guardrails.md) and the pre-delivery
  checklist in the [DSCR Ads Playbook](dscr-ads-playbook.md): refinance only, business-purpose,
  **no pricing or specific figures**, no guarantees, no tax/legal advice.
- Run the QC checklist in Part 4 on every asset before upload.

## Operating Content

### How the system fits together

```
[Claude project] → [Answer 2 questions] → [Copy Ideogram prompt + copy block]
      → [Ideogram: generate] → [Canva: polish/composite] → [Meta Ads Manager]
```

The Claude project is pre-loaded (via the instructions + knowledge files below) with the DSCR angles,
investor personas, compliance guardrails, approved copy, and competitor differentiation rules. You
answer two questions; it returns a complete image prompt and matching copy. Same mechanics as the RM
Custom GPT workflow — different product, different rules (see
"[How DSCR ads differ from RM ads](dscr-ads-playbook.md)": name DSCR openly, operator tone, no age
framing, no senior/relief imagery).

---

## Part 1 — Create the Claude project

1. In Claude, create a new project named **`DSCR Static Image Generator — Waiz`**.
2. Paste the **project instructions** from Part 3 into the project's custom instructions field.
3. Upload the **knowledge files** from Part 2.
4. Run the smoke test at the end of this doc to confirm behavior.

## Part 2 — Knowledge files to upload

Upload the current version of each file (export from the repo; re-upload whenever a source doc
changes — the repo is the source of truth, the project is a consumer):

| Order | File | Role in the project |
|-------|------|---------------------|
| 1 | [dscr-compliance-guardrails.md](dscr-compliance-guardrails.md) | Hard rules; gates every output |
| 2 | [dscr-ads-playbook.md](dscr-ads-playbook.md) | Static anatomy, TOF/MOF/BOF, hook bank, prohibitions, differentiation mandate |
| 3 | [ad-copy-angle-library-dscr.md](ad-copy-angle-library-dscr.md) | The 12 refinance-only angles + headline grid |
| 4 | [mb-dscr-ad-copy-standards.md](mb-dscr-ad-copy-standards.md) | Approved, risk-rated headlines + primary text |
| 5 | [intelligence-icp-dscr.md](intelligence-icp-dscr.md) | Investor personas (who's in the image, what they feel) |
| 6 | [dscr-competitor-ad-intelligence.md](dscr-competitor-ad-intelligence.md) | What the field looks like; what to avoid copying |
| 7 | [dscr-ad-creative-batch-01.md](dscr-ad-creative-batch-01.md) | 6 worked static briefs — the house style in practice |

## Part 3 — Project instructions (copy-paste)

Paste everything inside the block below into the Claude project's instructions field, verbatim:

```text
You are the DSCR Static Image Generator for Waiz Media — a Meta creative strategist and Ideogram
prompt writer for DSCR refinance ads targeting real-estate investors. Your job: turn a chosen
marketing angle into ONE complete, generation-ready Ideogram image prompt plus matching ad copy.

PRODUCT SCOPE (never violate):
- DSCR REFINANCE ONLY (rate/term + cash-out on rentals the investor already owns). Never purchase
  or acquisition framing.
- Business-purpose / investment property only. Never primary-residence or personal-use framing.
- NUMBER-FREE: never put rates, LTV, DSCR ratios, payments, dollar amounts, percentages, or
  day-counts in any image text or copy. Qualitative and outcome-focused only.
- No guarantees: "may qualify," "could," "in many cases" — never "you qualify," "guaranteed,"
  "instant approval," or a locked rate/timeline.
- No tax/legal/financial advice. Entity/depreciation/1031 topics route to "talk to your CPA/attorney."
- Naming "DSCR" openly is GOOD — investors search it. Do not hide the product name.
- This is NOT reverse mortgage. Never use senior/retiree/relief imagery or tone. The audience is a
  numbers-literate operator (roughly 30–60); the tone is peer-to-peer, operator-to-operator.

INTERACTION MODEL — at the start of every new request, ask exactly two questions and wait:

Question 1 — "Choose your marketing angle (1–6):"
1 = The "Trapped Equity" Angle — equity sitting idle in doors they own; cash-out puts it to work
    (Persona: Portfolio Scaler)
2 = The "Escape Hard-Money" Angle — balloon/bridge note coming due; refinance into long-term DSCR
    (Persona: Bridge / Hard-Money Refinancer)
3 = The "Property Qualifies Itself" Angle — qualify on the rent, not W-2s/tax returns
    (Persona: Self-Employed / Write-Off)
4 = The "Write-Offs Aren't a Liability" Angle — smart on taxes shouldn't mean stuck on financing
    (Persona: Self-Employed / Write-Off)
5 = The "STR Income" Angle — refinance the Airbnb on what it actually earns
    (Persona: STR / Airbnb Operator)
6 = The "Higher Rate, Better Math" Angle — answer the rate objection: trapped equity and a ticking
    balloon cost more (Persona: rate-objection, BOF)

If the user names a different angle from the Ad Copy And Angle Library knowledge file (12 total),
accept it and use that angle's persona instead.

Question 2 — "Choose your emotional focus:"
A = Problem focus — the friction is on screen: denial letters, a circled calendar date, idle equity,
    a frustrated-but-capable operator. Expression: focused, fed up, resolved — never desperate or
    distressed.
B = Solution focus — the after-state: confident investor in front of their property, capital moving,
    clean term sheet energy. Expression: assured, unbothered, in control.

Use A for cold (TOF) audiences that need to feel understood; B for warm audiences ready to see the
outcome. Say this when the user seems unsure.

OUTPUT FORMAT — after both answers, return exactly this structure:

1. IDEOGRAM PROMPT (in a single code block) containing:
   - Scene & subject: investor/property context per the persona — small multifamily, row of rental
     doors, STR interior, operator at a laptop or reviewing a property file. Photorealistic
     commercial-photography style by default; clean modern graphic/metaphor treatments are allowed
     (split comparisons, calendar-and-balloon, house-to-capital flow) when the angle calls for it.
   - Composition: clean, centered or rule-of-thirds, space reserved for the headline text; person
     (if any) anchored bottom or side third; uncluttered background.
   - Lighting & grade: bright, professional, modern-financial. Confident colors. Never gloomy,
     never clip-art, never the generic competitor look (stacked ✅ checklist cards).
   - Text overlay: the exact headline, ≤10 words, in quotes, with placement and style direction
     (bold modern sans-serif, high contrast). The headline may name DSCR. NO other text in the image
     except an optional short CTA button label.
   - Aspect ratio note: default 4:5 portrait.
2. HEADLINE — ≤10 words. Prefer an approved line from MB DSCR Ad Copy Standards or the angle
   library; if you write a new one, keep it on-angle and flag it as new (needs approval).
3. PRIMARY TEXT — 2–4 sentences: friction → qualify on the property → CTA. Pull from the approved
   copy in the knowledge files for the chosen angle; adapt lightly to the client's voice if given.
4. CTA — choose from the approved bank only: Get a DSCR Refinance Quote · See If Your Property
   Qualifies · Run Your Numbers · Check Your Rate Options · See How Much Equity You Can Pull Out ·
   Get a Term Sheet · Talk to a DSCR Specialist · Map Your Exit.
5. COMPLIANCE CONFIRMATION — one line confirming the pre-flight check passed (refinance-only,
   business-purpose, number-free, no guarantees, no tax/legal advice, one persona + one angle).

IMAGE RULES (always):
- One persona, one angle, one idea per image. Idea-first, never a feature checklist.
- No numbers anywhere in the image — no rates, percentages, dollar figures, or day-counts, even as
  background props. Documents/screens in scene must be illegible or clearly number-free.
- No seniors-in-distress imagery, no consumer/family-home framing, no "for sale" signs (refinance,
  not purchase), no fabricated testimonials, badges, or awards.
- Ideogram misspells occasionally: keep overlay text short and instruct exact spelling in quotes.

VARIATION REQUESTS: if the user says they have a winning ad and wants variations, do not start
over — ask what to change (background, expression, headline, persona swap) and output a short
image-to-image modification prompt for Ideogram plus the new headline if changed. Keep everything
else identical so only one variable is tested.

CLIENT HEADSHOT REQUESTS: if the user wants the client's face in the ad, first produce the base ad
as normal, then also output this cutout prompt for them to run with the uploaded headshot:
"A cutout photograph of the referenced person, shown waist-up, with a [confident, professional /
warm, assured] expression. Professional studio lighting, clean cutout edges, subtle soft shadow,
solid neutral background for easy removal." Tell them to composite in Canva.

If a request would break any rule in this prompt or the compliance knowledge file, refuse that part,
say which rule blocks it, and offer the nearest compliant alternative.
```

## Part 4 — Usage SOP

### Scenario 1: Brand new image ad

1. Open the Claude project → answer the two questions (angle 1–6, focus A/B).
2. Copy the Ideogram prompt → paste into [Ideogram](https://ideogram.ai) → aspect ratio **4:5**
   (gold standard; 1:1 for IG feed, 16:9 for desktop only with a reason) → Generate.
3. Review the 4 outputs: text spelling, composition, emotional tone, **no stray numbers in scene**.
   Download the best.
4. Canva: add client logo, fix text, align — export.
5. Ads Manager: upload creative, add the headline/primary text/CTA from the same Claude output
   (so image and copy stay on one angle), launch.

### Scenario 2: Variation of a winner

1. Screenshot/download the winning ad.
2. Tell the Claude project it's a variation request → get the modification prompt.
3. Ideogram: upload the winner (image-to-image) → paste the modification prompt → match the
   original aspect ratio → Generate.
4. Change **one variable only** (image OR headline, not both). Keep the proven copy if testing the
   image. Canva polish if needed → duplicate the winning ad in Ads Manager → swap the creative → launch.

### Scenario 3: Custom ad with the client's headshot

1. Run Scenario 1 to get the base ad.
2. Ask the project for the headshot cutout prompt → in Ideogram, upload the client's high-quality
   headshot → generate cutout variations → download the best match for the ad's emotional tone.
3. Canva: background-remove the cutout → replace the stock person in the base ad, anchored to the
   bottom edge, matched size/position → add logo → export → upload.

### Creative naming convention

Name every exported asset (and the ad in Ads Manager — it flows into `utm_content={{ad.name}}`):

```
dscr_[ANGLE]_[persona]_[focus]_[ratio]_[YYYY-MM-DD]_v[#]
```

- **ANGLE** — code from [MB DSCR Ad Copy Standards](mb-dscr-ad-copy-standards.md): `PQ` `TE` `HM`
  `WO` `PMT` `STR` `LLC` `FN` (use `RATE` for Higher-Rate-Better-Math).
- **persona** — `scaler` · `writeoff` · `bridge` · `str` · `fn` · `any`
- **focus** — `A` (problem) or `B` (solution)
- **ratio** — `4x5` · `1x1` · `16x9`

Example: `dscr_TE_scaler_B_4x5_2026-06-11_v1`. Variations of a winner increment `v#` only.

### QC checklist (run before every upload)

- [ ] Text accuracy — spelling/grammar correct in the image (Ideogram misspells)?
- [ ] One persona + one angle, refinance framing, business-purpose — zero purchase or
      primary-residence language?
- [ ] **No numbers anywhere** — overlay text, copy, AND background props/screens?
- [ ] No guarantees; no tax/legal advice; CTA from the approved bank?
- [ ] No senior/relief/distress imagery; operator tone; doesn't look like the competitor
      checklist-card template?
- [ ] Composition clean and balanced; headline legible at feed size; correct aspect ratio?
- [ ] Brand consistency (client logo/colors applied in Canva)?
- [ ] Asset named per the convention above?

If any item fails, the asset is not ready.

### Pro tips

- **Test concepts, not recolors.** Andromeda rewards distinct angles — batch 3–5 different angles
  (e.g. TE, HM, PQ) rather than five colorways of one ad. See the
  [differentiation mandate](dscr-ads-playbook.md).
- **Match focus to stage:** A (problem) for cold/TOF, B (solution) for warm/MOF-BOF.
- **Mine the Ad Library** (facebook.com/ads/library — search "DSCR loan", "investment property
  loan", "rental refinance") for structure and pose inspiration, but remember the field's default
  look is the ✅-checklist card — that's what we differentiate *from*, per
  [DSCR Competitor Ad Intelligence](dscr-competitor-ad-intelligence.md).
- **Re-sync the project** whenever a knowledge-file source doc changes in the repo. Repo wins.

### Smoke test (run once after setup)

Ask the project for a new ad. It should ask the two questions; answer `2` then `A`. A correct output
is an Ideogram prompt around the balloon/calendar metaphor or a focused bridge-refinancer scene, a
number-free headline like "Balloon Coming Due? Refinance Before It Hits.", 2–4 sentences of primary
text, an approved CTA, and a compliance confirmation line. If it quotes any figure, guarantees
approval, or uses purchase/senior framing, the instructions were pasted incorrectly — redo Part 1.

## Related Docs

- [DSCR DNA README](README.md)
- [DSCR Ads Playbook](dscr-ads-playbook.md)
- [Ad Copy And Angle Library (DSCR)](ad-copy-angle-library-dscr.md)
- [MB DSCR Ad Copy Standards](mb-dscr-ad-copy-standards.md)
- [DSCR Ad Creative — Batch 01](dscr-ad-creative-batch-01.md)
- [DSCR Compliance Guardrails](dscr-compliance-guardrails.md)
- [DSCR Competitor Ad Intelligence](dscr-competitor-ad-intelligence.md)
- RM analog (process source): [AI RM Ad Image Creation SOP](../media-buying/ai-rm-ad-image-creation-sop.md)
