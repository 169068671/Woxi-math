#!/bin/bash
# 双击运行 GeoGebra 方向导数案例复刻
DEMO="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$DEMO/../.." && pwd)"
PY="$ROOT/venv/bin/python3.14"
if [[ ! -x "$PY" ]]; then
  osascript -e 'display dialog "找不到 venv 中的 Python。请检查 '"$ROOT"'/venv/ 目录是否存在。" buttons {"好"} default button 1 with title "GeoGebra 方向导数演示"'
  exit 1
fi
exec env -u PYTHONHOME -u PYTHONPATH "$PY" "$DEMO/geogebra方向导数.py"
