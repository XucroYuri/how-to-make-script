from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List
import sys

if __package__ in (None, ""):
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.lib import collect_asset_index, load_background_bundles, relative_path, repo_root


# ---------- display mode (original) ----------

def build_index(root: Path) -> Dict[str, Any]:
    root = root.resolve()
    _, assets, manifests, fixtures = collect_asset_index(root)

    asset_index: Dict[str, List[Dict[str, Any]]] = {
        "knowledge_atom": [],
        "workflow_protocol": [],
        "evaluation_rubric": [],
    }

    for asset in assets:
        asset_index[asset["type"]].append(
            {
                "id": asset["id"],
                "title": asset["title"],
                "path": relative_path(root, asset["_path"]),
            }
        )

    skills = [
        {
            "id": manifest["id"],
            "name": manifest["name"],
            "entrypoint": manifest["entrypoint"],
            "protocol_id": manifest["protocol_id"],
        }
        for manifest in manifests
        if manifest.get("surface", "public") == "public"
    ]

    bundle_registry = load_background_bundles(root)
    background_bundles = [
        {
            "id": bundle["id"],
            "title": bundle["title"],
            "docs": bundle["docs"],
            "primary_outputs": bundle["primary_outputs"],
        }
        for bundle in bundle_registry.get("bundles", [])
    ]

    return {
        "assets": asset_index,
        "skills": skills,
        "background_bundles": background_bundles,
        "fixtures": [
            {
                "id": fixture["id"],
                "medium": fixture["medium"],
                "stage": fixture["stage"],
                "output": fixture["output"],
            }
            for fixture in fixtures
        ],
    }


# ---------- runtime mode ----------

ADJUNCT_TRIGGERS: Dict[str, Dict[str, str]] = {
    "voice_target":        {"bundle": "expression-lens", "mode": "smallest_adjunct"},
    "language_register":   {"bundle": "expression-lens", "mode": "smallest_adjunct"},
    "ip_continuity":       {"bundle": "expression-lens", "mode": "smallest_adjunct"},
    "experiential_depth":  {"bundle": "expression-lens", "mode": "smallest_adjunct"},
    "visual_vocab_locale": {"bundle": "visual-lens",     "mode": "smallest_adjunct"},
    "prompt_runtime":      {"bundle": "visual-lens",     "mode": "smallest_adjunct"},
    "shot_granularity":    {"bundle": "visual-lens",     "mode": "smallest_adjunct"},
    "team_mode":           {"bundle": "team-lens",       "mode": "smallest_adjunct"},
    "coordination_model":  {"bundle": "team-lens",       "mode": "smallest_adjunct"},
    "parallelism_budget":  {"bundle": "team-lens",       "mode": "smallest_adjunct"},
    "human_gate_level":    {"bundle": "team-lens",       "mode": "smallest_adjunct"},
    "subagent_family":     {"bundle": "subagent-lens",   "mode": "smallest_adjunct"},
    "persona_policy":      {"bundle": "subagent-lens",   "mode": "smallest_adjunct"},
    "dispatch_topology":   {"bundle": "subagent-lens",   "mode": "smallest_adjunct"},
    "target_contract":     {"bundle": "quality-gating",  "mode": "smallest_adjunct"},
    "audit_scope":         {"bundle": "quality-gating",  "mode": "smallest_adjunct"},
    "check_depth":         {"bundle": "quality-gating",  "mode": "smallest_adjunct"},
    "lens_focus":          {"bundle": "quality-gating",  "mode": "smallest_adjunct"},
    "recheck_mode":        {"bundle": "quality-gating",  "mode": "smallest_adjunct"},
    "acceptance_bar":      {"bundle": "quality-gating",  "mode": "smallest_adjunct"},
    "audience_segment":    {"bundle": "reality-lens",    "mode": "smallest_adjunct"},
    "audience_need_state": {"bundle": "reality-lens",    "mode": "smallest_adjunct"},
    "commissioning_context": {"bundle": "reality-lens",  "mode": "smallest_adjunct"},
    "business_model":      {"bundle": "reality-lens",    "mode": "smallest_adjunct"},
    "release_window":      {"bundle": "reality-lens",    "mode": "smallest_adjunct"},
    "platform":            {"bundle": "reality-lens",    "mode": "smallest_adjunct"},
    "writer_maturity":     {"bundle": "reality-lens",    "mode": "smallest_adjunct"},
    "project_horizon":     {"bundle": "project-surface", "mode": "smallest_adjunct"},
    "phase_focus":         {"bundle": "project-surface", "mode": "smallest_adjunct"},
    "truth_surface_policy": {"bundle": "project-surface", "mode": "smallest_adjunct"},
}

