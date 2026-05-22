---
title: LinkedIn LO Outreach SOP
domain: acquisition
owner: setter
status: draft
last_updated: 2026-05-21
review_cycle: weekly
artifact_type: sop
source_note: Process adapted from external LinkedIn DM training (May 2026), Waiz founder session, and 2025–2026 B2B LinkedIn outreach benchmarks.
---

# LinkedIn LO Outreach SOP

## Purpose

Run LinkedIn outbound to reverse mortgage loan officers (and secondary forward-LO recruit motion) to start real conversations and book intro or discovery calls. Covers sourcing, account-safe volume, warm-up, connect/DM/InMail sequencing, setter first touch + one no-reply bump, Gabriel replies through book, follow-up when ghosted, and pre-call discovery in chat.

## Scope

**Included:** Sales Navigator lists, native LinkedIn search, comment warm-up, pre-connect ritual, connect (blank or signal micro-note A/B), first DM, setter no-reply bump, Gabriel conversation + 3-touch ghost sequence, optional voice note, dream-account omnichannel, logging, compliance guardrails.

**Excluded:** Phone intro-call execution (see [Intro Call Qualification Framework](intro-call-qualification-framework.md)), pricing/deal terms (founder only per [Money Model](../../company/overview-money-model-april-26.md)), LinkedIn automation/bots, editing `source-docs/`.

## Owner

- **Setter (Pedro / VA):** Comment warm-up, lead mining, 90-second research, pre-connect ritual, connect (blank or micro-note per test), first DM, **one** no-reply bump 48–72h after opener if no reply, then stop.
- **Gabriel:** Every reply after prospect’s first response; 3-touch value sequence if ghosted after handoff or after engaging then cold; voice notes optional; book + pre-call discovery; dream-account email/phone after LinkedIn exhausted.

See [domain owners](../../_inventory/domain-owners.md).

## Trigger

- Daily Hunt Mode block or dedicated LinkedIn block per [Setter Daily Operations Playbook](setter-daily-operations-playbook.md).
- Reactivation of Sales Navigator subscription and named lead lists.

## Inputs

