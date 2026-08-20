---
title: Windows向日葵安装Woxi
created: 2026-08-20
updated: 2026-08-20
tags:
  - 工具/Woxi
  - 工具/排障
  - 系统/说明
---

# Windows 向日葵安装 Woxi

> [!note] 状态：待在 Windows 上实际安装
> 本机 macOS 的 Woxi Studio 会因 cosmic-text 溢出崩溃。日常交互请先用在线 Playground：<https://woxi.ad-si.com/playground/> ，代码见 [[方向导数演示.wls]]。Windows + 向日葵只在需要原生 Studio 时再用。

## 要下的包

官方 Releases：<https://github.com/ad-si/Woxi/releases/tag/v0.3.0>

普通 64 位 Windows 用：

`woxi-studio-v0.3.0-x86_64-pc-windows-msvc.zip`

（若那台电脑是 ARM，再改用 `aarch64-pc-windows-msvc`。）

## 装好之后

1. 解压 zip，运行里面的 Woxi Studio。
2. 向日葵连上后，用 Studio 打开本库 `02_演示/方向导数/方向导数演示.wls` 或对应 `.nb`。
3. 滑块会有远程延迟；要跟手仍用本库 HTML / Python。

命令行可另装同版本 `woxi` CLI，不走 Studio 渲染。
