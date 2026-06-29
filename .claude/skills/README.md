# Waiz Media OS — Agent Skills

Skills in this folder are **repo-local**. Cursor and Claude Code discover them from `.claude/skills/<name>/SKILL.md`.

## Content & marketing

| Skill | Path | Use when |
|-------|------|----------|
| **content-engine** | [content-engine/SKILL.md](content-engine/SKILL.md) | Weekly ideas, `/weekly-ideas`, `/script`, reels, carousels, trial concepts |
| **EditorProjectcreator** | [editor-project-creator/SKILL.md](editor-project-creator/SKILL.md) | Editor projects from calls; `/new-repurpose-project`, `/push-clip`, `/archive-project` — [lifecycle](../../docs/content-engine/personal/projects/lifecycle.md) |
| **creator-research** | [creator-research/SKILL.md](creator-research/SKILL.md) | Apify capture, viral format decomposition, `/apify-capture`, `/remix` |
| **knowledge-capture** | [knowledge-capture/SKILL.md](knowledge-capture/SKILL.md) | Paste transcript/call/research → update hook/angle/belief libraries |
| copywriting | [copywriting/SKILL.md](copywriting/SKILL.md) | Hooks, captions, carousel copy |
| ugc-scriptwriter | [ugc-scriptwriter/SKILL.md](ugc-scriptwriter/SKILL.md) | UGC / talking-head scripts |
| marketing-psychology | [marketing-psychology/SKILL.md](marketing-psychology/SKILL.md) | Angles, persuasion |
| brainstorming | [brainstorming/SKILL.md](brainstorming/SKILL.md) | Deep ideation |
| rm-creative-studio | [rm-creative-studio/SKILL.md](rm-creative-studio/SKILL.md) | Reverse mortgage ad creative |
| rm-fulfillment-agent | [rm-fulfillment-agent/SKILL.md](rm-fulfillment-agent/SKILL.md) | RM fulfillment — drips, bot, objections, lifecycle |
| linkedin-lo-outreach | [linkedin-lo-outreach/SKILL.md](linkedin-lo-outreach/SKILL.md) | LO outbound |
| pre-call-objection-videos | [pre-call-objection-videos/SKILL.md](pre-call-objection-videos/SKILL.md) | Nurture video manifest |

**Content engine hub:** [docs/content-engine/README.md](../../docs/content-engine/README.md) · [.agents/product-marketing.md](../../.agents/product-marketing.md)

Reference files: [content-engine/weekly-workflow.md](content-engine/weekly-workflow.md), [content-engine/format-templates.md](content-engine/format-templates.md), [knowledge-capture/routing-table.md](knowledge-capture/routing-table.md)

## Required for documentation work

| Skill | Path | Use when |
|-------|------|----------|
| **Waiz Business OS** | [waiz-business-os/SKILL.md](waiz-business-os/SKILL.md) | Any work in `docs/`, migration, SOPs, KPIs, repo structure, company operations — team Drive copies match [Objection Categories format](https://docs.google.com/document/d/19creUTdx5cTwWJVjdX3qPUMY40v1z379bCNoieY_Q5Y/edit) |
| **SOP Builder** | [sop-builder/SKILL.md](sop-builder/SKILL.md) | Brainstorm or build a new SOP/playbook/guide from scratch — guides discovery, picks the right doc type, maps to the correct folder, drafts the file, and offers Drive publish |
| **LinkedIn LO outreach** | [linkedin-lo-outreach/SKILL.md](linkedin-lo-outreach/SKILL.md) | LinkedIn DMs to reverse mortgage LOs — entry: [outbound/linkedin/manifest.yaml](../../docs/acquisition/outbound/linkedin/manifest.yaml) |
| **Pre-call objection videos** | [pre-call-objection-videos/SKILL.md](pre-call-objection-videos/SKILL.md) | Prospect nurture videos before strategy/demo — [manifest](../../docs/acquisition/marketing/pre-call-objection-videos-manifest.yaml) |
| **DOCX** | [docx/SKILL.md](docx/SKILL.md) | Reading or converting `.docx` from **waiz-os-archive** (`waiz-drive-export/`) |
| **XLSX** | [xlsx/SKILL.md](xlsx/SKILL.md) | Sales trackers, scorecards, spreadsheets — summarize in Markdown, keep raw file |
| **Team doc author** | [team-doc-author/SKILL.md](team-doc-author/SKILL.md) | Rewrite canonical docs into publish-ready team drafts (faithful render). Default authoring step |
| **Team doc translate** | [team-doc-translate/SKILL.md](team-doc-translate/SKILL.md) | Legacy heuristic scaffold for team drafts (optional starting point) |
| **Team doc publish** | [team-doc-publish/SKILL.md](team-doc-publish/SKILL.md) | One-way publish of approved `docs/` to team Google Drive (layperson-readable) |

Waiz Business OS references:

- [OPERATING_FRAMEWORK.md](waiz-business-os/OPERATING_FRAMEWORK.md)
- [TEMPLATES.md](waiz-business-os/TEMPLATES.md)

## Optional (by task)

| Skill | Use when |
|-------|----------|
| [rm-creative-studio/SKILL.md](rm-creative-studio/SKILL.md) | Brainstorm reverse-mortgage ad ideas and write compliant video ad scripts for client fulfillment — engine: [creative-studio/](../../docs/client-fulfillment/media-buying/creative-studio/README.md) |
| [rm-fulfillment-agent/SKILL.md](rm-fulfillment-agent/SKILL.md) | RM client fulfillment — drips, bot copy, objections, lifecycle, sub-agent design — deploy: [reverse-mortgage-agent/chatbot-deploy/](../../docs/client-fulfillment/reverse-mortgage-agent/chatbot-deploy/README.md) |
| [ugc-scriptwriter/SKILL.md](ugc-scriptwriter/SKILL.md) | Draft **generic** (non-RM) UGC scripts — talking-head, testimonial, creator — from a hook + product. For reverse-mortgage client ads use [rm-creative-studio](rm-creative-studio/SKILL.md) (compliance gate) |
| [copywriting/SKILL.md](copywriting/SKILL.md) | Marketing copy, landing pages, email voice |
| [pre-call-objection-videos/SKILL.md](pre-call-objection-videos/SKILL.md) | LO prospect video sends, transcripts, ad/nurture alignment |
| [marketing-psychology/SKILL.md](marketing-psychology/SKILL.md) | Mental models, persuasion, buyer psychology for messaging and offers |
| [linkedin-lo-outreach/SKILL.md](linkedin-lo-outreach/SKILL.md) | LinkedIn outbound — start at `docs/acquisition/outbound/linkedin/manifest.yaml` |
| [senior-prompt-engineer/SKILL.md](senior-prompt-engineer/SKILL.md) | Prompt libraries under `docs/prompts/` |
| [file-organizer/SKILL.md](file-organizer/SKILL.md) | Large folder cleanup proposals (propose before moving) |
| [brainstorming/SKILL.md](brainstorming/SKILL.md) | New product/process design before writing docs |
| [senior-architect/SKILL.md](senior-architect/SKILL.md) | CRM/automation architecture specs |

## Repo entry points (read before skills)

1. [CLAUDE.md](../../CLAUDE.md)
2. [docs/README.md](../../docs/README.md)
3. [docs/SOURCE-OF-TRUTH.md](../../docs/SOURCE-OF-TRUTH.md)
4. [docs/_inventory/migration-backlog.md](../../docs/_inventory/migration-backlog.md)
