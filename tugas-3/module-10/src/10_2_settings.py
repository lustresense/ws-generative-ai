"""LlamaIndex Settings: 9Router LLM + Gemini embeddings, chunk parameters.
Reference: Python for Gen AI Complete Guide, Module 10, pages 116.
Execution: api.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import init_llama
settings=init_llama()
print('LLM model:',settings.llm.model)
print('Embedding model:',settings.embed_model.model_name)
print('Chunk size:',settings.chunk_size,'Overlap:',settings.chunk_overlap)
