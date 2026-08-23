# 压力测试结果：fourier-series-analysis-synthesis

- 测试方式：独立 sub-agent 盲测；评测者只见 `SKILL.md` 与 prompt，未见期望类型和答案。
- 通过：6/6（100%）
- 所有诱饵通过：是
- 结论：接受

| 用例 | 类型 | 结果 | 盲测理由 |
|---|---|---|---|
| `should-trigger-01` | should_trigger | 通过 | 用户要推导傅立叶级数系数，正是从周期、基频和复内积进入分析流程的核心任务。 |
| `should-trigger-02` | should_trigger | 通过 | 用有限谐波重建方波属于该 skill 的综合流程，并需要量化截断误差和说明间断点附近的 Gibbs 现象。 |
| `should-trigger-03` | should_trigger | 通过 | 用户明确要求用离线实验讲清该 skill 的分析—综合双流程，任务与其执行步骤完全一致。 |
| `should-not-trigger-01` | should_not_trigger | 通过 | 天气查询不涉及周期函数、傅立叶级数系数或谐波重建。 |
| `should-not-trigger-02` | should_not_trigger | 通过 | 用户明确只要求另一个 skill 的适用场景；虽然两者相邻，当前 skill 不应在此处触发。 |
| `edge-01` | edge_case | 通过 | 请求仅限中文定义且排除推导和实验，属于 description 明确排除的纯定义查询。 |

## 判定说明

- `should_trigger` 必须激活本 skill，不能只激活兄弟 skill。
- `should_not_trigger` 诱饵容错为 0。
- `edge_case` 依当前测试定义应只给简短定义，不完整激活 skill。
