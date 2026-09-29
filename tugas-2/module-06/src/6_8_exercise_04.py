import anthropic
from pathlib import Path

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

def stream_to_file(prompt: str, output_path: str) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        with client.messages.stream(
            model=model,
            max_tokens=512,
            messages=[{"role": "user", "content": prompt}],
        ) as stream:
            for token in stream.text_stream:
                print(token, end="", flush=True)
                f.write(token)
                f.flush()
    print()

print("=" * 60)
print("6.8 EXERCISE 04 - STREAM TO FILE")
print("=" * 60)
out = Path(__file__).resolve().parents[1] / "data" / "stream_output.txt"
stream_to_file("Explain why streaming improves chat UX in one short paragraph.", str(out))
print(f"Saved to: {out}")
