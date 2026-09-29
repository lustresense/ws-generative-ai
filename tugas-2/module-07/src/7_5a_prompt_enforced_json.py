import anthropic
import json

from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv

ENV_FILE = find_dotenv(filename=".env", usecwd=True)
if not ENV_FILE:
    raise RuntimeError(".env tidak ditemukan. Copy .env.example menjadi .env di folder tugas-2.")
load_dotenv(ENV_FILE)


client = anthropic.Anthropic(api_key=os.environ["NINEROUTER_API_KEY"], base_url=os.environ["NINEROUTER_BASE_URL"].rstrip("/"))
model = os.getenv("ANTHROPIC_MODEL", "ag/claude-sonnet-4-6")

SYSTEM = """You are a data extractor. Extract information and return ONLY a JSON object.
No markdown, no explanation, no code fences. Raw JSON only.
Schema:
{
  "company": string,
  "founded": integer or null,
  "products": [string],
  "headquarters": string or null,
  "is_public": boolean
}"""
texts = [
    "Anthropic was founded in 2021 by Dario Amodei and others. It makes Claude AI models and is headquartered in San Francisco. It is a private company.",
    "OpenAI, founded in 2015, created ChatGPT and GPT-4. Based in San Francisco, it remains private despite a major Microsoft investment.",
]

def extract_company_info(text: str) -> dict:
    resp = client.messages.create(model=model, max_tokens=256, system=SYSTEM, messages=[{"role": "user", "content": text}])
    raw = resp.content[0].text.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    return json.loads(raw)

print("=" * 60)
print("7.5A - PROMPT-ENFORCED JSON")
print("=" * 60)
for text in texts:
    print(json.dumps(extract_company_info(text), indent=2))
    print()
