---
name: rewrite-doctor
description: Use when the user needs a script doctor style diagnosis and rewrite priorities.
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

## References
- `wp.rewrite-doctor`
- `ka.rewrite-diagnosis`
- `ka.causality-chain`
- `ka.feedback-subjectivity-management`
- `rb.rewrite-report`
