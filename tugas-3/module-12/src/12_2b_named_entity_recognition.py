"""Hugging Face pipeline NER using smaller DistilBERT, PERSON/ORG/LOC.
Reference: Python for Gen AI Complete Guide, Module 12, pages 135.
Execution: local.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from transformers import pipeline
from common import hf_models
ner=pipeline('ner',model=hf_models()['ner'],aggregation_strategy='simple',device=-1)
for ent in ner('OpenAI was founded in San Francisco. Sam Altman spoke in California.'):
    print(ent['word'],ent['entity_group'],round(ent['score'],3))
