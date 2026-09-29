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
print("6.2A - ANTHROPIC BASIC MESSAGE")
print("=" * 60)
message = client.messages.create(
    model=model,
    max_tokens=1024,
    messages=[{"role": "user", "content": "What is retrieval-augmented generation?"}],
)
print(message.content[0].text)
print(f"\nInput tokens : {message.usage.input_tokens}")
print(f"Output tokens: {message.usage.output_tokens}")
print(f"Model        : {model}")
