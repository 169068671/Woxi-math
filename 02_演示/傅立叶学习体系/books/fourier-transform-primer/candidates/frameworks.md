# 阶段 1 候选：思维模型 / 推理框架

- id: f01
  title: 投影—坐标—重建闭环
  type: framework
  source_chapter: 坐标变换（02:30；04:06；48:48）
  source_quote: |
    “把 OP 投影到三个新的基向量下面，那么投影的值就是在新的基向量下的坐标。”
  summary: |
    先选定一组能够表示对象的基，再用内积求对象在每个基方向上的投影。
    把投影结果解释为新坐标，而不是孤立的计算结果。
    反向过程用“坐标 × 对应基”逐项累加，重建原对象。
    分析与综合因此成为互逆而结构对称的两步。
    该闭环可迁移到向量、函数、信号及任意正交展开。
  tags: [projection, coordinates, reconstruction, analysis-synthesis]

- id: f02
  title: 离散加密到连续极限
  type: framework
  source_chapter: 函数内积（10:18–13:42）
  source_quote: |
    “我们应该要把这个间隙作为一个参考的一个因素把它乘上去……这样的话，我们才不会出现说越加密，它的数字越大。”
  summary: |
    先把连续对象采样为有限或可数数组，使运算变得可见。
    加密采样时必须保留采样间隔作为权重，避免量值随点数虚增。
    将“对应分量相乘、乘间隔、再求和”识别为黎曼和。
    最后取间隔趋零的极限，把离散求和转换为积分。
    这是从向量点积推出函数内积的通用离散—连续桥梁。
  tags: [discrete-continuous, limit, riemann-sum, reasoning]

- id: f03
  title: 函数的无穷维向量视角
  type: framework
  source_chapter: 函数内积（11:32）
  source_quote: |
    “你不要把函数当函数，你把函数当成是一个它的维度非常非常多的一个数组，或者是无穷维的向量去理解。”
  summary: |
    将函数在每个自变量位置的取值看成一个坐标分量。
    把有限维线性代数中的向量、基、坐标和投影整体迁移到函数空间。
    在此表示下，函数内积就是连续索引上的分量乘积累加。
    函数变换也由此重述为换基或坐标变换。
    该视角是概念迁移框架，实际使用时需补充函数空间条件。
  tags: [representation, function-space, infinite-dimensional, analogy]

- id: f04
  title: 积分变换的换基解释
  type: framework
  source_chapter: 积分变换（16:47–17:35）
  source_quote: |
    “把这个 f(x)……在正交的这个函数组上面去做投影……它会变成这个像函数，就是 F(ω)。”
  summary: |
    面对一个积分变换，先把核函数族视为新坐标系的基函数。
    固定一个参数值，对原函数与对应核函数做内积。
    积分消去原变量后，留下的参数成为新坐标的索引。
    全部参数上的投影组成像函数或变换域表示。
    再把坐标乘回基函数并累加，就得到逆变换的结构。
  tags: [integral-transform, change-of-basis, kernel, transform-domain]

- id: f05
  title: 用运算角色判断共轭
  type: framework
  source_chapter: 复数积分变换（18:36–19:39）
  source_quote: |
    “第一个含义，它实际上是求向量的投影……函数内积是要乘上共轭的……第二个……本质是一个线性组合，所以……不用加共轭。”
  summary: |
    不凭公式位置死记正负号或星号，而先判断当前操作的角色。
    若在求复空间中的投影或内积，对基函数取共轭。
    若在用坐标与基函数做线性组合，则保留原基函数。
    这样可从“分析还是综合”预测公式中的符号结构。
    该框架可迁移到傅立叶变换及其他复数正交变换。
  tags: [complex-inner-product, conjugate, role-based-reasoning, signs]

- id: f06
  title: 跨系统的方程同构识别
  type: framework
  source_chapter: 机电系统（20:53–23:36）
  source_quote: |
    “右边的这个微分方程跟左边的这个微分方程，它在形式上是完全完全一样的……这个东西叫做机电系统的相似性。”
  summary: |
    先分别依据领域定律建立机械系统和电路系统的微分方程。
    暂时忽略变量的物理名称，只比较导数阶次与系数结构。
    若方程形式一致，就建立质量、电阻、弹簧等参数的对应关系。
    已知系统的求解方法和行为判断便可迁移到另一系统。
    这是以数学结构而非表面对象进行类比的推理框架。
  tags: [structural-analogy, differential-equation, cross-domain, modeling]

