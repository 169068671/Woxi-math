# 压力测试结果：cross-system-equation-isomorphism

- 测试方式：独立 sub-agent 盲测；评测者只见 `SKILL.md` 与 prompt，未见期望类型和答案。
- 通过：6/6（100%）
- 所有诱饵通过：是
- 结论：接受

| 用例 | 类型 | 结果 | 盲测理由 |
|---|---|---|---|
| `should-trigger-01` | should_trigger | 通过 | 用户直接询问两个系统能否共享方法，正是比较控制方程结构并判断能否迁移解法的触发场景。 |
| `should-trigger-02` | should_trigger | 通过 | 机械—电路类比是该 skill 的直接语言信号，任务核心是识别方程角色同构。 |
| `should-trigger-03` | should_trigger | 通过 | 用户点名该方法并要求离线实验，既匹配主题也需要执行可验证步骤。 |
| `should-not-trigger-01` | should_not_trigger | 通过 | 天气查询与方程同构、数学推导或系统类比无关。 |
| `should-not-trigger-02` | should_not_trigger | 通过 | 用户明确限定只解释另一个 skill 的适用场景，应尊重点名路由，不调用本 skill。 |
| `edge-01` | edge_case | 通过 | 用户只要中文定义且明确不要推导或实验；本 skill 的边界明确排除纯粹查定义。 |

## 判定说明

- `should_trigger` 必须激活本 skill，不能只激活兄弟 skill。
- `should_not_trigger` 诱饵容错为 0。
- `edge_case` 依当前测试定义应只给简短定义，不完整激活 skill。
