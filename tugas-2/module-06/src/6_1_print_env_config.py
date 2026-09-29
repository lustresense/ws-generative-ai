import json

from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv

ENV_FILE = find_dotenv(filename=".env", usecwd=True)
if not ENV_FILE:
    raise RuntimeError(".env tidak ditemukan. Copy .env.example menjadi .env di folder tugas-2.")
load_dotenv(ENV_FILE)


CONFIG_KEYS = [
    "NINEROUTER_BASE_URL",
    "NINEROUTER_API_KEY",
    "OPENAI_MODEL",
    "ANTHROPIC_MODEL",
    "GEMINI_API_KEY",
    "GEMINI_OPENAI_BASE_URL",
    "GEMINI_EMBEDDING_MODEL",
    "VOYAGE_API_KEY",
    "VOYAGE_MODEL",
]
SECRET_KEYS = {"NINEROUTER_API_KEY", "GEMINI_API_KEY", "VOYAGE_API_KEY"}

def masked(value: str | None) -> str:
    return "************************" if value else "(not set)"

config = {}
for key in CONFIG_KEYS:
    value = os.getenv(key)
    config[key] = masked(value) if key in SECRET_KEYS else (value or "(not set)")

print("=" * 60)
print("6.1 - ENVIRONMENT CONFIGURATION")
print("=" * 60)
print(json.dumps(config, indent=2))
