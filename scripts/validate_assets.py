from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List
import sys

if __package__ in (None, ""):
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.lib import (
    ASSET_SCHEMA_BY_TYPE,
    collect_asset_index,
    load_router_matrix,
    load_schemas,
    relative_path,
    repo_root,
    validate_schema,
)


def validate_repository(root: Path) -> Dict[str, Any]:
    root = root.resolve()
    schemas = load_schemas(root)
    asset_by_id, assets, manifests, fixtures = collect_asset_index(root)

    errors: List[str] = []
    counts = {
        "knowledge_atom": 0,
        "workflow_protocol": 0,
        "evaluation_rubric": 0,
        "skill_manifest": len(manifests),
        "example_fixture": len(fixtures),
    }

    ids_seen = set()

    for asset in assets:
        asset_id = asset["id"]
        if asset_id in ids_seen:
            errors.append(f"Duplicate asset id: {asset_id}")
        ids_seen.add(asset_id)
        counts[asset["type"]] += 1
        schema_name = ASSET_SCHEMA_BY_TYPE[asset["type"]]
        errors.extend(
            f"{relative_path(root, asset['_path'])}: {message}"
            for message in validate_schema(asset, schemas[schema_name])
        )

    for manifest in manifests:
        manifest_id = manifest["id"]
        if manifest_id in ids_seen:
            errors.append(f"Duplicate manifest id: {manifest_id}")
        ids_seen.add(manifest_id)
        errors.extend(
            f"{relative_path(root, manifest['_path'])}: {message}"
            for message in validate_schema(manifest, schemas["skill-manifest.schema.json"])
        )

    for fixture in fixtures:
        fixture_id = fixture["id"]
        if fixture_id in ids_seen:
            errors.append(f"Duplicate fixture id: {fixture_id}")
        ids_seen.add(fixture_id)
        errors.extend(
            f"{relative_path(root, fixture['_path'])}: {message}"
            for message in validate_schema(fixture, schemas["example-fixture.schema.json"])
        )

    rubric_ids = {asset["id"] for asset in assets if asset["type"] == "evaluation_rubric"}
    atom_ids = {asset["id"] for asset in assets if asset["type"] == "knowledge_atom"}
    protocol_ids = {asset["id"] for asset in assets if asset["type"] == "workflow_protocol"}
    skill_ids = {manifest["id"] for manifest in manifests}

    for asset in assets:
        if asset["type"] == "knowledge_atom":
            for linked_id in asset.get("links", []):
                if linked_id not in asset_by_id:
                    errors.append(f"{relative_path(root, asset['_path'])}: unknown link id '{linked_id}'")
        elif asset["type"] == "workflow_protocol":
            for rubric_id in asset["rubrics"]:
                if rubric_id not in rubric_ids:
                    errors.append(f"{relative_path(root, asset['_path'])}: unknown rubric id '{rubric_id}'")
            for linked_id in asset["linked_atoms"]:
                if linked_id not in atom_ids:
                    errors.append(f"{relative_path(root, asset['_path'])}: unknown atom id '{linked_id}'")

    for manifest in manifests:
        if manifest["protocol_id"] not in protocol_ids:
            errors.append(f"{relative_path(root, manifest['_path'])}: unknown protocol id '{manifest['protocol_id']}'")
        for rubric_id in manifest["rubric_ids"]:
            if rubric_id not in rubric_ids:
                errors.append(f"{relative_path(root, manifest['_path'])}: unknown rubric id '{rubric_id}'")
        for linked_id in manifest["linked_atoms"]:
            if linked_id not in atom_ids:
                errors.append(f"{relative_path(root, manifest['_path'])}: unknown atom id '{linked_id}'")

    router_matrix = load_router_matrix(root)
    for route in router_matrix["routes"]:
        if route["skill_id"] not in skill_ids:
            errors.append(f"references/router-matrix.json: unknown skill id '{route['skill_id']}'")
        if route["protocol_id"] not in protocol_ids:
            errors.append(f"references/router-matrix.json: unknown protocol id '{route['protocol_id']}'")
        if route["rubric_id"] not in rubric_ids:
            errors.append(f"references/router-matrix.json: unknown rubric id '{route['rubric_id']}'")

    for fixture in fixtures:
        route = fixture["expected_route"]
        if route["skill_id"] not in skill_ids:
            errors.append(f"{relative_path(root, fixture['_path'])}: fixture uses unknown skill '{route['skill_id']}'")
        if route["protocol_id"] not in protocol_ids:
            errors.append(f"{relative_path(root, fixture['_path'])}: fixture uses unknown protocol '{route['protocol_id']}'")
        if route["rubric_id"] not in rubric_ids:
            errors.append(f"{relative_path(root, fixture['_path'])}: fixture uses unknown rubric '{route['rubric_id']}'")

    return {
        "errors": sorted(errors),
        "counts": counts,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=str(repo_root()))
    args = parser.parse_args()
    report = validate_repository(Path(args.root))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not report["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
