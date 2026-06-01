---
title: Higgsfield Prompt Builder (RM UGC)
domain: client-fulfillment
owner: media-buying-lead
status: draft
last_updated: 2026-05-30
review_cycle: monthly
artifact_type: playbook
---

# Higgsfield Prompt Builder (RM UGC)

Turns a finished reverse-mortgage ad **concept** into a ready-to-paste **Higgsfield AI-video
prompt** — single-prompt or chunked. Powers the `prompt` command of the
[rm-creative-studio skill](../../../../.claude/skills/rm-creative-studio/SKILL.md).

> This is a distinct **short-form UGC** flow (18–32s). It is **separate from** the long-form
> 45–90s [rm-script-generator.md](rm-script-generator.md). It reuses the same archetypes, VOC,
> and [compliance gate](compliance-gate-checklist.md), so output stays on-brand and compliant.
>
> **Source:** adapted from the *Universal UGC Script Writing System v2* (a niche-agnostic AI-video
> prompt framework). The transferable production mechanics are kept; the beauty/skin/physical-product
> parts are replaced for reverse mortgage; an RM compliance overlay is added (the source has none).

## Scope

- **In:** concept → short UGC voiceover → Higgsfield prompt(s) (standard or chunked), UGC
  creator-to-camera, RM compliant.
- **Out:** the 45–90s long-form script (use [rm-script-generator.md](rm-script-generator.md));
  static images ([ai-rm-ad-image-creation-sop.md](../ai-rm-ad-image-creation-sop.md)); the
  future auto-render agent ([FUTURE-video-agent-spec.md](FUTURE-video-agent-spec.md)).
- **Generic RM only.** No client-specific names, amounts, or results — use `[TO FILL]`.

## Inputs (collect or ask; do not invent)

- A **concept** from the [ideation matrix](rm-ad-ideation-matrix.md): archetype + angle + stage + hook type. (Or archetype + angle + stage directly.)
- VOC, fears, desires, objections from the [ICP doc](../../reverse-mortgage-dna/intelligence-icp-rm.md); talent/persona cues from [rm-archetypes-canonical.md](rm-archetypes-canonical.md).
- Talent demographic and setting preference (optional; defaults below).
- Whether a program-reveal asset is available (on-screen text card, document prop). TOF never uses one.

## 1. Two formats (pick by funnel stage)

| Attribute | Full Stack | Mid-Funnel Punchy |
|-----------|-----------|-------------------|
| Runtime | 28–32s | 18–22s |
| Word count | 150–180 | 55–70 |
| Beats | 5: hook, reframe, mechanism, payoff, CTA | 3: hook+reframe folded, mechanism+analogy, soft payoff+close |
| Default scenes | 3 | 2 (3 only if VO requires) |
| Chunk count | 5 | 3 |
| Use for | Cold/TOF audiences needing the full education arc | Warmer MOF/BOF audiences who know the problem |

## 2. RM UGC voiceover beat structure

Short-form beats adapted from the source, re-pointed at the RM **Debt Frame → Retirement-Tool
Frame** shift. Empathy uses verbatim or near-verbatim VOC (ICP §5). Beats respect the stage.

### Full Stack (5 beats)

| Beat | Timing | Job (RM) |
|------|--------|----------|
| 1. Hook | 0:00–0:03 | Call out the exact retired homeowner and confirm the specific frustration. Two sentences. For the prospect, never about the speaker. |
| 2. Reframe | 0:03–0:10 | Reveal why past attempts failed: they treated it as a Debt problem, so they kept doing Debt-frame things (skip, downsize, dip into savings). |
| 3. Mechanism + analogy | 0:10–0:20 | Introduce the idea by outcome first, one concept, in plain language, with a one-second tactile analogy. The analogy is the most important sentence. |
| 4. Payoff | 0:20–0:25 | Specific, dignified lived experience after — concrete, not abstract benefits. |
| 5. CTA | 0:25–0:30 | Soft, info-access close from the approved bank. |

### Mid-Funnel (3 beats)

