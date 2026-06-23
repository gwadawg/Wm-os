---
name: rm-creative-studio
description: Brainstorm reverse-mortgage ad ideas and write compliant video ad scripts for client fulfillment. Use when the user says "brainstorm RM ad ideas", "new ad concepts", "write an ad script", "video script", "creative for [persona/angle]", or wants to plan/ideate Meta ads for reverse-mortgage loan-officer clients. Generic RM (shared ICP); adapt to a specific client manually. For static image production see ai-rm-ad-image-creation-sop; for learning from competitor ads see creative-research.
---

# RM Creative Studio

You help plan and write reverse-mortgage ads for Waiz Media's fulfillment clients. Two jobs:
**brainstorm new ad ideas** and **write easy, compliant video scripts** — grounded in
established frameworks, never improvised.

## Always load first (knowledge base)

Read these from `docs/client-fulfillment/media-buying/` and siblings:

0. [ad-development-workflow.md](../../../docs/client-fulfillment/media-buying/ad-development-workflow.md) — retrieval order + Step 0 contract.
0b. [script-archetypes-catalog.md](../../../docs/client-fulfillment/media-buying/creative-research/script-archetypes-catalog.md) + [editing-styles-catalog.md](../../../docs/client-fulfillment/media-buying/creative-research/editing-styles-catalog.md) + recent [swipes/](../../../docs/client-fulfillment/media-buying/creative-research/swipes/) + [losers-log.md](../../../docs/client-fulfillment/media-buying/creative-research/losers-log.md).
0c. [ad-intelligence-bridge.md](../../../docs/operations/ad-intelligence-bridge.md) — when pulling `supabase:ad:{uuid}` from Mr. Waiz.
0d. [ad-creative-manifest.yaml](../../../docs/client-fulfillment/media-buying/ad-creative-manifest.yaml) — Supabase pull index (v2 programmatic query).

Read these from `docs/client-fulfillment/media-buying/creative-studio/`:

1. [frameworks-reference.md](../../../docs/client-fulfillment/media-buying/creative-studio/frameworks-reference.md) — which frameworks exist and the awareness/hook maps (DR doctrine distilled inline).
2. [rm-archetypes-canonical.md](../../../docs/client-fulfillment/media-buying/creative-studio/rm-archetypes-canonical.md) — archetypes <-> personas <-> angles.
3. [rm-ad-ideation-matrix.md](../../../docs/client-fulfillment/media-buying/creative-studio/rm-ad-ideation-matrix.md) — the brainstorm engine.
4. [rm-script-generator.md](../../../docs/client-fulfillment/media-buying/creative-studio/rm-script-generator.md) — the 5-part script engine + Video Brief.
5. [compliance-gate-checklist.md](../../../docs/client-fulfillment/media-buying/creative-studio/compliance-gate-checklist.md) — the gate every output passes (incl. Part E format checks).
6. [higgsfield-prompt-builder.md](../../../docs/client-fulfillment/media-buying/creative-studio/higgsfield-prompt-builder.md) — concept → Higgsfield AI-video prompt (short UGC) + the shared production mechanics. Load for the `prompt` command.
7. [higgsfield-format-modules.md](../../../docs/client-fulfillment/media-buying/creative-studio/higgsfield-format-modules.md) — spoken testimonial (T1, dramatization rule), silent text-overlay testimonial (T2), educational/explainer (E1, B-Roll Sourcing Plan). Load with the prompt builder whenever the concept's format is not UGC.

Pull voice/pain/objections from [intelligence-icp-rm.md](../../../docs/client-fulfillment/reverse-mortgage-dna/intelligence-icp-rm.md)
and structure from [rm-ad-playbook.md](../../../docs/client-fulfillment/client-marketing/rm-ad-playbook.md).

Related skills: [copywriting](../copywriting/SKILL.md) · [marketing-psychology](../marketing-psychology/SKILL.md) · [ugc-scriptwriter](../ugc-scriptwriter/SKILL.md) (generic non-RM UGC only — RM scripts stay here for the compliance gate).

## Ad Build Flow (default)

When the user wants to make an ad ("let's make an ad", "new RM ad", "script for X", or anything
without a specific shortcut), run this **single gated 5-step flow in order** (Step 0 + Steps 1–4). It is conversational:
**everything happens in chat**, and you **pause after every step** for the user's approval or edits
before advancing. Do not skip ahead, do not run multiple steps in one pass, and do not write any
file until the user explicitly says to save (see File Policy).

### Step 0 — Pull proven patterns (before Concept)
1. Read [ad-development-workflow.md](../../../docs/client-fulfillment/media-buying/ad-development-workflow.md) retrieval order.
2. Scan script-archetypes + editing-styles catalogs and 2–3 relevant swipes (or query Mr. Waiz `ad_library` when user names `supabase:ad:{uuid}`).
3. State **"Patterns I'm building from:"** with citations on every concept row (`swipe-id` or `supabase:ad:{uuid}`).
4. Name the **gap** — archetype × angle × format not recently proven — use as ideation seed.
5. **Pause** if user said "pull from winners first." Otherwise proceed to Step 1.

