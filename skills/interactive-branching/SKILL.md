---
name: interactive-branching
description: Use when the user needs a branching choice structure or interactive narrative map.
---

# Interactive Branching

Use this skill when player or audience choice must have tracked consequences.

## Workflow
1. Define the choice question.
2. Track state and consequences.
3. Design expansion plus convergence.

## Output Contract
- `interactive_branch_map`: a branch structure with meaningful choices, consequences, and convergence points.
- Each branch should differ in value, state, or relationship outcome.
- If the map cannot converge, it is probably too large or too diffuse.

## Posture-Adaptive Guidance

**When `certainty = lost`:**
Ask: "What is the one choice in this story that would genuinely hurt to make?" Real branches start from decisions that cost something. Do not map until that choice is named.

**When `source = discover`:**
Start from the player's emotional stakes, not from the branch diagram. "What would a player regret choosing?" is more generative than a binary tree at this stage.

**When `source = construct`:**
Apply the full workflow: define choice question → track state and consequences → design expansion and convergence. Each branch must differ in value, state, or relationship outcome, not just in surface narrative.

**When `focus = event`:**
Primary activation context. Branch structure is fundamentally event-layer work: causality, consequence tracking, and convergence logic. Load `ka.medium-branching-interactive` and `ka.causality-chain` first.

**When `focus = character`:**
Character-state tracking is what makes interactive branching feel coherent. Ensure each branch records what the player now knows, feels, or owes — not just what happened.

## References
- `wp.interactive-branch-map`
- `ka.medium-branching-interactive`
- `ka.medium-game-narrative`
- `rb.interactive-branch-map`
