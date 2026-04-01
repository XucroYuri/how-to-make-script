from __future__ import annotations

from pathlib import Path
import unittest

from scripts.check_semantic_consistency import check_semantic_consistency


class CheckSemanticConsistencyTest(unittest.TestCase):
    def test_semantic_consistency_is_preserved(self) -> None:
        report = check_semantic_consistency(Path(__file__).resolve().parents[1])
        self.assertEqual(report["errors"], [], msg="\n".join(report["errors"]))
