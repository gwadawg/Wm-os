---
title: Aged Lead Reactivation Script — RM
domain: client-fulfillment
owner: client-success
status: draft
last_updated: 2026-07-02
review_cycle: quarterly
artifact_type: script
shareability: lo-course
audience:
  - client
content_layer: canonical
product: reverse-mortgage
delivery_group: lead-nurture
methodology_sources:
  - docs/client-fulfillment/client-marketing/playbook-nurture-framework.md
delivery:
  - github
  - course-material
  - team-drive
---

# Aged Lead Reactivation Script — RM

> **Execution layer** for [Nurture Framework §4 — Aged lead reactivation](playbook-nurture-framework.md#4-aged-lead-reactivation).  
> **Dial order:** [LO Lead Dialing SOP — RM](sop-lo-lead-dialing-rm.md) (queue priority 5). **Rebook:** [BAMFAM Playbook — RM](../client-sales/playbook-bamfam-rm.md).

## Purpose

Word tracks for **re-engaging aged borrower leads** — opt-ins who went cold after initial nurture. Frame outreach as a **new opportunity check-in**, not an apology for following up.

## Scope

- LO or in-house assistant dialing **aged lists** in CRM (30+ days since last meaningful touch).
- Segments: never reached, reached no book, no-show, engaged no close.
- Does **not** replace automated long-term nurture — this is the **human reactivation layer**.

## Before you dial

1. **Pull CRM notes** — motivator, objection, spouse mention, timeline they gave.
2. **Pick the segment** — angle changes (table below).
3. **Compliance** — obey calling/texting laws; honor STOP/unsubscribe immediately ([RM Compliance Guardrails](../reverse-mortgage-dna/rm-compliance-guardrails.md)).

---

## Segment → angle

| Segment | Open with | Goal |
|---------|-----------|------|
| **Never reached** | They opted in; you're catching up | Book first conversation — treat as delayed fresh lead |
| **Reached, no book** | Reference prior touch lightly | BAMFAM — book inside 72 hours |
| **Booked, no show** | Acknowledge missed slot without guilt | Rebook sooner slot; confirm number saved |
| **Engaged, no close** | "Timing may have shifted" | Short education call — new numbers or life change |
| **Nurture-only** | Human break from automation | One clear ask to talk live |

---

## Opening calls (live)

### Never reached — aged opt-in

> Hey [NAME], this is [ASSISTANT] from [LO NAME]'s office. You had reached out a while back about [INTENT — equity / payment relief / debt]. [LO FIRST NAME] asked me to circle back — a lot has changed for folks in [AREA] and I wanted to see if it still makes sense to get you those numbers. Do you have two minutes, or should we grab **[tomorrow morning / tomorrow afternoon]**?

### Reached before, no appointment

> Hey [NAME], [ASSISTANT] from [LO NAME]'s office — we spoke briefly [timeframe] about [what they cared about]. I'm not calling to pressure you — I'm checking whether **timing shifted**. If a quick 15-minute call with [LO FIRST NAME] would help you see what's possible now, I have **[slot A / slot B]** open. Which is easier?

### No-show rebook

> Hi [NAME], it's [ASSISTANT] from [LO NAME]'s office. We had you down for [DAY] and I know schedules get crazy. Totally fine — I'd rather get you a time that actually works. I have **[earlier slot / next-day slot]** — want me to move you there?

### Engaged with LO, went cold

> Hey [NAME], [LO FIRST NAME] asked me to reach out. When we last talked you were weighing [their motivator]. A lot of homeowners we're speaking with right now are revisiting this because **[equity / bills / rates / family alignment]** shifted. Worth a fresh 15-minute look — **[slot A / slot B]**?

📋 Objection depth: [RM Borrower Objections](../reverse-mortgage-dna/rm-borrower-objections.md).

---

## Voicemail (aged)

> Hey [NAME], [ASSISTANT] from [LO NAME]'s office. You'd asked about [INTENT] — I'm circling back because a lot of folks are revisiting this now that [equity / costs / timing] has shifted. No pressure — call or text me back at this number and we'll find 15 minutes that work.

Follow with a short text in the same session per [dialing SOP](sop-lo-lead-dialing-rm.md).

---

## Text patterns (after call attempt or nurture break)

**Never reached / nurture-only:**

> Hi [NAME] — [ASSISTANT] from [LO NAME]'s office. You'd reached out about [INTENT]. Still something you're exploring, or did timing change? Happy to set a quick call — reply YES and I'll send times.

**Prior conversation:**

> Hi [NAME] — following up from our chat about [motivator]. [LO FIRST NAME] has openings **[day/time options]**. Want me to hold one?

**No-show:**

> Hi [NAME] — missed you on [DAY]. No worries. I can move you to **[slot A]** or **[slot B]** — which works?

Keep texts **one ask** — book the call, don't underwrite over SMS.

---

## Reactivation cadence (default)

Lighter than Week 1 fresh-lead blitz — you're re-opening, not hammering.

| Day | Action |
|-----|--------|
| 1 | Call (double-dial) + VM + text |
| 3 | Second call pass + text if no connect |
| 7 | Third attempt + email if you have it |
| 14+ | Return to long-term nurture or quarterly manual re-touch |

After **3 structured attempts** with no engagement, log disposition and let automation carry — unless CRM shows a new inbound signal (reply, form re-submit).

---

## Dispositions

| Outcome | Action |
|---------|--------|
| Booked | BAMFAM confirm on phone; reminders on |
| Re-engaged, needs nurture | Back into active sequence; note motivator |
| Not now — future date | BAMFAM callback date + task |
| Hard no / disqualify | Exit per CRM; no more outreach |
| STOP / unsubscribe | Remove from all channels immediately |

---

## Anti-patterns

| Don't | Do instead |
|-------|------------|
| "Sorry to bother you again" | Lead with value or timing check-in |
| Re-pitch full product on text | One ask — 15-minute call |
| Ignore prior notes | Reference their motivator in the first 20 seconds |
| Same script for every segment | Pick angle from segment table |

## Related docs

| Doc | Role |
|-----|------|
| [Nurture Framework §4](playbook-nurture-framework.md#4-aged-lead-reactivation) | Principles and psychology |
| [LO Lead Dialing SOP — RM](sop-lo-lead-dialing-rm.md) | Queue, double-dial, VM/text |
| [BAMFAM Playbook — RM](../client-sales/playbook-bamfam-rm.md) | Book on the phone |
