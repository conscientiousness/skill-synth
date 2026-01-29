# Skillseekers-Docs - Tutorials

**Pages:** 11

---

## Installation | Skill Seekers Docs

**URL:** https://skillseekersweb.com/docs/getting-started/installation

**Contents:**
- Installation Guide
- Prerequisites
- Method 1: Install via PyPI (Recommended)
- Method 2: Install from Source
  - Step 1: Install Python (5 minutes)
    - Check if You Already Have Python
  - Step 2: Install Git (3 minutes)
  - Step 3: Clone and Install (2 minutes)
- Set Up API Keys
  - For Claude (Anthropic)

Time: 15-30 minutes total (including all installations)

Result: Working Skill Seekers installation ready to create your first Claude skill

Before starting, you need:

The easiest way to install Skill Seekers is through PyPI:

For development or the latest features:

✅ If you see: Python 3.10.x or higher → Skip to Step 2!

Linux (Ubuntu/Debian):

✅ If you see: git version 2.x.x → Skip to Step 3!

Windows: Download from: https://git-scm.com/download/win

Skill Seekers can enhance skills using AI. Set up your API key:

Make it permanent (optional):

Add the export command to your shell profile (~/.bashrc, ~/.zshrc, or ~/.bash_profile):

Make sure pip’s bin directory is in your PATH:

Install using pip instead of python:

**Examples:**

Example 1 (go):
```go
# Install base package
pip install skill-seekers

# Or install with specific LLM platform support
pip install skill-seekers[gemini]  # For Google Gemini
pip install skill-seekers[openai]  # For OpenAI ChatGPT
pip install skill-seekers[all]     # For all platforms
```

Example 2 (markdown):
```markdown
skill-seekers --version
# Should show: skill-seekers 2.7.0 or higher
```

Example 3 (unknown):
```unknown
python3 --version
```

Example 4 (markdown):
```markdown
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python3
```

---

## Tutorial: Scraping Documentation | Skill Seekers Docs

**URL:** https://skillseekersweb.com/docs/tutorials/scraping-docs

**Contents:**
- Tutorial: Scraping Documentation
- What You’ll Learn
- Prerequisites
- Step 1: Choose a Documentation Site
- Step 2: Estimate Page Count
- Step 3: Scrape the Documentation
- Step 4: Review the Skill
- Step 5: Enhance with AI (Optional)
- Step 6: Package the Skill
- Step 7: Upload to AI Assistant

Learn how to scrape any documentation website and create an AI skill in this hands-on tutorial.

Time: 15 minutes | Level: Beginner | Result: Working React docs skill

For this tutorial, we’ll scrape React documentation. Skill Seekers includes 24 preset configs for popular frameworks.

View available presets:

Before scraping, estimate how many pages will be processed:

Run the scraper with the React preset:

Check what was created:

Transform the skill from basic (3/10) to comprehensive (9/10) using AI:

Option A: Local Enhancement (FREE with Claude Max)

This opens Claude Code in a new terminal and enhances the skill using your Claude Max subscription (no API costs!).

Option B: API Enhancement (Fast)

Package for your preferred platform:

Automatic Upload (Recommended):

Try these prompts in Claude:

Result: Claude responds with accurate, context-aware answers based on official React documentation!

Solution: Check your config selectors:

Interactive mode shows extracted content and lets you test selectors.

You just created your first AI skill! 🎉

Time investment: 15 minutes Result: Professional-quality AI skill ready to use!

**Examples:**

Example 1 (unknown):
```unknown
skill-seekers list-configs
```

Example 2 (markdown):
```markdown
Available configs:
- react.json        (React documentation)
- vue.json          (Vue.js documentation)
- django.json       (Django framework)
- godot.json        (Godot game engine)
- fastapi.json      (FastAPI framework)
... and 19 more
```

Example 3 (unknown):
```unknown
skill-seekers estimate --config configs/react.json
```

Example 4 (json):
```json
📊 Estimation Results:
Base URL: https://react.dev/learn
Estimated pages: ~180 pages
Estimated time: 3-5 minutes
Categories detected: 4
```

---

## Overview | Skill Seekers Docs

**URL:** https://skillseekersweb.com/docs/getting-started/overview/

**Contents:**
- What is Skill Seekers?
- Why Use Skill Seekers?
- Quick Example
- Key Capabilities
  - Multi-Source Support
  - Three-Stream Architecture (v2.6.0)
  - C3.x Codebase Analysis (v2.6.0)
  - Multi-Platform Export
  - Intelligent Processing
