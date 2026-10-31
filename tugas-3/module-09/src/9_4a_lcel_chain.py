"""LCEL prompt | model | StrOutputParser.
Reference: Python for Gen AI Complete Guide, Module 09, pages 104-105.
Execution: api.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import chat_llm,show
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
prompt=ChatPromptTemplate.from_messages([('system','Summarise in exactly {sentences} short sentences.'),('human','{text}')])
chain=prompt | chat_llm() | StrOutputParser()
show('LCEL',chain.invoke({'sentences':2,'text':'LangChain composes LLM calls, prompts, and parsers. Its LCEL syntax makes multi-step workflows easier to read.'}))
