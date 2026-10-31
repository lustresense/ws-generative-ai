"""Chroma metadata filtering and explicit embedding update/delete.
Reference: Python for Gen AI Complete Guide, Module 11, pages 127-128.
Execution: api.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import chromadb
from common import ROOT,gemini_embed
coll=chromadb.PersistentClient(path=str(ROOT/'module-11'/'data'/'chroma_store')).get_or_create_collection('m11_crud')
emb=gemini_embed()
texts=['RAG retrieves documents','An agent calls tools','Fine-tuning adapts a language model']
coll.upsert(ids=['d1','d2','d3'],documents=texts,embeddings=emb.embed_documents(texts),metadatas=[{'kind':'rag'},{'kind':'agent'},{'kind':'training'}])
q=emb.embed_query('RAG retrieves external sources')
print('Filtered:',coll.query(query_embeddings=[q],n_results=2,where={'kind':'rag'})['ids'])
new='RAG combines semantic search with answer generation'
coll.update(ids=['d1'],documents=[new],embeddings=emb.embed_documents([new]))
coll.delete(ids=['d2']); print('After delete:',coll.count())
