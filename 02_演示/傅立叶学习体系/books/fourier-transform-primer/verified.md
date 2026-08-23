# 阶段 1.5：三重验证通过单元

> 原始候选池共 90 条：17 个框架、25 条原则、15 个案例、15 个反例、18 个术语。案例与术语作为 A1/共享词典素材保留；框架、原则和反例经去重后形成 17 个方法论簇，其中 12 个通过 V1/V2/V3，5 个未通过或降级合并。

---

- id: v01
  title: 投影—坐标—重建闭环
  type: framework
  merged_from: [f01, f04, f14, p02, p03, p07, p19, ce04]
  V1_cross_domain:
    passed: true
    evidence:
      - "02:30–07:38：有限维向量换基"
      - "14:48–19:39：函数积分变换"
      - "45:32–59:43：傅立叶级数与变换"
  V2_predictive_power:
    passed: true
    novel_question: "面对一种没学过的正交变换，怎样判断正变换和逆变换各自在做什么？"
    derived_answer: "先识别基函数；正变换通常以对象和基的内积求坐标，逆变换则以坐标乘基并累加。再检查归一化和共轭约定。"
  V3_exclusivity:
    passed: true
    why_not_common: "不是泛泛的‘理解公式’，而是用同一个分析—综合闭环统一有限维换基、积分变换、傅立叶级数和傅立叶变换。"
  decision: 进入阶段 2

- id: v02
  title: 从有限维结构迁移到函数空间
  type: framework
  merged_from: [f03, p04, p06, g05, g06]
  V1_cross_domain:
    passed: true
    evidence:
      - "08:52–14:48：数组加密后把函数解释为无穷维向量"
      - "24:00–29:56：把求导和积分解释为函数空间的线性算子"
      - "45:32–59:43：把频率函数族解释为坐标基"
  V2_predictive_power:
    passed: true
    novel_question: "怎样从矩阵知识猜出一个新积分变换需要哪些构件？"
    derived_answer: "寻找对象空间、基/核函数、内积、投影系数、综合公式与可逆条件，分别对应向量、基、点积、坐标和矩阵逆变换。"
  V3_exclusivity:
    passed: true
    why_not_common: "视频的差异化入口是把函数空间概念系统映射回线性代数，而不是把‘函数像向量’停留在比喻层。"
  decision: 进入阶段 2

- id: v03
  title: 离散采样到连续积分的极限桥
  type: framework
  merged_from: [f02, p05, ce02, c02, c03]
  V1_cross_domain:
    passed: true
    evidence:
      - "10:18–13:42：点积经带采样间隔的黎曼和变成函数内积"
      - "50:42–55:48：离散频率求和经 Δf→df 变成频率积分"
  V2_predictive_power:
    passed: true
    novel_question: "一个离散算法要推广到连续对象时，最容易漏掉什么？"
    derived_answer: "必须保留网格间隔/测度权重，并同时追踪求和范围、索引变量和归一化；否则加密采样会让数值无故发散或缩放错误。"
  V3_exclusivity:
    passed: true
    why_not_common: "它把两个看似不同的过渡——点积到积分、傅立叶级数到变换——统一为同一套测度加权极限程序。"
  decision: 进入阶段 2

- id: v04
  title: 复内积的角色—共轭审计
  type: framework
  merged_from: [f05, p08, p09, p23, ce05, ce06, g07]
  V1_cross_domain:
    passed: true
    evidence:
      - "17:35–18:36：用 1+i 的自内积说明为何必须取共轭"
      - "19:07–19:39：一般复积分变换中区分投影与综合"
      - "57:51：傅立叶正变换负号与反变换正号"
  V2_predictive_power:
    passed: true
    novel_question: "遇到新教材把共轭写在内积的另一边，怎样判断它是否错误？"
    derived_answer: "不靠位置记忆，而检查内积约定、正定性与分析/综合角色；只要整套约定自洽并满足 ⟨f,f⟩≥0，就可能是合法写法。"
  V3_exclusivity:
    passed: true
    why_not_common: "把傅立叶核的正负号追溯到‘投影要共轭、综合用原基’的角色判断，比背公式更具迁移性。"
  decision: 进入阶段 2

