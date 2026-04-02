from pathlib import Path
import unittest

from scripts.check_canonical_terms import check_canonical_terms


ROOT = Path(__file__).resolve().parents[1]


class CheckCanonicalTermsTest(unittest.TestCase):
    def test_forbidden_terms_do_not_reappear_on_public_surfaces(self) -> None:
        report = check_canonical_terms(ROOT)
        self.assertEqual(report["errors"], [], msg="\n".join(report["errors"]))


if __name__ == "__main__":
    unittest.main()
