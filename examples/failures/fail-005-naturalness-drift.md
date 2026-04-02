## Case: fail-005

**Protocol used:** wp.scene-writing
**Skill used:** skill.scene-writing
**Failure category:** cross_artifact_naturalness_drift

**What went wrong:**
The premise and outline were relatively natural, but once the project reached scene drafting the prose slid back into emotion labels, balanced explanation bridges, and samey sentence rhythm. The downstream dialogue polish had to spend its effort undoing upstream contamination instead of sharpening subtext.

**Root cause:**
Naturalness checks existed as expression-lens guidance, but the core scene-writing path did not treat Chinese mechanical-language patterns as a real stop condition.

**Correction:**
Promote the Chinese mechanical-language rules into hard fails for core scene and screenplay drafts, and require a handoff self-check before the artifact moves downstream.

**Status:** addressed

**Lesson:**
Naturalness drift is a pipeline problem, not just a final-pass polish problem.
