---
name: discrete-continuous-limit
description: |
  当用户询问“为什么求和会变成积分？”、Riemann sum / discrete-to-continuous，或需要用该方法诊断数学推导时调用。执行时必须给出公式角色、适用条件与可验证结果。不适用于纯粹查定义，或问题实际属于 `finite-to-function-space` 的情形。
source_book: 《工科生苦傅立叶久矣！傅立叶变换究极入门》 AI Sci Ke 理工柯小西
source_chapter: 10:18–13:42；50:42–55:48
tags: [fourier, mathematics, learning-system]
related_skills:
  - slug: finite-to-function-space
    relation: depends-on
  - slug: series-to-transform-limit
    relation: composes-with
---

# 离散采样到连续积分的极限桥

## R — 原文（Reading）

> 相邻取点之间的间隙必须乘上去；细分趋向无穷时，求和就得到积分的形态。
>
> — AI Sci Ke 理工柯小西，10:18–13:42；50:42–55:48

## I — 方法论骨架（Interpretation）

把连续公式追溯为带网格宽度的离散求和。加密网格时同时更新采样间隔、求和范围和变量；只有这样极限才保持尺度。该程序既解释点积为何变积分，也解释离散频率和为何变频率积分。

核心公式：`Σ f(xᵢ)g(xᵢ)Δx → ∫ f(x)g(x)dx`。

## A1 — 视频中的应用（Past Application）

- **问题**：讲者需要把抽象公式还原为可理解、可迁移的结构。
- **方法论的使用**：函数内积从 Σf(xᵢ)g(xᵢ)Δx 过渡到积分；傅立叶级数从 ΣF(nf₀)e^{j2πnf₀t}f₀ 过渡到连续频率积分。
- **结论**：该方法能在至少两个独立语境中复用，并通过阶段 1.5 三重验证。
- **结果**：形成可计算、可画图、可检查边界的傅立叶学习单元。

## A2 — 触发场景（Future Trigger）

### 用户会在什么情境下需要这个 skill？

1. 正在学习傅立叶、线性代数或微分方程，但公式之间缺少统一解释。
2. 需要诊断一段推导中的符号、尺度、基、边界或重建错误。
3. 希望把概念转成可运行的数值实验或教学步骤。

### 语言信号

- “为什么求和会变成积分？”
- “采样越密数值为什么变大？”
- “Riemann sum / discrete-to-continuous”

### 与相邻 skill 的区分

- `finite-to-function-space`：depends-on
- `series-to-transform-limit`：composes-with

## E — 可执行步骤（Execution）

1. **写出带网格间隔的离散和**
   - 完成标准：已留下可核查的公式、条件或数值验证。
2. **让网格变密并追踪间隔和索引**
   - 完成标准：已留下可核查的公式、条件或数值验证。
3. **验证量纲、尺度和极限结果**
   - 完成标准：已留下可核查的公式、条件或数值验证。

4. **做反例核验**
   - 完成标准：至少检查一个边界或失败模式；若不满足前提，停止套用并明确说明。

## B — 边界（Boundary）

### 不要在以下情况使用

- 不能省略 Δx 或 Δf
- 极限与积分交换需要额外条件

### 视频警告的失败模式

- 把直觉类比当成无限制的严格等同。
- 只看公式外形，不追踪区间、变量、微元、共轭和归一化。

### 讲解的局限

- 视频以工程直觉为主；涉及函数空间、完备性、收敛和广义函数时必须补充更严格条件。

## 相关 skills

- `finite-to-function-space`：depends-on
- `series-to-transform-limit`：composes-with

## 审计信息

- **验证通过**：V1 ✓ / V2 ✓ / V3 ✓
- **测试目标**：100%（详见 `test-results.md`）
- **蒸馏时间**：2026-08-23
