import anthropic

from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv

ENV_FILE = find_dotenv(filename=".env", usecwd=True)
if not ENV_FILE:
    raise RuntimeError(".env tidak ditemukan. Copy .env.example menjadi .env di folder tugas-2.")
load_dotenv(ENV_FILE)


client = anthropic.Anthropic(api_key=os.environ["NINEROUTER_API_KEY"], base_url=os.environ["NINEROUTER_BASE_URL"].rstrip("/"))
model = os.getenv("ANTHROPIC_MODEL", "ag/claude-sonnet-4-6")

DIRECT_PROMPT = "If a model costs $3.00 per million input tokens and $15.00 per million output tokens, and a request uses 2,400 input tokens and 800 output tokens, what is the total cost in USD?"
COT_PROMPT = """If a model costs $3.00 per million input tokens and $15.00 per million output tokens,
and a request uses 2,400 input tokens and 800 output tokens, what is the total cost in USD?

Think through this step by step before giving the final answer."""
ZERO_SHOT_COT = """Solve this problem. Think step by step, showing each calculation.
Finally, state: ANSWER: $X.XXXXXX

Problem: A pipeline makes 50 API calls per hour. Each call uses an average of 1,200 input tokens
and 400 output tokens. The model costs $3.00/M input and $15.00/M output.
What is the daily cost?"""

print("=" * 60)
print("7.4A - CHAIN-OF-THOUGHT PROMPTING")
print("=" * 60)
for label, prompt in [("Direct", DIRECT_PROMPT), ("CoT", COT_PROMPT), ("Zero-shot CoT", ZERO_SHOT_COT)]:
    resp = client.messages.create(model=model, max_tokens=512, messages=[{"role": "user", "content": prompt}])
    print(f"\n=== {label} ===")
    print(resp.content[0].text[:700])
