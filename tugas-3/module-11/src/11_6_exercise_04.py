"""Exercise 4: export and import Chroma collection with vectors to JSON.
Reference: Python for Gen AI Complete Guide, Module 11, pages 134.
Execution: offline.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import json,chromadb
from common import ROOT,mock_embed
c=chromadb.EphemeralClient();col=c.get_or_create_collection('m11_original');texts=['RAG basics','Embeddings and search']
col.upsert(ids=['a','b'],documents=texts,embeddings=mock_embed(texts),metadatas=[{'topic':'rag'},{'topic':'vector'}])
raw=col.get(include=['documents','embeddings','metadatas'])
rows=[{'id':ident,'text':txt,'embedding':vec.tolist(),'metadata':meta} for ident,txt,vec,meta in zip(raw['ids'],raw['documents'],raw['embeddings'],raw['metadatas'])]
path=ROOT/'module-11'/'data'/'backup_export.json';path.write_text(json.dumps(rows,indent=2),encoding='utf-8')
restore=c.get_or_create_collection('m11_restored');loaded=json.loads(path.read_text(encoding='utf-8'))
restore.upsert(ids=[r['id'] for r in loaded],documents=[r['text'] for r in loaded],embeddings=[r['embedding'] for r in loaded],metadatas=[r['metadata'] for r in loaded])
print('Original:',col.count(),'Restored:',restore.count(),'Backup:',path)
assert col.count()==restore.count()
