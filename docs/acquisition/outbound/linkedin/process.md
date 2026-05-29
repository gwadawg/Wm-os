---
title: LinkedIn LO Outreach — Process
domain: acquisition
owner: setter
status: draft
last_updated: 2026-05-29
review_cycle: weekly
artifact_type: sop
source_note: Adapted from May 2026 founder training and 2025–2026 B2B LinkedIn benchmarks.
---

# LinkedIn LO Outreach — Process

Copy: [copy-angles.md](copy-angles.md) · Compliance: [compliance.md](compliance.md) · Logging: [log-schema.md](log-schema.md) · Checklist: [Setter Daily Checklist](../../sales/setter-daily-checklist.md) (P4)

## Purpose

LinkedIn outbound to reverse mortgage LOs (Track A) and forward LO recruits (Track B) → conversations → book with Gabriel → phone intro funnel.

## Scope

**In:** SN lists, comment warm-up, connect/DM sequence, setter **outreach only** (no setter replies), Gabriel replies through book, ghost sequence, dream-account omnichannel.

**Out:** Setter pricing, phone intro execution (see intro script), automated bots. Phone funnel: [Intro Call Qualification](../../sales/intro-call-qualification-framework.md), [Money Model](../../../company/overview-money-model-april-26.md).

## Owners (current)

| Role | Owns |
|------|------|
| **Setter** | Phase 0–4b: comments, mine, research, connect, first DM, **one** no-reply bump. **Does not reply** in LinkedIn threads. |
| **Gabriel** | **All LinkedIn replies**, Phase 6–7: conversation, ghost sequence, voice note, book, omnichannel |

