# 压力测试结果：eigenfunction-operator-algebra

- 测试方式：独立 sub-agent 盲测；评测者只见 `SKILL.md` 与 prompt，未见期望类型和答案。
- 通过：6/6（100%）
- 所有诱饵通过：是
- 结论：接受

| 用例 | 类型 | 结果 | 盲测理由 |
|---|---|---|---|
| `should-trigger-01` | should_trigger | 通过 | 询问为何使用 e^{st} 正是用微分算子特征函数将求导代数化的直接触发信号。 |
| `should-trigger-02` | should_trigger | 通过 | 把微分方程化为代数方程是该 skill 的核心任务。 |
| `should-trigger-03` | should_trigger | 通过 | 用户明确点名该方法并要求离线实验，需要执行特征函数法的可计算验证。 |
| `should-not-trigger-01` | should_not_trigger | 通过 | 天气查询与线性算子、特征函数和微分方程无关。 |
| `should-not-trigger-02` | should_not_trigger | 通过 | 用户明确指定另一个 skill 且只问其适用场景，本 skill 不应触发。 |
| `edge-01` | edge_case | 通过 | 用户只查询中文定义并明确不要推导或实验，符合本 skill 排除的纯定义情形。 |

## 判定说明

- `should_trigger` 必须激活本 skill，不能只激活兄弟 skill。
- `should_not_trigger` 诱饵容错为 0。
- `edge_case` 依当前测试定义应只给简短定义，不完整激活 skill。
