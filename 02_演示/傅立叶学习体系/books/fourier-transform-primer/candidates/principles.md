# 原则 / 规则 / 清单候选（阶段 1）

> 来源：《工科生苦傅立叶久矣！傅立叶变换究极入门》逐字稿。  
> 本文件只做候选提取，不筛选、不验证、不生成 skill。引文保留口语表达，每条均不超过 150 字。

- id: p01
  title: 坐标基应当正交归一
  type: principle
  source_chapter: 坐标变换总结 · 07:38
  source_quote: |
    “空间中的坐标系的基向量，它应该是由两两正交而且长度为 1 的这个 n 维向量组成。”
  summary: |
    在视频采用的坐标变换方法中，先检查候选基是否两两正交。
    再检查每个基向量的长度是否为 1。
    两项都满足时，坐标可直接用内积求出。
    这也使分析矩阵与综合矩阵呈转置/逆的对称关系。
    该断言是后续选择复指数频率基的直接判断标准。
  tags: [principle, basis, orthogonality, normalization]

- id: p02
  title: 用坐标乘基向量并求和重建对象
  type: rule
  source_chapter: 坐标变换总结 · 07:38
  source_quote: |
    “任何一个向量都可以表示成是在某一个基下面基向量的线性组合，那么这个线性组合的系数就是坐标。”
  summary: |
    已知一组基和对象在这组基下的坐标后，执行综合操作。
    将每个坐标系数乘以对应基向量。
    再把全部分量相加，恢复原对象。
    视频把这条有限维规则直接迁移到函数重建。
    它是傅立叶反变换所遵守的可操作断言。
  tags: [rule, synthesis, reconstruction, coordinates]

- id: p03
  title: 换坐标时逐一投影到新基
  type: rule
  source_chapter: 坐标变换总结 · 07:38
  source_quote: |
    “如果我们想把一个向量从一个坐标系变换到另一个坐标系，那我们就需要求这个向量在新的坐标系下每一个基向量上的投影。”
  summary: |
    要得到对象在新坐标系中的表示，不直接猜测新坐标。
    对新坐标系中的每一个基方向分别计算投影。
    每次投影所得标量就是相应方向的坐标。
    把所有投影结果按基的顺序收集成坐标向量。
    视频将傅立叶分析视为此规则在函数空间中的延伸。
  tags: [rule, projection, coordinate-transform, analysis]

- id: p04
  title: 用无穷维向量视角理解函数
  type: maxim
  source_chapter: 数组连续化与函数 · 11:32
  source_quote: |
    “你不要把函数当函数，你把函数当成是一个它的维度非常非常多的一个数组，或者是无穷维的向量去理解。”
  summary: |
    学习傅立叶变换时，先把函数的各个采样值看成向量分量。
    采样越密，分量数量越多，极限直觉对应连续函数。
    随后把点积、投影和坐标变换迁移到函数上。
    这种视角用于解释积分为何能成为函数内积。
    它是视频反复强调的首要学习策略。
  tags: [maxim, learning-strategy, function-space, vector]

- id: p05
  title: 离散内积必须乘采样间隔
  type: rule
  source_chapter: 函数内积的离散逼近 · 12:00
  source_quote: |
    “我们应该要把这个间隙作为一个参考的一个因素把它乘上去。”
  summary: |
    用离散采样近似函数内积时，不能只把样本乘积相加。
    每个样本乘积还要乘以相邻采样点之间的间隔。
    否则采样越密，求和值会无理由地持续变大。
    保留间隔后，离散求和才能形成黎曼和。
    取采样间隔趋零的极限，才得到积分形式。
  tags: [rule, riemann-sum, sampling, inner-product]

- id: p06
  title: 函数乘积积分要读成对应值累加
  type: principle
  source_chapter: 函数内积的解释 · 13:42
  source_quote: |
    “大家不要把它理解成是两个函数的相乘，你就把它理解成是对应的点上、对应的点的值相乘再求和的形式。”
  summary: |
    遇到函数内积积分时，不把注意力停留在两条曲线相乘。
    先在每个相同自变量位置取出两个函数值。
    把对应函数值相乘，并按采样间隔加权。
    再把所有位置的贡献累加。
    这条读法把抽象积分重新连接到熟悉的向量点积。
  tags: [principle, interpretation, integral, dot-product]

