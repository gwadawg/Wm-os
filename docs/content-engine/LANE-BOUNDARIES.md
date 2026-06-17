---
title: Content Engine — Lane Boundaries
domain: content-engine
owner: founder
status: active
last_updated: 2026-06-17
review_cycle: quarterly
artifact_type: playbook
---

# Lane Boundaries — Personal vs Business vs Client

Gabe runs **two public content identities**. This doc prevents voice bleed,
wrong CTAs, and KB entries landing in the wrong lane.

## The two brands

| | **Personal** | **Business (Waiz Media)** |
|---|--------------|---------------------------|
| **Handle / brand** | Gabe Goertzen / @gabeegoertzen | Waiz Media |
| **North star** | Social currency, optionality, full journey | Client acquisition, authority, LO trust |
| **Primary audience** | Upcoming entrepreneurs, ambitious lifestyle, LOs who follow *Gabe* | LOs, brokers, mortgage shops (buyers) |
| **Content feel** | Goofy, aggressive takes, journey, sports, ADHD, Rio story, AI/ops | Operator-grade, compliance-aware, product-specific |
| **Voice DNA** | [`_voice/personal-brand-dna.md`](_voice/personal-brand-dna.md) | [`_voice/waiz-media-brand-dna.md`](_voice/waiz-media-brand-dna.md) |
| **KB root** | `personal/` | `business/` + [`.agents/product-marketing.md`](../../.agents/product-marketing.md) |
| **Script folder** | `personal/scripts/` | `business/scripts/` |

**Why they follow personal but buy Waiz:** Personal = who Gabe is and the life
/ mindset. Waiz = the service for LO lead gen. Personal builds trust and
attention; business converts ICP to calls.

## Topic routing (where does this idea go?)

| Topic | Lane | Why |
|-------|------|-----|
| Rio move, sold everything, solo founder journey | **Personal** | Gabe's story |
| Magic, skate, surf, ADHD systems | **Personal** | Character + lived experience |
| Controversial personal development takes | **Personal** | @gabeegoertzen voice |
| Travel, lifestyle, ambitious identity | **Personal** | Personal brand pillar |
| AI/ops how-to's from Gabe's operator life | **Personal** | Can cross-reference Waiz, not sell Waiz |
| "Your ads aren't the problem — qualification is" | **Business** | LO buyer pain |
| DSCR vs RM marketing nuance | **Business** or **Client** | B2B thought leadership vs ad script |
| Waiz fulfillment OS, creative studio | **Business** | Agency positioning |
| Case study / client results | **Business** | Approved proof only |
| Meta ad script for DSCR client | **Client** | `docs/client-fulfillment/dscr-dna/` |
| UGC script for reverse mortgage | **Client** | `docs/client-fulfillment/reverse-mortgage-dna/` |
| Personal reel → adapted Waiz ad | **Repurposing** | Explicit pipeline only |

When a topic spans both (e.g. "how I built Waiz systems with AI"):

- **Personal angle:** Gabe's journey, personality, lessons learned → `personal/`
- **Business angle:** LO-facing mechanism, why Waiz runs this way → `business/`
- **Never:** Same script copy-pasted across lanes — rewrite for audience + voice

## Voice separation rules

### Personal voice (@gabeegoertzen)

- First person: I / my journey / my beliefs
- Hormozi-adjacent directness, goofy energy, swearing OK
- Stories from `personal/stories.md` (S1 Rio, S2 LO grind, etc.)
- Beliefs from `personal/beliefs.md`
- CTAs: follow, engage, DM — **not** "book a Waiz discovery call" as primary

### Business voice (Waiz Media)

- We / Waiz / our clients / our system
- Compliance-aware; no guaranteed outcomes or unapproved pricing
- Proof from approved case studies and product-marketing
- CTAs: book discovery, audit, DM for conversation
- **No** Rio diary, troublemaker origin, or personal hot takes unless
  reframed as agency lesson without Gabe lifestyle flex

### Hard boundaries (never cross)

| Don't on personal | Don't on business |
|-------------------|-------------------|
| Quote Waiz pricing or packages | Use Gabe's controversial PD rants as brand voice |
| Run client compliance-bound ad copy | Share unapproved client metrics |
| Speak as "Waiz Media" official offer | Lead with lifestyle/travel as primary hook |
| Guarantee LO lead outcomes | Imply personal brand IS the agency product |

## KB separation

| Data type | Personal home | Business home |
|-----------|---------------|---------------|
| Gabe biography / arc | `personal/stories.md` | — |
| Gabe beliefs / philosophy | `personal/beliefs.md` | — |
| Gabe audience language | `personal-brand-dna.md` § Customer Language | — |
| LO pain verbatim | — | `product-marketing.md` |
| Agency objections | — | `product-marketing.md` |
| Waiz positioning | — | `product-marketing.md`, `waiz-media-brand-dna.md` |
| B2B hooks | — | `business/hook-library.md` |
| Personal hooks | `personal/hook-library.md` | — |
| Content ideas | `personal/angle-library.md` | `business/angle-library.md` |
| Open questions | `personal/_gaps.md` | `business/_gaps.md` |

**Shared source, split distill:** A sales call transcript may yield LO pain →
business KB and a personal story angle → personal KB. Same raw input; two
distilled entries in two lanes.

## Client lane (third boundary)

Client content is **not** Gabe personal or Waiz organic — it is fulfillment
creative for a specific product (DSCR, RM) with compliance guardrails.

| | Client |
|---|--------|
| **When** | Ad scripts, UGC, lander copy for active client product |
| **Voice** | Client DNA pod + `client-voice-template.md` |
| **Home** | `docs/client-fulfillment/[slug]-dna/` |
| **Never** | Store in `personal/scripts/` or `business/scripts/` |

## Repurposing (explicit cross-lane)

Organic personal/business content that performs may feed ads — but only through
[repurposing/reels-to-ads-engine.md](repurposing/reels-to-ads-engine.md).
Default: personal insight → personal boost or Waiz-adjacent only; business →
Waiz acquisition ads.

## Lane detection for agents

| Signal | Lane |
|--------|------|
| User says `personal`, @gabeegoertzen, journey, beliefs, travel | personal |
| User says `business`, Waiz Media, LO audience, agency | business |
| User says `client:dscr`, `client:rm`, or client DNA doc open | client |
| Ambiguous | Ask once: "Personal, business, or client (which product)?" |

## Related

- [INFRASTRUCTURE.md](INFRASTRUCTURE.md) — paths, naming, dating
- [Personal README](personal/README.md)
- [Business README](business/README.md)
