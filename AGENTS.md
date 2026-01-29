# Repository Guidelines

## Skill Authoring Best Practices (Highest Priority)
- `SKILL.md` is the entrypoint; only its metadata is always loaded. Keep it short and move deep detail into `references/`, `scripts/`, and `assets/` (aim for under 500 lines).
- Use YAML frontmatter with `name` and `description` (single-line; keep within Codex limits of 100/500 chars). Add extra fields only when needed (e.g., `allowed-tools`, `user-invocable`, `disable-model-invocation`).
- Be explicit about triggers in the description and test them with example prompts or `/skill-name` invocations.
- Prefer instructions over scripts; use `scripts/` only when you need determinism or external calls, and document exact commands.
- Write step-by-step, imperative instructions with required inputs, permissions, and expected outputs/paths.

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
