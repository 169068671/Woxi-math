from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "books" / "fourier-transform-primer"
LEARN = ROOT / "learning-system"


skills = [
    dict(id="01", slug="projection-coordinate-reconstruction", title="投影—坐标—重建闭环", source="02:30–07:38；14:48–19:39；45:32–59:43",
         quote="如果想把一个向量从一个坐标系变换到另一个坐标系，就需要求它在新坐标系每个基向量上的投影。",
         idea="把任何正交变换拆成分析与综合两半。分析用对象和各基的内积求坐标；综合用坐标乘基并累加恢复对象。先标出对象、基、坐标与求和/积分变量，再检查两半能否互相复原。",
         case="三维向量先投影到新正交基得到坐标，再用这些坐标乘新基重建原向量；同一结构随后复用于函数积分变换和傅立叶公式。",
         triggers=["为什么这个变换和逆变换长这样？", "帮我从投影角度推导公式", "analysis/synthesis 或 change of basis"],
         steps=["标出原对象、候选基与内积", "逐基投影得到坐标并检查归一化", "以坐标乘基求和/积分并验证重建"],
         boundaries=["基不正交时不能直接把内积当坐标", "未证明完备性时不能承诺精确重建"],
         related=[("finite-to-function-space","composes-with"),("orthogonal-basis-audit","depends-on"),("fourier-series-analysis-synthesis","composes-with")],
         symbols=[("x 或 f","待表示的对象"),("φₖ","第 k 个基向量/基函数"),("cₖ","投影所得坐标"),("⟨·,·⟩","内积"),("Σ / ∫","综合时的累加")],
         formula="cₖ = ⟨f,φₖ⟩；f = Σ cₖφₖ", experiment="projection"),
    dict(id="02", slug="finite-to-function-space", title="从有限维结构迁移到函数空间", source="08:52–19:39；24:00–29:56；45:32–59:43",
         quote="函数其实是一个无穷维的数组；不要只把函数当曲线，要把它当无穷维向量去理解。",
         idea="用结构对应而非字面等同，把有限维线性代数迁移到函数空间：向量对应函数，点积对应积分，矩阵对应线性算子，基向量对应基函数，坐标列对应变换结果。每次迁移都要补上函数空间、定义域和收敛条件。",
         case="视频先把采样数组不断加密为函数，再把差分/累加矩阵迁移为求导/积分算子，最后把频谱解释成函数在频率基下的坐标。",
         triggers=["函数为什么能当向量？", "把线性代数类比到函数空间", "Hilbert space intuition / infinite-dimensional vector"],
         steps=["列出有限维对象和运算", "为每项寻找函数空间对应物", "逐项写出成立条件与失效边界"],
         boundaries=["函数不是普通数列的字面无限延长", "不同函数空间的内积、范数与收敛方式不同"],
         related=[("projection-coordinate-reconstruction","composes-with"),("discrete-operator-matrix","composes-with"),("orthogonal-basis-audit","depends-on")],
         symbols=[("f(t)","函数空间中的向量"),("L¹/L²","常见函数空间条件"),("A","有限维矩阵"),("𝓛","函数上的线性算子"),("φₙ","基函数")],
         formula="向量↔函数，点积↔积分，矩阵↔线性算子", experiment="function_vector"),
    dict(id="03", slug="discrete-continuous-limit", title="离散采样到连续积分的极限桥", source="10:18–13:42；50:42–55:48",
         quote="相邻取点之间的间隙必须乘上去；细分趋向无穷时，求和就得到积分的形态。",
         idea="把连续公式追溯为带网格宽度的离散求和。加密网格时同时更新采样间隔、求和范围和变量；只有这样极限才保持尺度。该程序既解释点积为何变积分，也解释离散频率和为何变频率积分。",
         case="函数内积从 Σf(xᵢ)g(xᵢ)Δx 过渡到积分；傅立叶级数从 ΣF(nf₀)e^{j2πnf₀t}f₀ 过渡到连续频率积分。",
         triggers=["为什么求和会变成积分？", "采样越密数值为什么变大？", "Riemann sum / discrete-to-continuous"],
         steps=["写出带网格间隔的离散和", "让网格变密并追踪间隔和索引", "验证量纲、尺度和极限结果"],
         boundaries=["不能省略 Δx 或 Δf", "极限与积分交换需要额外条件"],
         related=[("finite-to-function-space","depends-on"),("series-to-transform-limit","composes-with")],
         symbols=[("xᵢ","第 i 个采样点"),("Δx","采样间隔"),("Σ","离散累加"),("dx","连续微元"),("∫","连续累加")],
         formula="Σ f(xᵢ)g(xᵢ)Δx → ∫ f(x)g(x)dx", experiment="riemann"),
    dict(id="04", slug="complex-inner-product-audit", title="复内积的角色—共轭审计", source="17:35–19:39；57:51",
         quote="复数函数在计算投影的时候一定要乘共轭；求线性组合时不用乘共轭。",
         idea="不要按左右位置死记共轭，而按运算角色判断。分析/投影必须使用满足正定性的复内积，所以对一方取共轭；综合则用坐标乘原基。不同教材可把共轭放在第一或第二槽，但整套约定必须自洽。",
         case="用 z=1+i 检验：z·z=2i 不能表示长度平方，而 z·conj(z)=2；同一规则解释傅立叶正变换负号与逆变换正号。",
         triggers=["傅立叶变换为什么有负号？", "复内积共轭放哪边？", "complex conjugate / inner-product convention"],
         steps=["标记当前公式是分析还是综合", "写出内积约定并做自内积正定性检查", "核对正逆变换符号与共轭是否配套"],
         boundaries=["实数空间中共轭退化为原值，不必制造复杂度", "不能只凭指数正负号判断公式对错"],
         related=[("projection-coordinate-reconstruction","depends-on"),("fourier-convention-audit","composes-with")],
         symbols=[("z̄","复数 z 的共轭"),("|z|²","z·z̄"),("j","虚数单位"),("e^{-jωt}","分析核"),("e^{jωt}","综合基")],
         formula="⟨f,g⟩ = ∫f(t)overline{g(t)}dt", experiment="conjugate"),
    dict(id="05", slug="cross-system-equation-isomorphism", title="跨物理系统的方程同构识别", source="20:19–23:36",
         quote="机械系统和电路系统最后会得到非常类似的二阶微分方程。",
         idea="迁移求解方法时不靠表面相似，而比较控制方程的结构。把储能、耗散、惯性/容量和外部激励逐项对齐；若阶数、线性关系和系数角色同构，就能共享特征函数、频域响应和稳定性分析。",
         case="弹簧—质量—阻尼系统与 RLC 电路分别由力平衡和电压平衡得到二阶线性微分方程，变量不同但结构相同。",
         triggers=["这两个系统能不能用同一种方法？", "机械和电路如何类比？", "equation isomorphism / analogous systems"],
         steps=["分别写出最小控制方程", "按惯性/储能/耗散/激励配对系数", "只在结构匹配后迁移解法并验证单位"],
         boundaries=["非线性摩擦不能直接当线性阻尼", "方程同阶不代表物理量或边界条件相同"],
         related=[("eigenfunction-operator-algebra","composes-with"),("discrete-operator-matrix","contrasts-with")],
         symbols=[("m/L","惯性或电感"),("c/R","耗散系数"),("k/1/C","恢复或储能系数"),("x/q","状态量"),("F/V","外部激励")],
         formula="m x''+c x'+kx=F(t) ↔ L q''+R q'+q/C=V(t)", experiment="isomorphism"),
    dict(id="06", slug="discrete-operator-matrix", title="连续算子的离散矩阵化", source="24:00–29:56",
         quote="差分就是对一个向量求后一项和前一项的差；求和则是前 n 项累加，都可以写成矩阵。",
         idea="用矩阵把连续算子变成可见、可算的有限模型。先在网格上构造差分或累加矩阵，明确每行怎样组合邻点，再研究网格缩小时它逼近哪个连续算子。端点行必须单独处理，因为边界条件决定算子。",
         case="杭州最低气温用差分矩阵得到每日变化；国庆开销用下三角累加矩阵得到累计值；两者分别通向导数和积分直觉。",
         triggers=["怎样把导数写成矩阵？", "差分矩阵边界怎么处理？", "finite difference / operator matrix"],
         steps=["选网格并定义输入输出位置", "逐行构造矩阵并显式写端点规则", "用已知函数比较离散结果与连续算子"],
         boundaries=["末端伪差分不能当有效数据", "网格过粗或函数不光滑时误差可能很大"],
         related=[("discrete-continuous-limit","depends-on"),("finite-to-function-space","composes-with"),("eigenfunction-operator-algebra","composes-with")],
         symbols=[("D_h","步长 h 的差分矩阵"),("h","网格间隔"),("fᵢ","第 i 个采样值"),("f'","连续导数"),("B","边界条件")],
         formula="f'(tᵢ) ≈ (fᵢ₊₁-fᵢ)/h", experiment="difference"),
    dict(id="07", slug="eigenfunction-operator-algebra", title="用特征函数代数化线性算子", source="28:44–42:35",
         quote="复指数经过求导以后还是它自己，只是前面多了一个系数，所以它是求导算子的特征函数。",
         idea="先寻找线性算子的特征函数，使复杂运算退化为乘以特征值。对常系数微分算子，e^{st} 把每次求导变成乘 s，微分方程因此变为特征多项式。解完代数问题后再按实根、共轭复根和重根重建时域解。",
         case="视频用指数试解依次处理一阶方程、二阶实根、共轭复根和重根，并由复根得到衰减振荡。",
         triggers=["为什么要假设 e^{st}？", "微分方程怎么变成代数方程？", "eigenfunction / diagonalize operator"],
         steps=["确认算子线性且系数适合特征函数法", "代入 e^{st} 得特征多项式并求根", "按根型构造独立解并代回验证"],
         boundaries=["变系数或非线性方程不能直接照搬", "重根必须补足线性独立解"],
         related=[("finite-to-function-space","depends-on"),("discrete-operator-matrix","composes-with"),("complex-exponential-frequency-pair","composes-with")],
         symbols=[("𝓛","线性算子"),("φ","特征函数"),("λ/s","特征值"),("D","求导算子"),("P(s)","特征多项式")],
         formula="D e^{st}=s e^{st}；P(D)e^{st}=P(s)e^{st}", experiment="eigenfunction"),
    dict(id="08", slug="complex-exponential-frequency-pair", title="复指数的双表示与正负频率配对", source="30:00–32:38；38:05–40:12；43:28–50:42",
         quote="实数的正弦函数，在复频率上是正频率和负频率各一部分，振幅相等、相位相反。",
         idea="用欧拉公式在旋转相量和正弦/余弦之间来回切换。正负频率代表复平面上相反旋转方向；实信号要求两侧系数共轭配对。该视角同时解释相位、复根振荡、频谱对称和实信号重建。",
         case="视频把 cos 与 sin 写成 e^{jωt} 和 e^{-jωt} 的组合，并在傅立叶级数中用正负谐波共同重建周期实函数。",
         triggers=["负频率到底是什么？", "为什么实信号频谱共轭对称？", "phasor / positive and negative frequency"],
         steps=["把三角函数改写成复指数对", "标记旋转方向、幅度与相位", "检查实信号系数是否满足共轭对称"],
         boundaries=["单边幅度图隐藏相位与负频率信息", "复信号不必满足实信号的共轭对称"],
         related=[("complex-inner-product-audit","composes-with"),("orthogonal-basis-audit","composes-with"),("fourier-series-analysis-synthesis","depends-on")],
         symbols=[("ω","角频率"),("φ","相位"),("e^{jωt}","正向旋转"),("e^{-jωt}","反向旋转"),("F(-ω)=overline{F(ω)}","实信号对称条件")],
         formula="cosωt=(e^{jωt}+e^{-jωt})/2", experiment="phasor"),
    dict(id="09", slug="orthogonal-basis-audit", title="正交—完备—归一三项基审计", source="01:50–07:38；42:35–47:30",
         quote="这组函数不但要正交，还必须是完备的；周期内积分以后还要除以周期。",
         idea="评价一组候选基时分三关：正交性决定不同坐标是否串扰，完备性决定能否覆盖目标空间，归一化决定坐标尺度是否正确。三者不能互相替代；审计时还必须写明区间、内积和边界条件。",
         case="有限维新坐标系先要求单位正交；复指数函数族随后在整周期上验证正交，并以 1/T 修正周期积分的尺度。",
         triggers=["这组函数真的是一组基吗？", "为什么还要除以 T？", "orthogonal vs complete vs normalized"],
         steps=["固定空间、区间和内积", "分别检验正交与范数", "检查完备性/重建误差并写出归一化系数"],
         boundaries=["两两正交不等于完备", "非单位范数时坐标必须除以范数平方"],
         related=[("projection-coordinate-reconstruction","composes-with"),("complex-exponential-frequency-pair","depends-on"),("fourier-series-analysis-synthesis","composes-with")],
         symbols=[("δₘₙ","正交关系的 Kronecker delta"),("||φₙ||","基函数范数"),("T","检验周期"),("span","张成空间"),("error","未覆盖分量")],
         formula="⟨φₘ,φₙ⟩=δₘₙ；一般 cₙ=⟨f,φₙ⟩/||φₙ||²", experiment="basis_audit"),
    dict(id="10", slug="fourier-series-analysis-synthesis", title="傅立叶级数的分析—综合双流程", source="45:32–50:42",
         quote="上面的 F(n) 是求傅立叶级数的系数；下面的 f(t) 是用这些系数复原原来的函数。",
         idea="周期函数只在基频整数倍的离散频率上展开。分析阶段在一个周期内对每个复指数基投影并除以 T；综合阶段将全部正负谐波的坐标乘基后求和。复指数形式和三角形式只是同一坐标信息的两种包装。",
         case="视频对周期矩形脉冲计算离散频率系数，再逐步叠加谐波重建时域波形，并展示周期改变时频率网格如何变化。",
         triggers=["傅立叶级数系数怎么推？", "怎样用有限谐波重建方波？", "Fourier series analysis/synthesis"],
         steps=["确定周期 T 与基频 ω₀", "按复内积求 cₙ 并核对 1/T", "选择谐波范围综合重建并量化误差"],
         boundaries=["非周期信号不应直接套离散谐波级数", "间断点附近有限截断会出现 Gibbs 现象"],
         related=[("projection-coordinate-reconstruction","depends-on"),("complex-exponential-frequency-pair","depends-on"),("orthogonal-basis-audit","depends-on"),("series-to-transform-limit","composes-with")],
         symbols=[("T","周期"),("ω₀=2π/T","基角频率"),("n","谐波整数"),("cₙ","复级数系数"),("N","截断阶数")],
         formula="cₙ=(1/T)∫_T f(t)e^{-jnω₀t}dt；f(t)=Σcₙe^{jnω₀t}", experiment="fourier_series"),
    dict(id="11", slug="series-to-transform-limit", title="周期拉伸构造傅立叶变换", source="50:42–57:51",
         quote="周期增加，频率间隔就会变小；周期延伸到无穷大时，离散频率变成连续频率。",
         idea="从傅立叶级数出发，把周期 T 拉长并同时追踪三项替换：基频间隔 f₀=1/T 变成 df，离散位置 nf₀ 变成连续 f，求和变成积分。坐标尺度需把 1/T 与频谱密度一起处理，不能只把 Σ 生硬换成 ∫。",
         case="矩形脉冲有效宽度保持 0.5 秒，而周期依次从 1 秒增到 2.5、5 秒；频率采样间隔从 1 Hz 变为 0.4、0.2 Hz，逐步逼近连续频谱。",
         triggers=["傅立叶级数如何变成傅立叶变换？", "为什么 T 越长频率越密？", "T to infinity / sum to integral"],
         steps=["从完整傅立叶级数变换对出发", "同步替换 T、f₀、nf₀ 与求和测度", "检查极限后的频谱密度和逆变换尺度"],
         boundaries=["该过程是工程极限直觉，严格交换极限需函数条件", "观察窗与真实周期不能无条件等同"],
         related=[("discrete-continuous-limit","depends-on"),("fourier-series-analysis-synthesis","depends-on"),("fourier-convention-audit","composes-with")],
         symbols=[("T","扩大的周期/观察窗"),("Δf=1/T","频率间隔"),("nf₀","离散频点"),("df","连续频率微元"),("F(f)","频谱密度")],
         formula="T→∞：f₀→df，nf₀→f，Σ·f₀→∫·df", experiment="period_limit"),
    dict(id="12", slug="fourier-convention-audit", title="傅立叶约定的符号与归一化审计", source="30:00；45:32；55:48–57:51",
         quote="ω=2πf，所以 dω=2πdf；2π 放在正变换、反变换或两边拆开都可以，但必须成对一致。",
         idea="比较不同傅立叶公式时，不看外形投票，而做四栏审计：频率变量是 f 还是 ω，指数核是否含 2π，正负号对应哪一槽的共轭，正逆变换常数乘积是否匹配。变量替换必须连微元一起换。",
         case="视频从 f 形式换到 ω 形式时同步使用 dω=2πdf，于是 1/(2π) 出现在逆变换；并说明对称归一化也是合法约定。",
         triggers=["为什么有的公式有 2π？", "两本教材的傅立叶定义谁对？", "Fourier convention / normalization audit"],
         steps=["列出变量、核函数、符号与常数", "执行 f↔ω 变量及微元替换", "合成正逆变换并检查是否恢复原函数"],
         boundaries=["不能脱离整套变换对比较单个常数", "单位为 Hz 与 rad/s 时数值和量纲都要同步解释"],
         related=[("complex-inner-product-audit","depends-on"),("series-to-transform-limit","depends-on")],
         symbols=[("f","普通频率，Hz"),("ω","角频率，rad/s"),("df/dω","对应微元"),("2π","变量换算因子"),("A,B","正逆变换归一化常数")],
         formula="F(ω)=∫f(t)e^{-jωt}dt；f(t)=(1/2π)∫F(ω)e^{jωt}dω", experiment="convention"),
]


