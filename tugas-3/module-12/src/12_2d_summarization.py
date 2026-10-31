"""Hugging Face local summarization pipeline using small Flan-T5 instead of BART-large.
Reference: Python for Gen AI Complete Guide, Module 12, pages 136-137.
Execution: local.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from transformers import pipeline
from common import hf_models
model=hf_models()['summary'];summarizer=pipeline('summarization',model=model,device=-1)
article=('Large language models can generate text and help developers build applications. '
         'Retrieval-augmented generation finds external documents and places their content in the prompt. '
         'This lets the model refer to facts from a knowledge base. '
         'Fine-tuning changes model weights using a specialized dataset. '
         'Developers choose RAG when external knowledge changes often and use fine-tuning for model behavior adaptations.')
print('Summary:',summarizer('summarize: '+article,max_new_tokens=45,do_sample=False)[0]['summary_text'])
print('Small-model result may be imperfect; verify against source article.')
