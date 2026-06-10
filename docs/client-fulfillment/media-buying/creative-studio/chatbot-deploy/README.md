---
title: RM Creative Studio — Team Chatbot Deploy Kit
domain: client-fulfillment
owner: media-buying-lead
status: draft
last_updated: 2026-06-10
review_cycle: monthly
artifact_type: sop
---

# RM Creative Studio — Team Chatbot Deploy Kit

A no-code way to give the team the [Creative Studio](../README.md) as a chatbot they can open and
chat with. It runs the same gated 4-step flow (Concept → Script → Reiterate → Higgsfield prompt)
with the compliance gate built in, across all four creative formats: **UGC, spoken testimonial,
silent text-overlay testimonial, and educational / explainer** (with B-Roll Sourcing Plan).

**The repo stays the single source of truth.** The chatbot is just a delivery surface — a *copy* of
these docs loaded into an assistant. When you change a doc here, you re-upload it (see
[Keeping it in sync](#keeping-it-in-sync)).

## What you'll set up

- **Instructions:** the contents of [system-instructions.md](system-instructions.md) (everything
  below its divider line), pasted into the assistant's instructions field.
- **Knowledge files:** the eight canonical docs below, uploaded as the assistant's knowledge base.

## Files to upload as knowledge

Upload these exact files (they already live in the repo — don't make copies):

| # | File | Repo path |
|---|------|-----------|
| 1 | frameworks-reference | `docs/client-fulfillment/media-buying/creative-studio/frameworks-reference.md` |
| 2 | rm-archetypes-canonical | `docs/client-fulfillment/media-buying/creative-studio/rm-archetypes-canonical.md` |
| 3 | rm-ad-ideation-matrix | `docs/client-fulfillment/media-buying/creative-studio/rm-ad-ideation-matrix.md` |
| 4 | rm-script-generator | `docs/client-fulfillment/media-buying/creative-studio/rm-script-generator.md` |
| 5 | compliance-gate-checklist | `docs/client-fulfillment/media-buying/creative-studio/compliance-gate-checklist.md` |
| 6 | higgsfield-prompt-builder | `docs/client-fulfillment/media-buying/creative-studio/higgsfield-prompt-builder.md` |
| 7 | higgsfield-format-modules | `docs/client-fulfillment/media-buying/creative-studio/higgsfield-format-modules.md` |
| 8 | intelligence-icp-rm | `docs/client-fulfillment/reverse-mortgage-dna/intelligence-icp-rm.md` |

Optional extras (recommended once the basics work): `rm-compliance-guardrails.md` (the binding
founder-owned compliance source) and 1–2 known-good examples from
[outputs/](../outputs/) as few-shot references.

The internal markdown links inside these files won't click through inside the assistant — that's
fine. The assistant reads their **content**, not their links.

> Do **not** upload `SKILL.md` — its flow is already rewritten into `system-instructions.md` for a
> standalone assistant. Uploading both would create conflicting instructions.

## Setup — Claude Project (recommended)

The studio was authored in Claude's skill format, so a Claude Project is the most faithful match.

1. In Claude (Team or Enterprise plan, so you can share), create a **new Project** named
   `RM Creative Studio`.
2. Open **Project instructions** and paste everything below the divider in
   [system-instructions.md](system-instructions.md).
3. In **Project knowledge**, upload the eight files from the table above.
4. Test it (see [Test script](#test-script)).
5. Share the Project with the team (Projects are shareable within a Claude Team workspace).

## Setup — Custom GPT (ChatGPT alternative)

1. In ChatGPT (Team/Enterprise to share), go to **Explore GPTs → Create**.
2. In **Configure → Instructions**, paste everything below the divider in
   [system-instructions.md](system-instructions.md).
3. Under **Knowledge**, upload the eight files from the table above.
4. Turn **off** "Web Browsing" and "Code Interpreter" — this assistant only needs its knowledge.
5. Test it, then set sharing to **Anyone in my workspace** (or a shared link).

## Test script

Confirm the gate behavior before sharing. In a fresh chat, send:

1. `Let's make a new RM ad` → it should ask only for archetype, angle/stage, format, and count,
   then **stop**.
2. `any archetype, TOF, UGC, 3 concepts` → it should return a 3-row concept table with compliance
   flags, then **stop** and ask for a concept number.
3. Pick a concept → it should return a full 5-part script + Frameworks Applied + Compliance Gate,
   then **stop**.
4. `looks good, lock it` → it advances to the Higgsfield prompt step and **stops** for iteration.

Then confirm the format routing:

5. `Make a spoken testimonial ad, Financially Squeezed, MOF` → the script should be a past-tense
   story with a doubt beat; the final output must carry `Story type: Composite (dramatization)`
   and the disclosure line in Editor Notes, with **no result dollar figures**.
6. `Make an educational ad, myth-bust, MOF` → the prompt step must include a **B-Roll Sourcing
   Plan** table (GENERATE / SOURCE / EDITOR per scene) with stock search terms + licensing flags
   on SOURCE rows, and prompt chunks only for GENERATE rows.
7. `Make a silent text-overlay testimonial, TOF` → no voiceover; per-scene b-roll prompts (no one
   speaks to camera) + a caption table in Editor Notes; no product name anywhere.

If it ever runs multiple steps without pausing, names the product at TOF, or outputs a testimonial
without the dramatization disclosure, re-paste the instructions — something didn't save.

## Keeping it in sync

The chatbot's knowledge is a snapshot. Whenever you update one of the eight canonical docs (or the
flow in `system-instructions.md`) in this repo:

1. Re-upload the changed file(s) to the Project / GPT knowledge (replace the old version).
2. If you changed `system-instructions.md`, re-paste the instructions field.

Set a recurring reminder (monthly, matching the studio's review cycle) to reconcile the uploaded
knowledge against the repo.

## Limits to know

- It's a **copy**, so it drifts from the repo until you re-upload. For always-in-sync, the next step
  up is a custom web app that reads `docs/` at runtime.
- It **cannot save files** to the repo. When an ad is locked, it hands the team one consolidated
  copy-paste block to drop into [outputs/](../outputs/) themselves.
- Compliance still needs a human eye. The gate is a guardrail, not a sign-off — anything marked
  FAIL/HUMAN REVIEW goes to the media-buying lead.

## Related

- The studio itself: [creative-studio/README.md](../README.md)
- The skill (source of the flow): [rm-creative-studio SKILL.md](../../../../../.claude/skills/rm-creative-studio/SKILL.md)
- Future auto-render agent: [FUTURE-video-agent-spec.md](../FUTURE-video-agent-spec.md)