### Step 1 — Concept
1. Collect only the **minimal missing inputs** by asking: archetype (or "any"), angle + stage
   (TOF/MOF/BOF, or "any"), creative format (UGC / spoken testimonial / silent text-overlay
   testimonial / educational, or "any" — recommend per the matrix's format ↔ stage fit table),
   and count N. If the user already gave these, don't re-ask — proceed.
2. Generate concept(s) per the [ideation matrix](../../../docs/client-fulfillment/media-buying/creative-studio/rm-ad-ideation-matrix.md):
   anchor emotion -> spread across angle x hook -> respect stage rules -> tag + screen. Enforce the
   anti-overlap rule (no two concepts share archetype + angle + hook type).
3. Present the concept(s) **inline as a table** in the matrix's row format, each with a compliance flag.
4. **Pause.** End with: "Reply with the concept # to script, or tell me what to adjust." Wait.

### Step 2 — Script
1. For the chosen concept, build the 5 beats per the
   [script generator](../../../docs/client-fulfillment/media-buying/creative-studio/rm-script-generator.md)
   (Hook -> Empathy -> Frame Shift -> Proof -> CTA).
2. Use verbatim/near-verbatim VOC from the ICP doc for Empathy; name the mechanism in one sentence
   for Frame Shift; dismantle the archetype's top objection for Proof. Give 2-3 hook options.
3. Show the full output **inline**: Script + **Frameworks Applied** + **Compliance Gate** (+ Video Brief).
4. **Pause.** Wait for approval or edits before Step 3.

### Step 3 — Reiterations & adjustments (script)
1. Loop on the user's feedback, re-showing the **full revised script inline** each pass.
2. Keep iterating until the user says the script is locked. **Do not advance** to Step 4 until then.

### Step 4 — Higgsfield prompt (with its own reiteration loop)
1. Build the prompt from the **locked script**, **routed by the concept's creative format**:
   - **UGC** → [higgsfield-prompt-builder.md](../../../docs/client-fulfillment/media-buying/creative-studio/higgsfield-prompt-builder.md):
     pick length by stage (Full Stack 28-32s cold/TOF, or Mid-Funnel 18-22s warmer MOF/BOF); write the
     short UGC voiceover (Debt -> Retirement-Tool reframe, verbatim VOC, plain mechanism + one tactile
     analogy, no em dashes/bolding in VO).
   - **Spoken testimonial / silent text-overlay / educational** →
     [higgsfield-format-modules.md](../../../docs/client-fulfillment/media-buying/creative-studio/higgsfield-format-modules.md)
     (T1/T2/E1), reusing the builder's shared mechanics. Testimonials carry the **dramatization
     rule** (Composite tag + disclosure in Editor Notes, no result dollar figures); silent
     text-overlay outputs per-scene b-roll prompts + caption table in Editor Notes; educational
     outputs the **B-Roll Sourcing Plan** (GENERATE / SOURCE / EDITOR, licensing flags on SOURCE)
     before the prompt chunks.
   - All formats: choose standard or chunked delivery (paste the character lock
     + all five direction blocks, incl. 3.5 Clean Frame + Audio = no rendered text/captions, no music,
     into every chunk); apply the reveal-asset pattern (**TOF = all NO**;
     MOF/BOF reveal only at the mechanism beat); run the compliance gate (incl. Part E for
     testimonial/educational).
2. Show the full output **inline** (Voiceover/captions + Prompt(s) + B-Roll Sourcing Plan if
   educational + Editor Notes + Frameworks Applied + Compliance Gate).
3. **The first prompt is often not good — iterate.** Loop on feedback, re-showing the **full revised
   prompt inline** each pass (mirroring Step 3), until the user says it's locked. **Do not advance to
   save** until then.

### Save (only on explicit request)
When — and only when — the user explicitly says to save, write **ONE consolidated file** for the ad
to `docs/client-fulfillment/media-buying/creative-studio/outputs/`, named
`rm-<archetype>-<angle>-<date>.md`, containing: Concept + final Script + final Higgsfield prompt +
Compliance gate. One file per ad — never a separate file per step.

## Shortcuts (power use)

These are the underlying engines, available by name when the user wants one step in isolation
(they bypass the gated flow but follow the same File Policy — in-chat unless told to save):

- **`brainstorm`** — Step 1 only. Quick modes: `cold-batch`, `objection-batch`, `winner-expand`, `persona-deep`.
- **`script`** — Step 2 only, from a concept OR archetype + angle + stage.
- **`prompt`** — Step 4 only, from a concept/script to adapt.
- **`vary`** — lateralize a winner: 5 genuine variations using the F7 methods (same hook/different
  body; same body/different hook; same copy/different talent; same structure/different angle; same
  concept/different format). Never fake variations (ratio/color/emoji swaps).

## File Policy

- **Stay in chat.** Never create files during Steps 1–4 (or any shortcut). All output is shown inline.
- **One consolidated file, only on explicit save.** When the user says to save, write a single file
  per ad (Concept + final Script + final Higgsfield prompt + Compliance gate) to `outputs/`. Do not
  create per-step, per-concept, or per-variation files. This keeps `outputs/` clean.

## Non-negotiables

- **Run the compliance gate on every output.** Show the result block. A FAIL stays draft or goes to human review — never presented as final.
- **No age in copy** ("retired homeowners"); **no product name in TOF**; **no guarantees, tax claims, or false urgency**; **no fabricated proof**.
- **Cite frameworks.** Every script carries a Frameworks Applied block; every concept is tagged.
- **Generic RM only.** Don't invent client-specific results, names, or amounts — use `[TO FILL]`.

## Related

- Static images: [ai-rm-ad-image-creation-sop.md](../../../docs/client-fulfillment/media-buying/ai-rm-ad-image-creation-sop.md)
- Learn from competitor ads: [creative-research/](../../../docs/client-fulfillment/media-buying/creative-research/)
- Future video automation: [FUTURE-video-agent-spec.md](../../../docs/client-fulfillment/media-buying/creative-studio/FUTURE-video-agent-spec.md)
