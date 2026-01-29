# Skill Synth

Build, enhance, and package SKILL.md libraries with Skill Seekers. This repo provides repeatable workflows, curated outputs, and one‑command helpers for turning docs into production‑ready skills.

## Repository Layout
- `configs/` – scrape configs (source of truth)
- `output/` – generated skills + `_data` scrape cache + packaged zips
- `skills/` – curated copies you can edit by hand
- `scripts/` – automation helpers
- `templates/` – reusable templates

## Available Skills
- `using-skillseekers-docs` – Skill Seekers documentation: scraping, enhancement, packaging, upload, and MCP workflows.
- `using-tastytrade-python-sdk` – tastytrade (tastyworks) Python SDK: sessions, accounts, orders, instruments, market data, and streaming APIs.

## Quick Start (One Command)
Generate or update a skill from a URL (name is required):
```bash
scripts/skill_from_url.sh https://example.com/docs/ --name my-docs --engine codex
```
This will:
1) build a config under `configs/docs/`
2) scrape → enhance → package
3) sync the skill to `skills/<name>`
4) create `output/<name>.zip`

## Full Workflow (Manual)
1) **Create config**
```bash
python scripts/build_config_from_url.py https://example.com/docs/ --output configs/docs/my-docs.json --name my-docs
```
2) **Scrape**
```bash
uv run skill-seekers scrape --config configs/docs/my-docs.json --async --workers 6
```
3) **Enhance** (aligned with Skill Seekers prompt spec)
```bash
scripts/enhance.sh --engine codex output/my-docs
# or: --engine gemini
```
4) **Package**
```bash
printf "y\n" | uv run skill-seekers package --no-open output/my-docs/
```
5) **Sync curated copy** (optional)
```bash
cp -r output/my-docs skills/my-docs
```

## Update Existing Skill
When docs or repos change:
```bash
uv run skill-seekers scrape --config configs/docs/my-docs.json --async --workers 6
scripts/enhance.sh --engine codex output/my-docs
printf "y\n" | uv run skill-seekers package --no-open output/my-docs/
cp -r output/my-docs skills/my-docs
```

## Scripts
- `scripts/skill_from_url.sh` – one‑command pipeline from URL
- `scripts/enhance.sh` – entrypoint for Codex/Gemini enhancement
- `scripts/enhance_with_codex.sh` / `scripts/enhance_with_gemini.sh` – engine‑specific runners
- `scripts/build_config_from_url.py` – URL → config JSON

## Outputs Explained
- `output/<skill-name>/` – generated skill (SKILL.md + references)
- `output/<skill-name>_data/` – scrape cache (kept by Skill Seekers)
- `output/<skill-name>.zip` – packaged skill ready for upload
- `SKILL.md.backup` – enhancement backup (required by Skill Seekers‑style prompts)

## Notes & Best Practices
- Treat `configs/` as the canonical source for reproducible builds.
- If a site yields 404s, add those paths to `url_patterns.exclude`.
- For large docs, use split/router features (`reference.md` in Skill Seekers docs).
- Keep secrets in environment variables (API keys for upload).

## Common Flags
```bash
# one-command options
scripts/skill_from_url.sh <url> --name my-docs --engine codex --max-pages 300 --rate-limit 0.5 --workers 6
scripts/skill_from_url.sh <url> --name my-docs --engine none --no-sync --no-clean
```

## Troubleshooting
- Packaging may warn about missing code block language tags; add language tags or switch closing fences to ` ``` ` (with a space) to satisfy the quality checker.
- If enhancement fails due to CLI availability, ensure `codex` or `gemini` is installed and on PATH.

## License
See upstream dependencies (Skill Seekers) for licensing details.
