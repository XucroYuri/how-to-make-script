from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Set
import sys

if __package__ in (None, ""):
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.lib import collect_asset_index, load_json, load_router_matrix, repo_root


OUTPUT_RE = re.compile(r"^- `([^`]+)`", re.MULTILINE)
SUBSKILL_RE = re.compile(r"^- \[`([^`]+)`\]\(([^)]+)\)", re.MULTILINE)


def parse_root_outputs(skill_text: str) -> Set[str]:
    start = skill_text.index("## Default Output Contracts")
    end = skill_text.index("## Sub-Skills")
    return set(OUTPUT_RE.findall(skill_text[start:end]))


def parse_root_subskills(skill_text: str) -> Set[str]:
    start = skill_text.index("## Sub-Skills")
    end = skill_text.index("## Primary References")
    return {path for _, path in SUBSKILL_RE.findall(skill_text[start:end])}


def parse_supported_outputs(path: Path) -> Set[str]:
    return set(OUTPUT_RE.findall(path.read_text(encoding="utf-8")))


def parse_taxonomy_section(path: Path, heading: str) -> Set[str]:
    text = path.read_text(encoding="utf-8")
    start = text.index(f"## {heading}")
    next_heading = text.find("\n## ", start + 1)
    end = len(text) if next_heading == -1 else next_heading
    return set(OUTPUT_RE.findall(text[start:end]))


def parse_constraint_families(path: Path) -> Set[str]:
    text = path.read_text(encoding="utf-8")
    start = text.index("## Constraint Families")
    return set(OUTPUT_RE.findall(text[start:]))


