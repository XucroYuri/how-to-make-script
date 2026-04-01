import unittest
from pathlib import Path
from scripts.check_nl_routing import check_nl_routing


class CheckNLRoutingTest(unittest.TestCase):
    def test_nl_routing_bench_validates(self):
        report = check_nl_routing(Path(__file__).resolve().parents[1])
        self.assertEqual(
            report["errors"],
            [],
            f"NL routing bench validation failed: {report['errors']}",
        )

    def test_nl_routing_bench_has_minimum_coverage(self):
        report = check_nl_routing(Path(__file__).resolve().parents[1])
        coverage = report["coverage"]
        self.assertGreaterEqual(
            coverage["entry_count"],
            20,
            "NL routing bench should have at least 20 entries",
        )
        self.assertIn(
            "should_ask_clarification",
            coverage["behaviors"],
            "Bench must include ambiguity cases",
        )
        self.assertGreaterEqual(
            coverage["behaviors"]["should_ask_clarification"],
            3,
            "Bench should have at least 3 clarification cases",
        )


if __name__ == "__main__":
    unittest.main()
