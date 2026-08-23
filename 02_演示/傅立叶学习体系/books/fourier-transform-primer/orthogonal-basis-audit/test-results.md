# 压力测试结果：orthogonal-basis-audit

- 测试方式：独立 sub-agent 盲测；评测者只见 `SKILL.md` 与 prompt，未见期望类型和答案。
- 通过：6/6（100%）
- 所有诱饵通过：是
- 结论：接受

| 用例 | 类型 | 结果 | 盲测理由 |
|---|---|---|---|
| `should-trigger-01` | should_trigger | 通过 | 用户直接质疑一组函数是否构成基，必须区分并核验正交性、完备性与归一化，正中该 skill 的专属触发范围。 |
| `should-trigger-02` | should_trigger | 通过 | “为什么还要除以 T”是该 skill 明列的语言信号，问题指向非单位范数基的坐标尺度与归一化。 |
| `should-trigger-03` | should_trigger | 通过 | 用户明确要求用实验讲解该方法论本身，且实验需要把正交、完备、归一三个不可互换的条件分别可视化验证。 |
| `should-not-trigger-01` | should_not_trigger | 通过 | 天气查询与函数基、内积、归一化或数学推导审计无关。 |
| `should-not-trigger-02` | should_not_trigger | 通过 | 用户明确指定只解释另一个 skill 的适用场景；当前 skill 即使与其组合使用，也不应抢占调用。 |
| `edge-01` | edge_case | 通过 | 用户只要中文定义并明确排除推导和实验，属于该 skill 边界中排除的纯粹查定义场景。 |

## 判定说明

- `should_trigger` 必须激活本 skill，不能只激活兄弟 skill。
- `should_not_trigger` 诱饵容错为 0。
- `edge_case` 依当前测试定义应只给简短定义，不完整激活 skill。
