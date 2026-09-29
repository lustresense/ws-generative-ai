from openai import OpenAI
import json

from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv

ENV_FILE = find_dotenv(filename=".env", usecwd=True)
if not ENV_FILE:
    raise RuntimeError(".env tidak ditemukan. Copy .env.example menjadi .env di folder tugas-2.")
load_dotenv(ENV_FILE)


client = OpenAI(api_key=os.environ["NINEROUTER_API_KEY"], base_url=os.environ["NINEROUTER_BASE_URL"].rstrip("/") + "/v1")
model = os.getenv("OPENAI_MODEL", "cx/gpt-5.6-luna")

print("=" * 60)
print("7.5B - OPENAI JSON MODE VIA 9ROUTER")
print("=" * 60)
response = client.chat.completions.create(
    model=model,
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": 'Extract entities. Return JSON with this schema: {"people": [string], "organizations": [string], "locations": [string]}'},
        {"role": "user", "content": "Elon Musk founded SpaceX in Hawthorne, California. He also leads Tesla."},
    ],
)
result = json.loads(response.choices[0].message.content)
print(json.dumps(result, indent=2))
