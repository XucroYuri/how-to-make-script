# Reference Project Lessons

This document records what this repository is learning from adjacent creative-agent projects. The goal is not to copy those repos but to extract durable design lessons that strengthen screenplay-agent work.

## References

### InkOS (Narcooo/inkos)

**Key lessons:**
- Split long-horizon control documents from runtime compilation artifacts
- Compile inputs before writing instead of silently stuffing prompts
- Keep runtime traces inspectable
- Treat rules as a layered stack, not one flat instruction blob
- Keep human-readable intent notes separate from machine-facing state

**Adopt:** Stronger packet and surface thinking for future runtime layers; explicit distinction between long-term intent and current focus; inspectable packet assembly for high-value writing and review actions.

**Skip:** Novel-specific word-count governance; chapter-oriented CLI command surfaces; genre-specific novel telemetry.

### OpenWrite Skill (LiPu-jpg/Openwrite_skill)

**Key lessons:**
- Split long-horizon planning and drafting into separate entrypoints
- Require explicit handoff when planning assets are mature enough to draft from
- Keep `src/` truth separate from `data/` runtime and mirrors
- Assemble canonical packets instead of relying on invisible context
- Expose context inspection and packet export for debugging and trust

**Adopt:** Clearer phase entrypoints for planning, drafting, review, and export; stronger source-of-truth vs runtime-state doctrine; explicit handoff gates between planning and drafting surfaces.

**Skip:** Novel-specific hierarchy and chapter folder conventions; style-extraction pipelines that assume long-form prose; one-to-one naming from Goethe/Dante.

### Short Drama (0xsline/short-drama)

**Key lessons:**
- Domain-specific workflows get stronger when stage-to-artifact mapping is explicit
- Command-to-artifact mapping reduces ambiguity in production pipelines
- Quality self-check, compliance review, and export deserve their own named surfaces
- Mode switching for overseas formatting and market adaptation should be explicit
- Short-drama workflows benefit from rhythm, hook, monetization, and compliance scaffolding

**Adopt:** Stronger artifact ladders for medium-specific workflows; clearer review, compliance, and export surfaces; better support for short-drama-specific production design without flattening everything into feature norms.

**Skip:** Hard-coded hook ratios, paywall ratios, or genre presets as universal screenplay truth; platform-specific compliance assumptions as repo-wide law; short-drama command surface as default for all screenplay work.

### Shanyin Screenwriting Master (Shanyin-ai/shanyin-screenwriting-master)

**Key lessons:**
- Separate format-specific process logic for ultrashort, short, feature, and series workflows
- Track outer plot rhythm and inner emotional rhythm as related but distinct waves
- Use memory checkpoints to preserve long-form continuity without full-context reload
- Lock series container variables and arc budgets before spending major turns, reveals, and relationship jumps

**Adopt:** First-class continuity-compression surface rather than ad hoc "reload the whole draft"; stronger serial-container and arc-budget logic in structure planning; explicit dual-track rhythm language for diagnosing why a draft feels busy but emotionally static, or intimate but dramatically stalled.

**Skip:** One giant integrated screenplay prompt as main source of truth; hidden internal self-check loops that are not observable as protocols, rubrics, or artifacts; opaque packaged outputs whose editable source and machine-facing bundle can drift out of sync.

## Design Changes These References Motivated

These external projects pushed the following explicit design decisions in this repo:

- `project_surface_map` as a first-class output
- `story_memory_checkpoint` as a first-class long-horizon continuity output
- Source-of-truth vs runtime-state separation
- Canonical packet assembly
- Explicit phase entrypoints and handoffs
- Review and export surfaces as named workflow surfaces
- Format-aware structure scaling, dual-track rhythm, and serial arc budgeting (instead of one universal outline heuristic)

## Non-Dogma Rule

External reference projects are evidence of useful workflow shapes, not proof that one creative-agent architecture is universally correct. This repo should keep extracting what generalizes, what stays medium-bound, what stays tool-bound, and what should remain only as a case reference.
