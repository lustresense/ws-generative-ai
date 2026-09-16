# Module 05 — 5.1 NumPy Arrays and Dtypes
import numpy as np

scores = np.array([0.91, 0.76, 0.88, 0.65, 0.95], dtype=np.float32)
print(scores.dtype, scores.shape)

zeros = np.zeros((3, 4))
rng_vals = np.arange(0, 1.0, 0.1)
linspace = np.linspace(0, 1, 5)
print("Zeros shape:", zeros.shape)
print("arange:", rng_vals)
print("linspace:", linspace)

rng = np.random.default_rng(seed=42)
mock_embedding = rng.standard_normal(1536)
print(f"Embedding shape: {mock_embedding.shape}, mean: {mock_embedding.mean():.4f}")
