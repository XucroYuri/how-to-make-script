from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List
import sys

if __package__ in (None, ""):
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.lib import collect_asset_index, relative_path, repo_root


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

    return {
        "assets": asset_index,
        "skills": skills,
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=str(repo_root()))
    args = parser.parse_args()
    index = build_index(Path(args.root))
    print(json.dumps(index, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
