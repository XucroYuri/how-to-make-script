# Scenario Taxonomy

`scenario taxonomy` is the repository layer for classifying screenplay creation situations.

It is not a genre list and not a canon. It is a factorization map. The goal is to let agents and humans describe a request as a bundle of signals instead of flattening it into a single label like "film", "TV", or "commercial".

## Why This Layer Exists

Screenplay work changes shape across medium, format pressure, audience need state, narrative engine, emotional contract, production context, participation mode, business goal, source relation, collaboration mode, and risk profile.

If these are collapsed into one broad category, the repo becomes easy to read and hard to use. If they are separated too aggressively, the repo becomes precise but brittle. The scenario layer tries to keep both readability and routeability.

## Core Axes

- `medium`: the container the script must serve.
- `format_pressure`: the shape of the deliverable.
- `audience_need_state`: what the audience is trying to get from the work.
- `narrative_engine`: what keeps the story moving.
- `emotional_contract`: what feeling the work promises.
- `production_context`: what industrial condition is shaping the request.
- `participation_mode`: whether the audience is passive, branching, or stateful.
- `business_goal`: what the work is supposed to achieve for the project.
- `genre_pressure`: which genre promise is most active.
- `source_relation`: how closely the work is tied to existing source material.
- `collaboration_mode`: how the work is being developed socially.
- `risk_profile`: how constrained or sensitive the scenario is.

These axes are orthogonal lenses, not a checklist of mandatory truths. A real request may use only a few of them. Another request may need most of them.

## How To Factorize A Scenario

1. Identify the dominant container first.
2. Add the smallest set of axes that changes the route or the evaluation.
3. Keep multiple plausible routes visible if the brief is still genuinely open.
4. Treat genre as one lens among many, not as the master key.
5. If a request mixes creative exploration with review, separate the phases before you collapse the scenario.
6. If a challenged rule still has a surviving core, let scope correction narrow it rather than replacing it with a mirror universal.

## Scenario Card Families

The registry in [`references/scenario-taxonomy.json`](../../references/scenario-taxonomy.json) is the machine-readable version of this layer.
The atlas docs in [`docs/scenario-atlas.md`](../../docs/scenario-atlas.md) and [`docs/scenario-atlas-zh.md`](../../docs/scenario-atlas-zh.md) turn the same layer into practical reading.

Typical families include:

- original feature-film concept development
- episodic pilot and recurring engine design
- procedural case-of-the-week construction
- short-drama hook density work
- animation world-rule storytelling
- thriller reveal-chain design
- romance recognition and payoff design
- comedy setup-payoff design
- prestige ambiguity handling
- commercial single-message conversion
- branded film identity storytelling
- shortform social hook design
- game narrative quest-loop design
- branching interactive consequence design
- adaptation translation across containers
- rewrite diagnosis and script doctoring
- dialogue voice and subtext passes
- team workflow architecture
- audience fit analysis
- development brief construction
- writer learning path design
- path options divergence work
- boundary mapping
- scope correction

## What This Layer Should Prevent

- treating one medium as the default answer for every brief;
- treating one genre theory as a universal screenplay truth;
- confusing a strong example with a universal law;
- hiding hard boundaries inside soft taste language;
- collapsing hybrid requests too early;
- making review constraints operate as if they were exploration rules.

## Relation To Other Layers

- `00-ontology` owns the classification map.
- `10-foundations` owns reusable factorization principles.
- `20-workflows` owns routes that act on a scenario classification.
- `60-rubrics` owns quality checks for the outputs those routes produce.

The scenario taxonomy is therefore a bridge layer. It helps the repo say what kind of problem it is looking at before it decides what kind of answer to generate.

## TODOs: Questions To Keep Open

- [ ] Which additional scenario families still need their own reference cards?
- [ ] Are there requests that should be classified primarily by business goal rather than by medium?
- [ ] Which mixed scenarios are common enough to deserve their own first-class family?
- [ ] When should a scenario split into two cards instead of being described by one hybrid signature?
- [ ] Which scenario families should be attached to future case studies first?
