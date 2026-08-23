---
name: complex-inner-product-audit
description: |
  当用户询问“傅立叶变换为什么有负号？”、complex conjugate / inner-product convention，或需要用该方法诊断数学推导时调用。执行时必须给出公式角色、适用条件与可验证结果。不适用于纯粹查定义，或问题实际属于 `projection-coordinate-reconstruction` 的情形。
source_book: 《工科生苦傅立叶久矣！傅立叶变换究极入门》 AI Sci Ke 理工柯小西
source_chapter: 17:35–19:39；57:51
tags: [fourier, mathematics, learning-system]
related_skills:
  - slug: projection-coordinate-reconstruction
    relation: depends-on
  - slug: fourier-convention-audit
    relation: composes-with
---

# 复内积的角色—共轭审计

## R — 原文（Reading）

> 复数函数在计算投影的时候一定要乘共轭；求线性组合时不用乘共轭。
>
> — AI Sci Ke 理工柯小西，17:35–19:39；57:51

## I — 方法论骨架（Interpretation）

不要按左右位置死记共轭，而按运算角色判断。分析/投影必须使用满足正定性的复内积，所以对一方取共轭；综合则用坐标乘原基。不同教材可把共轭放在第一或第二槽，但整套约定必须自洽。

核心公式：`⟨f,g⟩ = ∫f(t)overline{g(t)}dt`。

## A1 — 视频中的应用（Past Application）

- **问题**：讲者需要把抽象公式还原为可理解、可迁移的结构。
- **方法论的使用**：用 z=1+i 检验：z·z=2i 不能表示长度平方，而 z·conj(z)=2；同一规则解释傅立叶正变换负号与逆变换正号。
- **结论**：该方法能在至少两个独立语境中复用，并通过阶段 1.5 三重验证。
- **结果**：形成可计算、可画图、可检查边界的傅立叶学习单元。

## A2 — 触发场景（Future Trigger）

### 用户会在什么情境下需要这个 skill？

1. 正在学习傅立叶、线性代数或微分方程，但公式之间缺少统一解释。
2. 需要诊断一段推导中的符号、尺度、基、边界或重建错误。
3. 希望把概念转成可运行的数值实验或教学步骤。

### 语言信号

- “傅立叶变换为什么有负号？”
- “复内积共轭放哪边？”
- “complex conjugate / inner-product convention”

### 与相邻 skill 的区分

- `projection-coordinate-reconstruction`：depends-on
- `fourier-convention-audit`：composes-with

## E — 可执行步骤（Execution）

1. **标记当前公式是分析还是综合**
   - 完成标准：已留下可核查的公式、条件或数值验证。
2. **写出内积约定并做自内积正定性检查**
   - 完成标准：已留下可核查的公式、条件或数值验证。
3. **核对正逆变换符号与共轭是否配套**
   - 完成标准：已留下可核查的公式、条件或数值验证。

4. **做反例核验**
   - 完成标准：至少检查一个边界或失败模式；若不满足前提，停止套用并明确说明。

## B — 边界（Boundary）

### 不要在以下情况使用

- 实数空间中共轭退化为原值，不必制造复杂度
- 不能只凭指数正负号判断公式对错

### 视频警告的失败模式

- 把直觉类比当成无限制的严格等同。
- 只看公式外形，不追踪区间、变量、微元、共轭和归一化。

### 讲解的局限

- 视频以工程直觉为主；涉及函数空间、完备性、收敛和广义函数时必须补充更严格条件。

## 相关 skills

- `projection-coordinate-reconstruction`：depends-on
- `fourier-convention-audit`：composes-with

## 审计信息

- **验证通过**：V1 ✓ / V2 ✓ / V3 ✓
- **测试目标**：100%（详见 `test-results.md`）
- **蒸馏时间**：2026-08-23