This split matches [P4 on the daily checklist](../../sales/setter-daily-checklist.md#priority-4--linkedin-outreach-only).

## Trigger

- Scheduled **P4 block** when P1–P3 are clear  
- **Any inbound LinkedIn reply** on a prospect thread → forward to Gabriel immediately (even if setter sent opener/bump)

## Inputs / outputs

- Gabriel profile: [linkedin.com/in/gabe-goertzen-5689a219b](https://www.linkedin.com/in/gabe-goertzen-5689a219b)
- Angles: [copy-angles.md](copy-angles.md)
- Log: [log-schema.md](log-schema.md) → [WM Sales Call Tracker](../../wm-sales-call-tracker.md)

**Handoff output:** Gabriel notified with thread URL, angle, tier, and context; tracker updated; optional GHL task for Gabriel.

---

## Setter reply policy (do not break)

Until ops changes this policy:

1. **Do not type a reply** to any prospect on LinkedIn — including thanks, answers, or “quick questions.”
2. **Forward every reply** to Gabriel the same day (see [Handoff to Gabriel](#handoff-to-gabriel-phase-5)).
3. Setter work on LinkedIn = **net-new outreach** (comments, connects, first DM, one bump) only.

If a reply looks simple, still forward — Gabriel owns conversation quality and booking.

---

## ICP tracks

| Track | Who |
| ----- | --- |
| **A** | Active reverse mortgage LO |
| **B** | Forward / other LO (recruit/nurture) |

## Account safety

| Rule | Action |
|------|--------|
| Ramp | Week 1 baseline; then +10–15%/week max |
| Pending | Withdraw stale; keep under ~500 pending |
| Accept rate | Pause 48h if weekly accept &lt;30% |
| Organic | Setter 5–10 ICP comments/day; Gabriel posts + 5+ comments/day |
| Channels | No same-day InMail + DM pitch to same person |

## Banned phrases (setter + Gabriel)

`curious`, `just circling back`, `any thoughts?`, `hope this finds you well`, pitch on connect notes, stacked questions.

---

## Process

### Phase 0 — Comment warm-up (setter, daily)

Before connects: **5–10** substantive comments on ICP posts (no pitch). Log `commented_before_connect`. If you DM within **24h**, use comment-first openers in [copy-angles.md](copy-angles.md).

### Phase 1 — Lead sourcing (30–60 min / P4 block)

SN named lists + **Posted on LinkedIn**; native post search, groups, engagement mining; **activity gate** (~90 days); signals: funded deals, reverse content, group membership.

### Phase 1b — 90-second research

Role/track (15s) → one activity line (30s) → angle # (30s) → tier standard/dream (15s).

### Phase 2 — Pre-connect ritual

View profile → optional follow company → connect per Phase 3.

### Phase 3 — Channel choice

```text
WARM     → DM, angles 1/4/5, no pitch in message 1
STANDARD → blank connect (default) OR micro-note A/B (log connect_type) → DM 24–48h after accept
TIER-A   → connect → DM first; InMail touch 2+ after 5–7d no reply (Gabriel only)
```

Micro-note: &lt;200 chars, one signal, zero pitch — [copy-angles.md](copy-angles.md).

### Phase 4 — Setter first DM

- One opener from [copy-angles.md](copy-angles.md) — **one question**, no pitch in message 1.  
- Log angle, connect_type, tier in tracker.  
- **If they reply:** do **not** answer → [Handoff to Gabriel](#handoff-to-gabriel-phase-5) immediately.

### Phase 4b — Setter one bump (48–72h)

- **One** bump only if: accepted + opener sent + **no reply**. Templates: [copy-angles.md](copy-angles.md) — setter bump section.  
- Log `setter_bump_sent = Y`.  
- **If they reply after the bump:** hand off to Gabriel — still **no setter reply**.  
- If still no reply after bump → `awaiting_gabriel_sequence` (Gabriel runs Phase 6b).  
- Pending connect **7+ days** with no accept → withdraw.

### Handoff to Gabriel (Phase 5)

When **any** reply hits a thread the setter touched (opener, bump, or comment-led DM):

| Step | Action |
|------|--------|
| 1 | **Stop** — no further setter messages in that thread |
| 2 | **Notify Gabriel** — Slack (tag Gabriel) with: LinkedIn profile URL, prospect name, angle #, connect_type, last setter message summary, their reply (copy/paste or screenshot) |
| 3 | **GHL** — task assigned to **Gabriel** if follow-up needs CRM context |
| 4 | **Log** — `replied=Y`, `handoff_at`, `handoff_to=gabriel`; tracker row current |

Optional: ✅ on internal ops Slack if your team uses a LI-alerts channel (same spirit as [Watchshift](../../sales/sop-watchshift.md) cadence).

### Phase 6 — Gabriel (reply → book)

Match energy; permission; I-moment; one question; discovery before offer ([Sales Intelligence Bible](../../intelligence/wm-sales-intelligence-bible.md)); value bump; optional **voice note** (30–40s, mobile, post-reply); book 2–3 times + email; pre-call discovery day before.

### Phase 6b — Gabriel ghost sequence

Touches at +3–4, +7–10, +12–14 days. Templates: [copy-angles.md](copy-angles.md). Mandatory — most wins often from follow-up. Setter does **not** send ghost touches.

### Phase 7 — Omnichannel (dream tier only)

After LinkedIn exhausted: one email + one phone; log flags. Gabriel-owned.

### Phase 8 — After book

Phone funnel: [Intro qualification](../../sales/intro-call-qualification-framework.md) · [Show rate](../../sales/no-shows-maximizing-show-rates-setter-levers.md) · [Objections](../../sales/objection-handling-hub.md) · optional [Pre-call videos](../../marketing/pre-call-objection-videos.md) on other channels.

---

## Quality bar

[Identity Core](../../../company/doctrine-identity-core-april-26.md): qualified conversations, acquisition system, specific signals, no fabricated proof. Setter-specific signals in openers; Gabriel-specific depth in replies.

## Escalation

| Situation | Action |
|-----------|--------|
| Prospect replied | Gabriel only — setter handoff |
| Pricing / compliance / hostile | Gabriel |
| Accept rate &lt;30% | Pause list; fix targeting with ops |
| Setter tempted to “just answer quick” | Forward anyway — policy |

## Metrics and review

See [log-schema.md](log-schema.md). Weekly: top 3 replies + 3 ghosts; diagnosis list/opener/conversation; update `last_winning_variant` in [copy-angles.md](copy-angles.md).

## Improvement

Week 1 baseline → caps → promote winners to `active`. Agent skill: [linkedin-lo-outreach](../../../../.claude/skills/linkedin-lo-outreach/SKILL.md).

## Related

- [manifest.yaml](manifest.yaml)
- [Setter Daily Checklist](../../sales/setter-daily-checklist.md)
- [Setter Lead Messaging](../../sales/setter-lead-messaging.md) — SMS only; not LinkedIn replies
- [Fathom training (context)](https://fathom.video/share/g694c5Eww6cwSRW1Lwrf4ikt7XkBgW1E)

## Open questions

- [ ] Week-1 connection/DM caps
- [ ] `blank` vs `micro_note` A/B winner
- [ ] Voice note on all warm replies or Tier-A only
- [ ] Standard Slack channel name for LI reply handoffs
