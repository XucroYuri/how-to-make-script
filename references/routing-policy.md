# Routing Policy

## Goal

Route script requests with enough structure that the selected skill, protocol, and rubric can be explained and tested.

## Required Dimensions
- `intent`
- `medium`
- `stage`
- `output`
- `constraints`

## Rules
- Never collapse all requests into one giant prompt.
- Prefer a single primary protocol per request.
- Select one primary rubric for the final artifact.
- Load only the atoms linked by the selected protocol unless the request explicitly asks for broader teaching or comparison.
- When multiple routes are plausible, prefer the narrower route over the generic route.

## Fallbacks
- If `medium` is unknown, use a generic narrative route only when the request is clearly not commercial or interactive.
- If `output` is absent, infer the smallest useful output from stage:
  - `ideation -> premise`
  - `structure -> beat_sheet`
  - `scene -> scene_draft`
  - `dialogue -> dialogue_polish`
  - `rewrite -> rewrite_report`

