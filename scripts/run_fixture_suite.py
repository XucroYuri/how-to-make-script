from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict
import sys

if __package__ in (None, ""):
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.check_routes import check_routes
from scripts.check_golden_artifact_formats import check_golden_artifact_formats
from scripts.lib import collect_fixtures, repo_root
from scripts.validate_assets import validate_repository


def run_fixture_suite(root: Path) -> Dict[str, Any]:
    root = root.resolve()
    validation = validate_repository(root)
    route_report = check_routes(root)
    golden_format_report = check_golden_artifact_formats(root)
    fixtures = collect_fixtures(root)

    media = sorted({fixture["medium"] for fixture in fixtures})
    stages = sorted({fixture["stage"] for fixture in fixtures})
    outputs = sorted({fixture["output"] for fixture in fixtures})

    golden_errors = []
    golden_root = root / "examples" / "golden"
    for golden_dir in sorted(path for path in golden_root.iterdir() if path.is_dir()):
        for filename in ("request.md", "route.json", "artifact.md"):
            if not (golden_dir / filename).exists():
                golden_errors.append(f"examples/golden/{golden_dir.name}/{filename} missing")

    errors = validation["errors"] + route_report["errors"] + golden_format_report["errors"] + golden_errors
    return {
        "errors": errors,
        "coverage": {
            "fixture_count": len(fixtures),
            "media": media,
            "stages": stages,
            "outputs": outputs,
            "golden_examples": golden_format_report["coverage"]["examples"],
            "golden_outputs": golden_format_report["coverage"]["outputs"],
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=str(repo_root()))
    args = parser.parse_args()
    report = run_fixture_suite(Path(args.root))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not report["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
