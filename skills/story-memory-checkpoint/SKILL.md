---
name: story-memory-checkpoint
description: Use when a screenplay project needs resumable continuity compression or handoff-safe state instead of full-context reload.
---

# Story Memory Checkpoint

Use this skill when the user needs to pause and resume a long screenplay project, hand current story state to another agent or human, or preserve continuity without reloading a whole draft or room archive.

## Workflow
1. Lock the covered span and the checkpoint purpose.
2. Compress current story state instead of retelling the plot.
3. Record unresolved promises, invariants, and canon-vs-hypothesis boundaries.
4. Separate external pressure rhythm from internal emotional or cognitive rhythm.
5. For serial work, note current arc-budget spend and remaining high-value turns.
6. Return a checkpoint with next safe entrypoint, priority source surfaces, and drift risks.

## Output Contract
- `story_memory_checkpoint`: current state, unresolved promises, invariants, dual-track rhythm, arc-budget status when relevant, next safe entrypoint, priority source surfaces, and drift warnings.
- Keep it short enough to replace a broad reload.
- Do not turn the checkpoint into a prose summary of the whole story.

## Posture-Adaptive Guidance

**When `certainty = lost`:**
Ask: "What is the last thing you were certain about in this story before you got lost?" One confirmed story truth is the right starting point for a checkpoint. Do not produce a full state compression — produce one anchor first.

**When `certainty = certain`:**
Apply the full checkpoint workflow: lock span → compress current state → record unresolved promises and invariants → separate dual-track rhythms → return with next safe entrypoint and drift warnings.

**When `focus = event`:**
Event-layer checkpoints should record: what has already been spent (turns, reveals, escalations) and what arc budget remains. Do not retell the plot; record the pressure-state.

**When `focus = character`:**
Character-layer checkpoints should record: active wants, outstanding lies, unresolved wounds, and open relationship debts. These are the continuity liabilities that cause drift in resumed work.

**When `focus = world`:**
World-layer checkpoints should record: which world rules have been explicitly established, which have been implied but not confirmed, and which remain unset and thus canonically open.

## References
- `wp.story-memory-checkpoint`
- `ka.story-memory-checkpoint`
- `ka.dual-track-rhythm`
- `ka.serial-arc-budgeting`
- `ka.room-artifact-ladder`
- `rb.story-memory-checkpoint`
