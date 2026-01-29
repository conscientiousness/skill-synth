# Skillseekers-Docs - Manual

**Pages:** 4

---

## MCP Setup | Skill Seekers Docs

**URL:** https://skillseekersweb.com/docs/manual/mcp/setup

**Contents:**
- MCP Setup Guide
- Overview
- Quick Start
  - One-Command Setup (Recommended)
- Supported Agents
- Manual Installation
  - Step 1: Install Dependencies
  - Step 2: Test the Server
  - Step 3: Configure Your Agent
    - For Claude Code (stdio)

Set up the Skill Seekers MCP server to use all features through Model Context Protocol with Claude Code and other AI coding agents.

The Skill Seekers MCP server provides 18 tools accessible through the Model Context Protocol, enabling natural language interaction with all Skill Seekers features.

The script automatically:

Note: Paths shown are for macOS. Linux and Windows paths detected automatically.

If you prefer manual setup or the script doesn’t work:

Edit ~/Library/Application Support/Claude/mcp.json:

Edit ~/Library/Application Support/Cursor/mcp_settings.json:

Note: For HTTP-based agents, start the server first:

Best for: Claude Code, VS Code + Cline

Best for: Cursor, Windsurf, IntelliJ IDEA

When running in HTTP mode:

generate_config - Generate config for any documentation site

list_configs - List all available preset configurations

validate_config - Validate config file structure

estimate_pages - Estimate page count before scraping

scrape_docs - Scrape documentation and build skill

scrape_github - Scrape GitHub repositories

scrape_pdf - Extract content from PDF files

package_skill - Package skill for platform

upload_skill - Upload to LLM platform

enhance_skill - AI-enhance SKILL.md

install_skill - Complete install workflow

fetch_config - Fetch configs from sources

submit_config - Submit new configs

add_config_source - Register private git repositories

list_config_sources - List all registered sources

remove_config_source - Remove registered sources

split_config - Split large documentation configs

generate_router - Generate router/hub skills

In Claude Code, tools appear in the tool use panel when relevant. You can also ask:

The setup script detects all installed agents:

Problem: MCP tools don’t show up in Claude Code

Problem: HTTP server fails to start

Problem: Can’t write to config file

Problem: ModuleNotFoundError: No module named 'mcp'

Problem: Setup script doesn’t detect your agent

Update agent configs to use new port:

Run multiple servers on different ports:

**Examples:**

Example 1 (markdown):
```markdown
# Clone repository
git clone https://github.com/yusufkaraaslan/Skill_Seekers.git
cd Skill_Seekers

# Run setup script
./setup_mcp.sh
```

Example 2 (markdown):
```markdown
# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Skill Seekers with MCP support
pip install -e ".[mcp]"

# Or install MCP dependencies separately
pip install mcp anthropic-mcp fastmcp
```

Example 3 (markdown):
```markdown
# Test stdio mode (default)
python -m skill_seekers.mcp.server_fastmcp

# Should show:
# MCP Server running in stdio mode
# Connected to client...
# (Press Ctrl+C to exit)

# Test HTTP mode
python -m skill_seekers.mcp.server_fastmcp --http --port 3000

# Should show:
# MCP Server running in HTTP mode on http://localhost:3000
# Health check: http://localhost:3000/health
# SSE endpoint: http://localhost:3000/sse
```

Example 4 (json):
```json
{
  "mcpServers": {
    "skill-seeker": {
      "command": "python",
      "args": ["-m", "skill_seekers.mcp.server_fastmcp"]
    }
  }
}
```

---

## C3.x Codebase Analysis | Skill Seekers Docs

**URL:** https://skillseekersweb.com/docs/manual/codebase-analysis/c3x-codebase-analysis

**Contents:**
- C3.x Codebase Analysis
- What is C3.x?
- Supported Languages
- C3.1: Design Pattern Detection
  - Patterns Detected
  - Example Output
  - Real-World Results
- C3.2: Test Example Extraction
  - Why Test Files?
  - Example Output

C3.x is Skill Seekers’ deep codebase analysis system that uses Abstract Syntax Tree (AST) parsing to extract comprehensive knowledge from source code. It goes far beyond simple scraping to understand how code actually works.

C3.x stands for Comprehensive Codebase Context Extraction with 7 analysis modules:

C3.x analyzes code through AST parsing for:

Automatically detects common design patterns in your codebase.

From analyzing fastmcp repository:

Extracts working code examples from test files.

From fastmcp repository:

Generates step-by-step tutorials from code patterns.

Analyzes configuration files to understand setup patterns.

Automatically scans for:

Identifies high-level architecture patterns.

Enable only specific modules:

