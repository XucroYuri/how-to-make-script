from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Set
import sys

if __package__ in (None, ""):
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.lib import load_json, repo_root


def iter_surface_files(root: Path, patterns: Iterable[str], excludes: Iterable[str]) -> Iterable[Path]:
    excluded: Set[Path] = set()
    for pattern in excludes:
        excluded.update(path.resolve() for path in root.glob(pattern) if path.is_file())

    seen: Set[Path] = set()
    for pattern in patterns:
        for path in root.glob(pattern):
            if not path.is_file():
                continue
            resolved = path.resolve()
            if resolved in excluded or resolved in seen:
                continue
            seen.add(resolved)
            yield path


def check_canonical_terms(root: Path) -> Dict[str, Any]:
    root = root.resolve()
    register = load_json(root / "references" / "canonical-term-register.json")
    rules = register.get("forbidden_terms", [])

    errors: List[str] = []
    scanned_files = 0

    for path in iter_surface_files(
        root,
        register.get("scan_globs", []),
        register.get("exclude_globs", []),
    ):
        text = path.read_text(encoding="utf-8")
        scanned_files += 1
        rel = path.resolve().relative_to(root).as_posix()
        lines = text.splitlines()
        for rule in rules:
            term = rule["term"]
            case_sensitive = rule.get("case_sensitive", True)
            reason = rule.get("reason", "forbidden canonical drift term")
            needle = term if case_sensitive else term.lower()
            for lineno, line in enumerate(lines, start=1):
                hay = line if case_sensitive else line.lower()
                if needle in hay:
                    errors.append(f"{rel}:{lineno}: forbidden term {term!r} ({reason})")

    return {
        "errors": sorted(errors),
        "summary": {
            "scanned_files": scanned_files,
            "rule_count": len(rules)
        }
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=str(repo_root()))
    args = parser.parse_args()
    report = check_canonical_terms(Path(args.root))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not report["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
