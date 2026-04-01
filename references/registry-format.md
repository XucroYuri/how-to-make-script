# Registry Format

## Router Matrix

`references/router-matrix.json` contains explicit routes. Each route entry names:
- supported `intent`
- supported `medium`
- supported `stage`
- supported `output`
- `skill_id`
- `protocol_id`
- `rubric_id`

## Skill Manifest

Each skill directory contains a `manifest.json` that declares:
- stable skill `id`
- entrypoint path
- supported intents, media, stages, outputs
- primary protocol
- linked rubrics
- linked atoms
- fallback behavior

