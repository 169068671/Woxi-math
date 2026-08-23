# 压力测试结果：discrete-operator-matrix

- 测试方式：独立 sub-agent 盲测；评测者只见 `SKILL.md` 与 prompt，未见期望类型和答案。
- 通过：6/6（100%）
- 所有诱饵通过：是
- 结论：接受

| 用例 | 类型 | 结果 | 盲测理由 |
|---|---|---|---|
| `should-trigger-01` | should_trigger | 通过 | 用户直接询问如何把导数表示成矩阵，精确匹配有限差分算子矩阵化。 |
| `should-trigger-02` | should_trigger | 通过 | 差分矩阵的边界处理是该 skill 明确覆盖的核心问题。 |
| `should-trigger-03` | should_trigger | 通过 | 用户点名连续算子离散矩阵化并要求可运行的离线实验。 |
| `should-not-trigger-01` | should_not_trigger | 通过 | 天气查询不涉及连续算子、离散网格或矩阵表示。 |
| `should-not-trigger-02` | should_not_trigger | 通过 | 用户明确要求只解释另一 skill 的适用场景，本 skill 不应抢占路由。 |
| `edge-01` | edge_case | 通过 | 请求仅限中文定义并排除推导和实验，属于本 skill 描述明确排除的纯定义查询。 |

## 判定说明

- `should_trigger` 必须激活本 skill，不能只激活兄弟 skill。
- `should_not_trigger` 诱饵容错为 0。
- `edge_case` 依当前测试定义应只给简短定义，不完整激活 skill。
