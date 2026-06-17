# Agents — Waiz Media OS

This repository is the Waiz Media operating system. Agents should treat `docs/` as canonical truth. Raw Drive exports live in the sibling **waiz-os-archive** repo — see [raw-export-archive.md](docs/_inventory/raw-export-archive.md).

## Start here

1. [CLAUDE.md](CLAUDE.md)
2. [docs/README.md](docs/README.md)
3. [docs/SOURCE-OF-TRUTH.md](docs/SOURCE-OF-TRUTH.md)

## Skills (required)

| Task | Skill |
|------|--------|
| Business docs, migration, SOPs | [.claude/skills/waiz-business-os/SKILL.md](.claude/skills/waiz-business-os/SKILL.md) |
| Word export conversion | [.claude/skills/docx/SKILL.md](.claude/skills/docx/SKILL.md) |
| Spreadsheet wrappers | [.claude/skills/xlsx/SKILL.md](.claude/skills/xlsx/SKILL.md) |
| Author a team Google Doc draft (rewrite for readability) | [.claude/skills/team-doc-author/SKILL.md](.claude/skills/team-doc-author/SKILL.md) |
| Translate docs for team readability (legacy scaffold) | [.claude/skills/team-doc-translate/SKILL.md](.claude/skills/team-doc-translate/SKILL.md) |
| Publish team Google Docs (author → approve → faithful publish) | [.claude/skills/team-doc-publish/SKILL.md](.claude/skills/team-doc-publish/SKILL.md) |
| LinkedIn LO outreach (DMs, SN, angles) | [.claude/skills/linkedin-lo-outreach/SKILL.md](.claude/skills/linkedin-lo-outreach/SKILL.md) |
| Pre-call objection videos (nurture URLs, transcripts, setter sends) | [.claude/skills/pre-call-objection-videos/SKILL.md](.claude/skills/pre-call-objection-videos/SKILL.md) — [manifest](docs/acquisition/marketing/pre-call-objection-videos-manifest.yaml) |
| **Content ideation + scripting (personal / business / client lanes)** | [.claude/skills/content-engine/SKILL.md](.claude/skills/content-engine/SKILL.md) — [content engine hub](docs/content-engine/README.md) |
| **Transcript / research → knowledge base updates** | [.claude/skills/knowledge-capture/SKILL.md](.claude/skills/knowledge-capture/SKILL.md) |

Full index: [.claude/skills/README.md](.claude/skills/README.md)

**Content engine entry:** [docs/content-engine/README.md](docs/content-engine/README.md) — [infrastructure](docs/content-engine/INFRASTRUCTURE.md), [lane boundaries](docs/content-engine/LANE-BOUNDARIES.md), archive policy.

**Product marketing context:** [.agents/product-marketing.md](.agents/product-marketing.md) — Waiz Media positioning for business-lane content.

**Team SOP layout:** Author draft (agent rewrite per [authoring contract](docs/templates/wm-team-draft-authoring-contract.md) + [doc-type profile](docs/templates/wm-team-doc-profiles.yaml)) → approve → faithful publish (renders the draft 1:1). Match [WM Objection Categories](https://docs.google.com/document/d/19creUTdx5cTwWJVjdX3qPUMY40v1z379bCNoieY_Q5Y/edit). See [team-drive-publish.md](docs/operations/systems/team-drive-publish.md).

## Do not

- Edit files under `waiz-os-archive/waiz-drive-export/` (or legacy `source-docs/` if still present locally)
- Create duplicate canonical docs (check `docs/_inventory/duplicate-resolutions.md`)
- Quote pricing not in an approved pricing sheet
- Store full transcripts or Apify JSON dumps in the OS repo — use `wm-content-archive/` sibling folder