| Beat | Timing | Job (RM) |
|------|--------|----------|
| 1. Hook + reframe folded | 0:00–0:06 | One line that calls out the audience and dismisses the wrong assumption in the same breath. |
| 2. Mechanism + analogy | 0:06–0:16 | Compressed mechanism plus the tactile analogy. The analogy stays intact at all costs. |
| 3. Soft payoff + close | 0:16–0:21 | One sensory beat plus the suggestion-style CTA. |

### Voiceover rules

- **Hook owns the first five words.** Identify the person, confirm the frustration. Passes the "prospect or speaker?" test.
- **Sentence flow, not choppy stutter.** Connectors and complete thoughts. No stacked two-word fragments.
- **Plain mechanism.** A 12-year-old understands it. Always paired with a tactile analogy ("Think of it less like ___ and more like ___").
- **No em dashes, no bolding in voiceover** (they break read-aloud rhythm). Commas, periods, short connectors.
- **Reframe pattern (RM):** "Most people think a tight retirement is an *income* problem, so they keep [Debt-frame behavior]. But the money is already in the house — they were just never shown the tool to use it." Adapt to the angle.
- **RM compliance is live in the voiceover** (see §8): no product name at TOF, no age, no guarantees, no tax advice, no false urgency, no pity.

### Soft CTA bank (RM, info-access)

- "I'll leave something below that explains how it actually works."
- "If you want to look into it, there's a link below."
- "I'll drop a free guide below so you don't have to go searching."
- Match friction to stage: TOF/MOF = info access; BOF = "book a quick call with [TO FILL]."

## 3. Direction blocks (paste into every prompt)

Five blocks lock production quality. **B-Roll Sequencing** and **UGC Realism** transfer from the
source. **Skin** and **Application** (beauty/physical) are replaced by **Subject/Setting Realism**
and **Concept-Reveal**. **Clean Frame + Audio** (3.5) is the RM add-on that forbids AI-rendered
text and music.

### 3.1 Subject / Setting Realism Block — paste verbatim, fill brackets

> Important subject direction: The creator is a credible, healthy, in-control retired homeowner
> with a calm, warm, dignified presence throughout the entire video. They look comfortable and
> at ease in their own home — relaxed posture, genuine micro-expressions, no distress, no worry,
> no frailty or hardship at any point. The home is clean, lived-in, and pleasant. This applies to
> every talking-to-camera scene and every cutaway. [SETTING WITH LIGHTING].

Principle: lock the subject into the dignified, in-control "after" state the viewer is being shown
the path to. This is also a hard compliance rule (no pity / no distressed-senior framing).

### 3.2 Concept-Reveal Block — paste verbatim, fill brackets

Reverse mortgage has **no physical product**, so the "reveal" is the *concept* — on-screen
program text, a simple document/guide prop, or a calm in-home moment — not a held object or cash.

> Important reveal direction: When the idea is introduced, show it as [DESIRED VISUAL — e.g. a
> clean on-screen text card / a plain printed guide on the kitchen table / the creator gesturing
> calmly]. No cash, no stacks of money, no flying dollars, no bank or lender logos, no
> "approved" stamps, no distressed-senior or crisis imagery at any point. The visual stays warm,
> ordinary, and dignified — the home and the person, not a financial product.

Principle: name the AI's default failure (money imagery, lender branding, crisis tone) and
override it with a calm, dignified, home-centered visual.

### 3.3 B-Roll Sequencing Block — paste verbatim

> Important b-roll sequencing: No reverse-mortgage or program reference appears on screen until
> the voiceover specifically introduces it. During the hook and reframe beats, the camera stays
> on the creator — no on-screen "reverse mortgage" / "HECM" text, no document props, no money or
> lender imagery, no decorative cutaways of the house. The program is only referenced visually at
> the exact moment the voiceover earns it.

Principle: tie program visibility to a specific line of voiceover. In chunked production, **omit
the reveal asset from any chunk where it should not appear** — a hard lock the AI cannot override.
At **TOF this means no program reveal in any chunk** (enforces the no-product-in-TOF rule).

### 3.4 UGC Realism Block — paste verbatim

