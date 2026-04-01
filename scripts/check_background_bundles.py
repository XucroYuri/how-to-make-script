from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Set
import sys

if __package__ in (None, ""):
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.lib import (
    collect_asset_index,
    load_json,
    load_schemas,
    relative_path,
    repo_root,
    validate_schema,
)


LOADING_MODES = {"route_kernel", "focus_pack", "compare_pack", "teaching_pack", "survey_pack"}


def parse_supported_outputs(path: Path) -> Set[str]:
    outputs: Set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("- `") and "`:" in line:
            outputs.add(line.split("`", 2)[1])
    return outputs


def parse_constraint_families(path: Path) -> Set[str]:
    text = path.read_text(encoding="utf-8")
    start = text.index("## Constraint Families")
    families: Set[str] = set()
    for line in text[start:].splitlines():
        line = line.strip()
        if line.startswith("- `") and line.endswith("`"):
            families.add(line.split("`", 2)[1])
    return families


def check_background_bundles(root: Path) -> Dict[str, Any]:
    root = root.resolve()
    errors: List[str] = []

    schemas = load_schemas(root)
    registry_path = root / "references" / "background-bundles.json"
    registry = load_json(registry_path)
    errors.extend(
        f"{relative_path(root, registry_path)}: {message}"
        for message in validate_schema(registry, schemas["background-bundle.schema.json"])
    )

    _, assets, _, _ = collect_asset_index(root)
    atom_ids = {asset["id"] for asset in assets if asset["type"] == "knowledge_atom"}
    output_ids = parse_supported_outputs(root / "references" / "supported-outputs.md")
    constraint_families = parse_constraint_families(root / "references" / "taxonomy.md")

    seen_bundle_ids: Set[str] = set()

    for bundle in registry.get("bundles", []):
        bundle_id = bundle["id"]
        if bundle_id in seen_bundle_ids:
            errors.append(f"{relative_path(root, registry_path)}: duplicate bundle id {bundle_id!r}")
        seen_bundle_ids.add(bundle_id)

        for doc_path in bundle["docs"]:
            path = root / doc_path
            if not path.exists():
                errors.append(
                    f"{relative_path(root, registry_path)}: bundle {bundle_id!r} references missing doc {doc_path!r}"
                )

        for atom_id in bundle["linked_atoms"]:
            if atom_id not in atom_ids:
                errors.append(
                    f"{relative_path(root, registry_path)}: bundle {bundle_id!r} references unknown atom {atom_id!r}"
                )

        for output_id in bundle["primary_outputs"]:
            if output_id not in output_ids:
                errors.append(
                    f"{relative_path(root, registry_path)}: bundle {bundle_id!r} references unknown output {output_id!r}"
                )

        for loading_mode in bundle["preferred_loading_modes"]:
            if loading_mode not in LOADING_MODES:
                errors.append(
                    f"{relative_path(root, registry_path)}: bundle {bundle_id!r} uses unknown loading mode {loading_mode!r}"
                )

        for family in bundle["constraint_families"]:
            if family not in constraint_families:
                errors.append(
                    f"{relative_path(root, registry_path)}: bundle {bundle_id!r} uses unknown constraint family {family!r}"
                )

    return {
        "errors": sorted(errors),
        "bundle_count": len(registry.get("bundles", [])),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=str(repo_root()))
    args = parser.parse_args()
    report = check_background_bundles(Path(args.root))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not report["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
