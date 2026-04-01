from pathlib import Path
import unittest

from scripts.check_community_surfaces import check_community_surfaces


ROOT = Path(__file__).resolve().parents[1]


class CheckCommunitySurfacesTest(unittest.TestCase):
    def test_community_surfaces_are_wired(self) -> None:
        report = check_community_surfaces(ROOT)
        self.assertFalse(report["errors"], report["errors"])
        self.assertGreaterEqual(report["category_count"], 6)
        self.assertGreaterEqual(report["discussion_template_count"], 4)
        self.assertGreaterEqual(report["label_count"], 12)
        self.assertGreaterEqual(report["doc_count"], 5)


if __name__ == "__main__":
    unittest.main()
