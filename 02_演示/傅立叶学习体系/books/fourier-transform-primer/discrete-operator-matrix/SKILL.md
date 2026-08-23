---
name: discrete-operator-matrix
description: |
  当用户询问“怎样把导数写成矩阵？”、finite difference / operator matrix，或需要用该方法诊断数学推导时调用。执行时必须给出公式角色、适用条件与可验证结果。不适用于纯粹查定义，或问题实际属于 `discrete-continuous-limit` 的情形。
source_book: 《工科生苦傅立叶久矣！傅立叶变换究极入门》 AI Sci Ke 理工柯小西
source_chapter: 24:00–29:56
tags: [fourier, mathematics, learning-system]
related_skills:
  - slug: discrete-continuous-limit
    relation: depends-on
  - slug: finite-to-function-space
    relation: composes-with
  - slug: eigenfunction-operator-algebra
    relation: composes-with
---

# 连续算子的离散矩阵化

## R — 原文（Reading）

> 差分就是对一个向量求后一项和前一项的差；求和则是前 n 项累加，都可以写成矩阵。
>
> — AI Sci Ke 理工柯小西，24:00–29:56

## I — 方法论骨架（Interpretation）

用矩阵把连续算子变成可见、可算的有限模型。先在网格上构造差分或累加矩阵，明确每行怎样组合邻点，再研究网格缩小时它逼近哪个连续算子。端点行必须单独处理，因为边界条件决定算子。

核心公式：`f'(tᵢ) ≈ (fᵢ₊₁-fᵢ)/h`。

## A1 — 视频中的应用（Past Application）

- **问题**：讲者需要把抽象公式还原为可理解、可迁移的结构。
- **方法论的使用**：杭州最低气温用差分矩阵得到每日变化；国庆开销用下三角累加矩阵得到累计值；两者分别通向导数和积分直觉。
- **结论**：该方法能在至少两个独立语境中复用，并通过阶段 1.5 三重验证。
- **结果**：形成可计算、可画图、可检查边界的傅立叶学习单元。

## A2 — 触发场景（Future Trigger）

### 用户会在什么情境下需要这个 skill？

1. 正在学习傅立叶、线性代数或微分方程，但公式之间缺少统一解释。
2. 需要诊断一段推导中的符号、尺度、基、边界或重建错误。
3. 希望把概念转成可运行的数值实验或教学步骤。

### 语言信号

- “怎样把导数写成矩阵？”
- “差分矩阵边界怎么处理？”
- “finite difference / operator matrix”

### 与相邻 skill 的区分

- `discrete-continuous-limit`：depends-on
- `finite-to-function-space`：composes-with
- `eigenfunction-operator-algebra`：composes-with

## E — 可执行步骤（Execution）

1. **选网格并定义输入输出位置**
   - 完成标准：已留下可核查的公式、条件或数值验证。
2. **逐行构造矩阵并显式写端点规则**
   - 完成标准：已留下可核查的公式、条件或数值验证。
3. **用已知函数比较离散结果与连续算子**
   - 完成标准：已留下可核查的公式、条件或数值验证。

4. **做反例核验**
   - 完成标准：至少检查一个边界或失败模式；若不满足前提，停止套用并明确说明。

## B — 边界（Boundary）

### 不要在以下情况使用

- 末端伪差分不能当有效数据
- 网格过粗或函数不光滑时误差可能很大

### 视频警告的失败模式

- 把直觉类比当成无限制的严格等同。
- 只看公式外形，不追踪区间、变量、微元、共轭和归一化。

### 讲解的局限

- 视频以工程直觉为主；涉及函数空间、完备性、收敛和广义函数时必须补充更严格条件。

## 相关 skills

- `discrete-continuous-limit`：depends-on
- `finite-to-function-space`：composes-with
- `eigenfunction-operator-algebra`：composes-with

## 审计信息

- **验证通过**：V1 ✓ / V2 ✓ / V3 ✓
- **测试目标**：100%（详见 `test-results.md`）
- **蒸馏时间**：2026-08-23
