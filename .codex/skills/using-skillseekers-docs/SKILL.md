---
name: using-skillseekers-docs
description: "Provides guidance for Skill Seekers documentation workflows: setup, scraping, enhancement, packaging, and CLI usage."
---

# Using Skill Seekers Docs Skill

Use this skill to navigate and apply Skill Seekers documentation across CLI, manual, reference, community, and tutorial sources. It consolidates official docs for scraping, enhancement, packaging, upload workflows, and MCP integration.

## Sources and Synthesis (Multi-Source)

This skill synthesizes multiple documentation sources (all labeled "unknown" in the ingestion but derived from official Skill Seekers docs):
- **CLI docs** (commands, options, and end-to-end workflows)
- **Manual docs** (MCP setup, codebase analysis/C3.x)
- **Reference docs** (skill file format, packaging structure, large-doc handling, config sources)
- **Community docs** (roadmap, changelog, contributing)
- **Tutorials** (step-by-step learning paths)
- **Index** (navigation map across categories)

**Agreements across sources (high confidence):**
- The core workflow is consistent: **scrape → enhance → package → upload**.
- Packaging targets include **Claude (default), Gemini, OpenAI, and generic Markdown**.
- MCP integration exposes a tool suite for scraping, packaging, enhancing, and config management.

**Noted differences (contextual, not contradictions):**
- Community pages discuss release milestones (e.g., v2.1.0 released, v2.2.0 planned), while the technical reference mentions **v2.6.0**. Treat community versions as roadmap context, and rely on the **Reference/CLI docs** for current technical behavior.

**Source priority when guidance conflicts:**
1. Code patterns / codebase analysis (none included in this skill)
2. Official documentation (reference/manual/cli/tutorials)
3. Community pages (roadmap, changelog)
4. Anything else

## When to Use This Skill

Trigger this skill when you need to:
- **Scrape documentation** into a Skill Seekers skill (configs, presets, URLs, PDFs).
- **Enhance, package, or upload** skills for Claude, Gemini, OpenAI, or Markdown.
- **Set up MCP** to access Skill Seekers tools inside Claude Code, Cursor, or other agents.
- **Handle large docs** with auto-splitting, routers, or multi-skill packaging.
- **Work with Git-based config sources** or validate/configure scraping.
- **Use C3.x codebase analysis** features or extract patterns/tests from repositories.

Concrete trigger phrases:
- “Package this skill for Claude/Gemini/OpenAI”
- “Set up MCP tools for Skill Seekers”
- “Scrape docs from this URL into a skill”
- “Split large docs into multiple skills / build a router skill”
- “Add a git config source / list configs / validate config”

## Key Concepts

- **Skill structure**: A skill is centered on `SKILL.md` with optional `references/`, `scripts/`, and `assets/`. Packaging creates a platform-specific archive.
- **Core workflow**: `scrape` creates the skill content, `enhance` improves SKILL.md, `package` builds platform archives, `upload` sends them to LLM platforms.
- **Targets**: `--target` determines the output format (Claude, Gemini, OpenAI, Markdown). Each platform expects a specific archive format.
- **MCP server**: Exposes Skill Seekers functionality via Model Context Protocol tools for agent integrations.
- **C3.x**: AST-driven codebase analysis for design patterns, tests, tutorials, and architecture extraction.
- **Routers & auto-splitting**: For large docs, split into sub-skills and generate router skills to route queries across them.

## Quick Reference (Practical Examples)

Each example is a real snippet from the official docs (CLI/Manual/Reference).

**1) End-to-end pipeline (CLI overview)**
```bash
# 1. Scrape documentation
skill-seekers scrape --config configs/react.json

# 2. Enhance with AI
skill-seekers enhance output/react/

# 3. Package for platform
skill-seekers package output/react/ --target claude

# 4. Upload to platform
skill-seekers upload output/react.zip
```

**2) Package for multiple platforms (CLI package)**
```bash
# Package for Claude (default)
skill-seekers package output/react/

# Package for specific platforms
skill-seekers package output/react/ --target gemini
skill-seekers package output/react/ --target openai
skill-seekers package output/react/ --target markdown
```

**3) Upload with explicit target (CLI upload)**
```bash
# Upload to Claude (default)
skill-seekers upload output/react.zip

# With explicit target
export ANTHROPIC_API_KEY=sk-ant-...
skill-seekers upload output/react.zip --target claude
```

