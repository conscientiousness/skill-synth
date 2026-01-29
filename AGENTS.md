# Repository Guidelines

## Skill Authoring Best Practices (Highest Priority)
- `SKILL.md` is the entrypoint; only its metadata is always loaded. Keep it short and move deep detail into `references/`, `scripts/`, and `assets/` (aim for under 500 lines).
- Use YAML frontmatter with `name` and `description` (single-line; keep within Codex limits of 100/500 chars). Add extra fields only when needed (e.g., `allowed-tools`, `user-invocable`, `disable-model-invocation`).
- Be explicit about triggers in the description and test them with example prompts or `/skill-name` invocations.
- Prefer instructions over scripts; use `scripts/` only when you need determinism or external calls, and document exact commands.
- Write step-by-step, imperative instructions with required inputs, permissions, and expected outputs/paths.

## Skill Seekers Best Practices (Docs Standard)
- Naming: use kebab-case gerund (verb + "ing") to describe the capability (e.g., `building-react-applications`).
- Description: third-person, actionable, and includes both "what" and "when" (discovery depends on this).
- Token budget: use progressive disclosure (Quick Reference first, deeper details later, then point to `references/`).
- Structure: YAML frontmatter required; organize references by category instead of one giant file.
- Quality: avoid verbose history, ensure examples run, and update regularly to prevent deprecated guidance.
- Scraping configs: start with `rate_limit: 0.5`, use `max_pages` only for testing, and tune `url_patterns.exclude` to avoid 404 noise.

## Claude Skills Best Practices
- `SKILL.md` is required with YAML frontmatter; `name` becomes the `/slash-command` and must be lowercase letters, digits, or hyphens (max 64 chars).
- `description` drives auto-invocation; write “what + when” clearly to avoid under/over-triggering.
- Keep `SKILL.md` concise (<500 lines) and move deep detail into `references/` or `examples/`.

## Codex Skills Best Practices
- Keep skills small and composable; avoid a single oversized workflow skill.
- Write clear step-by-step instructions; avoid vague or assumed context.
- Prefer instructions over scripts unless determinism or external calls are required.
- Use `description` to state “what + when” for reliable auto-invocation; test trigger prompts.
- Remember only `name` and `description` are loaded at startup; full `SKILL.md` loads on invocation.

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

## Security & Configuration Tips
- Do not commit API keys or tokens; use environment variables and local `.env` files.
- Treat `logs/` as transient and avoid committing user data or secrets.
