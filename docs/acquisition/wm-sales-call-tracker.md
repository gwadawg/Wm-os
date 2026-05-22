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

**sales-leadership** per [domain owners](_inventory/domain-owners.md). Setter logs LinkedIn touches daily; Gabriel updates reply/book fields after handoff.

## Source File

Keep the raw workbook in `source-docs/` — do not delete:

`source-docs/waiz-drive-export/Waiz Media OS/01 _ Acquisition/WM_Sales_Call_Tracker.xlsx`

## Operating Content

Open the spreadsheet for formulas and dashboards. Add a tab or column group **LinkedIn Outreach** using the field definitions below (mirror into xlsx when approved).

---

## LinkedIn Outreach Fields (`draft`)

**No daily targets in v1** — run one week, then set connects/openers goals from actual capacity.

| Column | Type | Who updates | Definition |
|--------|------|-------------|------------|
| `date` | date | Setter | First touch date |
| `prospect_name` | text | Setter | |
| `linkedin_url` | url | Setter | Profile URL |
| `track` | A \| B | Setter | A = reverse LO; B = forward/recruit |
| `angle_id` | 1–10 | Setter | From [angle library](sales/linkedin-dm-angle-library.md) |
| `channel` | enum | Setter | `connect_dm` \| `warm_dm` \| `inmail` |
| `lead_list` | text | Setter | SN list name or source (group, engagement mine, post search) |
| `connect_sent` | Y/N | Setter | Blank connect sent |
| `opener_sent` | Y/N | Setter | First DM sent |
| `inmail_sent` | Y/N | Setter | Sales Navigator message (note if credit used) |
| `replied` | Y/N | Gabriel | Prospect responded |
| `handoff_at` | datetime | Setter | When Gabriel notified |
| `booked` | Y/N | Gabriel | Call booked from thread |
| `booked_at` | date | Gabriel | |
| `intro_scheduled` | Y/N | Setter/Gabriel | If routed to phone intro per intro SOP |
| `notes` | text | Both | Signal used, objection snippet, ghost reason |

### Derived metrics (weekly)

| Metric | Formula |
|--------|---------|
| `reply_rate` | count(`replied`=Y) / count(`opener_sent`=Y) |
| `book_rate` | count(`booked`=Y) / count(`replied`=Y) |
| `angle_performance` | Pivot: `angle_id` × reply_rate, book_rate |

### Daily roll-up (optional row)

| Field | Definition |
|-------|------------|
| `connects_sent` | Sum connect_sent for day |
| `openers_sent` | Sum opener_sent for day |
| `inmails_sent` | Sum inmail_sent for day |
| `replies` | Sum replied for day |
| `books` | Sum booked for day |

---

## Related Docs

- [LinkedIn LO Outreach SOP](sales/linkedin-lo-outreach-sop.md)
- [LinkedIn DM Angle Library](sales/linkedin-dm-angle-library.md)
- [EOD Report SOP (Setters And Closers)](sales/eod-report-sop-setters-closers.md)
- [Intro Call Qualification Framework](sales/intro-call-qualification-framework.md)

## Open Questions

- [ ] Add LinkedIn tab/columns to xlsx in `source-docs/` (use xlsx skill).
- [ ] Confirm single source of truth (Sheets vs xlsx in repo).
- [ ] Set week-1 baseline targets after first week of logging.
