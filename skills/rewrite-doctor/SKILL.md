---
name: rewrite-doctor
description: Use when the user needs a script doctor style diagnosis and rewrite priorities.
---

# Rewrite Doctor

Use this skill when the request is diagnostic rather than generative.

## Workflow
1. Locate the failure layer.
2. Distinguish root causes from symptoms.
3. Return prioritized, actionable rewrite moves.

## Output Contract
- A diagnosis that separates concept, structure, scene, and line-level problems.
- A ranked list of rewrite moves with the highest leverage first.
- A clear note when the sample is too small to support a strong diagnosis.

## References
- `wp.rewrite-doctor`
- `ka.rewrite-diagnosis`
- `ka.causality-chain`
- `rb.rewrite-report`
