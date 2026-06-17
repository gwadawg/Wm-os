---
title: DSCR Static Image Generator — Claude Project Build Pack
domain: client-fulfillment
owner: media-buying-lead
status: draft
last_updated: 2026-06-11
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

Whatever you ask for — typically Ideogram-ready prompts, but no fixed template is required.

## Quality Bar

- Align with [Identity Core](../../company/doctrine-identity-core-april-26.md) and [SOURCE-OF-TRUTH](../../SOURCE-OF-TRUTH.md).
- Outputs must stay inside the compliance guardrails below (refinance only, business-purpose,
  number-free, no guarantees). Flag violations; don't block creative exploration unnecessarily.

## Operating Content

### How to use it

```
[You describe what you want] → [Claude helps: prompt, copy, direction, variations]
      → [Ideogram] → [Canva] → [Meta Ads Manager]
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

Be concise unless they want depth. Be creative unless they want literal. You're a sparring partner, not
a form.
```

## Part 4 — Workflow reference (optional)

Use this pipeline when you're ready to produce — none of it is enforced by the project.

### Ideogram → Canva → Meta

1. Get your prompt from the project (however you asked for it).
2. [Ideogram](https://ideogram.ai) → paste prompt → **4:5** default (1:1 or 16:9 when intentional) → Generate.
3. Check spelling, composition, no stray numbers in the scene → Download.
4. Canva: logo, text fixes, headshot composite → Export.
5. Ads Manager: upload, add copy, launch.

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

### Asset naming (optional)

If you want consistency in Ads Manager / UTMs:

```
dscr_[short-concept-slug]_[ratio]_[YYYY-MM-DD]_v[#]
```

Example: `dscr_balloon-exit_4x5_2026-06-11_v1`. Use whatever slug describes the concept — no angle
codes required.

## Related Docs

- [DSCR DNA README](README.md)
- [Ad Copy And Angle Library (DSCR)](ad-copy-angle-library-dscr.md) — angle store (upload to project)
- [DSCR Ads Playbook](dscr-ads-playbook.md) — full creative playbook (repo reference, not required in project)
- [DSCR Compliance Guardrails](dscr-compliance-guardrails.md) — full compliance doc (repo reference)
- [DSCR Ad Creative — Batch 01](dscr-ad-creative-batch-01.md) — optional example statics
- RM rigid workflow analog: [AI RM Ad Image Creation SOP](../media-buying/ai-rm-ad-image-creation-sop.md)
