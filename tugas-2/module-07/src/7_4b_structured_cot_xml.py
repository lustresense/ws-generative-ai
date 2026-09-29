import anthropic
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

SYSTEM = """Solve problems using this exact format:
<thinking>
Step-by-step reasoning here.
</thinking>
<answer>
The final answer only, no reasoning.
</answer>"""

print("=" * 60)
print("7.4B - STRUCTURED CoT WITH XML TAGS")
print("=" * 60)
resp = client.messages.create(
    model=model, max_tokens=512, system=SYSTEM,
    messages=[{"role": "user", "content": "A RAG pipeline retrieves 5 documents, each 400 tokens. The query is 50 tokens. The model has a 4096 token limit for context. How many tokens remain for the response?"}],
)
text = resp.content[0].text
thinking = re.search(r"<thinking>(.*?)</thinking>", text, re.DOTALL)
answer = re.search(r"<answer>(.*?)</answer>", text, re.DOTALL)
print("Reasoning:", thinking.group(1).strip() if thinking else "not found")
print("Answer   :", answer.group(1).strip() if answer else "not found")
