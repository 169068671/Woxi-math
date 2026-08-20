---
title: Woxi安装与使用
created: 2026-08-20
updated: 2026-08-20
tags:
  - 学段/拓展
  - 学科/数学
  - 工具/Woxi
  - 系统/说明
---

# Woxi 安装与使用

> [!warning] 这不是中考内容
> Woxi 是免费的 Wolfram Language 解释器（Rust 实现），用来跑类似 Mathematica 的表达式和 `.nb` 笔记本。  
> **不要占用中考复习时间，不要进入 00–09 过关流程。**

## 本机状态（2026-08-20）

本机是 Apple Silicon。装的是官方 **0.3.0** ARM64 正式版，校验和已对上。

| 组件 | 位置 | 说明 |
|---|---|---|
| 命令行 `woxi` | `/Users/wangzirui/.local/bin/woxi` | 已可用，新开终端即可 |
| Woxi Studio（当前） | `/Users/wangzirui/Applications/Woxi Studio.app` | 已装在用户应用程序 |
| Woxi Studio（目标） | `/Applications/Woxi Studio.app` | 需你本地运行旁边的脚本才能放进去 |

实测：`woxi eval "1 + 2"` 得到 `3`。

> [!tip] 日常请用本地 HTML / Python
> 双击 [[打开方向导数HTML.command]] 或 [[运行方向导数演示.command]]。断网也能跑。  
> 本机 Studio 会崩溃；官方在线 Playground 要下约 40MB。本地副本见 [[本地Woxi Playground]]。

## 你要做的一步：放进系统应用程序

系统文件夹需要本机密码，脚本不会自动执行。请你：

1. 打开 Finder，进入本库：`Woxi mathmatic平替/01_安装与排障/`
2. 双击 [[把Woxi装进系统应用程序.command]]
3. 若提示「无法打开」，右键该文件 → 打开
4. 弹出密码框时，输入开机密码
5. 看到「完成：Woxi Studio 已在 /Applications」即可关掉窗口

脚本只会把已有的 `Woxi Studio.app` 从用户应用程序复制到 `/Applications`，不会重新下载。

## 日常怎么用

**首选：本地演示（不联网）**

1. HTML：双击 [[打开方向导数HTML.command]]，改 [[方向导数演示.html]]
2. Python：双击 [[运行方向导数演示.command]]，改 `方向导数演示.py`
3. 命令行算式：`woxi eval "1 + 2"`（本机已装）
4. JupyterLab：双击 [[打开本地JupyterLab.command]]

```bash
woxi eval "1 + 2"
woxi repl
woxi run 脚本.wls
```

本机 Studio（macOS 26 上 3D / Manipulate 会崩溃，不要用来跑演示）：

- 复制进系统文件夹之后：Spotlight 搜 **Woxi Studio**，或打开「应用程序」
- 复制之前：打开 `/Users/wangzirui/Applications/Woxi Studio.app`

第一次打开若提示「无法验证开发者」，右键 → 打开。官方包是 ad-hoc 签名，未做 Apple 公证。

## 还没装的部分

无。JupyterLab 已在本库 `venv`，内核见 [[本地JupyterLab]]。

## 官方来源

- 项目：<https://github.com/ad-si/Woxi>
- 在线 Playground：<https://woxi.ad-si.com/playground/>
- 文档：<https://woxi.ad-si.com/docs/>
- 笔记本编辑器说明：<https://woxi.ad-si.com/docs/studio/>
