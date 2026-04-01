# Subagent Library Architecture

This repository now has a dedicated subagent-library layer for screenplay work.

The design goal is not “more agents.” It is better specialization under bounded loading.

## Layer Order

The intended order is:

1. `route`
2. `team mode`
3. `expert cast`
4. `dispatch topology`

That order matters.

If the system chooses cast or topology before route, it will overfit on organizational theater.
If it chooses team mode but never chooses a cast, collaboration stays too abstract.
If it chooses a cast but never defines dispatch, the system becomes a pile of specialists with no merge discipline.

## Three Kinds Of Subagents

### Functional

These own a screenplay craft problem.

Examples:
- premise pressure
- structure and engine
- character pressure
- scene execution
- dialogue and subtext
- brand message control
- branch/state logic
- visual story translation

### Process Node

These own a workflow position rather than a craft niche.

Examples:
- divergence
- counterexample retention
- rewrite triage
- convergence
- review
- table-read synthesis

### Reference Persona

These are bounded decision lenses inspired by real creators, studios, or public craft lineages.

They are useful when the work needs extra pressure from a recognizable school of practice:
- prestige moral collision
- romantic verbal precision
- animation humanist visuality
- high-concept clockwork
- social satire thriller
- luxury restraint brand film
- systemic choice design

They are not final authority.

## Persona Governance

The repo uses three levels:

- `inspired_by`
  Borrow workflow shape, craft pressure, or evaluative bias.
- `calibrated_reference`
  Allow tighter pressure on decisions or expression, but with explicit loading caps and blocked-use rules.
- `forbidden_roleplay`
  Never dispatch as a live persona. This covers direct impersonation, quote-like continuation, or identity claims the repo should not make.

The governing principle is:

- borrow decision style;
- do not pretend authorship;
- do not let persona override protocol, rubric, or hard boundary.

## Dispatch Topology Layer

The repo now treats topology as its own machine-readable layer.

Typical topologies:
- `orchestrator_specialist_ring`
- `writers_room_tree`
- `debate_then_merge_board`
- `dual_track_story_visual`
- `variant_strike_grid`
- `branch_state_triangle`
- `fresh_task_review_loop`

`fresh_task_review_loop` is the direct integration point with the subagent-driven-development idea:
- one implementer or lane owner;
- one spec reviewer;
- one quality reviewer;
- one convergence owner or final reviewer.

This is useful for repo asset development and for screenplay tasks where “solve the wrong problem beautifully” is a real risk.

## Scaling Rule

The library should grow by composition, not by one-off special snowflakes.

That means:
- keep the top-level router stable;
- attach new archetypes under the cast layer;
- attach new scheduling shapes under the topology layer;
- reserve new outputs for genuinely new contracts, not new vibes.

## What A Good Run Looks Like

For a hard screenplay task, the repo should be able to answer:

- which mode this resembles;
- which cast is minimally necessary;
- which persona lenses are worth loading;
- which topology should run;
- who merges;
- what packet flows between lanes;
- where a human should intervene;
- how the system shrinks again when complexity stops paying off.

## Key Files

- [`references/expert-subagent-library.json`](../references/expert-subagent-library.json)
- [`references/subagent-topology-matrix.json`](../references/subagent-topology-matrix.json)
- [`references/team-mode-matrix.json`](../references/team-mode-matrix.json)
- [`references/agent-team-roles.json`](../references/agent-team-roles.json)
- [`knowledge/20-workflows/wp-expert-subagent-cast.md`](../knowledge/20-workflows/wp-expert-subagent-cast.md)
- [`knowledge/20-workflows/wp-subagent-dispatch-plan.md`](../knowledge/20-workflows/wp-subagent-dispatch-plan.md)
