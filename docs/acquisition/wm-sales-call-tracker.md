---
title: WM Sales Call Tracker
domain: acquisition
owner: sales-leadership
status: draft
last_updated: 2026-05-21
review_cycle: weekly
source_document: source-docs/waiz-drive-export/Waiz Media OS/01 _ Acquisition/WM_Sales_Call_Tracker.xlsx
artifact_type: kpi
---

# WM Sales Call Tracker

## Purpose

Operational tracker for sales calls (setters and closers) and **LinkedIn outbound** prospects. Canonical **data** lives in the spreadsheet; this doc describes fields and how to use it.

## Scope

Acquisition reporting. Use the **xlsx** skill when updating structure or formulas in the workbook.

## Owner

**sales-leadership** per [domain owners](_inventory/domain-owners.md). Setter logs LinkedIn touches daily; Gabriel updates reply/book/sequence fields after handoff.

## Source File

Keep the raw workbook in `source-docs/` — do not delete:

`source-docs/waiz-drive-export/Waiz Media OS/01 _ Acquisition/WM_Sales_Call_Tracker.xlsx`

## Operating Content

Open the spreadsheet for formulas and dashboards. Add a tab or column group **LinkedIn Outreach** using the field definitions below (mirror into xlsx when approved).

---

## LinkedIn Outreach Fields

**Week 1 = baseline only.** Then set daily caps per [LinkedIn LO Outreach SOP](sales/linkedin-lo-outreach-sop.md) account-safety section.

### Prospect row

| Column | Type | Who updates | Definition |
|--------|------|-------------|------------|
| `date` | date | Setter | First touch date |
| `prospect_name` | text | Setter | |
| `linkedin_url` | url | Setter | Profile URL |
| `track` | A \| B | Setter | A = reverse LO; B = forward/recruit |
| `tier` | standard \| dream | Setter | Dream = Tier-A omnichannel eligible |
| `angle_id` | 1–10 | Setter | From [angle library](sales/linkedin-dm-angle-library.md) |
| `voice` | professional \| peer_lo \| casual | Setter | Voice variant used |
| `channel` | enum | Setter | `connect_dm` \| `warm_dm` \| `inmail` |
| `connect_type` | blank \| micro_note | Setter | A/B connect test |
| `commented_before_connect` | Y/N | Setter | Phase 0 comment on ICP post |
| `lead_list` | text | Setter | SN list or source |
| `connect_sent` | Y/N | Setter | Request sent |
| `connect_accepted` | Y/N | Setter | Accepted (for accept rate) |
| `opener_sent` | Y/N | Setter | First DM |
| `setter_bump_sent` | Y/N | Setter | One 48–72h bump |
| `inmails_sent` | Y/N | Gabriel | Usually touch 2+; note if credit used |
| `replied` | Y/N | Gabriel | Prospect responded |
| `handoff_at` | datetime | Setter | Gabriel notified |
| `sequence_stage` | enum | Both | `opener` \| `setter_bump` \| `gabe_1` \| `gabe_2` \| `gabe_3` \| `booked` \| `archived` |
| `voice_note_sent` | Y/N | Gabriel | Optional mobile voice note |
| `booked` | Y/N | Gabriel | Call booked |
| `booked_at` | date | Gabriel | |
| `omnichannel_email` | Y/N | Gabriel | Dream account after LI exhausted |
| `omnichannel_call` | Y/N | Gabriel | Dream account phone attempt |
| `intro_scheduled` | Y/N | Setter/Gabriel | Phone intro per intro SOP |
| `weekly_diagnosis` | list \| opener \| conversation | Gabriel | Weekly review tag |
| `notes` | text | Both | Signal, ghost reason, objections |

### Derived metrics (weekly)

| Metric | Formula | Healthy (guide) |
|--------|---------|-----------------|
| `connect_accept_rate` | accepted / sent | 30–45%+ targeted |
| `reply_rate` | replied / openers_sent | 10–18% strong; &lt;5% fix opener |
| `book_rate` | booked / replied | Track internally |
| `micro_note_vs_blank` | Pivot `connect_type` × accept × reply | Pick winner at 30+ each |
| `angle_performance` | Pivot `angle_id` × reply_rate, book_rate | |
| `follow_up_lift` | Replies after setter_bump or gabe_1+ | Should grow with Phase 4b/6b |

### Daily roll-up (setter)

| Field | Definition |
|-------|------------|
| `connects_sent` | Count connect_sent |
| `openers_sent` | Count opener_sent |
| `comments_posted` | Phase 0 comment count (target 5–10) |
| `setter_bumps_sent` | Count setter_bump_sent |
| `inmails_sent` | Count inmail (Gabriel) |
| `replies` | Count replied |
| `books` | Count booked |
| `connect_accept_rate` | Daily or rolling 7-day |

---

## Related Docs

- [LinkedIn LO Outreach SOP](sales/linkedin-lo-outreach-sop.md)
- [LinkedIn DM Angle Library](sales/linkedin-dm-angle-library.md)
- [EOD Report SOP (Setters And Closers)](sales/eod-report-sop-setters-closers.md)
- [Intro Call Qualification Framework](sales/intro-call-qualification-framework.md)

## Open Questions

- [ ] Add LinkedIn tab/columns to xlsx in `source-docs/` (use xlsx skill).
- [ ] Confirm single source of truth (Sheets vs xlsx in repo).
- [ ] Set week-1 baseline targets and daily caps after first week.
