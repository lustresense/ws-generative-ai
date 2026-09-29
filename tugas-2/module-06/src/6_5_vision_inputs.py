import anthropic
import base64
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

def describe_image_url(url: str) -> str:
    response = client.messages.create(
        model=model,
        max_tokens=512,
        messages=[{"role": "user", "content": [
            {"type": "image", "source": {"type": "url", "url": url}},
            {"type": "text", "text": "Describe what you see in this image."},
        ]}],
    )
    return response.content[0].text

def describe_image_file(path: str) -> str:
    p = Path(path)
    data = p.read_bytes()
    b64 = base64.standard_b64encode(data).decode()
    ext = p.suffix.lstrip(".").lower()
    if ext == "jpg":
        ext = "jpeg"
    media_type = f"image/{ext}"
    response = client.messages.create(
        model=model,
        max_tokens=512,
        messages=[{"role": "user", "content": [
            {"type": "image", "source": {"type": "base64", "media_type": media_type, "data": b64}},
            {"type": "text", "text": "What is in this image?"},
        ]}],
    )
    return response.content[0].text

print("=" * 60)
print("6.5 - VISION: URL + LOCAL BASE64")
print("=" * 60)
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Sunrise_over_the_sea.jpg/1280px-Sunrise_over_the_sea.jpg"
local_path = Path(__file__).resolve().parents[1] / "data" / "sample_vision.png"

print("[Option A - URL]")
try:
    print(describe_image_url(url))
except Exception as exc:
    print(f"URL image failed: {type(exc).__name__}: {exc}")

print("\n[Option B - Local base64]")
print(describe_image_file(str(local_path)))
