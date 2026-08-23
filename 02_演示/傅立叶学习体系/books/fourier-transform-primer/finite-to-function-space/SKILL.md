---
name: finite-to-function-space
description: |
  当用户询问“函数为什么能当向量？”、Hilbert space intuition / infinite-dimensional vector，或需要用该方法诊断数学推导时调用。执行时必须给出公式角色、适用条件与可验证结果。不适用于纯粹查定义，或问题实际属于 `projection-coordinate-reconstruction` 的情形。
source_book: 《工科生苦傅立叶久矣！傅立叶变换究极入门》 AI Sci Ke 理工柯小西
source_chapter: 08:52–19:39；24:00–29:56；45:32–59:43
tags: [fourier, mathematics, learning-system]
related_skills:
  - slug: projection-coordinate-reconstruction
    relation: composes-with
  - slug: discrete-operator-matrix
    relation: composes-with
  - slug: orthogonal-basis-audit
    relation: depends-on
---

# 从有限维结构迁移到函数空间

## R — 原文（Reading）

> 函数其实是一个无穷维的数组；不要只把函数当曲线，要把它当无穷维向量去理解。
>
> — AI Sci Ke 理工柯小西，08:52–19:39；24:00–29:56；45:32–59:43

## I — 方法论骨架（Interpretation）

用结构对应而非字面等同，把有限维线性代数迁移到函数空间：向量对应函数，点积对应积分，矩阵对应线性算子，基向量对应基函数，坐标列对应变换结果。每次迁移都要补上函数空间、定义域和收敛条件。

核心公式：`向量↔函数，点积↔积分，矩阵↔线性算子`。

## A1 — 视频中的应用（Past Application）

- **问题**：讲者需要把抽象公式还原为可理解、可迁移的结构。
- **方法论的使用**：视频先把采样数组不断加密为函数，再把差分/累加矩阵迁移为求导/积分算子，最后把频谱解释成函数在频率基下的坐标。
- **结论**：该方法能在至少两个独立语境中复用，并通过阶段 1.5 三重验证。
- **结果**：形成可计算、可画图、可检查边界的傅立叶学习单元。

## A2 — 触发场景（Future Trigger）

### 用户会在什么情境下需要这个 skill？

1. 正在学习傅立叶、线性代数或微分方程，但公式之间缺少统一解释。
2. 需要诊断一段推导中的符号、尺度、基、边界或重建错误。
3. 希望把概念转成可运行的数值实验或教学步骤。

### 语言信号

- “函数为什么能当向量？”
- “把线性代数类比到函数空间”
- “Hilbert space intuition / infinite-dimensional vector”

### 与相邻 skill 的区分

- `projection-coordinate-reconstruction`：composes-with
- `discrete-operator-matrix`：composes-with
- `orthogonal-basis-audit`：depends-on

## E — 可执行步骤（Execution）

1. **列出有限维对象和运算**
   - 完成标准：已留下可核查的公式、条件或数值验证。
2. **为每项寻找函数空间对应物**
   - 完成标准：已留下可核查的公式、条件或数值验证。
3. **逐项写出成立条件与失效边界**
   - 完成标准：已留下可核查的公式、条件或数值验证。

4. **做反例核验**
   - 完成标准：至少检查一个边界或失败模式；若不满足前提，停止套用并明确说明。

## B — 边界（Boundary）

### 不要在以下情况使用

- 函数不是普通数列的字面无限延长
- 不同函数空间的内积、范数与收敛方式不同

### 视频警告的失败模式

- 把直觉类比当成无限制的严格等同。
- 只看公式外形，不追踪区间、变量、微元、共轭和归一化。

### 讲解的局限

- 视频以工程直觉为主；涉及函数空间、完备性、收敛和广义函数时必须补充更严格条件。

## 相关 skills

- `projection-coordinate-reconstruction`：composes-with
- `discrete-operator-matrix`：composes-with
- `orthogonal-basis-audit`：depends-on

## 审计信息

- **验证通过**：V1 ✓ / V2 ✓ / V3 ✓
- **测试目标**：100%（详见 `test-results.md`）
- **蒸馏时间**：2026-08-23
