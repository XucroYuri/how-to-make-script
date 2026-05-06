from __future__ import annotations

import json
from pathlib import Path
import sys
from typing import Any, Dict, Iterable, List, Set, Tuple


ROOT_DIR_NAMES = {
    "knowledge": "knowledge",
    "skills": "skills",
    "schemas": "schemas",
    "references": "references",
    "examples": "examples",
}

ASSET_SCHEMA_BY_TYPE = {
    "knowledge_atom": "knowledge-atom.schema.json",
    "workflow_protocol": "workflow-protocol.schema.json",
    "evaluation_rubric": "evaluation-rubric.schema.json",
}


def repo_root(from_path: Path | None = None) -> Path:
    if from_path is None:
        from_path = Path(__file__).resolve()
    return from_path.parents[1]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_markdown_asset(path: Path) -> Dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path} does not start with JSON frontmatter")

    second = text.find("\n---\n", 4)
    if second == -1:
        raise ValueError(f"{path} is missing closing frontmatter fence")

    frontmatter = text[4:second]
    body = text[second + 5 :].lstrip("\n")
    metadata = json.loads(frontmatter)
    metadata["_body"] = body
    metadata["_path"] = str(path)
    return metadata


def iter_markdown_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        yield path


def collect_markdown_assets(root: Path) -> List[Dict[str, Any]]:
    assets: List[Dict[str, Any]] = []
    knowledge_root = root / ROOT_DIR_NAMES["knowledge"]
    for path in sorted(knowledge_root.rglob("*.md")):
        if path.read_text(encoding="utf-8").startswith("---\n"):
            assets.append(parse_markdown_asset(path))
    return assets


def collect_skill_manifests(root: Path) -> List[Dict[str, Any]]:
    manifests: List[Dict[str, Any]] = []
    for path in sorted((root / ROOT_DIR_NAMES["skills"]).rglob("manifest.json")):
        payload = load_json(path)
        payload["_path"] = str(path)
        manifests.append(payload)
    return manifests


def collect_fixtures(root: Path) -> List[Dict[str, Any]]:
    fixtures_path = root / ROOT_DIR_NAMES["examples"] / "agent" / "fixtures.json"
    payload = load_json(fixtures_path)
    fixtures: List[Dict[str, Any]] = []
    for item in payload:
        item["_path"] = str(fixtures_path)
        fixtures.append(item)
    return fixtures


def collect_nl_routing_bench(root: Path) -> List[Dict[str, Any]]:
    bench_path = root / ROOT_DIR_NAMES["examples"] / "agent" / "nl-routing-bench.json"
    payload = load_json(bench_path)
    entries: List[Dict[str, Any]] = []
    for item in payload:
        item["_path"] = str(bench_path)
        entries.append(item)
    return entries


def collect_e2e_journeys(root: Path) -> List[Dict[str, Any]]:
    journeys_path = root / ROOT_DIR_NAMES["examples"] / "agent" / "e2e-journeys.json"
    payload = load_json(journeys_path)
    journeys: List[Dict[str, Any]] = []
    for item in payload:
        item["_path"] = str(journeys_path)
        journeys.append(item)
    return journeys


def load_router_matrix(root: Path) -> Dict[str, Any]:
    return load_json(root / ROOT_DIR_NAMES["references"] / "router-matrix.json")


def load_background_bundles(root: Path) -> Dict[str, Any]:
    return load_json(root / ROOT_DIR_NAMES["references"] / "background-bundles.json")


def load_schemas(root: Path) -> Dict[str, Dict[str, Any]]:
    schemas: Dict[str, Dict[str, Any]] = {}
    for path in sorted((root / ROOT_DIR_NAMES["schemas"]).glob("*.json")):
        schemas[path.name] = load_json(path)
    return schemas


def validate_schema(instance: Any, schema: Dict[str, Any], path: str = "$") -> List[str]:
    errors: List[str] = []
    if instance is None and schema.get("nullable"):
        return errors
    expected_type = schema.get("type")

    if expected_type == "object":
        if not isinstance(instance, dict):
            return [f"{path}: expected object"]
        for key in schema.get("required", []):
            if key not in instance:
                errors.append(f"{path}: missing required key '{key}'")
        properties = schema.get("properties", {})
        for key, subschema in properties.items():
            if key in instance:
                errors.extend(validate_schema(instance[key], subschema, f"{path}.{key}"))
    elif expected_type == "array":
        if not isinstance(instance, list):
            return [f"{path}: expected array"]
        min_items = schema.get("minItems")
        if min_items is not None and len(instance) < min_items:
            errors.append(f"{path}: expected at least {min_items} items")
        item_schema = schema.get("items")
        if item_schema is not None:
            for index, item in enumerate(instance):
                errors.extend(validate_schema(item, item_schema, f"{path}[{index}]"))
    elif expected_type == "string":
        if not isinstance(instance, str):
            return [f"{path}: expected string"]
    elif expected_type == "integer":
        if not isinstance(instance, int) or isinstance(instance, bool):
            return [f"{path}: expected integer"]
        minimum = schema.get("minimum")
        if minimum is not None and instance < minimum:
            errors.append(f"{path}: expected at least {minimum}")
    elif expected_type == "boolean":
        if not isinstance(instance, bool):
            return [f"{path}: expected boolean"]
    elif expected_type is None:
        pass
    else:
        errors.append(f"{path}: unsupported schema type '{expected_type}'")

    if "const" in schema and instance != schema["const"]:
        errors.append(f"{path}: expected constant {schema['const']!r}")
    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{path}: expected one of {schema['enum']}, got {instance!r}")

    return errors


def parse_supported_outputs(path: Path) -> Set[str]:
    """Parse output IDs from references/supported-outputs.md."""
    outputs: Set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        # Old format: "- `output_name`: description"
        if line.startswith("- `") and "`:" in line:
            outputs.add(line.split("`", 2)[1])
        # New format: "### `output_name`"
        elif line.startswith("### `") and line.endswith("`"):
            outputs.add(line[5:-1])
    return outputs


def parse_constraint_families(path: Path) -> Set[str]:
    """Parse constraint family IDs from the Constraint Families section of taxonomy.md."""
    text = path.read_text(encoding="utf-8")
    try:
        start = text.index("## Constraint Families")
    except ValueError:
        print(f"Warning: heading '## Constraint Families' not found in {path}", file=sys.stderr)
        return set()
    families: Set[str] = set()
    for line in text[start:].splitlines():
        line = line.strip()
        if line.startswith("- `") and line.endswith("`"):
            families.add(line.split("`", 2)[1])
    return families


def collect_asset_index(root: Path) -> Tuple[Dict[str, Dict[str, Any]], List[Dict[str, Any]], List[Dict[str, Any]], List[Dict[str, Any]]]:
    assets = collect_markdown_assets(root)
    manifests = collect_skill_manifests(root)
    fixtures = collect_fixtures(root)
    asset_by_id = {asset["id"]: asset for asset in assets}
    return asset_by_id, assets, manifests, fixtures


def relative_path(root: Path, path: str | Path) -> str:
    return str(Path(path).resolve().relative_to(root.resolve()))
