---
name: branch-and-commit
description: Create a new branch, carry the existing uncommitted changes onto it, commit them with a conventional message, and push with upstream tracking.
---

# Branch and Commit

Use this skill when you have pending changes (often made on `main` or the wrong branch) and want them on a **new branch**, committed and pushed.

## Inputs
- Optional branch name. If missing, suggest one from the changed files.

---

## Workflow Steps

### 1. Inspect Current State
```bash
git branch --show-current
git status --short
git diff --stat
```
If there is nothing to commit, stop and tell the user.

### 2. Suggest a Branch Name
Use `<type>/<short-kebab-desc>`:
- `feature/` new functionality
- `fix/` bug fixes or responsive styling repairs
- `test/` test automation
- `chore/` config, dependencies, deployment
- `docs/` documentation only

Check the name is free: `git branch --list <branch-name>` and `git ls-remote --heads origin <branch-name>`.

### 3. Create the Branch (keeps uncommitted changes)
```bash
git checkout -b <branch-name>
```
Uncommitted changes travel with the checkout. No stash is needed.
If the changes were already committed on the wrong branch, move them instead:
```bash
git branch <branch-name>          # new branch at current HEAD
git reset --hard origin/<old-branch>   # only after confirming with the user
git checkout <branch-name>
```

### 4. Guardrails
- **Never stage:** `.env`, `.env.*` (except `.env.example`), credentials, secrets.
- **Flag:** `db.sqlite3` and other `*.sqlite3` files. Include only if the user confirms.
- **Exclude:** `__pycache__/`, `.DS_Store`, `staticfiles/`, `venv/`, temporary files.

### 5. Stage Only Relevant Files
```bash
git add <file1> <file2> ...
git status --short   # verify nothing unwanted is staged
```
Avoid a blind `git add .`.

### 6. Commit (Conventional Commits)
Format: `type(scope): imperative summary`
```bash
git commit -m "<type>(<scope>): <summary>"
```

### 7. Push with Upstream Tracking
```bash
git push -u origin <branch-name>
```
Then suggest a PR title and a 2-sentence description.

---

## Example
```bash
git checkout -b fix/mobile-responsive-layout
git add questions/static/questions/css/base.css questions/templates/questions/_sidebar.html
git commit -m "fix(ui): make sidebar collapsible on mobile"
git push -u origin fix/mobile-responsive-layout
```

## Related
- `.github/skills/commit-to-current-branch.skill.md` commits on the current branch without creating a new one.
- `.github/prompt/git-branch-commit.prompt.md` is the prompt version of this workflow.
