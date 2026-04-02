from pathlib import Path
import unittest

from scripts.check_golden_artifact_formats import (
    check_golden_artifact_formats,
    check_script_block_contract,
)


ROOT = Path(__file__).resolve().parents[1]


class GoldenArtifactFormatTest(unittest.TestCase):
    def test_golden_artifacts_match_output_format_contracts(self) -> None:
        report = check_golden_artifact_formats(ROOT)
        self.assertFalse(report["errors"], report["errors"])
        self.assertEqual(
            sorted(report["coverage"]["outputs"]),
            [
                "beat_sheet",
                "commercial_script",
                "interactive_branch_map",
                "scene_draft",
                "screenplay_draft",
            ],
        )
        self.assertEqual(
            sorted(report["coverage"]["examples"]),
            [
                "commercial-launch",
                "feature-drama",
                "feature-scene",
                "feature-screenplay",
                "interactive-quest",
            ],
        )

    def test_script_block_contract_rejects_bare_dialogue(self) -> None:
        contract = {
            "script_section": "Script Blocks",
            "min_scenes": 1,
            "min_dialogue_beats": 1,
            "scene_labels": ["Scene", "Purpose", "Action"],
            "av_labels": ["VFX", "SFX", "BGM"],
            "beat_requires_performance": True,
        }
        text = """# Sample Scene Draft

## Script Blocks
- Scene: INT. NEWSROOM - NIGHT
- Purpose: 编辑把林秋逼到无法继续回避旧案。
- Beat: 林秋 | Dialogue: 这案子，不归我。
- Action: 灯管轻轻嗡着，档案袋压在她手边。
"""

        errors = check_script_block_contract(
            text,
            contract,
            "examples/golden/feature-scene/artifact.md",
        )

        self.assertTrue(
            any("bare dialogue beat" in error for error in errors),
            errors,
        )

    def test_script_block_contract_rejects_unlabeled_av_notes(self) -> None:
        contract = {
            "script_section": "Script Blocks",
            "min_scenes": 1,
            "min_dialogue_beats": 1,
            "scene_labels": ["Scene", "Purpose", "Action"],
            "av_labels": ["VFX", "SFX", "BGM"],
            "beat_requires_performance": True,
        }
        text = """# Sample Scene Draft

## Script Blocks
- Scene: INT. NEWSROOM - NIGHT
- Purpose: 编辑把林秋逼到无法继续回避旧案。
- Action: 灯管轻轻嗡着，档案袋压在她手边。
- Music: 持续低频铺底。
- Beat: 林秋 | Performance: 盯着档案，不接编辑的眼神。 | Dialogue: 这案子，不归我。
"""

        errors = check_script_block_contract(
            text,
            contract,
            "examples/golden/feature-scene/artifact.md",
        )

        self.assertTrue(
            any("unknown script label 'Music'" in error for error in errors),
            errors,
        )


if __name__ == "__main__":
    unittest.main()
