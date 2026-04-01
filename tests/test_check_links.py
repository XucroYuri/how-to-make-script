from pathlib import Path
import unittest

from scripts.check_links import check_links


ROOT = Path(__file__).resolve().parents[1]


class CheckLinksTest(unittest.TestCase):
    def test_internal_markdown_links_resolve(self) -> None:
        report = check_links(ROOT)
        self.assertFalse(report["errors"], report["errors"])


if __name__ == "__main__":
    unittest.main()

