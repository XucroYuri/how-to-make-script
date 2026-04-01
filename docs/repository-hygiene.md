# Repository Hygiene

## Forbidden Workspace State

The repository treats `.obsidian/` as local editor state, not project source.

Rules:
- `.obsidian/` must stay ignored.
- `.obsidian/` must never be tracked in the current index.
- `.obsidian/` must never exist anywhere in published Git history.

## Current Verified State

At bootstrap time for this repository:
- `.obsidian/` exists locally;
- `.gitignore` excludes it;
- the repository has no commits yet;
- the repository has no remote yet;
- there is no pushed history to rewrite.

## If `.obsidian/` Is Staged But Not Yet Pushed

```bash
git rm -r --cached .obsidian
git commit --amend --no-edit
```

If the accidental commit is not the latest one, rewrite the local branch history before pushing.

## If `.obsidian/` Has Already Been Pushed

Rewrite the branch history and force-push the cleaned branch before publication:

```bash
git filter-repo --path .obsidian --invert-paths
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

