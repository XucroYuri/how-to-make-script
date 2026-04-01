from pathlib import Path
import unittest

from scripts.check_subagent_registries import validate_subagent_registries


ROOT = Path(__file__).resolve().parents[1]


class CheckSubagentRegistriesTest(unittest.TestCase):
    def test_subagent_registries_validate(self) -> None:
        report = validate_subagent_registries(ROOT)
        self.assertFalse(report["errors"], report["errors"])
        self.assertGreaterEqual(report["counts"]["archetype_count"], 20)
        self.assertGreaterEqual(report["counts"]["cast_template_count"], 5)
        self.assertGreaterEqual(report["counts"]["topology_count"], 5)


if __name__ == "__main__":
    unittest.main()
