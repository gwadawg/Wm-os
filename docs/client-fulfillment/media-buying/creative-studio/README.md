---
title: Creative Studio (RM Ads)
domain: client-fulfillment
owner: media-buying-lead
status: draft
last_updated: 2026-05-30
review_cycle: monthly
artifact_type: sop
---

# Creative Studio (RM Ads)

The outbound creative engine: brainstorm new reverse-mortgage ad ideas and write compliant
video ad scripts for fulfillment clients. Sibling to [creative-research/](../creative-research/)
(inbound: learn from others). Invoked via the
[rm-creative-studio skill](../../../../.claude/skills/rm-creative-studio/SKILL.md).

## What this gives you

- **Brainstorm** ad ideas systematically (not blank-page) across archetype x angle x stage x hook x format.
- **Write** ready-to-shoot 5-part video scripts with a Video Brief for the editor.
- **Build** short-form UGC **Higgsfield AI-video prompts** (standard or chunked) straight from a concept.
- Everything grounded in named frameworks and screened by a compliance gate.

## Folder map

```text
creative-studio/
├── README.md                    ← this file
├── frameworks-reference.md      ← the audit map (which frameworks, where they apply; DR doctrine distilled inline)
├── rm-archetypes-canonical.md   ← archetypes <-> personas <-> angles <-> hooks
├── rm-ad-ideation-matrix.md     ← the brainstorm engine
├── rm-script-generator.md       ← the 5-part script engine + Video Brief (long-form 45-90s)
├── higgsfield-prompt-builder.md ← concept → Higgsfield AI-video prompt (short UGC 18-32s)
├── compliance-gate-checklist.md ← the gate every output passes
├── FUTURE-video-agent-spec.md   ← Layer 2 (auto-render agent) — doc only
└── outputs/                     ← generated idea-batches + scripts land here
```

## How to use it

The default is a **single gated 4-step flow**: each step happens in chat, and the agent pauses
for your approval or edits before moving to the next.

| Step | What happens | Gate |
|------|--------------|------|
| **1. Concept** | The agent asks only for the minimal missing inputs (archetype, angle/stage, count), then shows compliance-flagged concept(s) as a table | Pick a concept # or request changes |
| **2. Script** | Full 5-part script + Frameworks Applied + Compliance Gate (+ Video Brief) for the chosen concept | Approve or edit |
| **3. Reiterations** | Iterate on the script — the full revised script is re-shown each pass — until you lock it | Lock the script |
| **4. Higgsfield prompt** | Short UGC voiceover + paste-ready Higgsfield prompt(s) (standard or chunked) + Compliance Gate, then iterate (the first pass often isn't good) until you lock it | Lock the prompt |

**Conversational by default — no clutter.** Everything stays in chat; the studio writes **one
consolidated file per ad** (concept + final script + final prompt + compliance gate) to
[outputs/](outputs/) only when you explicitly say to save. No per-step or per-concept files.

Shortcuts for one step in isolation (still in-chat unless you save): say `brainstorm`, `script`,
`prompt`, or "give me 5 variations of this winner" (`vary`).

## Quality guarantees (why outputs aren't improvised)

1. Source-cited construction — every rule traces to [frameworks-reference.md](frameworks-reference.md).
2. "Frameworks Applied" block on every script.
3. [Compliance gate](compliance-gate-checklist.md) on every output (hard rules + stage + DR quality rule).
4. Validation pass before the skill is treated as production-ready.

## Scope

- **Generic RM** (shared ICP/angles). Adapt to a specific loan-officer client manually; use `[TO FILL]` for client specifics.
- Static images live in [ai-rm-ad-image-creation-sop.md](../ai-rm-ad-image-creation-sop.md); this studio is video-script-first.

## Status

All files `status: draft` pending founder review and the validation pass.
