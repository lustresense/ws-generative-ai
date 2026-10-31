"""Weaviate local/docker collection with explicit vectors and hybrid search.
Reference: Python for Gen AI Complete Guide, Module 11, pages 130-133.
Execution: cloud.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import weaviate
from weaviate.classes.config import Configure,Property,DataType
from common import gemini_embed
with weaviate.connect_to_local() as client:
    if not client.collections.exists('Phase3Docs'):
        client.collections.create('Phase3Docs',vector_config=Configure.Vectors.self_provided(),properties=[Property(name='text',data_type=DataType.TEXT),Property(name='topic',data_type=DataType.TEXT)])
    collection=client.collections.get('Phase3Docs')
    texts=['RAG retrieves documents','Agents call software tools','Embedding models create vectors']
    for text,vec in zip(texts,gemini_embed().embed_documents(texts)):
        collection.data.insert(properties={'text':text,'topic':'genai'},vector=vec)
    print('Near vector:')
    print([x.properties for x in collection.query.near_vector(near_vector=gemini_embed().embed_query('retrieval'),limit=3).objects])
    print('Hybrid:')
    print([x.properties for x in collection.query.hybrid(query='RAG retrieval',vector=gemini_embed().embed_query('RAG retrieval'),alpha=0.5,limit=3).objects])
