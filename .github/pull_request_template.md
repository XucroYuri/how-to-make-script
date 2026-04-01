## Summary

- What changed?
- Which claim, route, rubric, template, or community surface does this PR touch?

## Why This Change Exists

- What evidence, objection, counterexample, or field report motivated it?
- Is this fixing a route failure, a theory gap, a rubric gap, a docs gap, or a governance gap?

## What Reviewers Should Challenge

- Which assumption in this PR do you most want reviewers to pressure-test?
- Where might this still be too broad, too weak, or too context-specific?

## Validation

- [ ] `python3 scripts/validate_assets.py`
- [ ] `python3 scripts/check_routes.py`
- [ ] `python3 scripts/check_links.py`
- [ ] `python3 scripts/check_forbidden_paths.py`
- [ ] `python3 scripts/check_question_todos.py`
- [ ] `python3 scripts/run_fixture_suite.py`
- [ ] `python3 -m unittest discover -s tests -v`

## Residual Uncertainty

- What is still uncertain?
- What follow-up issue, fixture, or rubric update might still be needed?
