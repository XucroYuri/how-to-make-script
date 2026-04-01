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
- `research_background_map`
- `path_options`
- `boundary_map`
- `scope_correction`
- `pattern_reference_pack`
- `context_loading_plan`
- `story_memory_checkpoint`
- `voice_style_guide`
- `visual_language_pack`
- `screen_to_video_brief`
- `team_workflow_blueprint`
- `expert_subagent_cast`
- `subagent_dispatch_plan`
- `project_surface_map`
- `quality_gate_report`

These contracts exist so agents can explicitly reason about audience demand, commissioning context, and writer capability growth, instead of burying those concerns in generic prose.
They also let the repo express plural routes, boundary logic, claim-narrowing behavior, contrastive reference teaching, and bounded loading control directly, instead of pretending every good answer collapses to one canonical artifact.
The newest expression contract makes voice, register, continuity, and "alive" text quality explicit without forcing all drafting requests through a style-template workflow.
The new visual-language contract makes cross-lingual shot vocabulary and culture-bound visual anchors explicit without forcing every screenplay request into multilingual mode.
The new screen-to-video bridge contract makes downstream visual translation explicit without confusing screenplay writing with vendor prompt syntax.
The new team contract makes multi-agent and human-agent screenplay collaboration explicit without pretending that one workflow fits every medium or production setting.
The new expert-cast contract makes it possible to select bounded specialist subagents and reference-persona lenses without turning every route into a bloated permanent team.
The new dispatch-plan contract makes scheduling, handoffs, review ordering, and context budgets explicit instead of leaving “orchestration” as invisible prompt lore.
The new project-surface contract makes canonical truth, runtime mirrors, packet assembly, review surfaces, and export surfaces explicit instead of leaving long-horizon project design to hidden repo habits.
The new quality-gate contract makes adaptive, lens-based self-checking explicit so the repo can audit text, bridges, governance artifacts, and recheck scopes without flattening everything into one rewrite note.
The new research-background contract makes broad screenplay theory, method-history, and background-support requests first-class instead of leaving them as loose documentation and loading heuristics.
The new story-memory-checkpoint contract makes resumable continuity compression explicit, so long-form writing can preserve state without defaulting to full-context reloads.

Registry-backed background bundles live in `references/` rather than `knowledge/`.
They are not a fifth core asset type; they are machine-checkable doc bundles that map broad research surfaces to callable atoms, outputs, and loading rules.

## Asset Rules
- Every asset has a stable `id`.
- Every linked `id` must resolve.
- Every protocol must name its rubrics and linked atoms.
- Every fixture must name its expected route.
- If an asset cannot be validated automatically, it should be split until it can.
- If an output depends on audience/industry/history/writer-development constraints, encode that dependency in the protocol and fixture constraints rather than ad-hoc prompt text.
- If a rule is not universal, encode its assumptions, boundary conditions, or rival routes instead of hiding the limitation in prose.
- If a challenge weakens a claim without killing its core, prefer a scope correction over deleting the claim or flipping it into a new universal.
- If a reference sample is used for teaching, pair it with a failure contrast and a non-dogma note so the repo does not silently turn samples into templates.
- If a request is complex, decide how much surrounding context to load explicitly instead of silently widening the bundle.

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
It should also preserve productive disagreement by giving the repository places to store rival paths, deferred boundaries, and counterexample-driven corrections.

For the current reality-grounding layer, pair this file with:
- [`docs/reality-lenses.md`](./reality-lenses.md)
- [`docs/source-map-real-world.md`](./source-map-real-world.md)
- [`docs/epistemic-stance.md`](./epistemic-stance.md)
- [`docs/exploration-vs-review.md`](./exploration-vs-review.md)
- [`docs/scenario-atlas.md`](./scenario-atlas.md)
- [`docs/context-loading-policy.md`](./context-loading-policy.md)
- [`docs/semantic-governance.md`](./semantic-governance.md)
- [`docs/progressive-disclosure-policy.md`](./progressive-disclosure-policy.md)
- [`docs/private-reference-distillation-policy.md`](./private-reference-distillation-policy.md)
- [`docs/source-map-screenplay-methods.md`](./source-map-screenplay-methods.md)
- [`docs/how-to-create-a-screenplay-research.md`](./how-to-create-a-screenplay-research.md)
- [`docs/how-to-create-a-screenplay-research-zh.md`](./how-to-create-a-screenplay-research-zh.md)
- [`docs/source-map-screenplay-creation-research.md`](./source-map-screenplay-creation-research.md)
