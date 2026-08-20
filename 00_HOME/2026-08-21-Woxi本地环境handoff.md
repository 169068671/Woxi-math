---
title: 2026-08-21 Woxi本地环境handoff
created: 2026-08-21
updated: 2026-08-21
tags:
  - 系统/说明
---

# Woxi 本地环境 Handoff（给 Codex）

> 一次性交接。审完或接完可删本文件，不必写成长期规则。  
> 仓库：`/Users/wangzirui/Woxi mathmatic平替`  
> 整理方：Cursor（2026-08-20 ～ 2026-08-21）  
> 请用中文，先给结果。不要 commit，除非用户明确说提交。不要把过程写进 Cursor 工作流汇总。

**这不是中考内容。** 不要占用 `孩子们的知识点` 的 00–09 过关流程。家长向短说明可以镜像到 `孩子们的知识点/10_共享知识/拓展/`，完整安装包、Python、崩溃报告、本地运行环境**以本库为准**。

---

## 1. 请你先读

按这个顺序，不要全库扫描：

1. [[首页]]
2. [[仓库结构说明]]
3. [[Woxi安装与使用]]
4. [[Woxi Studio macOS 26 渲染Bug分析报告]]
5. [[方向导数-家长先看]]
6. [[本地Woxi Playground]]
7. [[本地JupyterLab]]

原则一句话：**日常演示用本地 HTML / Python；Woxi 算式用本机 CLI；Studio 在这台 macOS 26 上不要开。**

---

## 2. 机器与软件事实（2026-08-21）

| 项 | 状态 |
|---|---|
| 本机 | Apple Silicon，macOS 26.5.x |
| `woxi` CLI | `/Users/wangzirui/.local/bin/woxi`，官方 **0.3.0** ARM64，`woxi eval "1 + 2"` → `3` |
| Woxi Studio | `/Users/wangzirui/Applications/Woxi Studio.app`；3D / `Manipulate` 会 SIGABRT（cosmic-text 0.15 溢出） |
| Python | 本库 `venv/`（Python 3.14.6；`pip` shebang 仍指向旧 `.venv` 路径，要用 `venv/bin/python -m pip`） |
| JupyterLab | 已在 `venv`，**4.6.3** |
| Woxi Jupyter 内核 | 已注册为 `woxi`，argv 指向上面的 CLI：`woxi jupyter {connection_file}` |
| 在线 Playground / JupyterLite | 能用但首次要下约 40MB WASM，国内会一直转圈；**不要当默认入口** |
| 外网下载 VPS `76.13.219.143` | 2026-08-21 测过：SSH/ping 超时，中转不可用 |

---

## 3. 已经做完的事

### 3.1 Obsidian 库结构

编号目录 + YAML + 双链 + `.obsidian`（附件进 `90_附件`，新笔记进 `07_收件箱`）。标签只走 [[标签索引]]。

### 3.2 方向导数演示（函数 `f=(x²+y²)/4`，点 P(1,1)）

**首选、完全离线：**

- 双击 `02_演示/方向导数/打开方向导数HTML.command`
- 或打开 `方向导数演示.html`
- Three.js r128 已在 `vendor/three.min.js`（约 590KB），**不要改回 CDN**

**次选：** 双击 `运行方向导数演示.command`（matplotlib；`venv` 在库根，脚本会向上找到 `00_HOME`）

箭头长短表示 `|D_u f|`；白色/最快方向是梯度。不要随便改坐标系：xy 在地面，z 竖直。

### 3.3 本地 Woxi Playground（WASM 已下）

`01_安装与排障/woxi-playground-local/pkg/woxi_bg.wasm` 约 39MB，属于本地 Playground 的必要运行依赖，已纳入仓库。  
双击 `打开本地Woxi Playground.command` → `http://127.0.0.1:8765/`。  
`worker.js` 已去掉 `Date.now()` 缓存戳，避免每次重下。  
编辑器仍从 `esm.sh` 拉 CodeMirror（几百 KB）。方向导数代码会拷到剪贴板。

### 3.4 本地 JupyterLab

双击 `01_安装与排障/打开本地JupyterLab.command`，打开 `02_演示/方向导数/方向导数演示.ipynb`。  
内核选 **Woxi (Wolfram Language)**，先跑 `1 + 2`。  
`woxi install-kernel` 在本库 cwd 会失败（它找 `./kernelspec/woxi`）；正本在 `01_安装与排障/kernelspec/woxi/kernel.json`，已 `jupyter kernelspec install --user --replace`。

### 3.5 明确不要做的

- 不要用本机 Woxi Studio 打开 `.nb` / `Manipulate`
- 不要把演示改成依赖 `woxi.ad-si.com`
- 不要往本库写 VPS 密码、API Key
- 不要把本库内容当成中考资料塞进 00–09

---

## 4. 请 Codex 接着做（按优先级）

只做用户点名的；不要顺手重构 HTML 观感。

1. **验收 JupyterLab（优先）**  
   双击 `打开本地JupyterLab.command`，确认 `1 + 2` 出 `3`。  
   再跑笔记本里的 `Manipulate`：若只打印表达式、没有滑块，这是 CLI 内核限制，不是新 bug。写进笔记一句即可，不要为此重写内核。

2. **若用户要跟手的 Woxi `Manipulate`**  
   用本地 Playground（8765）或继续用 HTML。不要为了滑块去修 Studio。

3. **Windows + 向日葵（仅用户明确要求时）**  
   见 [[Windows向日葵安装Woxi]]。包：`woxi-studio-v0.3.0-x86_64-pc-windows-msvc.zip`。滑块会有远程延迟。该页里「日常用在线 Playground」已过时，应改成本地 HTML / 本地 Playground。

4. **不要默认去下 JupyterLite 整站**  
   除非用户再说要。和 JupyterLab 不是一回事：Lite 是浏览器 WASM，Lab 已是本机 `woxi`。

---

## 5. 已知坑

| 坑 | 处理 |
|---|---|
| Studio + Plot3D / Manipulate | 崩溃，见崩溃报告 |
| 官方 Playground 一直 Loading | 在下 40MB WASM，刷新会重来 |
| `venv/bin/pip` | shebang 仍是 `.venv`；用 `venv/bin/python -m pip` |
| `woxi install-kernel` 在本库根目录 | 失败；用手写 kernelspec |
| 外网下载 skill / 开启代理 | 依赖那台 VPS，当前连不上；大文件改本机 `aria2c -x 16` |
| `打开Woxi Playground演示.command`（在 `02_演示/方向导数/`） | 旧入口，仍可能指向官网分享链接；新入口在 `01_安装与排障/woxi-playground-local/` |

---

## 6. 不要动的范围

- 不要改方向导数 HTML 的交互语义（所有方向、箭头长度编码 `|D|`、梯度）
- 不要把 `venv/`、`.mplconfig/`、`*.wasm` 链进 Obsidian 笔记
- 不要 commit、不要 push，除非用户要求
- 记忆库：Cursor 用 `/Users/wangzirui/Cursor工作流汇总`；Codex 用 Codex 自己的工作流汇总。互不代替。
