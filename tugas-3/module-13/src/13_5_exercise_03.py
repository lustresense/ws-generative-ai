"""Exercise 3: PlanAndExecute graph with planner LLM, executor and step index.
Reference: Python for Gen AI Complete Guide, Module 13, pages 152.
Execution: api.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import json,re
from typing import TypedDict
from langgraph.graph import StateGraph,START,END
from common import chat_llm
class State(TypedDict):topic:str;plan:list[str];index:int;results:list[str]
def planner(s):
    raw=str(chat_llm().invoke('Give exactly 3 short numbered steps to explain '+s['topic']+'. Return one per line.').content)
    steps=[re.sub(r'^\s*\d+[.)]\s*','',x.strip()) for x in raw.splitlines() if x.strip()][:3]
    if not steps:raise ValueError('Planner output contains no steps')
    return {'plan':steps,'index':0}
def executor(s):
    step=s['plan'][s['index']];return {'results':s['results']+[f"Completed step {s['index']+1}: {step}"], 'index':s['index']+1}
def route(s):return 'execute' if s['index']<len(s['plan']) else END
g=StateGraph(State);g.add_node('planner',planner);g.add_node('execute',executor);g.add_edge(START,'planner');g.add_edge('planner','execute');g.add_conditional_edges('execute',route,{'execute':'execute',END:END})
r=g.compile().invoke({'topic':'RAG','plan':[],'index':0,'results':[]},config={'recursion_limit':15})
print('Plan:',r['plan']);print('Completed:',r['results']);assert r['index']==len(r['plan'])
