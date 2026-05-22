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

Operational tracker for sales calls and outbound prospects. Canonical **data** lives in the spreadsheet; field definitions live in domain schemas.

## Source file

`source-docs/waiz-drive-export/Waiz Media OS/01 _ Acquisition/WM_Sales_Call_Tracker.xlsx`

Use the **xlsx** skill when updating workbook structure.

## Schemas

| Channel | Field definitions |
|---------|-------------------|
| LinkedIn LO outreach | [log-schema.md](outbound/linkedin/log-schema.md) |

LinkedIn process and caps: [process.md](outbound/linkedin/process.md).

## Owner

**sales-leadership** per [domain owners](../_inventory/domain-owners.md). Setter logs LinkedIn daily; Gabriel updates reply/book/sequence fields.

## Related

- [EOD Report SOP (Setters And Closers)](sales/eod-report-sop-setters-closers.md)
- [Intro Call Qualification Framework](sales/intro-call-qualification-framework.md)
- [LinkedIn outbound index](outbound/linkedin/README.md)

## Open questions

- [ ] Mirror LinkedIn columns into xlsx tab
- [ ] Confirm Sheets vs repo source of truth
- [ ] Week-1 baseline targets
