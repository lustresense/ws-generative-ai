import asyncio
import time
import pandas as pd
import anthropic
from openai import OpenAI

from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv

ENV_FILE = find_dotenv(filename=".env", usecwd=True)
if not ENV_FILE:
    raise RuntimeError(".env tidak ditemukan. Copy .env.example menjadi .env di folder tugas-2.")
load_dotenv(ENV_FILE)


openai_client = OpenAI(
    api_key=os.environ["NINEROUTER_API_KEY"],
    base_url=os.environ["NINEROUTER_BASE_URL"].rstrip("/") + "/v1",
)
anthropic_client = anthropic.Anthropic(
    api_key=os.environ["NINEROUTER_API_KEY"],
    base_url=os.environ["NINEROUTER_BASE_URL"].rstrip("/"),
)
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "cx/gpt-5.6-luna")
ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL", "ag/claude-sonnet-4-6")

async def call_one(prompt: str, model: str) -> dict:
    started = time.perf_counter()
    if model == ANTHROPIC_MODEL:
        def do_call():
            r = anthropic_client.messages.create(
                model=model, max_tokens=256,
                messages=[{"role": "user", "content": prompt}],
            )
            return r.content[0].text, r.usage.input_tokens, r.usage.output_tokens
    else:
        def do_call():
            r = openai_client.chat.completions.create(
                model=model, max_tokens=256,
                messages=[{"role": "user", "content": prompt}],
            )
            u = r.usage
            return r.choices[0].message.content or "", (u.prompt_tokens if u else 0), (u.completion_tokens if u else 0)
    text, input_tokens, output_tokens = await asyncio.to_thread(do_call)
    return {
        "model": model,
        "response_text": text.replace("\n", " ")[:180],
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "latency_ms": round((time.perf_counter() - started) * 1000, 1),
    }

async def compare_models(prompt: str, models: list[str]) -> pd.DataFrame:
    rows = await asyncio.gather(*(call_one(prompt, m) for m in models))
    return pd.DataFrame(rows, columns=["model", "response_text", "input_tokens", "output_tokens", "latency_ms"])

async def main():
    print("=" * 60)
    print("6.8 EXERCISE 03 - CONCURRENT MODEL COMPARISON")
    print("=" * 60)
    df = await compare_models("Explain semantic search in two sentences.", [OPENAI_MODEL, ANTHROPIC_MODEL])
    print(df.to_string(index=False))

if __name__ == "__main__":
    asyncio.run(main())
