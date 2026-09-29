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
print("6.3A - OPENAI SDK BASIC MESSAGE VIA 9ROUTER")
print("=" * 60)
response = client.chat.completions.create(
    model=model,
    max_tokens=1024,
    messages=[
        {"role": "system", "content": "You are a concise technical assistant."},
        {"role": "user", "content": "What is the difference between RAG and fine-tuning?"},
    ],
)
print(response.choices[0].message.content)
print(f"\nTokens used: {response.usage.total_tokens if response.usage else 'n/a'}")
print(f"Model      : {model}")
