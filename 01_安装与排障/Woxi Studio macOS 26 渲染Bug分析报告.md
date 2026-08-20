---
title: Woxi Studio macOS 26 渲染Bug分析报告
created: 2026-08-20
updated: 2026-08-20
tags:
  - 工具/Woxi
  - 工具/排障
  - 学段/拓展
---

# Woxi Studio macOS 26 渲染 Bug 分析报告

> 分析日期：2026-08-20
> Woxi 版本：v0.3.0（截至 2026-08-06 的最新版本）
> 操作系统：macOS 26.5.2 (25F84)，Apple Silicon (ARM-64)

---

## 一、问题概述

Woxi Studio v0.3.0 在 macOS 26 上运行包含 3D 图形（`Graphics3D`、`Plot3D`、`Show[Plot3D[...], Graphics3D[...]]`）或 `Manipulate` 交互式控件的代码时，会触发 SIGABRT 崩溃。崩溃在渲染阶段发生，与代码逻辑无关，是底层 GUI 依赖库的兼容性问题。

## 二、崩溃根因

通过分析 macOS 崩溃报告（`~/Library/Logs/DiagnosticReports/woxi-studio-*.ips`）和 stderr 日志，定位到完整的崩溃链：

### 崩溃链

```
1. cosmic-text 0.15.0 / glyph_cache.rs:100
   → SubpixelBin::new() 函数中 "attempt to add with overflow"（整数溢出）

2. iced_winit 0.14.0 / lib.rs:275
   → 事件通道断开 "SendError { kind: Disconnected }"

3. panic in a function that cannot unwind
   → Rust 运行时调用 abort() → SIGABRT，进程终止
```

### 关键堆栈

```
cosmic_text::glyph_cache::SubpixelBin::new     ← 溢出起点
  ↓
iced_winit::run                                ← 事件发送失败
  ↓
__rustc::rust_begin_unwind                     → panic_cannot_unwind → abort
```

### 根本原因

`cosmic-text` v0.15.0 的 `SubpixelBin::new(pos: f32)` 函数在处理亚像素字体位置时，将浮点坐标转换为整数索引的过程中发生整数加法溢出。这是一个已知 bug（[pop-os/cosmic-text#1354](https://github.com/pop-os/cosmic-text/issues/1354)），在 macOS 26 的字体渲染管线上更容易触发。

该 bug 在 `cosmic-text` v0.16+ 中已修复，最新版本为 v0.19.0。但 Woxi Studio v0.3.0 使用 `iced 0.14`，后者依赖 `cosmic-text 0.15.0`，因此问题无法从用户侧简单修补。

## 三、依赖关系

```
Woxi Studio v0.3.0
  └── iced 0.14
        ├── iced_winit 0.14.0      ← 事件循环
        ├── iced_tiny_skia         ← 2D 渲染
        └── cosmic-text 0.15.0     ← 字体/字形缓存（bug 所在）
              └── glyph_cache.rs
                    └── SubpixelBin::new()  ← 整数溢出
```

## 四、版本信息

| 项目 | 版本 |
|------|------|
| Woxi | v0.3.0（最新，2026-08-06 发布） |
| iced | 0.14 |
| cosmic-text | 0.15.0（有 bug 的版本） |
| cosmic-text 最新版 | 0.19.0（已修复） |
| macOS | 26.5.2 (25F84) |

Woxi 版本历史：

| 版本 | 发布日期 |
|------|---------|
| v0.1.0 | 2025-05-08 |
| v0.2.0 | 2026-07-16 |
| v0.3.0（当前最新） | 2026-08-06 |

## 五、影响范围

- **受影响**：Woxi Studio 的所有图形渲染功能，包括 `Graphics3D`、`Plot3D`、`Show` 组合 3D 图形、`Manipulate` 交互式控件
- **不受影响**：Woxi CLI（命令行工具不走 iced/cosmic-text 渲染管线）、在线 Playground、JupyterLite

## 六、解决方案

### 方案一：使用 Woxi CLI 替代 Studio

CLI 不使用 iced/cosmic-text 渲染管线，不会触发此 bug。可运行 `.wls` 脚本生成图形输出（SVG/PNG）。

```bash
woxi eval "Plot[Sin[x], {x, -Pi, Pi}]"
woxi run 方向导数演示.wls
```

### 方案二：使用在线 Playground（本库默认）

日常交互不要开本机 Studio。打开：

- 完整编辑器：https://woxi.ad-si.com/playground/
- 首页小窗：https://woxi.ad-si.com/
- JupyterLite：https://woxi.ad-si.com/jupyterlite/lab/index.html

方向导数：双击 [[打开Woxi Playground演示.command]]，或把 [[方向导数演示.wls]] 贴进 Playground 后点 Run。两者均支持 `Manipulate`，无需安装。

### 方案三：在 Windows 上安装 Woxi Studio

Woxi Studio 官方支持 Windows（x86-64 和 arm64）。从 GitHub Releases 下载：

- 下载地址：https://github.com/ad-si/Woxi/releases/tag/v0.3.0
- 文件名：`woxi-studio-v0.3.0-x86_64-pc-windows-msvc.zip`

Windows 不受此 cosmic-text macOS 特有 bug 影响。可通过向日葵远程桌面连接 Windows 机器使用，但 Manipulate 滑块交互会有网络延迟。

### 方案四：使用独立 HTML 可视化

已创建的基于 Three.js 的交互式可视化不依赖 Woxi Studio，可在任何浏览器中直接打开，无延迟、全交互：

- 文件：`方向导数演示.html`
- 功能：3D 曲面、方向箭头、极坐标图、步长与角度滑块

### 方案五：等待官方修复

此 bug 的根源在依赖库，需要 Woxi 官方在下个版本中升级到使用新版 `iced`（依赖 `cosmic-text ≥ 0.16`）。可在 GitHub 上报告此 macOS 26 崩溃问题以加速修复：

- Issue 页面：https://github.com/ad-si/Woxi/issues

## 七、建议

| 使用场景 | 推荐方案 |
|---------|---------|
| 带滑块的 3D 演示 | 在线 Playground，见 [[打开Woxi Playground演示.command]] |
| 快速验证代码 / 简单计算 | 在线 Playground |
| 离线、跟手的交互 | 独立 HTML / Python |
| 批量运行脚本 | Woxi CLI |
| 需要 Studio 完整编辑体验 | Windows 安装 + 向日葵远程，见 [[Windows向日葵安装Woxi]] |
| 长期方案 | 等待 Woxi 官方更新依赖修复 |

相关：[[Woxi安装与使用]] · [[方向导数-家长先看]]

---

*本报告基于 2026-08-20 的崩溃日志分析和 GitHub 公开信息编写。*
