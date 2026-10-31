"""VectorIndexRetriever retrieves nodes without calling generation model.
Reference: Python for Gen AI Complete Guide, Module 10, pages 119-120.
Execution: api.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import init_llama,tiny_documents
from llama_index.core import Document,VectorStoreIndex
from llama_index.core.retrievers import VectorIndexRetriever
init_llama();idx=VectorStoreIndex.from_documents([Document(text=t,metadata={'source':k}) for k,t in tiny_documents()])
retriever=VectorIndexRetriever(index=idx,similarity_top_k=3)
for node in retriever.retrieve('Which method changes model weights?'):print(round(node.score or 0,4),node.metadata.get('source'),node.text)
