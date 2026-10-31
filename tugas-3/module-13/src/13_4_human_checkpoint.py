"""Checkpoint with interrupt_before to wait for human approval and resume safely.
Reference: Python for Gen AI Complete Guide, Module 13, pages 150-152.
Execution: offline.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from typing import TypedDict,Annotated
import operator
from langgraph.graph import StateGraph,START,END
from langgraph.checkpoint.memory import MemorySaver
class ReviewState(TypedDict):
    plan:str; approved:bool; result:str; messages:Annotated[list[str],operator.add]
def plan_node(state):return {'plan':'1. Query index. 2. Summarise. 3. Present.','messages':['Plan prepared']}
def execute_node(state):
    return {'result':'Pipeline executed successfully' if state['approved'] else 'Execution skipped, not approved', 'messages':['Execution gate checked']}
graph=StateGraph(ReviewState);graph.add_node('plan',plan_node);graph.add_node('execute',execute_node)
graph.add_edge(START,'plan');graph.add_edge('plan','execute');graph.add_edge('execute',END)
app=graph.compile(checkpointer=MemorySaver(),interrupt_before=['execute'])
config={'configurable':{'thread_id':'phase3-checkpoint-demo'}}
state=app.invoke({'plan':'','approved':False,'result':'','messages':[]},config=config)
print('Paused plan:',state['plan']);print('Waiting for approval...')
# Workshop simulation: update persisted state rather than re-submitting input from START.
app.update_state(config,{'approved':True})
final=app.invoke(None,config=config)
print('Approved:',final['approved'],'Result:',final['result']);assert final['approved']
