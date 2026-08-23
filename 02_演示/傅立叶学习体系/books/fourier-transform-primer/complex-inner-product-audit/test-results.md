# 压力测试结果：complex-inner-product-audit

- 测试方式：独立 sub-agent 盲测；评测者只见 `SKILL.md` 与 prompt，未见期望类型和答案。
- 通过：6/6（100%）
- 所有诱饵通过：是
- 结论：接受

| 用例 | 类型 | 结果 | 盲测理由 |
|---|---|---|---|
| `should-trigger-01` | should_trigger | 通过 | 该 skill 明确把“傅立叶变换为什么有负号”列为语言信号，问题涉及分析内积中的共轭。 |
| `should-trigger-02` | should_trigger | 通过 | 复内积共轭放在哪一槽正是该 skill 的核心约定审计问题。 |
| `should-trigger-03` | should_trigger | 通过 | 用户点名复内积共轭审计并要求离线实验，属于该 skill 的教学验证场景。 |
| `should-not-trigger-01` | should_not_trigger | 通过 | 天气查询不涉及复内积、共轭或傅立叶符号约定。 |
| `should-not-trigger-02` | should_not_trigger | 通过 | 用户明确点名跨系统方程同构 skill，本 skill 与所询适用场景不匹配。 |
| `edge-01` | edge_case | 通过 | 用户只要求中文定义，明确不要推导或实验，符合该 skill 排除的纯定义情形。 |

## 判定说明

- `should_trigger` 必须激活本 skill，不能只激活兄弟 skill。
- `should_not_trigger` 诱饵容错为 0。
- `edge_case` 依当前测试定义应只给简短定义，不完整激活 skill。
