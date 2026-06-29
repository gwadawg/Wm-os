---
title: RM Fulfillment Assistant — Team Chatbot Deploy Kit
domain: client-fulfillment
owner: client-success
status: active
last_updated: 2026-06-22
review_cycle: monthly
artifact_type: sop
---

# RM Fulfillment Assistant — Team Chatbot Deploy Kit

A no-code way to give the fulfillment team an assistant for reverse mortgage **client delivery**:
copy, drips, bot behavior, objections, lifecycle, and sub-agent design.

**The repo stays the single source of truth.** The Claude Project is a delivery surface — a copy of
these docs loaded into an assistant. When you change a doc here, re-upload it (see
[Keeping it in sync](#keeping-it-in-sync)).

**Not the same as [RM Creative Studio](../../media-buying/creative-studio/chatbot-deploy/README.md)** —
that project is gated 4-step **video ad** creation only. Use both.

## What you'll set up

- **Instructions:** contents of [system-instructions.md](system-instructions.md) (everything below its divider line)
- **Knowledge files:** Tier 1 bundle below (13 files)

## Files to upload as knowledge (Tier 1)

Upload these exact files from the repo — don't make copies:

| # | File | Repo path |
|---|------|-----------|
| 1 | rm-compliance-guardrails | `docs/client-fulfillment/reverse-mortgage-dna/rm-compliance-guardrails.md` |
| 2 | doctrine-reverse-mortgage | `docs/client-fulfillment/reverse-mortgage-dna/doctrine-reverse-mortgage.md` |
| 3 | doctrine-rm-marketing | `docs/client-fulfillment/reverse-mortgage-dna/doctrine-rm-marketing.md` |
| 4 | intelligence-icp-rm | `docs/client-fulfillment/reverse-mortgage-dna/intelligence-icp-rm.md` |
| 5 | intelligence-rm-product | `docs/client-fulfillment/reverse-mortgage-dna/intelligence-rm-product.md` |
| 6 | rm-borrower-objections | `docs/client-fulfillment/reverse-mortgage-dna/rm-borrower-objections.md` |
| 7 | rm-high-quality-lead-acquisition | `docs/client-fulfillment/client-marketing/rm-high-quality-lead-acquisition.md` |
| 8 | fulfillment-lead-lifecycle | `docs/client-fulfillment/fulfillment-lead-lifecycle.md` |
| 9 | how-wm-ai-bot-works | `docs/client-fulfillment/crm-architecture/how-wm-ai-bot-works.md` |
| 10 | how-claimed-tag-works | `docs/client-fulfillment/crm-architecture/how-claimed-tag-works.md` |
| 11 | rm-imessage-intent-drip-7day | `docs/client-fulfillment/client-marketing/rm-imessage-intent-drip-7day.md` |
| 12 | script-appointment-setting-call | `docs/client-fulfillment/call-center/script-appointment-setting-call.md` |
| 13 | waiz-vs-client-marketing-boundaries | `docs/client-fulfillment/waiz-vs-client-marketing-boundaries.md` |

Machine-readable index: [knowledge-manifest.yaml](knowledge-manifest.yaml)

### Tier 2 optional (add when project has room)

| File | Repo path |
|------|-----------|
| rm-imessage-appointment-followup | `docs/client-fulfillment/client-marketing/rm-imessage-appointment-followup.md` |
| rm-imessage-second-booking-followup | `docs/client-fulfillment/client-marketing/rm-imessage-second-booking-followup.md` |
| ad-copy-angle-library-rm | `docs/client-fulfillment/media-buying/ad-copy-angle-library-rm.md` |
| constraint-troubleshooting-sop | `docs/client-fulfillment/client-success/constraint-troubleshooting-sop.md` |

> Do **not** upload `.claude/skills/rm-fulfillment-agent/SKILL.md` — its flow is rewritten into
> `system-instructions.md` for the standalone assistant.

## Setup — Claude Project

1. In Claude (Team or Enterprise), create a **new Project** named **`RM Fulfillment Assistant — Waiz`**.
2. Open **Project instructions** and paste everything below the divider in [system-instructions.md](system-instructions.md).
3. In **Project knowledge**, upload the 13 Tier 1 files from the table above.
4. Turn **off** Web Browsing and Code Interpreter — this assistant only needs its knowledge.
5. Run the [test script](test-validation.md) in a fresh chat.
6. Share the Project with the fulfillment team.

## Test script

Run all five prompts from [test-validation.md](test-validation.md) before sharing. Each includes pass criteria.

## Keeping it in sync

Whenever you update a Tier 1 doc, `system-instructions.md`, or `rm-borrower-objections.md`:

1. Re-upload the changed file(s) to Project knowledge (replace the old version).
2. If you changed `system-instructions.md`, re-paste the instructions field.

Set a recurring reminder (monthly) to reconcile uploaded knowledge against the repo.

## Limits to know

- It's a **copy** — it drifts until you re-upload. For always-in-sync, use the repo skill in Cursor.
- It **cannot save files** to the repo. Team copies approved outputs into GHL or docs manually.
- Compliance still needs a human eye. HUMAN REVIEW outputs go to client success or founder.

## Related

- Agent hub: [reverse-mortgage-agent/README.md](../README.md)
- RM Creative Studio (video ads): [creative-studio/chatbot-deploy/README.md](../../media-buying/creative-studio/chatbot-deploy/README.md)
- Repo skill: [.claude/skills/rm-fulfillment-agent/SKILL.md](../../../../.claude/skills/rm-fulfillment-agent/SKILL.md)
