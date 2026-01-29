# Repository Guidelines

## Skill Authoring Best Practices (Highest Priority)
- Keep skills small and composable; avoid a single oversized workflow skill.
- Naming: use kebab-case; prefer a gerund capability name (verb + "ing"); ensure Claude-compatible names (lowercase letters/digits/hyphens, max 64 chars).
- Frontmatter: YAML is required; always include `name` and a single-line `description` written in third person.
- Triggers: `description` should clearly say "what + when" (auto-invocation depends on this); test with realistic prompts and `/skill-name`.
- Token budget: keep `SKILL.md` concise (<500 lines). Use progressive disclosure: Quick Reference first, details later, then point to `references/`.
- Instructions > scripts: only add `scripts/` when determinism or external calls are required; document exact commands, required env vars, permissions, and expected outputs/paths.
- Safety/permissions: use `disable-model-invocation: true` for side-effecting tasks; use `user-invocable: false` for background-only skills; restrict scope with `allowed-tools`.
- Loading model: assume only `name`/`description` are always present and the full `SKILL.md` content loads on invocation (design for minimal always-on context).

## Skill Seekers Workflow Notes
- `configs/` is the canonical source of truth; `output/` is generated artifacts; `skills/` is the curated copy you can edit by hand.
- Scrape config defaults: start with `rate_limit: 0.5`; use `max_pages` only for testing; tune `url_patterns.exclude` to avoid 404 noise.

## Project Structure & Module Organization
- `main.py` is a minimal entrypoint; `pyproject.toml` pins Python 3.14+ and `skill-seekers`.
- `configs/` holds Skill Seekers configs by source (`docs/`, `github/`, `pdf/`, `unified/`).
- `output/` is raw generated content; treat as intermediate artifacts.
- `skills/` is curated, ready-to-use skills (e.g., `skills/<skill-name>/SKILL.md` plus `references/`, `scripts/`, `assets/`).
- `routers/` is for multi-skill router packages; `templates/` holds reusable templates.
- `packages/`, `scripts/`, and `logs/` are for distribution, automation, and run logs.

## Build, Test, and Development Commands
- `uv sync` - install dependencies from `pyproject.toml`/`uv.lock`.
- `uv run python main.py` - run the entrypoint with uv.
- `scripts/skill_from_url.sh <url> --name <skill-name>` - scrape → enhance → package → sync in one command.

## Security & Configuration Tips
- Do not commit API keys or tokens; use environment variables and local `.env` files.
- Treat `logs/` as transient and avoid committing user data or secrets.
