#!/usr/bin/env python3
"""Normalize SKILL.md YAML frontmatter to avoid YAML parse errors.

Currently, some consumers parse the YAML frontmatter strictly. Unquoted `description`
values containing characters like `: ` can cause failures (e.g. "mapping values are
not allowed in this context").

This script makes the frontmatter safer by ensuring `description` is a YAML-safe,
single-line string (double-quoted via JSON escaping) unless it's already quoted or
uses block scalar style.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


_FRONTMATTER_START_RE = re.compile(r"^---\s*$")
_KEY_LINE_RE = re.compile(r"^(?P<indent>\s*)(?P<key>[A-Za-z0-9_-]+):(?P<rest>.*)$")


def _split_inline_comment(value: str) -> tuple[str, str]:
    """Split `value` into (value_without_comment, comment_suffix).

    YAML treats `#` as a comment start when preceded by whitespace. We preserve any
    trailing comment as-is when rewriting the value.
    """

    idx = value.find(" #")
    if idx == -1:
        return value, ""
    return value[:idx], value[idx:]


def _normalize_description_value(raw_rest: str) -> str:
    value = raw_rest.lstrip(" \t").rstrip("\r\n")
    if not value:
        return value

    if value.startswith(("'", '"', "|", ">")):
        return value

    value_no_comment, comment = _split_inline_comment(value)
    value_no_comment = value_no_comment.strip()
    quoted = json.dumps(value_no_comment, ensure_ascii=False)
    return f"{quoted}{comment}"


def normalize_skill_md(path: Path) -> bool:
    """Normalize a SKILL.md file in-place. Returns True if modified."""

    text = path.read_text(encoding="utf-8", errors="strict")
    lines = text.splitlines(keepends=True)
    if not lines or not _FRONTMATTER_START_RE.match(lines[0].strip("\r\n")):
        raise ValueError("Missing YAML frontmatter (expected first line to be '---').")

    end_idx: int | None = None
    for i in range(1, len(lines)):
        if _FRONTMATTER_START_RE.match(lines[i].strip("\r\n")):
            end_idx = i
            break
    if end_idx is None:
        raise ValueError("Unterminated YAML frontmatter (missing closing '---').")

    fm_lines = lines[1:end_idx]
    changed = False
    new_fm_lines: list[str] = []

    for line in fm_lines:
        m = _KEY_LINE_RE.match(line.rstrip("\r\n"))
        if not m:
            new_fm_lines.append(line)
            continue

        key = m.group("key")
        if key != "description":
            new_fm_lines.append(line)
            continue

        indent = m.group("indent")
        rest = m.group("rest")
        normalized = _normalize_description_value(rest)

        newline = "\n"
        if line.endswith("\r\n"):
            newline = "\r\n"

        rewritten = f"{indent}description: {normalized}{newline}"
        if rewritten != line:
            changed = True
        new_fm_lines.append(rewritten)

    if not changed:
        return False

    new_text = "".join([lines[0], *new_fm_lines, *lines[end_idx:]])
    path.write_text(new_text, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize SKILL.md YAML frontmatter")
    parser.add_argument("path", help="Path to SKILL.md or to a skill directory")
    args = parser.parse_args()

    target = Path(args.path)
    if target.is_dir():
        target = target / "SKILL.md"

    if not target.exists():
        raise SystemExit(f"File not found: {target}")

    modified = normalize_skill_md(target)
    if modified:
        print(f"Normalized: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

