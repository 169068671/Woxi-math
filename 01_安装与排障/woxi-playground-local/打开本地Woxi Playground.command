#!/bin/bash
# 用本机已下载的 Woxi Playground（约 40MB WASM 在 pkg/），不访问 woxi.ad-si.com
ROOT="$(cd "$(dirname "$0")" && pwd)"
PORT=8765
WLS="$(cd "$ROOT/../../02_演示/方向导数" && pwd)/方向导数演示.wls"
if [[ ! -s "$ROOT/pkg/woxi_bg.wasm" ]]; then
  osascript -e 'display dialog "找不到本地 WASM（pkg/woxi_bg.wasm）。" buttons {"好"} default button 1 with title "本地 Woxi Playground"'
  exit 1
fi
if ! lsof -nP -iTCP:"$PORT" -sTCP:LISTEN >/dev/null 2>&1; then
  (cd "$ROOT" && python3 -m http.server "$PORT" >/tmp/woxi-local-playground.log 2>&1 &)
  sleep 0.6
fi
if [[ -f "$WLS" ]]; then
  pbcopy < "$WLS"
fi
open "http://127.0.0.1:${PORT}/"
osascript -e 'display dialog "本地 Playground 已打开。\n\n方向导数代码已复制。点左边编辑框 → Command+A → Command+V → 点 Run。\n第一次仍要几秒加载本地 WASM，不要刷新。" buttons {"好"} default button 1 with title "本地 Woxi Playground"'