EXPRESSION_LENS_ATOMS: Dict[str, List[str]] = {
    "scene_draft":        ["ka.character-voice-consistency", "ka.embodied-text-pressure", "ka.dialogue-subtext"],
    "screenplay_draft":   ["ka.character-voice-consistency", "ka.embodied-text-pressure", "ka.dialogue-subtext", "ka.cinematic-prose-register"],
    "dialogue_polish":    ["ka.character-voice-consistency", "ka.embodied-text-pressure", "ka.dialogue-subtext"],
    "commercial_script":  ["ka.register-adaptation", "ka.embodied-text-pressure"],
    "adaptation":         ["ka.ip-voice-continuity", "ka.character-voice-consistency", "ka.register-adaptation"],
}


def build_runtime_index(root: Path) -> Dict[str, Any]:
    root = root.resolve()
    from scripts.lib import load_router_matrix, load_json

    router_matrix = load_router_matrix(root)
    _, assets, manifests, _ = collect_asset_index(root)

    manifest_by_id = {m["id"]: m for m in manifests}
    asset_by_id = {a["id"]: a for a in assets}

    # A1: route_lookup — output -> intent -> medium -> stage -> route info
    route_lookup: Dict[str, Any] = {}
    for route in router_matrix["routes"]:
        for output in route["output"]:
            route_lookup.setdefault(output, {})
            for intent in route["intent"]:
                route_lookup[output].setdefault(intent, {})
                for medium in route["medium"]:
                    route_lookup[output][intent].setdefault(medium, {})
                    for stage in route["stage"]:
                        skill_manifest = manifest_by_id.get(route["skill_id"], {})
                        route_lookup[output][intent][medium][stage] = {
                            "skill": route["skill_id"],
                            "protocol": route["protocol_id"],
                            "rubric": route["rubric_id"],
                            "atoms": skill_manifest.get("linked_atoms", []),
                            "default_mode": skill_manifest.get("default_loading_mode", "focus_pack"),
                            "constraint_signals": route.get("constraint_signals", []),
                            "required_signals": route.get("required_constraint_signals", []),
                        }

    # fallback_chains — from manifest fallback_to_skill_id
    fallback_chains: Dict[str, Any] = {}
    for m in manifests:
        fallback = m.get("fallback_to_skill_id")
        fallback_chains[m["id"]] = fallback

    # A2: atom_by_protocol — mandatory vs optional atoms per protocol
    protocols = [a for a in assets if a["type"] == "workflow_protocol"]
    atom_by_protocol: Dict[str, Any] = {}
    for proto in protocols:
        linked = proto.get("linked_atoms", [])
        atom_by_protocol[proto["id"]] = {
            "mandatory": linked,
            "optional": [],
            "budget_class": proto.get("budget_class", "M"),
        }

    # atom_by_tag — keyword-based inverted index from atom kind/summary
    atom_by_tag: Dict[str, List[str]] = {}
    for a in assets:
        if a["type"] != "knowledge_atom":
            continue
        tags = _extract_tags(a)
        for tag in tags:
            atom_by_tag.setdefault(tag, []).append(a["id"])

    # adjunct_bundles with atom lists for expression lens
    adjunct_bundles: Dict[str, Any] = {
        "triggers": ADJUNCT_TRIGGERS,
        "expression_lens_atoms": EXPRESSION_LENS_ATOMS,
    }

    return {
        "route_lookup": route_lookup,
        "fallback_chains": fallback_chains,
        "atom_by_protocol": atom_by_protocol,
        "atom_by_tag": atom_by_tag,
        "adjunct_bundles": adjunct_bundles,
    }


def _extract_tags(atom: Dict[str, Any]) -> List[str]:
    """Extract searchable tags from a knowledge atom's kind and id."""
    tags: List[str] = []
    atom_id = atom.get("id", "")
    kind = atom.get("kind", "")

    # From id prefix after 'ka.'
    if atom_id.startswith("ka."):
        slug = atom_id[3:]
        # Split on hyphens to get individual terms
        for part in slug.split("-"):
            if len(part) > 2:
                tags.append(part)

    # From kind field
    if kind:
        tags.append(kind)

    return tags


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=str(repo_root()))
    parser.add_argument("--mode", choices=["display", "runtime"], default="display")
    args = parser.parse_args()

    if args.mode == "runtime":
        index = build_runtime_index(Path(args.root))
    else:
        index = build_index(Path(args.root))

    print(json.dumps(index, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
