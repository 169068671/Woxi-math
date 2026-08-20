#!/bin/bash
# 打开本机 JupyterLab，内核已注册 Woxi（Wolfram Language）
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PY="$ROOT/venv/bin/python"
NB="$ROOT/02_演示/方向导数/方向导数演示.ipynb"
export PATH="$ROOT/venv/bin:$HOME/.local/bin:$PATH"
export MPLCONFIGDIR="$ROOT/.mplconfig"
if [[ ! -x "$PY" ]]; then
  osascript -e 'display dialog "找不到 venv 里的 Python。" buttons {"好"} default button 1 with title "JupyterLab"'
  exit 1
fi
cd "$ROOT"
exec "$PY" -m jupyterlab --notebook-dir="$ROOT" "$NB"
