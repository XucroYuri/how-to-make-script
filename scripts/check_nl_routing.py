"""Validate the natural-language routing benchmark.

This script checks structural properties of the NL routing bench:
- every entry has required fields
- expected_behavior is one of the known values
- expected_route skill_id references an existing skill when present
- ambiguous classifications have clarification_target
- coverage: bench should exercise all output contract families
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List
import sys

if __package__ in (None, ""):
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.lib import collect_skill_manifests, load_router_matrix, repo_root

REQUIRED_FIELDS = ["id", "query", "expected_classification", "expected_behavior"]
KNOWN_BEHAVIORS = {
    "should_route",
    "should_ask_clarification",
    "should_route_or_ask",
    "should_ask_clarification_or_route_adjunct",
}
ROUTE_INTENT_FAMILIES = {"should_route", "should_route_or_ask"}


def check_nl_routing(root: Path) -> Dict[str, Any]:
    root = root.resolve()
    bench_path = root / "examples" / "agent" / "nl-routing-bench.json"
    if not bench_path.exists():
        return {"errors": ["nl-routing-bench.json not found"], "entry_count": 0}

    bench: List[Dict[str, Any]] = json.loads(
        bench_path.read_text(encoding="utf-8")
    )
    manifests = collect_skill_manifests(root)
    skill_ids = {m["id"] for m in manifests}
    router_matrix = load_router_matrix(root)
    output_families = set()
    for route in router_matrix["routes"]:
        for output in route["output"]:
            output_families.add(output)

    errors: List[str] = []
    covered_behaviors: Dict[str, int] = {}
    covered_outputs: set = set()
    covered_media: set = set()

    for entry in bench:
        eid = entry.get("id", "UNKNOWN")

        # Required fields
        for field in REQUIRED_FIELDS:
            if field not in entry:
                errors.append(f"{eid}: missing required field '{field}'")

        behavior = entry.get("expected_behavior", "")
        covered_behaviors[behavior] = covered_behaviors.get(behavior, 0) + 1

        # Behavior must be known
        if behavior and behavior not in KNOWN_BEHAVIORS:
            errors.append(
                f"{eid}: unknown behavior '{behavior}', expected one of {KNOWN_BEHAVIORS}"
            )

        # Route entries must reference existing skills
        if behavior in ROUTE_INTENT_FAMILIES and "expected_route" in entry:
            route = entry["expected_route"]
            if "skill_id" in route and route["skill_id"] not in skill_ids:
                errors.append(f"{eid}: references unknown skill '{route['skill_id']}'")

        # Ambiguous classifications with should_ask_clarification should have clarification_target
        classification = entry.get("expected_classification", {})
        has_ambiguity = any(
            v == "AMBIGUOUS" for v in classification.values()
        )
        if (
            has_ambiguity
            and behavior == "should_ask_clarification"
            and "clarification_target" not in entry
        ):
            errors.append(
                f"{eid}: has AMBIGUOUS classification with should_ask_clarification but no clarification_target"
            )

        # Track coverage
        output = classification.get("output", "")
        if output and output != "AMBIGUOUS":
            covered_outputs.add(output)
        medium = classification.get("medium", "")
        if medium and medium != "AMBIGUOUS":
            covered_media.add(medium)

    # Coverage report
    missing_outputs = output_families - covered_outputs
    coverage_report = {
        "entry_count": len(bench),
        "behaviors": covered_behaviors,
        "output_coverage": f"{len(covered_outputs)}/{len(output_families)}",
        "medium_coverage": f"{len(covered_media)}/9",
    }
    if missing_outputs:
        coverage_report["uncovered_outputs"] = sorted(missing_outputs)

    return {
        "errors": errors,
        "coverage": coverage_report,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=str(repo_root()))
    args = parser.parse_args()
    report = check_nl_routing(Path(args.root))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not report["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
