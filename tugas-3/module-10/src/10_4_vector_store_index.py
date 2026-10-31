"""LlamaIndex VectorStoreIndex and query engine with source nodes.
Reference: Python for Gen AI Complete Guide, Module 10, pages 118-119.
Execution: api.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import init_llama,tiny_documents,show
from llama_index.core import VectorStoreIndex,Document
init_llama();docs=[Document(text=t,metadata={'source':k}) for k,t in tiny_documents()]
index=VectorStoreIndex.from_documents(docs)
response=index.as_query_engine(similarity_top_k=3).query('How does RAG work?')
show('Answer',response)
for node in response.source_nodes:print('Source:',node.node.metadata,'score:',node.score)
