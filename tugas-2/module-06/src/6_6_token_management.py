import anthropic

from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv

ENV_FILE = find_dotenv(filename=".env", usecwd=True)
if not ENV_FILE:
    raise RuntimeError(".env tidak ditemukan. Copy .env.example menjadi .env di folder tugas-2.")
load_dotenv(ENV_FILE)


client = anthropic.Anthropic(
    api_key=os.environ["NINEROUTER_API_KEY"],
    base_url=os.environ["NINEROUTER_BASE_URL"].rstrip("/"),
)
model = os.getenv("ANTHROPIC_MODEL", "ag/claude-sonnet-4-6")

print("=" * 60)
print("6.6 - TOKEN MANAGEMENT")
print("=" * 60)
response = client.messages.count_tokens(
    model=model,
    system="You are a concise assistant.",
    messages=[{"role": "user", "content": "Explain the transformer architecture."}],
)
print(f"Estimated input tokens: {response.input_tokens}")

# Example pricing table preserved from the PDF module (not current 2026 billing).
PRICING = {
    "claude-sonnet-4-5": {"input": 3.00, "output": 15.00},
    "claude-opus-4-5": {"input": 15.00, "output": 75.00},
    "gpt-4o": {"input": 2.50, "output": 10.00},
    "gpt-4o-mini": {"input": 0.15, "output": 0.60},
}

def estimate_cost(model_name: str, input_tokens: int, output_tokens: int) -> float:
    if model_name not in PRICING:
        raise ValueError(f"Unknown model: {model_name}")
    p = PRICING[model_name]
    return (input_tokens * p["input"] + output_tokens * p["output"]) / 1_000_000

cost = estimate_cost("claude-sonnet-4-5", input_tokens=500, output_tokens=300)
print(f"Module example estimated cost: ${cost:.6f}")

CONTEXT_LIMITS = {
    "claude-sonnet-4-5": 200_000,
    "claude-opus-4-5": 200_000,
    "gpt-4o": 128_000,
    "gpt-4o-mini": 128_000,
    "gemini-1.5-pro": 1_000_000,
}

def fits_in_context(model_name: str, token_count: int, reserve_for_output: int = 2048) -> bool:
    limit = CONTEXT_LIMITS.get(model_name, 128_000)
    return token_count + reserve_for_output <= limit

print(f"Fits example context: {fits_in_context('claude-sonnet-4-5', 50_000)}")
