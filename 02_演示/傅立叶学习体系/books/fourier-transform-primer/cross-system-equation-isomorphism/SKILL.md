---
name: cross-system-equation-isomorphism
description: |
  当用户询问“这两个系统能不能用同一种方法？”、equation isomorphism / analogous systems，或需要用该方法诊断数学推导时调用。执行时必须给出公式角色、适用条件与可验证结果。不适用于纯粹查定义，或问题实际属于 `eigenfunction-operator-algebra` 的情形。
source_book: 《工科生苦傅立叶久矣！傅立叶变换究极入门》 AI Sci Ke 理工柯小西
source_chapter: 20:19–23:36
tags: [fourier, mathematics, learning-system]
related_skills:
  - slug: eigenfunction-operator-algebra
    relation: composes-with
  - slug: discrete-operator-matrix
    relation: contrasts-with
---

# 跨物理系统的方程同构识别

## R — 原文（Reading）

> 机械系统和电路系统最后会得到非常类似的二阶微分方程。
>
> — AI Sci Ke 理工柯小西，20:19–23:36

## I — 方法论骨架（Interpretation）

迁移求解方法时不靠表面相似，而比较控制方程的结构。把储能、耗散、惯性/容量和外部激励逐项对齐；若阶数、线性关系和系数角色同构，就能共享特征函数、频域响应和稳定性分析。

核心公式：`m x''+c x'+kx=F(t) ↔ L q''+R q'+q/C=V(t)`。

## A1 — 视频中的应用（Past Application）

- **问题**：讲者需要把抽象公式还原为可理解、可迁移的结构。
- **方法论的使用**：弹簧—质量—阻尼系统与 RLC 电路分别由力平衡和电压平衡得到二阶线性微分方程，变量不同但结构相同。
- **结论**：该方法能在至少两个独立语境中复用，并通过阶段 1.5 三重验证。
- **结果**：形成可计算、可画图、可检查边界的傅立叶学习单元。

## A2 — 触发场景（Future Trigger）

### 用户会在什么情境下需要这个 skill？

1. 正在学习傅立叶、线性代数或微分方程，但公式之间缺少统一解释。
2. 需要诊断一段推导中的符号、尺度、基、边界或重建错误。
3. 希望把概念转成可运行的数值实验或教学步骤。

### 语言信号

- “这两个系统能不能用同一种方法？”
- “机械和电路如何类比？”
- “equation isomorphism / analogous systems”

### 与相邻 skill 的区分

- `eigenfunction-operator-algebra`：composes-with
- `discrete-operator-matrix`：contrasts-with

## E — 可执行步骤（Execution）

1. **分别写出最小控制方程**
   - 完成标准：已留下可核查的公式、条件或数值验证。
2. **按惯性/储能/耗散/激励配对系数**
   - 完成标准：已留下可核查的公式、条件或数值验证。
3. **只在结构匹配后迁移解法并验证单位**
   - 完成标准：已留下可核查的公式、条件或数值验证。

4. **做反例核验**
   - 完成标准：至少检查一个边界或失败模式；若不满足前提，停止套用并明确说明。

## B — 边界（Boundary）

### 不要在以下情况使用

- 非线性摩擦不能直接当线性阻尼
- 方程同阶不代表物理量或边界条件相同

### 视频警告的失败模式

- 把直觉类比当成无限制的严格等同。
- 只看公式外形，不追踪区间、变量、微元、共轭和归一化。

### 讲解的局限

- 视频以工程直觉为主；涉及函数空间、完备性、收敛和广义函数时必须补充更严格条件。

## 相关 skills

- `eigenfunction-operator-algebra`：composes-with
- `discrete-operator-matrix`：contrasts-with

## 审计信息

- **验证通过**：V1 ✓ / V2 ✓ / V3 ✓
- **测试目标**：100%（详见 `test-results.md`）
- **蒸馏时间**：2026-08-23