- id: p07
  title: 重建函数需要整组基上的坐标
  type: rule
  source_chapter: 从单个投影到基函数组 · 15:53
  source_quote: |
    “原函数应该要在无穷多个基函数下去做投影，那么你才能够用这个无穷多个基函数的这个坐标去复原回原来的函数。”
  summary: |
    单个基函数上的一次投影只能给出一个坐标。
    若要恢复被视为无穷维向量的函数，需要一整组基函数。
    对组中各基函数分别投影，形成坐标集合。
    再用坐标集合与对应基函数做线性组合。
    因而评估一种变换时必须同时关注基函数族而非单个核函数。
  tags: [rule, completeness, basis-family, reconstruction]

- id: p08
  title: 复内积必须对一方取共轭
  type: rule
  source_chapter: 复数函数内积 · 17:35–18:36
  source_quote: |
    “如果我们是在复空间计算向量内积和函数内积的时候，我们是要默认对一个函数去取共轭的。”
  summary: |
    当向量或函数含复数时，计算内积不能直接把两者相乘。
    应先对其中一方取复共轭，再进行点乘或积分。
    这样对象与自身的内积才对应非负的模长平方。
    对实函数，共轭不改变函数本身。
    对复指数基，这条规则直接产生分析公式中的负号。
  tags: [rule, complex-inner-product, conjugate, positivity]

- id: p09
  title: 分清投影与综合是否需要共轭
  type: checklist
  source_chapter: 正变换与反变换 · 19:07–19:39
  source_quote: |
    “第一个含义，它实际上是求向量的投影……第二个……是把这个坐标所有的坐标，去跟这个所有的基向量去做一个线性组合。”
  summary: |
    看见一对变换公式时，先问当前步骤是分析还是综合。
    若是在求对象到基函数上的投影，就按复内积取共轭。
    若是在用坐标乘基函数重建，就直接做线性组合。
    由此检查正、反公式中指数符号是否与角色匹配。
    该清单用于避免孤立记忆傅立叶变换的正负号。
  tags: [checklist, analysis-synthesis, conjugate, sign]

- id: p10
  title: 用离散矩阵为连续算子建立直觉
  type: principle
  source_chapter: 差分、求和与连续极限 · 26:52–28:44
  source_quote: |
    “求导的本质就是在无限密集情况下的差分，然后呢积分的本质其实是无限密集的情况下的求和。”
  summary: |
    理解求导时，先考察离散序列的相邻差分矩阵。
    理解积分时，先考察离散序列的累加求和矩阵。
    再让采样逐渐变密，观察离散操作向连续操作过渡。
    由此把求导和积分理解为作用于函数的线性算子。
    这条原则为寻找算子的特征函数提供准备。
  tags: [principle, discretization, derivative, integral, operator]

- id: p11
  title: 优先在特征函数上化简线性算子
  type: principle
  source_chapter: 特征函数的用途 · 33:30
  source_quote: |
    “如果我们能把一个函数表示成复指数的组合，那么对这个函数去做求导和积分这样子的复杂的运算，它就可以被化简成代数运算。”
  summary: |
    面对线性求导或积分问题时，寻找该算子的特征函数。
    本视频中使用复指数，因为求导后只多出一个标量因子。
    先把目标函数表示为复指数分量的组合。
    在各分量上把算子作用替换为特征值乘法。
    最后组合各分量结果，把复杂算子运算降为代数运算。
  tags: [principle, eigenfunction, operator, algebraization]

- id: p12
  title: 常系数线性微分方程先试指数解
  type: rule
  source_chapter: 用特征函数解微分方程 · 35:35–37:02
  source_quote: |
    “我们是不是可以假设这个方程的解应该是一个 $e^{s_i t}$ 次方的线性组合？”
  summary: |
    求解视频所示常系数线性齐次微分方程时，先设解为 $e^{st}$。
    将试探解及其各阶导数代回原方程。
    提取始终非零的 $e^{st}$，得到关于 $s$ 的代数特征方程。
    求出所有特征根，并构造相应指数解。
    再对线性无关的指数解做线性组合形成通解。
  tags: [rule, ode, characteristic-equation, exponential]

- id: p13
  title: 共轭复根要转换为实衰减振荡
  type: rule
  source_chapter: 微分方程的复特征根 · 38:05–39:08
  source_quote: |
    “一般来说，我们都会把它用欧拉公式把它化简成一个看起来比较舒服的一个状态。”
  summary: |
    当实系数二阶方程出现一对共轭复根时，先保留指数解。
    再用欧拉公式把正、负旋转的复指数配对。
    将解改写为实数形式的正弦与余弦组合。
    若特征根含负实部，实数解表现为衰减振荡。
    该规则也连接了复指数频率表示与真实振动信号。
  tags: [rule, complex-roots, euler-formula, oscillation]

