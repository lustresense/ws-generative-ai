"""RunnableParallel produces summary and keywords from the same input.
Reference: Python for Gen AI Complete Guide, Module 09, pages 105-106.
Execution: api.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import chat_llm,show
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
llm=chat_llm();parser=StrOutputParser()
def chain(instruction):return ChatPromptTemplate.from_messages([('system',instruction),('human','{text}')]) | llm | parser
both=RunnableParallel(summary=chain('Summarise in one sentence.'),keywords=chain('Return exactly 3 comma-separated keywords.'))
show('Parallel',both.invoke({'text':'RAG retrieves external documents and adds them to an LLM prompt so answers are grounded.'}))
