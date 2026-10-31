"""Exercise 2: compare VectorStoreIndex and SummaryIndex on 10 sections and 5 questions.
Reference: Python for Gen AI Complete Guide, Module 10, pages 124.
Execution: api.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import init_llama
from llama_index.core import Document,VectorStoreIndex,SummaryIndex
init_llama()
docs=[Document(text=f'Section {i}: '+('RAG retrieves external sources.' if i%2==0 else 'Fine-tuning changes model parameters.')) for i in range(10)]
vector=VectorStoreIndex.from_documents(docs).as_query_engine(similarity_top_k=3)
summary=SummaryIndex.from_documents(docs).as_query_engine()
for q in ['What is RAG?','What does fine-tuning do?','What is repeated across the sections?','Summarize the 10 sections.','How many sections discuss RAG?']:
    print('\nQuestion:',q); print('Vector:',str(vector.query(q))[:230]);print('Summary:',str(summary.query(q))[:230])
print('Comparison is qualitative; see both responses and judge with original sections.')
