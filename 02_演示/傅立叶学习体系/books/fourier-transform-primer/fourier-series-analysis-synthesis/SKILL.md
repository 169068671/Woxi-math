---
name: fourier-series-analysis-synthesis
description: |
  当用户询问“傅立叶级数系数怎么推？”、Fourier series analysis/synthesis，或需要用该方法诊断数学推导时调用。执行时必须给出公式角色、适用条件与可验证结果。不适用于纯粹查定义，或问题实际属于 `projection-coordinate-reconstruction` 的情形。
source_book: 《工科生苦傅立叶久矣！傅立叶变换究极入门》 AI Sci Ke 理工柯小西
source_chapter: 45:32–50:42
tags: [fourier, mathematics, learning-system]
related_skills:
  - slug: projection-coordinate-reconstruction
    relation: depends-on
  - slug: complex-exponential-frequency-pair
    relation: depends-on
  - slug: orthogonal-basis-audit
    relation: depends-on
  - slug: series-to-transform-limit
    relation: composes-with
---

# 傅立叶级数的分析—综合双流程

## R — 原文（Reading）

> 上面的 F(n) 是求傅立叶级数的系数；下面的 f(t) 是用这些系数复原原来的函数。
>
> — AI Sci Ke 理工柯小西，45:32–50:42

## I — 方法论骨架（Interpretation）

周期函数只在基频整数倍的离散频率上展开。分析阶段在一个周期内对每个复指数基投影并除以 T；综合阶段将全部正负谐波的坐标乘基后求和。复指数形式和三角形式只是同一坐标信息的两种包装。

核心公式：`cₙ=(1/T)∫_T f(t)e^{-jnω₀t}dt；f(t)=Σcₙe^{jnω₀t}`。

## A1 — 视频中的应用（Past Application）

- **问题**：讲者需要把抽象公式还原为可理解、可迁移的结构。
- **方法论的使用**：视频对周期矩形脉冲计算离散频率系数，再逐步叠加谐波重建时域波形，并展示周期改变时频率网格如何变化。
- **结论**：该方法能在至少两个独立语境中复用，并通过阶段 1.5 三重验证。
- **结果**：形成可计算、可画图、可检查边界的傅立叶学习单元。

## A2 — 触发场景（Future Trigger）

### 用户会在什么情境下需要这个 skill？

1. 正在学习傅立叶、线性代数或微分方程，但公式之间缺少统一解释。
2. 需要诊断一段推导中的符号、尺度、基、边界或重建错误。
3. 希望把概念转成可运行的数值实验或教学步骤。

### 语言信号

- “傅立叶级数系数怎么推？”
- “怎样用有限谐波重建方波？”
- “Fourier series analysis/synthesis”

### 与相邻 skill 的区分

- `projection-coordinate-reconstruction`：depends-on
- `complex-exponential-frequency-pair`：depends-on
- `orthogonal-basis-audit`：depends-on
- `series-to-transform-limit`：composes-with

## E — 可执行步骤（Execution）

1. **确定周期 T 与基频 ω₀**
   - 完成标准：已留下可核查的公式、条件或数值验证。
2. **按复内积求 cₙ 并核对 1/T**
   - 完成标准：已留下可核查的公式、条件或数值验证。
3. **选择谐波范围综合重建并量化误差**
   - 完成标准：已留下可核查的公式、条件或数值验证。

4. **做反例核验**
   - 完成标准：至少检查一个边界或失败模式；若不满足前提，停止套用并明确说明。

## B — 边界（Boundary）

### 不要在以下情况使用

- 非周期信号不应直接套离散谐波级数
- 间断点附近有限截断会出现 Gibbs 现象

### 视频警告的失败模式

- 把直觉类比当成无限制的严格等同。
- 只看公式外形，不追踪区间、变量、微元、共轭和归一化。

### 讲解的局限

- 视频以工程直觉为主；涉及函数空间、完备性、收敛和广义函数时必须补充更严格条件。

## 相关 skills

- `projection-coordinate-reconstruction`：depends-on
- `complex-exponential-frequency-pair`：depends-on
- `orthogonal-basis-audit`：depends-on
- `series-to-transform-limit`：composes-with

## 审计信息

- **验证通过**：V1 ✓ / V2 ✓ / V3 ✓
- **测试目标**：100%（详见 `test-results.md`）
- **蒸馏时间**：2026-08-23
