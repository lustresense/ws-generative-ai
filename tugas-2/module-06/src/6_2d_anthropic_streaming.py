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
print("6.2D - ANTHROPIC STREAMING")
print("=" * 60)
with client.messages.stream(
    model=model,
    max_tokens=512,
    messages=[{"role": "user", "content": "List 5 use cases for vector databases."}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
    final = stream.get_final_message()
print()
print(f"\nTotal tokens: {final.usage.input_tokens + final.usage.output_tokens}")
