from pathlib import Path
import unittest

from scripts.check_forbidden_paths import check_forbidden_paths


ROOT = Path(__file__).resolve().parents[1]


class CheckForbiddenPathsTest(unittest.TestCase):
    def test_forbidden_paths_are_not_tracked_or_in_history(self) -> None:
        report = check_forbidden_paths(ROOT)
        self.assertFalse(report["errors"], report["errors"])
        self.assertIn(".obsidian/", report["forbidden_patterns"])


if __name__ == "__main__":
    unittest.main()

