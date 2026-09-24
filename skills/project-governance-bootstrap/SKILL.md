---
name: project-governance-bootstrap
description: Initialize a new project governance baseline, perform a read-only health audit of an existing repository, govern an audited project, or run its lightweight development and platform-validation workflow. Use for project setup, repository health checks, project takeover, governance remediation, and development under an existing AGENTS.md.
---

# Project Governance Bootstrap

Build and maintain a safe project baseline without turning governance into a product of its own.

## Select the mode

Infer the mode from the request and repository facts:

- `NEW`: initialize, start, or set up a new project.
- `AUDIT`: inspect, check health, or take over an existing project. This mode is strictly read-only.
- `GOVERN`: remediate an already audited Level B/C project or continue explicitly requested governance.
- `DEVELOPMENT`: implement ordinary work when the project already has an effective `AGENTS.md`.
- `PLATFORM_VALIDATION`: verify behavior on an external platform, device, review system, deployment, OAuth flow, or third-party API.

Do not enter `GOVERN` without an audit result. If an ordinary development request arrives in a governed project, do not rerun the full audit.

Use this lifecycle as a reasoning aid, not as a database:

```text
NEW → AUDITED → GOVERNED → DEVELOPMENT → PLATFORM_VALIDATION → RELEASE
```

Infer state from the repository. A project may record `Current Stage` in `docs/project.md`, but do not require a dedicated state file.

## Load only what the mode needs

- Always read [the master playbook](references/00_master_playbook.md).
- For `AUDIT`, also read [the quick audit](references/01_quick_audit.md).
- For `NEW`, also read [the new-project bootstrap](references/02_new_project_bootstrap.md).
- For `DEVELOPMENT`, read the target project's `AGENTS.md`, `docs/project.md`, any relevant `docs/decisions.md`, and [the execution loop](references/03_execution_loop.md).
- For `GOVERN`, use the audit findings and the governance order in the master playbook; read other references only when needed.
- For `PLATFORM_VALIDATION`, use the evidence rules in the master playbook and the reporting distinctions in the execution loop.

## Non-negotiable boundaries

- Protect existing files, history, data, and unique assets.
- Keep projects isolated; never import facts from unrelated work.
- Never delete uncertain material merely because it appears generated or untracked.
- Never create a remote, push, deploy, publish, release, purchase, or use a paid API without explicit authorization.
- Never force push or rewrite published history.
- Keep changes minimal and stop governance when the selected mode is complete.
- In `AUDIT`, make no filesystem, Git, configuration, build, cache, or platform mutations. Use only commands known to be read-only.
- Do not claim platform success from local evidence.

## Finish at the mode boundary

- `NEW`: create and validate the baseline, commit when authorized by the request, report, and stop before business development.
- `AUDIT`: output the required report and stop without remediation.
- `GOVERN`: resolve the authorized findings in safety order, validate, report, and stop before unrelated refactoring.
- `DEVELOPMENT`: complete the requested change, validate proportionally, report verified/unverified items and Git state.
- `PLATFORM_VALIDATION`: report the evidence actually observed and clearly distinguish local from platform verification.

