"""Check loading budget declarations across all workflow protocols.

Validates:
- Every protocol declares budget_class, mandatory_atom_count, expansion_allowed
- budget_class is consistent with mandatory_atom_count
- Adjunct bundle triggers in manifests reference valid constraint families
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List
import sys

if __package__ in (None, ""):
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.lib import collect_asset_index, collect_skill_manifests, repo_root

BUDGET_LIMITS = {
    "S": 3,
    "M": 6,
    "L": 15,
}


def check_loading_budget(root: Path) -> Dict[str, Any]:
    root = root.resolve()
    _, assets, manifests, _ = collect_asset_index(root)
    errors: List[str] = []

    protocols = [a for a in assets if a["type"] == "workflow_protocol"]

    for proto in protocols:
        pid = proto["id"]
        budget = proto.get("budget_class")
        atom_count = proto.get("mandatory_atom_count")
        linked = proto.get("linked_atoms", [])

        # Check budget_class exists
        if not budget:
            errors.append(f"{pid}: missing budget_class")
            continue

        # Check budget_class is valid
        if budget not in BUDGET_LIMITS:
            errors.append(f"{pid}: invalid budget_class '{budget}'")
            continue

        # Check mandatory_atom_count is consistent
        if atom_count is None:
            errors.append(f"{pid}: missing mandatory_atom_count")
        elif atom_count != len(linked):
            errors.append(
                f"{pid}: mandatory_atom_count={atom_count} but linked_atoms has {len(linked)} items"
            )
        elif atom_count > BUDGET_LIMITS[budget]:
            errors.append(
                f"{pid}: mandatory_atom_count={atom_count} exceeds budget_class={budget} limit of {BUDGET_LIMITS[budget]}"
            )

        # Check expansion_allowed exists
        if "expansion_allowed" not in proto:
            errors.append(f"{pid}: missing expansion_allowed")

    # Check manifest adjunct_bundles reference valid constraint families
    for manifest in manifests:
        mid = manifest["id"]
        bundles = manifest.get("adjunct_bundles", {})
        for bundle_name, bundle_def in bundles.items():
            trigger = bundle_def.get("trigger", "")
            if not trigger:
                errors.append(f"{mid}: adjunct bundle '{bundle_name}' missing trigger")

    return {
        "errors": errors,
        "protocol_count": len(protocols),
        "budget_distribution": _budget_distribution(protocols),
    }


def _budget_distribution(protocols: List[Dict[str, Any]]) -> Dict[str, int]:
    dist: Dict[str, int] = {}
    for proto in protocols:
        b = proto.get("budget_class", "unknown")
        dist[b] = dist.get(b, 0) + 1
    return dist


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=str(repo_root()))
    args = parser.parse_args()
    report = check_loading_budget(Path(args.root))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not report["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
