"""Hugging Face pipeline sentiment classification using a small DistilBERT model.
Reference: Python for Gen AI Complete Guide, Module 12, pages 134-135.
Execution: local.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from transformers import pipeline
from common import hf_models
p=pipeline('text-classification',model=hf_models()['classification'],device=-1)
texts=['This LLM API is very fast and easy to use.','The API documentation is confusing and slow.','The model works for basic tasks.']
for text,result in zip(texts,p(texts)):print(result['label'],round(result['score'],3),text)
