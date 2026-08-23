#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parents[1]
CHUNK_DIR = PROJECT_DIR / "transcript" / "chunks" / "audio"
OUTPUT_DIR = PROJECT_DIR / "transcript" / "gemini-3.7-flash"
COST_DIR = PROJECT_DIR / "cost"
BRIDGE_PATH = Path.home() / "Library/Application Support/Claude/mcp-servers/multi_model_bridge_mcp.py"
MODEL = "google/gemini-3.7-flash"
MAX_TOKENS = 4000
SAFETY_LIMIT_USD = 0.13


def load_bridge():
    spec = importlib.util.spec_from_file_location("multi_model_bridge_mcp", BRIDGE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load bridge: {BRIDGE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def duration_seconds(path: Path) -> float:
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return float(result.stdout.strip())


def timestamp(seconds: float) -> str:
    total = max(0, int(round(seconds)))
    return f"{total // 60:02d}:{total % 60:02d}"


def main() -> None:
    chunks = sorted(CHUNK_DIR.glob("*.m4a"))
    if not chunks:
        raise RuntimeError(f"No audio chunks found in {CHUNK_DIR}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    COST_DIR.mkdir(parents=True, exist_ok=True)
    bridge = load_bridge()

    before = bridge.current_openrouter_usage()
    write_json(COST_DIR / "before-paid.json", before)
    before_usage = float(before.get("usage") or 0)

    requests_path = OUTPUT_DIR / "requests.json"
    if requests_path.is_file():
        request_state = json.loads(requests_path.read_text(encoding="utf-8"))
        requests = list(request_state.get("requests") or [])
    else:
        requests = []

    completed_outputs: list[Path] = []
    response_cost_sum = sum(float((item.get("usage") or {}).get("cost") or 0) for item in requests)

    for index, chunk in enumerate(chunks):
        output_path = OUTPUT_DIR / f"{chunk.stem}.txt"
        if output_path.is_file() and output_path.stat().st_size > 20:
            completed_outputs.append(output_path)
            continue

        current = bridge.current_openrouter_usage()
        snapshot_delta = float(current.get("usage") or 0) - before_usage
        observed_cost = max(snapshot_delta, response_cost_sum)
        if observed_cost >= SAFETY_LIMIT_USD:
            raise RuntimeError(
                f"Safety cost limit reached before chunk {index + 1}: ${observed_cost:.6f}"
            )

        start = index * 360.0
        end = start + duration_seconds(chunk)
        prompt = f"""
这是一段中文傅立叶变换教学视频的音频，第 {index + 1}/{len(chunks)} 段，对应原视频全局时间 {timestamp(start)}–{timestamp(end)}。

请生成可追溯的简体中文逐字稿：
1. 只转写音频中实际说出的内容，不总结、不纠错、不补充知识。
2. 保留傅立叶、正弦、余弦、频率、相位、复数、积分等数学术语，特别保留讲者对公式、符号和数值的读法。
3. 听不清的词写【听不清】，不要猜。
4. 在话题转折处加全局时间戳 [MM:SS]，每隔约 30–60 秒至少一个；时间戳必须落在 {timestamp(start)}–{timestamp(end)} 范围内。
5. 若音频中有引言、笑声或屏幕操作提示，用简短方括号标注。
6. 不得在音频结束后循环重复文字。

只输出该分段逐字稿。
""".strip()

        status = {
            "state": "running",
            "model": MODEL,
            "chunk": index + 1,
            "chunks_total": len(chunks),
            "file": str(chunk),
            "started_at": datetime.now(timezone.utc).isoformat(),
        }
        write_json(OUTPUT_DIR / "status.json", status)

        transcript, usage, request_id = bridge.audio_chat_openrouter(
            chunk,
            model=MODEL,
            prompt=prompt,
            max_tokens=MAX_TOKENS,
        )
        transcript = bridge.simplify_text(transcript).strip()
        output_path.write_text(transcript + "\n", encoding="utf-8")
        completed_outputs.append(output_path)

        repetitive = bool(bridge.looks_repetitive(transcript))
        request_record = {
            "chunk": index + 1,
            "file": str(chunk),
            "output": str(output_path),
            "request_id": request_id,
            "model": MODEL,
            "usage": usage,
            "repetitive_warning": repetitive,
        }
        requests.append(request_record)
        response_cost_sum += float(usage.get("cost") or 0)
        write_json(requests_path, {"requests": requests})

        if repetitive:
            raise RuntimeError(f"Repetitive output detected in chunk {index + 1}; no automatic retry")

    merged_path = OUTPUT_DIR / "e2Nd4iStm7s-简体中文逐字稿.md"
    merged_parts = []
    for index, output_path in enumerate(completed_outputs, start=1):
        merged_parts.append(f"## 分段 {index:02d}\n\n{output_path.read_text(encoding='utf-8').strip()}")
    merged_path.write_text("\n\n".join(merged_parts) + "\n", encoding="utf-8")

    after = bridge.current_openrouter_usage()
    write_json(COST_DIR / "after-paid.json", after)
    snapshot_delta = float(after.get("usage") or 0) - before_usage
    cost_report = {
        "model": MODEL,
        "chunks": len(chunks),
        "requests": len(requests),
        "automatic_retries": 0,
        "response_cost_sum_usd": response_cost_sum,
        "snapshot_delta_usd": snapshot_delta,
        "started_at": before.get("captured_at"),
        "finished_at": after.get("captured_at"),
        "safety_limit_usd": SAFETY_LIMIT_USD,
        "attribution_warning": "Snapshot delta is exact only if no concurrent task used the same OpenRouter key.",
    }
    write_json(COST_DIR / "transcription-cost.json", cost_report)
    (COST_DIR / "transcription-cost.md").write_text(
        "# OpenRouter 转写费用\n\n"
        f"- 模型：`{MODEL}`\n"
        f"- 分段 / 请求：{len(chunks)} / {len(requests)}\n"
        "- 自动重试：0\n"
        f"- 响应内费用合计：${response_cost_sum:.9f}\n"
        f"- 账户快照差额：${snapshot_delta:.9f}\n"
        f"- 安全线：${SAFETY_LIMIT_USD:.2f}\n\n"
        "> 若同一 API Key 在转写期间被其他任务使用，快照差额会包含其他任务。\n",
        encoding="utf-8",
    )
    write_json(
        OUTPUT_DIR / "status.json",
        {
            "state": "completed",
            "model": MODEL,
            "chunks_total": len(chunks),
            "requests": len(requests),
            "merged_transcript": str(merged_path),
            "cost": cost_report,
            "finished_at": datetime.now(timezone.utc).isoformat(),
        },
    )
    print(json.dumps({"state": "completed", "transcript": str(merged_path), "cost": cost_report}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
