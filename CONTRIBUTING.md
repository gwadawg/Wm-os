# Contributing to Waiz Media OS

This repo is the Waiz Media operating system. `docs/` is the source of truth. Contributors build new SOPs and processes here; the repo owner reviews every change before it becomes official, and the owner alone publishes to the team Google Drive.

If you are using Claude Code, also read the "Contributors Using Claude Code" section in [CLAUDE.md](CLAUDE.md).

## The flow

```
branch  ->  build with Claude Code  ->  push  ->  open PR  ->  owner approves + merges
```

1. Start a branch before each session:
   ```bash
   git checkout main
   git pull
   git checkout -b contrib/<short-name>
   ```
2. Build the doc with Claude Code. Use the existing skills for structure: `waiz-business-os` and `sop-builder` (see [.claude/skills/README.md](.claude/skills/README.md)).
3. New docs use YAML frontmatter with `status: draft`. The owner flips to `active` after review.
4. Commit and push your branch:
   ```bash
   git add .
   git commit -m "Add <process> SOP draft"
   git push -u origin contrib/<short-name>
   ```
5. Open a pull request into `main`. The owner reviews the diff, then approves and merges. Do not merge your own PR.

## The approval checkpoint

The pull request is the checkpoint. `main` only changes when the owner approves and merges, so nothing you do affects the live OS until then. Branch protection requires one approval, and GitHub does not let you approve your own PR — so the owner's review is always required.

## Do not

- Do not commit directly to `main`. Always use a branch + PR.
- Do not merge your own pull request.
- Do not edit:
  - [docs/SPINE.md](docs/SPINE.md) (approved operating spine)
  - [docs/_inventory/team-publish-registry.yaml](docs/_inventory/team-publish-registry.yaml) (team publish registry)
  - anything under `scripts/` or `config/` (publish tooling and credentials)
  - anything in the `waiz-os-archive` sibling repo (frozen raw export)
- Do not run team publish tooling (`scripts/team-doc-approve.py`, `scripts/publish-team-doc.py`) or any Google Drive publish step. Only the owner publishes to the team.
- Do not invent pricing. Pricing is owner-only.

## Conventions

- Filenames: lowercase kebab-case, stable once linked (see [docs/SOURCE-OF-TRUTH.md](docs/SOURCE-OF-TRUTH.md)).
- One source of truth per process. Link related docs instead of duplicating sections.
- Durable operating docs include: purpose, scope, owner, trigger, inputs, outputs, process, quality bar, metrics, and related docs.

## After merge (owner only)

1. Review the PR diff; request changes or approve and merge.
2. Set the doc `status: active` when ready.
3. If it should reach the team, publish per [.claude/skills/team-doc-publish/SKILL.md](.claude/skills/team-doc-publish/SKILL.md).
