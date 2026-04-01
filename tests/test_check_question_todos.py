from pathlib import Path
import unittest

from scripts.check_question_todos import check_question_todos


ROOT = Path(__file__).resolve().parents[1]


class CheckQuestionTodosTest(unittest.TestCase):
    def test_all_knowledge_files_have_todo_question_sections(self) -> None:
        report = check_question_todos(ROOT)
        self.assertFalse(report["errors"], report["errors"])
        self.assertGreaterEqual(report["knowledge_file_count"], 40)
        self.assertGreaterEqual(report["backlog_doc_count"], 2)
        self.assertGreaterEqual(report["question_count"], 120)


if __name__ == "__main__":
    unittest.main()