- id: p14
  title: 重根的附加解乘以时间因子
  type: rule
  source_chapter: 微分方程的重根 · 40:12–42:35
  source_quote: |
    “在有重根的情况下，我们假如说知道了一个解是 $x_1=e^{s_1t}$ 次方，那么另外一个解就是 $t$ 乘上 $e^{s_1t}$ 次方。”
  summary: |
    当二阶常系数线性齐次方程的特征方程出现二重根时，不能重复使用同一指数解。
    保留第一个解 $e^{st}$。
    通过相近两根的差商取极限，得到第二个线性无关解 $te^{st}$。
    最终用 $Ae^{st}+Bte^{st}$ 构造通解。
    这是一条可直接套用的重根处理规则。
  tags: [rule, repeated-root, ode, linear-independence]

- id: p15
  title: 频率基必须同时满足正交与完备
  type: checklist
  source_chapter: 选择复指数基 · 42:35–43:28
  source_quote: |
    “周期函数它可以表示成具有相同周期的复指数函数的线性组合……而且呢还有另外一个点，就是说，这些函数都是两两正交归一的。”
  summary: |
    为周期函数选择展开基时，先检查函数族能否表示目标函数。
    这对应视频所说的完备性要求。
    再检查不同基函数在指定周期内的内积是否为零。
    同时检查每个基函数的归一化约定。
    只有覆盖能力与相互可分离性兼具，才能稳定分析并重建。
  tags: [checklist, frequency-basis, completeness, orthogonality]

- id: p16
  title: 复指数正交性要在整周期上检验
  type: rule
  source_chapter: 复指数函数的正交性 · 43:28–45:12
  source_quote: |
    “它只要 $m\neq n$……你去在 $xy$ 方向去积分，你积出来都是 0。”
  summary: |
    比较两个整数倍频复指数时，选取一个完整周期或若干完整周期作为积分区间。
    计算内积时对其中一个复指数取共轭。
    若频率索引不同，剩余旋转在整周期积分中相互抵消。
    若索引相同，正反旋转抵消为常数。
    因此正交判断必须连同积分区间和共轭操作一起执行。
  tags: [rule, orthogonality-test, harmonic, integration-interval]

- id: p17
  title: 傅立叶级数系数按单位周期归一化
  type: rule
  source_chapter: 周期函数的频率投影 · 46:16–47:00
  source_quote: |
    “周期函数它去求内积，你必须要去求单位周期之内的结果。”
  summary: |
    计算周期函数在某个谐波上的坐标时，在一个完整周期内积分。
    投影核使用相应复指数基的共轭。
    积分结果还要除以周期 $T$，即乘以 $1/T$。
    这样换成多个周期积分时，不会让同一坐标随区间倍增。
    该规则固定了视频采用的傅立叶级数系数归一化。
  tags: [rule, fourier-series, coefficient, period-normalization]

- id: p18
  title: 复指数综合必须包含正负频率
  type: rule
  source_chapter: 傅立叶级数的重建 · 47:30–48:48
  source_quote: |
    “这个 $n$ 它是具有正频率和负频率的……从负无穷到正无穷去对 $F_n$……乘上这个基向量去做一个求和。”
  summary: |
    用复指数傅立叶级数重建周期函数时，索引不能只取正整数。
    先保留 $n=0$ 的直流分量。
    再同时加入正频率与负频率对应的坐标和基函数。
    对全部整数索引从负无穷到正无穷求和。
    对实信号，正负频率系数形成共轭配对。
  tags: [rule, synthesis, positive-frequency, negative-frequency]

- id: p19
  title: 始终用“投影—线性组合”核对傅立叶公式
  type: maxim
  source_chapter: 傅立叶级数的统一解释 · 48:48
  source_quote: |
    “一定要记住这边还是函数内积和线性组合的关系。”
  summary: |
    阅读傅立叶级数或变换公式时，先标出哪一式负责分析。
    把分析式解释为函数内积和坐标投影。
    再标出哪一式负责综合。
    把综合式解释为坐标乘基函数后的累加。
    任何符号疑问都先回到这对操作检查，而非孤立背诵。
  tags: [maxim, formula-check, projection, linear-combination]

