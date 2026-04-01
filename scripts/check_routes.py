from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List
import sys

if __package__ in (None, ""):
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.lib import collect_fixtures, load_router_matrix, repo_root


def match_route(route: Dict[str, Any], fixture: Dict[str, Any]) -> bool:
    return (
        fixture["intent"] in route["intent"]
        and fixture["medium"] in route["medium"]
        and fixture["stage"] in route["stage"]
        and fixture["output"] in route["output"]
    )


def check_routes(root: Path) -> Dict[str, Any]:
    root = root.resolve()
    router_matrix = load_router_matrix(root)
    fixtures = collect_fixtures(root)
    errors: List[str] = []

    for fixture in fixtures:
        matches = [route for route in router_matrix["routes"] if match_route(route, fixture)]
        if not matches:
            errors.append(f"{fixture['id']}: no route matched")
            continue
        if len(matches) > 1:
            errors.append(f"{fixture['id']}: multiple routes matched")
            continue
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
