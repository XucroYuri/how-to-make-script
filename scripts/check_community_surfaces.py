from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List

if __package__ in (None, ""):
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.lib import repo_root


REQUIRED_DOCS = (
    "docs/community-feedback-loop.md",
    "docs/community-feedback-loop-zh.md",
    "docs/community-triage-loop.md",
    "docs/community-operations.md",
    "docs/community-operations-zh.md",
)

REQUIRED_LABELS = {
    "needs-triage",
    "type:challenge",
    "type:route",
    "type:field-report",
    "type:learning",
    "type:community",
    "status:routed",
    "status:encoded",
    "discussion-first",
    "needs-practitioner-input",
}


def check_community_surfaces(root: Path) -> Dict[str, Any]:
    root = root.resolve()
    errors: List[str] = []

    discussion_map_path = root / "references" / "discussion-surface-map.json"
    label_taxonomy_path = root / "references" / "community-label-taxonomy.json"
    config_path = root / ".github" / "ISSUE_TEMPLATE" / "config.yml"

    if not discussion_map_path.exists():
        errors.append("references/discussion-surface-map.json: missing")
        discussion_map: Dict[str, Any] = {"categories": []}
    else:
        discussion_map = json.loads(discussion_map_path.read_text(encoding="utf-8"))

    if not label_taxonomy_path.exists():
        errors.append("references/community-label-taxonomy.json: missing")
        label_taxonomy: Dict[str, Any] = {"labels": []}
    else:
        label_taxonomy = json.loads(label_taxonomy_path.read_text(encoding="utf-8"))

    config_text = config_path.read_text(encoding="utf-8") if config_path.exists() else ""
    if not config_text:
        errors.append(".github/ISSUE_TEMPLATE/config.yml: missing or empty")

    for doc in REQUIRED_DOCS:
        if not (root / doc).exists():
            errors.append(f"{doc}: missing")

    category_slugs: List[str] = []
    expected_discussion_template_count = 0
    for category in discussion_map.get("categories", []):
        slug = category.get("slug")
        if not isinstance(slug, str) or not slug:
            errors.append("references/discussion-surface-map.json: category missing slug")
            continue
        if slug in category_slugs:
            errors.append(f"references/discussion-surface-map.json: duplicate slug {slug!r}")
        category_slugs.append(slug)

        if category.get("form_expected"):
            expected_discussion_template_count += 1
            template_path = root / ".github" / "DISCUSSION_TEMPLATE" / f"{slug}.yml"
            if not template_path.exists():
                errors.append(f".github/DISCUSSION_TEMPLATE/{slug}.yml: missing")

        if category.get("contact_link_expected"):
            expected_url = f"/discussions/categories/{slug}"
            if expected_url not in config_text:
                errors.append(
                    ".github/ISSUE_TEMPLATE/config.yml: "
                    f"missing contact link for discussion category {slug!r}"
                )

    labels = label_taxonomy.get("labels", [])
    label_names: List[str] = []
    for label in labels:
        name = label.get("name")
        if not isinstance(name, str) or not name:
            errors.append("references/community-label-taxonomy.json: label missing name")
            continue
        if name in label_names:
            errors.append(f"references/community-label-taxonomy.json: duplicate label {name!r}")
        label_names.append(name)
        for key in ("color", "description", "group"):
            if not isinstance(label.get(key), str) or not label[key]:
                errors.append(
                    "references/community-label-taxonomy.json: "
                    f"label {name!r} missing {key!r}"
                )

    missing_required_labels = sorted(REQUIRED_LABELS - set(label_names))
    for name in missing_required_labels:
        errors.append(
            f"references/community-label-taxonomy.json: missing required label {name!r}"
        )

    return {
        "errors": errors,
        "category_count": len(category_slugs),
        "discussion_template_count": expected_discussion_template_count,
        "label_count": len(label_names),
        "doc_count": sum(1 for doc in REQUIRED_DOCS if (root / doc).exists()),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=str(repo_root()))
    args = parser.parse_args()
    report = check_community_surfaces(Path(args.root))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not report["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