- id: p20
  title: 周期拉长时按倒数更新频率间隔
  type: rule
  source_chapter: 周期与频率间隔 · 50:42–53:36
  source_quote: |
    “周期越长，你的基频越小……频率间隔它会随着周期的增大而减小。”
  summary: |
    分析周期为 $T$ 的函数时，先计算基频和频率间隔 $\Delta f=1/T$。
    当时间周期被拉长时，按倒数关系重新计算 $\Delta f$。
    傅立叶级数的频率采样点随之变密。
    当 $T$ 趋于无穷时，用频率间隔趋零解释连续频率极限。
    这条规则是从傅立叶级数过渡到傅立叶变换的操作入口。
  tags: [rule, period, frequency-spacing, limit]

- id: p21
  title: 从级数到变换执行三项连续化替换
  type: checklist
  source_chapter: 傅立叶级数到傅立叶变换 · 54:00–54:55
  source_quote: |
    “把 $nf_0$ 用 $f$ 去替换，然后把 $f_0$ 用 $df$ 替换，然后这个时候呢，求和其实就变成了积分。”
  summary: |
    让周期 $T$ 趋于无穷，并使基频 $f_0=1/T$ 趋于无穷小。
    把离散谐波位置 $nf_0$ 替换为连续频率变量 $f$。
    把频率间隔 $f_0$ 替换为微元 $df$。
    把离散频率上的求和替换为连续频率上的积分。
    这三项构成视频给出的傅立叶变换极限推导清单。
  tags: [checklist, fourier-limit, continuous-frequency, sum-to-integral]

- id: p22
  title: 切换到角频率时同步变换微元
  type: rule
  source_chapter: 普通频率与角频率换元 · 55:48
  source_quote: |
    “$\omega=2\pi f$，所以 $d\omega=2\pi df$，那么 $df$ 是不是应该等于 $d\omega$ 除以 $2\pi$？”
  summary: |
    把普通频率 $f$ 改写为角频率 $\omega$ 时，不只替换指数中的变量。
    同时根据 $\omega=2\pi f$ 计算微元关系。
    使用 $df=d\omega/(2\pi)$ 改写积分测度。
    因而在视频的约定下，反变换前出现 $1/(2\pi)$。
    该规则用于检查频率变量换元后的归一化因子。
  tags: [rule, angular-frequency, change-of-variable, normalization]

- id: p23
  title: 傅立叶正负号从变换角色推导
  type: rule
  source_chapter: 傅立叶变换符号说明 · 57:51
  source_quote: |
    “这边是求投影，所以求投影要乘共轭；这边是求线性组合，求线性组合是不用乘共轭的。”
  summary: |
    判断傅立叶指数正负号时，先识别公式承担的角色。
    正变换是对 $e^{j\omega t}$ 做复内积投影，所以使用其共轭 $e^{-j\omega t}$。
    反变换是用坐标与原基函数做线性组合，所以保留 $e^{j\omega t}$。
    由分析/综合角色推出符号，而不是背诵“前负后正”。
    若教材采用另一套配对约定，也应保持两式共轭对应。
  tags: [rule, fourier-transform, exponent-sign, conjugation]

- id: p24
  title: 归一化常数位置可变但变换对必须一致
  type: principle
  source_chapter: 傅立叶变换归一化约定 · 57:51
  source_quote: |
    “这个 $2\pi$ 其实你无论是放在正变换也好，放在反变换也好，其实都没有关系。”
  summary: |
    比较不同教材的傅立叶公式时，不因 $2\pi$ 位置不同立即判错。
    先确认它使用普通频率还是角频率。
    再检查正变换和反变换的归一化常数是否彼此配套。
    常数可全部放在一侧，也可对称拆分到两侧。
    实际计算中必须从头到尾坚持同一套约定。
  tags: [principle, convention, normalization, transform-pair]

- id: p25
  title: 用积分后剩余的变量识别变换输出
  type: rule
  source_chapter: 像函数与频谱映射 · 58:45
  source_quote: |
    “当它这个积分积完了之后，这个 $t$ 就消失了，最后剩下的就是 $\omega$，就变成频谱。”
  summary: |
    阅读积分变换时，先区分积分变量和参数变量。
    对时间变量 $t$ 完成积分后，$t$ 被消去。
    核函数中未被积分的频率参数 $\omega$ 保留下来。
    因而正变换的输出是关于 $\omega$ 的函数，即频谱。
    这条规则可用于检查变换前后自变量是否书写正确。
  tags: [rule, integral-transform, variable-tracking, spectrum]
