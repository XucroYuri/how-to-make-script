from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List
import sys

if __package__ in (None, ""):
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.lib import collect_fixtures, load_json, load_router_matrix, repo_root


def normalized_constraint_keys(register: Dict[str, Any], fixture: Dict[str, Any]) -> set[str]:
    aliases = register.get("aliases", {})
    detail_keys = register.get("detail_keys", {})
    keys = set()
    for key in fixture.get("constraints", {}):
        keys.add(key)
        if key in aliases:
            keys.add(aliases[key]["canonical"])
        if key in detail_keys:
            keys.add(detail_keys[key]["family"])
    return keys


def match_route(
    register: Dict[str, Any], route: Dict[str, Any], fixture: Dict[str, Any]
) -> bool:
    if not (
        fixture["intent"] in route["intent"]
        and fixture["medium"] in route["medium"]
        and fixture["stage"] in route["stage"]
        and fixture["output"] in route["output"]
    ):
        return False

    # required_constraint_signals: all must be present in fixture constraints
    required = route.get("required_constraint_signals", [])
    if required:
        constraints = normalized_constraint_keys(register, fixture)
        return all(key in constraints for key in required)

    return True


def constraint_score(register: Dict[str, Any], route: Dict[str, Any], fixture: Dict[str, Any]) -> int:
    constraints = normalized_constraint_keys(register, fixture)
    return sum(1 for key in route.get("constraint_signals", []) if key in constraints)


def check_routes(root: Path) -> Dict[str, Any]:
    root = root.resolve()
    router_matrix = load_router_matrix(root)
    fixtures = collect_fixtures(root)
    register = load_json(root / "references" / "constraint-key-register.json")
    errors: List[str] = []

    for fixture in fixtures:
        matches = [route for route in router_matrix["routes"] if match_route(register, route, fixture)]
        if not matches:
            errors.append(f"{fixture['id']}: no route matched")
            continue
        if len(matches) > 1:
            scored = sorted(
                ((constraint_score(register, route, fixture), route) for route in matches),
                key=lambda item: item[0],
                reverse=True,
            )
            top_score = scored[0][0]
            top = [route for score, route in scored if score == top_score]
            if len(top) > 1:
                # Ambiguity: multiple routes with equal scores — report as ambiguity
                route_ids = [r["skill_id"] for r in top]
                errors.append(
                    f"{fixture['id']}: ambiguous — multiple routes matched with equal score: {route_ids}"
                )
                continue
            match = top[0]
        else:
            match = matches[0]
        expected = fixture["expected_route"]
        for key in ("skill_id", "protocol_id", "rubric_id"):
            if match[key] != expected[key]:
                errors.append(
                    f"{fixture['id']}: expected {key}={expected[key]!r}, got {match[key]!r}"
                )

    return {
        "errors": errors,
        "fixture_count": len(fixtures),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=str(repo_root()))
    args = parser.parse_args()
    report = check_routes(Path(args.root))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not report["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
