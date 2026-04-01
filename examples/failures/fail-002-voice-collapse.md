## Case: fail-002

**Protocol used:** wp.scene-writing
**Skill used:** skill.scene-writing
**What went wrong:** All characters in a multi-character scene used identical sentence rhythm and vocabulary. The elderly professor and the young hacker both spoke in clipped, analytical prose.
**Root cause:** The scene-writing protocol loaded conflict-pressure but exposition-control but did not include character-voice-consistency or embodied-text-pressure as mandatory atoms for multi-character scenes.
**Correction:** When `stage=scene` and output includes multiple speaking characters, scene-writing should auto-trigger the expression-lens adjunct bundle with character-voice-consistency.
**Status:** open
**Category:** voice_collapse
**Lesson:** Multi-character scene writing requires voice separation as a mandatory check, not an optional adjunct. The protocol's linked_atoms should expand when the scene has 2+ speaking roles.
