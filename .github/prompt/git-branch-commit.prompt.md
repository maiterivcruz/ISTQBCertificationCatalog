---
description: Branch pending changes, write a conventional commit, and prepare for push
---

Inspect my current git status and unstaged/staged diffs. Help me branch and commit my working changes cleanly:

1. **Suggest Branch Name:**
   - Analyze the modified files and propose a concise branch name following conventional standards:
     - `feature/<short-desc>` for new functionality
     - `fix/<short-desc>` for bug fixes or responsive styling repairs
     - `test/<short-desc>` for test automation additions
     - `chore/<short-desc>` for config, dependencies, or deployments

2. **Terminal Commands:**
   - Give me the exact copy-paste terminal command sequence to:
     a) Create and switch to the new branch while keeping my uncommitted changes:
        `git checkout -b <branch-name>`
     b) Stage only the relevant changed files (flag if `.env`, `db.sqlite3`, or untracked temporary files shouldn't be added).
     c) Commit using the Conventional Commits format (`type(scope): imperative summary`).
     d) Push to remote with upstream tracking:
        `git push -u origin <branch-name>`

3. **Pull Request Summary:**
   - Write a 2-sentence PR title and description ready to paste into GitHub.
