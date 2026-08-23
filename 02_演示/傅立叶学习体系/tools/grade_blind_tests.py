from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "books" / "fourier-transform-primer"


for prompt_path in sorted(ROOT.glob("*/test-prompts.json")):
    skill_dir = prompt_path.parent
    blind_path = skill_dir / "blind-results.json"
    if not blind_path.exists():
        continue
    expected = json.loads(prompt_path.read_text(encoding="utf-8"))
    blind = json.loads(blind_path.read_text(encoding="utf-8"))
    observed = {r["id"]: r for r in blind["results"]}
    rows = []
    passed = 0
    bait_passed = True
    for case in expected["test_cases"]:
        got = observed.get(case["id"], {})
        want_trigger = case["type"] == "should_trigger"
        if case["type"] == "edge_case":
            want_trigger = False
        ok = bool(got) and got.get("would_trigger") is want_trigger
        if case["type"] == "should_trigger" and ok:
            ok = got.get("selected_skill") == expected["skill"]
        if case["type"] == "should_not_trigger" and got.get("would_trigger"):
            bait_passed = False
        passed += int(ok)
        rows.append(f"| `{case['id']}` | {case['type']} | {'通过' if ok else '失败'} | {got.get('reason','缺失')} |")
    total = len(expected["test_cases"])
    rate = passed / total if total else 0
    accepted = rate >= 0.8 and bait_passed
    report = f'''# 压力测试结果：{expected['skill']}

- 测试方式：独立 sub-agent 盲测；评测者只见 `SKILL.md` 与 prompt，未见期望类型和答案。
- 通过：{passed}/{total}（{rate:.0%}）
- 所有诱饵通过：{'是' if bait_passed else '否'}
- 结论：{'接受' if accepted else '回炉阶段 2'}

| 用例 | 类型 | 结果 | 盲测理由 |
|---|---|---|---|
{chr(10).join(rows)}

## 判定说明

- `should_trigger` 必须激活本 skill，不能只激活兄弟 skill。
- `should_not_trigger` 诱饵容错为 0。
- `edge_case` 依当前测试定义应只给简短定义，不完整激活 skill。
'''
    (skill_dir / "test-results.md").write_text(report, encoding="utf-8")
    print(expected["skill"], f"{passed}/{total}", "ACCEPT" if accepted else "REWORK")
