---
name: voice-style-calibration
description: 需要为角色、IP、品牌或交互特定写作提供语音风格指南时使用。
---

# Voice Style Calibration

Use this skill when the user asks for language style calibration, character voice separation, IP continuity, brand tone control, or stronger lived-in expression before drafting.

## Workflow
1. Identify the speaking identity and the current expression job.
2. Lock voice anchors, lived pressure, and register envelope.
3. Define variability budget and drift warnings.
4. Return a guide that constrains drift without freezing creativity.

## Output Contract
- `voice_style_guide`: a calibration guide with voice anchors, lived-pressure notes, register envelope, variability budget, and drift warnings.
- The guide should make future drafting easier, not replace future drafting.
- Treat sample lines as disposable demonstrations, not canon templates.

## Posture-Adaptive Guidance

**When `certainty = lost`:**
Ask: "Say one line this character would say that no other character in this story would say." One authentic line is more useful than a voice taxonomy. Let it anchor the calibration.

**When `source = discover`:**
Surface the voice from character psychology: "What does this person reach for when they are under pressure — precision, deflection, humour, silence?" Register follows from need, not from aesthetics.

**When `source = construct`:**
Apply the full workflow: speaking identity → expression job → voice anchors → lived-pressure notes → register envelope → variability budget → drift warnings. Sample lines are demonstrations, not canon.

**When `focus = language`:**
Primary activation context. Load `ka.character-voice-consistency`, `ka.verbal-rhythm`, and `ka.embodied-text-pressure` first. Register envelope and variability budget are the most actionable outputs.

**When `focus = character`:**
Voice is character psychology made audible. Before calibrating register, confirm the character's wound-lie-want-need axis. Voice that contradicts that axis is not authentic voice, even if it sounds interesting.

## References
- `wp.voice-style-guide`
- `rb.voice-style-guide`
- `ka.character-voice-consistency`
- `ka.cross-protocol-referral-edges`
- `ka.dialogue-subtext`
- `ka.embodied-text-pressure`
- `ka.ip-voice-continuity`
- `ka.register-adaptation`
- `ka.tone-writing-moves`
