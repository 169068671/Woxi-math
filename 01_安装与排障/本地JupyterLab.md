---
title: 本地 JupyterLab
created: 2026-08-21
updated: 2026-08-21
tags:
  - 工具/Woxi
  - 系统/说明
---

# 本地 JupyterLab

已装在本库 `venv` 里（4.6.3），并用本机 `/Users/wangzirui/.local/bin/woxi` 注册了内核 **Woxi (Wolfram Language)**。

双击 [[打开本地JupyterLab.command]]，会打开 [[方向导数演示.ipynb]]。

从新建 Woxi 笔记本、执行验证到导出离线 HTML 的完整步骤，见 [[Woxi-JupyterLab到HTML展示工作流]]。

1. 右上角内核选 **Woxi (Wolfram Language)**
2. 先跑 `1 + 2` 确认内核可用
3. 再跑下面的 `Manipulate`

> [!note]
> Jupyter 内核走本机 `woxi` 命令行，不经过 Studio，也不会去下 40MB WASM。  
> `Manipulate` 若只显示表达式、不能拖滑块，用 [[打开方向导数HTML.command]] 或 [[本地Woxi Playground]]。
