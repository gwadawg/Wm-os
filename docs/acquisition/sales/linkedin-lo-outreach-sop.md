---
title: LinkedIn LO Outreach SOP
domain: acquisition
owner: setter
status: draft
last_updated: 2026-05-21
review_cycle: weekly
artifact_type: sop
source_note: Process adapted from external LinkedIn DM training (May 2026) and Waiz founder session; not verbatim third-party copy.
---

# LinkedIn LO Outreach SOP

## Purpose

Run LinkedIn outbound to reverse mortgage loan officers (and secondary forward-LO recruit motion) to start real conversations and book intro or discovery calls. This SOP covers lead sourcing through booking and pre-call discovery in chat.

## Scope

**Included:** Sales Navigator lists, native LinkedIn search (posts, groups, engagement mining), blank connects, first DM openers (setter), all follow-up DMs through book (Gabriel), pre-call discovery in chat, logging in the sales tracker.

**Excluded:** Phone intro-call execution (see [Intro Call Qualification Framework](intro-call-qualification-framework.md)), pricing/deal terms (founder only per [Money Model](../../company/overview-money-model-april-26.md)), LinkedIn automation/bots, editing `source-docs/`.

## Owner

- **Setter (Pedro / VA):** Lead mining, activity check, blank connects, first DM only.
- **Gabriel:** Every reply after the prospect’s first response through book + pre-call discovery in DMs.

See [domain owners](../../_inventory/domain-owners.md).

## Trigger

- Daily Hunt Mode block or dedicated LinkedIn block per [Setter Daily Operations Playbook](setter-daily-operations-playbook.md).
- Reactivation of Sales Navigator subscription and named lead lists.

## Inputs

