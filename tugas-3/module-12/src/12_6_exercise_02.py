"""Exercise 2: TokenBudgetChecker filters texts exceeding a token limit.
Reference: Python for Gen AI Complete Guide, Module 12, pages 143.
Execution: local.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from transformers import AutoTokenizer
from common import hf_models
class TokenBudgetChecker:
    def __init__(self,model,max_tokens):self.tok=AutoTokenizer.from_pretrained(model);self.max=max_tokens
    def filter(self,texts):return [(text,len(self.tok.encode(text))) for text in texts if len(self.tok.encode(text))<=self.max]
checker=TokenBudgetChecker(hf_models()['generator'],40)
print(checker.filter(['What is RAG?','Explain retrieval.','word '*80]))
