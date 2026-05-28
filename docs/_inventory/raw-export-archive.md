---
title: Raw Export Archive
domain: inventory
owner: operations
status: active
last_updated: 2026-05-28
review_cycle: as-needed
---

# Raw Export Archive

The frozen Google Drive export no longer lives in `Wm-os`. It moved to a sibling repository so the OS repo stays small for daily work (including team Google Doc publish).

## Clone layout

```text
~/Documents/GitHub/
├── Wm-os/                 ← canonical docs, scripts, skills
└── wm-os-archive/         ← raw export only (196MB+)
    └── waiz-drive-export/
        └── Waiz Media OS/
```

## Local path (when both repos are cloned)

| Historical path in frontmatter | Current path on disk |
|-------------------------------|----------------------|
| `source-docs/waiz-drive-export/...` | `../wm-os-archive/waiz-drive-export/...` (relative to `Wm-os` root) |

## Setup

```bash
cd ~/Documents/GitHub
git clone git@github.com:gwadawg/wm-os-archive.git wm-os-archive
```

Create the GitHub repo `wm-os-archive` (private recommended), then push from the local folder at `~/Documents/GitHub/wm-os-archive` (already initialized with the export).

If the archive repo is not cloned, migration and `.docx` conversion workflows cannot read raw sources. Team publish from approved `docs/` is unaffected.

## Related

- [Google Drive Inventory](google-drive-inventory.md)
- [Source Of Truth Rules](../SOURCE-OF-TRUTH.md)
- Archive repo README: `../wm-os-archive/README.md` (sibling clone)
