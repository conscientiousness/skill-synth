# Skillseekers-Docs - Community

**Pages:** 4

---

## Future Releases Roadmap | Skill Seekers Docs

**URL:** https://skillseekersweb.com/docs/community/future-releases

**Contents:**
- Future Releases Roadmap
- Release Philosophy
- ✅ Release: v2.1.0 (Released: November 29, 2025)
  - Completed Features
    - Testing & Quality
- Release: v2.2.0 (Estimated: Q1 2026)
  - Planned Features
    - Community & Documentation
    - Enhancements
    - Performance

This document outlines planned features, improvements, and the vision for upcoming releases of Skill Seekers.

We follow semantic versioning (MAJOR.MINOR.PATCH) and maintain backward compatibility wherever possible. Each release focuses on delivering value to users while maintaining code quality and test coverage.

Focus: Test Coverage & Quality Improvements

Focus: Web Presence & Community Growth

GitHub Pages website (skillseekersweb.com)

Plugin system foundation

Support for additional documentation formats

Improved caching strategies

Focus: Developer Experience & Integrations

Web UI for config generation

CI/CD integration examples

Docker containerization

REST API documentation formats

Real-time documentation monitoring

Multi-language documentation

Collaborative skill curation

Semantic understanding

Features are prioritized based on:

See our Flexible Roadmap for:

Pick any task and submit a PR! See Contributing Guide for guidelines.

We aim for predictable releases:

Have questions about the roadmap or want to suggest a feature?

Together, we’re building the future of documentation-to-AI skill conversion! 🚀

---

## Changelog | Skill Seekers Docs

**URL:** https://skillseekersweb.com/docs/community/changelog

**Contents:**
- Changelog
- Unreleased
  - Added
  - Changed
  - Fixed
  - Removed
- [2.7.0] - 2026-01-18
  - 🔐 Smart Rate Limit Management & Multi-Token Configuration
  - Added
  - Changed

All notable changes to Skill Seeker will be documented in this file.

The format is based on Keep a Changelog, and this project adheres to Semantic Versioning.

This minor feature release introduces intelligent GitHub rate limit handling, multi-profile token management, and comprehensive configuration system. Say goodbye to indefinite waits and confusing token setup!

🎯 Multi-Token Configuration System - Flexible GitHub token management with profiles

🧙 Interactive Configuration Wizard - Beautiful terminal UI for easy setup

🚦 Smart Rate Limit Handler - Intelligent GitHub API rate limit management

📦 Resume Command - Resume interrupted scraping jobs

⚙️ CLI Enhancements - New flags and improved UX

🧪 Comprehensive Test Suite - Full test coverage for new features

