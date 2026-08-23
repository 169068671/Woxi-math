# 压力测试结果：series-to-transform-limit

- 测试方式：独立 sub-agent 盲测；评测者只见 `SKILL.md` 与 prompt，未见期望类型和答案。
- 通过：6/6（100%）
- 所有诱饵通过：是
- 结论：接受

| 用例 | 类型 | 结果 | 盲测理由 |
|---|---|---|---|
| `should-trigger-01` | should_trigger | 通过 | 问题直接要求建立傅立叶级数到傅立叶变换的极限桥，正是该 skill 的专属主题。 |
| `should-trigger-02` | should_trigger | 通过 | “T 越长频率越密”是该 skill 明列的语言信号，要求解释 f0=1/T 与连续频谱极限。 |
| `should-trigger-03` | should_trigger | 通过 | 用户点名要求以离线实验讲解周期拉伸构造傅立叶变换，任务与该 skill 的案例和执行流程一致。 |
| `should-not-trigger-01` | should_not_trigger | 通过 | 天气查询与傅立叶级数极限、频率网格或频谱密度无关。 |
| `should-not-trigger-02` | should_not_trigger | 通过 | 用户明确只要另一个 skill 的适用场景；当前 skill 与其虽可组合，但不应抢占调用。 |
| `edge-01` | edge_case | 通过 | 只查中文定义且不需要推导或实验，属于 description 明确排除的纯定义场景。 |

## 判定说明

- `should_trigger` 必须激活本 skill，不能只激活兄弟 skill。
- `should_not_trigger` 诱饵容错为 0。
- `edge_case` 依当前测试定义应只给简短定义，不完整激活 skill。
