# 压力测试结果：fourier-convention-audit

- 测试方式：独立 sub-agent 盲测；评测者只见 `SKILL.md` 与 prompt，未见期望类型和答案。
- 通过：6/6（100%）
- 所有诱饵通过：是
- 结论：接受

| 用例 | 类型 | 结果 | 盲测理由 |
|---|---|---|---|
| `should-trigger-01` | should_trigger | 通过 | 用户追问傅立叶公式中的 2π，直接涉及频率变量、指数核和正逆变换归一化约定。 |
| `should-trigger-02` | should_trigger | 通过 | 比较两本教材的傅立叶定义不能只看单个常数，需要审计整套 f/ω、2π、符号和正逆常数，正中该 skill。 |
| `should-trigger-03` | should_trigger | 通过 | 用户点名要求用离线实验讲清傅立叶约定和归一化审计，与该 skill 的执行目标完全一致。 |
| `should-not-trigger-01` | should_not_trigger | 通过 | 天气查询不涉及傅立叶定义、频率变量或归一化约定。 |
| `should-not-trigger-02` | should_not_trigger | 通过 | 用户明确只解释另一个 skill 的适用场景，当前傅立叶约定审计不应触发。 |
| `edge-01` | edge_case | 通过 | 请求仅为中文定义并明确不要推导或实验，属于该 skill 明确排除的纯定义查询。 |

## 判定说明

- `should_trigger` 必须激活本 skill，不能只激活兄弟 skill。
- `should_not_trigger` 诱饵容错为 0。
- `edge_case` 依当前测试定义应只给简短定义，不完整激活 skill。
