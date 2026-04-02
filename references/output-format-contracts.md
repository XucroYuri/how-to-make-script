# Output Format Contracts

This file defines the repository's minimum Markdown delivery contract for golden screenplay artifacts.

It is not a claim that one screenplay format is universally correct.
It is a repository-level handoff rule so examples, routes, reviews, and regression checks all point at the same surface.

Use this together with:
- [`references/supported-outputs.md`](./supported-outputs.md) for public output names;
- route `output` fields in `examples/golden/*/route.json` for the chosen contract;
- [`references/output-format-contracts.json`](./output-format-contracts.json) for machine-checked enforcement.

## Machine-Checked Contracts

### `beat_sheet`
- Title: H1 should include `Beat Sheet`.
- Required H2 sections:
  - `Story Engine`
  - `Beat List`
- Each required section must expose list items, not just one loose paragraph.

### `commercial_script`
- Title: H1 should include `Commercial Script`.
- Required H2 sections:
  - `Core Message`
  - `Shot Flow`
  - `CTA`
- The document must make message, execution flow, and action prompt independently visible.

### `interactive_branch_map`
- Title: H1 should include `Interactive Branch Map`.
- Required H2 sections:
  - `Player Goal`
  - `State Variables`
  - `Branches`
  - `Convergence Plan`
- The document must expose player objective, tracked state, branch-level differences, and how the structure closes.

### `scene_draft`
- Title: H1 should include `Scene Draft`.
- Required H2 sections:
  - `Scene Objective`
  - `Script Blocks`
- `Script Blocks` is machine-checked as a labeled screenplay stream.
- Each scene must declare `Scene`, `Purpose`, and at least one `Action`.
- Dialogue beats must not be bare. Each beat needs either inline `Performance:` / `Action:` guidance or an adjacent preceding `Action:` line.
- `VFX` / `SFX` / `BGM` are optional, but if used they must appear as fixed labels, not freeform prose.

### `screenplay_draft`
- Title: H1 should include `Screenplay Draft`.
- Required H2 sections:
  - `Story Engine`
  - `Script Blocks`
- `Script Blocks` is machine-checked as a multi-scene labeled screenplay stream.
- The artifact must contain at least two scenes and enough dialogue beats to prove it is a playable page-level draft.
- Each scene must declare `Scene`, `Purpose`, and at least one `Action`.
- Dialogue beats must not be bare. Each beat needs either inline `Performance:` / `Action:` guidance or an adjacent preceding `Action:` line.
- `VFX` / `SFX` / `BGM` are optional, but if used they must appear as fixed labels, not freeform prose.

## Scope Note

These contracts currently cover the repository's golden example outputs.
They can expand to more outputs later, but new format rules should stay minimal and contract-first:
- expose the artifact's decision surface;
- avoid turning one good sample into dogma;
- prefer a small stable structure over a verbose template.
