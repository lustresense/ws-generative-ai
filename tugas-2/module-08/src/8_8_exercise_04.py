import hashlib
import json
import sqlite3
from pathlib import Path
from openai import OpenAI

from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv

ENV_FILE = find_dotenv(filename=".env", usecwd=True)
if not ENV_FILE:
    raise RuntimeError(".env tidak ditemukan. Copy .env.example menjadi .env di folder tugas-2.")
load_dotenv(ENV_FILE)


client = OpenAI(api_key=os.environ["GEMINI_API_KEY"], base_url=os.environ["GEMINI_OPENAI_BASE_URL"])
model = os.getenv("GEMINI_EMBEDDING_MODEL", "gemini-embedding-2")
db_path = Path(__file__).resolve().parents[1] / "data" / "embedding_cache.db"

def cache_key(text: str, model_name: str) -> str:
    return hashlib.sha256((text + model_name).encode("utf-8")).hexdigest()

def init_db():
    with sqlite3.connect(db_path) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS embeddings (cache_key TEXT PRIMARY KEY, model TEXT, text TEXT, vector_json TEXT)")

def embed_with_cache(text: str, model_name: str = model) -> list[float]:
    key = cache_key(text, model_name)
    with sqlite3.connect(db_path) as conn:
        row = conn.execute("SELECT vector_json FROM embeddings WHERE cache_key=?", (key,)).fetchone()
        if row:
            print("CACHE HIT :", key[:12])
            return json.loads(row[0])
    print("CACHE MISS:", key[:12], "-> calling embedding API")
    response = client.embeddings.create(input=[text], model=model_name)
    vector = response.data[0].embedding
    with sqlite3.connect(db_path) as conn:
        conn.execute("INSERT OR REPLACE INTO embeddings(cache_key, model, text, vector_json) VALUES(?,?,?,?)", (key, model_name, text, json.dumps(vector)))
    return vector

print("=" * 60)
print("8.8 EXERCISE 04 - SQLITE EMBEDDING CACHE")
print("=" * 60)
init_db()
text = "RAG combines retrieval with generation for grounded answers."
# Reset this one demonstration key so every workshop run visibly shows MISS -> HIT.
with sqlite3.connect(db_path) as conn:
    conn.execute("DELETE FROM embeddings WHERE cache_key=?", (cache_key(text, model),))
v1 = embed_with_cache(text)
v2 = embed_with_cache(text)
print("Vector length:", len(v1))
print("Same cached value:", v1 == v2)
print("Database:", db_path)
