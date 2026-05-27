---
name: pre-call-objection-videos
description: >-
  Prospect-facing Waiz nurture videos (URLs, transcripts, objection mapping) for setters,
  closers, ads, and landing pages. Use when sending pre-call video links, writing Hammer-Them
  nurture, ad scripts, landing copy, or handling trust/guarantee/leads/agency objections before
  strategy or demo calls. Read manifest.yaml first.
---

# Pre-Call Objection Video Assets

**Read first:** [pre-call-objection-videos-manifest.yaml](../../../docs/acquisition/marketing/pre-call-objection-videos-manifest.yaml)

| Task | File |
|------|------|
| Index, transcripts, send guidance | [pre-call-objection-videos.md](../../../docs/acquisition/marketing/pre-call-objection-videos.md) |
| Objection taxonomy | [wm-objection-categories.md](../../../docs/acquisition/sales/wm-objection-categories.md) |
| Objection hub | [objection-handling-hub.md](../../../docs/acquisition/sales/objection-handling-hub.md) |
| Buyer psychology | [wm-sales-intelligence-bible.md](../../../docs/acquisition/intelligence/wm-sales-intelligence-bible.md) |

## When to use this skill

- Setter/closer asks **which video to send** and **which URL** (always use `prospect_page_url`, not YouTube, for sales sends).
- Draft **email/SMS/WhatsApp** nurture that references or quotes video content.
- Write **ad scripts**, **landing page** copy, or **retargeting** aligned to existing filmed angles.
- Pre-handle objections: burned by agency, guarantee, leads-only, call center, differentiation, market size, trust.

## Workflow

1. Follow `load_order` in the manifest.
2. Match prospect objection or funnel stage to `assets[].pre_handle_beliefs` / `use_cases` in the manifest (or the quick-send table in the hub doc).
3. Pull **key messages** and **transcript** from the hub doc section for that asset — do not invent claims not in the transcript.
4. For **guarantee or pricing numbers** in asset #6: confirm against [money model](../../../docs/company/overview-money-model-april-26.md) — founder-only; do not drift from live offer.
5. **Shorts** may end with social CTAs (“comment reverse”); sales sends use the **prospect landing page** link.

## Default nurture sequence (not strict)

| Order | Asset ID | When |
|-------|----------|------|
| 1 | `whoweare-why-we-do-what-we-do` | Trust / who is Waiz |
| 2 | `rm-opportunity-industry` | Market size / urgency |
| 3 | `what-makes-waiz-different` | Differentiation / 3 pillars |
| 4–6 | `burnt-by-other-agencies`, `leads-arent-everything`, `do-we-guarantee-results` | **Jump-send** when matching objection surfaces |
| 7 | `reverse-sales-team-call-center` | Dial team / “who follows up?” depth |

## Related skills

[waiz-business-os](../waiz-business-os/SKILL.md) · [copywriting](../copywriting/SKILL.md) · [linkedin-lo-outreach](../linkedin-lo-outreach/SKILL.md) · [marketing-psychology](../marketing-psychology/SKILL.md) · [team-doc-publish](../team-doc-publish/SKILL.md)

## Do not

- Commit `.mp4` files to the repo (host on YouTube / landing pages only).
- Duplicate full transcripts in other docs — link to the hub doc.
- Quote guarantee or pricing terms not confirmed on the live offer.
