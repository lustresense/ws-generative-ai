# Module 01 — Exercise 1
def token_cost(tokens: int, model: str) -> float:
    costs_per_1k = {
        "gpt-4o": 0.005,
        "claude-sonnet-4-5": 0.006,
        "gemini-1.5-pro": 0.0035,
    }
    if model not in costs_per_1k:
        raise ValueError(f"Unknown model: {model}")
    return (tokens / 1000) * costs_per_1k[model]


for model in ["gpt-4o", "claude-sonnet-4-5"]:
    print(f"{model}: ${token_cost(2500, model):.6f}")

try:
    token_cost(1000, "unknown-model")
except ValueError as error:
    print(f"Error: {error}")
