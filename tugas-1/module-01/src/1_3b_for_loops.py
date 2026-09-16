# Module 01 — 1.3 for loops
models = ["gpt-4o", "claude-sonnet-4-5", "gemini-1.5-pro"]

for model in models:
    print(f"Checking: {model}")

for i, model in enumerate(models):
    print(f"{i + 1}. {model}")

token_limits = {
    "gpt-4o": 128000,
    "claude-sonnet-4-5": 200000,
}

for model, limit in token_limits.items():
    print(f"{model}: {limit:,} tokens")
