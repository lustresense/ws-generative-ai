# Module 05 — Exercise 4
import hashlib
import numpy as np


def mock_embedding(text: str, dim: int = 16) -> np.ndarray:
    digest = hashlib.sha256(text.encode("utf-8")).digest()
    seed = int.from_bytes(digest[:8], "little")
    rng = np.random.default_rng(seed)
    return rng.standard_normal(dim)


def pairwise_cosine(matrix: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    normalised = matrix / np.where(norms == 0, 1, norms)
    return normalised @ normalised.T


corpus = [
    "RAG retrieves documents before generation.",
    "Retrieval augmented generation uses external documents.",
    "Python is a programming language.",
    "Vector databases store embedding vectors.",
    "Agents can call tools to complete tasks.",
]
embeddings = np.vstack([mock_embedding(text) for text in corpus])
similarity = pairwise_cosine(embeddings)

best_pair = None
best_score = -np.inf
for i in range(len(corpus)):
    for j in range(i + 1, len(corpus)):
        if similarity[i, j] > best_score:
            best_score = float(similarity[i, j])
            best_pair = (i, j)

print("Pairwise cosine similarity matrix:")
print(np.round(similarity, 3))
i, j = best_pair
print(f"Highest pair: {i} & {j}")
print(f"Score: {best_score:.4f}")
print("A:", corpus[i])
print("B:", corpus[j])
