"""Exercise 4: MemorySaver thread_id remembers facts across invocations.
Reference: Python for Gen AI Complete Guide, Module 13, pages 152.
Execution: api.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from typing import Annotated,TypedDict
import operator
from langgraph.graph import StateGraph,START,END
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage,AIMessage
from common import chat_llm
class State(TypedDict):messages:Annotated[list,operator.add]
def chat(s):return {'messages':[AIMessage(content=str(chat_llm().invoke(s['messages']).content))]}
g=StateGraph(State);g.add_node('chat',chat);g.add_edge(START,'chat');g.add_edge('chat',END)
app=g.compile(checkpointer=MemorySaver());config={'configurable':{'thread_id':'phase3-history'}}
first=app.invoke({'messages':[HumanMessage(content='Remember this: My demo project is called VectorGarden.')]},config=config)
second=app.invoke({'messages':[HumanMessage(content='What is the name of my demo project?')]},config=config)
print('First:',first['messages'][-1].content);print('Second:',second['messages'][-1].content)
print('Stored messages:',len(second['messages']));assert len(second['messages'])>=4
