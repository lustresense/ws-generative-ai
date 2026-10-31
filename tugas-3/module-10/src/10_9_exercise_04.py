"""Exercise 4: retrieve top-10 then LLM relevance rerank top-3.
Reference: Python for Gen AI Complete Guide, Module 10, pages 125.
Execution: api.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import re
from common import init_llama,chat_llm
from llama_index.core import Document,VectorStoreIndex
init_llama();docs=[Document(text=f'Note {i}: {topic}') for i,topic in enumerate(['RAG retrieval and grounding','Embedding vectors','Fine-tuning weights','Agent tool calling','Prompt evaluation','Vector indexing','Context windows','Metadata filters','Database persistence','Response synthesis','Training loss','GPU memory'])]
index=VectorStoreIndex.from_documents(docs)
question='How do RAG and embeddings work together?'
rows=[]
for item in index.as_retriever(similarity_top_k=10).retrieve(question):
    answer=chat_llm().invoke(f'Rate relevance 0 to 10. Respond ONLY an integer. Question: {question}\nText: {item.text}').content
    m=re.search(r'\b(?:10|[0-9])\b',str(answer))
    rows.append((int(m.group()) if m else 0,item.text))
for score,content in sorted(rows,reverse=True)[:3]:print(score,content)
