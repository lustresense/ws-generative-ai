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

WEAK_SYSTEM = "You are an AI assistant."
STRONG_SYSTEM = """You are a senior Python engineer reviewing code for a production AI pipeline.

Your job:
- Identify bugs, security issues, and performance problems
- Suggest concrete improvements with code examples
- Explain WHY each issue matters

Rules:
- Be direct. Do not pad with compliments.
- If code is correct, say so briefly and move on.
- Always include the corrected code when suggesting a fix.

Format:
Return your review as a numbered list. Each item: Issue → Impact → Fix."""

code = """Review this function:

def get_user(user_id):
    key = os.getenv('DB_KEY')
    result = requests.get(f'http://db/{user_id}?key={key}')
    return result.json()"""

print("=" * 60)
print("7.2 - SYSTEM PROMPTS")
print("=" * 60)
response = client.messages.create(model=model, max_tokens=1024, system=STRONG_SYSTEM, messages=[{"role": "user", "content": code}])
print(response.content[0].text)
