# New Project Bootstrap

## Outcome

Create a safe, minimal project baseline and then stop before business-feature development.

## Procedure

1. Confirm the project name, purpose, intended root, formal implementation directory, primary branch, runtime/platform, and expected validation.
2. Inspect the current directory and nested repositories. Preserve every existing file unless its replacement is explicitly approved.
3. Determine whether Git already exists. Initialize only the intended project root, never over an undisclosed repository.
4. Check repository-local `user.name` and `user.email` before committing. Ask for identity only when it is missing and cannot be inferred from explicit project instructions. Never alter global Git config.
5. Create a narrow `.gitignore` for OS metadata, editor temporaries, logs, environment secrets, caches, and the actual technology stack. Prefer root-anchored output patterns when the directory is truly generated.
6. Create and fill:
   - `AGENTS.md`
   - `README.md`
   - `docs/project.md`
   - `docs/decisions.md`
7. Create `docs/assets.md` only when the project has unique or non-rebuildable assets whose tracking, backup, or recovery must be recorded.
8. Establish the smallest meaningful validation capability for the actual stack. Do not add a framework solely for governance.
9. Inspect staged content for secrets, personal paths, unrelated project facts, generated noise, and accidental large assets.
10. Run appropriate local validation and `git diff --check`.
11. Create the first safe baseline commit when the user requested initialization and committing is within that request.
12. Report files created, validation run, commit/Git state, open risks, and unverified platform behavior. Stop.

## Template use

Use repository templates as starting points, then replace every placeholder with verified project facts. Remove inapplicable optional sections rather than leaving fictional content.

Required placeholder concepts include:

- project name
- formal implementation directory
- primary branch
- validation commands

Do not copy repository-maintenance rules into the business project. Do not put changing history in README or AI workflow rules in product documentation.

## Prohibited automatic actions

Without a separate explicit request, do not:

- create or change a Git remote
- push
- deploy or publish
- create an empty `DESIGN.md`
- start feature implementation
- add speculative architecture, dependencies, or a CLI

The bootstrap ends when the baseline is safe, validated, and reported.

