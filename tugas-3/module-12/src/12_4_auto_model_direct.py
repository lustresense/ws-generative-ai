"""AutoModelForCausalLM direct generation with torch.no_grad.
Reference: Python for Gen AI Complete Guide, Module 12, pages 139.
Execution: local.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from transformers import AutoTokenizer,AutoModelForCausalLM
from common import hf_models
import torch
name=hf_models()['generator'];tok=AutoTokenizer.from_pretrained(name);model=AutoModelForCausalLM.from_pretrained(name).eval()
inputs=tok('The advantage of local language models is',return_tensors='pt')
with torch.no_grad():out=model.generate(**inputs,max_new_tokens=25,do_sample=False,pad_token_id=tok.eos_token_id)
print(tok.decode(out[0],skip_special_tokens=True))
