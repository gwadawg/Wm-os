---
title: LinkedIn Outreach Log Schema
domain: acquisition
owner: sales-leadership
status: draft
last_updated: 2026-05-21
review_cycle: weekly
artifact_type: kpi
---

# LinkedIn Outreach Log Schema

Fields for LinkedIn rows in [WM Sales Call Tracker](../../wm-sales-call-tracker.md). Process caps: [process.md](process.md).

**Week 1 = baseline only** — then set daily caps.

## Prospect row

| Column | Who | Definition |
|--------|-----|------------|
| `date` | Setter | First touch |
| `prospect_name` | Setter | |
| `linkedin_url` | Setter | |
| `track` | Setter | A \| B |
| `tier` | Setter | standard \| dream |
| `angle_id` | Setter | 1–10 — [copy-angles.md](copy-angles.md) |
| `voice` | Setter | professional \| peer_lo \| casual |
| `channel` | Setter | connect_dm \| warm_dm \| inmail |
| `connect_type` | Setter | blank \| micro_note |
| `commented_before_connect` | Setter | Y/N |
| `lead_list` | Setter | SN list or source |
| `connect_sent` | Setter | Y/N |
| `connect_accepted` | Setter | Y/N |
| `opener_sent` | Setter | Y/N |
| `setter_bump_sent` | Setter | Y/N |
| `inmails_sent` | Gabriel | Touch 2+ |
| `replied` | Gabriel | Y/N |
| `handoff_at` | Setter | datetime |
| `sequence_stage` | Both | opener \| setter_bump \| gabe_1 \| gabe_2 \| gabe_3 \| booked \| archived |
| `voice_note_sent` | Gabriel | Y/N |
| `booked` | Gabriel | Y/N |
| `omnichannel_email` | Gabriel | Y/N |
| `omnichannel_call` | Gabriel | Y/N |
| `weekly_diagnosis` | Gabriel | list \| opener \| conversation |
| `notes` | Both | |

## Daily roll-up

`connects_sent`, `openers_sent`, `comments_posted` (target 5–10), `setter_bumps_sent`, `replies`, `books`, rolling `connect_accept_rate`.

## Benchmarks (interpretation)

| Metric | Healthy | Weak signal |
|--------|---------|-------------|
| Connect accept | 30–45%+ | &lt;20% list/note |
| Opener → reply | 10–18% | &lt;5% opener |
| Reply → book | Internal | Conversation/offer |
| Follow-up lift | Up after 4b/6b | Missing sequence |

## Weekly review (Gabriel, 15 min)

1. Top 3 replies + 3 ghosts → `weekly_diagnosis`
2. micro_note vs blank pivot
3. Paste winner to [copy-angles.md](copy-angles.md) `last_winning_variant`
