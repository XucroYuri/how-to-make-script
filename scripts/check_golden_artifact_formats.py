from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Tuple
import sys

if __package__ in (None, ""):
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.lib import collect_asset_index, load_json, load_schemas, relative_path, repo_root, validate_schema


LIST_ITEM_PATTERN = re.compile(r"^\s*(?:- |\d+\. )")
SCRIPT_LABEL_PATTERN = re.compile(r"^\s*-\s*(?P<label>[A-Za-z]+):\s*(?P<value>.*\S)?\s*$")
SCRIPT_BEAT_FIELD_PATTERN = re.compile(r"^(?P<label>[A-Za-z]+):\s*(?P<value>.+)$")


def parse_title_and_sections(text: str) -> Tuple[str | None, Dict[str, List[str]]]:
    title: str | None = None
    sections: Dict[str, List[str]] = {}
    current_section: str | None = None

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if line.startswith("# ") and title is None:
            title = line[2:].strip()
            current_section = None
            continue
        if line.startswith("## "):
            current_section = line[3:].strip()
            sections[current_section] = []
            continue
        if current_section is not None:
            sections[current_section].append(line)

    return title, sections


def count_list_items(lines: List[str]) -> int:
    return sum(1 for line in lines if LIST_ITEM_PATTERN.match(line))


def check_script_block_contract(text: str, contract: Dict[str, Any], artifact_label: str) -> List[str]:
    title, sections = parse_title_and_sections(text)
    del title
    errors: List[str] = []
    script_section = contract["script_section"]
    lines = sections.get(script_section)
    if lines is None:
        return [f"{artifact_label}: missing script section '## {script_section}'"]

    required_labels = set(contract["scene_labels"])
    av_labels = set(contract["av_labels"])
    allowed_labels = required_labels | av_labels | {"Beat"}
    beat_requires_performance = contract["beat_requires_performance"]
    scene_count = 0
    dialogue_beat_count = 0
    current_scene: Dict[str, Any] | None = None
    previous_label: str | None = None

    def finish_scene() -> None:
        nonlocal current_scene
        if current_scene is None:
            return
        missing = sorted(label for label in required_labels if current_scene["labels"].get(label, 0) < 1)
        if missing:
            errors.append(
                f"{artifact_label}: scene {current_scene['index']} missing required labels {missing}"
            )
        current_scene = None

    for raw_line in lines:
        line = raw_line.rstrip()
        if not line.strip():
            continue

        match = SCRIPT_LABEL_PATTERN.match(line)
        if match is None:
            errors.append(
                f"{artifact_label}: unexpected freeform script line {line!r}; "
                "use '- Label: value' screenplay blocks"
            )
            previous_label = None
            continue

        label = match.group("label")
        value = (match.group("value") or "").strip()
        if label not in allowed_labels:
            errors.append(f"{artifact_label}: unknown script label {label!r}")
            previous_label = None
            continue

        if label == "Scene":
            finish_scene()
            scene_count += 1
            current_scene = {
                "index": scene_count,
                "labels": {"Scene": 1},
            }
            if not value:
                errors.append(f"{artifact_label}: scene {scene_count} has empty Scene label")
            previous_label = label
            continue

        if current_scene is None:
            errors.append(f"{artifact_label}: label {label!r} appears before the first Scene block")
            previous_label = None
            continue

        current_scene["labels"][label] = current_scene["labels"].get(label, 0) + 1
        if not value:
            errors.append(
                f"{artifact_label}: scene {current_scene['index']} label {label!r} has empty value"
            )
            previous_label = label
            continue

        if label != "Beat":
            previous_label = label
            continue

        dialogue_beat_count += 1
        parts = [part.strip() for part in value.split("|")]
        if not parts or not parts[0]:
            errors.append(
                f"{artifact_label}: scene {current_scene['index']} beat is missing a speaker"
            )
            previous_label = label
            continue

        beat_fields: Dict[str, str] = {}
        for field_text in parts[1:]:
            field_match = SCRIPT_BEAT_FIELD_PATTERN.match(field_text)
            if field_match is None:
                errors.append(
                    f"{artifact_label}: scene {current_scene['index']} beat has malformed field {field_text!r}"
                )
                continue
            field_label = field_match.group("label")
            if field_label not in {"Performance", "Action", "Dialogue"}:
                errors.append(
                    f"{artifact_label}: scene {current_scene['index']} beat has unknown field {field_label!r}"
                )
                continue
            beat_fields[field_label] = field_match.group("value").strip()

        if "Dialogue" not in beat_fields or not beat_fields["Dialogue"]:
            errors.append(
                f"{artifact_label}: scene {current_scene['index']} beat is missing Dialogue text"
            )

        has_inline_carrier = bool(beat_fields.get("Performance") or beat_fields.get("Action"))
        has_adjacent_action = previous_label == "Action"
        if beat_requires_performance and not (has_inline_carrier or has_adjacent_action):
            errors.append(
                f"{artifact_label}: scene {current_scene['index']} has bare dialogue beat for {parts[0]!r}"
            )

        previous_label = label

    finish_scene()

    if scene_count < contract["min_scenes"]:
        errors.append(
            f"{artifact_label}: needs at least {contract['min_scenes']} scenes, got {scene_count}"
        )
    if dialogue_beat_count < contract["min_dialogue_beats"]:
        errors.append(
            f"{artifact_label}: needs at least {contract['min_dialogue_beats']} dialogue beats, got {dialogue_beat_count}"
        )

    return errors


