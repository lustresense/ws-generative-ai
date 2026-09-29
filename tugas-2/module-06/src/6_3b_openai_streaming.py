from openai import OpenAI

from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv

ENV_FILE = find_dotenv(filename=".env", usecwd=True)
if not ENV_FILE:
    raise RuntimeError(".env tidak ditemukan. Copy .env.example menjadi .env di folder tugas-2.")
load_dotenv(ENV_FILE)


client = OpenAI(
    api_key=os.environ["NINEROUTER_API_KEY"],
    base_url=os.environ["NINEROUTER_BASE_URL"].rstrip("/") + "/v1",
)
model = os.getenv("OPENAI_MODEL", "cx/gpt-5.6-luna")

print("=" * 60)
print("6.3B - OPENAI SDK STREAMING VIA 9ROUTER")
print("=" * 60)
stream = client.chat.completions.create(
    model=model,
    max_tokens=512,
    stream=True,
    messages=[{"role": "user", "content": "Explain embeddings in 3 bullet points."}],
)
for chunk in stream:
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)
print()
