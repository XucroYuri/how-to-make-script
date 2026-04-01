from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List

if __package__ in (None, ""):
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.lib import repo_root


FORBIDDEN_PATTERNS = [
    ".obsidian/",
    ".omx/",
    ".codex/",
    ".claude/",
    ".claude-code/",
    ".opencode/",
    ".openclaw/",
    ".gemini/",
    ".gemini-cli/",
    ".aider/",
    ".cursor/",
    ".continue/",
    ".roo/",
    ".windsurf/",
    ".avante/",
]


def git_lines(root: Path, *args: str) -> List[str]:
    cmd = ["git", *args]
    result = subprocess.run(
        cmd,
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return []
    return [line for line in result.stdout.splitlines() if line.strip()]


def check_forbidden_paths(root: Path) -> Dict[str, Any]:
    root = root.resolve()
    errors: List[str] = []
    warnings: List[str] = []

    tracked_files = git_lines(root, "ls-files")
    for file_path in tracked_files:
        normalized = file_path.replace("\\", "/")
        for pattern in FORBIDDEN_PATTERNS:
            if normalized == pattern.rstrip("/") or normalized.startswith(pattern):
                errors.append(f"tracked forbidden path: {normalized}")

    if (root / ".git").exists():
        for pattern in FORBIDDEN_PATTERNS:
            history_refs = git_lines(root, "rev-list", "--all", "--", pattern.rstrip("/"))
            if history_refs:
                errors.append(
                    f"history contains forbidden path {pattern} in {len(history_refs)} commit(s)"
                )

    ignored = git_lines(root, "status", "--short", "--ignored")
    ignored_paths = [line[3:].strip().replace("\\", "/") for line in ignored if line.startswith("!! ")]
    for pattern in FORBIDDEN_PATTERNS:
        prefix = pattern.rstrip("/")
        if any(path == prefix or path.startswith(pattern) for path in ignored_paths):
            warnings.append(f"{pattern} is present locally but ignored, which is expected")

    return {
        "errors": errors,
        "warnings": warnings,
        "forbidden_patterns": FORBIDDEN_PATTERNS,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=str(repo_root()))
    args = parser.parse_args()
    report = check_forbidden_paths(Path(args.root))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not report["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
