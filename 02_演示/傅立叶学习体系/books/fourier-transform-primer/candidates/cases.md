# 案例候选池（阶段 1）

> 来源：《工科生苦傅立叶久矣！傅立叶变换究极入门》视频逐字稿。以下只做案例提取，不筛选、不判定是否最终 skill 化。

```yaml
- id: c01
  title: 三维向量在新正交基下的坐标变换
  type: case
  source_chapter: "分段 01–02（02:30–07:38）"
  source_quote: |
    "把 OP 这个向量投影到新的基向量下……(3,4,5) 跟 (2/3,2/3,1/3) 点乘，最后得到 19/3。"
  summary: |
    讲者以 OP=(3,4,5) 和一组新的三维正交归一基为算例，
    逐项计算向量在各基方向上的内积，得到新坐标。
    随后再用“新坐标 × 新基向量”的线性组合恢复 (3,4,5)。
    该算例把分析与综合展示为互逆的两步，
    为后续把傅立叶变换解释成函数空间坐标变换建立有限维原型。
  bound_to:
    - "投影—坐标—重建统一模型"
    - "正交矩阵坐标变换"
  outcome: |
    投影得到的新坐标包含 19/3 等数值；用这些坐标与新基做线性组合，成功恢复原向量 (3,4,5)。
  tags: [case, linear-algebra, projection, coordinates, reconstruction]

- id: c02
  title: 数列采样加密成为连续函数
  type: case
  source_chapter: "分段 02（10:18–11:32）"
  source_quote: |
    "数组叫做 fn，解析式是 n 平方加 n……让 n 的细分变得越来越小……fn 就变成了连续的函数 fx。"
  summary: |
    讲者从离散数列 f_n=n²+n 出发，先列出 f₁=2、f₂=6、f₃=12，
    再允许 n 按 0.1 等更小间隔取值。
    随着采样间隔不断缩小，离散数组在直觉上趋向连续函数 f(x)=x²+x。
    该例用于建立“函数可视为无穷维数组”的认知桥梁，
    并为点积过渡到函数内积提供准备。
  bound_to:
    - "函数作为无穷维向量"
    - "离散采样到连续函数的极限直觉"
  outcome: |
    离散序列的取点逐渐加密，最终被解释为连续函数 f(x)=x²+x 的全部取值。
  tags: [case, sequence, sampling, continuum, function-space]

- id: c03
  title: 两个采样函数的点积过渡为积分
  type: case
  source_chapter: "分段 02–03（11:32–14:48）"
  source_quote: |
    "当间隙是 0.5 的时候……把整个相乘的结果乘上 0.5……从一个求和的方式变成了一个积分的方式。"
  summary: |
    讲者先在 x=1,2,…,9 的离散点上，把 f 与 g 的对应值相乘后求和。
    当采样加密到 0.5 间隔时，他指出若不乘采样间隔，点积会随取点增多而虚增。
    补入 Δx 后，表达式成为黎曼和；继续加密就得到 ∫f(x)g(x)dx。
    该案例直接演示了有限维点积如何延伸为函数内积，
    也是积分变换“投影求坐标”解释的计算依据。
  bound_to:
    - "从离散点积构造函数内积"
    - "函数投影的积分表示"
  outcome: |
    加入采样间隔后，离散求和在加密极限中稳定过渡为函数内积的积分形式。
  tags: [case, inner-product, riemann-sum, integral, projection]

- id: c04
  title: 用 1+i 的自内积检验复共轭
  type: case
  source_chapter: "分段 03–04（17:35–18:36）"
  source_quote: |
    "假设有一个 a=1+i……不乘共轭……等于 2i，不等于 2……必须是一个乘共轭的情况。"
  summary: |
    讲者用复数 a=1+i 检验内积应当给出模长平方这一要求。
    若直接计算 a·a，会得到 2i，无法作为非负的长度平方。
    改为 a 与其共轭相乘，则得到 2。
    这个最小算例解释了复函数投影中为何必须出现共轭，
    并为傅立叶正变换指数中的负号埋下来源。
  bound_to:
    - "复内积中的共轭规则"
    - "傅立叶正变换负号的来源"
  outcome: |
    乘共轭后得到 |1+i|²=2，满足内积产生模长平方的要求。
  tags: [case, complex-number, conjugate, inner-product, norm]

- id: c05
  title: 弹簧—质量—阻尼系统建立二阶微分方程
  type: case
  source_chapter: "分段 04（20:19–22:40）"
  source_quote: |
    "F(t)减去 kx，减去 R_m 乘上 x 的一阶导，等于 m 乘上 x 的二阶导。"
  summary: |
    讲者取受外力 F(t) 驱动的质量块，并加入线性弹簧和速度阻尼。
    依据合力等于 ma，把位移、速度、加速度统一写成 x 的各阶导数。
    整理后得到 m x'' + R_m x' + kx = F(t)。
    这个机械工程案例说明实际动力系统会自然产生线性常系数微分方程，
    从而引出为何需要寻找能简化微分算子的函数基。
  bound_to:
    - "线性微分系统的算子表示"
    - "特征函数简化工程系统"
  outcome: |
    力学关系被统一为标准二阶常系数微分方程，成为后续特征函数方法的工程动机。
  tags: [case, mechanics, spring-mass-damper, differential-equation, linear-system]

- id: c06
  title: RLC 电路与机械系统的同型方程
  type: case
  source_chapter: "分段 04（23:03–23:36）"
  source_quote: |
    "LC 乘上 u_C 的二阶导加上 RC 乘上 u_C 的一阶导再加上 u_C 会等于最后的这个 u。"
  summary: |
    讲者把串联 RLC 电路各器件关系写成同一个电容电压 u_C 的导数。
    由 i=C du_C/dt、u_R=Ri、u_L=L di/dt，
    得到 LC u_C'' + RC u_C' + u_C = u。
    它与弹簧—质量—阻尼系统的方程结构完全对应，
    用来说明傅立叶/特征函数方法能够跨机械与电学系统复用。
  bound_to:
    - "机电系统相似性"
    - "线性微分系统的统一表示"
  outcome: |
    电路模型被化为与机械系统同型的二阶常系数微分方程，显出跨域统一结构。
  tags: [case, circuit, RLC, electromechanical-analogy, differential-equation]

- id: c07
  title: 杭州每日最低气温的差分矩阵
  type: case
  source_chapter: "分段 05（24:00–25:45）"
  source_quote: |
    "杭州从 9 月 30 号开始，每天的最低气温是这样的一列数……在它左边乘上一个矩阵……得到这个差分。"
  summary: |
    讲者给出杭州连续多日最低气温序列，要求计算每天相对前一天的温差。
    将“后一项减前一项”逐行写入矩阵后，
    矩阵只在相邻两条对角线上出现 -1 与 1。
    该例把熟悉的差分计算改写成线性变换，
    为“求导可视作差分算子的连续极限”提供有限维实例。
  bound_to:
    - "差分作为矩阵算子"
    - "求导作为线性算子的离散原型"
  outcome: |
    气温序列左乘带状差分矩阵后，一次得到全部相邻日温差；末项因缺少后一日数据被判为无效。
  tags: [case, temperature, difference-matrix, derivative, linear-operator]

- id: c08
  title: 国庆每日开销的累加矩阵
  type: case
  source_chapter: "分段 05（25:45–26:52）"
  source_quote: |
    "国庆的期间每天的开销……求他前 n 天的累积开销……求和的矩阵……下三角下面都是 1。"
  summary: |
    讲者用学生国庆期间的逐日开销序列，计算每天为止的累计消费。
    第 n 个累计值需要把前 n 项全部相加，
    因而对应一个下三角区域全为 1 的矩阵。
    该例把前缀和操作表示成线性矩阵，
    并用来支持“积分是无限密集求和”的算子直觉。
  bound_to:
    - "累加作为矩阵算子"
    - "积分作为线性算子的离散原型"
  outcome: |
    每日前缀和可通过一次下三角矩阵乘法得到，呈现了积分算子的离散结构。
  tags: [case, expenses, cumulative-sum, integral, linear-operator]

- id: c09
  title: 在 S 域对三个指数分量直接求导
  type: case
  source_chapter: "分段 06（34:18–35:35）"
  source_quote: |
    "这个函数是 y=e^{-2t}+3e^{-t}+0.1e^{0.5t}……前面的系数 1 就会被乘上 -2。"
  summary: |
    讲者把 y=e^{-2t}+3e^{-t}+0.1e^{0.5t} 表示为三个 S 域位置及其系数。
    求导时不再对时域曲线做差分，
    而是让每个系数分别乘对应特征值 -2、-1、0.5。
    之后按原指数基重建导函数。
    此例具体展示了特征函数如何把微分运算化为逐分量代数乘法。
  bound_to:
    - "复指数是微分算子的特征函数"
    - "算子运算在特征基下对角化"
  outcome: |
    三个 S 域系数由 (1,3,0.1) 直接变为 (-2,-3,0.05)，无需在时域逐点求差。
  tags: [case, s-domain, exponential, differentiation, eigenfunction]

- id: c10
  title: 特征函数法求一阶微分方程
  type: case
  source_chapter: "分段 06–07（35:35–37:02）"
  source_quote: |
    "dx/dt+3x=0……假设有一个解叫做 x=e^{st}……消掉变成特征方程，就是 s+3=0。"
  summary: |
    面对 x'+3x=0，讲者假设解为微分算子的特征函数 e^{st}。
    代入后所有项都含 e^{st}，可将其消去，
    原微分方程随即变成代数方程 s+3=0。
    解得 s=-3，再恢复为指数形式。
    这是“选对基即可把算子方程降为代数问题”的最简示范。
  bound_to:
    - "用特征函数求解线性微分方程"
    - "微分运算代数化"
  outcome: |
    一阶微分方程被降为 s+3=0，得到通解 x=C e^{-3t}。
  tags: [case, first-order-ode, characteristic-equation, eigenfunction]

- id: c11
  title: 二阶方程的两个实特征根
  type: case
  source_chapter: "分段 07（37:02–38:05）"
  source_quote: |
    "x 的二阶导加上 3 倍 x 一阶导，再加上 2 倍 x=0……解是 -1，一个解是 -2。"
  summary: |
    讲者把 x''+3x'+2x=0 的候选解设为 e^{st}。
    代入并消去非零指数项，得到 s²+3s+2=0。
    两个实根 -1、-2 对应两条线性无关的指数解，
    再用线性组合写出通解。
    此例把一阶情形推广到多特征值的二阶系统。
  bound_to:
    - "特征方程与线性组合"
    - "二阶线性微分方程求解"
  outcome: |
    求得通解 x=C₁e^{-t}+C₂e^{-2t}，展示多个特征分量的重建。
  tags: [case, second-order-ode, real-roots, superposition, eigenfunction]

- id: c12
  title: 共轭复根对应衰减振荡
  type: case
  source_chapter: "分段 07（38:05–40:12）"
  source_quote: |
    "s₁=-1+j，s₂=-1-j……得到的解……e^{-t}cos t，e^{-t}sin t……衰减震荡。"
  summary: |
    一个二阶常系数方程产生共轭复根 -1±j。
    讲者先保留 e^{(-1±j)t} 两个复指数解，
    再借欧拉公式改写为 e^{-t}cos t 与 e^{-t}sin t。
    线性组合最终呈现衰减包络内的正弦振荡。
    该例把复指数、正负频率和真实工程振荡形态连接起来。
  bound_to:
    - "欧拉公式连接复指数与三角函数"
    - "复特征根的工程解释"
  outcome: |
    复数形式的两个解转成实值通解 A e^{-t}sin(t+φ)，揭示实部控制衰减、虚部控制振荡。
  tags: [case, complex-roots, damped-oscillation, euler-formula, ode]

- id: c13
  title: 重根极限推导 t e^{st}
  type: case
  source_chapter: "分段 07–08（40:12–42:35）"
  source_quote: |
    "取一个……线性组合，上面 e^{s₁t}-e^{s₂t}，下面 s₁-s₂……重根……结果变成 t×e^{s₂t}。"
  summary: |
    针对特征方程 s²+4s+4=0 的重根，讲者不直接背诵第二解。
    他构造两个指数解的差商，令 s₁ 与 s₂ 不断靠近，
    再用泰勒展开或洛必达法则计算 0/0 极限。
    极限产生 t e^{st}，补足与 e^{st} 线性无关的第二个解。
    此案例展示了重根公式如何由连续极限而非记忆规则得到。
  bound_to:
    - "特征函数解微分方程"
    - "用极限构造重根的广义解"
  outcome: |
    对双重根 s=-2，得到通解 x=Ae^{-2t}+Bt e^{-2t}。
  tags: [case, repeated-root, limit, generalized-solution, ode]

- id: c14
  title: 用旋转螺旋解释复指数正交
  type: case
  source_chapter: "分段 08（43:28–45:12）"
  source_quote: |
    "只要 m≠n……只要剩下的有螺旋……在 xy 方向去积分，积出来都是 0。"
  summary: |
    讲者把 e^{jnωt} 画成一个周期内旋转 n 圈的复平面螺旋。
    两个不同频率做内积时，共轭使旋转圈数相减；
    只要仍有整圈旋转，各方向贡献就在整周期积分中抵消为零。
    相同频率时正反旋转完全抵消成常量，积分得到归一结果。
    这个可视化实例用旋转抵消机制解释复指数族的正交性。
  bound_to:
    - "复指数基的正交性"
    - "正负频率与复共轭"
  outcome: |
    不同整数谐波的周期内积为 0，相同谐波的归一内积为 1。
  tags: [case, phasor, helix, orthogonality, complex-exponential]

- id: c15
  title: 拉长周期的矩形脉冲 MATLAB 仿真
  type: case
  source_chapter: "分段 09（51:24–53:36）"
  source_quote: |
    "周期从 1 秒变成了 2.5 秒……Δf 是 0.4Hz……延长到了 5 秒……Δf 应该是 0.2Hz。"
  summary: |
    讲者编写约 30 行 MATLAB 程序，对周期矩形脉冲计算傅立叶级数系数。
    脉冲宽度固定为 0.5 秒，周期依次取 1 秒、2.5 秒与 5 秒。
    相应频率间隔从 1 Hz 降到 0.4 Hz、0.2 Hz，频谱采样点越来越密。
    再把周期无限拉长，就直观得到离散频率趋向连续频率的图景。
    该仿真是视频从傅立叶级数过渡到傅立叶变换的主要实验证据。
  bound_to:
    - "从傅立叶级数到傅立叶变换的极限直觉"
    - "周期与频率间隔 Δf=1/T"
  outcome: |
    仿真显示周期越长，频率间隔越小；支持 T→∞ 时离散谱趋向连续谱的解释。
  tags: [case, matlab, rectangular-pulse, fourier-series, continuous-spectrum]
```

## 自检

- [x] 每条案例均有 `bound_to`，且绑定到视频中的方法论主题。
- [x] 每条案例均有带时间戳的来源位置和不超过 150 字的原文引文。
- [x] 案例覆盖讲者实际使用的算例、工程模型、可视化例证或仿真实例。
- [x] 未在本阶段筛选候选，未写 skill，未做跨单元链接。