def check_golden_artifact_formats(root: Path) -> Dict[str, Any]:
    root = root.resolve()
    schemas = load_schemas(root)
    contracts = load_json(root / "references" / "output-format-contracts.json")
    schema_errors = validate_schema(
        contracts,
        schemas["output-format-contracts.schema.json"],
    )

    errors = [
        f"references/output-format-contracts.json: {message}"
        for message in schema_errors
    ]
    contract_by_output = {
        contract["output"]: contract
        for contract in contracts.get("contracts", [])
    }

    asset_by_id, _, _, _ = collect_asset_index(root)
    examples: List[str] = []
    outputs: List[str] = []

    golden_root = root / "examples" / "golden"
    for example_dir in sorted(path for path in golden_root.iterdir() if path.is_dir()):
        examples.append(example_dir.name)
        route_path = example_dir / "route.json"
        artifact_path = example_dir / "artifact.md"

        if not route_path.exists() or not artifact_path.exists():
            continue

        route = load_json(route_path)
        output = route.get("output")
        if not output:
            errors.append(f"{relative_path(root, route_path)}: missing required key 'output'")
            continue

        outputs.append(output)

        contract = contract_by_output.get(output)
        if contract is None:
            errors.append(
                f"{relative_path(root, route_path)}: output {output!r} has no format contract"
            )
            continue

        protocol_id = route.get("protocol_id")
        protocol = asset_by_id.get(protocol_id)
        if protocol is None:
            errors.append(
                f"{relative_path(root, route_path)}: unknown protocol id {protocol_id!r}"
            )
            continue
        if output not in protocol.get("output_contract", []):
            errors.append(
                f"{relative_path(root, route_path)}: output {output!r} not declared in protocol {protocol_id!r}"
            )

        artifact_text = artifact_path.read_text(encoding="utf-8")
        title, sections = parse_title_and_sections(artifact_text)

        title_includes = contract["title_includes"]
        if not title or title_includes not in title:
            errors.append(
                f"{relative_path(root, artifact_path)}: title should include {title_includes!r}"
            )

        for section in contract["required_sections"]:
            heading = section["heading"]
            if heading not in sections:
                errors.append(
                    f"{relative_path(root, artifact_path)}: missing required section '## {heading}'"
                )
                continue
            item_count = count_list_items(sections[heading])
            if item_count < section["min_items"]:
                errors.append(
                    f"{relative_path(root, artifact_path)}: section '## {heading}' needs at least {section['min_items']} list items, got {item_count}"
                )

        if "script_block_contract" in contract:
            errors.extend(
                check_script_block_contract(
                    artifact_text,
                    contract["script_block_contract"],
                    relative_path(root, artifact_path),
                )
            )

    return {
        "errors": errors,
        "coverage": {
            "examples": examples,
            "outputs": sorted(set(outputs)),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=str(repo_root()))
    args = parser.parse_args()
    report = check_golden_artifact_formats(Path(args.root))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not report["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
