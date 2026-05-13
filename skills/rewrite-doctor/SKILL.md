---
name: rewrite-doctor
description: 需要剧本医生式的诊断和改写优先级排序时使用。
---

# Rewrite Doctor

Use this skill when the request is diagnostic rather than generative and the main need is rewrite prioritization inside story/text layers.

## Workflow
1. Locate the failure layer.
2. Distinguish root causes from symptoms.
3. Return prioritized, actionable rewrite moves.

If the user instead needs a structured audit, preflight, acceptance gate, or recheck across non-story artifacts, prefer `quality_gate_report`.

## Output Contract
- A diagnosis that separates concept, structure, scene, and line-level problems.
- A ranked list of rewrite moves with the highest leverage first.
- A clear note when the sample is too small to support a strong diagnosis.

## Posture-Adaptive Guidance

**When `certainty = lost`:**
Ask: "Where does the draft feel most wrong to you — even if you can't explain why?" One felt location is enough to start. Do not ask for a complete description of all the problems. Let the writer's discomfort be the first diagnostic tool.

**When `source = discover`:**
Begin with the failure layer, not the fix. "This feels like a structure problem, not a dialogue problem" is more useful than a rewrite suggestion at this stage.

**When `source = construct`:**
Apply the full diagnostic workflow: locate failure layer → distinguish root causes from symptoms → return prioritised rewrite moves, highest leverage first.

**When `focus = character`:**
Most "dialogue problems" are character-psychology problems one layer up. Ask: "Is this character doing something in this scene that contradicts their established wound or want?" Fix the motivation first, then the lines.

**When `focus = event`:**
Most "scene problems" are causality problems one level up. Ask: "What should this scene force the next scene to become?" If the answer is "nothing in particular," the scene is not earning its place.

**When `focus = language`:**
Restrict diagnosis to line-level: rhythm, register, subtext, and voice separation. Do not drift into structure or character-arc notes unless they are directly causing the language failure.

## Cross-Layer Diagnosis

When a problem spans multiple layers（e.g., pacing affects both structure AND scene level）, do not force a single-layer diagnosis:

- **Acknowledge the cross-layer nature**. Name which layers are involved and how they interact. For example: "This pacing issue originates at the structure layer（Act II is 15 beats too long）but manifests at the scene layer（scenes 22-28 all run 30% longer than their dramatic weight justifies）."
- **Address both layers**. A structure problem that creates scene-level symptoms cannot be fixed by scene-level edits alone. Provide the structural fix AND the scene-level cleanup.
- **Prioritize the root cause first**. If the structure layer caused the scene layer to drift, fix the structure first. Surface the scene-level fixes as a second pass, not as the primary intervention.

### Pacing Rhythm Awareness

When diagnosing pacing problems, consider rhythm across both event and emotional tracks:

- Refer to `ka.pacing-rhythm` for beat-level tempo control — where to accelerate, where to breathe.
- Refer to `ka.dual-track-rhythm` for the interaction between external pressure rhythm（plot events）and internal rhythm（character emotional/psychological state）. Pacing failures often come from one track overwhelming the other, not from absolute speed.
- Ask: "Is this scene slow, or is it failing to alternate between external and internal rhythm?" A scene can feel slow even at high event density if the emotional rhythm is absent.

## References
- `wp.rewrite-doctor`
- `rb.rewrite-report`
- `ka.causality-chain`
- `ka.cross-protocol-referral-edges`
- `ka.dialogue-subtext`
- `ka.dual-track-rhythm`
- `ka.feedback-subjectivity-management`
- `ka.pacing-rhythm`
- `ka.rewrite-diagnosis`
- `ka.scene-function`
- `ka.setup-and-payoff`
- `ka.act-two-diagnosis`
- `ka.weak-opening-diagnosis`
