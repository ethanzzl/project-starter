#!/usr/bin/env python3
"""Static validation for the project-starter repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = (
    "AGENTS.md",
    "README.md",
    "CHANGELOG.md",
    "templates/AGENTS.md.template",
    "templates/README.md.template",
    "templates/.gitignore.template",
    "templates/docs/project.md.template",
    "templates/docs/decisions.md.template",
    "templates/docs/assets.md.template",
    "skills/project-governance-bootstrap/SKILL.md",
    "skills/project-governance-bootstrap/references/00_master_playbook.md",
    "skills/project-governance-bootstrap/references/01_quick_audit.md",
    "skills/project-governance-bootstrap/references/02_new_project_bootstrap.md",
    "skills/project-governance-bootstrap/references/03_execution_loop.md",
    "docs/architecture.md",
    "docs/usage.md",
    "docs/examples.md",
    "scripts/validate.py",
)

REQUIRED_AGENT_VARIABLES = {
    "PROJECT_NAME",
    "FORMAL_IMPLEMENTATION_DIR",
    "PRIMARY_BRANCH",
    "VALIDATION_COMMANDS",
}

VARIABLE_RE = re.compile(r"\{\{([A-Z][A-Z0-9_]*)\}\}")
BRACE_RE = re.compile(r"\{\{.*?\}\}")
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")

ABSOLUTE_PATH_PATTERNS = (
    re.compile(r"(?<![A-Za-z0-9_])/Users/[^\s`'\"<>]+"),
    re.compile(r"(?<![A-Za-z0-9_])/home/[^\s`'\"<>]+"),
    re.compile(r"[A-Za-z]:\\Users\\[^\s`'\"<>]+", re.IGNORECASE),
)

PROJECT_SPECIFIC_TERMS = (
    "avivaluo",
    "暖芽",
    "小红书小组件",
)


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def check_required_files(errors: list[str]) -> None:
    for item in REQUIRED_FILES:
        path = ROOT / item
        if not path.is_file():
            errors.append(f"missing required file: {item}")
        elif not path.read_text(encoding="utf-8").strip():
            errors.append(f"required file is empty: {item}")


def check_template_paths_and_variables(errors: list[str]) -> None:
    template_root = ROOT / "templates"
    for path in sorted(item for item in template_root.rglob("*") if item.is_file()):
        content = path.read_text(encoding="utf-8")
        for pattern in ABSOLUTE_PATH_PATTERNS:
            if pattern.search(content):
                errors.append(f"user-specific absolute path in {relative(path)}")

        placeholders = set(VARIABLE_RE.findall(content))
        raw_placeholders = set(BRACE_RE.findall(content))
        valid_placeholders = {f"{{{{{name}}}}}" for name in placeholders}
        for invalid in sorted(raw_placeholders - valid_placeholders):
            errors.append(f"invalid template variable {invalid!r} in {relative(path)}")

    agents_template = template_root / "AGENTS.md.template"
    if agents_template.is_file():
        found = set(VARIABLE_RE.findall(agents_template.read_text(encoding="utf-8")))
        for name in sorted(REQUIRED_AGENT_VARIABLES - found):
            errors.append(f"missing required AGENTS template variable: {name}")


def check_reference_isolation(errors: list[str]) -> None:
    references = ROOT / "skills/project-governance-bootstrap/references"
    for path in sorted(references.glob("*.md")):
        content = path.read_text(encoding="utf-8")
        for pattern in ABSOLUTE_PATH_PATTERNS:
            if pattern.search(content):
                errors.append(f"absolute path in Skill reference: {relative(path)}")
        lowered = content.casefold()
        for term in PROJECT_SPECIFIC_TERMS:
            if term.casefold() in lowered:
                errors.append(
                    f"business-project-specific term {term!r} in {relative(path)}"
                )


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and (path.suffix == ".md" or path.name.endswith(".md.template"))
        and ".git" not in path.parts
    )


def check_markdown_links(errors: list[str]) -> None:
    for path in markdown_files():
        content = path.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK_RE.findall(content):
            target = raw_target.strip().split()[0].strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            file_target = unquote(target.split("#", 1)[0])
            resolved = (path.parent / file_target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(
                    f"local Markdown link escapes repository in {relative(path)}: {target}"
                )
                continue
            if not resolved.exists():
                errors.append(
                    f"broken local Markdown link in {relative(path)}: {target}"
                )


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    check_template_paths_and_variables(errors)
    check_reference_isolation(errors)
    check_markdown_links(errors)

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation passed:")
    print(f"- required files: {len(REQUIRED_FILES)}")
    print(f"- Markdown files checked: {len(markdown_files())}")
    print("- template paths and variables: valid")
    print("- Skill reference isolation: valid")
    print("- local Markdown links: valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
