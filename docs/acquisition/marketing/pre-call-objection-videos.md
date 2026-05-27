---
title: Pre-Call Objection Video Assets
domain: acquisition
owner: marketing-lead
status: draft
last_updated: 2026-05-28
review_cycle: monthly
artifact_type: reference
---

# Pre-Call Objection Video Assets

## Purpose

Registry of Waiz Media **prospect-facing** videos that pre-handle beliefs and objections before intro, discovery, or demo calls. Host files stay on YouTube / landing pages; this doc holds URLs, intent, objection mapping, and transcripts for sales, marketing, and AI.

## Scope

Reverse mortgage loan officer prospects (Waiz acquisition). Not client RM homeowner ad creative — see [client marketing](../../client-fulfillment/client-marketing/README.md).

## Owner

Marketing lead (assets); setters/closers execute sends. See [domain owners](../../_inventory/domain-owners.md).

## Trigger

- Prospect books or is in nurture before strategy/demo call.
- Live objection matches a `pre_handle_belief` in the [manifest](pre-call-objection-videos-manifest.yaml).
- Marketing writes ads, landing pages, or email sequences that must match filmed angles.

## Inputs

- Prospect objection or funnel stage (from call notes or CRM).
- [Manifest](pre-call-objection-videos-manifest.yaml) + section below for URL and transcript.

## Outputs

- One **prospect_page_url** sent to the LO (not the raw YouTube link for sales).
- Optional: email/SMS copy pulled from **key messages** or transcript (no invented claims).

## When To Use

- **Setter / closer:** Send the prospect link after book or when trust/credibility is the gap.
- **Marketing:** Landing page embeds, ad nurture, Hammer-Them-style sequences.
- **AI:** Load [pre-call-objection-videos skill](../../.claude/skills/pre-call-objection-videos/SKILL.md) + manifest + this file.

## Quick send by objection

