"""Exercise 3: map-reduce document summarization with multiple chunks.
Reference: Python for Gen AI Complete Guide, Module 09, pages 115.
Execution: api.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import chat_llm,show
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
text=('RAG performs indexing, retrieval and generation. Good chunking improves retrieval quality. Metadata filtering restricts results. '+ 'A reranker can improve ordering of candidate documents. ')*14
chunks=RecursiveCharacterTextSplitter(chunk_size=380,chunk_overlap=35).split_text(text)
llm=chat_llm(); map_chain=ChatPromptTemplate.from_messages([('human','Summarise key facts in one sentence: {text}')])|llm|StrOutputParser()
summaries=[map_chain.invoke({'text':chunk}) for chunk in chunks]
reduce_chain=ChatPromptTemplate.from_messages([('human','Combine these short summaries in 3 sentences, no new facts: {text}')])|llm|StrOutputParser()
print('Chunks:',len(chunks));show('Map-reduce final',reduce_chain.invoke({'text':'\n'.join(summaries)}))
