"""Pinecone external serverless index + upsert + query. Requires opt-in/API key.
Reference: Python for Gen AI Complete Guide, Module 11, pages 128-130.
Execution: cloud.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import required,gemini_embed
from pinecone import Pinecone,ServerlessSpec
import os
api=required('PINECONE_API_KEY'); pc=Pinecone(api_key=api)
name=os.getenv('PINECONE_INDEX','genai-phase3-demo')
embed=gemini_embed(); docs=['RAG is retrieval plus generation','Fine-tuning changes model weights'];v=embed.embed_documents(docs);dim=len(v[0])
if name not in pc.list_indexes().names():
    pc.create_index(name=name,dimension=dim,metric='cosine',spec=ServerlessSpec(cloud='aws',region='us-east-1'))
index=pc.Index(name)
index.upsert(vectors=[{'id':f'd{i}','values':vec,'metadata':{'text':text,'source':'phase3'}} for i,(vec,text) in enumerate(zip(v,docs))])
print(index.query(vector=embed.embed_query('external knowledge for AI'),top_k=2,include_metadata=True))
