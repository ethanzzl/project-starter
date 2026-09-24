# Repository Maintenance Rules

## Project Isolation

- This repository maintains reusable project-governance templates and the `project-governance-bootstrap` Skill only.
- Do not add facts, brands, paths, branches, assets, or product rules from any specific business project.
- Treat every target project as independent unless a task explicitly requests comparison, migration, or reuse.

## Source of Truth

Use this order when sources disagree:

1. The current task
2. The repository's actual files
3. This `AGENTS.md`
4. `docs/architecture.md`
5. `README.md`
6. General knowledge

Call out meaningful conflicts instead of silently guessing.

## Change Rules

- Prefer the smallest change that fully solves the task.
- Keep templates generic and portable.
- Do not introduce platform-specific assumptions without an explicit requirement.
- Do not write user-specific absolute paths into templates or references.
- Do not hard-code a GitHub username into business-project templates.
- Do not automatically create remotes, deploy, release, or publish.
- Do not turn this repository into a CLI framework.

## Validation

After changes, run at minimum:

```bash
python3 scripts/validate.py
git diff --check
```

When the Skill changes, also run the Codex Skill quick validator when it is available.

## Git Safety

- Preserve existing files and history.
- Never force push or rewrite published history.
- Confirm the remote and current branch before an ordinary push.
- Keep commits focused and report the final worktree state.

