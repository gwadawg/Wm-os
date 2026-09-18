---
name: rm-creative-studio
description: >-
  Brainstorm reverse-mortgage (RM / HECM / HomeSafe) ad ideas and write compliant
  video ad scripts for RM client fulfillment only. Use when the user names reverse
  mortgage, RM, HECM, HomeSafe, or retired-homeowner client Meta video ads.
  Do NOT use for DSCR, Waiz agency ads, or bare "write an ad script" without an RM
  product signal — route DSCR to dscr-creative-studio + wm-creative.
  After script lock, hand off to wm-creative (Arcads); Higgsfield is retired.
  Statics: ai-rm-ad-image-creation-sop or wm-static-studio. Research: creative-research.
---

# RM Creative Studio

Plan and write **reverse-mortgage** client ads. Two jobs: **brainstorm** and
**compliant video scripts** — then hand off to **wm-creative** for Arcads.

**Product fence:** This skill is **RM only**. If the job is DSCR or Waiz agency,
stop and switch paths. Ask **RM / DSCR / Waiz?** when unset.

## Always load first (knowledge base)

Read these from `docs/client-fulfillment/media-buying/` and siblings:

0. [ad-development-workflow.md](../../../docs/client-fulfillment/media-buying/ad-development-workflow.md) — retrieval order + Step 0 contract.
0b. [script-archetypes-catalog.md](../../../docs/client-fulfillment/media-buying/creative-research/script-archetypes-catalog.md) + [editing-styles-catalog.md](../../../docs/client-fulfillment/media-buying/creative-research/editing-styles-catalog.md) + recent [swipes/](../../../docs/client-fulfillment/media-buying/creative-research/swipes/) + [losers-log.md](../../../docs/client-fulfillment/media-buying/creative-research/losers-log.md).
0c. [ad-intelligence-bridge.md](../../../docs/operations/ad-intelligence-bridge.md) — when pulling `supabase:ad:{uuid}` from Mr. Waiz.
0d. [ad-creative-manifest.yaml](../../../docs/client-fulfillment/media-buying/ad-creative-manifest.yaml) — Supabase pull index.

Read these from `docs/client-fulfillment/media-buying/creative-studio/`:

1. [frameworks-reference.md](../../../docs/client-fulfillment/media-buying/creative-studio/frameworks-reference.md)
2. [rm-archetypes-canonical.md](../../../docs/client-fulfillment/media-buying/creative-studio/rm-archetypes-canonical.md) — **3 personas × 3 archetypes** (family = trigger; Veteran deprecated)
2b. [rm-creative-taxonomy.md](../../../docs/client-fulfillment/reverse-mortgage-dna/rm-creative-taxonomy.md) — process + day-1 campaign shape (strategy · outcome · stage)
3. [rm-ad-ideation-matrix.md](../../../docs/client-fulfillment/media-buying/creative-studio/rm-ad-ideation-matrix.md)
4. [rm-script-generator.md](../../../docs/client-fulfillment/media-buying/creative-studio/rm-script-generator.md)
5. [compliance-gate-checklist.md](../../../docs/client-fulfillment/media-buying/creative-studio/compliance-gate-checklist.md)
6. [format-rules-video.md](../../../docs/client-fulfillment/media-buying/creative-studio/format-rules-video.md) — T1/T2/E1 rules (load when format ≠ plain UGC)
7. [arcads-handoff.md](../../../docs/client-fulfillment/media-buying/creative-studio/arcads-handoff.md) — Step 4 packet for wm-creative
7b. [silent-story-ad-playbook.md](../../../docs/client-fulfillment/media-buying/creative-studio/silent-story-ad-playbook.md) — T2 caption-engine (when relevant)

