# Module 04 — 4.1 JSON
import json
import pathlib

MODULE_DIR = pathlib.Path(__file__).resolve().parents[1]
MODULE_DIR.joinpath("data").mkdir(exist_ok=True)

results = {
    "model": "claude-sonnet-4-5",
    "benchmark": "MMLU",
    "scores": {"science": 0.91, "math": 0.88, "history": 0.85},
    "total_samples": 14042,
    "timestamp": "2025-01-15T09:30:00Z",
}

out = MODULE_DIR / "data" / "results.json"
out.write_text(json.dumps(results, indent=2), encoding="utf-8")

data = json.loads(out.read_text(encoding="utf-8"))
print(f"Model: {data['model']}")
avg = sum(data["scores"].values()) / len(data["scores"])
print(f"Average score: {avg:.2%}")
print(f"Saved: {out.name}")
