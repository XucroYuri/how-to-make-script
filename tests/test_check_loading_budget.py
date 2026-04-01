import unittest
from pathlib import Path
from scripts.check_loading_budget import check_loading_budget


class CheckLoadingBudgetTest(unittest.TestCase):
    def test_loading_budgets_declared(self):
        report = check_loading_budget(Path(__file__).resolve().parents[1])
        self.assertEqual(report["errors"], [])
        self.assertEqual(report["protocol_count"], 28)

        # Budget distribution should cover S, M, L
        dist = report["budget_distribution"]
        self.assertIn("S", dist)
        self.assertIn("M", dist)
        self.assertIn("L", dist)


if __name__ == "__main__":
    unittest.main()