**4) PDF extraction (CLI pdf)**
```bash
# Basic PDF extraction
skill-seekers pdf --pdf docs/manual.pdf --name myskill

# Scanned PDFs with OCR
skill-seekers pdf --pdf docs/scanned.pdf --name myskill --ocr
```

**5) Add a git-based config source (Reference: git-config-sources)**
```bash
# Add git repository as config source
skill-seekers add-git-source \
  https://github.com/your-org/scraping-configs.git \
  --name company-configs

# Private repo with authentication
skill-seekers add-git-source \
  https://github.com/your-org/private-configs.git \
  --name private-configs
```

**6) Auto-split large docs + router (Reference: large-documentation)**
```bash
# Automatic splitting at 50K tokens per skill
skill-seekers scrape --config configs/large-docs.json \
  --auto-split \
  --max-tokens 50000 \
  --output output/large-docs/

# Creates:
# output/large-docs-part1/
# output/large-docs-part2/
# output/large-docs-part3/
# output/large-docs-router/
```

**7) Router for multiple doc subsets (Reference: large-documentation)**
```bash
# 1. Split by category
skill-seekers scrape --config configs/k8s-concepts.json --output output/k8s-concepts/
skill-seekers scrape --config configs/k8s-tasks.json --output output/k8s-tasks/
skill-seekers scrape --config configs/k8s-api.json --output output/k8s-api/

# 2. Create router
skill-seekers router \
  output/k8s-concepts/ \
  output/k8s-tasks/ \
  output/k8s-api/ \
  --output output/k8s-router/ \
  --name kubernetes-complete
```

**8) MCP quick start (Manual: MCP setup)**
```bash
# Clone repository
git clone https://github.com/yusufkaraaslan/Skill_Seekers.git
cd Skill_Seekers

# Run setup script
./setup_mcp.sh
```

**9) Minimal scrape config (Reference: large-documentation)**
```json
{
  "name": "kubernetes-concepts",
  "base_url": "https://kubernetes.io/docs/concepts/",
  "url_patterns": {
    "include": ["concepts"],
    "exclude": []
  },
  "max_pages": 500
}
```

## Reference Files (What to Read and When)

All reference files below are **unknown source type** with **medium confidence**, but they are consistent with official Skill Seekers documentation. Use them as the primary source of truth unless you have codebase evidence.

- **`references/index.md`** — *Index / Navigation*. Lists categories and file mapping. Start here to choose the right reference file.
- **`references/cli.md`** — *CLI Commands & Options*. Use for `package`, `upload`, `pdf`, and other CLI workflows.
- **`references/manual.md`** — *Setup & Advanced Features*. MCP setup, tool list, and C3.x codebase analysis overview.
- **`references/reference.md`** — *Technical Reference*. Skill file format, package structure, large-doc handling, config schema, git config sources.
- **`references/community.md`** — *Roadmap & Changelog*. Release philosophy, planned features, and community guidance.
- **`references/tutorials.md`** — *Learning Paths*. Step-by-step guides and practical walkthroughs.

## Working with This Skill

### For Beginners
- Start with `references/index.md` to pick the right category.
- Read `references/tutorials.md` for guided workflows and baseline concepts.
- Use the **end-to-end pipeline** in the Quick Reference to get your first skill built.

### For Intermediate Users
- Use `references/cli.md` to fine-tune options (targets, PDF extraction, presets).
- Use `references/reference.md` for config schema and large-document handling.
- Use git config sources when you need shared org-level scraping configs.

### For Advanced Users
- Use `references/manual.md` for MCP setup and tool-based integration.
- Apply C3.x analysis when scraping codebases with AST-level insights.
- Build router skills to manage large doc sets or multiple sources.

### Navigation & Conflict Resolution
- If two sources differ, prioritize **reference/manual/cli** over **community**.
- Treat roadmap/changelog as intent, not authoritative behavior.
- When uncertain, validate by running the CLI command (e.g., `skill-seekers --help` or the specific subcommand help).

## Updating This Skill

To refresh with the latest documentation:
1. Re-run the Skill Seekers scraper with the same config(s).
2. Rebuild the skill output folder and re-package as needed.
3. Re-check the reference files for changes in CLI flags or package formats.
