# Module 02 — Exercise 1
responses = [
    {"model": "model-a", "tokens": 500, "latency_ms": 420},
    {"model": "model-b", "tokens": 250, "latency_ms": 310},
    {"model": "model-c", "tokens": 700, "latency_ms": 610},
    {"model": "model-d", "tokens": 400, "latency_ms": 480},
]

fast_responses = sorted(
    [r for r in responses if r["latency_ms"] < 500],
    key=lambda r: r["tokens"],
)

for response in fast_responses:
    print(response)
