"""Exercise 1: compare ten prompts using two Hugging Face text generation pipelines.
Reference: Python for Gen AI Complete Guide, Module 12, pages 143.
Execution: heavy.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import time,statistics
from transformers import pipeline
from common import hf_models
class ModelBenchmark:
    def __init__(self,models):self.models=models
    def run(self,prompts):
        for model in self.models:
            pipe=pipeline('text-generation',model=model,device=-1)
            lat=[];lengths=[]
            for prompt in prompts:
                t=time.perf_counter();text=pipe(prompt,max_new_tokens=12,do_sample=False,pad_token_id=pipe.tokenizer.eos_token_id)[0]['generated_text']
                lat.append((time.perf_counter()-t)*1000);lengths.append(len(text))
            print(f'{model:35s} avg_ms={statistics.mean(lat):.1f} avg_chars={statistics.mean(lengths):.1f} n={len(prompts)}')
ModelBenchmark([hf_models()['generator'],'sshleifer/tiny-gpt2']).run([f'Artificial intelligence is useful for topic {i} because' for i in range(10)])
print('NOTE: tiny-gpt2 is for speed/testing, not useful language quality.')