- What’s New in v2.7.0

Skill Seekers is an automated tool that transforms documentation websites, GitHub repositories, and PDF files into production-ready Claude AI skills. Instead of manually reading and summarizing documentation, Skill Seekers:

Result: Get comprehensive Claude skills for any framework, API, or tool in 20-40 minutes instead of hours of manual work.

That’s it! You now have a comprehensive Astro skill in Claude.

Smart Rate Limit Management & Multi-Token Configuration:

Self-Hosting & Bootstrap Feature:

Enhanced Testing & Quality:

Read the full v2.7.0 changelog →

**Examples:**

Example 1 (go):
```go
# Install
pip install skill-seekers

# Scrape documentation
skill-seekers scrape https://docs.astro.build/en/getting-started/

# Package for Claude
skill-seekers package output/astro/

# Upload to Claude
skill-seekers upload astro.zip
```

---

## Tutorial: Analyzing GitHub Repositories | Skill Seekers Docs

**URL:** https://skillseekersweb.com/docs/tutorials/analyzing-github

**Contents:**
- Tutorial: Analyzing GitHub Repositories
- What You’ll Learn
- Step 1: Basic GitHub Scraping
- Step 2: Add Local Analysis (Unlimited!)
- Step 3: Review Generated Files

Learn how to analyze GitHub repositories and generate comprehensive codebase documentation with C3.x analysis.

Time: 20 minutes | Level: Intermediate | Result: Complete codebase skill with patterns, examples, and architecture

See: GitHub Analysis Manual for complete details.

**Examples:**

Example 1 (unknown):
```unknown
skill-seekers github \
  --repository facebook/react \
  --output output/react-repo/
```

Example 2 (markdown):
```markdown
# Clone repo locally first
git clone https://github.com/facebook/react.git /tmp/react

# Analyze with C3.x features
skill-seekers github \
  --repository facebook/react \
  --local-repo-path /tmp/react \
  --output output/react-complete/
```

Example 3 (unknown):
```unknown
output/react-complete/
├── SKILL.md
├── ARCHITECTURE.md              # NEW: Comprehensive overview
├── references/
│   ├── api_reference.md
│   ├── dependencies.md
│   └── codebase_analysis/
│       ├── patterns/            # Design patterns detected
│       ├── examples/            # Test examples extracted
│       ├── guides/              # How-to tutorials generated
│       └── configuration/       # Config files analyzed
```

---

## Overview | Skill Seekers Docs

**URL:** https://skillseekersweb.com/docs/getting-started/overview

**Contents:**
- What is Skill Seekers?
- Why Use Skill Seekers?
- Quick Example
- Key Capabilities
  - Multi-Source Support
  - Three-Stream Architecture (v2.6.0)
  - C3.x Codebase Analysis (v2.6.0)
  - Multi-Platform Export
  - Intelligent Processing
- What’s New in v2.7.0

Skill Seekers is an automated tool that transforms documentation websites, GitHub repositories, and PDF files into production-ready Claude AI skills. Instead of manually reading and summarizing documentation, Skill Seekers:

Result: Get comprehensive Claude skills for any framework, API, or tool in 20-40 minutes instead of hours of manual work.

That’s it! You now have a comprehensive Astro skill in Claude.

Smart Rate Limit Management & Multi-Token Configuration:

Self-Hosting & Bootstrap Feature:

Enhanced Testing & Quality:

Read the full v2.7.0 changelog →

**Examples:**

Example 1 (go):
```go
# Install
pip install skill-seekers

# Scrape documentation
skill-seekers scrape https://docs.astro.build/en/getting-started/

# Package for Claude
skill-seekers package output/astro/

# Upload to Claude
skill-seekers upload astro.zip
```

---

## How to Submit a Config | Skill Seekers Docs

**URL:** https://skillseekersweb.com/docs/guides/submit-config

**Contents:**
- How to Submit a Config
- Overview
- Submission Process
  - 1. Create Your Config
  - 2. Test Your Config
  - 3. Validate Online
  - 4. Submit to GitHub
    - Method A: Automatic Submission (Recommended)
    - Method B: Manual Submission
- What Happens Next?

Learn how to validate and submit your custom configuration files to the official Skill Seekers config repository.

The Skill Seekers community welcomes configuration contributions for any framework, library, or documentation site. Your configs help other developers quickly create AI skills for their tools.

