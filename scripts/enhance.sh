#!/usr/bin/env bash
set -euo pipefail

# Usage: scripts/enhance.sh [--engine codex|gemini] [SKILL_DIR]
# Default engine: codex

ENGINE="codex"
SKILL_DIR=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    -e|--engine)
      ENGINE="${2:-}"; shift 2 ;;
    -h|--help)
      echo "Usage: scripts/enhance.sh [--engine codex|gemini] [SKILL_DIR]"; exit 0 ;;
    *)
      SKILL_DIR="$1"; shift ;;
  esac
 done

if [[ -z "$SKILL_DIR" ]]; then
  SKILL_DIR="skills/using-tastytrade-python-sdk"
fi

case "$ENGINE" in
  codex)
    scripts/enhance_with_codex.sh "$SKILL_DIR" ;;
  gemini)
    scripts/enhance_with_gemini.sh "$SKILL_DIR" ;;
  *)
    echo "Unknown engine: $ENGINE (use codex or gemini)" >&2
    exit 1
    ;;
 esac
