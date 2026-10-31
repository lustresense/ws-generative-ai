"""Pydantic schema with structured output; JSON fallback if provider rejects schema.
Reference: Python for Gen AI Complete Guide, Module 09, pages 108-109.
Execution: api.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import json
from typing import List
from pydantic import BaseModel,Field
from common import chat_llm,show
from langchain_core.prompts import ChatPromptTemplate
class ModelComparison(BaseModel):
    models:List[str]=Field(description='Model names')
    best_for_cost:str
    best_for_quality:str
    recommendation:str
llm=chat_llm()
question='Compare GPT-4o and Claude Sonnet for budget and code. Do not invent benchmark numbers.'
try:
    result=llm.with_structured_output(ModelComparison).invoke(question)
except Exception as exc:
    print(f'[NOTE] Router does not support native structured output: {type(exc).__name__}; using prompt-based JSON fallback.')
    raw=llm.invoke('Return a JSON object with models (array), best_for_cost, best_for_quality, recommendation (strings). '+question+' Output only JSON.').content
    result=ModelComparison.model_validate_json(str(raw).removeprefix('```json').removesuffix('```').strip())
show('Pydantic',result.model_dump_json(indent=2))
