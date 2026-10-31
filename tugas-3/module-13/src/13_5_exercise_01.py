"""Exercise 1: LangGraph researcher using mock web search, LLM summary, saved note.
Reference: Python for Gen AI Complete Guide, Module 13, pages 152.
Execution: api.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from typing import TypedDict,Annotated
import operator
from langgraph.graph import StateGraph,START,END
from common import chat_llm
NOTES=[]
def web_search(query):return ['RAG retrieves external documents at query time.','Chunking affects retrieval relevance.','Evaluation checks whether retrieved documents are relevant.']
def summarize(text):return str(chat_llm().invoke('Summarize these findings in two sentences without new claims:\n'+text).content)
def save_note(content):NOTES.append({'topic':'RAG','summary':content});return len(NOTES)
class State(TypedDict):topic:str;findings:list[str];summary:str;saved:bool
def search_node(s):return {'findings':web_search(s['topic'])}
def summary_node(s):return {'summary':summarize(' '.join(s['findings']))}
def save_node(s):save_note(s['summary']);return {'saved':True}
g=StateGraph(State)
for name,fn in [('web_search',search_node),('summarize',summary_node),('save_note',save_node)]:g.add_node(name,fn)
g.add_edge(START,'web_search');g.add_edge('web_search','summarize');g.add_edge('summarize','save_note');g.add_edge('save_note',END)
result=g.compile().invoke({'topic':'RAG','findings':[],'summary':'','saved':False})
print('Tool findings:',result['findings']);print('Saved notes:',NOTES);assert result['saved']
print('Search tool is MOCK, not live web research.')
