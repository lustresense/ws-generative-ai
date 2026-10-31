"""Exercise 2: MultiCollectionSearch merges Chroma scores across collections.
Reference: Python for Gen AI Complete Guide, Module 11, pages 134.
Execution: offline.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import chromadb
from common import mock_embed
c=chromadb.EphemeralClient()
for name,docs in {'research':['RAG retrieves facts','Vector storage'],'software':['Python functions','LLM prompt chains']}.items():
    col=c.get_or_create_collection(name,metadata={'hnsw:space':'cosine'});col.upsert(ids=[f'{name}_{i}' for i in range(len(docs))],documents=docs,embeddings=mock_embed(docs))
class MultiCollectionSearch:
    def __init__(self,client,names):self.client,self.names=client,names
    def search(self,query,k=3):
        ranked=[]
        for name in self.names:
            result=self.client.get_collection(name).query(query_embeddings=mock_embed([query]),n_results=k,include=['documents','distances'])
            ranked.extend((1-float(distance),name,text) for text,distance in zip(result['documents'][0],result['distances'][0]))
        return sorted(ranked,reverse=True)[:k]
print(MultiCollectionSearch(c,['research','software']).search('vector AI',3))
print('Note: score uses 1-distance for comparable cosine collections.')
