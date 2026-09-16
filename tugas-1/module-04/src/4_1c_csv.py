# Module 04 — 4.1 CSV
import csv
import pathlib
from collections import defaultdict

MODULE_DIR = pathlib.Path(__file__).resolve().parents[1]
MODULE_DIR.joinpath("data").mkdir(exist_ok=True)

rows = [
    {"prompt": "What is RAG?", "model": "claude-sonnet-4-5", "tokens": 312, "latency_ms": 410},
    {"prompt": "Explain embeddings", "model": "claude-sonnet-4-5", "tokens": 498, "latency_ms": 580},
    {"prompt": "What is RAG?", "model": "gpt-4o", "tokens": 287, "latency_ms": 360},
]

csv_file = MODULE_DIR / "data" / "eval.csv"
with csv_file.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["prompt", "model", "tokens", "latency_ms"])
    writer.writeheader()
    writer.writerows(rows)

model_latencies: dict[str, list[float]] = defaultdict(list)
with csv_file.open(encoding="utf-8") as f:
    for row in csv.DictReader(f):
        model_latencies[row["model"]].append(float(row["latency_ms"]))

for model, latencies in model_latencies.items():
    avg = sum(latencies) / len(latencies)
    print(f"{model}: avg latency {avg:.0f}ms")
