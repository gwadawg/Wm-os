# Agents — Waiz Media OS

This repository is the Waiz Media operating system. Agents should treat `docs/` as canonical truth and `source-docs/` as read-only exports.

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
| Translate docs for team readability | [.claude/skills/team-doc-translate/SKILL.md](.claude/skills/team-doc-translate/SKILL.md) |
| Publish team Google Docs (one-way from `docs/`) | [.claude/skills/team-doc-publish/SKILL.md](.claude/skills/team-doc-publish/SKILL.md) |

Full index: [.claude/skills/README.md](.claude/skills/README.md)

## Do not

- Edit files under `source-docs/waiz-drive-export/`
- Create duplicate canonical docs (check `docs/_inventory/duplicate-resolutions.md`)
- Quote pricing not in an approved pricing sheet
