# Team Collaboration Taxonomy

`team collaboration taxonomy` is the repository layer for screenplay work that is too large, too risky, or too cross-functional for a single undifferentiated agent or writer pass.

It exists because real screenplay development is rarely one person thinking in a vacuum. Feature development, TV rooms, animation story departments, branded-content studios, and interactive narrative teams all divide work differently. The repository therefore needs a way to describe collaboration patterns explicitly instead of pretending every request should be answered by one generic “writer agent.”

## Why This Layer Exists

The same screenplay problem can require very different social and agent structures:

- a feature rewrite may need a tight producer-director-writer chain;
- a TV season engine may need a showrunner-led room;
- an animation story problem may need iterative storyboard and visual feedback;
- a brand film may need creative plus strategy plus distribution alignment;
- a branching narrative may need narrative, systems, and QA loops.

If those modes are flattened into one route, the agent can still generate text, but it cannot mirror the real structure of work.

## Core Terms

- `team_mode`: the reusable operating model for the job.
- `coordination_model`: how work moves between roles, for example supervisor tree, swarm, handoff chain, or review board.
- `parallelism_budget`: how many lanes can move at once before synthesis becomes noisy.
- `human_gate_level`: how much human approval is required before the workflow can move forward.
- `artifact_chain`: the ordered deliverables the team is responsible for producing and reviewing.
- `handoff_packet`: the bounded state that one role passes to the next instead of dumping all context.

## Default Team Modes

- `feature_dev_pod`
- `showrunner_room`
- `animation_story_trust`
- `brand_content_studio`
- `interactive_branch_lab`
- `franchise_continuity_board`

These are not the only valid modes. They are the first set of reusable operating models the repository will recognize explicitly.

## Design Rules

1. Keep the root skill as orchestrator, not as the entire team.
2. Use specialist roles only when they change the quality of the next decision.
3. Keep handoffs bounded; do not share the whole repo with every role.
4. Separate exploration lanes from review gates.
5. Put humans at the high-risk or high-ambiguity gates, not everywhere.
6. Preserve multiple valid team modes when real-world practice differs by medium or company.

## What This Layer Should Prevent

- turning every screenplay request into one overstuffed super-agent workflow;
- using the same collaboration pattern for feature, TV, brand, animation, and interactive work;
- treating all specialist output as equal when some steps should remain review-gated;
- passing raw context dumps instead of structured handoff packets;
- confusing “parallel” with “everyone reads everything.”

## Relation To Other Layers

- `00-ontology` owns the collaboration vocabulary.
- `10-foundations` owns reusable multi-agent principles and mode summaries.
- `20-workflows` owns executable collaboration blueprints, concrete subagent casts, and dispatch plans.
- `60-rubrics` owns team-workflow quality checks.
- `references/` owns the machine-readable team-mode, cast, and topology registries.

The team layer answers the collaboration family.
The subagent layer answers the concrete roster and dispatch structure.

## TODOs: Questions To Keep Open

- [ ] Which current screenplay workflows still need their own first-class team mode?
- [ ] Should future versions distinguish human-only, agent-only, and human-agent hybrid rooms as separate topologies?
- [ ] Which collaboration failures should become regression fixtures rather than staying only in docs?
- [ ] When should a complex task use one team mode versus a hybrid of two modes?
- [ ] Which team modes need separate variants for indie, studio, and platform-first development?
