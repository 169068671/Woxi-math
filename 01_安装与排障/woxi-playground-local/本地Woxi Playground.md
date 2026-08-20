---
title: 本地 Woxi Playground
created: 2026-08-21
updated: 2026-08-21
tags:
  - 工具/Woxi
  - 系统/说明
---

# 本地 Woxi Playground

官方在线页要下约 40MB WASM。已用多线程把同一份解释器下到本目录 `pkg/woxi_bg.wasm`。

双击 [[打开本地Woxi Playground.command]]，会在本机 `http://127.0.0.1:8765/` 打开。方向导数代码会拷到剪贴板，粘贴后点 Run。

> [!note]
> 编辑器用的 CodeMirror 仍从 esm.sh 加载（几百 KB）。解释器本体不再走 `woxi.ad-si.com`。

日常 3D 滑块演示仍优先用 [[打开方向导数HTML.command]]。
