# Module 01 — 1.4 Lambda Functions
responses = [
    {"model": "gpt-4o", "tokens": 540},
    {"model": "claude-sonnet-4-5", "tokens": 310},
    {"model": "gemini-1.5-pro", "tokens": 820},
]

sorted_responses = sorted(responses, key=lambda r: r["tokens"])
for r in sorted_responses:
    print(f"{r['model']}: {r['tokens']} tokens")