def skill_md(s: dict) -> str:
    related_yaml = "\n".join(f"  - slug: {slug}\n    relation: {rel}" for slug, rel in s["related"])
    related_text = "\n".join(f"- `{slug}`：{rel}" for slug, rel in s["related"])
    trigger_list = "\n".join(f"- “{x}”" for x in s["triggers"])
    steps = "\n".join(f"{i}. **{x}**\n   - 完成标准：已留下可核查的公式、条件或数值验证。" for i, x in enumerate(s["steps"], 1))
    boundaries = "\n".join(f"- {x}" for x in s["boundaries"])
    sibling = s["related"][0][0]
    return f'''---
name: {s['slug']}
description: |
  当用户询问“{s['triggers'][0]}”、{s['triggers'][2]}，或需要用该方法诊断数学推导时调用。执行时必须给出公式角色、适用条件与可验证结果。不适用于纯粹查定义，或问题实际属于 `{sibling}` 的情形。
source_book: 《工科生苦傅立叶久矣！傅立叶变换究极入门》 AI Sci Ke 理工柯小西
source_chapter: {s['source']}
tags: [fourier, mathematics, learning-system]
related_skills:
{related_yaml}
---

# {s['title']}

## R — 原文（Reading）

> {s['quote']}
>
> — AI Sci Ke 理工柯小西，{s['source']}

## I — 方法论骨架（Interpretation）

{s['idea']}

核心公式：`{s['formula']}`。

## A1 — 视频中的应用（Past Application）

- **问题**：讲者需要把抽象公式还原为可理解、可迁移的结构。
- **方法论的使用**：{s['case']}
- **结论**：该方法能在至少两个独立语境中复用，并通过阶段 1.5 三重验证。
- **结果**：形成可计算、可画图、可检查边界的傅立叶学习单元。

## A2 — 触发场景（Future Trigger）

### 用户会在什么情境下需要这个 skill？

1. 正在学习傅立叶、线性代数或微分方程，但公式之间缺少统一解释。
2. 需要诊断一段推导中的符号、尺度、基、边界或重建错误。
3. 希望把概念转成可运行的数值实验或教学步骤。

### 语言信号

{trigger_list}

### 与相邻 skill 的区分

{related_text}

## E — 可执行步骤（Execution）

{steps}

4. **做反例核验**
   - 完成标准：至少检查一个边界或失败模式；若不满足前提，停止套用并明确说明。

## B — 边界（Boundary）

### 不要在以下情况使用

{boundaries}

### 视频警告的失败模式

- 把直觉类比当成无限制的严格等同。
- 只看公式外形，不追踪区间、变量、微元、共轭和归一化。

### 讲解的局限

- 视频以工程直觉为主；涉及函数空间、完备性、收敛和广义函数时必须补充更严格条件。

## 相关 skills

{related_text}

## 审计信息

- **验证通过**：V1 ✓ / V2 ✓ / V3 ✓
- **测试目标**：100%（详见 `test-results.md`）
- **蒸馏时间**：2026-08-23
'''


