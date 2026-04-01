from pathlib import Path
import unittest

from scripts.generate_index import build_index


ROOT = Path(__file__).resolve().parents[1]


class GenerateIndexTest(unittest.TestCase):
    def test_index_contains_assets_and_skills(self) -> None:
        index = build_index(ROOT)
        self.assertIn("assets", index)
        self.assertIn("skills", index)
        self.assertGreaterEqual(len(index["assets"]["knowledge_atom"]), 20)
        self.assertGreaterEqual(len(index["skills"]), 10)


if __name__ == "__main__":
    unittest.main()