- id: v05
  title: 跨物理系统的方程同构识别
  type: framework
  merged_from: [f06, c05, c06]
  V1_cross_domain:
    passed: true
    evidence:
      - "20:19–22:40：弹簧—质量—阻尼机械系统"
      - "23:03–23:36：RLC 电路系统"
  V2_predictive_power:
    passed: true
    novel_question: "热系统或流体系统能否复用机械系统的求解方法？"
    derived_answer: "先把储能、耗散、惯性/容量和外部激励逐项对应；若得到同阶同系数结构的线性微分方程，就能迁移相同的特征函数与频域分析。"
  V3_exclusivity:
    passed: true
    why_not_common: "不是笼统类比，而是以微分方程的结构同构为可检验的迁移标准。"
  decision: 进入阶段 2

- id: v06
  title: 连续算子的离散矩阵化
  type: framework
  merged_from: [f07, p10, c07, c08, ce08, g09]
  V1_cross_domain:
    passed: true
    evidence:
      - "24:00–25:45：气温序列的差分矩阵"
      - "25:45–26:52：每日开销的累加矩阵"
      - "26:52–29:56：差分/累加极限对应求导/积分"
  V2_predictive_power:
    passed: true
    novel_question: "怎样为二阶导数构造一个可计算的离散算子？"
    derived_answer: "把一阶差分矩阵连续作用两次，或由相邻点构造二阶差分模板，同时单独规定端点边界，避免把伪末项当有效数据。"
  V3_exclusivity:
    passed: true
    why_not_common: "它给出从连续算子直觉到数值矩阵的双向桥梁，并显式暴露边界项，而非只说‘导数是变化率’。"
  decision: 进入阶段 2

- id: v07
  title: 用特征函数代数化线性算子
  type: framework
  merged_from: [f08, f10, p11, p12, p13, p14, c09, c10, c11, c12, c13, ce09, ce11]
  V1_cross_domain:
    passed: true
    evidence:
      - "28:44–33:30：从矩阵特征向量迁移到微分算子的特征函数"
      - "34:18–37:02：指数分量求导与一阶微分方程"
      - "37:02–42:35：二阶方程的实根、复根和重根"
  V2_predictive_power:
    passed: true
    novel_question: "为什么线性时不变系统对单一复指数输入只改变幅度和相位？"
    derived_answer: "复指数是微分及其多项式算子的特征函数；系统作用被压缩为对该频率乘一个复特征值，因此频率不被混合。"
  V3_exclusivity:
    passed: true
    why_not_common: "它把‘试指数解’提升为算子谱观点，能同时解释微分方程求解和频率响应。"
  decision: 进入阶段 2

- id: v08
  title: 复指数的双表示与正负频率配对
  type: framework
  merged_from: [f09, p13, p18, c12, ce10, g11, g12]
  V1_cross_domain:
    passed: true
    evidence:
      - "30:00–32:38：欧拉公式连接复指数与正弦余弦"
      - "38:05–40:12：共轭复根合成为实衰减振荡"
      - "47:30–50:42：傅立叶级数用正负频率共同重建实信号"
  V2_predictive_power:
    passed: true
    novel_question: "若一个实信号的负频率幅度被独立修改，会发生什么？"
    derived_answer: "共轭对称被破坏，逆变换一般产生复信号；要保持实值，正负频率的系数必须成共轭配对。"
  V3_exclusivity:
    passed: true
    why_not_common: "它把正负频率解释为复平面的旋转方向，并用共轭配对解释实信号，而非把负频率当作无意义记号。"
  decision: 进入阶段 2

