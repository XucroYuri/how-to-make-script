# Changelog

## Unreleased

### Phase A: Creative Posture Awareness Layer

**A1 — Posture detection atoms and root skill integration (2026-05-05)**
- Added three new knowledge atoms: `ka.creative-posture-source`, `ka.creative-posture-certainty`, `ka.creative-posture-focus`.
- Added Posture Sync step to root `SKILL.md` (runs before route selection).
- Added nine Posture-Adaptive Response Rules to root skill.
- Extended `constraint-key-register.json` with `posture_mode` canonical family and aliases.
- Extended `constraint-taxonomy.md` and `references/taxonomy.md` with Creative Posture Constraints section.

**A2 — Posture-weighted atom loading (2026-05-05)**
- Added optional `posture_relevance` field to `knowledge-atom.schema.json` (three axes: source, certainty, focus; five levels: primary/high/medium/low/suppress).
- Added `posture_relevance` weights to all 98 existing knowledge atoms across foundations, craft, media, and genre directories.
- Extended `validate_assets.py` with posture_relevance structural checker.
- Added `docs/posture-weighted-loading.md` explaining the three-axis system, five levels, composite scoring rule, and worked example.

**A3 — Sub-skill posture-adaptive guidance (2026-05-05)**
- Added `## Posture-Adaptive Guidance` section to all 29 sub-skill `SKILL.md` files.
- Each section provides tailored guidance for `lost` / `exploring` / `certain` certainty states, `discover` / `construct` / `generate` source modes, and relevant attention focus layers.

## 0.1.0 - 2026-04-02
- First public initialization release of the research-first screenplay agent skill monorepo.
- Added the root orchestration skill, thin public sub-skills, runtime-oriented manifests, and routeable output contracts.
- Added screenplay knowledge atoms, workflow protocols, rubrics, registries, examples, reference packs, and validation/test infrastructure.
- Added routing benchmarks, loading-budget checks, end-to-end journeys, failure examples, and roadmap priorities for the next execution phases.
- Refreshed bilingual documentation so both human readers and downstream agents can use the repository as a durable operating surface.