C3.x uses intelligent caching:

After C3.x analysis, you can enhance with AI:

Use basic mode instead:

Time: 1-2 minutes Gets: File structure, imports, entry points (no C3.x)

**Examples:**

Example 1 (json):
```json
{
  "pattern": "Strategy",
  "confidence": 0.95,
  "location": "src/providers/oauth_provider.py",
  "line_number": 42,
  "context": {
    "interface": "OAuthProvider",
    "implementations": [
      "GoogleProvider",
      "AzureProvider",
      "GitHubProvider"
    ],
    "usage_count": 206
  },
  "explanation": "Strategy pattern allows runtime selection of OAuth provider implementation"
}
```

Example 2 (json):
```json
{
  "title": "OAuth with Google Provider",
  "source": "tests/test_oauth.py:23-45",
  "language": "python",
  "code": "def test_google_oauth():\n    provider = GoogleProvider(\n        client_id='test-id',\n        client_secret='test-secret',\n        redirect_uri='http://localhost:8000/callback'\n    )\n    \n    auth_url = provider.get_authorization_url()\n    assert 'accounts.google.com' in auth_url",
  "description": "Configure Google OAuth provider with credentials and generate authorization URL",
  "category": "authentication",
  "complexity": "medium",
  "confidence": 0.92
}
```

Example 3 (markdown):
```markdown
# How to Implement OAuth Authentication

## Overview
This guide shows how to add OAuth authentication using the Strategy pattern.

## Prerequisites
- Provider credentials (client_id, client_secret)
- Redirect URI configured

## Step 1: Create Provider Instance
\`\`\`python
from fastmcp import GoogleProvider

provider = GoogleProvider(
    client_id="your-client-id",
    client_secret="your-secret",
    redirect_uri="http://localhost:8000/callback"
)
\`\`\`

## Step 2: Generate Authorization URL
\`\`\`python
auth_url = provider.get_authorization_url()
# Redirect user to auth_url
\`\`\`

## Step 3: Handle Callback
\`\`\`python
token = provider.exchange_code(request.params['code'])
user_info = provider.get_user_info(token)
\`\`\`

## Common Issues
- **Redirect URI mismatch:** Ensure URI matches exactly in provider console
- **Invalid credentials:** Double-check client_id and client_secret
```

Example 4 (json):
```json
{
  "file": "config/settings.json",
  "format": "json",
  "structure": {
    "database": {
      "host": "localhost",
      "port": 5432,
      "name": "myapp_db"
    },
    "oauth": {
      "providers": ["google", "github"],
      "redirect_uri": "/auth/callback"
    }
  },
  "security_issues": [
    {
      "severity": "high",
      "issue": "Hardcoded database password",
      "line": 5,
      "recommendation": "Use environment variables"
    }
  ],
  "best_practices": [
    {
      "category": "security",
      "suggestion": "Add secrets rotation policy"
    }
  ]
}
```

---

## AI Enhancement | Skill Seekers Docs

**URL:** https://skillseekersweb.com/docs/manual/enhancement/ai-enhancement

**Contents:**
- AI Enhancement Guide
- Overview
- Quick Start
  - LOCAL Enhancement (Recommended - FREE)
  - API Enhancement (Alternative)
- Enhancement Modes
  - 1. Headless Mode (Default)
  - 2. Background Mode
  - 3. Daemon Mode
  - 4. Terminal Mode (Interactive)

Transform basic SKILL.md files into comprehensive, production-quality documentation using AI enhancement.

The Problem: Auto-generated SKILL.md files are often too generic:

The Solution: Let Claude analyze your reference documentation and create enhanced SKILL.md with:

Uses your Claude Code Max subscription - no API costs!

Time: 30-60 seconds per skill

Uses Anthropic API directly (~$0.15-$0.30 per skill):

Skill Seekers supports 4 enhancement modes for different workflows:

Best for: CI/CD pipelines, automation scripts

Best for: When you want to continue working

Best for: Long-running tasks that must survive parent process exit

Best for: Manual work, debugging

Local Mode (Recommended - No API Key):

Model: Claude Sonnet 4 Format: Maintains YAML frontmatter

Model: Gemini 2.0 Flash Format: Converts to plain markdown (no frontmatter) Output: Updates system_instructions.md

Model: GPT-4o Format: Converts to plain text Output: Updates assistant_instructions.txt

Note: Local mode is FREE and only available for Claude AI.

When using --background or --daemon, a status file is created:

Location: {skill_directory}/.enhancement_status.json

What it does: Skips ALL confirmations, auto-answers “yes” to everything

Default behavior: Force mode is ON by default for maximum automation

