# Development Execution Loop

## Inputs

Before ordinary development, read the target project's `AGENTS.md`, `docs/project.md`, and any decision record relevant to the requested area. Use current code and configuration when documentation is stale, and report the conflict.

## Loop

```text
goal
→ read before editing
→ smallest complete change
→ failure path
→ validation
→ commit when requested or established by project workflow
→ completion report
```

### Goal

Translate the request into an observable outcome, constraints, and a proportionate success test. Do not expand the feature.

### Read before editing

Locate the actual implementation, nearby tests, callers, project rules, and current Git state. Reuse the project's existing patterns and dependencies.

### Smallest complete change

Fix the root cause or implement the requested behavior with the minimum necessary surface area. Do not introduce new layers, frameworks, utilities, or configuration for a local problem.

### Failure path

Check invalid input, missing state, partial external failure, recovery behavior, and any path that could lose data or assets. A workaround must be labeled as a workaround.

### Validation

Choose checks proportional to risk: focused tests, type-check, lint, build, runtime/API checks, browser checks, or platform evidence. Do not treat code inspection as execution.

Use these labels:

- `Local Verified`: checks actually executed locally and their results.
- `Platform Verified`: behavior directly observed on the real target platform.
- `Unverified`: checks not executed, including the reason when useful.

A local pass cannot be promoted to platform verification. A push cannot be promoted to deployment verification.

### Commit

Before committing, inspect status, diff, staged content, and `git diff --check`. Keep unrelated user changes out of the commit. Do not push unless explicitly authorized; never force push.

### Completion report

Report:

1. What changed
2. Why this solution was chosen
3. Local Verified
4. Platform Verified, if any
5. Unverified items
6. Known risks or follow-up
7. Commit and worktree state

Do not call a preview, upload, submission, review, or pending deployment “released.”

