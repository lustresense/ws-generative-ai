"""RunnableLambda routes requests to a coding or explanatory prompt.
Reference: Python for Gen AI Complete Guide, Module 09, pages 106-107.
Execution: api.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import chat_llm,show
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
llm=chat_llm();parser=StrOutputParser()
code=ChatPromptTemplate.from_messages([('system','Respond with a very short Python code example.'),('human','{input}')])|llm|parser
prose=ChatPromptTemplate.from_messages([('system','Explain clearly in 2 sentences.'),('human','{input}')])|llm|parser
def route(x):
    return code.invoke(x) if any(word in x['input'].lower() for word in ('write','implement','function','code')) else prose.invoke(x)
router=RunnableLambda(route)
for text in ('Write a function to add numbers.','What is a transformer?'):
    show(text,router.invoke({'input':text}))
