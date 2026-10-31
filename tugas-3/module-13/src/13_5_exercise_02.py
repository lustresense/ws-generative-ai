"""Exercise 2: max-8-tool-call limiter on a ReAct-style graph.
Reference: Python for Gen AI Complete Guide, Module 13, pages 152.
Execution: offline.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from typing import TypedDict
from langgraph.graph import StateGraph,START,END
class State(TypedDict):calls:int;final:str;history:list[str]
def agent(s):return {'history':s['history']+[f"Agent step after {s['calls']} calls"]}
def tool(s):return {'calls':s['calls']+1,'history':s['history']+['Mock calculator called']}
def route(s):return 'limit' if s['calls']>=8 else 'tool'
def limit(s):return {'final':'Reached step limit'}
g=StateGraph(State)
for n,f in [('agent',agent),('tool',tool),('limit',limit)]:g.add_node(n,f)
g.add_edge(START,'agent');g.add_conditional_edges('agent',route,{'limit':'limit','tool':'tool'});g.add_edge('tool','agent');g.add_edge('limit',END)
out=g.compile().invoke({'calls':0,'final':'','history':[]},config={'recursion_limit':25})
print('Calls:',out['calls'],'Answer:',out['final']);assert out['calls']==8 and out['final']=='Reached step limit'
print('Tool calls are intentionally mocked to deterministically test the limit.')
