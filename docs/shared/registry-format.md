# Registry Format

## Router Matrix

`references/router-matrix.json` contains explicit routes. Each route entry names:
- supported `intent`
- supported `medium`
- supported `stage`
- supported `output`
- optional `constraint_signals` used for route explanation and tie-breaking
- `skill_id`
- `protocol_id`
- `rubric_id`

## Skill Manifest

Each skill directory contains a `manifest.json` that declares:
- stable skill `id`
- entrypoint path
- optional `surface` (`public` or `internal`)
- supported intents, media, stages, outputs
- primary protocol
- linked rubrics
- linked atoms
- fallback behavior
