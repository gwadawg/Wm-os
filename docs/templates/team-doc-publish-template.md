---
title: Team Doc Publish Template
domain: templates
owner: operations
status: active
last_updated: 2026-05-21
review_cycle: quarterly
---

# Team Doc Publish Template

Design-focused specification for Google Drive team docs. Translation skill: [.claude/skills/team-doc-translate/SKILL.md](../../.claude/skills/team-doc-translate/SKILL.md). Code: `scripts/lib/team_doc_translator.py`.

## Document structure (required order)

1. **Title** — benefit-oriented plain English
2. **At a glance** — who, when, outcome, time estimate, escalate-to
3. **What this is for** — 2–4 sentences
4. **Before you start** — prerequisites (bullets)
5. **How to do it** — phased numbered steps (not raw Operating Content dump)
6. **Done right looks like** — short checklist bullets
7. **When to get help** — who and when to escalate
8. **Related procedures** — hyperlinks to published team Docs only
9. **Footer** — published date, owner role, ref slug (no GitHub)

## Design principles

- Scannable in 60 seconds: at-a-glance + first phase visible without scrolling endlessly
- One idea per bullet; no paragraph over 4 lines
- Title Case subheadings — never ALL CAPS walls
- Tables and broken schedules → summarized bullets or phases
- Second-person action voice where natural
- Callouts (`▸ IMPORTANT`, `▸ TIP`) for rare must-know rules only

## Never include

- YAML, `source_document`, Open Questions, migration notes
- Links to `_inventory/`, `SPINE.md`, `SOURCE-OF-TRUTH.md`, `kpis/`
- Specific pricing (escalate to Gabriel)
- AI metadata (`domain:`, `artifact_type:`, `review_cycle`)

## Related docs

- [Team Drive Publish SOP](../operations/systems/team-drive-publish.md)
- [team-publish-registry.yaml](../_inventory/team-publish-registry.yaml)
- [team-doc-translate skill](../../.claude/skills/team-doc-translate/SKILL.md)
