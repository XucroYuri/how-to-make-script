## Case: fail-004

**Protocol used:** wp.scene-writing
**Skill used:** skill.scene-writing
**Failure category:** av_cue_omission

**What went wrong:**
The scene clearly depended on a low mechanical hum and a sudden blackout beat, but the draft buried both ideas in freeform prose. Downstream readers could not reliably tell whether those were staging essentials or decorative narration.

**Root cause:**
The old contract had no stable surface for `VFX`, `SFX`, or `BGM`, so audiovisual information drifted between action lines, parenthetical-style notes, and vague mood language.

**Correction:**
Keep `VFX` / `SFX` / `BGM` optional, but require fixed labels whenever those cues are explicitly present.

**Status:** addressed

**Lesson:**
Optional does not mean freeform. If a cue matters, it needs a stable slot.