- Sales Navigator (lead lists, filters, optional InMail credits).
- Native LinkedIn (search, groups, company page engagement).
- [LinkedIn DM Angle Library](linkedin-dm-angle-library.md).
- Gabriel profile: [linkedin.com/in/gabe-goertzen-5689a219b](https://www.linkedin.com/in/gabe-goertzen-5689a219b) (banner/bio must match “knows their world,” not generic lead vendor).
- Optional: Clay for hyper-specific lists (watch for inactive/ghost profiles).

## Outputs

- Logged prospect row in [WM Sales Call Tracker](../wm-sales-call-tracker.md) (LinkedIn fields).
- Blank connect sent and/or first DM sent (setter).
- Handoff to Gabriel on first reply with angle # and thread link.
- Booked call with email + specific time (Gabriel).
- Pre-call discovery captured in chat before the meeting.

## Tools


| Tool                             | Use                                                                                                            |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Sales Navigator                  | Build/save lead lists; filter industry, geo, company size; **Posted on LinkedIn** filter when available        |
| LinkedIn (native)                | Post keyword search, groups, engagement on large reverse pages — **not** available inside Sales Navigator      |
| Sales Navigator InMail / message | Tier-A prospects; limited credits — see channel tree                                                           |
| LinkedIn DMs                     | Primary inbox after connect; warmer, conversational                                                            |
| Claude project                   | Draft/humanize replies — see [LinkedIn DM Draft Prompt](../../prompts/acquisition/linkedin-dm-draft-prompt.md) |
| WM Sales Call Tracker            | Volume and angle performance                                                                                   |


## ICP Tracks


| Track | Who                           | Goal                                                |
| ----- | ----------------------------- | --------------------------------------------------- |
| **A** | Active reverse mortgage LO    | Bottom-funnel; sell done-for-you acquisition system |
| **B** | Forward / other loan officers | Educate on reverse opportunity; recruit or nurture  |


Label every prospect **Track A** or **Track B** in the tracker.

## Process

### Phase 1 — Lead sourcing (setter, 30–60 min/day)

1. **Sales Navigator — build lists**
  - Create named lead lists (examples: dream accounts, spoke-to-before-cold, group-mined).
  - Filters: reverse mortgage / HECM / retirement lending titles, geography, company size as needed.
  - Enable **Posted on LinkedIn** (or equivalent activity signal) when available.
2. **LinkedIn native — intent signals**
  - Search posts for niche language (e.g. retirement equity, HECM wins, funded deals) — not only “reverse mortgage” (too many companies).
  - Join reverse mortgage **groups**; mine members who fit ICP.
  - Mine **engagement** on large reverse companies’ posts (likes/comments = top-of-mind signal).
3. **Activity gate (required)**
  - Profile must show recent activity: own post, repost, or comment on others’ content in the last ~90 days.
  - Skip profiles with zero engagement (dead accounts).
4. **Perfect-fit proxies** (ad spend not visible on profile)
  - Posts funded deals / production wins.
  - Heavy reverse or retirement-lending content.
  - Active in reverse groups or engaging with reverse educators/brands.
  - Track A default unless profile clearly forward LO only (Track B).

### Phase 2 — Channel choice (setter)

```text
Warm (liked Gabe’s post, profile view, commented, new follower)
  → DM in LinkedIn inbox with mutuality opener (Angle 5 or 1). No pitch in message 1.

Tier-A + strong intent (dream account, obvious in-market signals)
  → Consider Sales Navigator message/InMail if credits apply.
  → Use credits only on best fits; some accounts do not consume a credit.

Standard cold
  → Blank connection request (NO note). Never pitch in the connect request.
  → After accept → first DM in LinkedIn inbox from angle library.

A/B test (log in tracker): InMail-first vs connect-first for Track A.
Default for LO persona: blank connect + DM unless testing InMail.
```

**Why blank connects:** Higher accept rate; connect notes set a sales agenda and feel automated.

**InMail vs DM:** InMail can email the prospect and bypass profile-click resistance; LinkedIn DMs are checked more often for active posters. Do not double-channel the same pitch same day.

### Phase 3 — Setter execution (first touch only)

1. Pick angle from [LinkedIn DM Angle Library](linkedin-dm-angle-library.md) from the strongest visible signal.
2. Send **one** opener: one question, no pitch, no mention of Waiz offer in message 1 (see library for voice variants).
3. Log in tracker: date, name, URL, track, angle #, channel, opener sent = Y.
4. **Stop** when prospect replies — hand off immediately.

### Phase 4 — Handoff to Gabriel

**Trigger:** Any inbound reply from the prospect.

Setter actions:

1. Do not send further messages in that thread.
2. Notify Gabriel (Slack/task) with: name, LinkedIn URL, angle used, screenshot or thread link, track A/B.
3. Update tracker: `replied = Y`, `handoff_at` = timestamp.

### Phase 5 — Gabriel conversation (reply → book)

1. **Match** their length, speed, and tone (do not reply with paragraphs to one-liners; do not instant-reply if they take days unless the conversation is hot).
2. **Permission before advice:** e.g. “Mind if I bounce a few thoughts off you?” before a value drop.
3. **I-moment before direct asks:** Share brief relevant experience, then ask (not interrogation-only).
4. **One question per message.** No stacked questions.
5. **Discovery in DM** before hard pitch: volume, what’s working, team vs solo, quality of conversations — align with [WM Sales Intelligence Bible](../intelligence/wm-sales-intelligence-bible.md) (volume imperative, referral math, climate).
6. **Value bump** if they go cold after sharing a specific goal: tie insight to what *they* said (not generic “checking in”).
7. **Book** with 2–3 specific times + ask for email for invite. Prefer proposed times over cold Calendly link unless you need questionnaire qualification.
8. **Pre-call discovery** after book (day before): “Looking forward to tomorrow — mind if I ask a couple things here so we make the most of the time?” Then need, volume target, timeline — see intro framework for FUN themes without re-running a full intro on LinkedIn.

**Banned words/phrases (setter and Gabriel):**

- `curious` / `just curious`
- `just circling back`
- `any thoughts?`
- `hope this finds you well`
- Pitch text on connection requests
- Stacked questions in one bubble

### Phase 6 — After book

Route to existing sales spine:

- [Intro Call Qualification Framework](intro-call-qualification-framework.md) for phone intro if that is the booked stage.
- [No Shows And Maximizing Show Rates](no-shows-maximizing-show-rates-setter-levers.md) for show-rate levers.
- Objections: [Objection Handling Hub](objection-handling-hub.md).

## Quality Bar

- Waiz voice: **qualified conversations**, **acquisition system**, strategic partner — not “leads” or generic agency (see [Identity Core](../../company/doctrine-identity-core-april-26.md)).
- Opener references something **specific** (post line, group, mutual, signal) — not “loved your content.”
- No fabricated stats or case studies; use only approved proof from company materials.
- Gabriel profile passes the “selling to me” sniff test before high-volume outbound.
- Long game: Gabe posting and commenting on niche content increases warm inbound (profile views, thanks-for-the-like openers).

## Escalation


| Situation                                           | Escalate to                  |
| --------------------------------------------------- | ---------------------------- |
| Pricing, discount, deal structure                   | Gabriel / founder            |
| Prospect asks for contract/legal                    | Gabriel                      |
| Harassment, hostile, or compliance-sensitive claims | Gabriel — do not argue in DM |
| Unsure Track A vs B                                 | Gabriel before pitch         |


## Metrics

Log daily in [WM Sales Call Tracker](../wm-sales-call-tracker.md). **Do not use invented targets until week 1 baseline is set.**


| Field           | Definition                              |
| --------------- | --------------------------------------- |
| `connects_sent` | Blank connection requests sent          |
| `openers_sent`  | First DMs sent (post-accept or warm DM) |
| `inmails_sent`  | Sales Navigator messages using credits  |
| `replies`       | Prospects who responded                 |
| `books`         | Calls booked from LinkedIn thread       |
| `reply_rate`    | replies / openers_sent (weekly)         |
| `book_rate`     | books / replies (weekly)                |
| `angle_id`      | 1–10 from angle library                 |


**Weekly review (15 min, Gabriel):** Top 3 replies + 3 ghosts → update winning variant in [angle library](linkedin-dm-angle-library.md).

## Improvement Loop

1. Run one week with fields above populated.
2. Set realistic daily volume targets (connects, openers) from actual capacity.
3. Promote this SOP from `draft` to `active` after founder review.
4. Use agent skill [linkedin-lo-outreach](../../../.claude/skills/linkedin-lo-outreach/SKILL.md) to propose angle library edits from logged outcomes.

## Related Docs

- [LinkedIn DM Angle Library](linkedin-dm-angle-library.md)
- [LinkedIn DM Draft Prompt](../../prompts/acquisition/linkedin-dm-draft-prompt.md)
- [Setter Daily Operations Playbook](setter-daily-operations-playbook.md)
- [Intro Call Qualification Framework](intro-call-qualification-framework.md)
- [WM Sales Intelligence Bible](../intelligence/wm-sales-intelligence-bible.md)
- [Identity Core](../../company/doctrine-identity-core-april-26.md)
- [EOD Report SOP (Setters And Closers)](eod-report-sop-setters-closers.md)
- Training recording (context only): [Fathom — LinkedIn Training May 20](https://fathom.video/share/g694c5Eww6cwSRW1Lwrf4ikt7XkBgW1E)

## Open Questions

- Week 1 baseline volumes for setter (connects, openers, mining minutes).
- InMail-first vs connect-first winner for Track A.
- Approve Professional vs Casual voice default for LO personas after 10 live threads.