Create a config file using the unified format:

Before submitting, test your config locally:

Visit skillseekersweb.com/configs and scroll to the validator:

The validator checks:

Once validated, there are two submission methods:

If automatic submission doesn’t work:

Automated Checks (5 minutes)

Manual Review (24-48 hours)

Your config will be approved if it:

✅ Validates without errors ✅ Scrapes successfully ✅ Extracts meaningful content ✅ Follows naming conventions ✅ Doesn’t duplicate existing configs ✅ Has accurate selectors ✅ Respects rate limits

Common Rejection Reasons: ❌ Invalid JSON syntax ❌ Missing required fields ❌ Incorrect selectors (no content extracted) ❌ Duplicate of existing config ❌ Rate limit too aggressive ❌ Broken or inaccessible URLs

Configs are organized into categories in the gallery:

React, Vue, Angular, Svelte, Astro, etc.

Django, FastAPI, Express, Laravel, Rails, etc.

Godot, Unity, Unreal, etc.

Kubernetes, Docker, Ansible, Terraform, etc.

Git, VS Code, Claude Code, etc.

React Native, Flutter, Ionic, etc.

TensorFlow, PyTorch, Pandas, etc.

Jest, Pytest, Cypress, Playwright, etc.

Where does your config fit? Mention the category in your submission for faster processing.

When submitting configs with multiple sources:

Explain in submission:

For private documentation or internal tools:

We’ll approve the structure even if we can’t test the scraping.

For sites with 500+ pages:

Browse 27+ preset configs for inspiration:

Contributors are recognized in:

Top contributors get:

Before submitting, ensure:

Questions? Open a GitHub Discussion or Issue.

**Examples:**

Example 1 (json):
```json
{
  "name": "your-framework",
  "description": "Complete framework knowledge combining docs and codebase.",
  "merge_mode": "rule-based",
  "sources": [
    {
      "type": "documentation",
      "base_url": "https://docs.yourframework.com",
      "selectors": {
        "main_content": "article",
        "title": "h1",
        "code_blocks": "pre code"
      },
      "rate_limit": 0.5,
      "max_pages": 200
    }
  ]
}
```

Example 2 (markdown):
```markdown
# Validate the config structure
skill-seekers validate configs/your-framework.json

# Test scraping
skill-seekers scrape configs/your-framework.json

# Check the output
ls output/your-framework/
```

Example 3 (json):
```json
{
  "name": "advanced-framework",
  "description": "Complete knowledge from docs, GitHub, and PDF manual.",
  "merge_mode": "rule-based",
  "sources": [
    {
      "type": "documentation",
      "base_url": "https://docs.framework.com"
    },
    {
      "type": "github",
      "repo": "company/framework",
      "enable_codebase_analysis": true,
      "code_analysis_depth": "deep"
    },
    {
      "type": "pdf",
      "path": "https://framework.com/manual.pdf"
    }
  ]
}
```

Example 4 (json):
```json
{
  "max_pages": 500,
  "rate_limit": 1.0,
  "url_patterns": {
    "include": ["/getting-started/", "/api/", "/guides/"],
    "exclude": ["/blog/", "/changelog/", "/community/"]
  }
}
```

---

## Tutorial: Multi-Source Skills | Skill Seekers Docs

**URL:** https://skillseekersweb.com/docs/tutorials/multi-source-skills

**Contents:**
- Tutorial: Multi-Source Skills (Unified Scraping)
- Why Unified Skills?
- Step 1: Create Unified Config
- Step 2: Run Unified Scraper
- Step 3: Review Conflict Detection
- Step 4: Enhance and Package

Learn how to combine multiple sources (docs + GitHub + PDFs) into one comprehensive skill.

Time: 25 minutes | Level: Advanced | Result: Unified skill with complete knowledge

Problem: Documentation alone doesn’t show real usage. Code alone doesn’t explain concepts. PDFs have specs but no examples.

Solution: Combine all sources into one skill!

Skill Seekers automatically detects and resolves duplicate content:

Result: Complete Django knowledge - concepts, examples, patterns, and specifications - all in one skill!

See: Unified Scraping Manual for advanced techniques.

**Examples:**

