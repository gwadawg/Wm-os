---
title: Repo Hygiene Checklist
domain: inventory
owner: operations
status: active
last_updated: 2026-05-29
review_cycle: weekly
---

# Repo Hygiene Checklist

Owner-run checklist for **Git branches**, **folder hygiene**, **draft vs active**, and **team publish** alignment. Regenerate counts with the commands in [Maintenance commands](#maintenance-commands).

Related: [migration-backlog.md](migration-backlog.md), [team-publish-registry.yaml](team-publish-registry.yaml), [CONTRIBUTING.md](../../CONTRIBUTING.md), [team-drafts README](../team-drafts/README.md).

---

## 1. Git branches

### Policy (keep)

| Rule | Action |
|------|--------|
| `main` = approved OS | Protect on GitHub; require PR + owner approval |
| Contributors | `contrib/<topic>` only → PR → merge → delete branch |
| Owner | Short-lived `feat/*` or `fix/*` OK; merge within days |
| Do **not** use | `develop`, per-domain branches, per-client branches |

### Stale branch audit (2026-05-29)

| Branch | Verdict | Action |
|--------|---------|--------|
| `feat/sop-builder-skill` | **Superseded** — 0 commits ahead of `main`; `main` is 9+ commits ahead. `sop-builder` skill already on `main`. | Delete local + remote (commands below) |
| `origin/cursor/pre-intro-followup-messaging-1e4f` | Likely abandoned Cursor agent branch | Review diff on GitHub; delete if merged or obsolete |

```bash
# After confirming nothing unique on the branch:
git checkout main
git branch -d feat/sop-builder-skill
git push origin --delete feat/sop-builder-skill   # owner only

# Optional: list stale remote branches
git fetch --prune
git branch -r --merged origin/main
```

### GitHub settings (recommended)

- [ ] Branch protection on `main` (require PR, 1 approval, no self-approve)
- [ ] Auto-delete head branches after merge
- [ ] Restrict who can push to `main` (owner + admins only)

---

## 2. Folder hygiene

| Item | Status | Action |
|------|--------|--------|
| `source-docs/` | Empty except `.DS_Store` | Keep [source-docs/README.md](../../source-docs/README.md) pointer to `waiz-os-archive`; do not re-import raw export here |
| `docs/automations/` | Placeholder README | Specs live under `client-fulfillment/crm-architecture/` until automations domain is populated — see [automations/README](../automations/README.md) |
| `docs/prompts/` | Thin (3 files) | Add prompts when a workflow gets a repeatable AI step; mirror domain subfolders |
| `docs/kpis/` | Growing (draft diagnostic stack) | Founder sign-off on [client-kpi-judgment-standard.md](../kpis/client-kpi-judgment-standard.md) before marking `active` |
| `.tools/pandoc/` | Vendored binary | OK for publish pipeline; do not duplicate pandoc elsewhere |
| Drive tree in repo | — | **Never** mirror old `Waiz Media OS` Drive folders under `docs/` |

---

## 3. Draft vs active vs Drive (priority)

These canonical files are **`publish_status: active`** in [team-publish-registry.yaml](team-publish-registry.yaml) but still **`status: draft`** in frontmatter. Team may be executing Drive copies while Git labels them draft — fix by founder review, then flip to `active` and update [SPINE.md](../SPINE.md) if listed.

| Canonical path | Owner action |
|----------------|--------------|
| [setter-daily-checklist.md](../acquisition/sales/setter-daily-checklist.md) | Review → `active` |
| [sop-watchshift.md](../acquisition/sales/sop-watchshift.md) | Review → `active` |
| [sop-power-dialer-new-leads.md](../acquisition/sales/sop-power-dialer-new-leads.md) | Review → `active` |
| [setter-lead-messaging.md](../acquisition/sales/setter-lead-messaging.md) | Review → `active` |
| [eod-report-sop-setters-closers.md](../acquisition/sales/eod-report-sop-setters-closers.md) | Review → `active` (checklist notes Pedro sign-off) |
| [outbound/linkedin/process.md](../acquisition/outbound/linkedin/process.md) | Review → `active`; close migration backlog publish item |
| [outbound/linkedin/copy-angles.md](../acquisition/outbound/linkedin/copy-angles.md) | Review → `active`; close migration backlog publish item |

### Pending first publish (registry)

| Canonical path | Registry | Owner action |
|----------------|----------|--------------|
| [script-demo-appointment-confirmation.md](../acquisition/sales/script-demo-appointment-confirmation.md) | `publish_status: pending` | Review → `active` → prepare/approve team draft → publish to `02 - Setters` |

### SPINE-listed but still draft

| Doc | Note |
|-----|------|
| [script-demo-appointment-confirmation.md](../acquisition/sales/script-demo-appointment-confirmation.md) | Listed in SPINE setter row as `draft` |
| LinkedIn [manifest.yaml](../acquisition/outbound/linkedin/manifest.yaml) | SPINE notes draft |

---

## 4. Team drafts pipeline

### Workflow (every new setter/closer doc)

1. `python scripts/team-doc-prepare.py docs/.../canonical.md`
2. Edit `docs/team-drafts/<slug>.team.md`
3. `python scripts/team-doc-approve.py docs/team-drafts/<slug>.team.md --check-only`
4. `python scripts/team-doc-approve.py docs/team-drafts/<slug>.team.md`
5. Canonical `status: active` → `python scripts/publish-team-doc.py docs/.../canonical.md`
6. Confirm [team-publish-registry.yaml](team-publish-registry.yaml) row (`team_draft_path`, `google_doc_id`, `last_published`)

### Team draft files vs registry (2026-05-29)

| Team draft | In registry `team_draft_path`? | Notes |
|------------|-------------------------------|--------|
| All setter stack drafts (`00`–`05`, EOD, etc.) | Yes | Published; align canonical `status` (section 3) |
| [fulfillment-constraint-diagnosis-kpi-standards.team.md](../team-drafts/fulfillment-constraint-diagnosis-kpi-standards.team.md) | **No** — published via `template_based` only | Optional: add `team_draft_path` to registry row for traceability |
| Demo confirmation | **No team draft yet** | Create after canonical `active` |

### Untracked / in-progress drafts (working tree)

If these exist locally but are not committed, commit on `contrib/*` or owner branch after approve:

- `eod-report-sop-setters-closers.team.md` + `.meta.yaml`
- `script-intro-call-basic.team.md` + `.meta.yaml`
- `setter-daily-checklist.team.md` + `.meta.yaml`
- `setter-lead-messaging.team.md` + `.meta.yaml`
- `sop-power-dialer-new-leads.team.md` + `.meta.yaml`
- `sop-watchshift.team.md` + `.meta.yaml`

---

## 5. Migration backlog (open items)

From [migration-backlog.md](migration-backlog.md) — not branch/folder work, but blocks “production grade” OS:

- [ ] Publish LinkedIn process + copy-angles — **blocked on** canonical `active` (section 3)
- [ ] Publish Demo Appointment Confirmation — **blocked on** canonical `active` + team draft
- [ ] Add owners to every active SOP
- [ ] Add triggers, inputs, outputs, definition of done to every SOP
- [ ] Add KPIs to sales, MB, onboarding, CS workflows
- [ ] Map SOPs → automations or prompt workflows

---

## 6. Weekly owner routine (15 min)

1. `git fetch --prune` — delete merged remote branches
2. Scan [team-publish-registry.yaml](team-publish-registry.yaml) for `publish_status: pending`
3. Run draft/active mismatch script (below) — flip reviewed docs to `active`
4. Glance [migration-backlog.md](migration-backlog.md) open checkboxes
5. One fulfillment + one acquisition doc promoted per week (draft → active)

---

## Maintenance commands

```bash
# Draft vs active counts
find docs -name '*.md' -print0 | xargs -0 grep -l '^status: draft' | wc -l
find docs -name '*.md' -print0 | xargs -0 grep -l '^status: active' | wc -l

# Published on Drive but canonical still draft (requires repo root)
python3 << 'PY'
import re
from pathlib import Path
text = Path("docs/_inventory/team-publish-registry.yaml").read_text()
entries, cur = [], {}
for line in text.splitlines():
    if line.startswith("- repo_path:"):
        if cur: entries.append(cur)
        cur = {"repo_path": line.split(":",1)[1].strip()}
    elif cur and "publish_status:" in line:
        cur["publish_status"] = line.split(":",1)[1].strip()
if cur: entries.append(cur)
for e in entries:
    if e.get("publish_status") != "active": continue
    p = Path(e["repo_path"])
    if not p.exists(): continue
    st = re.search(r"^status:\s*(\S+)", p.read_text()[:800], re.M)
    if st and st.group(1) == "draft":
        print(e["repo_path"])
PY

# Team drafts missing registry team_draft_path
python3 << 'PY'
import re
from pathlib import Path
reg = Path("docs/_inventory/team-publish-registry.yaml").read_text()
drafts = {p.stem.replace(".team","") for p in Path("docs/team-drafts").glob("*.team.md")}
in_reg = set(re.findall(r"team_draft_path: docs/team-drafts/([^.]+)\.team\.md", reg))
print("Drafts not in registry:", sorted(drafts - in_reg))
PY
```

---

## 7. Optional hardening (later)

- [ ] GitHub Action: require frontmatter `title`, `owner`, `status` on new `docs/**/*.md`
- [ ] Link checker on `docs/` internal links (weekly cron)
- [ ] Do **not** add per-client folders under `docs/` unless template-only
