#!/usr/bin/env bash
# NetHack Companion 日本語版 ビルドスクリプト (Bash ラッパー)
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
PY_SCRIPT="$ROOT_DIR/tools/build_jp.py"

python3 "$PY_SCRIPT" "$@"
