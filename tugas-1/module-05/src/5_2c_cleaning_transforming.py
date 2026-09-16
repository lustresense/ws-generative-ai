# Module 05 — 5.2 Cleaning and Transforming
import pandas as pd


raw = pd.DataFrame({
    "prompt": ["Q1", "Q2", "Q3", "Q4", "Q5"],
    "response": ["OK", None, "Good", "Bad", "OK"],
    "score": [0.9, None, 0.85, 0.3, 0.88],
    "latency_ms": [410, 520, None, 390, 480],
})

print(raw.isnull().sum())

raw["score"] = raw["score"].fillna(raw["score"].mean())
raw["latency_ms"] = raw["latency_ms"].fillna(raw["latency_ms"].median())
clean = raw.dropna(subset=["response"]).copy()
clean["pass"] = clean["score"] >= 0.7

print(clean)
print(f"Pass rate: {clean['pass'].mean():.0%}")
