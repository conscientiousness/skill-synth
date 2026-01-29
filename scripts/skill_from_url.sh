#!/usr/bin/env bash
set -euo pipefail

# Usage: scripts/skill_from_url.sh <url> --name NAME [--engine codex|gemini|none]
#                                     [--max-pages N] [--rate-limit SEC]
#                                     [--workers N] [--no-clean] [--no-sync]
#
# Example:
#   scripts/skill_from_url.sh https://skillseekersweb.com/docs/getting-started/overview/ --name using-skillseekers-docs --engine codex

URL=""
NAME=""
ENGINE="codex"
MAX_PAGES="300"
RATE_LIMIT="0.5"
WORKERS="6"
CLEAN="1"
SYNC="1"
CONFIG=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    -n|--name)
      NAME="${2:-}"; shift 2 ;;
    -e|--engine)
      ENGINE="${2:-}"; shift 2 ;;
    --max-pages)
      MAX_PAGES="${2:-}"; shift 2 ;;
    --rate-limit)
      RATE_LIMIT="${2:-}"; shift 2 ;;
    --workers)
      WORKERS="${2:-}"; shift 2 ;;
    --config)
      CONFIG="${2:-}"; shift 2 ;;
    --no-clean)
      CLEAN="0"; shift ;;
    --no-sync)
      SYNC="0"; shift ;;
    -h|--help)
      echo "Usage: scripts/skill_from_url.sh <url> [--name NAME] [--engine codex|gemini|none]";
      echo "                                     [--max-pages N] [--rate-limit SEC]";
      echo "                                     [--workers N] [--no-clean] [--no-sync]";
      exit 0 ;;
    *)
      if [[ -z "$URL" ]]; then
        URL="$1"; shift
      else
        echo "Unknown argument: $1" >&2
        exit 1
      fi
      ;;
  esac
 done

if [[ -z "$URL" ]]; then
  echo "URL is required." >&2
  exit 1
fi

if [[ -z "$NAME" && -z "$CONFIG" ]]; then
  echo "--name is required unless --config is provided." >&2
  exit 1
fi

if [[ -z "$CONFIG" ]]; then
  CONFIG="configs/docs/${NAME}.json"

  NAME=$(python scripts/build_config_from_url.py "$URL" --output "$CONFIG" --name "$NAME" \
    --max-pages "$MAX_PAGES" --rate-limit "$RATE_LIMIT")
fi

if [[ -z "$NAME" && -n "$CONFIG" ]]; then
  NAME=$(python - <<'PY'
import json, sys
cfg = json.load(open(sys.argv[1], 'r', encoding='utf-8'))
print(cfg.get('name',''))
PY
"$CONFIG")
fi

if [[ -z "$NAME" ]]; then
  echo "Could not determine skill name." >&2
  exit 1
fi

if [[ "$CLEAN" == "1" ]]; then
  python - <<'PY'
import shutil, pathlib, sys
name = sys.argv[1]
for p in [pathlib.Path('output')/name, pathlib.Path('output')/f"{name}_data"]:
    if p.exists():
        shutil.rmtree(p)
PY
"$NAME"
fi

uv run skill-seekers scrape --config "$CONFIG" --async --workers "$WORKERS"
python scripts/normalize_skill_frontmatter.py "output/$NAME/SKILL.md"

if [[ "$ENGINE" != "none" ]]; then
  scripts/enhance.sh --engine "$ENGINE" "output/$NAME"
  python scripts/normalize_skill_frontmatter.py "output/$NAME/SKILL.md"
fi

printf "y\n" | uv run skill-seekers package --no-open "output/$NAME/"

if [[ "$SYNC" == "1" ]]; then
  python - <<'PY'
import shutil, pathlib, sys
src = pathlib.Path('output')/sys.argv[1]
dst = pathlib.Path('skills')/sys.argv[1]
if dst.exists():
    shutil.rmtree(dst)
shutil.copytree(src, dst)
PY
"$NAME"
fi

echo "Done. Output: output/$NAME and output/$NAME.zip"
