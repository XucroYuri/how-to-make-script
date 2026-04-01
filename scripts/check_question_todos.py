from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List

if __package__ in (None, ""):
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.lib import repo_root


CHECKBOX_RE = re.compile(r"^- \[ \] .+", re.MULTILINE)
QUESTION_DOC_PATTERNS = (
    "docs/socratic-question-backlog*.md",
    "docs/socratic-question-layer*.md",
)
TODO_SECTION_RE = re.compile(r"^## .*TODO", re.MULTILINE)


def check_question_todos(root: Path) -> Dict[str, Any]:
    root = root.resolve()
    errors: List[str] = []
    checked_sources: List[str] = []
    checked_question_count = 0
    knowledge_file_count = 0
    backlog_doc_count = 0

    for path in sorted((root / "knowledge").rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        checked_sources.append(str(path.relative_to(root)))
        knowledge_file_count += 1
        if not TODO_SECTION_RE.search(text):
            errors.append(f"{path.relative_to(root)}: missing TODO question section")
            continue
        checkboxes = CHECKBOX_RE.findall(text)
        if len(checkboxes) < 3:
            errors.append(f"{path.relative_to(root)}: fewer than 3 TODO checkbox questions")
        checked_question_count += len(checkboxes)

    docs_dir = root / "docs"
    candidate_paths: List[Path] = []
    for pattern in QUESTION_DOC_PATTERNS:
        candidate_paths.extend(sorted(docs_dir.glob(Path(pattern).name)))

    for path in sorted(set(candidate_paths)):
        text = path.read_text(encoding="utf-8")
        checked_sources.append(str(path.relative_to(root)))
        backlog_doc_count += 1
        checkboxes = CHECKBOX_RE.findall(text)
        if len(checkboxes) < 3:
            errors.append(f"{path.relative_to(root)}: fewer than 3 TODO checkbox questions")
        checked_question_count += len(checkboxes)

    return {
        "errors": errors,
        "knowledge_file_count": knowledge_file_count,
        "backlog_doc_count": backlog_doc_count,
        "checked_source_count": len(checked_sources),
        "question_count": checked_question_count,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=str(repo_root()))
    args = parser.parse_args()
    report = check_question_todos(Path(args.root))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not report["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