| If prospect says… | Send asset # | Prospect page |
|-------------------|-------------|---------------|
| Who are you? / can I trust you? | 1 | [whoweare](https://wm.waizmedia.net/reversemortgage/whoweare) |
| Is reverse big enough? / bad timing? | 2 | [rmopportunity](https://wm.waizmedia.net/reversemortgage/rmopportunity) |
| How are you different? / what do you do? | 3 | [whatmakesusdifferent](https://wm.waizmedia.net/reversemortgage/whatmakesusdifferent) |
| Burned by another agency | 4 | [burnt](https://wm.waizmedia.net/reversemortgage/burnt) |
| Just need leads / CPL focus | 5 | [leads](https://wm.waizmedia.net/reversemortgage/leads) |
| Guarantee? / pay per appointment? | 6 | [doweguaranteeresults](https://wm.waizmedia.net/reversemortgage/doweguaranteeresults) |
| Who dials? / call center concern | 7 | [callcenter](https://wm.waizmedia.net/reversemortgage/callcenter) |

## Index

| # | Title | Prospect page | Watch | Primary pre-handle |
|---|-------|---------------|-------|-------------------|
| 1 | [Why We Do What We Do](#1-why-we-do-what-we-do) | [whoweare](https://wm.waizmedia.net/reversemortgage/whoweare) | [YouTube](https://youtu.be/RYnwas5j7iI) | Trust, company credibility, industry mission |
| 2 | [Opportunity in the Reverse Mortgage Industry](#2-opportunity-in-the-reverse-mortgage-industry) | [rmopportunity](https://wm.waizmedia.net/reversemortgage/rmopportunity) | [YouTube](https://youtu.be/wlGAgHRX_QI) | Market size, urgency, educate-first vs. sell-first |
| 3 | [What Makes Waiz Media Different?](#3-what-makes-waiz-media-different) | [whatmakesusdifferent](https://wm.waizmedia.net/reversemortgage/whatmakesusdifferent) | [YouTube](https://youtu.be/uYr9nfeGHHs) | vs. other agencies; 3-part system (content, booked appts, infra) |
| 4 | [Burnt By Different Companies?](#4-burnt-by-different-companies) | [burnt](https://wm.waizmedia.net/reversemortgage/burnt) | [YouTube Short](https://youtu.be/8sqNYp6T3Vg) | Burned by agencies; fear + why generic reverse marketing fails |
| 5 | [Leads Aren't Everything](#5-leads-arent-everything) | [leads](https://wm.waizmedia.net/reversemortgage/leads) | [YouTube Short](https://youtu.be/HZf-n-7DDm8) | Leads-only model broken; what LOs should track instead |
| 6 | [Do We Guarantee Results?](#6-do-we-guarantee-results) | [doweguaranteeresults](https://wm.waizmedia.net/reversemortgage/doweguaranteeresults) | [YouTube Short](https://youtu.be/Km5e5lM5mrw) | Guarantee objection; vs. pay-per-result; what Waiz guarantees |
| 7 | [How Does Our Reverse Sales Team Work?](#7-how-does-our-reverse-sales-team-work) | [callcenter](https://wm.waizmedia.net/reversemortgage/callcenter) | [YouTube](https://youtu.be/RgjA7v6K3lk) | Dial team / assistants; speed + persistence; vs. lead dumps |

Machine index: [pre-call-objection-videos-manifest.yaml](pre-call-objection-videos-manifest.yaml).

## Landing page copy (eyebrow + headline)

Use on each `wm.waizmedia.net/reversemortgage/*` page above the video embed. Eyebrow = small label; headline = primary H1.

| # | Page | Eyebrow | Headline |
|---|------|---------|----------|
| 1 | [whoweare](https://wm.waizmedia.net/reversemortgage/whoweare) | About Waiz Media | Why we built a company exclusively for reverse mortgage loan officers |
| 2 | [rmopportunity](https://wm.waizmedia.net/reversemortgage/rmopportunity) | The market opportunity | The reverse mortgage opportunity is larger — and more urgent — than most LOs realize |
| 3 | [whatmakesusdifferent](https://wm.waizmedia.net/reversemortgage/whatmakesusdifferent) | How we're different | What makes Waiz Media different from every other marketing agency |
| 4 | [burnt](https://wm.waizmedia.net/reversemortgage/burnt) | If you've been burned before | Why past agency experiences fail — and how we're built differently |
| 5 | [leads](https://wm.waizmedia.net/reversemortgage/leads) | Beyond lead lists | Leads aren't enough. Here's what actually moves your pipeline. |
| 6 | [doweguaranteeresults](https://wm.waizmedia.net/reversemortgage/doweguaranteeresults) | Our guarantee | Do we guarantee results? Yes — and here's exactly what that means. |
| 7 | [callcenter](https://wm.waizmedia.net/reversemortgage/callcenter) | Inside our operation | How our reverse sales team books qualified appointments on your calendar |

---

## 1. Why We Do What We Do

**ID:** `whoweare-why-we-do-what-we-do`

### Links

| Type | URL |
|------|-----|
| Prospect page (send this) | https://wm.waizmedia.net/reversemortgage/whoweare |
| YouTube | https://youtu.be/RYnwas5j7iI |

### Purpose

Establish trust and show prospects who Waiz is and why the company focuses on reverse mortgage LO acquisition — before the strategy call. Reduces “who are these guys?” and generic-agency skepticism.

### Objection / belief mapping

| WM category | Beliefs addressed |
|-------------|-------------------|
| **Uncertainty-based** | Trust in Waiz; credibility vs. another marketing vendor |
| **Context (not a single objection)** | Industry stigma; education vs. demand; referrals/recycled leads vs. a real system |

Pair with [Identity Core](../../company/doctrine-identity-core-april-26.md) and [WM Sales Intelligence Bible](../intelligence/wm-sales-intelligence-bible.md) for live call reframes.

### When to send

- After calendar book, before strategy / intro call (nurture sequence).
- When prospect is warm but hesitant about **partner fit** or **industry focus**.
- Landing page: “who we are” for ad traffic and retargeting.

### Key messages (for scripts & creative)

- LOs entered reverse because they believe in the product, not because it was easy.
- Reverse does not have a demand problem — it has a **marketing and education** problem.
- Reverse was left behind while the rest of mortgage modernized; outdated marketing worsened stigma.
- Waiz chose **reverse-only** (not a generic LO agency) to solve education at scale.
- People buy **outcomes** (payment relief, helping family, aging in place), not “a HECM.”
- Significant tested spend and angles → playbook LOs do not have to rebuild.
- Position: **strategic partner**, not vendor — systems + playbooks for predictable pipeline.

### Transcript

> Source: YouTube auto-captions (`RYnwas5j7iI`). Light cleanup for readability; verify against video if quoting verbatim in ads.

So, I want to take a minute to talk about why we do what we do. If you're like any of the other reverse LOs that we talk with, you didn't get into the business because it was easy. You got into it because you genuinely believed in the product that you were serving. You've seen reverses change people's lives, and yet every single day you're fighting an uphill battle against the stigma, misinformation, and the market that just doesn't get it.

And our company was built on one simple core belief, which is reverse mortgages don't have a demand problem, they have a marketing and education problem. For years I've watched this industry get left behind. While the rest of the mortgage world adopted modern marketing, the reverse space was stuck with outdated, ineffective strategies that only made the stigma worse. And I saw hundreds of talented, dedicated LOs, people who are great at their jobs, struggling to build a consistent business because they were forced to depend on unreliable referrals or waste their time with low-quality, recycled leads.

We decided to choose a different path. Instead of building another generic marketing agency that serves every single type of loan officer, we made a deliberate choice to focus exclusively on the reverse mortgage industry. And why, you may ask? Because we believe that solving the education problem is the single highest leveraging thing that you can do in the space, and that's something, honestly, that we're good at.

It's not as simple as just picking up a camera and talking about what reverse mortgages is. People don't buy products, they buy outcomes. They don't buy a HECM, they buy the peace of mind of eliminating their mortgage payment. They buy the joy of being able to help their grandkids with college, the security of knowing that they can age in place without financial stress.

Our core philosophy is that if you want to break the stigma, you have to connect to people on a deeper level, and you have to show them the use cases that match their life. And that's why we've tested millions of dollars of marketing in perfecting this system. We've tested hundreds of different angles, positions, stories just to find out what actually resonates with different types of homeowners in this country. We know what works, and just as importantly, we know what doesn't work. We built the playbook so you don't have to. We know how to speedrun your success because we've already made the most expensive mistakes for you.

Our job is to take this hard-earned knowledge and build an engine that lets you focus on the highest and best use of your time, which is closing deals and being on sales calls with homeowners in this demographic. We're not just a service provider, we are a strategic partner dedicated to do one thing, and it's giving you the tools, the systems, and the proven playbooks to build a predictable and scalable business that you deserve in this industry.

We're all in on this industry, and if you are, too, you're in the right place. So, we look forward to speaking with you on our next call.

---

## 2. Opportunity in the Reverse Mortgage Industry

**ID:** `rm-opportunity-industry`

### Links

| Type | URL |
|------|-----|
| Prospect page (send this) | https://wm.waizmedia.net/reversemortgage/rmopportunity |
| YouTube | https://youtu.be/wlGAgHRX_QI |

### Purpose

Show prospects that Waiz understands the reverse mortgage industry and the scale of the opportunity — and why **now** is the time to act. Pre-sells the macro case (demographics, equity, penetration) and the educate-first strategy before the strategy call.

### Objection / belief mapping

| WM category | Beliefs addressed |
|-------------|-------------------|
| **Uncertainty-based** | “Is reverse big enough?” / “Do you know this industry?” |
| **Logistical / logic-based** | “I’ll wait” / “referrals are enough” / “I just need to sell better” |
| **Context** | Stigma and bad marketing explain low penetration — opportunity is in the 98%, not fighting over the 2% |

Often pairs after [#1 Why We Do What We Do](#1-why-we-do-what-we-do) (trust → opportunity) or when prospect doubts market timing.

### When to send

- When prospect likes reverse but undervalues **market size** or **urgency**.
- Top-of-funnel ads and landing traffic (`rmopportunity`).
- Nurture before strategy call: “watch this, then we’ll show you the system on our call.”
- Counter: “reverse is niche,” “bad time,” “I’ll grow on referrals.”

### Key messages (for scripts & creative)

- By 2030: ~73M baby boomers 65+; ~11,000/day crossing that threshold this decade.
- Baby boomers hold ~**$17T** in home equity (2024 estimate) — largest housing wealth concentration in history.
- Reverse penetration ~**2%** of eligible market → **98% untapped**.
- Why not biggest mortgage channel yet: **education + stigma**, not lack of demand.
- Wrong fix: “be a better salesperson” or referrals/word-of-mouth alone.
- Waiz thesis: unlock the market with **education strategy** and trustworthy content **before** the sales conversation.
- **Educate first** → capture the 98%, not fight over the active 2%.
- CTA: book a call to learn how to capitalize.

### Transcript

> Source: YouTube auto-captions (`wlGAgHRX_QI`). Light cleanup; “Ways Media” corrected to Waiz Media. Verify against video for verbatim ad copy.

Okay, so you're probably here because you see the potential in reverse mortgages. And my goal in this short video is to prove that opportunity is bigger than you possibly can think. And the timing has never been better than it is right now. So, I'm going to start with the hard data here and just lay out the facts.

By 2030, the US Census Bureau projects that all 73 million baby boomers will be over the age of 65. And that's more than 11,000 Americans crossing that threshold every single day the rest of this decade. Which really means that there's going to be a huge tappable market to get into for reverse mortgages.

And this demographic isn't just aging, it's sitting on a mountain of wealth. As of 2024, baby boomers hold an estimate of $17 trillion in home equity. Let me repeat that, $17 trillion. This is the largest concentration of house wealth in all of history, and yet reverse mortgages has only penetrated about 2% of its eligible market, which is absolutely nuts. Where do you know where 98% of your tappable market does not hold the product you serve? And this isn't a niche product, it's a massively underserved super prime asset class.

So, the obvious question is, if the market is this massive, why isn't it the biggest channel in the mortgage industry? And honestly, the answer is simple. It's a massive education problem. For decades, reverse mortgages have been plagued by stigma and misinformation, and the industry's marketing has failed to build trust. And as a result, most homeowners either don't know about the product or they believe the myth from 20 years ago.

And I've seen a lot of loan officers try to solve this problem by becoming better sales people, but reality, we're attacking the wrong problem here. You can't sell to what people don't understand. And even more than that, you can't rely on growing your business off referrals and just hoping that this industry will grow off word of mouth. We need to attack the problem much more aggressively.

And that's the key philosophy here at Waiz Media, is that we recognize the key to unlocking the $17 trillion market isn't just a better sales pitch, it's a better education strategy. It's about breaking the stigma with higher quality, trustworthy content before the conversation ever begins.

So, when you shift from sell first to educate first, you stop fighting for the 2% of the market that's already active, and you start capturing the 98% that's been waiting for someone to finally explain this product the right way. Our mission is to re-educate the market and equip the best loan officers with the system to capitalize off of it.

And this isn't just another product line, it's the single largest, most underserved demographic and economic opportunity in the reverse mortgage world for the next 20 years. The only question is who will be there to capture it.

So, if you want to learn more on how you can take advantage of this opportunity and grow your reverse mortgage business, go ahead and book a call with us and we're looking forward to speaking with you.

---

## 3. What Makes Waiz Media Different?

**ID:** `what-makes-waiz-different`

### Links

| Type | URL |
|------|-----|
| Prospect page (send this) | https://wm.waizmedia.net/reversemortgage/whatmakesusdifferent |
| YouTube | https://youtu.be/uYr9nfeGHHs |

### Purpose

Sell prospects on how Waiz differs from generic marketing agencies and “leads in a CSV” vendors — before the strategy call. Frames the **three-part system**: education/content, booked appointments (not raw leads), and full acquisition infrastructure.

### Objection / belief mapping

| WM category | Beliefs addressed |
|-------------|-------------------|
| **Uncertainty-based** | “You’re like every other agency” / “Do you actually understand reverse?” |
| **Fear-based** | Burned by agencies; stock ads that look scammy; tire-kicker leads |
| **Logistical / logic** | “I just need leads” vs. need dial team + CRM; referrals vs. owning growth |

Pairs well after [#1](#1-why-we-do-what-we-do) and [#2](#2-opportunity-in-the-reverse-mortgage-industry) when prospect is comparing vendors or asking “what do you actually do?”

### When to send

- Prospect says they’ve tried agencies, Facebook ads, or lead vendors before.
- Before demo/strategy call when **differentiation** is the gap (not market size or trust alone).
- Landing page for mid-funnel traffic who already believe in reverse.

### Key messages (for scripts & creative)

- **Reverse-only** — not all LO types; laser focus vs. “everything to everyone.”
- Reverse has unique **stigma + marketing + infrastructure** problems; forward mortgage playbooks fail here.
- **Pillar 1 — Stigma:** content engine (hundreds of thousands invested); viral-style education; no generic stock “scam” ads; positions LO as trusted authority; qualified interest vs. tire kickers.
- **Pillar 2 — Booked appointments:** not CSV dumps or “here’s leads, good luck”; real dial team books qualified appointments; LO focuses on highest-leverage work (calls/closes).
- **Pillar 3 — Infrastructure:** AI-powered CRM, automation, follow-up — full end-to-end acquisition machine built for their business.
- Close: system is proven; question is readiness to stop depending on referrals and control growth → book call for fit.

### Transcript

> Source: YouTube auto-captions (`uYr9nfeGHHs`). Light cleanup. Verify against video for verbatim ad copy.

So, what makes us different from all the other marketing agencies out there that promise you the world? And to be clear, we're not just some typical agency and we especially don't work with any type of loan officer because we work exclusively only with reverse mortgage loan officers.

So, while all the other agencies out there are trying to be everything to everyone, we've made this strategic decision to focus only on reverses. And that laser focus is the foundation of our entire system because we recognize the challenges in this industry are completely unique. And we understand that reverse mortgages have a stigma, marketing and infrastructure problem. So when applying generic forward mortgage strategies to the space, it's a true recipe for failure. And that is why we have built a completely new model.

So this is a three-part system designed to solve three of the biggest bottlenecks in your business.

**First, we solve the stigma.** We've invested over hundreds of thousands to build a content engine that actually educates homeowners. We don't run generic stock copy-paste ads that scream scam. We create high-quality viral-style video content that breaks through misconceptions and positions you as a trusted authority in the industry. And this is how you get in front of homeowners who are genuinely interested and not just tire kickers.

**Second, we deliver booked appointments, not just lists of leads.** Other companies will dump a CSV file on your lap, say good luck, or maybe just run crappy Facebook ads and let you chase after the leads. We do take over the front end of your business completely. Our goal is for you to wake up to conversations with people who are qualified and expecting your call, not just throwing leads on your lap. So, we have a real person team that will dial all the leads on your behalf, book appointments for you, and do all the work so you can just focus on the highest leveraging activity in your business.

**And then lastly, we provide the infrastructure to support it all.** This isn't just about ads in a call center. We equip you with the AI-powered CRM and all the automation follow-up sequences you would need to manage your pipeline and convert conversations into closed deals. This is a full end-to-end client acquisition machine custom built for you and your business.

You see, we didn't build this by accident. We have a mission to completely transform how the world sees this product. And it starts by giving the best loan officers like you the leverage you deserve.

The question isn't whether the system works. We've already proven that. The real question is, are you ready to stop depending on referrals and finally take control of your business's growth? If so, we're looking forward to speaking with you on our call to go over more details and see if this is the right fit for you.

---

## 4. Burnt By Different Companies?

**ID:** `burnt-by-other-agencies`

### Links

| Type | URL |
|------|-----|
| Prospect page (send this) | https://wm.waizmedia.net/reversemortgage/burnt |
| YouTube Short | https://youtu.be/8sqNYp6T3Vg |

**Format:** YouTube Short (vertical). Source transcript includes a social CTA (“comment reverse” / DM); use the **prospect page** as the canonical send link for sales.

### Purpose

Handle the objection when prospects were **burned by other marketing agencies** — validate skepticism, explain why those experiences happen, and contrast with Waiz (reverse-only depth, booked appointments vs. lead dumps, founder fit in marketing/ops). Also frames why reverse mortgage marketing has been done wrong for years (generic templates, wrong demographic/psychology, multi-product agencies).

### Objection / belief mapping

| WM category | Beliefs addressed |
|-------------|-------------------|
| **Fear-based** | Burned before; garbage leads; agency ghosted; contract lock-in with no results |
| **Uncertainty-based** | Can I trust Waiz? / Is this another template shop? |
| **Context** | Why forward/generic mortgage marketing fails in reverse (stigma, psychology, objections, demographic) |

**Jump-send:** Use as soon as prospect shares agency horror stories — does not have to wait for #1–#3. Often pairs with [#3 What Makes Waiz Different](#3-what-makes-waiz-media-different).

### When to send

- Live objection: “I tried an agency before…” / “ads didn’t work” / “leads were trash.”
- Setter notes: prior vendor, chargeback energy, high skepticism on call 1.
- Retargeting creatives for prospects who engaged but stalled after bad vendor history.

### Key messages (for scripts & creative)

- Skepticism after being burned is **rational**, not rude.
- Common failures heard on calls: garbage leads, money gone, locked contracts, zero results.
- **Why it happened:** agencies serve every LO product (DSCR, HELOC, purchase, etc.) → templates, not reverse-specific depth.
- Reverse borrower: different stigma, psychology, objections, demographic → marketing must be different.
- Skepticism of **LO-turned-agency** models: different business (sales vs. marketing ops); “if the system worked, why leave highest-paying LO role?”
- Gabriel’s credibility frame: marketing/operations background, reverse-only focus.
- **Waiz contrast:** booked appointments on calendar, not “contact in a CRM bow.”
- Root issue: industry marketed reverse **incorrectly for years**, not that “ads don’t work.”

### Transcript

> Source: YouTube auto-captions (`8sqNYp6T3Vg`). Short-form; ends with social CTA. Light cleanup.

If you were burnt by another marketing agency before, I don't blame you for being skeptical. In fact, I'd probably be worried if you weren't, right? We hear this on almost every single call. I tried ads before and the leads were garbage. My agency took my money and disappeared. I got locked into a contract and saw zero results. And every time I hear that, it genuinely pisses me off because those agencies make it much harder for the ones actually doing the work to earn your trust.

So, let me tell you exactly why those experiences happened and what we do differently.

**First, we only work with reverse mortgage loan officers.** I think this is pretty much obvious as most agencies literally take any loan officer that walks through the door. Whether it's DSCRs, HELOCs, commercials, purchases, it does not matter. If you have a budget, they have a proposal for you. And the problem with that is that you cannot be great at everything. The reverse mortgage borrower is completely different and has completely different behaviors than a first-time home buyer. The stigma is different, the psychology is different, the objections are different, the demographic is completely different. The entire marketing approach has to be different, too.

So, when you see an agency splitting their attention across every product in the mortgage space, the quality gets diluted. You are not getting their best thinking, you're getting their template with your name on it. So, not only do we love this space so much, but we made a decision to focus all our attention on it and be freaking good. We went all in. One demographic, one product, every single ad that we've written, every funnel we've built, every follow-up sequence we've deployed has been built exclusively for reverse mortgage loan officers. Guys, you can see that depth is so much different than recycled campaigns.

And one of the things that really baffle me is that there's loan officers out there who left their high-paying career to start a marketing agency because their system happened to be so good and they want to give it to you. And I don't want to throw stones at anyone here, but if you just think about that for a second, running a marketing agency is a completely different sport. Different skill set, different operations, literally different everything. It's a whole different business. If you really put your mind to it, it's not a logical nor natural next step to jump from being a high producer as a loan officer to starting a marketing agency because it's really just a whole different career.

As the same thing goes for me, I can't step into your shoes and start selling reverse mortgages cuz we know how to generate the leads. So, if the system they had was genuinely working that well, why leave? Why walk away from the highest-paying position in the mortgage industry to go build something from scratch? You see, the math just doesn't add up and that disconnect, I can't really explain, but my heart has always been here in marketing, in operations. I love what we do here. I love the reverse mortgage industry, and I'm here for a reason, and I think that really matters when you're deciding on who to trust with your front end of your business.

**Now, second thing is, we don't just send you leads, we book appointments onto your calendar.** Most agencies just hand you a contact and consider their job done. And they might just wrap it in a bow with a pretty CRM and make it look all fancy when it's really just a normal tool that we all use.

So, comment down reverse below and I will send you that exact playbook to your or DM me.

> **Note:** Final lines are Short-native CTA. On the [burnt prospect page](https://wm.waizmedia.net/reversemortgage/burnt), confirm embed ends with your standard book-a-call CTA for sales sends.

## Suggested sequence

| Order | Asset | Role |
|-------|-------|------|
| 1 | Why We Do What We Do | Trust + mission |
| 2 | Opportunity in the Reverse Mortgage Industry | Market proof + urgency + educate-first |
| 3 | What Makes Waiz Media Different? | Differentiation + offer mechanics (3 pillars) |
| 4 | Burnt By Different Companies? | Fear / burned-by-agency objection (**can jump ahead when objection surfaces**) |
| 5 | Leads Aren't Everything | Reframe leads-only vendors; metrics beyond lead count (**pairs with #3–#4**) |
| 6 | Do We Guarantee Results? | Guarantee / pay-per-result objection (**jump-send when guarantee comes up**) |
| 7 | How Does Our Reverse Sales Team Work? | Call center / dial team depth (**pairs with #3 pillar 2, #6**) |

---

## 5. Leads Aren't Everything (Here's What Loan Officers Should Track Instead)

**ID:** `leads-arent-everything`

### Links

| Type | URL |
|------|-----|
| Prospect page (send this) | https://wm.waizmedia.net/reversemortgage/leads |
| YouTube Short | https://youtu.be/HZf-n-7DDm8 |

**Format:** YouTube Short (vertical). Source transcript includes social CTA; use **prospect page** as canonical send link for sales. Opens mid-argument (“And that’s all fine at first…”) — may be part 3 of a Short series on the page.

### Purpose

Explain why the **leads-only model** that dominated reverse mortgage marketing for the past decade is broken — and that sustainable success takes more than generating more leads. Pre-handles “you’re just another lead agency” by reframing what actually matters: contact science, dial team, booked appointments, and **transparent metrics** (dashboard), not a monthly lead report.

### Objection / belief mapping

| WM category | Beliefs addressed |
|-------------|-------------------|
| **Uncertainty-based** | “Waiz is like every other agency” / “you only sell leads” |
| **Logistical / logic-based** | “I just need more leads” / lead count as the wrong north star |
| **Context** | Why the old lead-gen playbook failed even when vendors delivered “leads” |

**Jump-send:** When prospect compares Waiz to CSV/lead vendors or fixates on CPL/lead volume. Pairs with [#3](#3-what-makes-waiz-media-different) (full system) and [#4](#4-burnt-by-different-companies) (burned on garbage leads).

### When to send

- Objection: “I only care about cost per lead” / “how many leads per month?”
- Prospect equates marketing success with lead list size.
- After #4 when they were burned but still think the answer is *more* leads, not a different model.

### Key messages (for scripts & creative)

- **Reaching prospects changed:** spam filters, call screening, channel/timing — not the same game as 10 years ago; nurture is a full-time job.
- Most agencies **hand you a list** and expect you to solve decades of consumer-behavior shift alone.
- Waiz: every lead **called by real humans** (reverse sales team), pre-qualified, objections handled, **appointment on calendar** — LO shows up to sell.
- **Transparency:** live dashboard — every lead, call, appointment, dollar spent; no monthly “trust me” reports.
- Not ads + email report — **full front end** (ads, funnel, follow-up science, live setters, booked appointments) running in background.
- **Infrastructure compounds** over time (data improves, cost per appointment drops) vs. a 90-day campaign you turn off.
- Replaces **referral dependency** long-term.

### Transcript

> Source: YouTube auto-captions (`HZf-n-7DDm8`). Light cleanup (“life setters” → live setters). Verify against video for verbatim ad copy.

And that's all fine at first until you realize that actually getting a hold of someone nowadays is a completely different game than it was 10 years ago. Spam blockers are way more advanced. People screen calls completely different. The way someone makes decisions, the way they respond to a text, the timing, the message, the channel, all of it has changed. It used to be so much simpler. You'd call, they picked up, and things would be so much smoother. But now there's a whole science to it, and we've spent years figuring it out, testing hundreds of different funnels, scripts, text sequences, call timing strategies, follow-up cadences to find out what actually gets reverse mortgage prospects to actually pick up, respond, and show up on the call. You know, not to stress on it. It's literally a full-time job on its own.

And most agencies aren't doing it correctly. They literally just hand you a list and expect you to figure out a decades' worth of consumer behavior shifts on your own. And we handle all of it. Every lead that will come into your funnel will be called directly from our reverse sales team that's real people, not AI callers. They pre-qualify the prospect, handle the initial objections, and put a booked appointment directly on your calendar. So, you're not chasing anyone. You just show up and focus on what you do best, which is taking sales calls.

The third thing is you get full transparency and full scope of the project. You have always access to your dashboard. You can see every lead that comes in, every call that we make, every appointment we book, every dollar spent. You're not waiting on monthly reports being emailed to you to tell you what you want to hear. You log in at any time and see exactly what's happening in real time. So, there's no surprises, there's no secrets, and there's no excuses. Just numbers for you so you can understand where your business is at.

So, I just want to be clear here. We're not just some marketing agency that runs ads and emails you a report at the end of the month. That's not what this is. What we built is an entire front end of your business, the ads, the funnel, the follow-up science, and the live setters, the booked appointments, all of it done for you, running in the background while you focus on closing.

Most agencies are a cost and this infrastructure compounds the longer it runs, the data it has, better it performs and lower your cost per appointment gets. This isn't just a campaign you turn on for 90 days and evaluate. This is a system that replaces the referral dependency you've been living with for years.

So, comment down reverse below and I will send you that exact playbook to your DMs.

> **Note:** Final lines are Short-native CTA. Confirm [leads prospect page](https://wm.waizmedia.net/reversemortgage/leads) uses book-a-call CTA for sales sends.

---

## 6. Do We Guarantee Results?

**ID:** `do-we-guarantee-results`

### Links

| Type | URL |
|------|-----|
| Prospect page (send this) | https://wm.waizmedia.net/reversemortgage/doweguaranteeresults |
| YouTube Short | https://youtu.be/Km5e5lM5mrw |

**Format:** YouTube Short (vertical). Source transcript includes social CTA; use **prospect page** as canonical send link for sales.

### Purpose

Break the **guarantee objection** — what Waiz guarantees vs. competitor “pay per close / pay per appointment” offers that sound safer but misalign incentives. Pre-handles skepticism on guarantees before the strategy call.

### Compliance (read before live use)

This video states **specific guarantee numbers** (e.g. 50 qualified conversations in 90 days, work-for-free clause). Per [Money Model](../../company/overview-money-model-april-26.md), pricing and deal terms are **founder-only**. Confirm current offer language on every call and in ad copy; do not let AI invent or drift from the live agreement.

### Objection / belief mapping

| WM category | Beliefs addressed |
|-------------|-------------------|
| **Uncertainty-based** | “Do you guarantee results?” / “What if it doesn’t work?” |
| **Fear-based** | Burned before; need a “safe” pay-per-result structure |
| **Logistical / logic** | Pay-per-appointment sounds lower risk; volume = success |

**Jump-send:** As soon as prospect mentions guarantees, pay-per-close, or a competitor’s “too good to be true” offer. Pairs with [#5](#5-leads-arent-everything) (volume vs. quality) and [#3](#3-what-makes-waiz-media-different) (full system).

### When to send

- Objection: “What’s your guarantee?” / “Other agency only charges per appointment.”
- Prospect comparing Waiz to pay-per-result vendors.
- Before demo when **offer clarity** is blocking the book.

### Key messages (for scripts & creative)

- **Yes, Waiz guarantees results** — but define what that means vs. industry gimmicks.
- **Warning on pay-per-close / pay-per-appointment:** often new agencies using your ad spend to learn; you fund their education.
- **Misaligned incentive:** paid per booking → volume over quality → tire-kickers, no-shows, bad fits.
- **Waiz preference:** fewer, **pre-screened** homeowners who understand the product vs. flooding calendar with cold leads.
- **Waiz guarantee (as stated in video):** 50 conversations with **qualified** homeowners in your area in 90 days; work for free if not met — **verify live terms.**
- **Why conversations are warmer:** education-first funnel, video content, stigma addressed, team contact before LO calendar.
- **Vetting:** team qualifies age, LTV, etc. before LO call — not booking unqualified profiles to hit a number.
- **Due diligence questions** for competitors: niche tenure, # of RM LO clients, written process/proof.
- Social CTA at end; use landing page for sales sends.

### Transcript

> Source: YouTube auto-captions (`Km5e5lM5mrw`). Light cleanup (“pre-season” → pre-screened, “dressed” → addressed). Verify guarantee numbers against live offer before quoting.

So, do we guarantee results? And let me be completely straight with you. Yes, we do. But, before I tell you exactly what that looks like, I want you to be very careful about the guarantees you're seeing out there right now. Because if you've been on calls with agencies promising you a pay per close or pay per appointment, I want you to ask yourself one question. Why would a serious agency need to structure in that specific way?

Well, because what we found out while working in the marketing agency for so long is that these agencies offering those type of models almost always do it for one reason. It's cuz they're new. They need your ad spend to learn the process. And they're willing to take the risk of a pay per result model because they have nothing to lose. You are the one funding their education.

And here's one of the other problems about those models that no one talks about. When an agency gets paid for whenever they book an appointment on your calendar, what do you think that incentivizes them to do? Push volume, book anyone, sacrifice quality over quantity. So, instead of getting 10 pre-qualified homeowners who need a reverse mortgage and are genuinely interested, you get about 40 people who barely remember clicking on the ad or don't even show up on the call. And if they even get on the call, the call goes nowhere. It's just a waste of your time. And that's not a system, that's a numbers game at your expense.

And we don't want our incentives to be misaligned with yours. We'd rather put 15 pre-screened homeowners on your calendar who already understand the product than flood you with 60 cold leads that burn your time and kill your confidence in the process.

So, let me tell you exactly how our guarantee works. We actually guarantee you 50 conversations with qualified homeowners in your area within the next 90 days. And if we don't get that, we'll work for free.

Let me tell you this. First, the leads coming into your calendar have already been through our full process, our education-first system. They've already watched video content that explains the product. They've addressed the stigma. They've gone through our full funnel process. They've talked to our team. And by the time they hit your calendar, they're not even cold anymore. They're warm. They're informed about who you are as an individual, and they show up because they want to be there.

Second, we're guaranteeing conversations with people who are actually qualified. So, our team actually calls them and vets them to make sure their LTV, their age is all in check before they hop on the call with you. We're not booking like 50-year-olds with 70 LTVs and just burn your time. So, not only is there intent there, but they're also pre-vetted so that when you actually hop on the call with them, it's going to be a substantial conversation that hopefully goes somewhere.

So, to answer the question that's on the top of your mind, yes, we guarantee results. Yes, our incentives are completely aligned with yours. And so, if you're talking with another agency that has a offer that seems just too good to be true, like a pay per result that just mathematically seems improbable for them, ask them how long they've been in this niche for. Ask them how many reverse mortgage loan officers they have worked with. And really dive deep into their processes, their infrastructure, and if they don't have it written or any proof of it, it's just a bunch of bogus and they're telling you what you want to hear. The answers are going to tell you everything you need to know within that.

So, if you want to learn more, if you want to get our playbook on exactly how everything works front to end, go ahead and comment reverse marketing and we'll go ahead and DM you our written playbook.

> **Note:** Final lines are Short-native CTA. Confirm [doweguaranteeresults prospect page](https://wm.waizmedia.net/reversemortgage/doweguaranteeresults) uses book-a-call CTA for sales.

---

## 7. How Does Our Reverse Sales Team Work?

**ID:** `reverse-sales-team-call-center`

### Links

| Type | URL |
|------|-----|
| Prospect page (send this) | https://wm.waizmedia.net/reversemortgage/callcenter |
| YouTube | https://youtu.be/RgjA7v6K3lk |

**Format:** Long-form (not a Short).

### Purpose

Explain Waiz’s **reverse sales assistant** operation — why the dial team matters, how it works, and how it differentiates from agencies that only deliver leads or generic call centers. Pre-handles “I’ll dial my own leads” and “call centers hurt my brand.”

### Objection / belief mapping

| WM category | Beliefs addressed |
|-------------|-------------------|
| **Uncertainty-based** | “Is this a generic offshore call center?” / “Will this hurt my brand?” |
| **Logistical / logic-based** | “I can follow up myself” / “I don’t need a team” / speed-to-lead doesn’t matter |
| **Context** | Supports [#3](#3-what-makes-waiz-media-different) pillar 2 (booked appointments) and [#6](#6-do-we-guarantee-results) (pre-vetted conversations) |

**Jump-send:** When prospect asks how follow-up works, who dials leads, or compares Waiz to ads-only vendors.

### When to send

- After [#3](#3-what-makes-waiz-media-different) when they want **depth on the dial team**.
- Objection: “I don’t want a call center” / “I’ll work my own leads.”
- Before strategy call when **operations credibility** is the gap.

### Key messages (for scripts & creative)

- **100% real humans** (not AI) with reverse/borrower conversation experience — stigma, objections, demographic nuance.
- **Pre-filter before LO sees lead:** LTV, age, geographic area — no “throw crap at the wall.”
- **Positioning:** team brands as the LO’s **assistant**, not third-party call center → prospect sees LO as established operator.
- **Beyond booking:** qualify, handle RM objections, educate on product; optional live transfers; heavy lifting done before LO call.
- **Per-LO training:** licensed states, who the LO is, how they operate — sounds like front desk of LO’s office.
- **Speed:** MIT-cited frame — contact within **5 minutes** of opt-in (900% drop if slower); team calls within minutes, **6 days/week**.
- **Persistence:** multiple attempts per day across days; **80%+** of leads need **5+** contact attempts; most agencies quit after 1–2.
- **LO reality:** no time for 50–100 daily dials while wearing every other hat.
- **Outcome:** calendar of **pre-qualified appointments**, not a list of names that don’t pick up.

### Transcript

> Source: YouTube auto-captions (`RgjA7v6K3lk`). Light cleanup. Verify MIT/stat claims if used verbatim in regulated copy.

So, let me walk you inside our reverse sales assistant operation because this is honestly one of the secret weapons that separate us from every other marketing agency in this space.

First off, our team is 100% real humans, not AI, and they have real experience in talking with borrowers. They understand the product, they understand the stigma, they understand all the objections, and they've been trained specifically on how to have these conversations with these type of homeowners because quite frankly, this demographic is different.

Now, here's where it gets different from anything else you've probably seen out there because before we even bring you a lead, we filter based on LTV, age, and your specific area. So, instead of throwing a bunch of crap at the wall and hoping something sticks, instead, every person entering your pipeline has already been pre-screened to match the criteria that actually matters for your reverse mortgage business.

So, not only is the team pre-vetting and spot-checking these leads to make sure they're worth your time, but they're branding themselves as your assistant, not a call center, not a third-party vendor, your assistant. So, from the prospect's perspective, you already have an operation. You're already the leading professional in this space. That positioning alone changes the entire dynamic of the conversation before you ever pick up the phone.

And yeah, they're not only just booking appointments or even doing live transfers to you. They're not only qualifying, but they're asking the right questions, they're handling objections on reverse mortgages, and educating the prospect on what the product actually does. So, by the time that call hits your calendar, you're not starting from scratch. So, really the hardest part's already done. All the heavy lifting is done for you.

We also train the team specifically on you as well. The states you're licensed in, who you are, how you operate, and so when they get on the phone, they don't just sound like a generic call center, they sound like they're sitting at the front desk of your office.

So, now that I covered how they work, let's talk about the science and cadence behind the system and our process because this is typically where most outlets go wrong when they're trying to manage their own database by themselves and why their system falls apart.

MIT did a study showing that your chance of reaching a lead drops by 900% if you wait longer than 5 minutes after they opt in. 900%. So, the moment someone fills out a form on your page, our team is on the phone. Not in an hour, not at the end of the day, within minutes. And this is 6 days a week.

But speed is really only half of it. The other half is the persistence and timing. So, our team calls your leads multiple times throughout the day across multiple days because that's what data shows — that over 80% of leads require at least five contact attempts before they pick up. Most agencies give up after two or maybe even one. And this is another big reason why you can't handle your own nurturing process on your own. You're wearing all the hats in the business. The last thing you have time for is to be doing 50 to 100 dials a day on your cold database.

And that's the operation. That's what consistency looks like and that's what it means to wake up with a calendar full of pre-qualified appointments instead of a list of names that don't pick up.

## Related Docs

- [Objection Handling Hub](../sales/objection-handling-hub.md)
- [WM Objection Categories](../sales/wm-objection-categories.md)
- [Marketing README](README.md)
- [Sales Operating Hub](../sales/README.md)
