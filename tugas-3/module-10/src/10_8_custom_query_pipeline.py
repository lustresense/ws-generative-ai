"""RetrieverQueryEngine with COMPACT and TREE_SUMMARIZE response modes.
Reference: Python for Gen AI Complete Guide, Module 10, pages 123-124.
Execution: api.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import init_llama,show
from llama_index.core import VectorStoreIndex,Document
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.response_synthesizers import get_response_synthesizer,ResponseMode
init_llama();idx=VectorStoreIndex.from_documents([Document(text='HNSW enables approximate nearest neighbor search.'),Document(text='IVF partitions vectors into clusters.'),Document(text='Quantization reduces vector storage cost.')]); retriever=VectorIndexRetriever(index=idx,similarity_top_k=2)
for mode in (ResponseMode.COMPACT,ResponseMode.TREE_SUMMARIZE):
    engine=RetrieverQueryEngine(retriever=retriever,response_synthesizer=get_response_synthesizer(response_mode=mode))
    show(str(mode),engine.query('What index algorithms accelerate vector search?'))