- id: v09
  title: 正交—完备—归一三项基审计
  type: framework
  merged_from: [f12, f13, p01, p15, p16, p17, ce01, ce13, ce14, g01, g13]
  V1_cross_domain:
    passed: true
    evidence:
      - "01:50–07:38：有限维坐标基要求正交归一"
      - "42:35–45:12：复指数函数族的正交与完备"
      - "46:16–47:30：周期内积需要 1/T 归一化"
  V2_predictive_power:
    passed: true
    novel_question: "一组函数两两正交，为什么仍可能不能重建目标函数？"
    derived_answer: "正交只保证坐标互不干扰；还需完备性覆盖目标空间，且需归一化或除以范数平方，才能正确取得尺度。"
  V3_exclusivity:
    passed: true
    why_not_common: "将常被混用的三个条件拆成独立审计项，能直接诊断错误展开和错误归一化。"
  decision: 进入阶段 2

- id: v10
  title: 傅立叶级数的分析—综合双流程
  type: framework
  merged_from: [f14, p17, p18, p19, c14, g14]
  V1_cross_domain:
    passed: true
    evidence:
      - "16:47–19:39：一般积分变换先提出分析/综合结构"
      - "45:32–48:48：周期函数的系数提取与重建"
      - "48:48–50:42：复指数形式与三角形式互换"
  V2_predictive_power:
    passed: true
    novel_question: "只保留有限个谐波时，怎样系统判断近似误差来自哪里？"
    derived_answer: "先由分析公式得到全部坐标，再查看被截断坐标的能量与相位；综合误差来自被删频率分量，而非重建公式本身。"
  V3_exclusivity:
    passed: true
    why_not_common: "把系数计算和函数重建明确分工，并统一复指数与三角形式，形成可执行的公式检查流程。"
  decision: 进入阶段 2

- id: v11
  title: 周期拉伸构造傅立叶变换
  type: framework
  merged_from: [f15, p20, p21, c15, g16, g17]
  V1_cross_domain:
    passed: true
    evidence:
      - "50:42–53:36：矩形脉冲周期从 1 秒拉长到 2.5、5 秒的频谱实验"
      - "54:00–55:48：T→∞、f₀→df、nf₀→f、求和→积分的公式推导"
  V2_predictive_power:
    passed: true
    novel_question: "为什么观察时间更长时可分辨的频率网格更细？"
    derived_answer: "有限观察窗相当于周期 T 的频率网格，间隔为 1/T；延长 T 会缩小频率间隔，这也是离散谱趋向连续谱的核心尺度关系。"
  V3_exclusivity:
    passed: true
    why_not_common: "它用可操作的周期拉伸实验与三项连续化替换连接级数和变换，而不是把两个公式并列背诵。"
  decision: 进入阶段 2

- id: v12
  title: 傅立叶约定的符号与归一化审计
  type: framework
  merged_from: [f16, p22, p23, p24, ce15, g18]
  V1_cross_domain:
    passed: true
    evidence:
      - "30:00–32:38：ω 与复指数/三角函数的关系"
      - "45:32–50:42：使用普通频率 f 的傅立叶级数"
      - "55:48–57:51：f↔ω、df↔dω 与 2π 归一化换元"
  V2_predictive_power:
    passed: true
    novel_question: "两本教材的傅立叶变换一个带 2π、一个不带，怎样判断它们是否等价？"
    derived_answer: "列出指数核使用 f 还是 ω、同步变换微元，并检查正逆变换常数的乘积；位置可不同，但整套变换对必须自洽。"
  V3_exclusivity:
    passed: true
    why_not_common: "它把符号差异变成一套变量—微元—核函数—归一化的机械审计程序，可直接防止教材间换公式出错。"
  decision: 进入阶段 2

---

## 汇总

- 通过：12 个方法论单元
- 淘汰或降级合并：5 个方法论簇
- 保留为案例素材：15 条
- 保留为边界素材：15 条反例（已绑定至通过单元）
- 保留为共享词典：18 个术语

阶段 2 只会把以上 12 个通过单元制作成独立 skill；必须先取得用户轻确认。
