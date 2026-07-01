"""Build and render the client playbooks index from repo docs."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

import yaml

from .doc_frontmatter import read_doc_meta
from .paths import repo_root

CATALOG_DIR = "docs/client-fulfillment/client-playbooks"
CATALOG_YAML = f"{CATALOG_DIR}/catalog.yaml"
CATALOG_MD = f"{CATALOG_DIR}/catalog.md"

CLIENT_ARTIFACT_TYPES = frozenset(
    {"playbook", "sop", "script", "guide", "training", "doctrine", "overview"}
)

FILENAME_HINTS = ("playbook", "-sop", "script-", "guide-", "training-")

EXCLUDE_DIR_PARTS = frozenset(
    {
        "outputs",
        "swipes",
        "chatbot-deploy",
        "creative-research",
        "team-drafts",
        "_inventory",
        "client-playbooks",
    }
)

EXCLUDE_FILENAMES = frozenset({"README.md", "_gaps.md", "FUTURE-video-agent-spec.md", "catalog.md"})

LEGACY_DELIVERY_ALIASES = {
    "skool": "course-material",
    "bootcamp": "course-material",
    "boot-camp": "course-material",
}

SHAREABILITY_TIERS = frozenset({"lo-course", "paying-client", "internal-fulfillment"})


@dataclass
class CatalogEntry:
    repo_path: str
    title: str
    artifact_type: str
    content_layer: str
    audience: list[str]
    delivery: list[str]
    status: str
    owner: str
    domain: str
    delivery_group: str
    product: str
    canonical_parent: str | None
    methodology_sources: list[str]
    portal_url: str | None
    shareability: str
    last_updated: str
    source: str

    def to_dict(self) -> dict[str, Any]:
        d: dict[str, Any] = {
            "repo_path": self.repo_path,
            "title": self.title,
            "artifact_type": self.artifact_type,
            "content_layer": self.content_layer,
            "audience": self.audience,
            "delivery": self.delivery,
            "shareability": self.shareability,
            "status": self.status,
            "owner": self.owner,
            "domain": self.domain,
            "delivery_group": self.delivery_group,
            "product": self.product,
            "methodology_sources": self.methodology_sources,
            "last_updated": self.last_updated,
            "source": self.source,
        }
        if self.canonical_parent:
            d["canonical_parent"] = self.canonical_parent
        if self.portal_url:
            d["portal_url"] = self.portal_url
        return d


def _normalize_delivery(channels: list[str]) -> list[str]:
    out: list[str] = []
    for ch in channels:
        key = str(ch).strip().lower()
        out.append(LEGACY_DELIVERY_ALIASES.get(key, key))
    return out


def catalog_yaml_path(root: Path | None = None) -> Path:
    return (root or repo_root()) / CATALOG_YAML


def catalog_md_path(root: Path | None = None) -> Path:
    return (root or repo_root()) / CATALOG_MD


def load_catalog_config(root: Path | None = None) -> dict[str, Any]:
    path = catalog_yaml_path(root)
    if not path.is_file():
        return _default_config()
    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    for key, default in _default_config().items():
        data.setdefault(key, default)
    return data


def _default_config() -> dict[str, Any]:
    return {
        "workflow": "client-playbooks",
        "version": 1,
        "status": "active",
        "last_synced": None,
        "delivery_groups": [],
        "shareability_tiers": [],
        "protected_path_prefixes": [],
        "methodology_pools": {},
        "exclude_paths": [],
        "overrides": {},
        "entries": [],
    }


def save_catalog_config(data: dict[str, Any], root: Path | None = None) -> None:
    path = catalog_yaml_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)


def rel_repo_path(path: Path, root: Path) -> str:
    return str(path.relative_to(root)).replace("\\", "/")


def _infer_content_layer(repo_path: str) -> str:
    if "/course-material/" in repo_path:
        return "course-material"
    if "/clients/" in repo_path:
        return "client-instance"
    return "canonical"


def _infer_audience(meta: dict[str, Any], repo_path: str) -> list[str]:
    raw = meta.get("audience")
    if isinstance(raw, list):
        return [str(x) for x in raw]
    if isinstance(raw, str):
        return [raw]
    if meta.get("client_delivery") is True:
        return ["client"]
    if repo_path.startswith("docs/client-fulfillment/"):
        if "/course-material/" in repo_path or "/client-marketing/" in repo_path:
            return ["client"]
        if "/media-buying/" in repo_path or "/client-success/" in repo_path:
            return ["client", "team"]
        if "/onboarding/" in repo_path:
            return ["client", "team"]
    return ["team"]


def _infer_delivery(meta: dict[str, Any], content_layer: str) -> list[str]:
    raw = meta.get("delivery")
    if isinstance(raw, list):
        return _normalize_delivery([str(x) for x in raw])
    if isinstance(raw, str):
        return _normalize_delivery([raw])
    if content_layer == "course-material":
        return ["course-material", "github"]
    if content_layer == "client-instance":
        return ["google-doc", "github"]
    return ["github", "team-drive"]


def _infer_artifact_type(meta: dict[str, Any], filename: str) -> str:
    if meta.get("artifact_type"):
        return str(meta["artifact_type"])
    lower = filename.lower()
    if "playbook" in lower:
        return "playbook"
    if "-sop" in lower or lower.startswith("sop-"):
        return "sop"
    if lower.startswith("script-"):
        return "script"
    if "guide" in lower:
        return "guide"
    if "training" in lower:
        return "training"
    if lower.startswith("doctrine-"):
        return "doctrine"
    return "guide"


def _infer_delivery_group(repo_path: str, meta: dict[str, Any], config: dict[str, Any]) -> str:
    if meta.get("delivery_group"):
        return str(meta["delivery_group"])
    path = repo_path.lower()
    if "nurture" in path or "drip" in path or "imessage" in path:
        return "lead-nurture"
    if "onboarding" in path:
        return "onboarding"
    if "creative" in path or "ad-" in path or "ads" in path or "media-buying" in path:
        return "meta-ads-creative"
    if "crm" in path or "bot" in path or "infrastructure" in path:
        return "crm-automation"
    if "client-success" in path or "constraint" in path or "reset" in path:
        return "client-success"
    if "course-material" in path:
        return "course-material"
    if "reverse-mortgage-dna" in path or "dscr-dna" in path:
        return "product-knowledge"
    if "call-center" in path:
        return "call-center"
    return "general"


def _infer_product(repo_path: str, meta: dict[str, Any]) -> str:
    if meta.get("product"):
        return str(meta["product"])
    if "dscr" in repo_path.lower():
        return "dscr"
    if "reverse-mortgage" in repo_path or "/rm-" in repo_path or "rm_" in repo_path:
        return "reverse-mortgage"
    return "reverse-mortgage"


def _portal_url(meta: dict[str, Any]) -> str | None:
    for key in ("portal_url", "skool_url", "client_portal_url"):
        if meta.get(key):
            return str(meta[key])
    return None


def _infer_shareability(meta: dict[str, Any], repo_path: str, artifact_type: str) -> str:
    raw = meta.get("shareability")
    if raw in SHAREABILITY_TIERS:
        return str(raw)

    path = repo_path.lower()

    if path.endswith("-framework.md") and "/playbook-" in path:
        return "lo-course"

    if "/course-material/" in path:
        return "lo-course"

    if "/crm-architecture/" in path:
        return "internal-fulfillment"
    if "/onboarding/a-z" in path or "/onboarding/" in path and "a-z" in path:
        return "internal-fulfillment"
    if "/media-buying/" in path:
        return "internal-fulfillment"
    if "/client-success/" in path:
        return "internal-fulfillment"
    if "10-day" in path or "drip-campaign" in path or "imessage-intent-drip" in path:
        return "internal-fulfillment"
    if "how-wm-ai-bot" in path:
        return "internal-fulfillment"

    if artifact_type == "playbook" and "/playbook-" in path and not path.endswith("-framework.md"):
        if "/client-marketing/" in path:
            return "paying-client"

    if "/client-marketing/" in path:
        if "sop-lo-" in path or "playbook-bamfam" in path or "playbook-rm-conceptual" in path:
            return "lo-course"
        return "paying-client"

    if "/reverse-mortgage-dna/" in path or "/dscr-dna/" in path:
        return "lo-course"

    return "internal-fulfillment"


def _should_include(path: Path, meta: dict[str, Any], root: Path, config: dict[str, Any]) -> bool:
    repo_path = rel_repo_path(path, root)
    if path.name in EXCLUDE_FILENAMES:
        return False
    if repo_path in set(config.get("exclude_paths") or []):
        return False
    for part in path.parts:
        if part in EXCLUDE_DIR_PARTS:
            return False
    if meta.get("client_delivery") is False:
        return False
    if meta.get("client_delivery") is True:
        return True
    if not repo_path.startswith("docs/client-fulfillment/"):
        return False
    artifact = _infer_artifact_type(meta, path.name)
    if artifact in CLIENT_ARTIFACT_TYPES:
        return True
    lower = path.name.lower()
    return any(h in lower for h in FILENAME_HINTS)


def _merge_override(entry: CatalogEntry, override: dict[str, Any]) -> CatalogEntry:
    for key, val in override.items():
        if key in ("repo_path", "notes"):
            continue
        if key == "delivery" and val is not None:
            entry.delivery = _normalize_delivery(list(val))
            continue
        if hasattr(entry, key) and val is not None:
            setattr(entry, key, val)
    entry.source = "override"
    return entry


def scan_entry(path: Path, root: Path, config: dict[str, Any]) -> CatalogEntry | None:
    meta = read_doc_meta(path)
    if not _should_include(path, meta, root, config):
        return None
    repo_path = rel_repo_path(path, root)
    layer_raw = meta.get("content_layer") or _infer_content_layer(repo_path)
    if layer_raw == "training-wrapper":
        layer_raw = "course-material"
    content_layer = str(layer_raw)
    methodology = meta.get("methodology_sources") or []
    if isinstance(methodology, str):
        methodology = [methodology]
    canonical = meta.get("canonical_parent")
    if canonical:
        canonical = str(canonical).replace("\\", "/")

    artifact_type = _infer_artifact_type(meta, path.name)
    entry = CatalogEntry(
        repo_path=repo_path,
        title=str(meta.get("title") or meta["_title"]),
        artifact_type=artifact_type,
        content_layer=content_layer,
        audience=_infer_audience(meta, repo_path),
        delivery=_infer_delivery(meta, content_layer),
        status=str(meta.get("status") or "draft"),
        owner=str(meta.get("owner") or "unassigned"),
        domain=str(meta.get("domain") or "client-fulfillment"),
        delivery_group=_infer_delivery_group(repo_path, meta, config),
        product=_infer_product(repo_path, meta),
        canonical_parent=canonical,
        methodology_sources=[str(m).replace("\\", "/") for m in methodology],
        portal_url=_portal_url(meta),
        shareability=_infer_shareability(meta, repo_path, artifact_type),
        last_updated=str(meta.get("last_updated") or ""),
        source="scan",
    )
    override = (config.get("overrides") or {}).get(repo_path)
    if override:
        entry = _merge_override(entry, override)
    return entry


def scan_all(root: Path | None = None) -> list[CatalogEntry]:
    root = root or repo_root()
    config = load_catalog_config(root)
    entries: list[CatalogEntry] = []
    fulfillment = root / "docs/client-fulfillment"
    if fulfillment.is_dir():
        for path in sorted(fulfillment.rglob("*.md")):
            entry = scan_entry(path, root, config)
            if entry:
                entries.append(entry)
    docs = root / "docs"
    for path in sorted(docs.rglob("*.md")):
        if str(path).startswith(str(fulfillment)):
            continue
        meta = read_doc_meta(path)
        if meta.get("client_delivery") is True:
            entry = scan_entry(path, root, config)
            if entry:
                entries.append(entry)
    entries.sort(key=lambda e: (e.delivery_group, e.content_layer, e.title.lower()))
    return entries


def sync_catalog(root: Path | None = None, *, write_yaml: bool = True, write_md: bool = True) -> dict[str, Any]:
    root = root or repo_root()
    config = load_catalog_config(root)
    entries = scan_all(root)
    config["entries"] = [e.to_dict() for e in entries]
    config["last_synced"] = date.today().isoformat()
    config["entry_count"] = len(entries)
    if write_yaml:
        save_catalog_config(config, root)
    if write_md:
        catalog_md_path(root).write_text(render_markdown(config, entries), encoding="utf-8")
    return config


def _group_label(config: dict[str, Any], group_id: str) -> str:
    for g in config.get("delivery_groups") or []:
        if g.get("id") == group_id:
            return str(g.get("label") or group_id)
    return group_id.replace("-", " ").title()


def _entry_link(repo_path: str) -> str:
    return "../" + repo_path.replace("docs/client-fulfillment/", "")


def _methodology_link(path: str) -> str:
    if path.startswith("docs/client-fulfillment/"):
        return "../" + path.replace("docs/client-fulfillment/", "")
    if path.startswith("docs/"):
        return "../../" + path.removeprefix("docs/")
    if path.startswith(".claude/"):
        return "../../" + path
    return path


def render_markdown(config: dict[str, Any], entries: list[CatalogEntry]) -> str:
    today = date.today().isoformat()
    lines = [
        "---",
        "title: Client Playbooks — Catalog",
        "domain: client-fulfillment",
        "owner: community-education",
        "status: active",
        f"last_updated: {today}",
        "review_cycle: weekly",
        "generated: true",
        "---",
        "",
        "# Client Playbooks — Catalog",
        "",
        "> **Auto-generated** from repo frontmatter. Do not edit by hand.",
        "> Regenerate: `python scripts/sync-client-playbooks.py`",
        "> Start here: [README.md](README.md) · Config: [catalog.yaml](catalog.yaml)",
        "",
        f"Last synced: **{config.get('last_synced', today)}** · **{len(entries)}** playbooks, SOPs, and training docs indexed",
        "",
        "See [Client Playbooks README](README.md) for how to create new assets.",
        "",
        "## Methodology pools",
        "",
    ]
    pools = config.get("methodology_pools") or {}
    if not pools:
        lines.append("_Configure pools in `catalog.yaml` → `methodology_pools`._")
    else:
        for pool_id, pool in pools.items():
            label = pool.get("label") or pool_id
            lines.append(f"### {label}")
            lines.append("")
            for src in pool.get("sources") or []:
                p = src.get("path", "")
                role = src.get("role", "")
                lines.append(f"- [{p}]({_methodology_link(p)}) — {role}")
            lines.append("")

    lines.append("## By topic")
    lines.append("")

    by_group: dict[str, list[CatalogEntry]] = {}
    for e in entries:
        by_group.setdefault(e.delivery_group, []).append(e)

    for group_id in sorted(by_group.keys()):
        label = _group_label(config, group_id)
        lines.append(f"### {label} (`{group_id}`)")
        lines.append("")
        lines.append("| Title | Type | Layer | Shareability | Status | Audience | Delivery |")
        lines.append("|-------|------|-------|--------------|--------|----------|----------|")
        for e in by_group[group_id]:
            link = _entry_link(e.repo_path)
            aud = ", ".join(e.audience)
            deliv = ", ".join(e.delivery)
            lines.append(
                f"| [{e.title}]({link}) | {e.artifact_type} | {e.content_layer} | "
                f"{e.shareability} | {e.status} | {aud} | {deliv} |"
            )
        lines.append("")

    lo_course = [e for e in entries if e.shareability == "lo-course"]
    if lo_course:
        lines.extend(["## LO course — `lo-course` only", ""])
        lines.append(
            "Safe for prospect LO course modules. See "
            "[shareability boundaries](../shareability-boundaries.md) and "
            "[checklist](SHAREABILITY-CHECKLIST.md)."
        )
        lines.append("")
        for e in lo_course:
            link = _entry_link(e.repo_path)
            lines.append(f"- [{e.title}]({link}) — `{e.delivery_group}`")
        lines.append("")

    wrappers = [e for e in entries if e.content_layer == "course-material"]
    if wrappers:
        lines.extend(["## Course material → canonical source", ""])
        for e in wrappers:
            parent = e.canonical_parent or "_not linked_"
            lines.append(f"- **{e.title}** → {parent}")
        lines.append("")

    lines.extend(
        [
            "## Related",
            "",
            "- [Client Playbooks README](README.md)",
            "- [Shareability boundaries](../shareability-boundaries.md)",
            "- [Shareability checklist](SHAREABILITY-CHECKLIST.md)",
            "- [Course material](../course-material/README.md)",
            "- [Fulfillment Operating System](../fulfillment-operating-system.md)",
            "- [Client playbook template](../../templates/client-playbook-template.md)",
            "- [Client playbooks skill](../../.claude/skills/client-playbooks/SKILL.md)",
            "",
        ]
    )
    return "\n".join(lines)
