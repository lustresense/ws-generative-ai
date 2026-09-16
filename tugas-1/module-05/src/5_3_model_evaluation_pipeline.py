# Module 05 — 5.3 Mini Project: Model Evaluation Pipeline
import numpy as np
import pandas as pd
from dataclasses import dataclass, field
from pathlib import Path

MODULE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = MODULE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)


@dataclass
class EvalResult:
    prompt: str
    model: str
    response: str
    latency_ms: float
    score: float = field(default=0.0)


def mock_llm_call(prompt: str, model: str) -> tuple[str, float]:
    rng = np.random.default_rng(abs(hash(prompt + model)) % 2**31)
    latency = rng.uniform(300, 700)
    response = f"[{model}] Answer to: {prompt[:30]}"
    return response, latency


def score_response(response: str, expected_keywords: list[str]) -> float:
    found = sum(1 for kw in expected_keywords if kw.lower() in response.lower())
    return found / len(expected_keywords) if expected_keywords else 0.0


prompts = [
    ("What is a transformer?", ["attention", "model"]),
    ("Define RAG", ["retrieval", "generation"]),
    ("What is fine-tuning?", ["training", "weights"]),
]
models = ["claude-sonnet-4-5", "gpt-4o"]
results: list[EvalResult] = []

for prompt, keywords in prompts:
    for model in models:
        response, latency = mock_llm_call(prompt, model)
        score = score_response(response, keywords)
        results.append(EvalResult(prompt, model, response, latency, score))

df = pd.DataFrame([vars(r) for r in results])
summary = df.groupby("model").agg(
    avg_score=("score", "mean"),
    avg_latency=("latency_ms", "mean"),
).round(3)
print(summary)

output_path = DATA_DIR / "eval_results.csv"
df.to_csv(output_path, index=False)
print(f"Saved to {output_path.name}")
