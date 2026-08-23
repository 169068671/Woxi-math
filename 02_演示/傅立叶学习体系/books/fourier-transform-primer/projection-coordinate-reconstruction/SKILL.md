---
name: projection-coordinate-reconstruction
description: |
  当用户询问“为什么这个变换和逆变换长这样？”、analysis/synthesis 或 change of basis，或需要用该方法诊断数学推导时调用。执行时必须给出公式角色、适用条件与可验证结果。不适用于纯粹查定义，或问题实际属于 `finite-to-function-space` 的情形。
source_book: 《工科生苦傅立叶久矣！傅立叶变换究极入门》 AI Sci Ke 理工柯小西
source_chapter: 02:30–07:38；14:48–19:39；45:32–59:43
tags: [fourier, mathematics, learning-system]
related_skills:
  - slug: finite-to-function-space
    relation: composes-with
  - slug: orthogonal-basis-audit
    relation: depends-on
  - slug: fourier-series-analysis-synthesis
    relation: composes-with
---

# 投影—坐标—重建闭环

## R — 原文（Reading）

> 如果想把一个向量从一个坐标系变换到另一个坐标系，就需要求它在新坐标系每个基向量上的投影。
>
> — AI Sci Ke 理工柯小西，02:30–07:38；14:48–19:39；45:32–59:43

## I — 方法论骨架（Interpretation）

把任何正交变换拆成分析与综合两半。分析用对象和各基的内积求坐标；综合用坐标乘基并累加恢复对象。先标出对象、基、坐标与求和/积分变量，再检查两半能否互相复原。

核心公式：`cₖ = ⟨f,φₖ⟩；f = Σ cₖφₖ`。

## A1 — 视频中的应用（Past Application）

- **问题**：讲者需要把抽象公式还原为可理解、可迁移的结构。
- **方法论的使用**：三维向量先投影到新正交基得到坐标，再用这些坐标乘新基重建原向量；同一结构随后复用于函数积分变换和傅立叶公式。
- **结论**：该方法能在至少两个独立语境中复用，并通过阶段 1.5 三重验证。
- **结果**：形成可计算、可画图、可检查边界的傅立叶学习单元。

## A2 — 触发场景（Future Trigger）

### 用户会在什么情境下需要这个 skill？

1. 正在学习傅立叶、线性代数或微分方程，但公式之间缺少统一解释。
2. 需要诊断一段推导中的符号、尺度、基、边界或重建错误。
3. 希望把概念转成可运行的数值实验或教学步骤。

### 语言信号

- “为什么这个变换和逆变换长这样？”
- “帮我从投影角度推导公式”
- “analysis/synthesis 或 change of basis”

### 与相邻 skill 的区分

- `finite-to-function-space`：composes-with
- `orthogonal-basis-audit`：depends-on
- `fourier-series-analysis-synthesis`：composes-with

## E — 可执行步骤（Execution）

1. **标出原对象、候选基与内积**
   - 完成标准：已留下可核查的公式、条件或数值验证。
2. **逐基投影得到坐标并检查归一化**
   - 完成标准：已留下可核查的公式、条件或数值验证。
3. **以坐标乘基求和/积分并验证重建**
   - 完成标准：已留下可核查的公式、条件或数值验证。

4. **做反例核验**
   - 完成标准：至少检查一个边界或失败模式；若不满足前提，停止套用并明确说明。

## B — 边界（Boundary）

### 不要在以下情况使用

- 基不正交时不能直接把内积当坐标
- 未证明完备性时不能承诺精确重建

### 视频警告的失败模式

- 把直觉类比当成无限制的严格等同。
- 只看公式外形，不追踪区间、变量、微元、共轭和归一化。

### 讲解的局限

- 视频以工程直觉为主；涉及函数空间、完备性、收敛和广义函数时必须补充更严格条件。

## 相关 skills

- `finite-to-function-space`：composes-with
- `orthogonal-basis-audit`：depends-on
- `fourier-series-analysis-synthesis`：composes-with

## 审计信息

- **验证通过**：V1 ✓ / V2 ✓ / V3 ✓
- **测试目标**：100%（详见 `test-results.md`）
- **蒸馏时间**：2026-08-23
