"""Exercise 1: two LLM calls, extract three facts then three quiz questions.
Reference: Python for Gen AI Complete Guide, Module 09, pages 115.
Execution: api.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import json
from common import chat_llm,show
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
llm=chat_llm()
facts=ChatPromptTemplate.from_messages([('system','Extract exactly 3 numbered factual statements, one per line. No preamble.'),('human','{text}')])|llm|StrOutputParser()
quiz=ChatPromptTemplate.from_messages([('system','Create exactly 3 quiz questions from these facts. Return ONLY a JSON array of 3 strings.'),('human','{facts}')])|llm|StrOutputParser()
raw=quiz.invoke({'facts':facts.invoke({'text':'RAG retrieves relevant documents. Embeddings represent text as vectors. Vector stores rank similar documents.'})})
try: questions=json.loads(raw.strip().removeprefix('```json').removesuffix('```').strip())
except json.JSONDecodeError: questions=[line.lstrip('123. -') for line in raw.splitlines() if line.strip()]
show('Questions',questions)
