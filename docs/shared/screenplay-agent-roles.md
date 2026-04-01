# Screenplay Agent Roles

This file defines a small default role set for screenplay-oriented multi-agent work.
These roles are not mandatory for every run. They are reusable building blocks for `team_workflow_blueprint`.

For the larger expert-subagent system, treat this file as the default base layer.
The extended library lives in:
- [`references/agent-team-roles.json`](../../references/agent-team-roles.json)
- [`references/expert-subagent-library.json`](../../references/expert-subagent-library.json)
- [`references/subagent-topology-matrix.json`](../../references/subagent-topology-matrix.json)

Use this file when you need a stable mental model fast.
Use the registries when you need a concrete cast or dispatch plan.

## Core Roles

- `showrunner_orchestrator`
  - Owns route stability, synthesis, review cadence, and final creative convergence.
  - Best for: episodic work, hybrid team workflows, high-risk rewrite or approval loops.

- `story_architect`
  - Owns premise, engine, structure, escalation, and rewrite logic at the macro level.
  - Best for: feature development, season engines, adaptation reframing.

- `character_voice_editor`
  - Owns role-specific voice anchors, continuity, register guardrails, and “alive” expression checks.
  - Best for: dialogue, adaptation, IP continuity, branded tone control.

- `scene_runner`
  - Owns scene cards, scene drafts, tactical escalation, and playable scene-level change.
  - Best for: scene-heavy drafting and local rewrite passes.

- `market_and_commissioning_strategist`
  - Owns audience fit, development brief logic, platform fit, and commissioning pressure.
  - Best for: feature development, branded content, platform-first television.

- `branch_system_designer`
  - Owns branch maps, state logic, replay structure, and interactive scope control.
  - Best for: game narrative and branching interactive work.

- `review_board`
  - Owns final approval, contradiction checks, boundary enforcement, and escalation to human review.
  - Best for: high-risk, high-cost, or externally constrained work.

## Role Rules

- Do not instantiate every role by default.
- Use a role only when it changes the next decision materially.
- Give each role a minimal bundle and bounded handoff packet.
- Keep final synthesis with one orchestrator or review board, not with every worker.

## Suggested Tier Mapping

- `LOW`
  - targeted lookups, fixture additions, one-file edits, narrow note generation
- `STANDARD`
  - story architect, scene runner, character voice editor, market strategist
- `THOROUGH`
  - showrunner orchestrator, review board, route-family redesign, hybrid team-mode planning

## Expansion Rule

- Base roles answer the question “who usually matters.”
- The expert library answers the question “which exact specialist or persona lens should enter now.”
- The topology matrix answers the question “how should they actually run.”
