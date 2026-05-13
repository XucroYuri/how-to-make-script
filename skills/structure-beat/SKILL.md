---
name: structure-beat
description: 需要节拍表、序列或完整大纲时使用。
---

# Structure Beat

Use this skill to expand a premise into a causally connected outline.

## Workflow
1. Choose the structure family that matches the project's actual engine.
2. Choose the beat carrier that best exposes that engine.
3. For serial containers, lock arc budget before distributing major turns.
4. Map turning points, escalation, and dual-track rhythm.
5. Check cause-and-effect links.
6. Output beat sheet, outline, or treatment at the requested depth.

## Output Contract
- `beat_sheet`: a turning-point sequence with escalation.
- `outline`: an ordered sequence of scenes or sequences.
- `treatment`: a prose expansion that still preserves causal structure.
- Do not output filler beats that do not change pressure, knowledge, or choice.
- For episodic or serial work, do not spend reveal and relationship turns before the container and arc budget are clear.

## Posture-Adaptive Guidance

**When `certainty = lost`:**
Ask: "What is the one event in this story that everything else is building toward — even if you can't get there yet?" One fixed endpoint is enough to start a beat sheet from. Do not ask for a full structure family selection.

**When `source = discover`:**
Start from the feeling of the story's shape, not from a structure template. "Does this feel like it tightens like a vice, or like it builds to an avalanche, or like it slowly collapses inward?" Let the intuited shape select the structure family.

**When `source = construct`:**
Apply the full workflow: structure family → beat carrier → arc budget → turning points → escalation → dual-track rhythm → cause-and-effect check. For serial containers, arc budget precedes beat distribution.

**When `source = generate`:**
Give the premise a single collision event and write the beats that feel necessary without planning. Use the result to reveal the structure family that the story is trying to be.

**When `focus = event`:**
Primary activation context. Load `ka.causality-chain`, `ka.structure-family-selection`, and `ka.beat-carrier-selection` first. Every beat must change at least one of: pressure, knowledge, relationship, or choice availability.

**When `focus = character`:**
Structure serves character transformation. Ask at each major beat: "What has this character been forced to understand about themselves that they could not deny a beat earlier?"

## References
- `wp.structure-beat-outline`
- `rb.outline`
- `ka.beat-carrier-selection`
- `ka.causality-chain`
- `ka.cross-protocol-referral-edges`
- `ka.dual-track-rhythm`
- `ka.medium-episode`
- `ka.medium-feature-film`
- `ka.medium-short-drama`
- `ka.medium-animation`
- `ka.medium-documentary`
- `ka.pacing-rhythm`
- `ka.serial-arc-budgeting`
- `ka.story-goal`
- `ka.structure-family-selection`
