"""Exercise 2: manual MultiQueryRetriever, three LLM paraphrases and SHA256 dedup.
Reference: Python for Gen AI Complete Guide, Module 09, pages 115.
Execution: api.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import hashlib
from common import chat_llm,gemini_embed,tiny_documents,show
from langchain_core.documents import Document
from langchain_chroma import Chroma
llm=chat_llm();docs=[Document(page_content=t,metadata={'source':k}) for k,t in tiny_documents()]
store=Chroma.from_documents(docs,gemini_embed(),collection_name='m09_multiquery')
question='How does external knowledge improve LLM answers?'
raw=llm.invoke('Write exactly 3 paraphrased search queries, one per line, no numbering: '+question).content
queries=[q.strip(' 0123456789.-') for q in str(raw).splitlines() if q.strip()][:3]
while len(queries)<3:queries.append(question)
unique={}
for q in queries:
    for d in store.similarity_search(q,k=3): unique[hashlib.sha256(d.page_content.encode()).hexdigest()]=d
print('Queries:',queries)
for d in unique.values(): show(d.metadata['source'],d.page_content,200)
