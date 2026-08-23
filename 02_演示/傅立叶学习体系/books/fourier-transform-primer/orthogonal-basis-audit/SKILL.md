---
name: orthogonal-basis-audit
description: |
  当用户询问“这组函数真的是一组基吗？”、orthogonal vs complete vs normalized，或需要用该方法诊断数学推导时调用。执行时必须给出公式角色、适用条件与可验证结果。不适用于纯粹查定义，或问题实际属于 `projection-coordinate-reconstruction` 的情形。
source_book: 《工科生苦傅立叶久矣！傅立叶变换究极入门》 AI Sci Ke 理工柯小西
source_chapter: 01:50–07:38；42:35–47:30
tags: [fourier, mathematics, learning-system]
related_skills:
  - slug: projection-coordinate-reconstruction
    relation: composes-with
  - slug: complex-exponential-frequency-pair
    relation: depends-on
  - slug: fourier-series-analysis-synthesis
    relation: composes-with
---

# 正交—完备—归一三项基审计

## R — 原文（Reading）

> 这组函数不但要正交，还必须是完备的；周期内积分以后还要除以周期。
>
> — AI Sci Ke 理工柯小西，01:50–07:38；42:35–47:30

## I — 方法论骨架（Interpretation）

评价一组候选基时分三关：正交性决定不同坐标是否串扰，完备性决定能否覆盖目标空间，归一化决定坐标尺度是否正确。三者不能互相替代；审计时还必须写明区间、内积和边界条件。

核心公式：`⟨φₘ,φₙ⟩=δₘₙ；一般 cₙ=⟨f,φₙ⟩/||φₙ||²`。

## A1 — 视频中的应用（Past Application）

- **问题**：讲者需要把抽象公式还原为可理解、可迁移的结构。
- **方法论的使用**：有限维新坐标系先要求单位正交；复指数函数族随后在整周期上验证正交，并以 1/T 修正周期积分的尺度。
- **结论**：该方法能在至少两个独立语境中复用，并通过阶段 1.5 三重验证。
- **结果**：形成可计算、可画图、可检查边界的傅立叶学习单元。

## A2 — 触发场景（Future Trigger）

### 用户会在什么情境下需要这个 skill？

1. 正在学习傅立叶、线性代数或微分方程，但公式之间缺少统一解释。
2. 需要诊断一段推导中的符号、尺度、基、边界或重建错误。
3. 希望把概念转成可运行的数值实验或教学步骤。

### 语言信号

- “这组函数真的是一组基吗？”
- “为什么还要除以 T？”
- “orthogonal vs complete vs normalized”

### 与相邻 skill 的区分

- `projection-coordinate-reconstruction`：composes-with
- `complex-exponential-frequency-pair`：depends-on
- `fourier-series-analysis-synthesis`：composes-with

## E — 可执行步骤（Execution）

1. **固定空间、区间和内积**
   - 完成标准：已留下可核查的公式、条件或数值验证。
2. **分别检验正交与范数**
   - 完成标准：已留下可核查的公式、条件或数值验证。
3. **检查完备性/重建误差并写出归一化系数**
   - 完成标准：已留下可核查的公式、条件或数值验证。

4. **做反例核验**
   - 完成标准：至少检查一个边界或失败模式；若不满足前提，停止套用并明确说明。

## B — 边界（Boundary）

### 不要在以下情况使用

- 两两正交不等于完备
- 非单位范数时坐标必须除以范数平方

### 视频警告的失败模式

- 把直觉类比当成无限制的严格等同。
- 只看公式外形，不追踪区间、变量、微元、共轭和归一化。

### 讲解的局限

- 视频以工程直觉为主；涉及函数空间、完备性、收敛和广义函数时必须补充更严格条件。

## 相关 skills

- `projection-coordinate-reconstruction`：composes-with
- `complex-exponential-frequency-pair`：depends-on
- `fourier-series-analysis-synthesis`：composes-with

## 审计信息

- **验证通过**：V1 ✓ / V2 ✓ / V3 ✓
- **测试目标**：100%（详见 `test-results.md`）
- **蒸馏时间**：2026-08-23
