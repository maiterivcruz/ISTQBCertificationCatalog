---
name: commit-to-current-branch
description: Inspect git status, stage relevant changes safely, and create a commit on the current branch with a suggested conventional message.
---

# Commit to Current Branch

Use this skill whenever you need to commit pending changes directly to the **currently active branch** without switching or creating a new branch.

## Purpose
- Inspect `git status` and diffs on the current branch.
- Exclude sensitive or unwanted files (e.g., `.env`, temporary files, untracked artifacts).
- Generate a suggested commit message following **Conventional Commits** (`type(scope): imperative summary`).
- Present the commands or execute the commit upon user confirmation.

---

## Workflow Steps

### 1. Inspect Current State
Check the active branch and uncommitted changes:
```bash
git branch --show-current
git status --short
git diff --stat
```

### 2. Guardrails (Never Commit Secrets or Caches)
- **Always ignore/verify:** `.env`, `.env.local`, credentials, secrets.
- **Flag if present:** `*.sqlite3` / `db.sqlite3` unless the user explicitly asks to commit a seed database.
- **Exclude caches:** `__pycache__/`, `.DS_Store`, build artifacts.

### 3. Determine the Commit Type & Scope
Categorize changes using standard conventional commit types:
- `feat`: new feature or functionality (e.g., `feat(catalog): add chapter progress indicator`)
- `fix`: bug fix or UI correction (e.g., `fix(ui): resolve mobile sidebar horizontal overflow`)
- `docs`: documentation only (e.g., `docs(readme): add live Render demo url and cold start note`)
- `style`: formatting, whitespace, no production code change
- `refactor`: code restructuring without changing behavior
- `chore`: dependencies, tooling, or deployment config (e.g., `chore(deploy): update render build command`)
- `test`: test suites or automated tests

### 4. Provide the Suggested Commit Command

Provide the exact command sequence:

```bash
# 1. Stage only the intended files explicitly (avoid blindly using `git add .`)
git add <file1> <file2> ...

# 2. Commit with conventional message
git commit -m "<type>(<scope>): <concise imperative summary>"

# 3. (Optional) Push to the remote tracking branch if requested
git push origin $(git branch --show-current)
```

---

## Example Outputs

### Example 1: Documentation Update
```bash
git add README.md
git commit -m "docs(readme): add live Render service link and cold-start notice"
```

### Example 2: Mobile UI Fix
```bash
git add questions/static/questions/css/base.css questions/templates/questions/_sidebar.html
git commit -m "fix(ui): improve mobile sidebar collapse and full-width layout"
```
