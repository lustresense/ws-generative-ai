# Module 03 — 3.5 Modules and Packages
from demo_ai_project.config import LLMConfig
from demo_ai_project.clients.anthropic import AnthropicClient
from demo_ai_project.retrieval.chunker import chunk_text
import demo_ai_project.retrieval.embedder as embedder

cfg = LLMConfig(model="claude-sonnet-4-5", temperature=0.3)
client = AnthropicClient(cfg.model)
chunks = chunk_text("hello world from a small package demo", chunk_size=12)
vectors = embedder.embed_texts(["hello", "world"])

print(cfg)
print(client)
print("Chunks:", chunks)
print("Vectors:", vectors)
