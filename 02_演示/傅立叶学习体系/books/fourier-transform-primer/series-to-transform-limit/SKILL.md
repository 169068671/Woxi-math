---
name: series-to-transform-limit
description: |
  当用户询问“傅立叶级数如何变成傅立叶变换？”、T to infinity / sum to integral，或需要用该方法诊断数学推导时调用。执行时必须给出公式角色、适用条件与可验证结果。不适用于纯粹查定义，或问题实际属于 `discrete-continuous-limit` 的情形。
source_book: 《工科生苦傅立叶久矣！傅立叶变换究极入门》 AI Sci Ke 理工柯小西
source_chapter: 50:42–57:51
tags: [fourier, mathematics, learning-system]
related_skills:
  - slug: discrete-continuous-limit
    relation: depends-on
  - slug: fourier-series-analysis-synthesis
    relation: depends-on
  - slug: fourier-convention-audit
    relation: composes-with
---

# 周期拉伸构造傅立叶变换

## R — 原文（Reading）

> 周期增加，频率间隔就会变小；周期延伸到无穷大时，离散频率变成连续频率。
>
> — AI Sci Ke 理工柯小西，50:42–57:51

## I — 方法论骨架（Interpretation）

从傅立叶级数出发，把周期 T 拉长并同时追踪三项替换：基频间隔 f₀=1/T 变成 df，离散位置 nf₀ 变成连续 f，求和变成积分。坐标尺度需把 1/T 与频谱密度一起处理，不能只把 Σ 生硬换成 ∫。

核心公式：`T→∞：f₀→df，nf₀→f，Σ·f₀→∫·df`。

## A1 — 视频中的应用（Past Application）

- **问题**：讲者需要把抽象公式还原为可理解、可迁移的结构。
- **方法论的使用**：矩形脉冲有效宽度保持 0.5 秒，而周期依次从 1 秒增到 2.5、5 秒；频率采样间隔从 1 Hz 变为 0.4、0.2 Hz，逐步逼近连续频谱。
- **结论**：该方法能在至少两个独立语境中复用，并通过阶段 1.5 三重验证。
- **结果**：形成可计算、可画图、可检查边界的傅立叶学习单元。

## A2 — 触发场景（Future Trigger）

### 用户会在什么情境下需要这个 skill？

1. 正在学习傅立叶、线性代数或微分方程，但公式之间缺少统一解释。
2. 需要诊断一段推导中的符号、尺度、基、边界或重建错误。
3. 希望把概念转成可运行的数值实验或教学步骤。

### 语言信号

- “傅立叶级数如何变成傅立叶变换？”
- “为什么 T 越长频率越密？”
- “T to infinity / sum to integral”

### 与相邻 skill 的区分

- `discrete-continuous-limit`：depends-on
- `fourier-series-analysis-synthesis`：depends-on
- `fourier-convention-audit`：composes-with

## E — 可执行步骤（Execution）

1. **从完整傅立叶级数变换对出发**
   - 完成标准：已留下可核查的公式、条件或数值验证。
2. **同步替换 T、f₀、nf₀ 与求和测度**
   - 完成标准：已留下可核查的公式、条件或数值验证。
3. **检查极限后的频谱密度和逆变换尺度**
   - 完成标准：已留下可核查的公式、条件或数值验证。

4. **做反例核验**
   - 完成标准：至少检查一个边界或失败模式；若不满足前提，停止套用并明确说明。

## B — 边界（Boundary）

### 不要在以下情况使用

- 该过程是工程极限直觉，严格交换极限需函数条件
- 观察窗与真实周期不能无条件等同

### 视频警告的失败模式

- 把直觉类比当成无限制的严格等同。
- 只看公式外形，不追踪区间、变量、微元、共轭和归一化。

### 讲解的局限

- 视频以工程直觉为主；涉及函数空间、完备性、收敛和广义函数时必须补充更严格条件。

## 相关 skills

- `discrete-continuous-limit`：depends-on
- `fourier-series-analysis-synthesis`：depends-on
- `fourier-convention-audit`：composes-with

## 审计信息

- **验证通过**：V1 ✓ / V2 ✓ / V3 ✓
- **测试目标**：100%（详见 `test-results.md`）
- **蒸馏时间**：2026-08-23
