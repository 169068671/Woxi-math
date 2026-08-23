---
title: Woxi JupyterLab 到 HTML 展示工作流
created: 2026-08-21
updated: 2026-08-21
tags:
  - 工具/Woxi
  - 系统/说明
---

# Woxi JupyterLab 到 HTML 展示工作流

> [!summary] 固定目标
> 用本机 JupyterLab 编写和执行 Woxi（Wolfram Language）代码，确认输出无错误，再导出一个包含代码、文字和图形结果的离线 HTML，最后直接用浏览器查看。

## 适用范围

- 数学计算、函数绘图和其他 Woxi 演示。
- 需要保留可继续编辑的 `.ipynb`，同时交付可直接查看的 `.html`。
- 不使用 Woxi Studio；本机 macOS 26 上的 Studio 存在渲染崩溃问题。

示例文件：

- 可编辑笔记本：[[y=x²绘图.ipynb]]
- 离线展示页：[[y=x²绘图结果.html]]
- 本地环境说明：[[本地JupyterLab]]

## 固定流程

### 1. 建立主题目录

每个数学主题单独放在：

```text
02_演示/主题名/
```

例如：

```text
02_演示/抛物线/
```

目录内至少保留两份交付物：

```text
主题名.ipynb
主题名结果.html
```

### 2. 启动本地 JupyterLab

双击 [[打开本地JupyterLab.command]]。进入 JupyterLab 后新建或打开笔记本，右上角内核必须显示：

```text
Woxi (Wolfram Language)
```

> [!warning]
> JupyterLab 是编辑界面，Woxi 才是执行代码的内核。不要误选 Python 内核，也不要为此打开 Woxi Studio。

### 3. 先做一次内核自检

在第一个代码单元运行：

```wolfram
1 + 2
```

正常结果是 `3`。这只表示 JupyterLab 已成功连接 Woxi，不属于正式数学演示内容。若没有输出 `3`，先检查右上角内核是否为 **Woxi (Wolfram Language)**。

### 4. 编写 Woxi 代码

例如绘制 $y=x^2$：

```wolfram
Plot[
 x^2,
 {x, -5, 5},
 AxesLabel -> {"x", "y"},
 PlotLabel -> "y = x^2",
 PlotStyle -> Blue,
 GridLines -> Automatic,
 ImageSize -> 600
]
```

代码使用 Wolfram/Mathematica 风格语法，由 Woxi 内核执行，不是 Python 代码。

### 5. 在 JupyterLab 中完整运行

执行 **Run → Run All Cells**，确认：

1. 内核自检输出 `3`。
2. 正式代码单元出现计算或图形结果。
3. 页面中没有红色报错信息。
4. 保存笔记本，让结果嵌入 `.ipynb`。

### 6. 用命令做全本复跑验证

在仓库根目录执行：

```bash
venv/bin/python -m jupyter nbconvert \
  --execute \
  --to notebook \
  --inplace \
  --ExecutePreprocessor.timeout=60 \
  '02_演示/主题名/主题名.ipynb'
```

这一步会从头执行所有单元并把最新结果写回笔记本。命令正常结束且没有 traceback，才进入 HTML 导出。

> [!tip]
> 当前环境已经允许 `venv/bin/python -m jupyter nbconvert` 这一命令前缀，用于后续笔记本验证和导出。

### 7. 导出带结果的离线 HTML

继续在仓库根目录执行：

```bash
venv/bin/python -m jupyter nbconvert \
  --to html \
  --output '主题名结果.html' \
  '02_演示/主题名/主题名.ipynb'
```

HTML 会生成在笔记本所在目录。图形和输出会嵌入页面，不依赖 JupyterLab，也不需要联网。

### 8. 浏览器展示

在 Finder、Codex 文件链接或 Obsidian 中打开生成的 `主题名结果.html`。浏览器地址会是本地 `file:///...` 路径。

检查页面中：

- 标题和说明正常显示。
- Woxi 代码完整显示。
- 计算或 SVG 图形结果正常显示。
- 刷新页面后仍能看到结果。

### 9. 用户关掉浏览页后收尾

用户说「可以关了」、关掉结果页、或明确看完后，必须同时关掉 JupyterLab 和这次打开的相关网页。不要退出整个浏览器，也不要删除 `.ipynb` / `.html`。

停止本库这次启动的 JupyterLab（含 Woxi 内核），不要留在后台：

```bash
pkill -INT -f 'jupyterlab --notebook-dir=.*/Woxi mathmatic平替' || true
```

只关闭相关网页：`localhost:8888` 的 JupyterLab 标签、本次 `主题名结果.html` 标签。Chrome 可用：

```bash
osascript -e 'tell application "Google Chrome"
  repeat with w in windows
    repeat with t in reverse of (tabs of w)
      set u to URL of t
      if u contains "localhost:8888" or u contains "绘图结果.html" then close t
    end repeat
  end repeat
end tell'
```

笔记本和离线 HTML 留在 `02_演示/主题名/`。下次直接打开 HTML 即可，不必再开 JupyterLab。

## 固定交付标准

一次完整交付必须同时具备：

- [ ] `.ipynb` 使用 `Woxi (Wolfram Language)` 内核。
- [ ] 笔记本已从头到尾执行，代码单元没有错误输出。
- [ ] 图形或计算结果已经嵌入笔记本。
- [ ] 已生成同目录离线 `.html`。
- [ ] HTML 已在浏览器实际打开检查。
- [ ] 向用户提供可点击的 HTML 路径；如需继续编辑，再同时提供 `.ipynb` 路径。
- [ ] 用户关掉浏览页后：JupyterLab 已停止，相关标签已关；结果文件仍保留。

## 常见问题

| 现象 | 处理 |
|---|---|
| `1 + 2` 不输出 `3` | 检查内核是否为 `Woxi (Wolfram Language)`，必要时重启内核 |
| `Plot` 只显示 `-Graphics-` | 先在 JupyterLab 中看富媒体输出；CLI 纯文本测试只代表已生成图形对象 |
| HTML 中没有最新结果 | 先执行第 6 步复跑并写回笔记本，再重新导出 HTML |
| `Manipulate` 没有可拖动滑块 | 属于 Woxi CLI/Jupyter 内核限制；改用 [[本地Woxi Playground]] 或本地 HTML |
| Woxi Studio 崩溃 | 不修 Studio，继续使用本流程 |
| 用户已关浏览页，JupyterLab 还在 | 执行第 9 步：停 JupyterLab，并关掉 `localhost:8888` 和本次结果 HTML 标签 |