> Important UGC realism direction: This is a casually filmed video. The phone is propped somewhere
> off-camera, so both hands are free throughout. Natural handheld jitter and small micro-movements
> give it a self-filmed feel. The creator gestures naturally with both hands, shifts weight, and
> speaks like they are telling a friend something useful. Never frozen in a still pose, never hands
> in pockets or behind the back. The energy is "I want to tell you something," not "I am posing for
> a commercial." Warm and calm, never hyped or salesy.

### 3.5 Clean Frame + Audio Block — paste verbatim

AI video models render text badly (warped, misspelled) and invent uncontrolled background music.
Both read as "AI ad" and break the UGC feel. So the model renders **no** text and **no** music;
captions and the CTA are burned in by the editor in post, and audio is the creator's voice plus
quiet room tone.

> Important clean-frame and audio direction: Do not render any text in the frame — no captions,
> subtitles, titles, lower-thirds, watermarks, logos, or written words of any kind anywhere in the
> video. Audio is only the creator's natural speaking voice with quiet, real room tone. No
> background music, no soundtrack, no score, no sound effects, no musical sting.

Principle: name the AI's default failures (garbled on-screen text, generic stock music) and
forbid them. Document the intended captions/CTA text separately for the editor — never as an
`On-screen text:` instruction inside the prompt, which the model will try to render.

## 4. Character lock (paste verbatim into every chunk)

Write once, paste into every chunk so the same creator + setting carries across generations.

> [CREATOR: a [GENDER] retired homeowner, warm and credible, [HAIR/APPEARANCE], wearing
> [OUTFIT]. Calm, dignified, in-control energy.] [SETTING: [ROOM] with [LIGHTING].]

- **Talent:** credible retired homeowner by default; for some archetypes an adult child or a
  trusted advisor surrogate fits (e.g. Legacy Planner heirs angle). Choose to match the concept.
