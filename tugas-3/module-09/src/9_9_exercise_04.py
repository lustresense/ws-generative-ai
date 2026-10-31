"""Exercise 4: RAG answer plus second LLM groundedness judge 0-10.
Reference: Python for Gen AI Complete Guide, Module 09, pages 115.
Execution: api.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import chat_llm,gemini_embed,tiny_documents,show
from langchain_core.documents import Document
from langchain_chroma import Chroma
llm=chat_llm();db=Chroma.from_documents([Document(page_content=t) for _,t in tiny_documents()],gemini_embed(),collection_name='m09_quality')
question='How does RAG answer questions?';context='\n'.join(d.page_content for d in db.similarity_search(question,k=3))
answer=llm.invoke(f'Answer only from context. Context:\n{context}\nQuestion: {question}').content
score=llm.invoke(f'Score groundedness 0-10 by checking claims against context. Return number and one reason. Context:\n{context}\nAnswer:\n{answer}').content
show('Answer',answer);show('Groundedness judge (subjective)',score)
