import numpy as np
from dataclasses import dataclass, field
from typing import Optional
from openai import OpenAI

from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv

ENV_FILE = find_dotenv(filename=".env", usecwd=True)
if not ENV_FILE:
    raise RuntimeError(".env tidak ditemukan. Copy .env.example menjadi .env di folder tugas-2.")
load_dotenv(ENV_FILE)


openai_client = OpenAI(api_key=os.environ["GEMINI_API_KEY"], base_url=os.environ["GEMINI_OPENAI_BASE_URL"])
EMBED_MODEL = os.getenv("GEMINI_EMBEDDING_MODEL", "gemini-embedding-2")

@dataclass
class Document:
    id: str
    text: str
    metadata: dict = field(default_factory=dict)
    embedding: Optional[np.ndarray] = field(default=None, repr=False)

@dataclass
class SearchResult:
    document: Document
    score: float
    rank: int

def embed_batch(texts: list[str], model: str = EMBED_MODEL) -> np.ndarray:
    response = openai_client.embeddings.create(input=texts, model=model)
    vectors = sorted(response.data, key=lambda e: e.index if e.index is not None else 0)
    return np.array([v.embedding for v in vectors], dtype=np.float32)

class VectorStore:
    def __init__(self, embed_model: str = EMBED_MODEL):
        self.embed_model = embed_model
        self._documents: list[Document] = []
        self._matrix: Optional[np.ndarray] = None

    def add_documents(self, documents: list[Document]) -> None:
        vectors = embed_batch([d.text for d in documents], model=self.embed_model)
        norms = np.linalg.norm(vectors, axis=1, keepdims=True)
        normed = (vectors / np.where(norms == 0, 1, norms)).astype(np.float32)
        for doc, vec in zip(documents, normed):
            doc.embedding = vec
            self._documents.append(doc)
        self._matrix = np.array([d.embedding for d in self._documents], dtype=np.float32)

    def search(self, query: str, k: int = 5) -> list[SearchResult]:
        if self._matrix is None or not self._documents:
            raise RuntimeError("No documents indexed yet.")
        q_vec = embed_batch([query], model=self.embed_model)[0]
        q_norm = np.linalg.norm(q_vec)
        if q_norm == 0:
            return []
        q_vec = (q_vec / q_norm).astype(np.float32)
        scores = self._matrix @ q_vec
        k = min(k, len(self._documents))
        top_idx = np.argsort(scores)[::-1][:k]
        return [SearchResult(self._documents[int(i)], float(scores[i]), rank + 1) for rank, i in enumerate(top_idx)]

    @property
    def size(self) -> int:
        return len(self._documents)

class MutableVectorStore(VectorStore):
    def _rebuild(self):
        self._matrix = np.array([d.embedding for d in self._documents], dtype=np.float32) if self._documents else None

    def delete(self, doc_id: str) -> bool:
        before = len(self._documents)
        self._documents = [d for d in self._documents if d.id != doc_id]
        self._rebuild()
        return len(self._documents) < before

    def update(self, doc_id: str, new_text: str) -> bool:
        for doc in self._documents:
            if doc.id == doc_id:
                vec = embed_batch([new_text], model=self.embed_model)[0]
                norm = np.linalg.norm(vec)
                doc.text = new_text
                doc.embedding = (vec / (norm if norm else 1)).astype(np.float32)
                self._rebuild()
                return True
        return False

print("=" * 60)
print("8.8 EXERCISE 03 - VECTOR STORE DELETE / UPDATE")
print("=" * 60)
store = MutableVectorStore()
store.add_documents([
    Document("d1", "RAG retrieves documents before generation."),
    Document("d2", "Vector databases store embeddings."),
    Document("d3", "Fine-tuning updates model weights."),
    Document("d4", "Prompt engineering changes instructions."),
])
print("Initial size/matrix:", store.size, store._matrix.shape)
print("Delete d2:", store.delete("d2"), "->", store.size, store._matrix.shape)
print("Update d3:", store.update("d3", "Fine-tuning adapts a pretrained model using task-specific training data."), "->", store._matrix.shape)
print("Search after mutations:")
for r in store.search("How do I adapt model weights?", k=2):
    print(f" [{r.rank}] {r.document.id} score={r.score:.4f} | {r.document.text}")
