"""CrewAI BaseTool with Pydantic schema for example token costs and context limits.
Reference: Python for Gen AI Complete Guide, Module 14, pages 155-156.
Execution: offline.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from crewai.tools import BaseTool
from pydantic import BaseModel,Field
from typing import Type
import json
class CostInput(BaseModel):model:str=Field(description='Model name');input_tokens:int;output_tokens:int
class CostTool(BaseTool):
    name:str='Token Cost Calculator';description:str='Calculate cost using historical PDF example prices, not current billing.'
    args_schema:Type[BaseModel]=CostInput
    def _run(self,model:str,input_tokens:int,output_tokens:int)->str:
        prices={'gpt-4o':(2.50,10.00),'gpt-4o-mini':(.15,.60)}
        if model not in prices:return json.dumps({'error':'unknown model'})
        p=prices[model];return json.dumps({'cost_usd':round((input_tokens*p[0]+output_tokens*p[1])/1e6,6),'source':'PDF historical example'})
class ContextInput(BaseModel):model:str
class ContextTool(BaseTool):
    name:str='Context Window Lookup';description:str='Returns historical example context sizes from PDF.'
    args_schema:Type[BaseModel]=ContextInput
    def _run(self,model:str)->str:return json.dumps({'model':model,'example_context':{'gpt-4o':128000,'gpt-4o-mini':128000}.get(model,'unknown')})
cost_tool=CostTool();context_tool=ContextTool()
print(cost_tool._run('gpt-4o-mini',1000,500));print(context_tool._run('gpt-4o'))
