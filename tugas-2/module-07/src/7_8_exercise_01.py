import anthropic
import pandas as pd

from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv

ENV_FILE = find_dotenv(filename=".env", usecwd=True)
if not ENV_FILE:
    raise RuntimeError(".env tidak ditemukan. Copy .env.example menjadi .env di folder tugas-2.")
load_dotenv(ENV_FILE)


client = anthropic.Anthropic(api_key=os.environ["NINEROUTER_API_KEY"], base_url=os.environ["NINEROUTER_BASE_URL"].rstrip("/"))
model = os.getenv("ANTHROPIC_MODEL", "ag/claude-sonnet-4-6")

PROMPTS = {
    "basic": "Review this Python code. Identify problems and suggest fixes.",
    "intermediate": "You are a Python code reviewer. Identify correctness, security, and performance issues. Explain each issue and provide a fix.",
    "expert": "You are a senior Python engineer reviewing production AI code. Prioritize correctness, security, reliability, and performance. For each issue return: severity, issue, impact, concrete fix. Be concise and do not pad with compliments.",
}
SNIPPETS = [
    "def divide(a,b): return a/b",
    "def load(path): return open(path).read()",
    "password = 'admin123'",
    "items=[]\nfor i in range(1000): items = items + [i]",
    "def get(url):\n    import requests\n    return requests.get(url).json()",
]

def heuristic_quality(text: str) -> int:
    terms = ["security", "impact", "fix", "error", "exception", "timeout", "resource", "severity"]
    return sum(1 for t in terms if t in text.lower())

rows = []
for level, system in PROMPTS.items():
    for idx, snippet in enumerate(SNIPPETS, start=1):
        r = client.messages.create(model=model, max_tokens=350, system=system, messages=[{"role": "user", "content": snippet}])
        text = r.content[0].text.strip()
        rows.append({"prompt_level": level, "snippet": idx, "quality_signal": heuristic_quality(text), "preview": text.replace("\n", " ")[:110]})

df = pd.DataFrame(rows)
print("=" * 60)
print("7.8 EXERCISE 01 - SYSTEM PROMPT LEVEL COMPARISON")
print("=" * 60)
print(df.to_string(index=False))
print("\nAverage quality signal:")
print(df.groupby("prompt_level")["quality_signal"].mean().round(2).to_string())