- id: f07
  title: 连续算子的离散矩阵化
  type: framework
  source_chapter: 差分、求和与算子（24:38–28:44）
  source_quote: |
    “求导的本质就是在无限密集情况下的差分，然后呢积分的本质其实是无限密集的情况下的求和。”
  summary: |
    先在有限数列上写出差分或累计求和的逐项规则。
    再把规则编码为稀疏差分矩阵或下三角累加矩阵。
    观察矩阵形状怎样表达局部依赖或历史累积。
    将采样不断加密，把微分、积分理解为对应连续线性算子的极限。
    此框架把抽象算子转成可计算、可画出的线性代数对象。
  tags: [operator, discretization, matrix-representation, finite-difference]

- id: f08
  title: 特征函数代数化算子
  type: framework
  source_chapter: 特征向量与特征函数（29:26–35:10）
  source_quote: |
    “如果我们能把一个函数表示成复指数的组合，那么对这个函数去做求导和积分这样子的复杂的运算，它就可以被化简成代数运算。”
  summary: |
    针对复杂线性算子，先寻找作用后形状不变、只改变标量的对象。
    将一般输入展开为这些特征函数的线性组合。
    在线性作用下，每个分量只需乘上相应特征值。
    完成简单代数运算后，再将分量组合回原表示。
    该框架解释了为何选对表示能把微分问题降维为乘法问题。
  tags: [eigenfunction, diagonalization, operator, algebraization]

- id: f09
  title: 欧拉公式的双表示桥梁
  type: framework
  source_chapter: 复指数与三角函数（30:00–32:38）
  source_quote: |
    “复指数和三角函数就是一家……基于欧拉公式，我们就可以得到 e^{jωt} 就是 cosωt 加上 j sinωt。”
  summary: |
    用欧拉公式在旋转复指数与实数正弦、余弦之间切换表示。
    将有相位的实振荡拆成正频率和负频率两个复指数分量。
    通过系数的共轭关系同时读取幅度与相位。
    当实数表达便于观察时转回三角函数，当算子运算更重要时留在复指数域。
    这是按问题选择表示、而非把两套公式割裂记忆的方法。
  tags: [euler-formula, representation-switch, phasor, positive-negative-frequency]

- id: f10
  title: 特征函数求解常系数微分方程
  type: framework
  source_chapter: 微分方程（35:35–39:08）
  source_quote: |
    “我们是不是可以假设这个方程的解应该是一个 e^{s_i t} 次方的线性组合……把每一个 s_i 都找到，那么原来的方程的所有解是不是就可以找到了？”
  summary: |
    识别方程由常系数线性微分算子组成，提出指数型试探解。
    利用指数求导只乘以 s 的性质，把试探解代入原方程。
    消去不为零的指数因子，得到关于 s 的代数特征方程。
    求出各根，对相应指数解做线性组合。
    若出现复根，再借欧拉公式改写为衰减或增长的实振荡形式。
  tags: [characteristic-equation, differential-equation, eigenfunction, workflow]

- id: f11
  title: 合并根的极限构造法
  type: framework
  source_chapter: 微分方程重根（40:12–42:35）
  source_quote: |
    “当我们去得到重根的情况的时候，其实就是这个 x₁ 和 x₂ 无限靠近的情况……去对这个值去取一个极限。”
  summary: |
    将重根视为两个不同特征根逐渐合并的极限，而非特殊规则。
    先构造两个指数解之差除以根之差的线性组合。
    令两根距离趋零，把差商转成关于参数的导数。
    由此自然产生第二个解 t e^{st}。
    该方法可迁移到“退化时独立对象消失”的极限补全问题。
  tags: [limit, repeated-root, generalized-solution, constructive-reasoning]

