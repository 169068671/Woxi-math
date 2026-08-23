---
name: eigenfunction-operator-algebra
description: |
  当用户询问“为什么要假设 e^{st}？”、eigenfunction / diagonalize operator，或需要用该方法诊断数学推导时调用。执行时必须给出公式角色、适用条件与可验证结果。不适用于纯粹查定义，或问题实际属于 `finite-to-function-space` 的情形。
source_book: 《工科生苦傅立叶久矣！傅立叶变换究极入门》 AI Sci Ke 理工柯小西
source_chapter: 28:44–42:35
tags: [fourier, mathematics, learning-system]
related_skills:
  - slug: finite-to-function-space
    relation: depends-on
  - slug: discrete-operator-matrix
    relation: composes-with
  - slug: complex-exponential-frequency-pair
    relation: composes-with
---

# 用特征函数代数化线性算子

## R — 原文（Reading）

> 复指数经过求导以后还是它自己，只是前面多了一个系数，所以它是求导算子的特征函数。
>
> — AI Sci Ke 理工柯小西，28:44–42:35

## I — 方法论骨架（Interpretation）

先寻找线性算子的特征函数，使复杂运算退化为乘以特征值。对常系数微分算子，e^{st} 把每次求导变成乘 s，微分方程因此变为特征多项式。解完代数问题后再按实根、共轭复根和重根重建时域解。

核心公式：`D e^{st}=s e^{st}；P(D)e^{st}=P(s)e^{st}`。

## A1 — 视频中的应用（Past Application）

- **问题**：讲者需要把抽象公式还原为可理解、可迁移的结构。
- **方法论的使用**：视频用指数试解依次处理一阶方程、二阶实根、共轭复根和重根，并由复根得到衰减振荡。
- **结论**：该方法能在至少两个独立语境中复用，并通过阶段 1.5 三重验证。
- **结果**：形成可计算、可画图、可检查边界的傅立叶学习单元。

## A2 — 触发场景（Future Trigger）

### 用户会在什么情境下需要这个 skill？

1. 正在学习傅立叶、线性代数或微分方程，但公式之间缺少统一解释。
2. 需要诊断一段推导中的符号、尺度、基、边界或重建错误。
3. 希望把概念转成可运行的数值实验或教学步骤。

### 语言信号

- “为什么要假设 e^{st}？”
- “微分方程怎么变成代数方程？”
- “eigenfunction / diagonalize operator”

### 与相邻 skill 的区分

- `finite-to-function-space`：depends-on
- `discrete-operator-matrix`：composes-with
- `complex-exponential-frequency-pair`：composes-with

## E — 可执行步骤（Execution）

1. **确认算子线性且系数适合特征函数法**
   - 完成标准：已留下可核查的公式、条件或数值验证。
2. **代入 e^{st} 得特征多项式并求根**
   - 完成标准：已留下可核查的公式、条件或数值验证。
3. **按根型构造独立解并代回验证**
   - 完成标准：已留下可核查的公式、条件或数值验证。

4. **做反例核验**
   - 完成标准：至少检查一个边界或失败模式；若不满足前提，停止套用并明确说明。

## B — 边界（Boundary）

### 不要在以下情况使用

- 变系数或非线性方程不能直接照搬
- 重根必须补足线性独立解

### 视频警告的失败模式

- 把直觉类比当成无限制的严格等同。
- 只看公式外形，不追踪区间、变量、微元、共轭和归一化。

### 讲解的局限

- 视频以工程直觉为主；涉及函数空间、完备性、收敛和广义函数时必须补充更严格条件。

## 相关 skills

- `finite-to-function-space`：depends-on
- `discrete-operator-matrix`：composes-with
- `complex-exponential-frequency-pair`：composes-with

## 审计信息

- **验证通过**：V1 ✓ / V2 ✓ / V3 ✓
- **测试目标**：100%（详见 `test-results.md`）
- **蒸馏时间**：2026-08-23
