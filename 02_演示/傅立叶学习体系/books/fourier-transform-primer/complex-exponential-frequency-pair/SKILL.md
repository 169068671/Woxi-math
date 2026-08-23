---
name: complex-exponential-frequency-pair
description: |
  当用户询问“负频率到底是什么？”、phasor / positive and negative frequency，或需要用该方法诊断数学推导时调用。执行时必须给出公式角色、适用条件与可验证结果。不适用于纯粹查定义，或问题实际属于 `complex-inner-product-audit` 的情形。
source_book: 《工科生苦傅立叶久矣！傅立叶变换究极入门》 AI Sci Ke 理工柯小西
source_chapter: 30:00–32:38；38:05–40:12；43:28–50:42
tags: [fourier, mathematics, learning-system]
related_skills:
  - slug: complex-inner-product-audit
    relation: composes-with
  - slug: orthogonal-basis-audit
    relation: composes-with
  - slug: fourier-series-analysis-synthesis
    relation: depends-on
---

# 复指数的双表示与正负频率配对

## R — 原文（Reading）

> 实数的正弦函数，在复频率上是正频率和负频率各一部分，振幅相等、相位相反。
>
> — AI Sci Ke 理工柯小西，30:00–32:38；38:05–40:12；43:28–50:42

## I — 方法论骨架（Interpretation）

用欧拉公式在旋转相量和正弦/余弦之间来回切换。正负频率代表复平面上相反旋转方向；实信号要求两侧系数共轭配对。该视角同时解释相位、复根振荡、频谱对称和实信号重建。

核心公式：`cosωt=(e^{jωt}+e^{-jωt})/2`。

## A1 — 视频中的应用（Past Application）

- **问题**：讲者需要把抽象公式还原为可理解、可迁移的结构。
- **方法论的使用**：视频把 cos 与 sin 写成 e^{jωt} 和 e^{-jωt} 的组合，并在傅立叶级数中用正负谐波共同重建周期实函数。
- **结论**：该方法能在至少两个独立语境中复用，并通过阶段 1.5 三重验证。
- **结果**：形成可计算、可画图、可检查边界的傅立叶学习单元。

## A2 — 触发场景（Future Trigger）

### 用户会在什么情境下需要这个 skill？

1. 正在学习傅立叶、线性代数或微分方程，但公式之间缺少统一解释。
2. 需要诊断一段推导中的符号、尺度、基、边界或重建错误。
3. 希望把概念转成可运行的数值实验或教学步骤。

### 语言信号

- “负频率到底是什么？”
- “为什么实信号频谱共轭对称？”
- “phasor / positive and negative frequency”

### 与相邻 skill 的区分

- `complex-inner-product-audit`：composes-with
- `orthogonal-basis-audit`：composes-with
- `fourier-series-analysis-synthesis`：depends-on

## E — 可执行步骤（Execution）

1. **把三角函数改写成复指数对**
   - 完成标准：已留下可核查的公式、条件或数值验证。
2. **标记旋转方向、幅度与相位**
   - 完成标准：已留下可核查的公式、条件或数值验证。
3. **检查实信号系数是否满足共轭对称**
   - 完成标准：已留下可核查的公式、条件或数值验证。

4. **做反例核验**
   - 完成标准：至少检查一个边界或失败模式；若不满足前提，停止套用并明确说明。

## B — 边界（Boundary）

### 不要在以下情况使用

- 单边幅度图隐藏相位与负频率信息
- 复信号不必满足实信号的共轭对称

### 视频警告的失败模式

- 把直觉类比当成无限制的严格等同。
- 只看公式外形，不追踪区间、变量、微元、共轭和归一化。

### 讲解的局限

- 视频以工程直觉为主；涉及函数空间、完备性、收敛和广义函数时必须补充更严格条件。

## 相关 skills

- `complex-inner-product-audit`：composes-with
- `orthogonal-basis-audit`：composes-with
- `fourier-series-analysis-synthesis`：depends-on

## 审计信息

- **验证通过**：V1 ✓ / V2 ✓ / V3 ✓
- **测试目标**：100%（详见 `test-results.md`）
- **蒸馏时间**：2026-08-23
