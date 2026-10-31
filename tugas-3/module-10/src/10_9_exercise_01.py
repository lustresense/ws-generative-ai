"""Exercise 1: folder Q&A returns answer and source filenames.
Reference: Python for Gen AI Complete Guide, Module 10, pages 124.
Execution: api.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import init_llama,ROOT,show
from llama_index.core import Document,VectorStoreIndex
folder=ROOT/'module-10'/'data'/'sample_docs';folder.mkdir(parents=True,exist_ok=True)
(folder/'rag.txt').write_text('RAG retrieves documents before generation.',encoding='utf-8')
(folder/'vector.txt').write_text('Vector databases store numeric embeddings for similarity search.',encoding='utf-8')
init_llama();index=VectorStoreIndex.from_documents([Document(text=f.read_text(encoding='utf-8'),metadata={'filename':f.name}) for f in sorted(folder.glob('*.txt'))])
def ask(question):
    r=index.as_query_engine(similarity_top_k=2).query(question)
    return {'answer':str(r),'sources':sorted({s.node.metadata.get('filename') for s in r.source_nodes})}
show('ask()',ask('What is RAG?'))