- id: f12
  title: 旋转抵消判断正交性
  type: framework
  source_chapter: 复指数正交性（43:28–45:12）
  source_quote: |
    “它只要 m≠n……只要剩下的有螺旋……在 xy 方向去积分，你积出来都是 0。”
  summary: |
    将复指数画成复平面上的旋转或螺旋，而不只看符号积分。
    内积中的共轭使两个频率相减，留下差频旋转。
    若频率不同，完整周期内各方向贡献互相抵消，积分为零。
    若频率相同，旋转消失为常量，积分保留非零能量。
    该几何模型可用于预测谐波是否正交。
  tags: [orthogonality, geometric-reasoning, rotating-phasor, cancellation]

- id: f13
  title: 以单位区间归一化投影
  type: framework
  source_chapter: 傅立叶级数系数（47:00）
  source_quote: |
    “如果没有 1/T……在两个周期内积分，积出来的数值是不是变成两倍了……积分积完还要除以这个周期。”
  summary: |
    当积分结果随观察区间重复次数线性增长时，先识别尺度依赖。
    用区间长度除掉重复累积，把总量转换为单位区间平均量。
    归一化后，坐标不再因选择一个、两个或多个周期而改变。
    该推理也解释正交基未单位化时为何要除以范数平方。
    它是从不变量要求反推归一化因子的通用框架。
  tags: [normalization, invariance, period-average, projection]

- id: f14
  title: 分析—综合双流程
  type: framework
  source_chapter: 傅立叶级数（46:16–48:48）
  source_quote: |
    “上面的这个式子，它其实就是函数内积……下面的这个呢……就是用函数投影下来的坐标跟基函数去做线性组合。”
  summary: |
    把任意变换公式拆成分析与综合两条流程检查。
    分析阶段逐个频率做内积，得到一组坐标或系数。
    综合阶段把每个系数乘对应基函数，再跨全部索引求和。
    由此可以逐项核对变量、符号、共轭和归一化是否放对位置。
    傅立叶级数只是这一双流程在离散谐波基上的实例。
  tags: [analysis, synthesis, decomposition, reconstruction]

- id: f15
  title: 周期拉伸的离散—连续谱极限
  type: framework
  source_chapter: 从傅立叶级数到傅立叶变换（50:42–55:48）
  source_quote: |
    “周期增加，频率的间隔就会变小……把周期延伸到无穷大……频率间隔就变得无穷小了，也就是连续的频率。”
  summary: |
    从周期函数的离散谐波开始，明确频率间隔 Δf=1/T。
    保持局部信号形状，同时逐步增加周期 T，观察谱线变密。
    令 T 趋于无穷，使 Δf 过渡为微分 df，nΔf 过渡为连续 f。
    将带 Δf 权重的离散求和识别为频率积分。
    这样从傅立叶级数构造出傅立叶变换的极限直觉。
  tags: [fourier-series, fourier-transform, continuum-limit, frequency-spacing]

- id: f16
  title: 变量替换追踪归一化常数
  type: framework
  source_chapter: f 与 ω 约定（55:48–57:51）
  source_quote: |
    “ω 等于 2πf，所以 dω 等于 2πdf，那么 df 是不是应该等于 dω 除以 2π？”
  summary: |
    遇到不同版本的变换公式，先确认频率变量是 f 还是角频率 ω。
    对指数相位和积分测度同时执行变量替换，不能只换符号。
    由 dω=2πdf 推出额外的 1/(2π) 归一化因子。
    再检查该常数被分配到正变换、反变换或两者对称位置。
    这能区分约定差异与真正的数学矛盾。
  tags: [change-of-variables, normalization-convention, angular-frequency, dimensional-check]

- id: f17
  title: 变量消去识别变换域
  type: framework
  source_chapter: 傅立叶变换映射（58:45）
  source_quote: |
    “当它这个积分积完了之后，这个 t 就消失了，最后剩下的就是 ω，就变成频谱。”
  summary: |
    阅读积分变换时，先标出被积变量与作为参数保留的变量。
    积分沿被积变量聚合全部信息，因此该变量在结果中被消去。
    核函数中的另一个参数留下，成为输出函数的新自变量。
    由变量的去留判断输入域与输出域，而不是只依赖变换名称。
    该方法可迁移到拉普拉斯变换、积分核方法和边缘化运算。
  tags: [variable-elimination, transform-domain, integral-kernel, parameterization]