Pull VOC from [intelligence-icp-rm.md](../../../docs/client-fulfillment/reverse-mortgage-dna/intelligence-icp-rm.md)
and structure from [rm-ad-playbook.md](../../../docs/client-fulfillment/client-marketing/rm-ad-playbook.md).
**Product line fit:** [rm-product-lines.md](../../../docs/client-fulfillment/reverse-mortgage-dna/rm-product-lines.md).
Do **not** load [new-hire-mortgage-icp-primer.md](../../../docs/company/new-hire-mortgage-icp-primer.md) — team training only; it dilutes RM VOC.

Related: [copywriting](../copywriting/SKILL.md) · [marketing-psychology](../marketing-psychology/SKILL.md).  
Do **not** use [ugc-scriptwriter](../ugc-scriptwriter/SKILL.md) for RM client ads.

## Ad Build Flow (default)

Gated flow in chat; **pause after every step**. No files until explicit save.

### Step 0 — Pull proven patterns
0. Confirm **RM** product line (HECM vs HomeSafe) via rm-product-lines. Reject if user meant DSCR.
1. Read ad-development-workflow retrieval order.
2. Scan catalogs + 2–3 swipes (or `supabase:ad:{uuid}`).
3. State **"Patterns I'm building from:"** with citations.
4. Name the **gap** → ideation seed.
5. Pause if user said "pull from winners first."

### Step 1 — Concept
1. Minimal inputs: archetype, angle + stage, format (UGC / T1 / T2 / E1 / …), count N.
2. Generate via ideation matrix; anti-overlap rule.
3. Present table + compliance flag.
4. Pause: "Reply with the concept # to script…"

### Step 2 — Script
1. Five beats per script generator (Hook → Empathy → Frame Shift → Proof → CTA).
2. VOC for Empathy; mechanism for Frame Shift; top objection for Proof; 2–3 hooks.
3. Show Script + Frameworks Applied + Compliance Gate (+ Video Brief).
4. Pause.

### Step 3 — Lock script
Iterate until user locks. Do not advance until locked.

### Step 4 — Arcads handoff (not a render step)
1. Apply [format-rules-video.md](../../../docs/client-fulfillment/media-buying/creative-studio/format-rules-video.md) for T1/T2/E1 (dramatization, B-Roll plan).
2. Build the packet from [arcads-handoff.md](../../../docs/client-fulfillment/media-buying/creative-studio/arcads-handoff.md).
3. Show inline; iterate Editor Notes if needed.
4. End with: **Continue in wm-creative** — product_line RM → dialogue gate → credit gate → Arcads (default 2 variants).

### Save (only on explicit request)
One file: `docs/client-fulfillment/media-buying/creative-studio/outputs/rm-<archetype>-<angle>-<date>.md`  
Contents: Concept + final Script + **Arcads handoff** + Compliance gate.

## Shortcuts

- **`brainstorm`** — Step 1 (`cold-batch`, `objection-batch`, `winner-expand`, `persona-deep`)
- **`script`** — Step 2
- **`handoff`** / **`prompt`** — Step 4 packet only (alias `prompt` kept for habit)
- **`vary`** — five genuine variations (F7 methods)

## File Policy

Stay in chat through Steps 0–4. One consolidated file only on explicit save.

## Non-negotiables

- Compliance gate on every output.
- No age in copy; no product name in TOF; no guarantees / tax claims / false urgency; no fabricated proof.
- Frameworks Applied on every script.
- Generic RM only — `[TO FILL]` for client specifics.
- **Never** load or produce Higgsfield prompts.

## Related

- Produce video: sibling repo **wm-creative** (`wm-arcads-studio`)
- Statics: [ai-rm-ad-image-creation-sop.md](../../../docs/client-fulfillment/media-buying/ai-rm-ad-image-creation-sop.md) or wm-creative `wm-static-studio`
- Research: [creative-research/](../../../docs/client-fulfillment/media-buying/creative-research/)
- DSCR equivalent: [dscr-creative-studio](../dscr-creative-studio/SKILL.md) (rulebook: [dscr-video-script-playbook.md](../../../docs/client-fulfillment/dscr-dna/dscr-video-script-playbook.md))
