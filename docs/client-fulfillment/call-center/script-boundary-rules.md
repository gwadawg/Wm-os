---
title: Call Center Script Boundary Rules
domain: client-fulfillment
owner: client-success
status: draft
last_updated: 2026-05-26
review_cycle: monthly
artifact_type: doctrine
---

# Call Center Script Boundary Rules

## Purpose

Prevent cross-use of fulfillment call-center scripts and acquisition sales scripts.

## Scope

Applies to all script execution and script editing in `docs/client-fulfillment/call-center/`.

## Non-Negotiable Rules

- Fulfillment call-center scripts are for client-side B2C conversations after sign.
- Do not use acquisition setter/closer scripts in fulfillment call-center operations.
- Do not store fulfillment call-center script updates in acquisition folders.
- Any Waiz prospecting or Waiz-closing conversation belongs to acquisition sales docs.

## Allowed Fulfillment Script System

- [Call Center Script Factory SOP](sop-call-center-script-factory.md)
- Domain index: [Client Fulfillment — Call Center](README.md)

## Routing Rule

If the conversation is about selling Waiz (prospecting, intro, discovery, demo, objections), route to:

- [Sales Operating Hub](../../acquisition/sales/README.md)
- [Acquisition Script Boundary Rules](../../acquisition/sales/script-boundary-rules.md)

## Escalation

- Unclear script ownership -> client-success lead.
- Mixed-domain script draft detected -> stop and re-home before use.
