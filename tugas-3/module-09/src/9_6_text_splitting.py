"""Documents and RecursiveCharacterTextSplitter with overlap.
Reference: Python for Gen AI Complete Guide, Module 09, pages 109-110.
Execution: offline.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
docs=[Document(page_content=('LangChain composes prompts, models and tools. '*7),metadata={'source':'guide1'}), Document(page_content=('RAG retrieves documents and gives them to an LLM for grounded answers. '*5),metadata={'source':'guide2'})]
splitter=RecursiveCharacterTextSplitter(chunk_size=150,chunk_overlap=25)
chunks=splitter.split_documents(docs)
for i,c in enumerate(chunks): print(f'{i}: {len(c.page_content)} chars | {c.metadata} | {c.page_content[:65]}')
