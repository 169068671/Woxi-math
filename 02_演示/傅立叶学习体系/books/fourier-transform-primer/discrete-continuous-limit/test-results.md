# 压力测试结果：discrete-continuous-limit

- 测试方式：独立 sub-agent 盲测；评测者只见 `SKILL.md` 与 prompt，未见期望类型和答案。
- 通过：6/6（100%）
- 所有诱饵通过：是
- 结论：接受

| 用例 | 类型 | 结果 | 盲测理由 |
|---|---|---|---|
| `should-trigger-01` | should_trigger | 通过 | 求和如何在极限中变为积分是该 skill 的直接触发问题。 |
| `should-trigger-02` | should_trigger | 通过 | 采样变密后数值反而变大，通常表明离散和漏了网格宽度，正是该 skill 的尺度审计场景。 |
| `should-trigger-03` | should_trigger | 通过 | 用户点名该单元并要求离线数值实验，符合该 skill 的可计算验证场景。 |
| `should-not-trigger-01` | should_not_trigger | 通过 | 天气查询与离散求和、网格极限或积分无关。 |
| `should-not-trigger-02` | should_not_trigger | 通过 | 用户明确要求另一个关于复内积与共轭的 skill，本 skill 不应触发。 |
| `edge-01` | edge_case | 通过 | 请求仅为中文定义，明确排除推导和实验，属于 skill 说明中排除的纯定义场景。 |

## 判定说明

- `should_trigger` 必须激活本 skill，不能只激活兄弟 skill。
- `should_not_trigger` 诱饵容错为 0。
- `edge_case` 依当前测试定义应只给简短定义，不完整激活 skill。
