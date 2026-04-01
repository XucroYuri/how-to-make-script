# Subagent Cast Reference Pack

This pack teaches cast design, not one canonical team.

Each example shows:
- the task pressure;
- a stronger cast;
- a weaker cast;
- why the stronger cast works better;
- why the weaker cast fails;
- a non-dogma note.

## Case 1: Prestige Feature Rewrite

### Problem

A feature film has a strong central premise but its second act is drifting. The user wants a multi-agent setup that can challenge structure, preserve character pressure, and avoid prestige fog.

### Stronger Cast

- `story_architect`
- `character_lead`
- `subagent.rewrite-triage-lead`
- `subagent.counterexample-keeper`
- `subagent.convergence-editor`
- optional lens: `persona.prestige-moral-collision`

### Weaker Cast

- `story_architect`
- `persona.prestige-moral-collision`
- `persona.poetic-observational-minimalism`
- `persona.high-concept-clockwork`

### Why The Stronger Cast Wins

- It separates diagnosis from taste pressure.
- It preserves one explicit merge owner.
- It keeps only one persona lens, so the work gets pressure without losing route clarity.
- It adds a counterexample node, which protects the rewrite from converging too fast on prestige-looking but weak fixes.

### Why The Weaker Cast Fails

- It is mostly a vibe council.
- No one owns rewrite triage.
- No one owns convergence.
- Three persona lenses start competing before the system even knows what is broken.

### Non-Dogma Note

If the draft is already structurally stable and only needs line pressure, this cast is too large. A smaller scene/dialogue pass plus one reviewer may be enough.

## Case 2: Luxury Brand Film

### Problem

A skincare brand film needs one message spine, strong premium restraint, and shortform cutdown potential.

### Stronger Cast

- `brand_platform_strategist`
- `scene_specialist`
- `subagent.brand-message-guardian`
- `subagent.variant-lane-operator`
- `subagent.convergence-editor`
- optional lens: `persona.luxury-restraint-brand-film`

### Weaker Cast

- `scene_specialist`
- `persona.luxury-restraint-brand-film`
- `persona.kinetic-pop-energy`
- `persona.romantic-verbal-precision`

### Why The Stronger Cast Wins

- The message owner and variant operator are both present, so the campaign can expand without losing the spine.
- The luxury persona acts only as tone pressure.
- The convergence editor prevents endless version drift.

### Why The Weaker Cast Fails

- It confuses aesthetic taste with strategy.
- No role is responsible for variant governance.
- The cast can generate stylish fragments, but not a disciplined campaign workflow.

### Non-Dogma Note

For a single one-off brand film with no cutdown plan, the variant lane may be unnecessary. Keep the brand guardian, drop the operator.

## Case 3: Branching Interactive Mystery

### Problem

The project needs meaningful player choice, clear state logic, and strong dialogue under interrogation pressure.

### Stronger Cast

- `interactive_systems_narrative`
- `continuity_keeper`
- `subagent.state-qa-architect`
- `subagent.counterexample-keeper`
- `subagent.convergence-editor`
- optional lens: `persona.branching-systemic-choice`

### Weaker Cast

- `story_architect`
- `subagent.dialogue-subtext-doctor`
- `persona.branching-systemic-choice`

### Why The Stronger Cast Wins

- It keeps state, continuity, and convergence visible as separate responsibilities.
- The persona lens pressures choice value, but does not replace systems work.
- The counterexample node helps catch fake branches and dead-state storytelling early.

### Why The Weaker Cast Fails

- It treats interactive design like linear dialogue plus a systems-flavored vibe.
- No one owns state verification.
- No one owns scope control.

### Non-Dogma Note

For a very small prototype, the full cast may be too heavy. In that case, keep `interactive_systems_narrative`, `subagent.state-qa-architect`, and one human decision owner.
