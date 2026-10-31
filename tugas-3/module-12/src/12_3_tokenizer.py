"""AutoTokenizer encode/decode, token strings, batch padding and token budget.
Reference: Python for Gen AI Complete Guide, Module 12, pages 137-138.
Execution: local.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from transformers import AutoTokenizer
from common import hf_models
tok=AutoTokenizer.from_pretrained(hf_models()['generator'])
tok.pad_token=tok.eos_token
text='Retrieval-Augmented Generation combines search with LLMs.'
ids=tok.encode(text);print('Count:',len(ids),'IDs:',ids);print('Decoded:',tok.decode(ids));print('Tokens:',tok.convert_ids_to_tokens(ids))
batch=tok(['What is RAG?','Explain vector search in detail.'],padding=True,truncation=True,max_length=64,return_tensors='pt')
print('Input shape:',tuple(batch['input_ids'].shape),'Mask:',tuple(batch['attention_mask'].shape))
print('Long prompt tokens:',len(tok.encode('Summarize: '+'word '*500)))
