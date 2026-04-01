from pathlib import Path
import unittest

from scripts.run_fixture_suite import run_fixture_suite


ROOT = Path(__file__).resolve().parents[1]


class FixtureSuiteTest(unittest.TestCase):
    def test_fixture_suite_reports_expected_coverage(self) -> None:
        report = run_fixture_suite(ROOT)
        self.assertFalse(report["errors"], report["errors"])
        self.assertGreaterEqual(report["coverage"]["fixture_count"], 30)
        self.assertIn("feature_film", report["coverage"]["media"])
        self.assertIn("commercial", report["coverage"]["media"])
        self.assertIn("game_narrative", report["coverage"]["media"])


if __name__ == "__main__":
    unittest.main()

