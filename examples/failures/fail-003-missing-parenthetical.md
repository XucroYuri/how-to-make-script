## Case: fail-003

**Protocol used:** wp.scene-writing
**Skill used:** skill.scene-writing
**Failure category:** missing_parenthetical

**What went wrong:**
The draft produced dialogue-only turns with no inline performance and no adjacent action beat. The lines read intelligibly, but actors and downstream editors had no clue how the pressure should land.

**Root cause:**
The old scene contract treated dialogue as text content rather than as a performable beat. The rubric checked function and conflict, but not whether each line was actually anchored to behavior.

**Correction:**
Add a hard fail for bare dialogue beats and require every dialogue turn to carry either inline performance or an adjacent action beat in the screenplay block format.

**Status:** addressed

**Lesson:**
If the line cannot be performed without guessing, it is not a safe screenplay handoff yet.
