---
name: dscr-creative-studio
description: >-
  Brainstorm DSCR refinance (investor, business-purpose) ad ideas and write
  compliant video ad scripts for DSCR client fulfillment only. Use when the user
  names DSCR, DSCR refi, investor refinance, rental-property cash-out, or
  real-estate-investor client Meta video ads. Do NOT use for reverse mortgage,
  Waiz agency ads, or bare "write an ad script" without a DSCR product signal —
  route RM to rm-creative-studio. After script lock, hand off to wm-creative
  (Arcads). Statics: dscr-static-image-generator-project or wm-static-studio.
---

# DSCR Creative Studio

Plan and write **DSCR refinance** client ads. Two jobs: **brainstorm** and
**compliant video scripts** — then hand off to **wm-creative** for Arcads.

**Product fence:** This skill is **DSCR only**. If the job is RM or Waiz
agency, stop and switch paths. Ask **RM / DSCR / Waiz?** when unset.

Canonical SOP for beats, fence, and handoff shape:
[dscr-video-script-playbook.md](../../../docs/client-fulfillment/dscr-dna/dscr-video-script-playbook.md).
This skill is the entry point and gated flow; the playbook is the rulebook.

## Always load first (knowledge base)

DSCR doctrine is **two files for ideation**. Do not load the whole `dscr-dna/`
folder into a creative prompt. Do **not** load
[new-hire-mortgage-icp-primer.md](../../../docs/company/new-hire-mortgage-icp-primer.md).
Do **not** load nurture drips, setter scripts, or campaign-architecture docs
into the creative prompt.

1. [intelligence-icp-dscr.md](../../../docs/client-fulfillment/dscr-dna/intelligence-icp-dscr.md)
   — who, product, NEVER, creative bar. Proven angles are a starting slate,
   not a closed menu.
2. [dscr-creative-taxonomy.md](../../../docs/client-fulfillment/dscr-dna/dscr-creative-taxonomy.md)
   — **buckets (DENIED / DEADLINE / IDLE / IN-MARKET), creative jobs, angle
   map, labeling.** Use this for naming and sorting every concept.
3. [dscr-video-script-playbook.md](../../../docs/client-fulfillment/dscr-dna/dscr-video-script-playbook.md)
   — beats, word budget, handoff packet.

**After a direction is chosen** (not before):

4. [dscr-campaign-master-angles.md](../../../docs/client-fulfillment/dscr-dna/dscr-campaign-master-angles.md)
   — expand a *winning* proven angle; MOF / BOF tokens.
5. [dscr-gtm-positioning-brief.md](../../../docs/client-fulfillment/dscr-dna/dscr-gtm-positioning-brief.md)
   — beachhead, test waves.

**Before ship (gate):**

6. [dscr-compliance-guardrails.md](../../../docs/client-fulfillment/dscr-dna/dscr-compliance-guardrails.md)

Optional pattern pull: Mr. Waiz `ad_library` with `product=dscr` via
[ad-intelligence-bridge.md](../../../docs/operations/ad-intelligence-bridge.md).
If a row's `summary` is thin, **ask** — do not invent hooks or KPIs.

Related: [copywriting](../copywriting/SKILL.md) ·
[marketing-psychology](../marketing-psychology/SKILL.md).
Do **not** use [rm-creative-studio](../rm-creative-studio/SKILL.md) (RM
archetypes, RM VOC, HECM compliance) or
[ugc-scriptwriter](../ugc-scriptwriter/SKILL.md) (no compliance gate) for DSCR
client ads.

## Ad Build Flow (default)

Gated flow in chat; **pause after every step**. No files until explicit save.

### Step 0 — Confirm + patterns
0. Confirm **DSCR** (investor refinance, business-purpose). Reject if user
   meant RM or Waiz.
1. Load ICP file only. State **"Patterns I'm building from:"** — ICP slate
   angles and, if pulled, Mr. Waiz DSCR winners with citations.
2. Name the **gap** → ideation seed.
3. Pause if user said "pull from winners first."

### Step 1 — Concept
1. Minimal inputs: **bucket** (DENIED / DEADLINE / IDLE / IN-MARKET), angle
   (from ICP slate or new inside NEVER), creative job, stage
   (cold / warm), format (UGC talking head default), count N.
2. Present short concept table with `bucket · job · slug · angle` +
   compliance flag per row.
3. Pause: "Reply with the concept # to script…"

### Step 2 — Script
1. Beats per playbook: **Hook → Problem → Mechanism → Proof → CTA**.
   Default ~10–15s speakable (~2.5 wps) for Arcads UGC; longer only if asked.
2. Hook from investor world / myth / operator pain — never an LO sales open.
   Mechanism = one plain how-it-works line. Proof real or clearly
   hypothetical; **no fabricated testimonials**.
3. Show Script + Angle/Stage + Compliance Gate (against
   dscr-compliance-guardrails) + 2–3 alt hooks.
4. Pause.

### Step 3 — Lock script
Iterate until user locks. Do not advance until locked.

### Step 4 — Arcads handoff (not a render step)
1. Build the packet using the **DSCR** shape in the playbook (`product_line:
   DSCR`, format, stage / angle, compliance PASS, locked dialogue, production
   notes).
2. Show inline; iterate notes if needed.
3. End with: **Continue in wm-creative** — product_line DSCR → talent refs →
   dialogue gate → credit gate → Arcads (default 2 variants). Prefer
   service / operator UGC; no CPG "holds the bottle" unless a real prop exists.

### Save (only on explicit request)
One file: `docs/client-fulfillment/media-buying/creative-studio/outputs/dscr-<angle>-<stage>-<date>.md`
Contents: Concept + final Script + **Arcads handoff** + Compliance gate.

## Shortcuts

- **`brainstorm`** — Step 1 (`cold-batch`, `objection-batch`, `winner-expand`)
- **`script`** — Step 2
- **`handoff`** — Step 4 packet only
- **`vary`** — genuine variations (new hook, new proof angle, new stage) — not
  synonyms

## Non-negotiables

- Compliance gate on every output; guardrails loaded before anything ships.
- No guarantees, no illegal rate / approval promises, no fabricated proof.
- Stay inside the ICP **NEVER** list. Thin claims → ask, do not invent.
- No RM VOC ("retired homeowners", HECM, FHA non-recourse) in DSCR copy.
- Generic DSCR only — `[TO FILL]` for client specifics.
- **Never** load or produce Higgsfield prompts.

## Related

- Produce video: sibling repo **wm-creative** (`wm-arcads-studio`)
- Statics: [dscr-static-image-generator-project.md](../../../docs/client-fulfillment/dscr-dna/dscr-static-image-generator-project.md)
  or wm-creative `wm-static-studio`
- DSCR hub: [dscr-dna/README.md](../../../docs/client-fulfillment/dscr-dna/README.md)
- RM equivalent: [rm-creative-studio](../rm-creative-studio/SKILL.md)
