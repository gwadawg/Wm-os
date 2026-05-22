---
name: linkedin-lo-outreach
description: Drafts and improves LinkedIn outreach to reverse mortgage loan officers using Waiz SOPs, angle library, and sales intelligence. Use for LinkedIn DMs, Sales Navigator outreach, setter openers, micro-notes, comment-first warm-up, follow-up sequences, Gabriel reply coaching, voice notes, or booking language.
---

# LinkedIn LO Outreach

Waiz Media LinkedIn outbound for reverse mortgage LOs.

**Setter:** Phase 0 comments → 90s research → pre-connect ritual → connect (blank or micro-note A/B) → first DM → **one** no-reply bump → handoff on reply.

**Gabriel:** All replies, 3-touch ghost sequence, optional voice note, book, pre-call discovery; InMail touch 2+; dream-account omnichannel.

## Before You Draft

1. Read [linkedin-lo-outreach-sop.md](../../../docs/acquisition/sales/linkedin-lo-outreach-sop.md).
2. Read [linkedin-dm-angle-library.md](../../../docs/acquisition/sales/linkedin-dm-angle-library.md).
3. [Identity Core](../../../docs/company/doctrine-identity-core-april-26.md) + [WM Sales Intelligence Bible](../../../docs/acquisition/intelligence/wm-sales-intelligence-bible.md).
4. Pricing → [Money Model](../../../docs/company/overview-money-model-april-26.md) only.

## Classify The Request

| Type | Who | Rules |
|------|-----|--------|
| Comment (Phase 0) | Setter | 5–10/day, no pitch, ICP posts |
| Connect micro-note | Setter | &lt;200 chars, signal only, A/B vs blank |
| Setter opener | Setter | Angle 1–10, message 1, handoff on reply |
| Setter bump | Setter | One only, 48–72h, no pitch |
| Gabriel reply | Gabriel | Permission, I-moment, discovery |
| Ghost touch 1–3 | Gabriel | Value → value → opt-out |
| Voice note | Gabriel | Post-reply, 30–40s, mobile, warm only |
| InMail | Gabriel | After connect+DM stall, Tier-A |
| Book / pre-call | Gabriel | Times + email; discovery after book |

Label: **Track A/B**, **tier** (standard/dream), **warm/cold**, voice (**Professional / Peer LO / Casual**).

## Workflow

1. Strongest signal (prefer **comment thread** if Phase 0 ran).
2. Angle # + voice + `connect_type` if applicable.
3. Draft; annotate psychology (mutuality, permission, follow-up value — no fake scarcity).
4. Quality checklist.
5. Log fields: `sequence_stage`, `connect_type`, `commented_before_connect`.

## Quality Checklist

- [ ] One question per message
- [ ] Banned phrases absent (including setter bump — rephrase “curious if” → “wondering if”)
- [ ] No pitch in M1 or connect note
- [ ] Specific signal (not “loved your content”)
- [ ] No fabricated stats; compliance-safe for mortgage B2B
- [ ] InMail not first touch unless explicit test flag
- [ ] Account safety: no volume spike recommendation

## Output Format

```markdown
## Classification
- Track: A | B
- Tier: standard | dream
- Stage: comment | micro_note | opener | setter_bump | reply | ghost_1 | ghost_2 | ghost_3 | voice_note | book | pre_call
- Angle: #N
- Voice: Professional | Peer LO | Casual
- connect_type: blank | micro_note | n/a

## Draft
[text]

## Annotations
- Principle: [...]
- sequence_stage: [...]

## Handoff
[HANDOFF_ON_REPLY if setter and prospect may reply]
```

## Reference

[reference.md](reference.md) — account limits, sequences, voice notes, benchmarks.

## Examples

[examples.md](examples.md)

## Prompt

[linkedin-dm-draft-prompt.md](../../../docs/prompts/acquisition/linkedin-dm-draft-prompt.md)
