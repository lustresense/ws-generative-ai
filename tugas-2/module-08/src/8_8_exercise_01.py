import numpy as np
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

class DuplicateDetector:
    def __init__(self, threshold: float = 0.95):
        self.threshold = threshold
    def embed(self, docs: list[str]) -> np.ndarray:
        r = client.embeddings.create(input=docs, model=model)
        vecs = np.array([e.embedding for e in sorted(r.data, key=lambda x: x.index if x.index is not None else 0)], dtype=np.float32)
        norms = np.linalg.norm(vecs, axis=1, keepdims=True)
        return vecs / np.where(norms == 0, 1, norms)
    def find_duplicates(self, docs: list[str]):
        v = self.embed(docs)
        sim = v @ v.T
        pairs = []
        for i in range(len(docs)):
            for j in range(i + 1, len(docs)):
                if sim[i, j] >= self.threshold:
                    pairs.append((i, j, float(sim[i, j])))
        return sorted(pairs, key=lambda x: x[2], reverse=True)

base = [
    "RAG combines document retrieval with language model generation.",
    "Vector databases store embedding vectors for semantic search.",
    "Fine-tuning updates model weights using task-specific data.",
    "Prompt engineering guides model behavior through instructions.",
    "Cosine similarity measures how aligned two vectors are.",
    "Transformers use attention to model token relationships.",
    "Agents can call tools and perform multi-step tasks.",
    "Chunking splits long documents into retrievable pieces.",
    "Embeddings represent semantic meaning as numerical vectors.",
    "Evaluation measures whether retrieval returns relevant documents.",
]
corpus = []
for i in range(5):
    for text in base:
        # Groups 0 and 1 intentionally contain exact near-duplicates; the corpus still has 50 entries.
        corpus.append(text if i < 2 else f"{text} Example variant number {i}.")

print("=" * 60)
print("8.8 EXERCISE 01 - DUPLICATE DETECTOR (50 DOCS)")
print("=" * 60)
detector = DuplicateDetector(threshold=0.95)
pairs = detector.find_duplicates(corpus)
print(f"Corpus size: {len(corpus)} | duplicate pairs >= {detector.threshold}: {len(pairs)}")
for i, j, score in pairs[:12]:
    print(f" ({i:02d}, {j:02d}) similarity={score:.4f} | {corpus[i][:55]}")
