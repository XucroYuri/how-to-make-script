---
name: story-memory-checkpoint
description: 剧本项目需要可恢复的连续性压缩或交接安全状态（而非全量上下文重载）时使用。
---

# Story Memory Checkpoint

Use this skill when the user needs to pause and resume a long screenplay project, hand current story state to another agent or human, or preserve continuity without reloading a whole draft or room archive.

### When to Auto-Suggest a Checkpoint

Agent should proactively suggest a checkpoint at E2E stage transitions between these stages:

- `idea` → `premise`（story engine about to be committed）
- `premise` → `character`（character continuity needs locking before world-building）
- `character` → `structure`（story engine may shift when plot form takes over）
- `structure` → `scene`（character and event continuity must be locked before writing pages）
- Any pause or handoff in a multi-step pipeline

Do not auto-suggest checkpoints for single-step requests or trivial continuations. A checkpoint is warranted when losing state would cost meaningful re-work.

### What a Minimal Checkpoint Contains

A minimal `story_memory_checkpoint` must include:

1. **Current stage**: which stage the project is at（idea / premise / character / structure / scene / dialogue / polish）
2. **Locked decisions**: what has been committed and should not be reopened without explicit intent
3. **Open questions**: what is unresolved and must be carried forward as pending debt
4. **Next planned step**: which stage comes next, with the entry surface（e.g., "beat sheet → scene draft for Act II opening"）

For serial or long-form work, also include arc-budget spend and remaining high-value turns.

### How to Resume from a Checkpoint

When reloading from a checkpoint:

- Load only the state fields needed for the next step — do not reload the full project context.
- Begin by confirming the locked decisions are still valid（e.g., "We left off with the protagonist as a retired firefighter, goal: reclaim reputation, obstacle: official cover-up. Does this still hold?"）
- Surface any open questions that the next step must resolve before proceeding.
- If the checkpoint is stale（e.g., user provides new information that contradicts a locked decision）, flag the conflict before resuming.

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
- `rb.story-memory-checkpoint`
- `ka.cross-protocol-referral-edges`
- `ka.dual-track-rhythm`
- `ka.room-artifact-ladder`
- `ka.script-as-coordination-artifact`
- `ka.serial-arc-budgeting`
- `ka.story-memory-checkpoint`