def check_semantic_consistency(root: Path) -> Dict[str, Any]:
    root = root.resolve()
    errors: List[str] = []

    _, assets, manifests, fixtures = collect_asset_index(root)
    router = load_router_matrix(root)
    skill_text = (root / "SKILL.md").read_text(encoding="utf-8")
    taxonomy_path = root / "references" / "taxonomy.md"
    supported_outputs_path = root / "references" / "supported-outputs.md"
    constraint_register = load_json(root / "references" / "constraint-key-register.json")

    root_outputs = parse_root_outputs(skill_text)
    root_subskills = parse_root_subskills(skill_text)
    supported_outputs = parse_supported_outputs(supported_outputs_path)
    taxonomy_outputs = parse_taxonomy_section(taxonomy_path, "Outputs")
    taxonomy_constraints = parse_constraint_families(taxonomy_path)

    protocol_outputs: Set[str] = set()
    protocol_map: Dict[str, Dict[str, Any]] = {}
    rubric_map: Dict[str, Dict[str, Any]] = {}
    for asset in assets:
        if asset["type"] == "workflow_protocol":
            protocol_map[asset["id"]] = asset
            protocol_outputs.update(asset["output_contract"])
        if asset["type"] == "evaluation_rubric":
            rubric_map[asset["id"]] = asset

    route_outputs = {output for route in router["routes"] for output in route["output"]}
    fixture_outputs = {fixture["output"] for fixture in fixtures}

    public_manifests = [manifest for manifest in manifests if manifest.get("surface", "public") == "public"]
    internal_manifests = [manifest for manifest in manifests if manifest.get("surface") == "internal"]
    public_manifest_outputs = {
        output for manifest in public_manifests for output in manifest["supports"]["outputs"]
    }

    output_sets = {
        "SKILL.md": root_outputs,
        "references/supported-outputs.md": supported_outputs,
        "references/taxonomy.md": taxonomy_outputs,
        "workflow protocols": protocol_outputs,
        "router matrix": route_outputs,
        "public manifests": public_manifest_outputs,
        "fixtures": fixture_outputs,
    }

    baseline_name, baseline_outputs = next(iter(output_sets.items()))
    for name, outputs in output_sets.items():
        if outputs != baseline_outputs:
            errors.append(
                f"output drift between {baseline_name} and {name}: "
                f"missing={sorted(baseline_outputs - outputs)}, extra={sorted(outputs - baseline_outputs)}"
            )

    routed_skill_ids = {route["skill_id"] for route in router["routes"]}
    for manifest in public_manifests:
        skill_id = manifest["id"]
        entrypoint = manifest["entrypoint"]
        if skill_id not in routed_skill_ids:
            errors.append(f"{entrypoint}: public skill is not routeable")
        if entrypoint not in root_subskills:
            errors.append(f"{entrypoint}: public skill is missing from root SKILL sub-skill list")
        protocol = protocol_map.get(manifest["protocol_id"])
        if protocol is None:
            continue
        missing_atoms = sorted(set(protocol["linked_atoms"]) - set(manifest["linked_atoms"]))
        if missing_atoms:
            errors.append(f"{entrypoint}: manifest missing protocol atoms {missing_atoms}")
        missing_outputs = sorted(set(protocol["output_contract"]) - set(manifest["supports"]["outputs"]))
        if missing_outputs:
            errors.append(f"{entrypoint}: manifest outputs missing protocol contracts {missing_outputs}")
        for rubric_id in manifest["rubric_ids"]:
            rubric = rubric_map.get(rubric_id)
            if rubric is None:
                continue
            uncovered = sorted(set(protocol["output_contract"]) - set(rubric["applies_to"]))
            if uncovered:
                errors.append(
                    f"{entrypoint}: rubric {rubric_id!r} does not cover protocol outputs {uncovered}"
                )

    for manifest in internal_manifests:
        skill_id = manifest["id"]
        entrypoint = manifest["entrypoint"]
        if skill_id in routed_skill_ids:
            errors.append(f"{entrypoint}: internal skill must not be present in router matrix")
        if entrypoint in root_subskills:
            errors.append(f"{entrypoint}: internal skill must not be listed as a public root sub-skill")

    signal_required_outputs = {
        "audience_fit_note",
        "development_brief",
        "learning_path",
        "research_background_map",
        "path_options",
        "boundary_map",
        "scope_correction",
        "pattern_reference_pack",
        "context_loading_plan",
        "story_memory_checkpoint",
        "voice_style_guide",
        "visual_language_pack",
        "screen_to_video_brief",
        "team_workflow_blueprint",
        "expert_subagent_cast",
        "subagent_dispatch_plan",
        "project_surface_map",
        "quality_gate_report",
    }

    for route in router["routes"]:
        signals = route.get("constraint_signals", [])
        if any(output in signal_required_outputs for output in route["output"]) and not signals:
            errors.append(
                f"references/router-matrix.json: route for outputs {route['output']} is missing constraint_signals"
            )
        rubric = rubric_map.get(route["rubric_id"])
        if rubric is not None:
            uncovered = sorted(set(route["output"]) - set(rubric["applies_to"]))
            if uncovered:
                errors.append(
                    "references/router-matrix.json: "
                    f"rubric {route['rubric_id']!r} does not cover route outputs {uncovered}"
                )
        for signal in signals:
            if signal not in taxonomy_constraints:
                errors.append(
                    f"references/router-matrix.json: unknown constraint signal {signal!r} "
                    f"for outputs {route['output']}"
                )

    aliases = constraint_register.get("aliases", {})
    detail_keys = constraint_register.get("detail_keys", {})
    for key, payload in aliases.items():
        canonical = payload.get("canonical")
        if canonical not in taxonomy_constraints:
            errors.append(
                f"references/constraint-key-register.json: alias {key!r} points to unknown canonical family {canonical!r}"
            )
    for key, payload in detail_keys.items():
        family = payload.get("family")
        if family not in taxonomy_constraints:
            errors.append(
                f"references/constraint-key-register.json: detail key {key!r} points to unknown family {family!r}"
            )

    allowed_constraint_keys = set(taxonomy_constraints) | set(aliases) | set(detail_keys)
    for fixture in fixtures:
        for key in fixture["constraints"]:
            if key not in allowed_constraint_keys:
                errors.append(
                    f"examples/agent/fixtures.json: fixture {fixture['id']} uses unknown constraint key {key!r}"
                )
        rubric = rubric_map.get(fixture["expected_route"]["rubric_id"])
        if rubric is not None and fixture["output"] not in set(rubric["applies_to"]):
            errors.append(
                "examples/agent/fixtures.json: "
                f"fixture {fixture['id']} expects rubric {fixture['expected_route']['rubric_id']!r} "
                f"which does not apply to output {fixture['output']!r}"
            )

    return {
        "errors": sorted(errors),
        "summary": {
            "public_skill_count": len(public_manifests),
            "internal_skill_count": len(internal_manifests),
            "output_count": len(baseline_outputs),
            "constraint_family_count": len(taxonomy_constraints),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=str(repo_root()))
    args = parser.parse_args()
    report = check_semantic_consistency(Path(args.root))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not report["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
