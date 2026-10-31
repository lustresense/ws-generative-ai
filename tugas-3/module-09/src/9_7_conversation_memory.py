"""RunnableWithMessageHistory stores messages per session ID.
Reference: Python for Gen AI Complete Guide, Module 09, pages 110-112.
Execution: api.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import chat_llm,show
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
store={}
def history(session):return store.setdefault(session,InMemoryChatMessageHistory())
prompt=ChatPromptTemplate.from_messages([('system','Be a concise tutor.'),MessagesPlaceholder('history'),('human','{input}')])
chain=RunnableWithMessageHistory(prompt | chat_llm() | StrOutputParser(),history,input_messages_key='input',history_messages_key='history')
config={'configurable':{'session_id':'lesson-demo'}}
for q in ['What does RAG stand for?', 'What topic did I just ask about?']:
    show('Conversation',chain.invoke({'input':q},config=config))
print('Stored messages:',len(history('lesson-demo').messages))