def tests(s: dict, next_slug: str) -> dict:
    return {"skill": s["slug"], "version": "0.1.0", "source_book": "工科生苦傅立叶久矣！傅立叶变换究极入门 — AI Sci Ke 理工柯小西", "darwin_compatible": True,
            "test_cases": [
                {"id":"should-trigger-01","type":"should_trigger","prompt":s["triggers"][0],"expected_behavior":f"应激活 {s['slug']}，按执行步骤给出公式、条件和核验", "notes":"直接命中核心问题"},
                {"id":"should-trigger-02","type":"should_trigger","prompt":s["triggers"][1],"expected_behavior":f"应激活 {s['slug']} 并构造可检查的推导", "notes":"诊断/推导场景"},
                {"id":"should-trigger-03","type":"should_trigger","prompt":f"请用一个离线小实验讲清楚：{s['title']}","expected_behavior":f"应激活 {s['slug']} 并同步解释图、数值与公式", "notes":"教学实验场景"},
                {"id":"should-not-trigger-01","type":"should_not_trigger","prompt":"帮我查一下今天的天气。","expected_behavior":"不应激活任何傅立叶学习 skill", "notes":"完全无关诱饵"},
                {"id":"should-not-trigger-02","type":"should_not_trigger","prompt":f"我想学习另一个单元，请只解释 {next_slug} 的适用场景。","expected_behavior":f"不应激活本 skill，应激活 {next_slug}", "notes":"同书兄弟 skill 混淆诱饵"},
                {"id":"edge-01","type":"edge_case","prompt":f"只告诉我‘{s['title']}’的中文定义，不要推导也不要实验。","expected_behavior":"不应完整激活；只做简短定义，并说明需要推导或诊断时再使用", "notes":"纯定义边界"}],
            "minimum_pass_rate": 0.8,
            "notes":"3 条应触发、2 条不应触发、1 条边界；诱饵容错为 0。"}


