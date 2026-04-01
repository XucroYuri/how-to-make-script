# Content Model

## Structured Markdown

Reusable knowledge lives in Markdown files with JSON frontmatter:

```markdown
---
{
  "id": "ka.story-goal",
  "type": "knowledge_atom",
  "title": "故事目标",
  "...": "..."
}
---
# Human-readable body
```

This keeps the files:
- readable in GitHub;
- easy for humans to edit;
- dependency-light for Python tooling.
- easy for agents to load selectively.

The JSON frontmatter is the machine contract. The Markdown body is the human explanation. Keep both aligned.

## Asset Types

### `knowledge_atom`
- Smallest reusable craft unit.
- Captures one theory, tactic, rule, failure mode, or decision heuristic.
- Should be specific enough to drive one decision, not a cluster of loosely related ideas.
- Should be narrow enough that loading it does not drag unrelated craft baggage into the answer.

### `workflow_protocol`
- A stable creative workflow contract.
- Defines how multiple atoms are composed for a target output.
- Should answer: what comes in, what comes out, what steps happen, and when to stop.
- It is the main driver of agent behavior once a route is selected.

### `evaluation_rubric`
- Converts qualitative taste into review dimensions and hard-fail rules.
- Should make rewrite decisions concrete instead of vague.
- It should be usable directly at answer time as a compact self-check.

### `example_fixture`
- Encodes example requests and expected routes for regression checks.
- Should exercise route selection, not just content generation.
- It should represent plausible user requests, not schema-only toy data.

Real-world grounding outputs are first-class contracts:
- `audience_fit_note`
- `development_brief`
- `learning_path`

These contracts exist so agents can explicitly reason about audience demand, commissioning context, and writer capability growth, instead of burying those concerns in generic prose.

## Asset Rules
- Every asset has a stable `id`.
- Every linked `id` must resolve.
- Every protocol must name its rubrics and linked atoms.
- Every fixture must name its expected route.
- If an asset cannot be validated automatically, it should be split until it can.
- If an output depends on audience/industry/history/writer-development constraints, encode that dependency in the protocol and fixture constraints rather than ad-hoc prompt text.

## Question Backlog

Before creating new assets, check the Socratic backlog first:
- [`docs/socratic-question-backlog-en.md`](./socratic-question-backlog-en.md) for agent-facing intake;
- [`docs/socratic-question-backlog.md`](./socratic-question-backlog.md) for practitioner-facing intake.

The backlog is a discovery layer, not a source-of-truth layer. Its job is to turn gaps into one of four concrete outcomes:
- a new atom;
- a new protocol;
- a new rubric;
- a new fixture or case note.

The content model is therefore optimized for bounded loading, route stability, and repeatable output behavior, not for one-shot repository summarization.

For the current reality-grounding layer, pair this file with:
- [`docs/reality-lenses.md`](./reality-lenses.md)
- [`docs/source-map-real-world.md`](./source-map-real-world.md)
