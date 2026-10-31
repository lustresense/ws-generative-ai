"""LangChain ChatOpenAI vs ChatAnthropic, invoke/stream/batch.
Reference: Python for Gen AI Complete Guide, Module 09, pages 101-103.
Execution: api.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import chat_llm, anthropic_llm, show
from langchain_core.messages import SystemMessage, HumanMessage
messages=[SystemMessage(content='Answer briefly.'),HumanMessage(content='What is LCEL?')]
for label, factory in [('OpenAI-compatible',chat_llm),('Anthropic-compatible',anthropic_llm)]:
    llm=factory(); show(label+' invoke',llm.invoke(messages).content)
print('\nSTREAM:')
for part in chat_llm().stream('Name 3 GenAI library categories, briefly.'):
    print(part.content,end='',flush=True)
print()
for answer in chat_llm().batch(['Define RAG in one sentence.','Define embedding in one sentence.'],config={'max_concurrency':2}):
    show('Batch',answer.content,250)
