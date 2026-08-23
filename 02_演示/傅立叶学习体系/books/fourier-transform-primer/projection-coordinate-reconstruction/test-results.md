# 压力测试结果：projection-coordinate-reconstruction

- 测试方式：独立 sub-agent 盲测；评测者只见 `SKILL.md` 与 prompt，未见期望类型和答案。
- 通过：6/6（100%）
- 所有诱饵通过：是
- 结论：接受

| 用例 | 类型 | 结果 | 盲测理由 |
|---|---|---|---|
| `should-trigger-01` | should_trigger | 通过 | 问题直接追问变换与逆变换的结构来源，正是把变换拆成投影求坐标与用坐标重建的触发场景。 |
| `should-trigger-02` | should_trigger | 通过 | 用投影角度推导公式是该 skill 的明确语言信号。 |
| `should-trigger-03` | should_trigger | 通过 | 用户点名该单元并要求可运行的离线实验，属于教学与数值验证场景。 |
| `should-not-trigger-01` | should_not_trigger | 通过 | 天气查询与投影、坐标变换或数学推导无关。 |
| `should-not-trigger-02` | should_not_trigger | 通过 | 用户明确指定了另一个 skill，问的是有限维结构迁移到函数空间的适用场景。 |
| `edge-01` | edge_case | 通过 | 用户限定为纯定义查询，且明确不要推导或实验；该 skill 的边界明确排除纯粹查定义。 |

## 判定说明

- `should_trigger` 必须激活本 skill，不能只激活兄弟 skill。
- `should_not_trigger` 诱饵容错为 0。
- `edge_case` 依当前测试定义应只给简短定义，不完整激活 skill。