Default timeout: 600 seconds (10 minutes)

Adjust based on skill size:

What happens on timeout:

Test Case: steam-economy skill

The enhancement successfully:

Enhancement creates these files:

“claude command not found”

“Enhancement timed out”

“SKILL.md was not updated”

Background task not progressing:

Status file shows error:

“No API key provided”

“No reference files found”

“anthropic package not installed”

Don’t like the result?

Use enhancement when:

Skip enhancement when:

**Examples:**

Example 1 (markdown):
```markdown
# Basic enhancement
skill-seekers enhance output/react/

# With custom timeout
skill-seekers enhance output/react/ --timeout 1200

# Background mode (non-blocking)
skill-seekers enhance output/react/ --background

# Daemon mode (survives terminal close)
skill-seekers enhance output/react/ --daemon
```

Example 2 (markdown):
```markdown
# Install dependencies
pip install anthropic

# Set API key
export ANTHROPIC_API_KEY=sk-ant-...

# Enhance
skill-seekers enhance output/react/ --mode api
```

Example 3 (markdown):
```markdown
# Runs in foreground, waits for completion
skill-seekers enhance output/react/

# With force mode (no confirmations)
skill-seekers enhance output/react/ --force
```

Example 4 (markdown):
```markdown
# Start in background
skill-seekers enhance output/react/ --background

# Returns immediately with status file created
# Monitor progress:
skill-seekers enhance-status output/react/

# Watch in real-time:
skill-seekers enhance-status output/react/ --watch
```

---

## PDF Documentation | Skill Seekers Docs

**URL:** https://skillseekersweb.com/docs/manual/scraping/pdf

**Contents:**
- PDF Documentation Scraping
- Overview
- Quick Start
  - Basic Usage
  - Complete Workflow
- Usage Modes
  - Mode 1: Direct PDF (Quick)
  - Mode 2: Config File (Recommended)
  - Mode 3: From Extracted JSON (Iteration)
- Advanced Features

Extract content from PDF documentation and convert to AI skills with advanced features including OCR, table extraction, parallel processing, and MCP integration.

Skill Seekers’ PDF scraper converts PDF documentation into AI skills with:

Uses default settings:

Create configs/manual_pdf.json:

Extract text from scanned PDFs using Optical Character Recognition:

Performance: ~2-5 seconds per page

Handle encrypted PDFs:

Security note: Password is passed via command line (visible in process list). For sensitive documents, use environment variables.

Extract tables from PDFs:

Best with: Well-formatted tables, not complex merged cells

Process pages in parallel for 3x faster extraction:

Note: Only activates for PDFs with > 5 pages

Detects chapter boundaries automatically:

Break large PDFs into manageable chunks:

Intelligently merges code blocks split across pages:

Result: Combined into single code block

If PDF has detectable chapters:

Provide custom categories in config:

The scrape_pdf MCP tool provides PDF scraping through Model Context Protocol:

See: MCP Setup for MCP server configuration

Use --from-json for iteration

Problem: Only “content” or “other” category

Problem: Too many poor code examples

Problem: No images in assets/images/

Problem: OCR fails or gives poor results

Problem: Password not accepted

**Examples:**

Example 1 (sql):
```sql
# Extract from PDF
skill-seekers pdf --input manual.pdf --output output/manual/

# With OCR for scanned PDFs
skill-seekers pdf --input scanned.pdf --output output/scanned/ --ocr

# Password-protected PDF
skill-seekers pdf --input encrypted.pdf --password "your-password"

# Extract tables
skill-seekers pdf --input data.pdf --extract-tables

# Parallel processing (3x faster)
skill-seekers pdf --input large.pdf --parallel --workers 8
```

Example 2 (go):
```go
# 1. Extract from PDF
skill-seekers pdf --input manual.pdf --output output/manual/

# 2. Enhance (optional)
skill-seekers enhance output/manual/

# 3. Package
skill-seekers package output/manual/ --target claude

# 4. Upload
skill-seekers upload manual-claude.zip
```

Example 3 (unknown):
```unknown
skill-seekers pdf \
  --input manual.pdf \
  --output output/manual/ \
  --extract-images \
  --min-quality 6.0
```

Example 4 (json):
```json
{
  "name": "mymanual",
  "description": "My Manual documentation",
  "pdf_path": "docs/manual.pdf",
  "extract_options": {
    "chunk_size": 10,
    "min_quality": 6.0,
    "extract_images": true,
    "min_image_size": 150
  },
  "categories": {
    "getting_started": ["introduction", "setup"],
    "api": ["api", "reference", "function"],
    "tutorial": ["tutorial", "example", "guide"]
  }
}
```

---
