# Module 05 — Exercise 1
from pathlib import Path
import pandas as pd

MODULE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = MODULE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

rows = [
    ("gpt-4o", "qa", 0.88, 380),
    ("gpt-4o", "code", 0.92, 420),
    ("gpt-4o", "math", 0.90, 400),
    ("gpt-4o", "summary", 0.84, 360),
    ("gpt-4o", "reasoning", 0.91, 450),
    ("claude", "qa", 0.91, 410),
    ("claude", "code", 0.94, 430),
    ("claude", "math", 0.89, 420),
    ("claude", "summary", 0.92, 390),
    ("claude", "reasoning", 0.93, 460),
    ("gemini", "qa", 0.86, 330),
    ("gemini", "code", 0.87, 350),
    ("gemini", "math", 0.92, 370),
    ("gemini", "summary", 0.88, 320),
    ("gemini", "reasoning", 0.89, 380),
    ("llama", "qa", 0.81, 250),
    ("llama", "code", 0.85, 280),
    ("llama", "math", 0.80, 270),
    ("llama", "summary", 0.83, 240),
    ("llama", "reasoning", 0.82, 300),
]

df = pd.DataFrame(rows, columns=["model", "task", "score", "latency_ms"])
path = DATA_DIR / "llm_benchmark_scores.csv"
df.to_csv(path, index=False)

loaded = pd.read_csv(path)
mean_score = loaded.groupby("model")["score"].mean().sort_values(ascending=False)
best_rows = loaded.loc[loaded.groupby("model")["score"].idxmax(), ["model", "task", "score"]]
correlation = loaded["score"].corr(loaded["latency_ms"])

print("Mean score per model:")
print(mean_score.round(3))
print("\nBest-performing task per model:")
print(best_rows.to_string(index=False))
print(f"\nScore-latency correlation: {correlation:.4f}")
