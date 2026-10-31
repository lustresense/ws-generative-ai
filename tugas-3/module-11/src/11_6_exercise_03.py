"""Exercise 3: tenant-isolated Chroma collections with safe stable tenant IDs.
Reference: Python for Gen AI Complete Guide, Module 11, pages 134.
Execution: offline.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import hashlib,chromadb
from common import mock_embed
class TenantVectorStore:
    def __init__(self):self.client=chromadb.EphemeralClient()
    def collection(self,tenant):
        if not tenant:raise ValueError('tenant cannot be empty')
        name='tenant_'+hashlib.sha256(tenant.encode()).hexdigest()[:24]
        return self.client.get_or_create_collection(name)
    def add(self,tenant,ident,text):self.collection(tenant).upsert(ids=[ident],documents=[text],embeddings=mock_embed([text]))
    def search(self,tenant,query):
        col=self.collection(tenant)
        if col.count()==0:return []
        return col.query(query_embeddings=mock_embed([query]),n_results=5)['documents'][0]
store=TenantVectorStore();store.add('alice','a1','Confidential Alice AI notes');store.add('bob','b1','Confidential Bob AI notes')
print('Alice:',store.search('alice','AI'));print('Bob:',store.search('bob','AI'))
