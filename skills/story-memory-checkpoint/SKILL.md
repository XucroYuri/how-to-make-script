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

## References
- `wp.story-memory-checkpoint`
- `ka.story-memory-checkpoint`
- `ka.dual-track-rhythm`
- `ka.serial-arc-budgeting`
- `ka.room-artifact-ladder`
- `rb.story-memory-checkpoint`