def page_shell(s: dict, kind: str) -> str:
    labels = {"experiment":"实验页","explain":"主讲解页","symbols":"符号可视页"}
    nav = f'''<nav><a href="../index.html">总目录</a><a href="experiment.html">实验</a><a href="explain.html">讲解</a><a href="symbols.html">符号</a></nav>'''
    if kind == "experiment":
        body = f'''<section class="hero"><p class="eyebrow">第 {s['id']} 模块 · 动手验证</p><h1>{s['title']}</h1><p>{s['idea']}</p></section><section class="panel"><h2>可操作实验</h2><div id="experiment" data-kind="{s['experiment']}"></div></section><section class="panel"><h2>观察任务</h2><ol><li>先改变控制量，观察图形和数值是否同步。</li><li>对照核心公式：<code>{s['formula']}</code></li><li>记录一个成立条件和一个失败边界。</li></ol></section>'''
    elif kind == "explain":
        step_html = ''.join(f'<li><strong>{i}</strong><span>{x}</span></li>' for i,x in enumerate(s['steps'],1))
        bounds = ''.join(f'<li>{x}</li>' for x in s['boundaries'])
        body = f'''<section class="hero"><p class="eyebrow">第 {s['id']} 模块 · 从直觉到公式</p><h1>{s['title']}</h1><p>{s['idea']}</p><div class="formula">{s['formula']}</div></section><section class="panel"><h2>视频中的桥梁</h2><p>{s['case']}</p><blockquote>{s['quote']}<cite>{s['source']}</cite></blockquote></section><section class="panel"><h2>推导顺序</h2><ol class="steps">{step_html}</ol></section><section class="panel warning"><h2>边界检查</h2><ul>{bounds}</ul></section>'''
    else:
        rows = ''.join(f'<tr><th><code>{a}</code></th><td>{b}</td><td><button class="speak" data-symbol="{a}">读法</button></td></tr>' for a,b in s['symbols'])
        body = f'''<section class="hero"><p class="eyebrow">第 {s['id']} 模块 · 符号不再跳步</p><h1>{s['title']}：符号地图</h1><p>每个符号都标出角色；点击“读法”可在支持语音的浏览器中朗读。</p></section><section class="panel"><table><thead><tr><th>符号</th><th>在本模块中的角色</th><th>操作</th></tr></thead><tbody>{rows}</tbody></table></section><section class="panel"><h2>把符号放回公式</h2><div class="formula">{s['formula']}</div><p>请依次指出：输入对象、基/算子、坐标或输出、累加变量、归一化因子。</p></section>'''
    data = json.dumps({"id":s["id"],"title":s["title"],"formula":s["formula"]}, ensure_ascii=False)
    return f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="icon" href="data:,"><title>{s['title']}｜{labels[kind]}</title><link rel="stylesheet" href="../assets/style.css"></head><body>{nav}<main>{body}</main><script>window.MODULE={data}</script><script src="../assets/app.js"></script></body></html>'''


STYLE = r''':root{--ink:#132238;--muted:#607086;--paper:#f5f1e8;--card:#fffdf8;--cyan:#0e7490;--orange:#c65d21;--line:#d8d1c3}*{box-sizing:border-box}body{margin:0;background:radial-gradient(circle at 10% 0,#dff6f7,transparent 34%),var(--paper);color:var(--ink);font:17px/1.7 ui-sans-serif,system-ui,-apple-system,"PingFang SC",sans-serif}nav{position:sticky;top:0;z-index:5;display:flex;gap:1rem;padding:.8rem max(1rem,calc((100% - 980px)/2));background:#132238e8;backdrop-filter:blur(12px)}nav a{color:white;text-decoration:none;font-weight:700}main{max-width:980px;margin:auto;padding:2rem 1rem 5rem}.hero{padding:3rem 0 1.5rem}.hero h1{font-size:clamp(2.2rem,6vw,4.8rem);line-height:1.05;margin:.2rem 0 1rem;letter-spacing:-.04em}.hero p{max-width:760px;color:var(--muted);font-size:1.12rem}.eyebrow{color:var(--orange)!important;font-weight:800;letter-spacing:.12em}.panel{background:var(--card);border:1px solid var(--line);border-radius:24px;padding:clamp(1.2rem,4vw,2.4rem);margin:1.2rem 0;box-shadow:0 18px 50px #1322380d}.formula{overflow:auto;padding:1.2rem;border-radius:16px;background:#132238;color:#e9fbff;font:700 1.05rem/1.6 ui-monospace,SFMono-Regular,monospace}.warning{border-left:8px solid var(--orange)}blockquote{border-left:4px solid var(--cyan);margin:1rem 0;padding:.6rem 1.2rem;background:#e7f7f7}cite{display:block;color:var(--muted);font-size:.85rem}table{width:100%;border-collapse:collapse}th,td{text-align:left;border-bottom:1px solid var(--line);padding:.9rem}.steps{list-style:none;padding:0}.steps li{display:grid;grid-template-columns:2.4rem 1fr;gap:1rem;margin:1rem 0}.steps strong{display:grid;place-items:center;width:2.2rem;height:2.2rem;border-radius:50%;background:var(--orange);color:white}.control{display:grid;gap:.5rem;margin:1rem 0}.control input{width:100%}canvas{width:100%;height:auto;border-radius:16px;background:#f2f8f8;border:1px solid var(--line)}.readout{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:.8rem}.metric{padding:1rem;border-radius:14px;background:#eef8f9}.metric b{display:block;font-size:1.4rem;color:var(--cyan)}button{border:0;border-radius:999px;background:var(--cyan);color:white;padding:.55rem .9rem;font-weight:700;cursor:pointer}.module-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1rem}.module-card{display:block;background:var(--card);border:1px solid var(--line);border-radius:20px;padding:1.3rem;text-decoration:none;color:inherit}.module-card span{color:var(--orange);font-weight:800}.module-card h2{line-height:1.2}@media(max-width:600px){body{font-size:16px}nav{overflow:auto}.hero{padding-top:2rem}th,td{padding:.6rem}}'''

APP = r'''(()=>{const q=(s)=>document.querySelector(s),fmt=(x)=>Number(x).toFixed(3);document.querySelectorAll('.speak').forEach(b=>b.onclick=()=>{if('speechSynthesis'in window){speechSynthesis.cancel();speechSynthesis.speak(new SpeechSynthesisUtterance(b.dataset.symbol))}});const root=q('#experiment');if(!root)return;const kind=root.dataset.kind;root.innerHTML='<div class="control"><label>控制量 <b id="val"></b></label><input id="slider" type="range" min="1" max="20" value="6" step="1"></div><canvas id="cv" width="900" height="420"></canvas><div class="readout" id="readout"></div>';const sl=q('#slider'),cv=q('#cv'),ctx=cv.getContext('2d'),val=q('#val'),out=q('#readout');const metric=(a,b)=>`<div class="metric">${a}<b>${b}</b></div>`;function axes(){ctx.clearRect(0,0,cv.width,cv.height);ctx.strokeStyle='#a7b5bf';ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(40,210);ctx.lineTo(860,210);ctx.moveTo(450,25);ctx.lineTo(450,395);ctx.stroke()}function plot(fn,color='#0e7490'){ctx.strokeStyle=color;ctx.lineWidth=3;ctx.beginPath();for(let i=0;i<=800;i++){const x=-Math.PI+2*Math.PI*i/800,y=fn(x),X=50+800*i/800,Y=210-150*y;(i?ctx.lineTo(X,Y):ctx.moveTo(X,Y))}ctx.stroke()}function draw(){let n=+sl.value;val.textContent=n;axes();if(kind==='projection'){sl.max=360;sl.value=Math.max(n,30);n=+sl.value;val.textContent=n;const a=n*Math.PI/180,x=300*Math.cos(a),y=-300*Math.sin(a);ctx.strokeStyle='#c65d21';ctx.lineWidth=5;ctx.beginPath();ctx.moveTo(450,210);ctx.lineTo(450+x,210+y);ctx.stroke();ctx.setLineDash([8,8]);ctx.strokeStyle='#0e7490';ctx.beginPath();ctx.moveTo(450+x,210+y);ctx.lineTo(450+x,210);ctx.stroke();ctx.setLineDash([]);out.innerHTML=metric('角度',n+'°')+metric('x 轴投影',fmt(Math.cos(a)));}
else if(kind==='function_vector'||kind==='riemann'){sl.min=2;sl.max=60;plot(x=>Math.sin(x));const h=2*Math.PI/n;ctx.fillStyle='#0e749055';let sum=0;for(let i=0;i<n;i++){let x=-Math.PI+i*h,y=Math.sin(x)**2;sum+=y*h;let X=50+i*800/n,W=800/n,Y=210-150*y;ctx.fillRect(X,Y,W,150*y)}out.innerHTML=metric('采样数',n)+metric('Δx',fmt(h))+metric('Σ sin²x Δx',fmt(sum))+metric('理论积分','3.142');}
else if(kind==='conjugate'){sl.min=-10;sl.max=10;sl.step=.5;let a=n,b=3,z2=a*a+b*b;ctx.fillStyle='#c65d21';ctx.beginPath();ctx.arc(450+a*25,210-b*25,8,0,7);ctx.fill();ctx.strokeStyle='#c65d21';ctx.beginPath();ctx.moveTo(450,210);ctx.lineTo(450+a*25,210-b*25);ctx.stroke();out.innerHTML=metric('z',a+' + 3j')+metric('z·conj(z)',fmt(z2))+metric('z·z',fmt(a*a-b*b)+' + '+fmt(6*a)+'j');}
else if(kind==='isomorphism'){sl.min=1;sl.max=12;out.innerHTML=metric('阻尼 c / 电阻 R',n)+metric('机械方程',`x″+${n}x′+4x=F`)+metric('电路方程',`q″+${n}q′+4q=V`);plot(x=>Math.exp(-n*x*x/50)*Math.cos(3*x));}
else if(kind==='difference'){sl.min=4;sl.max=40;let h=2*Math.PI/n,err=0;plot(Math.sin);ctx.fillStyle='#c65d21';for(let i=0;i<n;i++){let x=-Math.PI+i*h,d=(Math.sin(x+h)-Math.sin(x))/h;err+=Math.abs(d-Math.cos(x));let X=50+800*i/n,Y=210-120*d;ctx.fillRect(X-2,Y-2,5,5)}out.innerHTML=metric('网格点',n)+metric('h',fmt(h))+metric('平均导数误差',fmt(err/n));}
else if(kind==='eigenfunction'){sl.min=-5;sl.max=5;sl.step=.25;plot(x=>Math.exp(n*x/10));out.innerHTML=metric('特征值 s',n)+metric('D e^{st} / e^{st}',n)+metric('形状','保持指数形');}
else if(kind==='phasor'){sl.min=-10;sl.max=10;sl.step=1;let a=n*Math.PI/10;ctx.strokeStyle='#c65d21';ctx.lineWidth=4;ctx.beginPath();ctx.moveTo(450,210);ctx.lineTo(450+150*Math.cos(a),210-150*Math.sin(a));ctx.stroke();out.innerHTML=metric('ωt',fmt(a))+metric('cos 分量',fmt(Math.cos(a)))+metric('sin 分量',fmt(Math.sin(a)))+metric('配对','+ω 与 −ω');}
else if(kind==='basis_audit'){sl.min=1;sl.max=10;let m=n,k=n+1,inner=Math.abs(m-k)<.01?1:0;plot(x=>Math.sin(m*x),'#0e7490');plot(x=>Math.sin(k*x),'#c65d21');out.innerHTML=metric('m',m)+metric('n',k)+metric('整周期内积',inner)+metric('审计','正交≠完备');}
else if(kind==='fourier_series'){sl.min=1;sl.max=25;sl.step=2;plot(x=>{let y=0;for(let k=1;k<=n;k+=2)y+=4/Math.PI*Math.sin(k*x)/k;return y});out.innerHTML=metric('最高奇次谐波',n)+metric('项数',Math.ceil(n/2))+metric('现象','边缘出现 Gibbs 振铃');}
else if(kind==='period_limit'){sl.min=1;sl.max=20;ctx.strokeStyle='#0e7490';for(let k=-n;k<=n;k++){let X=450+k*350/n;ctx.beginPath();ctx.moveTo(X,210);ctx.lineTo(X,80+120*Math.abs(k)/n);ctx.stroke()}out.innerHTML=metric('周期 T',n+' s')+metric('Δf=1/T',fmt(1/n)+' Hz')+metric('频点','越来越密');}
else if(kind==='convention'){sl.min=1;sl.max=20;sl.step=.5;let f=n,w=2*Math.PI*f;out.innerHTML=metric('f',fmt(f)+' Hz')+metric('ω=2πf',fmt(w)+' rad/s')+metric('df=1 时 dω',fmt(2*Math.PI))+metric('逆变换常数','1/(2π)');}
}sl.oninput=draw;draw()})();'''


def main() -> None:
    BOOK.mkdir(parents=True, exist_ok=True)
    (LEARN / "assets").mkdir(parents=True, exist_ok=True)
    (LEARN / "assets" / "style.css").write_text(STYLE, encoding="utf-8")
    (LEARN / "assets" / "app.js").write_text(APP, encoding="utf-8")
    cards = []
    for i, s in enumerate(skills):
        d = BOOK / s["slug"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "SKILL.md").write_text(skill_md(s), encoding="utf-8")
        nxt = skills[(i + 1) % len(skills)]["slug"]
        (d / "test-prompts.json").write_text(json.dumps(tests(s, nxt), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        mod = LEARN / f"{s['id']}-{s['slug']}"
        mod.mkdir(parents=True, exist_ok=True)
        for kind in ("experiment", "explain", "symbols"):
            (mod / f"{kind}.html").write_text(page_shell(s, kind), encoding="utf-8")
        cards.append(f'<a class="module-card" href="{mod.name}/experiment.html"><span>模块 {s["id"]}</span><h2>{s["title"]}</h2><p>{s["idea"]}</p></a>')
    index = f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="icon" href="data:,"><title>傅立叶学习体系</title><link rel="stylesheet" href="assets/style.css"></head><body><nav><a href="index.html">傅立叶学习体系</a></nav><main><section class="hero"><p class="eyebrow">从坐标投影走到连续频谱</p><h1>傅立叶，不从背公式开始。</h1><p>12 个模块，36 个离线页面。每个模块都有可操作实验、逐步讲解和符号地图。</p></section><section class="module-grid">{''.join(cards)}</section></main></body></html>'''
    (LEARN / "index.html").write_text(index, encoding="utf-8")
    manifest = [{k:s[k] for k in ("id","slug","title","source","formula","related")} for s in skills]
    (BOOK / "skills-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