🎯 Bootstrap Skill Feature - Self-hosting capability (PR #249)

🔧 MCP Now Optional - User choice for installation profile

🧪 E2E Testing for Bootstrap - Comprehensive end-to-end tests

📚 Comprehensive Documentation Overhaul - Complete v2.7.0 documentation update

📦 Git Submodules for Configuration Management - Improved config organization and API deployment

🔍 Config Discovery Enhancements - Improved config listing

GitHub Fetcher - Integrated rate limit handler

GitHub Scraper - Added rate limit support

Main CLI - Enhanced with new commands

pyproject.toml - New entry points and dependency restructuring

install_skill.py - Lazy MCP loading

Code Quality Improvements - Fixed all 21 ruff linting errors across codebase

Version Synchronization - Fixed version mismatch across package (Issue #248)

Case-Insensitive Regex in Install Workflow - Fixed install workflow failures (Issue #236)

Test Fixture Error - Fixed pytest fixture error in bootstrap skill tests

MCP Setup Modernization - Updated MCP server configuration (PR #252, @MiaoDX)

Rate limit indefinite wait - No more infinite waiting

Token setup confusion - Clear, guided setup process

CI/CD failures - Non-interactive mode support

AttributeError in codebase_scraper.py - Fixed incorrect flag check (PR #249)

Existing users - No migration needed! Everything works as before.

MCP users - If you use MCP integration features:

New installation profiles:

None - this release is fully backward compatible.

This minor feature release completes the C3.x codebase analysis suite with standalone SKILL.md generation for codebase scraper, adds comprehensive documentation reorganization, and includes quality-of-life improvements for setup and testing.

This patch release improves the packaging configuration by switching from manual package listing to automatic package discovery.

This patch release fixes a critical packaging bug that made v2.5.0 completely unusable for PyPI users.

This major feature release adds complete multi-platform support for Claude AI, Google Gemini, OpenAI ChatGPT, and Generic Markdown export.

This major release upgrades the MCP infrastructure to the 2025 specification with support for 5 AI coding agents.

This release adds automatic skill installation to 10+ AI coding agents with a single command.

This major release adds git-based config sources, enabling teams to fetch configs from private/team repositories.

This release significantly improves GitHub repository scraping with unlimited local analysis.

This release focuses on quality and reliability improvements.

Skill Seekers is now available on PyPI! Install with: pip install skill-seekers

Major enhancement to PDF extraction capabilities.

Major improvements to documentation scraping.

This is the first production-ready release with complete feature set.

**Examples:**

Example 1 (markdown):
```markdown
# Reinstall with MCP support
pip install -U skill-seekers[mcp]

# Or install everything
pip install -U skill-seekers[all]
```

Example 2 (markdown):
```markdown
# CLI only (no MCP)
pip install skill-seekers

# With MCP integration
pip install skill-seekers[mcp]

# With multi-LLM support (Gemini, OpenAI)
pip install skill-seekers[all-llms]

# Everything
pip install skill-seekers[all]

# See all options
skill-seekers-setup
```

Example 3 (sql):
```sql
# Set up GitHub token (one-time)
skill-seekers config --github

# Add multiple profiles
skill-seekers config
# → Select "1. GitHub Token Setup"
# → Select "1. Add New Profile"

# Use specific profile
skill-seekers github --repo owner/repo --profile work

# CI/CD mode
skill-seekers github --repo owner/repo --non-interactive

# View configuration
skill-seekers config --show

# Bootstrap skill-seekers as a Claude Code skill
./scripts/bootstrap_skill.sh
cp -r output/skill-seekers ~/.claude/skills/
```

---

## Skill Seekers Development Roadmap | Skill Seekers Docs

**URL:** https://skillseekersweb.com/docs/community/roadmap

**Contents:**
- Skill Seeker Development Roadmap
- Vision
- 🎯 New Approach: Flexible, Incremental Development
- 🎯 Milestones
  - ✅ v1.0 - Production Release (COMPLETED - Oct 19, 2025)
    - Core Features ✅
    - MCP Integration ✅
    - Large Documentation Support ✅
    - Auto-Upload Feature ✅
- 📋 Task Categories (Flexible Development)

Transform Skill Seeker into the easiest way to create Claude AI skills from any knowledge source - documentation websites, PDFs, codebases, GitHub repos, Office docs, and more - with both CLI and MCP interfaces.

Philosophy: Small tasks → Pick one → Complete → Move on

Instead of rigid milestones, we now use a flexible task-based approach:

See: Flexible Roadmap for the complete task list!

Released: October 19, 2025 | Tag: v1.0.0

See Flexible Roadmap for detailed task breakdown.

Goal: Create professional website and community presence Timeline: November 2025 (Due: Nov 3, 2025)

Goal: Address technical debt and performance Timeline: Late November 2025

Technical Enhancements:

Goal: Smart defaults and auto-configuration Timeline: December 2025

Goal: Build ecosystem around skill generation

See Contributing Guide for:

Last Updated: October 20, 2025

**Examples:**

Example 1 (sql):
```sql
User: "Create skill from https://tailwindcss.com/docs"
Tool: Auto-detects Tailwind, uses template, generates in 30 seconds
```

---

## Contributing to Skill Seekers | Skill Seekers Docs

**URL:** https://skillseekersweb.com/docs/community/contributing

**Contents:**
- Contributing to Skill Seekers
- Table of Contents
- Branch Workflow
  - Branch Structure
  - Branches
  - Workflow Example
- Code of Conduct
- How Can I Contribute?
  - Reporting Bugs
  - Suggesting Enhancements

First off, thank you for considering contributing to Skill Seekers! It’s people like you that make Skill Seekers such a great tool.

⚠️ IMPORTANT: Skill Seekers uses a two-branch workflow.

main - Production branch

development - Integration branch

Feature branches - Your work

This project and everyone participating in it is governed by our commitment to fostering an open and welcoming environment. Please be respectful and constructive in all interactions.

Before creating bug reports, please check the existing issues to avoid duplicates.

When creating a bug report, include:

Enhancement suggestions are tracked as GitHub issues.

We welcome new framework configurations! To add one:

We actively welcome your pull requests!

⚠️ IMPORTANT: All PRs must target the development branch, not main.

Fork and clone the repository

Create a feature branch from development

Create a Pull Request

We follow PEP 8 with some modifications:

Releases are managed by maintainers:

Contributors will be recognized in:

Thank you for contributing to Skill Seekers! 🎉

**Examples:**

Example 1 (unknown):
```unknown
main (production)
  ↑
  │ (only maintainer merges)
  │
development (integration) ← default branch for PRs
  ↑
  │ (all contributor PRs go here)
  │
feature branches
```

Example 2 (sql):
```sql
# 1. Fork and clone
git clone https://github.com/YOUR_USERNAME/Skill_Seekers.git
cd Skill_Seekers

# 2. Add upstream
git remote add upstream https://github.com/yusufkaraaslan/Skill_Seekers.git

# 3. Create feature branch from development
git checkout development
git pull upstream development
git checkout -b my-feature

# 4. Make changes, commit, push
git add .
git commit -m "Add my feature"
git push origin my-feature

# 5. Create PR targeting 'development' branch
```

Example 3 (json):
```json
**Bug:** MCP tool fails when config has no categories

**Steps to Reproduce:**
1. Create config with empty categories: `"categories": {}`
2. Run `skill-seekers scrape --config configs/test.json`
3. See error

**Expected:** Should use auto-inferred categories
**Actual:** Crashes with KeyError

**Environment:**
- OS: Ubuntu 22.04
- Python: 3.10.5
- Version: v2.7.0
```

Example 4 (json):
```json
**Add Svelte Documentation Config**

Adds configuration for Svelte documentation (https://svelte.dev/docs).

- Config: `configs/svelte.json`
- Tested with max_pages: 100
- Successfully categorized: getting_started, components, api, advanced
- Total pages available: ~150
```

---
