"""Exercise 3: metadata filter by year AND topic.
Reference: Python for Gen AI Complete Guide, Module 10, pages 124-125.
Execution: api.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import init_llama
from llama_index.core import Document,VectorStoreIndex
from llama_index.core.vector_stores import MetadataFilters,MetadataFilter,FilterCondition
init_llama();docs=[Document(text=f'Knowledge entry {i} about embeddings and RAG',metadata={'year':2024 if i%2==0 else 2025,'topic':'embeddings' if i<4 else 'agents'}) for i in range(6)]
index=VectorStoreIndex.from_documents(docs)
filters=MetadataFilters(filters=[MetadataFilter(key='year',value=2024),MetadataFilter(key='topic',value='embeddings')],condition=FilterCondition.AND)
for node in index.as_retriever(similarity_top_k=5,filters=filters).retrieve('embedding knowledge'):
    print(node.metadata, node.text)
