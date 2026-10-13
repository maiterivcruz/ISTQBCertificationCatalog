# Skill: Commit to Current Branch with Suggested Comment

## Purpose
Inspect the current git status, filter out sensitive or non-repository files, and commit directly to the **current active branch** using a clear conventional commit message.

## Inputs
- Current branch (`git branch --show-current`)
- Modified files and staged/unstaged diffs (`git status --short`)

## Steps

1. **Inspect git status:**
   ```bash
   git branch --show-current
   git status --short
   ```

2. **Verify exclusions:**
   - Confirm `.env`, passwords, or API keys are **not** staged or committed.
   - Do not stage `db.sqlite3` unless explicitly requested.

3. **Stage specific files:**
   Stage only the relevant modified files explicitly:
   ```bash
   git add <path/to/file> ...
   ```

4. **Suggest a Conventional Commit comment:**
   Follow `<type>(<scope>): <short imperative action>`:
   - `feat(...)`: new functionality
   - `fix(...)`: bug fixes and UI repairs
   - `docs(...)`: documentation changes (e.g. `README.md`)
   - `chore(...)`: tooling, build, or dependencies

5. **Commit and optionally push:**
   ```bash
   git commit -m "<suggested_message>"
   git push origin $(git branch --show-current)
   ```
