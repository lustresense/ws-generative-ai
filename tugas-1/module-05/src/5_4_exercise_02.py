# Module 05 — Exercise 2
import numpy as np


def normalise_embeddings(matrix: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    if np.any(norms == 0):
        raise ValueError("Cannot normalise a zero vector")
    return matrix / norms


rng = np.random.default_rng(42)
matrix = rng.standard_normal((5, 8))
normalised = normalise_embeddings(matrix)
row_norms = np.linalg.norm(normalised, axis=1)

print("Original shape:", matrix.shape)
print("Row norms after normalisation:", row_norms)
print("All equal 1.0:", np.allclose(row_norms, 1.0))