Example 1 (json):
```json
{
  "name": "django-complete",
  "sources": [
    {
      "type": "documentation",
      "base_url": "https://docs.djangoproject.com/en/stable/",
      "max_pages": 500,
      "priority": 1
    },
    {
      "type": "github",
      "repository": "django/django",
      "local_repo_path": "/path/to/django",
      "include_issues": true,
      "priority": 2
    },
    {
      "type": "pdf",
      "directory": "/path/to/django-books/",
      "priority": 3
    }
  ],
  "conflict_resolution": "priority"
}
```

Example 2 (unknown):
```unknown
skill-seekers unified \
  --config configs/django-complete.json \
  --output output/django-unified/
```

Example 3 (json):
```json
⚠️ Conflict Detection Report:
- 23 duplicate pages found
- 18 resolved by priority
- 5 merged (complementary content)
✅ Final skill: 892 unique pages
```

Example 4 (go):
```go
# Enhance
skill-seekers enhance output/django-unified/

# Package
skill-seekers package output/django-unified/ --target claude
```

---

## Create Your First Skill | Skill Seekers Docs

**URL:** https://skillseekersweb.com/docs/getting-started/first-skill

**Contents:**
- Create Your First Skill
- What We’ll Build
- Step 1: Check Your Installation
- Step 2: Scrape the Documentation
- Step 3: Review What Was Created
- Step 4: Enhance with AI (Optional)
- Step 5: Package the Skill
- Step 6: Upload to Claude
- Step 7: Test Your Skill
- What You Just Learned

Learn by doing! This tutorial walks you through creating your first AI skill from documentation in just 5 minutes.

Prerequisites: Skill Seekers installed (Installation Guide)

Time: 5 minutes | Result: Working Claude skill ready to upload

We’ll create a skill from Tailwind CSS documentation because it’s:

Final result: A Claude skill that knows Tailwind CSS utilities, components, and best practices.

Make sure Skill Seekers is ready:

You should see something like: Skill Seekers v2.7.0

If not installed: See Installation Guide

Run this single command:

Transform from basic (3/10) to comprehensive (9/10):

Option A: Local Enhancement (FREE with Claude Max)

Uses your Claude Max subscription - no API costs!

Option B: API Enhancement (Fast)

What enhancement does:

Package for Claude AI:

Try these prompts in Claude:

Result: Claude responds with accurate, context-aware answers based on official Tailwind documentation!

Time investment: 5 minutes (10-15 with enhancement)

Result: Production-quality AI skill ready to use!

Now that you know the basics, try:

Skill Seekers includes 24 presets for popular frameworks:

Add code analysis to your skills:

See: Analyzing GitHub Tutorial

Turn technical PDFs into searchable skills:

See: Extracting PDFs Tutorial

Combine docs + GitHub + PDFs:

See: Multi-Source Tutorial

Problem: Scraper couldn’t find content

Solution: Use interactive mode to test selectors:

Full troubleshooting: Troubleshooting Guide

Your typical workflow:

Questions? Open an issue: https://github.com/yusufkaraaslan/Skill_Seekers/issues

**Examples:**

Example 1 (unknown):
```unknown
skill-seekers --version
```

Example 2 (unknown):
```unknown
skill-seekers scrape https://tailwindcss.com/docs/installation --max-pages 50
```

Example 3 (json):
```json
🔍 Checking for llms.txt...
📥 Scraping documentation...
   ├─ Page 1/50: Installation
   ├─ Page 2/50: Editor Setup
   ├─ Page 3/50: Utility-First Fundamentals
   ...
   └─ Page 50/50: Plugin API

✅ Skill created: output/tailwindcss/SKILL.md
📊 Statistics:
   - Pages: 50
   - Code examples: 127
   - Categories: 8
   - Time: 45 seconds
```

Example 4 (unknown):
```unknown
ls output/tailwindcss/
```

---

## Troubleshooting Guide | Skill Seekers Docs

**URL:** https://skillseekersweb.com/docs/guides/troubleshooting

**Contents:**
- Troubleshooting Guide
- Installation Issues
  - Python Not Found
  - Module Not Found
  - Permission Denied
- Runtime Issues
  - File Not Found
  - Config File Not Found
- MCP Setup Issues
  - MCP Server Not Loading

Common issues and solutions when using Skill Seeker.

Check if Python is installed:

Use python instead of python3:

Install dependencies:

Use —user flag if permission denied:

Check pip is working:

Use sudo (not recommended):

Use virtual environment (best practice):

Check you’re in the Skill_Seekers directory:

Change to the correct directory:

Create missing config:

Check configuration file:

