---
name: fourier-convention-audit
description: |
  当用户询问“为什么有的公式有 2π？”、Fourier convention / normalization audit，或需要用该方法诊断数学推导时调用。执行时必须给出公式角色、适用条件与可验证结果。不适用于纯粹查定义，或问题实际属于 `complex-inner-product-audit` 的情形。
source_book: 《工科生苦傅立叶久矣！傅立叶变换究极入门》 AI Sci Ke 理工柯小西
source_chapter: 30:00；45:32；55:48–57:51
tags: [fourier, mathematics, learning-system]
related_skills:
  - slug: complex-inner-product-audit
    relation: depends-on
  - slug: series-to-transform-limit
    relation: depends-on
---

# 傅立叶约定的符号与归一化审计

## R — 原文（Reading）

> ω=2πf，所以 dω=2πdf；2π 放在正变换、反变换或两边拆开都可以，但必须成对一致。
>
> — AI Sci Ke 理工柯小西，30:00；45:32；55:48–57:51

## I — 方法论骨架（Interpretation）

比较不同傅立叶公式时，不看外形投票，而做四栏审计：频率变量是 f 还是 ω，指数核是否含 2π，正负号对应哪一槽的共轭，正逆变换常数乘积是否匹配。变量替换必须连微元一起换。

核心公式：`F(ω)=∫f(t)e^{-jωt}dt；f(t)=(1/2π)∫F(ω)e^{jωt}dω`。

## A1 — 视频中的应用（Past Application）

- **问题**：讲者需要把抽象公式还原为可理解、可迁移的结构。
- **方法论的使用**：视频从 f 形式换到 ω 形式时同步使用 dω=2πdf，于是 1/(2π) 出现在逆变换；并说明对称归一化也是合法约定。
- **结论**：该方法能在至少两个独立语境中复用，并通过阶段 1.5 三重验证。
- **结果**：形成可计算、可画图、可检查边界的傅立叶学习单元。

## A2 — 触发场景（Future Trigger）

### 用户会在什么情境下需要这个 skill？

1. 正在学习傅立叶、线性代数或微分方程，但公式之间缺少统一解释。
2. 需要诊断一段推导中的符号、尺度、基、边界或重建错误。
3. 希望把概念转成可运行的数值实验或教学步骤。

### 语言信号

- “为什么有的公式有 2π？”
- “两本教材的傅立叶定义谁对？”
- “Fourier convention / normalization audit”

### 与相邻 skill 的区分

- `complex-inner-product-audit`：depends-on
- `series-to-transform-limit`：depends-on

## E — 可执行步骤（Execution）

1. **列出变量、核函数、符号与常数**
   - 完成标准：已留下可核查的公式、条件或数值验证。
2. **执行 f↔ω 变量及微元替换**
   - 完成标准：已留下可核查的公式、条件或数值验证。
3. **合成正逆变换并检查是否恢复原函数**
   - 完成标准：已留下可核查的公式、条件或数值验证。

4. **做反例核验**
   - 完成标准：至少检查一个边界或失败模式；若不满足前提，停止套用并明确说明。

## B — 边界（Boundary）

### 不要在以下情况使用

- 不能脱离整套变换对比较单个常数
- 单位为 Hz 与 rad/s 时数值和量纲都要同步解释

### 视频警告的失败模式

- 把直觉类比当成无限制的严格等同。
- 只看公式外形，不追踪区间、变量、微元、共轭和归一化。

### 讲解的局限

- 视频以工程直觉为主；涉及函数空间、完备性、收敛和广义函数时必须补充更严格条件。

## 相关 skills

- `complex-inner-product-audit`：depends-on
- `series-to-transform-limit`：depends-on

## 审计信息

- **验证通过**：V1 ✓ / V2 ✓ / V3 ✓
- **测试目标**：100%（详见 `test-results.md`）
- **蒸馏时间**：2026-08-23
