#!/usr/bin/env python3
"""Build a Skill Seekers scrape config from a URL."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import urlparse

DEFAULT_EXCLUDES = [
    "/zh/",
    "search",
    "#",
    "_static/",
    "_sources/",
    "genindex.html",
    "py-modindex.html",
    "objects.inv",
]


def _slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "skill"


def _derive_base_path(path: str) -> str:
    parts = [p for p in path.split("/") if p]
    if not parts:
        return "/"
    if "docs" in parts:
        idx = parts.index("docs")
        return "/" + "/".join(parts[: idx + 1]) + "/"
    return "/" + parts[0] + "/"


def _derive_name(host: str, path: str) -> str:
    parts = [p for p in path.split("/") if p]
    if parts:
        last = re.sub(r"\.(html?|php|aspx?)$", "", parts[-1])
        if last in {"index", "overview"}:
            parts = parts[:-1]
        else:
            parts[-1] = last
    parts = parts[:3]
    return _slugify("-".join([host] + parts))


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Skill Seekers config JSON from URL")
    parser.add_argument("url")
    parser.add_argument("--output", required=True, help="Path to write config JSON")
    parser.add_argument("--name", required=True, help="Skill name (required)")
    parser.add_argument("--description", help="Override skill description")
    parser.add_argument("--max-pages", type=int, default=300)
    parser.add_argument("--rate-limit", type=float, default=0.5)
    args = parser.parse_args()

    parsed = urlparse(args.url)
    if not parsed.scheme or not parsed.netloc:
        raise SystemExit("Invalid URL: must include scheme and host")

    host = parsed.hostname or parsed.netloc
    base_path = _derive_base_path(parsed.path)
    base_url = f"{parsed.scheme}://{host}{base_path}"
    include_pattern = base_path if base_path != "/" else parsed.path or "/"

    name = args.name
    description = args.description or f"Use this skill for documentation at {parsed.netloc}{base_path}"

    config = {
        "name": name,
        "description": description,
        "base_url": base_url,
        "start_urls": [args.url],
        "selectors": {
            "main_content": "article, main, div[role='main']",
            "title": "title",
            "code_blocks": "pre code",
        },
        "url_patterns": {
            "include": [include_pattern],
            "exclude": DEFAULT_EXCLUDES,
        },
        "rate_limit": args.rate_limit,
        "max_pages": args.max_pages,
    }

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(config, indent=2), encoding="utf-8")
    print(name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
