# Quick Audit

## Read-only invariant

This audit must not change files, Git state, caches, lockfiles, build output, platform state, or metadata under the project. Avoid commands that compile, format, install, generate, fix, migrate, authenticate, or update indexes. If a useful check may write, inspect its behavior first or mark it unverified.

After the report, stop. Do not automatically remediate findings.

## Audit scope

### Project identity

- Intended product or purpose
- Candidate project root
- Formal implementation directory
- Conflicting names or identities
- Nested or sibling repository boundaries

### Git

- Repository root, branch, worktree/index state
- Remote and upstream
- Recent baseline and whether history exists
- Tracked, untracked, ignored, and submodule state where relevant
- Local identity only if future commits are expected

### Root directory and technology

- Root-directory organization and ambiguous implementations
- Detected languages, frameworks, package managers, build systems, and lockfiles
- Whether documented commands match actual configuration

### Documentation

- `AGENTS.md`, README, current project facts, durable decisions, and asset records
- Stale or contradictory claims
- Missing information that blocks safe work

### Isolation and portability

- References to unrelated projects, brands, branches, or assets
- User-specific absolute paths and environment-dependent links
- Root assumptions that break in multi-project workspaces

### Secrets and privacy

- Likely credentials, tokens, keys, personal data, environment files, or secret-bearing logs
- Whether sensitive files are tracked or insufficiently ignored
- Report suspected exposure without reproducing secret values

### Assets and data

- Unique, editable, historical, generated, ignored, or externally stored assets
- Rebuildability and backup/recovery evidence
- Databases, migrations, snapshots, and destructive scripts

### `.gitignore`

- Missing secrets, caches, logs, editor files, and stack-specific generated material
- Overbroad patterns that could hide source, assets, or nested content
- Tracked files that ignore rules cannot retroactively protect

### Verification capability

- Available read-only evidence for test, type-check, lint, build, runtime, and platform status
- Commands documented by the project
- Checks not run because they would mutate state

## Severity

- `P0`: immediate risk of data/asset loss, secret exposure, destructive behavior, or a repository identity error that makes work unsafe.
- `P1`: significant correctness, recovery, portability, or governance gap that should be resolved before substantial development.
- `P2`: non-blocking maintainability, clarity, or consistency issue.

## Health level

- `Level A`: clear identity and boundaries, safe baseline, adequate documentation, no open P0/P1, and usable validation.
- `Level B`: workable but has one or more material P1 gaps; ordinary work may continue only with explicit awareness of the risks.
- `Level C`: unsafe or ambiguous baseline, any P0, multiple compounding P1s, or insufficient evidence to modify the project safely.

State when the level is limited by missing evidence.

## Required report

Output only these sections, with concise evidence:

1. Project identity
2. Git
3. Technology stack
4. Root-directory health
5. Documentation
6. Cross-project contamination
7. Paths and portability
8. Secrets and privacy
9. Unique assets and data
10. `.gitignore`
11. Verification capability
12. P0 / P1 / P2 findings
13. Level A / B / C
14. Recommended next step

End by stating that the audit was read-only and remediation was not performed.

