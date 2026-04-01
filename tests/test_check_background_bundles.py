from pathlib import Path
import unittest

from scripts.check_background_bundles import check_background_bundles


ROOT = Path(__file__).resolve().parents[1]


class CheckBackgroundBundlesTest(unittest.TestCase):
    def test_background_bundles_validate(self) -> None:
        report = check_background_bundles(ROOT)
        self.assertFalse(report["errors"], report["errors"])
        self.assertGreaterEqual(report["bundle_count"], 1)


if __name__ == "__main__":
    unittest.main()
