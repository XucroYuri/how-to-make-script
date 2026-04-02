# Agent Skill Review 2026-04

## Scope

This review looked at the repository as an executable agent system rather than only as a knowledge library.

Review goals:
- logical consistency between root claims and actual implementation;
- route reliability across diverse screenplay scenarios;
- progressive disclosure instead of permanent maximal loading;
- semantic drift control across docs, manifests, workflows, routes, and fixtures;
- higher probability of strong outputs through clearer contracts and governance.

## Main Findings

### 1. Constraint semantics were over-claimed

The repo said it routed by `intent x medium x stage x output x constraints`, but the executable route checks only used the first four dimensions.

Fix:
- clarified route wording in the root skill and routing policy;
- added `constraint_signals` to router entries;
- updated route checking so constraint signals can break future near-ties instead of remaining purely rhetorical.

### 2. Manifest / protocol drift had started

Several skill manifests no longer covered the atoms required by their own workflow protocols.

Fix:
- aligned manifests with protocol-linked atoms;
- added semantic consistency checks so this drift now fails CI instead of becoming undetected behavior mismatch.

### 3. Public vs internal surfaces were not explicit

At least one skill surface existed in the repo without being routed or listed as a public root surface.

Fix:
- introduced `surface: internal` for skill manifests;
- added CI rules so public surfaces must be routeable and root-visible, while internal surfaces must stay out of public routing.

### 4. Constraint keys were drifting between canonical names and legacy detail keys

Fixtures used a mix of canonical families, shorthand aliases, and narrow detail keys.

Fix:
- expanded the constraint taxonomy where the missing families were clearly first-class;
- introduced a constraint-key register for aliases and sanctioned detail keys;
- added CI to prevent unknown constraint keys from silently spreading.

### 5. Progressive disclosure was present in spirit, but not explicit enough as a policy

The repo had advanced outputs, but the escalation ladder was still mostly implied.

Fix:
- added a dedicated progressive disclosure policy;
- separated core artifact routes, calibration lenses, divergence/diagnosis surfaces, collaboration design, and long-horizon governance.

## Current Residual Risks

- `constraint_signals` now exist, but route selection is still mostly output-anchored by design. That is correct for the current matrix, but future route families must keep the signal layer honest.
- The repo remains broad. Good governance now depends on maintainers keeping new outputs and new axes rare, explicit, and test-backed.
- Pattern packs, team modes, and project-surface outputs still need discipline to avoid becoming “smart answer” dumping grounds.

## Review Result

The design is now materially stronger as a durable agent system:
- more honest about how routing really works;
- stricter about semantic consistency;
- clearer about when advanced layers should or should not activate;
- better protected against silent drift as the repository grows.
