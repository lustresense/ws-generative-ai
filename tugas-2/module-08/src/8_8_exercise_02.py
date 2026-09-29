import math
import re
from collections import Counter
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

def tokenize(text: str): return re.findall(r"[a-z0-9]+", text.lower())

def embed(texts):
    r = client.embeddings.create(input=texts, model=model)
    v = np.array([e.embedding for e in sorted(r.data, key=lambda x: x.index if x.index is not None else 0)], dtype=np.float32)
    norms = np.linalg.norm(v, axis=1, keepdims=True)
    return v / np.where(norms == 0, 1, norms)

class HybridSearch:
    def __init__(self, documents: list[str], alpha: float = 0.7):
        self.documents = documents
        self.alpha = alpha
        self.doc_vectors = embed(documents)
        self.tokens = [tokenize(d) for d in documents]
        self.avgdl = sum(map(len, self.tokens)) / len(self.tokens)
        self.df = Counter()
        for toks in self.tokens:
            for term in set(toks): self.df[term] += 1

    def keyword_scores(self, query: str):
        q = tokenize(query); n = len(self.documents); scores = []
        for toks in self.tokens:
            tf = Counter(toks); dl = len(toks); score = 0.0
            for term in q:
                if term not in tf: continue
                idf = math.log(1 + (n - self.df[term] + 0.5) / (self.df[term] + 0.5))
                f = tf[term]; k1, b = 1.5, 0.75
                score += idf * (f * (k1 + 1)) / (f + k1 * (1 - b + b * dl / self.avgdl))
            scores.append(score)
        arr = np.array(scores, dtype=np.float32)
        return arr / arr.max() if arr.max() > 0 else arr

    def search(self, query: str, k: int = 3):
        qv = embed([query])[0]
        semantic = self.doc_vectors @ qv
        semantic = (semantic + 1) / 2
        keyword = self.keyword_scores(query)
        final = self.alpha * semantic + (1 - self.alpha) * keyword
        idx = np.argsort(final)[::-1][:k]
        return [(int(i), float(final[i]), float(semantic[i]), float(keyword[i])) for i in idx]

docs = [
    "RAG retrieves external documents before generating an answer.",
    "Vector databases support semantic nearest-neighbour search over embeddings.",
    "Fine-tuning changes model weights using training examples.",
    "Document chunking prepares long text for RAG retrieval.",
    "BM25 is a lexical ranking algorithm based on term frequency and inverse document frequency.",
]

print("=" * 60)
print("8.8 EXERCISE 02 - HYBRID SEARCH")
print("=" * 60)
searcher = HybridSearch(docs, alpha=0.7)
query = "How does RAG retrieve documents?"
print(f"Query: {query} | alpha={searcher.alpha}")
for i, final, sem, key in searcher.search(query):
    print(f" final={final:.4f} semantic={sem:.4f} keyword={key:.4f} | {docs[i]}")
