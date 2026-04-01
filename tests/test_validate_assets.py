from pathlib import Path
import unittest

from scripts.validate_assets import validate_repository


ROOT = Path(__file__).resolve().parents[1]


class ValidateAssetsTest(unittest.TestCase):
    def test_repository_assets_validate(self) -> None:
        report = validate_repository(ROOT)
        self.assertFalse(report["errors"], report["errors"])
        self.assertGreaterEqual(report["counts"]["knowledge_atom"], 20)
        self.assertGreaterEqual(report["counts"]["workflow_protocol"], 9)
        self.assertGreaterEqual(report["counts"]["evaluation_rubric"], 6)
        self.assertGreaterEqual(report["counts"]["skill_manifest"], 10)


if __name__ == "__main__":
    unittest.main()

