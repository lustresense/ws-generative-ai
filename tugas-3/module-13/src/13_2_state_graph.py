"""LangGraph TypedDict state, reducers, conditional edges, iteration to final answer.
Reference: Python for Gen AI Complete Guide, Module 13, pages 144-145.
Execution: offline.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from typing import TypedDict,Annotated
import operator
from langgraph.graph import StateGraph,START,END
class AgentState(TypedDict):
    messages:Annotated[list[str],operator.add]
    step_count:int
    final_answer:str
def think_node(state:AgentState)->dict:
    return {'messages':[f"Step {state['step_count']+1}: analysing the problem"], 'step_count':state['step_count']+1}
def answer_node(state:AgentState)->dict:
    return {'final_answer':'Based on the two analysis steps, the answer is X.'}
def route(state:AgentState)->str:
    return 'think' if state['step_count']<2 else 'answer'
graph=StateGraph(AgentState)
graph.add_node('think',think_node);graph.add_node('answer',answer_node)
graph.add_edge(START,'think');graph.add_conditional_edges('think',route,{'think':'think','answer':'answer'});graph.add_edge('answer',END)
app=graph.compile();out=app.invoke({'messages':[],'step_count':0,'final_answer':''})
print('Messages:',out['messages']);print('Answer:',out['final_answer']);assert out['step_count']==2
