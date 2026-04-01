from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List
import sys

if __package__ in (None, ""):
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.lib import load_router_matrix, repo_root


def _overlap(a: List[str], b: List[str]) -> List[str]:
    return sorted(set(a).intersection(b))


def check_route_overlaps(root: Path) -> Dict[str, Any]:
    root = root.resolve()
    routes = load_router_matrix(root)["routes"]
    errors: List[str] = []

    for i, left in enumerate(routes):
        for j in range(i + 1, len(routes)):
            right = routes[j]
            intent = _overlap(left["intent"], right["intent"])
            medium = _overlap(left["medium"], right["medium"])
            stage = _overlap(left["stage"], right["stage"])
            output = _overlap(left["output"], right["output"])
            if intent and medium and stage and output:
                left_signals = sorted(left.get("constraint_signals", []))
                right_signals = sorted(right.get("constraint_signals", []))
                errors.append(
                    "Potential overlapping routes: "
                    f"{i} and {j} share "
                    f"intent={intent}, medium={medium}, stage={stage}, output={output}, "
                    f"left_signals={left_signals}, right_signals={right_signals}"
                )

    return {
        "errors": errors,
        "route_count": len(routes),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=str(repo_root()))
    args = parser.parse_args()
    report = check_route_overlaps(Path(args.root))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not report["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
