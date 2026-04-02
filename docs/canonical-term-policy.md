# Canonical Term Policy

## Purpose

This repository needs terminology that stays readable for humans and stable for agents.

The rule is simple:
- one public concept should have one primary name;
- user-facing prose should read naturally in its target language;
- machine-facing IDs and contracts should not churn just because display wording improves.

This policy complements:
- [`docs/semantic-governance.md`](./semantic-governance.md)
- [`docs/bilingual-authoring.md`](./bilingual-authoring.md)
- [`references/canonical-term-register.json`](../references/canonical-term-register.json)

## Surface Tiers

### `L0` Contract Layer

Applies to IDs, schema fields, router outputs, manifest keys, fixture contract keys, and checker-facing names.

Rule:
- keep canonical IDs stable;
- do not add prose aliases inside machine-facing fields;
- do not rename a stable public contract unless the repository is intentionally migrating a public interface.

Examples:
- `voice_style_guide` stays the output ID.
- `expression_lens` can remain an internal English concept in code or registry names.

### `L1` Execution Layer

Applies to workflow protocols, rubrics, policies, supported-output docs, and execution-facing references.

Rule:
- use canonical display terms by default;
- allow one first-mention gloss when the English contract name matters;
- keep wording specific enough that an agent will not confuse adjacent concepts.

Example:
- `voice_style_guide` may appear as `voice_style_guide` in backticks, but nearby prose should use the canonical display name instead of inventing fresh synonyms.

### `L2` Reading Layer

Applies to README files, reference packs, examples, onboarding prose, and contributor-facing guides.

Rule:
- optimize for natural reading first;
- keep the underlying concept aligned with `L0`/`L1`;
- use a parenthetical gloss only when a reader would plausibly know the old term or the English internal name better than the new display term.

Example:
- Chinese prose should prefer `角色声音` over literal or technical wording.

### `L3` Historical Layer

Applies to roadmaps, review notes, and archive-style documents.

Rule:
- old wording may remain when the document is preserving historical context;
- if an obsolete term is still important to interpret the document, add a short mapping note on first mention.

## Treatment Rules

### Hard Replace

Use a hard replace when a term:
- carries the wrong domain meaning;
- sounds mechanical or translated in the target language;
- creates routing or concept-boundary ambiguity.

Examples:
- `声纹` -> `角色声音`
- `voiceprint` -> `character voice` or another domain-correct term
- `表达镜头` -> `表达校准包`
- `Voice Pattern Pack` -> `Character Voice Reference Pack`

### Preserve With Parenthetical Gloss

Use a gloss when:
- the machine-facing term must stay stable;
- the English contract name is still useful for lookup;
- the repository is transitioning from an older display term.

Examples:
- `voice_style_guide` in backticks, with nearby prose using `Voice Style Guide` or the Chinese display equivalent
- first mention of `expression lens` in a Chinese governance doc, if the English internal term matters to cross-reference a file name

### Preserve As-Is

Preserve the original term when:
- it is already the repository's stable interface name;
- it is a normal, domain-correct term for that layer;
- changing it would create more drift than it removes.

Examples:
- `voice_style_guide`
- `taxonomy`
- `canonical packet`

## Current Canonical Decisions

- `character voice`
  - canonical Chinese: `角色声音`
  - allowed narrow Chinese subcase: `角色口吻`
  - forbidden drift terms: `声纹`, `voiceprint`
- `voice_style_guide`
  - stable output ID stays `voice_style_guide`
  - canonical display English: `Voice Style Guide`
  - canonical display Chinese: `表达风格指南`
- `expression lens`
  - canonical Chinese display: `表达校准包`
  - forbidden Chinese drift term: `表达镜头`
- reference-pack surface for voice calibration
  - canonical display English: `Character Voice Reference Pack`
  - canonical display Chinese: `角色声音参考包`

## Enforcement

The register in [`references/canonical-term-register.json`](../references/canonical-term-register.json) is the source of truth for banned or migration-sensitive terms.

The repository checker in [`scripts/check_canonical_terms.py`](../scripts/check_canonical_terms.py):
- scans high-risk public surfaces;
- excludes declared historical surfaces where legacy wording may remain for recordkeeping;
- rejects forbidden terms;
- protects the repo from silently reintroducing retired wording.

## Change Procedure

When introducing or renaming a public concept:
1. update the canonical register;
2. update the relevant policy or governance prose;
3. update the active public surfaces;
4. only then update examples and reference packs if the new term changes how users read the concept.
