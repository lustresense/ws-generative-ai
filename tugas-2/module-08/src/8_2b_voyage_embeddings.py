import voyageai
import numpy as np

from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv

ENV_FILE = find_dotenv(filename=".env", usecwd=True)
if not ENV_FILE:
    raise RuntimeError(".env tidak ditemukan. Copy .env.example menjadi .env di folder tugas-2.")
load_dotenv(ENV_FILE)


vo = voyageai.Client(api_key=os.environ["VOYAGE_API_KEY"])
model = os.getenv("VOYAGE_MODEL", "voyage-4-lite")

print("=" * 60)
print("8.2B - VOYAGE AI EMBEDDINGS")
print("=" * 60)
print("PDF model: voyage-3 | Current workshop model:", model)
result = vo.embed(
    ["What is RAG?", "Explain vector databases."],
    model=model,
    input_type="document",
)
embeddings = np.array(result.embeddings, dtype=np.float32)
print(f"Shape      : {embeddings.shape}")
print(f"Token usage: {result.total_tokens}")
print(f"First 5 values: {embeddings[0][:5]}")
