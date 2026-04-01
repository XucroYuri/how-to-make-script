from pathlib import Path
import unittest

from scripts.check_routes import check_routes


ROOT = Path(__file__).resolve().parents[1]


class CheckRoutesTest(unittest.TestCase):
    def test_fixtures_resolve_to_expected_routes(self) -> None:
        report = check_routes(ROOT)
        self.assertFalse(report["errors"], report["errors"])
        self.assertGreaterEqual(report["fixture_count"], 30)


if __name__ == "__main__":
    unittest.main()