- Sales Navigator (lead lists, filters, InMail credits — **second touch only** by default).
- Native LinkedIn (search, groups, engagement mining, **comments on ICP posts**).
- [LinkedIn DM Angle Library](linkedin-dm-angle-library.md).
- Gabriel profile: [linkedin.com/in/gabe-goertzen-5689a219b](https://www.linkedin.com/in/gabe-goertzen-5689a219b).
- Optional: Clay for hyper-specific lists (validate activity; discard ghosts).

## Outputs

- Logged prospect row in [WM Sales Call Tracker](../wm-sales-call-tracker.md).
- Connect + opener (+ optional setter bump) per channel rules.
- Handoff to Gabriel on **any** prospect reply.
- Gabriel follow-up sequence or omnichannel touch for dream accounts when applicable.
- Booked call with email + specific time; pre-call discovery in chat.

## Tools

| Tool | Use |
|------|-----|
| Sales Navigator | Lead lists; **Posted on LinkedIn** filter; InMail **after** connect+DM no-reply (Tier-A) |
| LinkedIn (native) | Posts, groups, engagement mining, **comments** |
| LinkedIn DMs | Primary inbox after connect |
| LinkedIn mobile app | Optional **voice notes** (Gabriel only, post-reply) |
| Claude project | [LinkedIn DM Draft Prompt](../../prompts/acquisition/linkedin-dm-draft-prompt.md) |
| WM Sales Call Tracker | Volume, A/B, sequence stage, benchmarks |

## ICP Tracks

| Track | Who | Goal |
| ----- | ----------------------------- | --------------------------------------------------- |
| **A** | Active reverse mortgage LO | Bottom-funnel; sell done-for-you acquisition system |
| **B** | Forward / other loan officers | Educate on reverse opportunity; recruit or nurture |

Label every prospect **Track A** or **Track B** in the tracker.

## Account Safety And Volume (required)

LinkedIn limits are **dynamic** (trust score, acceptance rate, pending backlog) — not a fixed “100/week” for every account.

| Rule | Action |
|------|--------|
| **Ramp** | Week 1 = baseline only; increase connects/openers max **10–15% per week** — no spikes from zero to high volume |
| **Pending invites** | Withdraw stale requests weekly; keep pending **under ~500** |
| **Acceptance guardrail** | If weekly connect acceptance **under 30%**, pause connects 48h — fix targeting, signals, or micro-note quality |
| **Organic ratio** | Before outbound block: Gabriel **posts/comments**; setter **5–10 substantive comments/day** on ICP posts (no pitch in comments) |
| **Double-channel** | Never same-day InMail + DM pitch to same person |

Set concrete daily caps after week 1 baseline in tracker. New or low-trust accounts: start lower (industry guidance often ~10–15 connects/day max early).

## Process

### Phase 0 — Comment warm-up (setter, daily)

**Before** connect requests in the same session:

1. Find **10–100 reaction** posts where Track A/B LOs comment (reverse educators, lenders, industry news).
2. Leave **5–10 thoughtful comments/day** — insight or real question, never “Great post!” or pitch.
3. If setter commented, log `commented_before_connect = Y` and reference that thread in opener (Angle 4 / library).
4. Prefer DM within **24 hours** of a real comment exchange when they reply on the post.

**Gabriel:** Own founder posts + **5+ comments/day** on niche content (long-game inbound).

### Phase 1 — Lead sourcing (setter, 30–60 min/day)

1. **Sales Navigator** — named lists (dream accounts, geo, group-mined, spoke-to-before-cold); **Posted on LinkedIn** when available.
2. **LinkedIn native** — post search (retirement equity, HECM wins); groups; engagement mining on large reverse pages.
3. **Activity gate** — post, repost, or comment in ~90 days; skip dead profiles.
4. **Perfect-fit proxies** — funded-deal posts, heavy reverse content, group/engagement signals (ad spend not visible on profile).

### Phase 1b — 90-second research (setter, per prospect)

Before connect or DM:

| Step | Time | Capture |
|------|------|---------|
| Role + company | 15s | Track A or B |
| One recent activity | 30s | Post/comment line for opener |
| Strongest signal | 30s | Angle # |
| Tier | 15s | Standard / Tier-A dream |

Tier-A = dream account: extra care on signal; still default **connect → DM first**, not InMail-first.

### Phase 2 — Pre-connect ritual (setter)

Immediately before connection request:

1. **View** their profile (shows intent; supports acceptance).
2. **Follow** their company page if legitimate shop (optional, skip if unclear).
3. Send connect per channel tree below.

### Phase 3 — Channel choice (setter)

```text
WARM (liked Gabe’s post, profile view, commented on Gabe’s post, new follower)
  → DM with mutuality opener (Angle 1, 4, or 5). No pitch in message 1.
  → If setter already commented on their post: reference that thread in opener.

STANDARD COLD (default)
  → Pre-connect ritual (view + optional company follow)
  → Connect: BLANK (default) OR signal-only MICRO-NOTE (A/B — log connect_type)
       Micro-note rules: under 200 characters, one specific signal, zero pitch, zero links
       Example: “Hey [Name] — saw your comment on [topic] on [Person]’s post. Would be good to connect.”
  → After accept → first DM from angle library within 24–48h

TIER-A DREAM (exec, low accept rate, or strategic account)
  → Same as STANDARD: connect → DM → wait 5–7 days
  → If no accept: consider withdraw + InMail OR omnichannel (Gabriel)
  → If accepted, opener sent, no reply 5–7 days: Gabriel InMail as TOUCH 2 (not first touch)
  → Do not burn InMail credits on first touch unless testing with tracker flag

NO same-day InMail + DM to same prospect.
```

**Why blank default:** Generic notes hurt acceptance; **specific** micro-notes can beat blank on reply-after-accept — test via `connect_type` in tracker.

**InMail:** Supplementary after connect path stalls — not default opener for LO persona.

### Phase 4 — Setter execution (first touch)

1. Pick angle from [LinkedIn DM Angle Library](linkedin-dm-angle-library.md) (strongest signal; use **Peer LO** voice when profile is plain-spoken producer, not corporate).
2. Send **one** opener: one question, no Waiz pitch in message 1.
3. Log: track, angle #, channel, `connect_type` (`blank` | `micro_note`), `commented_before_connect`.
4. **Stop** on prospect reply → hand off to Gabriel.

### Phase 4b — Setter no-reply bump (one only)

If **accepted + opener sent + no reply** after **48–72 hours**:

1. Setter may send **one** short bump (under 3 lines, one question, no pitch).
2. Examples in angle library — e.g. “No worries if timing’s off — wondering if [original topic] is still on your radar?”
3. Log `setter_bump_sent = Y`. **Do not** send a second bump.
4. If still no reply → status `awaiting_gabriel_sequence` for Gabriel or archive per weekly review.

If **connect pending 7+ days** → withdraw request; re-queue or Tier-A omnichannel.

### Phase 5 — Handoff to Gabriel

**Trigger:** Any inbound reply.

1. Setter stops thread.
2. Notify Gabriel: name, URL, angle, connect_type, comment context, thread link/screenshot.
3. Tracker: `replied = Y`, `handoff_at`.

### Phase 6 — Gabriel conversation (reply → book)

1. **Match** length, speed, tone.
2. **Permission** before advice (“Mind if I bounce a few thoughts off you?”).
3. **I-moment** before direct asks.
4. **One question** per message.
5. **Discovery in DM** before offer — volume, what’s working, conversation quality ([WM Sales Intelligence Bible](../intelligence/wm-sales-intelligence-bible.md)).
6. **Value bump** tied to their words if cold mid-thread.
7. **Voice note (optional)** — after warm reply, max **30–40 seconds**, mobile LinkedIn only, 1st-degree; personalize in first 5 seconds; no pitch in first half. Log `voice_note_sent`.
8. **Book** — 2–3 specific times + email; Calendly only if qualification needed.
9. **Pre-call discovery** day before — permission, then need/volume/timeline.

**Banned (setter + Gabriel):** `curious`, `just circling back`, `any thoughts?`, `hope this finds you well`, pitch on connect notes, stacked questions.

### Phase 6b — Gabriel ghost sequence (no reply after engagement or handoff stall)

When prospect **engaged then went silent** OR **setter bump got no reply** (Gabriel owns):

| Touch | Day (from last activity) | Content |
|-------|--------------------------|---------|
| 1 | +3–4 | Value tied to their stated pain (insight, not “checking in”) |
| 2 | +7–10 | Different angle — case proof **only if approved**, or industry pattern |
| 3 | +12–14 | Soft breakup + opt-out: “Happy to leave you alone if timing’s wrong — just say the word.” |

Log `gabriel_touch_1/2/3`. No fourth touch without new signal (they posted, viewed profile, etc.).

Industry note: **50–70%** of LinkedIn outcomes often come from follow-ups — this sequence is mandatory, not optional.

### Phase 7 — Omnichannel (dream accounts only)

After LinkedIn sequence exhausted (connect withdrawn or 3 Gabriel touches, no book):

1. **One** email if address known — reference LinkedIn context, single CTA.
2. **One** phone attempt if high-value and number available — setter or Gabriel per team norm.
3. Log `omnichannel_email`, `omnichannel_call` in tracker.

Do not spam multiple channels same day.

### Phase 8 — After book

- [Intro Call Qualification Framework](intro-call-qualification-framework.md)
- [No Shows And Maximizing Show Rates](no-shows-maximizing-show-rates-setter-levers.md)
- [Objection Handling Hub](objection-handling-hub.md)

## Compliance And Trust (mortgage B2B)

| Do | Don't |
|----|-------|
| Speak to **qualified conversations** and systems | Guarantee production, rates, or “#1” claims |
| Use approved case proof only | Imply HUD/FHA endorsement unless accurate |
| Offer opt-out on touch 3 | Argue compliance in DM |
| Keep Track B as **marketing/partnership** conversation | Imply employment/recruiting where selling services |

Escalate legal/compliance questions to Gabriel immediately.

## Quality Bar

- Waiz voice per [Identity Core](../../company/doctrine-identity-core-april-26.md).
- Opener = **specific** signal (post line, comment thread, group, mutual).
- No fabricated stats.
- Gabriel profile = landing page (niche, not generic lead vendor).

## Escalation

| Situation | Escalate to |
|-----------|-------------|
| Pricing, discount, deal structure | Gabriel / founder |
| Contract/legal/compliance | Gabriel |
| Hostile or harassing | Gabriel — disengage |
| Unsure Track A vs B | Gabriel before pitch |
| Weekly accept rate under 30% | Gabriel — pause and fix list |

## Metrics

Log in [WM Sales Call Tracker](../wm-sales-call-tracker.md). Week 1 = baseline only; then set caps.

### Core fields

| Field | Definition |
|-------|------------|
| `connects_sent` | Requests sent |
| `connect_type` | `blank` \| `micro_note` |
| `connect_accepted` | Y/N (for accept rate) |
| `comments_posted` | Setter comment count (daily roll-up) |
| `openers_sent` | First DM |
| `setter_bump_sent` | One no-reply bump |
| `inmails_sent` | SN message (usually touch 2+) |
| `replies` | Prospect responded |
| `books` | Call booked |
| `angle_id` | 1–10 |
| `sequence_stage` | opener / setter_bump / gabe_1 / gabe_2 / gabe_3 / booked / archived |

### Benchmarks (interpretation — not targets until baseline set)

| Metric | Healthy | Diagnosis if weak |
|--------|---------|-------------------|
| Connect accept rate | 30–45%+ targeted | &lt;20% = list or note problem |
| Opener → reply | 10–18% strong | &lt;5% = too pitchy or generic |
| Reply → book | Track internally | Discovery or offer timing |
| Follow-up contribution | Rising after Phase 4b/6b live | No sequence = leaving wins on table |

### Weekly review (15 min, Gabriel)

1. Top 3 replies + 3 ghosts — tag diagnosis: **list / opener / conversation**.
2. `connect_type` A/B: accept rate and reply rate by blank vs micro_note.
3. Update `last_winning_variant` in [angle library](linkedin-dm-angle-library.md).

## Improvement Loop

1. Week 1 baseline → set caps and ramp.
2. Review micro-note A/B at 30+ connects per variant.
3. Promote to `active` after founder sign-off.
4. Agent skill: [linkedin-lo-outreach](../../../.claude/skills/linkedin-lo-outreach/SKILL.md).

## Related Docs

- [LinkedIn DM Angle Library](linkedin-dm-angle-library.md)
- [LinkedIn DM Draft Prompt](../../prompts/acquisition/linkedin-dm-draft-prompt.md)
- [Setter Daily Operations Playbook](setter-daily-operations-playbook.md)
- [Intro Call Qualification Framework](intro-call-qualification-framework.md)
- [WM Sales Intelligence Bible](../intelligence/wm-sales-intelligence-bible.md)
- [Identity Core](../../company/doctrine-identity-core-april-26.md)
- [EOD Report SOP](eod-report-sop-setters-closers.md)
- Context: [Fathom — LinkedIn Training May 20](https://fathom.video/share/g694c5Eww6cwSRW1Lwrf4ikt7XkBgW1E)

## Open Questions

- [ ] Week-1 baseline volumes and daily caps.
- [ ] `micro_note` vs `blank` winner at 30+ connects each.
- [ ] Voice note: use on all warm replies or Tier-A only?
