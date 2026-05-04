# Changelog

## Unreleased

### Phase A: Creative Posture Awareness Layer

**A1 — Posture detection atoms and root skill integration (2026-05-05)**
- Added three new knowledge atoms: `ka.creative-posture-source`, `ka.creative-posture-certainty`, `ka.creative-posture-focus`.
- Added Posture Sync step to root `SKILL.md` (runs before route selection).
- Added nine Posture-Adaptive Response Rules to root skill.
- Extended `docs/shared/constraint-key-register.json` with `posture_mode` canonical family and aliases.
- Extended `constraint-taxonomy.md` and `references/taxonomy.md` with Creative Posture Constraints section.

**A2 — Posture-weighted atom loading (2026-05-05)**
- Added optional `posture_relevance` field to `knowledge-atom.schema.json` (three axes: source, certainty, focus; five levels: primary/high/medium/low/suppress).
- Added `posture_relevance` weights to all 98 existing knowledge atoms across foundations, craft, media, and genre directories.
- Extended `validate_assets.py` with posture_relevance structural checker.
- Added `docs/posture-weighted-loading.md` explaining the three-axis system, five levels, composite scoring rule, and worked example.

**A3 — Sub-skill posture-adaptive guidance (2026-05-05)**
- Added `## Posture-Adaptive Guidance` section to all 29 sub-skill `SKILL.md` files.
- Each section provides tailored guidance for `lost` / `exploring` / `certain` certainty states, `discover` / `construct` / `generate` source modes, and relevant attention focus layers.

### Phase B: Audience Experience Evaluation Layer

**B1 — Audience Proxy Protocol (2026-05-05)**
- Added workflow protocol `wp.audience-proxy-review`: multi-persona progressive scene reading with four default proxy personas (Core Viewer, Casual Viewer, Story Editor, Genre Veteran), per-agent viewer state model (patience, trust, hooked, open_questions, predictions, concerns), and Anti-Sycophancy Guard with forbidden diplomatic phrase list and mandatory honesty self-check.
- Added evaluation rubric `rb.audience-experience`: five experience-layer dimensions (entry_pull, patience_curve, stakes_felt, promise_honesty, concern_resolution), hard-fail rules including Anti-Sycophancy Guard breach detection, and experience-grounded rewrite actions.
- Added knowledge atom `ka.audience-proxy-personas`: framework atom encoding the four proxy personas, viewer state model, anti-sycophancy guard mechanism, and decision rules for persona selection and report honesty.
- Registered new output contract `audience_proxy_report` in `references/supported-outputs.md`.
- Added `Audience-Proxy Loading Rule` and `audience_proxy_report` route heuristic to root `SKILL.md`.
- Added `audience_proxy_report` output pattern to root `SKILL.md` Output Pattern section.

### Refactor: Simplification Pass (2026-05-05)

**Wave 1 — Reduce over-engineering from Phase A2**
- Removed Preflight Sync section from root `SKILL.md` (GitHub API mid-request sync does not belong in an LLM skill prompt).
- Merged 13 individual domain Loading Rules in `SKILL.md` into one generic Domain-Specific Loading Rule (3 conditions).
- Trimmed Route Selection Heuristics from 22 to 9 (removed tautological "prefer X when user asks for X" entries).
- Trimmed Output Pattern section from 14 bullets to 6; replaced verbose per-domain descriptions with one generic line.
- Result: root `SKILL.md` reduced ~39% (321 → 196 lines).
- Removed `posture_relevance` field from all 103 knowledge atoms: per-atom axis weights were unverifiable and unmaintainable; LLM can infer relevance from atom titles and content.
- Removed `posture_relevance` property from `schemas/knowledge-atom.schema.json`.
- Removed posture_relevance structural checker from `scripts/validate_assets.py`.

### Phase F: Knowledge Deepening (2026-05-05)

**F1 — High-value craft atoms**
- Added `ka.dialogue-subtext`: three subtext mechanisms (deflection, understatement, displacement), deletion test, and direct prompt primitives for LLM use.
- Added `ka.weak-opening-diagnosis`: five canonical opening failure modes (世界建构优先, 气氛开场, 解释性台词开场, 主角迟到, 假平静开场) with per-mode diagnostic rules and minimal fix entry points.
- Added `ka.specificity-pressure`: four specificity techniques (具名替换, 动作分解, 感知锚定, 选择压力) that counter LLM abstraction tendency; operationalizes "show don't tell" as executable prompt tools.
- Added `ka.collision-prompts`: 12 structural collision templates (two-person, one-room, irreconcilable-wants patterns) to break predictable LLM scene generation; core to `generate` posture mode.

### Phase C: Iterative Generation-Evaluation Loop (2026-05-05)

**C1 — Iterative draft pipeline**
- Added `wp.iterative-draft-pipeline`: 6-step generate→audience-proxy-review→revise loop. Maximum 3 rounds; structural failure triggers outline-layer return rather than continued local patching. Links `wp.audience-proxy-review` and `rb.audience-experience` as evaluation layer.

### Phase B2/B3 Redefined + Final Wave: High-Value Gaps (2026-05-05)

**B2 — Light-touch fallback line**
- Added referral edge to `wp.quality-gate-report` fallbacks: when audit core issue is audience experience degradation rather than contract compliance, output `context_loading_plan` pointing to `wp.audience-proxy-review` instead of expanding audience dimensions inside the quality gate.
- B3 (`ka.scene-audience-contract`) skipped — already covered by existing audience-proxy, opening-job-selection, and scene-function atoms.

**Final wave — Three high-value gaps**
- Added `ka.cross-protocol-referral-edges`: heuristic atom encoding three canonical inter-protocol referral edges (quality-gate→audience-proxy, rewrite-doctor→quality-gate, scene-writing→session-execution-plan). Prevents protocol scope creep by making boundaries explicit.
- Added `ka.setup-and-payoff`: craft atom with plant/reinforce/payoff tracking, cross-scene ledger primitive, three payoff types (direct/variant/implicit), and empty-plant detection rule. Counters LLM "setup amnesia" in long-form writing.
- Added `wp.subtractive-pass` + `rb.subtractive-pass`: deletion-first revision protocol targeting LLM over-writing tendency. Three-layer deletion (declarative dialogue, stateless paragraphs, authorial transitions). Stop condition: any further deletion would break narrative continuity.
- Added fixture `fx.subtractive-pass-01`.

**Polish**
- Removed stale `docs/posture-weighted-loading.md` (artifact of reverted Phase A2).
- Removed temporary `scripts/remove_posture_relevance.py`.
- Updated stale README counts (69→107 atoms, 28→33 protocols, 28→31 rubrics, 95→98 fixtures, 31→33 outputs).

### Phase D: Emergence Guidance Layer (2026-05-05, redesigned)

**D1 — Emergence conditioner (redesigned from readiness check)**
- Added `wp.emergence-conditioner`: active conditioning protocol (not passive readiness gate). Configures three emergence conditions — compressed space, irreconcilable wants, forbidden reveal — to create structural pressure for authentic character behavior. Links `ka.collision-prompts` as template source.

## 0.1.0 - 2026-04-02
- First public initialization release of the research-first screenplay agent skill monorepo.
- Added the root orchestration skill, thin public sub-skills, runtime-oriented manifests, and routeable output contracts.
- Added screenplay knowledge atoms, workflow protocols, rubrics, registries, examples, reference packs, and validation/test infrastructure.
- Added routing benchmarks, loading-budget checks, end-to-end journeys, failure examples, and roadmap priorities for the next execution phases.
- Refreshed bilingual documentation so both human readers and downstream agents can use the repository as a durable operating surface.
