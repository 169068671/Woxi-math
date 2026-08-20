#!/bin/bash
# 双击即可打开方向导数 3D 演示
DEMO="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$DEMO/../.." && pwd)"
PY="$ROOT/venv/bin/python"
if [[ ! -x "$PY" ]]; then
  osascript -e 'display dialog "还没有安装运行环境。请先在终端执行：\n\ncd \"'"$ROOT"'\"\npython3 -m venv venv\nvenv/bin/pip install numpy matplotlib" buttons {"好"} default button 1 with title "方向导数演示"'
  exit 1
fi
exec "$PY" "$DEMO/方向导数演示.py"