- **Dignity standard:** comfortable, capable, at ease — never frail, distressed, or pitied.
- **Demographic variation across a campaign:** rotate credible retired-homeowner profiles and at
  least one advisor/adult-child variation. (The source's 19–45 beauty spread does **not** apply.)
- **No age in copy.** Talent depiction is a visual fact; never state an age in voiceover or on-screen text.

## 5. Asset tagging = stage discipline

The source uses `@[product asset]` to control when the product appears. RM has no product, so the
controlled asset is the **program reveal** (on-screen text card or document prop named e.g.
`@guide` / `@card`).

- Include the reveal asset **only** in the chunk(s) where the voiceover earns the concept.
- **TOF:** never include a reveal asset in any chunk — the program does not exist yet on screen.
- **MOF/BOF:** include it at the mechanism reveal only.

| Format | Chunks | Reveal-asset pattern (MOF/BOF) | Reveal-asset pattern (TOF) |
|--------|--------|--------------------------------|----------------------------|
| Mid-Funnel | 3 | NO, YES, NO | NO, NO, NO |
| Full Stack | 5 | NO, NO, NO, YES, NO | NO, NO, NO, NO, NO |

## 6. Prompt skeletons

### 6.1 Standard production skeleton (single continuous prompt)

Deliverable is a clean prose prompt block — no headers, tables, or notes inside it.

```
Create a UGC-style reverse-mortgage ad. The creator is [CHARACTER LOCK]. Natural, real, casually
filmed look in [SETTING WITH LIGHTING].

[SUBJECT / SETTING REALISM BLOCK]
[CONCEPT-REVEAL BLOCK]
[B-ROLL SEQUENCING BLOCK]
[UGC REALISM BLOCK]
[CLEAN FRAME + AUDIO BLOCK]

Camera style: [CAMERA DIRECTION — natural handheld, subtle drift, motivated cuts only].
[SCENE COUNT AND PACING NOTE — 2–3 scenes; warm, calm, no hype.]

Here's the full script:
"[VOICEOVER SCRIPT]"
```

### 6.2 Chunked production skeleton (stitch in post)

Use when generating clips in chunks with the same creator/setting. Paste the **character lock**
and all **five direction blocks** (incl. 3.5 Clean Frame + Audio) into every chunk. Then per chunk:

- Chunk number + beat label (Hook / Reframe / Mechanism / Payoff / CTA)
- Voiceover text (verbatim from the script)
- Estimated runtime (seconds)
- Reveal-asset inclusion (YES/NO per §5) — controls program visibility
- Visual direction (angle, gesture timing, what the creator is doing)
- Continuity notes (outfit, hair, setting, lighting, position to match)
- Captions/CTA text are documented separately for the editor (never as an `On-screen text:` line in the prompt — see §3.5)

## 7. Chunk breakdown templates

### 7.1 Mid-Funnel — 3 chunks (18–22s)

- **Chunk 1 — Hook + Reframe.** 5–7s. Reveal asset: **NO**. Talking-to-camera in primary setting, both hands free, natural gestures, no program reference visible. Establishes the baseline (outfit, hair, lighting, position).
- **Chunk 2 — Mechanism + Reveal.** 8–10s. Reveal asset: **YES** (MOF/BOF only). New angle motivated by movement (creator turns to the kitchen table / gestures to an on-screen card). The concept lands with the tactile analogy. Calm, dignified reveal — no money/lender imagery.
- **Chunk 3 — Payoff + Soft CTA.** 5–6s. Reveal asset: **NO**. Return to talking-to-camera, bookend Chunk 1 framing, soft genuine smile on payoff, subtle downward gesture on CTA.

Stitching: natural seam between Chunk 1 and 2. Chunk 2 is hardest to drop (carries the reveal); Chunks 1/3 are easier to regenerate.

### 7.2 Full Stack — 5 chunks (28–32s)

- **Chunk 1 — Hook.** 5–6s. Reveal: **NO**. Talking-to-camera, steady eye contact, lived-in setting behind. Locks baseline.
- **Chunk 2 — Reframe part 1.** 5–6s. Reveal: **NO**. Same shot, slight angle shift / subtle drift. Dismissive gesture on the failed Debt-frame attempts.
- **Chunk 3 — Reframe part 2 (the structural truth).** 5–6s. Reveal: **NO**. Continuous talking-to-camera; this is where the hook tension peaks before the idea is introduced.
- **Chunk 4 — Mechanism + Reveal.** 8–10s. Reveal: **YES** (MOF/BOF). New angle motivated by movement; phone propped; the analogy lands; dignified concept reveal, no money/lender imagery.
- **Chunk 5 — Payoff + Soft CTA.** 5–6s. Reveal: **NO**. Bookend Chunk 1 framing; earned smile; downward gesture on CTA.

Stitching: natural seam between Chunk 3 and 4. Chunks 1/2/3/5 are talking-to-camera in the primary setting; the bookend (1 ↔ 5) masks small inconsistencies. Chunk 3 is the easiest to fold into Chunk 2 if a generation fails; Chunk 4 is hardest to regenerate (plan extra time).

## 8. Camera, b-roll, and failure-mode standards

- **Constant motion.** Every shot moves: natural handheld jitter on talking-to-camera; subtle drift / micro-push-ins on hands-free; tracking/dolly/reveal on b-roll. No locked-off shots.
- **Visual-to-voiceover sync.** Every visual matches the word being said at that moment.
- **Motivated cuts only.** Cut when the creator moves to do something, when the idea is named (reveal), or for a scripted action. Never cut for decorative furniture/art/establishing shots.
- **Normal speed.** No slow-mo, no speed-ramps.
- **Scene discipline.** Mid-funnel 2 scenes (3 only if VO requires); full stack 3.
- **Setting variation across a campaign:** warm dim kitchen evening, bright morning, soft afternoon side window, lived-in family room, sunlit porch — rotate so the feed isn't repetitive.

### RM-specific failure modes (self-correct on every output)

- Distressed / frail / pitied senior, or crisis tone — violates the dignity standard.
- Cash, money stacks, flying dollars, lender/bank logos, "approved" stamps.
- Program named or shown on screen before the voiceover earns it (and never at TOF).
- Stating or implying an age in voiceover or on-screen text.
- Guarantee language, "tax-free," or false urgency in the script.
- Rambling hooks (narrating the creator's day), choppy two-word phrasing, jargon mechanisms, frozen poses, static b-roll, decorative cutaways, over-formatting the prompt block.
- AI-rendered on-screen text/captions or invented background music — forbid both (§3.5); captions and CTA are burned in by the editor, audio is voice + room tone only.

## 9. PDF → RM mapping (what transferred, changed, or was dropped)

| Source element | RM treatment |
|----------------|--------------|
| Two formats (Full Stack / Mid-Funnel) | **Kept** as-is (runtime/word/beat counts). |
| Universal prompt skeleton (3.1) | **Kept**, RM variables. |
| Skin Direction Block | **Replaced** → Subject / Setting Realism (dignified, in-control "after"). |
| Application Direction Block | **Replaced** → Concept-Reveal (no physical product; no money/lender imagery). |
| B-Roll Sequencing Block | **Kept**, re-pointed at the program reveal / TOF hard-lock. |
| UGC Realism Block | **Kept**, warm/calm RM energy. |
| Reframe pattern (structural-vs-surface) | **Re-pointed** → Debt Frame → Retirement-Tool Frame. |
| `@[product asset]` tagging | **Kept as mechanism**, re-pointed at program reveal = stage discipline. |
| Chunked workflow + chunk templates | **Kept**, RM reveal-asset pattern (incl. all-NO at TOF). |
| Camera/b-roll standards, failure modes | **Kept** + RM-specific failures added. |
| Demographic spread (19–45 beauty) | **Replaced** → credible retired-homeowner + advisor/adult-child variation. |
| Captions / testing (§13–14) | **Optional reference**; defer to existing media-buying SOPs. |
| Compliance | **Added** (source has none) → §10 overlay + the compliance gate. |

## 10. RM compliance overlay (map gate → prompt fields)

Every output passes the [compliance gate](compliance-gate-checklist.md). This maps the gate onto
the prompt so failures are designed out, not caught late.

| Gate item | Where it lives in the prompt |
|-----------|------------------------------|
| No product name in TOF | Voiceover + on-screen text; reveal asset omitted from all TOF chunks (§5). |
| No age in copy | Voiceover + on-screen text; talent depiction is visual only. |
| No guaranteed outcomes | Voiceover wording ("may," "could," "in many cases"). |
| No tax advice | Voiceover wording; no "tax-free" on screen. |
| No false urgency / scarcity | CTA from the approved bank; no "act now" on screen. |
| No fabricated proof | Any number/name is `[TO FILL]` or clearly hypothetical. |
| No pity / distress imagery | Subject/Setting Realism + Concept-Reveal blocks. |
| Program disclosed succinctly, never as headline | Reveal timing in §5/§7 (mechanism beat only, MOF+). |

## 11. Output template

Produce this for each script. The prompt block(s) are clean prose ready to paste into Higgsfield.

```
# Higgsfield Prompt: <ID> — <archetype> / <angle> / <stage>
Format: <Full Stack 28–32s | Mid-Funnel 18–22s> | Delivery: <Standard | Chunked> | Talent: <retired homeowner / advisor / adult-child>

## Voiceover (short UGC)
"<full voiceover script>"

## Prompt(s)
<standard single prompt block — OR — chunk 1..N blocks, each self-contained with character lock + 5 direction blocks (incl. 3.5 Clean Frame + Audio) + reveal-asset YES/NO>

## Frameworks Applied
- Hook: <hook type> | Reframe: Debt → Retirement-Tool | Mechanism: <one-sentence + analogy> | CTA: approved bank
- Reveal-asset pattern: <NO,YES,NO etc.>

## Compliance Gate
A Hard:    PASS / FAIL -> <item>
B Stage:   PASS / FIX
C Quality: PASS (VOC / mechanism / proof / awareness) / DRAFT
D Hygiene: PASS / FIX
RESULT: READY | DRAFT (reason) | HUMAN REVIEW (reason)
```

## Quality escalation

- **Generic** → swap abstract words for VOC (ICP §5); sharpen the tactile analogy.
- **Flat** → reopen the pain→impact pair; write a concrete after-scene, not adjectives.
- **Off-tone** → re-check the dignity standard; remove any hint of pity, hype, or money imagery.

A prompt set that cannot show VOC + mechanism + dignified reveal + stage-matched awareness stays
`draft`, never `final`.
