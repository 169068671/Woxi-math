# 压力测试结果：complex-exponential-frequency-pair

- 测试方式：独立 sub-agent 盲测；评测者只见 `SKILL.md` 与 prompt，未见期望类型和答案。
- 通过：6/6（100%）
- 所有诱饵通过：是
- 结论：接受

| 用例 | 类型 | 结果 | 盲测理由 |
|---|---|---|---|
| `should-trigger-01` | should_trigger | 通过 | 负频率的含义是该 skill 的直接触发问题，需用相反旋转方向解释。 |
| `should-trigger-02` | should_trigger | 通过 | 实信号频谱为何共轭对称正是该 skill 的核心解释和审计内容。 |
| `should-trigger-03` | should_trigger | 通过 | 用户点名复指数双表示与正负频率配对，并要求离线可视实验。 |
| `should-not-trigger-01` | should_not_trigger | 通过 | 天气查询与复指数、频谱或正负频率无关。 |
| `should-not-trigger-02` | should_not_trigger | 通过 | 用户明确限定只解释另一个 skill 的适用场景，因此不调用本 skill。 |
| `edge-01` | edge_case | 通过 | 仅要求中文定义且明确排除推导和实验，属于本 skill 不适用的纯定义查询。 |

## 判定说明

- `should_trigger` 必须激活本 skill，不能只激活兄弟 skill。
- `should_not_trigger` 诱饵容错为 0。
- `edge_case` 依当前测试定义应只给简短定义，不完整激活 skill。
