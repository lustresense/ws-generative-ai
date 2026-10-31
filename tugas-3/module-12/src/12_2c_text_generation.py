"""Hugging Face local text-generation pipeline (DistilGPT2, CPU).
Reference: Python for Gen AI Complete Guide, Module 12, pages 136.
Execution: local.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from transformers import pipeline
from common import hf_models
model=hf_models()['generator'];generator=pipeline('text-generation',model=model,device=-1)
for i,result in enumerate(generator('The future of AI agents is',max_new_tokens=24,num_return_sequences=2,do_sample=True,temperature=0.8,pad_token_id=generator.tokenizer.eos_token_id),1):
    print(i,result['generated_text'])
print('Model:',model,'NOTE: DistilGPT2 is completion-only, not an instruction-tuned chat model.')
