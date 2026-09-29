from pathlib import Path
import os
import sys
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
ENV = ROOT / ".env"
if not ENV.exists():
    print("[FAIL] .env belum ada.")
    print("       Copy .env.example menjadi .env lalu isi API key/domain.")
    sys.exit(1)
load_dotenv(ENV)

required = [
    "NINEROUTER_BASE_URL", "NINEROUTER_API_KEY", "OPENAI_MODEL", "ANTHROPIC_MODEL",
    "GEMINI_API_KEY", "GEMINI_OPENAI_BASE_URL", "GEMINI_EMBEDDING_MODEL",
    "VOYAGE_API_KEY", "VOYAGE_MODEL",
]
missing = [k for k in required if not os.getenv(k)]
print("=" * 68)
print("TUGAS 2 PRE-FLIGHT")
print("=" * 68)
if missing:
    print("[FAIL] Missing ENV:", ", ".join(missing))
    sys.exit(1)
print("[OK] .env loaded; all required values are present.")

try:
    import anthropic
    from openai import OpenAI
    import voyageai
    import numpy
    import pandas
except Exception as exc:
    print(f"[FAIL] Dependency import: {type(exc).__name__}: {exc}")
    print("       Run: pip install -r requirements.txt")
    sys.exit(1)
print("[OK] Python dependencies import successfully.")

failures = []

# 9Router OpenAI-compatible chat
try:
    oa = OpenAI(
        api_key=os.environ["NINEROUTER_API_KEY"],
        base_url=os.environ["NINEROUTER_BASE_URL"].rstrip("/") + "/v1",
    )
    r = oa.chat.completions.create(
        model=os.environ["OPENAI_MODEL"],
        max_tokens=12,
        messages=[{"role": "user", "content": "Reply exactly: OK"}],
    )
    print(f"[OK] OpenAI-compatible chat | {os.environ['OPENAI_MODEL']} | {r.choices[0].message.content!r}")
except Exception as exc:
    failures.append("9Router OpenAI-compatible")
    print(f"[FAIL] OpenAI-compatible chat: {type(exc).__name__}: {exc}")

# 9Router Anthropic-compatible messages
try:
    ac = anthropic.Anthropic(
        api_key=os.environ["NINEROUTER_API_KEY"],
        base_url=os.environ["NINEROUTER_BASE_URL"].rstrip("/"),
    )
    r = ac.messages.create(
        model=os.environ["ANTHROPIC_MODEL"],
        max_tokens=12,
        messages=[{"role": "user", "content": "Reply exactly: OK"}],
    )
    print(f"[OK] Anthropic-compatible messages | {os.environ['ANTHROPIC_MODEL']} | {r.content[0].text!r}")
except Exception as exc:
    failures.append("9Router Anthropic-compatible")
    print(f"[FAIL] Anthropic-compatible messages: {type(exc).__name__}: {exc}")

# Gemini through OpenAI-compatible embeddings endpoint
try:
    gc = OpenAI(api_key=os.environ["GEMINI_API_KEY"], base_url=os.environ["GEMINI_OPENAI_BASE_URL"])
    r = gc.embeddings.create(input=["preflight semantic search"], model=os.environ["GEMINI_EMBEDDING_MODEL"])
    print(f"[OK] Gemini embedding | {os.environ['GEMINI_EMBEDDING_MODEL']} | dimension={len(r.data[0].embedding)}")
except Exception as exc:
    failures.append("Gemini embedding")
    print(f"[FAIL] Gemini embedding: {type(exc).__name__}: {exc}")

# Voyage embedding
try:
    vc = voyageai.Client(api_key=os.environ["VOYAGE_API_KEY"])
    r = vc.embed(["preflight semantic search"], model=os.environ["VOYAGE_MODEL"], input_type="document")
    print(f"[OK] Voyage embedding | {os.environ['VOYAGE_MODEL']} | dimension={len(r.embeddings[0])}")
except Exception as exc:
    failures.append("Voyage embedding")
    print(f"[FAIL] Voyage embedding: {type(exc).__name__}: {exc}")

print("-" * 68)
if failures:
    print("PRE-FLIGHT FAILED:", ", ".join(failures))
    sys.exit(1)
print("READY — API dasar untuk Module 06–08 berhasil diuji.")
