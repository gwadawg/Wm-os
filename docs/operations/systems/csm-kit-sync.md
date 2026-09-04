---
title: CSM Kit Sync
domain: operations
owner: operations
status: active
last_updated: 2026-09-04
review_cycle: quarterly
---

# CSM Kit Sync

## Purpose

Promote Client Success–safe docs and Waiz brand tokens from Wm-os into the sibling **wm-csm-kit** Cursor workspace without exposing finance, acquisition pricing, or owner strategy.

## Scope

- Allowlisted Markdown under [config/csm-kit-allowlist.yaml](../../../config/csm-kit-allowlist.yaml)
- Brand token refresh from carousel/offer-sheet CSS
- Redaction of known sensitive lines in overdue-payments SOP

## Owner

Operations / founder.

## Trigger

- New or updated CS / onboarding / KPI-judgment doc that the CSM should use
- Brand token or doctrine visual change
- After merging CS docs to `main`

## Process

1. Confirm the path belongs on the allowlist (or add it intentionally).
2. From Wm-os root:

```bash
python3 scripts/promote-csm-kit.py --dry-run
python3 scripts/promote-csm-kit.py
```

3. Open `../wm-csm-kit`, review diff (especially redactionsacted files and `brand/tokens.*`).
4. Commit and push **wm-csm-kit** (script does not auto-commit).
5. CSM pulls the kit repo.

## Classification question (new CS docs)

When finishing a CS/onboarding/KPI doc, ask: **Promote to CSM kit?** If yes, add the path to the allowlist and run promote.

## Never promote

Company finance, expenses, acquisition offers/sales guts, comp plans, full media-buying / CRM architecture trees, drip copy libraries, SPINE, publish registry, scripts/credentials. Exception: brand doctrine path explicitly allowlisted for visual identity only.

## Related

- Sibling kit: `../wm-csm-kit`
- Mr. Waiz CSM brief API (live data — separate from this sync)
