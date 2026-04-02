# Semantic Governance

This repository now has enough outputs, route surfaces, and workflow layers that semantic drift is a real engineering risk, not just a wording problem.

The goal of this policy is simple: the same concept should not silently mean different things in the root skill, router, manifests, protocols, fixtures, and docs.

## Governance Rules

1. One public concept should have one primary name.
2. Public prose naming should follow [`docs/canonical-term-policy.md`](./canonical-term-policy.md) and [`references/canonical-term-register.json`](../references/canonical-term-register.json).
3. Legacy shorthand can survive, but only through an explicit alias or detail-key register.
4. Public skill surfaces must be routeable and visible from the root skill.
5. Internal helper skills may exist, but they must be marked `surface: internal`.
6. A skill manifest must at least cover the atoms required by its primary protocol.
7. Output contracts must stay aligned across:
   - `SKILL.md`
   - [`references/supported-outputs.md`](../references/supported-outputs.md)
   - [`references/output-format-contracts.md`](../references/output-format-contracts.md) when a golden artifact is meant to demonstrate a concrete Markdown delivery shape
   - [`references/taxonomy.md`](../references/taxonomy.md)
   - `workflow_protocol.output_contract`
   - routed skill manifests
   - fixtures
8. Route claims must stay honest.
   - If constraints only affect loading, say so.
   - If constraints are used as route signals or tie-breakers, declare them.

## Constraint Key Policy

Canonical route-facing families live in [`references/taxonomy.md`](../references/taxonomy.md).

Legacy aliases and sanctioned detail keys live in [`references/constraint-key-register.json`](../references/constraint-key-register.json).

Use the register when:
- old fixtures still carry earlier wording;
- a detailed production key is useful locally but too narrow to become a top-level taxonomy family;
- the repo needs backward compatibility without letting new content drift further.

## Route Signal Policy

`router-matrix` entries may declare `constraint_signals`.

These signals do not turn the router into a fuzzy keyword engine. They exist for three narrower jobs:
- explain why a route is appropriate;
- disambiguate near-equal adjacent routes when overlaps appear later;
- make loading decisions traceable instead of opaque.

## Surface Policy

- `public` skill surfaces are part of the root orchestration story.
- `internal` skill surfaces may exist for decomposition, comparison, or future migration, but they should not appear as public entrypoints unless they are routed and documented.

## Validation

Semantic governance is enforced by:
- [`scripts/check_canonical_terms.py`](../scripts/check_canonical_terms.py)
- [`scripts/check_semantic_consistency.py`](../scripts/check_semantic_consistency.py)
- [`scripts/check_routes.py`](../scripts/check_routes.py)
- [`scripts/check_route_overlaps.py`](../scripts/check_route_overlaps.py)
- [`scripts/check_golden_artifact_formats.py`](../scripts/check_golden_artifact_formats.py)

The point is not taxonomy perfection. The point is to stop undetected drift before the repo starts telling the agent conflicting stories about what it is supposed to do.
