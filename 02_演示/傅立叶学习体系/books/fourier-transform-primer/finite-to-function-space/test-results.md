# 压力测试结果：finite-to-function-space

- 测试方式：独立 sub-agent 盲测；评测者只见 `SKILL.md` 与 prompt，未见期望类型和答案。
- 通过：6/6（100%）
- 所有诱饵通过：是
- 结论：接受

| 用例 | 类型 | 结果 | 盲测理由 |
|---|---|---|---|
| `should-trigger-01` | should_trigger | 通过 | 问题直接询问函数为何能被视为向量，属于从有限维线性代数迁移到函数空间的核心触发。 |
| `should-trigger-02` | should_trigger | 通过 | 用户明确要求把线性代数结构类比到函数空间，与 skill 的执行目标完全一致。 |
| `should-trigger-03` | should_trigger | 通过 | 用户点名该单元并要求离线实验，符合将抽象迁移变为可计算教学步骤的场景。 |
| `should-not-trigger-01` | should_not_trigger | 通过 | 天气查询不涉及函数空间或线性代数结构迁移。 |
| `should-not-trigger-02` | should_not_trigger | 通过 | 用户明确指定了离散到连续极限的相邻 skill，本 skill 不应抢占调用。 |
| `edge-01` | edge_case | 通过 | 这是只要中文定义的纯信息请求，而该 skill 明确不用于纯粹查定义。 |

## 判定说明

- `should_trigger` 必须激活本 skill，不能只激活兄弟 skill。
- `should_not_trigger` 诱饵容错为 0。
- `edge_case` 依当前测试定义应只给简短定义，不完整激活 skill。
