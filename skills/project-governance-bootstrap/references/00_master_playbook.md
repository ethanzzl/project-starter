# Master Playbook

## Purpose

Use this playbook to choose the correct project-governance mode, protect existing work, and stop when governance is complete.

## New project or existing project

Classify from facts, not the folder name.

A project is likely `NEW` when it has no meaningful implementation or history and the user asks to initialize it. A project is existing when it has code, assets, documentation, Git history, deployments, or other material that must be preserved—even if Git is missing or the repository has no commits.

If the requested mode and repository facts conflict, describe the conflict before taking a mutating action. Default to preserving content.

## Project isolation

- Establish the current project root and repository boundary before interpreting files.
- Do not borrow product facts, paths, conventions, brands, assets, or decisions from other projects.
- In a workspace containing several repositories, treat each repository independently.
- A non-repository workspace root does not make every descendant part of one project.

## Source of truth

Use this precedence:

1. The current user request
2. The target repository's actual code and configuration
3. The target repository's `AGENTS.md` or override rules
4. The target repository's current documentation
5. Current conversation context for this project
6. General engineering knowledge

Report meaningful contradictions between files and code; do not silently choose stale documentation.

## Asset and data safety

Safety order:

1. Identify unique or non-rebuildable assets and data.
2. Confirm whether they are tracked, ignored, externally backed up, or recoverable.
3. Preserve uncertain material.
4. Back up before any authorized destructive cleanup.
5. Verify recovery before deleting a confirmed duplicate or disposable output.

A clean Git worktree proves only that tracked state matches Git. It does not prove that ignored, untracked, external, or platform-hosted assets are safe.

For data-bearing projects, identify the authoritative store, schema/migration mechanism, backup path, environment separation, and destructive commands. Never run migrations, resets, or production writes merely as a governance check.

For creative projects, distinguish source assets, generated outputs, historical exports, licenses, and external backups. Do not assume a rendered export can replace an editable source.

## Git baseline

Before a Git mutation, determine:

- repository root and nested repositories
- current branch or unborn branch
- worktree and index state
- remotes and upstream
- recent history and tags when present
- local Git identity when a commit is requested

Do not initialize Git over an undisclosed nested repository. Do not create a remote or push unless explicitly requested. Never force push or rewrite published history. A baseline commit must include only reviewed, safe files and no secrets.

## Documentation baseline

Keep responsibilities separate:

- `AGENTS.md`: how an AI agent works in this project
- `README.md`: how a person enters and uses the project
- `docs/project.md`: current project facts
- `docs/decisions.md`: durable decisions and consequences
- `docs/assets.md`: important asset and recovery facts, only when needed

Do not create empty ceremony documents. Record changing facts once, in the most appropriate file.

## Governance order

After a completed audit, govern only findings authorized by the user and use this order:

```text
asset safety
→ data safety
→ Git baseline
→ project boundaries
→ core documentation
→ path portability
→ .gitignore
→ temporary files and root-directory cleanup
→ final validation
```

Do not refactor product code merely to make the repository look tidy. If provenance is unclear, retain the material and document the uncertainty. Stop after the authorized governance findings are resolved.

## Validation boundaries

Use exact labels:

- `Local Verified`: supported by local commands or direct local observation.
- `Platform Verified`: supported by direct evidence from the actual platform, device, deployment, review system, OAuth provider, or third-party API.
- `Unverified`: not executed or not observable in the current environment.

Local builds do not prove a live deployment, store review, real-device behavior, or external API authorization. A Git push is not deployment proof.

External mutations—including deployment, publication, release, review submission, purchases, and paid API usage—require explicit authorization. Release is a separate transition from platform validation.

## Multi-project workspaces

- Inventory repository boundaries before choosing a root.
- Check whether shared assets live outside each repository.
- Avoid running root-wide cleanup or ignore changes across unrelated projects.
- Apply the nearest project rules to each file.
- Report cross-project absolute links, copied credentials, or mixed histories as risks; do not automatically migrate them.

## Stop condition

Governance is complete when the selected mode's outcome is achieved, required safety risks are addressed or explicitly deferred, and evidence is reported. Then return to product development. Do not keep adding process, abstractions, configuration, or documents.

