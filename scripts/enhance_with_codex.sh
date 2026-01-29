#!/usr/bin/env bash
set -euo pipefail

# Usage: scripts/enhance_with_codex.sh [SKILL_DIR]
# Example: scripts/enhance_with_codex.sh skills/using-tastytrade-python-sdk

SKILL_DIR=${1:-skills/using-tastytrade-python-sdk}
SKILL_DIR=${SKILL_DIR%/}
SKILL_MD="$SKILL_DIR/SKILL.md"

if ! command -v codex >/dev/null 2>&1; then
  echo "codex CLI not found. Install with: npm i -g @openai/codex" >&2
  exit 1
fi

if [[ ! -f "$SKILL_MD" ]]; then
  echo "SKILL.md not found at: $SKILL_MD" >&2
  exit 1
fi

PROMPT_FILE=$(mktemp)
python scripts/build_skillseekers_prompt.py "$SKILL_DIR" > "$PROMPT_FILE"

if [[ ! -s "$PROMPT_FILE" ]]; then
  echo "Failed to build prompt (empty)." >&2
  rm -f "$PROMPT_FILE"
  exit 1
fi

# Backup before edits (Skill Seekers convention)
cp "$SKILL_MD" "$SKILL_MD.backup"

CODEX_FLAGS=${CODEX_FLAGS:-"--full-auto"}

# Run Codex in non-interactive mode and feed prompt from stdin.
# Docs: codex exec can read prompt from stdin when PROMPT is '-'.
# https://developers.openai.com/codex/cli/reference
codex exec $CODEX_FLAGS --cd "$SKILL_DIR" - < "$PROMPT_FILE"

rm -f "$PROMPT_FILE"

if [[ -f "$SKILL_MD" ]]; then
  echo "Updated: $SKILL_MD"
  echo "Backup:  $SKILL_MD.backup"
else
  echo "SKILL.md missing after run; restoring backup." >&2
  mv "$SKILL_MD.backup" "$SKILL_MD"
  exit 1
fi
