"""Exercise 3: NER pipeline extracts unique PERSON/ORG/LOC lists from corpus.
Reference: Python for Gen AI Complete Guide, Module 12, pages 143.
Execution: local.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from transformers import pipeline
from common import hf_models
ner=pipeline('ner',model=hf_models()['ner'],aggregation_strategy='simple',device=-1)
def extract_entities_from_corpus(texts):
    result={'PERSON':set(),'ORG':set(),'LOC':set()}
    for text in texts:
        for entity in ner(text):
            tag={'PER':'PERSON','ORG':'ORG','LOC':'LOC'}.get(entity['entity_group'])
            if tag:result[tag].add(entity['word'])
    return {k:sorted(values) for k,values in result.items()}
print(extract_entities_from_corpus(['Dario Amodei discussed Anthropic in San Francisco.','Google employees visited London.','OpenAI operates in San Francisco.']))
