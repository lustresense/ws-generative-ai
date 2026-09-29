from openai import OpenAI
import numpy as np

from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv

ENV_FILE = find_dotenv(filename=".env", usecwd=True)
if not ENV_FILE:
    raise RuntimeError(".env tidak ditemukan. Copy .env.example menjadi .env di folder tugas-2.")
load_dotenv(ENV_FILE)


client = OpenAI(
    api_key=os.environ["GEMINI_API_KEY"],
    base_url=os.environ["GEMINI_OPENAI_BASE_URL"],
)
model = os.getenv("GEMINI_EMBEDDING_MODEL", "gemini-embedding-2")

def embed(texts: list[str], model_name: str = model) -> np.ndarray:
    response = client.embeddings.create(input=texts, model=model_name)
    vectors = sorted(response.data, key=lambda e: e.index if e.index is not None else 0)
    return np.array([v.embedding for v in vectors], dtype=np.float32)

texts = [
    "Retrieval-Augmented Generation combines search with LLMs.",
    "RAG retrieves documents then generates an answer from them.",
    "The Eiffel Tower is in Paris.",
    "Python is a popular programming language.",
    "Fine-tuning trains a model on new data.",
]

print("=" * 60)
print("8.2A - OPENAI SDK EMBEDDINGS VIA GEMINI")
print("=" * 60)
embeddings = embed(texts)
print(f"Model               : {model}")
print(f"Shape               : {embeddings.shape}")
print(f"Norm of first vector: {np.linalg.norm(embeddings[0]):.4f}")
print(f"First 5 values      : {embeddings[0][:5]}")
