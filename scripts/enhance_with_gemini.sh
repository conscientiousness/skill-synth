#!/usr/bin/env bash
set -euo pipefail

# Usage: scripts/enhance_with_gemini.sh [SKILL_DIR]
# Example: scripts/enhance_with_gemini.sh skills/using-tastytrade-python-sdk

SKILL_DIR=${1:-skills/using-tastytrade-python-sdk}
SKILL_DIR=${SKILL_DIR%/}
SKILL_MD="$SKILL_DIR/SKILL.md"

if ! command -v gemini >/dev/null 2>&1; then
  echo "gemini CLI not found. See: https://geminicli.com/" >&2
  exit 1
fi

if [[ ! -f "$SKILL_MD" ]]; then
  echo "SKILL.md not found at: $SKILL_MD" >&2
  exit 1
fi

python scripts/normalize_skill_frontmatter.py "$SKILL_MD"

PROMPT_FILE=$(mktemp)
python scripts/build_skillseekers_prompt.py "$SKILL_DIR" > "$PROMPT_FILE"

if [[ ! -s "$PROMPT_FILE" ]]; then
  echo "Failed to build prompt (empty)." >&2
  rm -f "$PROMPT_FILE"
  exit 1
fi

# Backup before edits (Skill Seekers convention)
cp "$SKILL_MD" "$SKILL_MD.backup"

TMP_OUT=$(mktemp)
GEMINI_FLAGS=${GEMINI_FLAGS:-""}

# Run Gemini in headless mode, prompt via stdin.
# Docs: https://geminicli.com/
cat "$PROMPT_FILE" | gemini $GEMINI_FLAGS > "$TMP_OUT"

rm -f "$PROMPT_FILE"

# Basic validation: require frontmatter; trim any leading junk.
python - "$TMP_OUT" <<'PY'
import pathlib, sys
out_path = pathlib.Path(sys.argv[1])
text = out_path.read_text(encoding="utf-8", errors="ignore")
lines = text.splitlines()
start = None
for i, line in enumerate(lines):
    if line.strip() == "---":
        start = i
        break
if start is None:
    print("Output missing YAML frontmatter; aborting.", file=sys.stderr)
    sys.exit(1)
trimmed = "\n".join(lines[start:]).strip() + "\n"
out_path.write_text(trimmed, encoding="utf-8")
PY

mv "$TMP_OUT" "$SKILL_MD"
python scripts/normalize_skill_frontmatter.py "$SKILL_MD"

echo "Updated: $SKILL_MD"
echo "Backup:  $SKILL_MD.backup"
