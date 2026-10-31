"""LangChain RAG chain with Chroma vector store, Gemini embeddings and 9Router chat.
Reference: Python for Gen AI Complete Guide, Module 09, pages 112-114.
Execution: api.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import chat_llm,gemini_embed,show,tiny_documents
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
docs=[Document(page_content=text,metadata={'source':title}) for title,text in tiny_documents()]
vdb=Chroma.from_documents(docs,embedding=gemini_embed(),collection_name='m09_rag_demo')
retriever=vdb.as_retriever(search_kwargs={'k':3})
def format_docs(items):return '\n'.join(f'[{d.metadata["source"]}] {d.page_content}' for d in items)
prompt=ChatPromptTemplate.from_messages([('system','Answer using ONLY context. If missing, say unknown.\nContext:\n{context}'),('human','{question}')])
chain=({'context':retriever|format_docs,'question':RunnablePassthrough()}|prompt|chat_llm()|StrOutputParser())
for question in ('How does RAG work?','What is France capital?'):
    show(question,chain.invoke(question))