Verify paths are ABSOLUTE (not placeholders):

❌ Bad: $REPO_PATH or /path/to/Skill_Seekers ✅ Good: /Users/john/Projects/Skill_Seekers

Test server manually:

RESTART Claude Code completely:

Problem: Config has $REPO_PATH or /Users/username/ instead of real paths

Check working directory:

Test CLI tools directly:

Check network connection:

Use smaller max_pages for testing:

Increase rate_limit in config:

Problem: Pages scraped but content is empty

Check selector in config:

Verify website is accessible:

Try different selectors:

Issue: Can’t run ./setup_mcp.sh

Issue: Homebrew not installed

Issue: pip3 not found

Issue: Permission errors

Issue: Python not in PATH

Issue: Line ending errors

Use these to check your setup:

If none of these solutions work:

Check existing issues: https://github.com/yusufkaraaslan/Skill_Seekers/issues

Open a new issue with:

Include this debug info:

Still stuck? Open an issue: https://github.com/yusufkaraaslan/Skill_Seekers/issues/new

**Examples:**

Example 1 (yaml):
```yaml
python3: command not found
```

Example 2 (unknown):
```unknown
which python3
python --version  # Try without the 3
```

Example 3 (unknown):
```unknown
python cli/doc_scraper.py --help
```

Example 4 (julia):
```julia
ModuleNotFoundError: No module named 'requests'
ModuleNotFoundError: No module named 'bs4'
ModuleNotFoundError: No module named 'mcp'
```

---

## Tutorial: Extracting PDFs | Skill Seekers Docs

**URL:** https://skillseekersweb.com/docs/tutorials/extracting-pdfs

**Contents:**
- Tutorial: Extracting PDFs
- Basic PDF Extraction
- OCR for Scanned PDFs
- Password-Protected PDFs
- Extract Tables
- Parallel Processing (3x Faster)

Learn how to extract technical documentation from PDFs and create searchable AI skills.

Time: 10 minutes | Level: Beginner | Result: PDF-based skill

See: PDF Scraping Manual for complete guide.

**Examples:**

Example 1 (unknown):
```unknown
skill-seekers pdf \
  --input /path/to/manual.pdf \
  --output output/manual/
```

Example 2 (markdown):
```markdown
# Install Tesseract first
# Ubuntu: sudo apt-get install tesseract-ocr
# macOS: brew install tesseract

skill-seekers pdf \
  --input /path/to/scanned.pdf \
  --output output/scanned/ \
  --ocr
```

Example 3 (unknown):
```unknown
skill-seekers pdf \
  --input /path/to/encrypted.pdf \
  --output output/encrypted/ \
  --password "your-password"
```

Example 4 (unknown):
```unknown
skill-seekers pdf \
  --input /path/to/spec.pdf \
  --output output/spec/ \
  --extract-tables
```

---

## Tutorial: Creating Custom Configs | Skill Seekers Docs

**URL:** https://skillseekersweb.com/docs/tutorials/creating-configs

**Contents:**
- Tutorial: Creating Custom Configs
- Interactive Config Creation
- Manual Config Creation
- Test Your Config
- Share Your Config

Learn how to create custom configuration files for documentation websites not covered by presets.

Time: 15 minutes | Level: Intermediate | Result: Working custom config

The easiest way to create a config:

Create configs/my-framework.json:

See: Config Format Reference for all available options.

**Examples:**

Example 1 (unknown):
```unknown
skill-seekers scrape --interactive
```

Example 2 (json):
```json
{
  "name": "my-framework",
  "base_url": "https://docs.my-framework.com/",
  "selectors": {
    "content": "article.documentation",
    "title": "h1.page-title",
    "code": "pre code"
  },
  "url_patterns": [
    "^https://docs.my-framework.com/guide/",
    "^https://docs.my-framework.com/api/"
  ],
  "exclude_patterns": [
    "/changelog/",
    "/blog/"
  ],
  "max_pages": 200,
  "rate_limit": 0.5
}
```

Example 3 (markdown):
```markdown
# Estimate page count
skill-seekers estimate --config configs/my-framework.json

# Test on first 10 pages
skill-seekers scrape \
  --config configs/my-framework.json \
  --max-pages 10 \
  --output output/test/
```

Example 4 (markdown):
```markdown
# Submit to community
skill-seekers submit-config \
  --config configs/my-framework.json \
  --description "My Framework documentation config"
```

---
