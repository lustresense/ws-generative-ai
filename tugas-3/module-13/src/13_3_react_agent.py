"""ReAct reasoning/tools loop with safe calculator and static module-price example.
Reference: Python for Gen AI Complete Guide, Module 13, pages 145-150.
Execution: api.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import ast,operator,json
from typing import TypedDict,Annotated
from langgraph.graph import StateGraph,START,END
from langchain_core.messages import HumanMessage,SystemMessage,ToolMessage,AIMessage
from common import chat_llm
ops={ast.Add:operator.add,ast.Sub:operator.sub,ast.Mult:operator.mul,ast.Div:operator.truediv,ast.Pow:operator.pow}
def calculator(expression:str)->str:
    def calc(node):
        if isinstance(node,ast.Expression):return calc(node.body)
        if isinstance(node,ast.Constant) and type(node.value) in (int,float):return node.value
        if isinstance(node,ast.BinOp) and type(node.op) in ops:
            a,b=calc(node.left),calc(node.right)
            if abs(a)>1e10 or abs(b)>1e10:return 'too large'
            if isinstance(node.op,ast.Pow) and abs(b)>8:return 'exponent too large'
            return ops[type(node.op)](a,b)
        raise ValueError('unsupported expression')
    try:return str(calc(ast.parse(expression,mode='eval')))
    except (SyntaxError,ValueError,ZeroDivisionError,OverflowError) as exc:return f'Error: {exc}'
def token_cost_lookup(model:str)->str:
    example={'gpt-4o':{'input':2.50,'output':10.0},'gpt-4o-mini':{'input':0.15,'output':0.60}}
    return json.dumps({'model':model,'module_example_pricing_not_current':example.get(model,'unknown')})
TOOLS={'calculator':calculator,'token_cost_lookup':token_cost_lookup}
from langchain_core.tools import tool
@tool
def calculate(expression:str)->str:
    """Calculate an arithmetic expression using safe elementary operations."""
    return calculator(expression)
@tool
def example_token_cost(model:str)->str:
    """Look up illustrative PDF pricing, not current API prices."""
    return token_cost_lookup(model)
llm=chat_llm().bind_tools([calculate,example_token_cost])
class State(TypedDict):messages:Annotated[list,operator.add]
def agent_node(state):return {'messages':[llm.invoke([SystemMessage(content='Use available tools to calculate. Costs are historical examples, not current prices.')]+state['messages'])]}
def tools_node(state):
    last=state['messages'][-1];out=[]
    for call in last.tool_calls[:4]:
        fn={'calculate':calculate,'example_token_cost':example_token_cost}.get(call['name'])
        value=fn.invoke(call['args']) if fn else 'Unknown tool'
        out.append(ToolMessage(content=str(value),tool_call_id=call['id']))
    return {'messages':out}
def route(state):return 'tools' if getattr(state['messages'][-1],'tool_calls',None) else END
g=StateGraph(State);g.add_node('agent',agent_node);g.add_node('tools',tools_node);g.add_edge(START,'agent');g.add_conditional_edges('agent',route,{'tools':'tools',END:END});g.add_edge('tools','agent')
output=g.compile().invoke({'messages':[HumanMessage(content='Calculate 10000 * (800 * 2.5 + 300 * 10) / 1000000, using the calculator tool.')]},config={'recursion_limit':12})
for message in output['messages']:
    if isinstance(message,AIMessage) and not message.tool_calls:print('Final:',message.content)
