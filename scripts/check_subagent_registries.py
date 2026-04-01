from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Set
import sys

if __package__ in (None, ""):
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.lib import repo_root


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def _collect_ids(items: List[Dict[str, Any]]) -> Set[str]:
    return {item["id"] for item in items}


def validate_subagent_registries(root: Path) -> Dict[str, Any]:
    root = root.resolve()
    errors: List[str] = []

    expert = _load_json(root / "references/expert-subagent-library.json")
    topology = _load_json(root / "references/subagent-topology-matrix.json")
    team_matrix = _load_json(root / "references/team-mode-matrix.json")
    team_profiles = _load_json(root / "references/team-workflow-modes.json")
    base_roles = _load_json(root / "references/agent-team-roles.json")

    archetypes = expert["archetypes"]
    cast_templates = expert["cast_templates"]
    archetype_ids = _collect_ids(archetypes)
    persona_ids = {item["id"] for item in archetypes if item["kind"] == "reference_persona"}
    cast_template_ids = _collect_ids(cast_templates)
    topology_ids = _collect_ids(topology["topologies"])
    base_role_ids = _collect_ids(base_roles["roles"])
    team_mode_ids = _collect_ids(team_matrix["modes"])
    team_profile_ids = _collect_ids(team_profiles["modes"])

    if team_profiles.get("canonical_registry") != "references/team-mode-matrix.json":
        errors.append("references/team-workflow-modes.json: canonical_registry must point to references/team-mode-matrix.json")

    if team_matrix.get("mode_profile_registry") != "references/team-workflow-modes.json":
        errors.append("references/team-mode-matrix.json: mode_profile_registry must point to references/team-workflow-modes.json")

    if team_matrix["handoff_packet_fields"] != topology["packet_fields"]:
        errors.append("references/team-mode-matrix.json: handoff_packet_fields must match references/subagent-topology-matrix.json packet_fields")

    for item in archetypes:
        for ref in item.get("composes_with", []):
            if ref not in archetype_ids and ref not in base_role_ids:
                errors.append(f"references/expert-subagent-library.json: unknown composes_with ref '{ref}' in {item['id']}")
        fallback_to = item.get("fallback_to")
        if fallback_to and fallback_to not in archetype_ids and fallback_to not in base_role_ids:
            errors.append(f"references/expert-subagent-library.json: unknown fallback_to ref '{fallback_to}' in {item['id']}")

    for template in cast_templates:
        for ref in template.get("core_roles", []) + template.get("optional_roles", []):
            if ref not in archetype_ids and ref not in base_role_ids:
                errors.append(f"references/expert-subagent-library.json: unknown role ref '{ref}' in template {template['id']}")
        for ref in template.get("persona_candidates", []):
            if ref not in persona_ids:
                errors.append(f"references/expert-subagent-library.json: unknown persona ref '{ref}' in template {template['id']}")

    for mode in team_matrix["modes"]:
        profile_id = mode.get("profile_id")
        if profile_id and profile_id not in team_profile_ids:
            errors.append(f"references/team-mode-matrix.json: unknown profile_id '{profile_id}' in mode {mode['id']}")
        for ref in mode.get("recommended_cast_templates", []):
            if ref not in cast_template_ids:
                errors.append(f"references/team-mode-matrix.json: unknown cast template '{ref}' in mode {mode['id']}")
        for ref in mode.get("recommended_dispatch_topologies", []):
            if ref not in topology_ids:
                errors.append(f"references/team-mode-matrix.json: unknown topology '{ref}' in mode {mode['id']}")

    for mode in team_profiles["modes"]:
        canonical_mode_id = mode.get("canonical_mode_id")
        if canonical_mode_id not in team_mode_ids:
            errors.append(f"references/team-workflow-modes.json: unknown canonical_mode_id '{canonical_mode_id}' in mode {mode['id']}")
        for ref in mode.get("recommended_cast_templates", []):
            if ref not in cast_template_ids:
                errors.append(f"references/team-workflow-modes.json: unknown cast template '{ref}' in mode {mode['id']}")
        for ref in mode.get("recommended_dispatch_topologies", []):
            if ref not in topology_ids:
                errors.append(f"references/team-workflow-modes.json: unknown topology '{ref}' in mode {mode['id']}")
        for ref in mode.get("recommended_persona_candidates", []):
            if ref not in persona_ids:
                errors.append(f"references/team-workflow-modes.json: unknown persona '{ref}' in mode {mode['id']}")

    return {
      "errors": sorted(errors),
      "counts": {
          "archetype_count": len(archetypes),
          "cast_template_count": len(cast_templates),
          "topology_count": len(topology["topologies"]),
          "team_mode_count": len(team_matrix["modes"]),
          "team_profile_count": len(team_profiles["modes"]),
      },
    }


def main() -> int:
    report = validate_subagent_registries(repo_root())
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not report["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
