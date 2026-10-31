"""Persist LlamaIndex to disk and load it without reindexing.
Reference: Python for Gen AI Complete Guide, Module 10, pages 122-123.
Execution: api.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import init_llama,ROOT,show
from llama_index.core import VectorStoreIndex,Document,StorageContext,load_index_from_storage
init_llama();folder=ROOT/'module-10'/'data'/'llama_index_store';folder.mkdir(parents=True,exist_ok=True)
index=VectorStoreIndex.from_documents([Document(text='LlamaIndex saves indexes and source documents to local persistent storage.')]);index.storage_context.persist(persist_dir=str(folder))
loaded=load_index_from_storage(StorageContext.from_defaults(persist_dir=str(folder)))
show('After reload',loaded.as_query_engine().query('What is persistent storage for?'))
print('Directory:',folder)
