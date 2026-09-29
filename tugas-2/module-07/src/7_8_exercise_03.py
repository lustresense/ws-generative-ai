import anthropic
import json
import re

from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv

ENV_FILE = find_dotenv(filename=".env", usecwd=True)
if not ENV_FILE:
    raise RuntimeError(".env tidak ditemukan. Copy .env.example menjadi .env di folder tugas-2.")
load_dotenv(ENV_FILE)


client = anthropic.Anthropic(api_key=os.environ["NINEROUTER_API_KEY"], base_url=os.environ["NINEROUTER_BASE_URL"].rstrip("/"))
model = os.getenv("ANTHROPIC_MODEL", "ag/claude-sonnet-4-6")

def strip_fences(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.I)
    text = re.sub(r"\s*```$", "", text)
    return text.strip()

def safe_json_parse(text: str) -> dict:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    cleaned = strip_fences(text)
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass
    repair_prompt = f"Fix this invalid JSON. Return raw valid JSON only, no markdown:\n\n{text}"
    resp = client.messages.create(model=model, max_tokens=256, messages=[{"role": "user", "content": repair_prompt}])
    repaired = strip_fences(resp.content[0].text)
    return json.loads(repaired)

samples = [
    '{"model":"claude","score":92.1}',
    '```json\n{"model":"gpt","score":87.3}\n```',
    "{'model': 'gemini', 'score': 89.0,}",
]
print("=" * 60)
print("7.8 EXERCISE 03 - AUTOMATIC JSON REPAIR")
print("=" * 60)
for s in samples:
    print("Input :", s.replace("\n", " "))
    print("Parsed:", safe_json_parse(s))
    print()
