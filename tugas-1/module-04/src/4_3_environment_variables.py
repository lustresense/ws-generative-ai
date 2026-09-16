# Module 04 — 4.3 Environment Variables and Secrets
import os
from pathlib import Path
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[3]
load_dotenv(ROOT / ".env")


def get_api_key(provider: str) -> str:
    key_map = {
        "anthropic": "ANTHROPIC_API_KEY",
        "openai": "OPENAI_API_KEY",
        "google": "GOOGLE_API_KEY",
    }
    env_var = key_map.get(provider.lower())
    if not env_var:
        raise ValueError(f"Unknown provider: {provider}")

    key = os.getenv(env_var)
    if not key:
        raise EnvironmentError(
            f"{env_var} is not set. Add it to your .env file."
        )
    return key


for provider in ["anthropic", "openai", "google"]:
    try:
        key = get_api_key(provider)
        print(f"{provider}: key loaded ({key[:4]}... hidden)")
    except EnvironmentError as error:
        print(f"{provider}: {error}")
