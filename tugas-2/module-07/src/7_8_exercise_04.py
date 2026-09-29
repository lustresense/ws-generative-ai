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

PROMPT = """You receive evaluation scores for 10 LLMs across exactly 3 tasks.
Reason through the comparison carefully. Compute each model's mean score, rank all models from highest to lowest mean, then write exactly two sentences recommending the strongest model while mentioning the trade-off visible in the task scores.
Return a compact ranked list followed by a section named RECOMMENDATION."""

DATASETS = [
    [(f"M{i}", 70+i, 68+i*1.2, 75+i*0.7) for i in range(10)],
    [(f"A{i}", 90-i*0.8, 72+i*1.1, 80+(i%3)) for i in range(10)],
    [(f"X{i}", 65+i*2.0, 95-i*1.3, 74+i*0.4) for i in range(10)],
]

print("=" * 60)
print("7.8 EXERCISE 04 - CoT MODEL RANKING, 3 INPUTS")
print("=" * 60)
for n, rows in enumerate(DATASETS, start=1):
    table = "model,task1,task2,task3\n" + "\n".join(f"{m},{a:.1f},{b:.1f},{c:.1f}" for m,a,b,c in rows)
    resp = client.messages.create(model=model, max_tokens=700, system=PROMPT, messages=[{"role": "user", "content": table}])
    print(f"\n=== INPUT SET {n} ===")
    print(resp.content[0].text)
