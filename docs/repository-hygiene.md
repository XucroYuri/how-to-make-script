# Repository Hygiene

## Forbidden Workspace State

The repository treats local editor and agent-tool state as workstation noise, not project source.

Rules:
- local-tool state paths from the canonical denylist in `.gitignore` and `scripts/check_forbidden_paths.py` must stay ignored
- forbidden local-tool paths must never be tracked in the current index.
- forbidden local-tool paths must never exist anywhere in published Git history.

## Current Policy

This repository is already published.
That means hygiene is not only about future ignores; it also includes history auditing and CI enforcement.

## If A Forbidden Path Is Staged But Not Yet Pushed

```bash
git rm -r --cached <path>
git commit --amend --no-edit
```

If the accidental commit is not the latest one, rewrite the local branch history before pushing.

## If A Forbidden Path Has Already Been Pushed

Rewrite the branch history and force-push the cleaned branch before publication:

```bash
git filter-repo --path <path> --invert-paths
git push --force-with-lease origin <branch>
```

After the rewrite:
- invalidate or rotate any sensitive local metadata if needed;
- ask collaborators to rebase or re-clone;
- verify with `python3 scripts/check_forbidden_paths.py`.

## Automated Enforcement

The repository enforces this with:
- `.gitignore`
- [`scripts/check_forbidden_paths.py`](../scripts/check_forbidden_paths.py)
- unit tests
- CI with full-history checkout
