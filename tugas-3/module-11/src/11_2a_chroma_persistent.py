"""ChromaDB persistent client with explicitly generated Gemini embeddings.
Reference: Python for Gen AI Complete Guide, Module 11, pages 125-127.
Execution: api.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import chromadb
from common import ROOT,gemini_embed
client=chromadb.PersistentClient(path=str(ROOT/'module-11'/'data'/'chroma_store'))
collection=client.get_or_create_collection(name='m11_knowledge',metadata={'hnsw:space':'cosine'})
docs=['RAG retrieves relevant documents.','Fine-tuning adjusts model weights.','Prompt engineering steers model responses.','Vector databases store embeddings.','Agents call tools and make decisions.']
emb=gemini_embed();vectors=emb.embed_documents(docs)
ids=[f'doc_{i}' for i in range(len(docs))]
collection.upsert(ids=ids,documents=docs,embeddings=vectors,metadatas=[{'category':'technique','index':i} for i in range(len(docs))])
print('Count:',collection.count())
result=collection.query(query_embeddings=[emb.embed_query('how to add knowledge without training?')],n_results=3,include=['documents','distances','metadatas'])
for t,d in zip(result['documents'][0],result['distances'][0]):print(round(d,4),t)
