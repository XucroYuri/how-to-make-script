from pathlib import Path
import unittest

from scripts.check_route_overlaps import check_route_overlaps


ROOT = Path(__file__).resolve().parents[1]


class CheckRouteOverlapsTest(unittest.TestCase):
    def test_routes_do_not_overlap(self) -> None:
        report = check_route_overlaps(ROOT)
        self.assertFalse(report["errors"], report["errors"])
        self.assertGreaterEqual(report["route_count"], 1)


if __name__ == "__main__":
    unittest.main()
