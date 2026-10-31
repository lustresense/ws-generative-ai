"""SummaryIndex synthesizes answers from all documents.
Reference: Python for Gen AI Complete Guide, Module 10, pages 120-122.
Execution: api.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import init_llama,show
from llama_index.core import Document,SummaryIndex
init_llama();docs=[Document(text=t) for t in ['Coding: models may vary in latency and accuracy.','Reasoning: benchmark results require comparable tests.','Language: prompt design affects evaluation.','Conclusion: match model choice to your task.']]
index=SummaryIndex.from_documents(docs)
show('Synthesis over full document',index.as_query_engine().query('What is the conclusion about selecting AI models?'))
