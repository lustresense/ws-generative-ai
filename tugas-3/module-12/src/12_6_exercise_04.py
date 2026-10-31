"""Exercise 4: custom 20 Q&A dataset, complete LoRA loop and after-training inference.
Reference: Python for Gen AI Complete Guide, Module 12, pages 143.
Execution: heavy.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import os,torch
from transformers import AutoModelForCausalLM,AutoTokenizer,Trainer,TrainingArguments,default_data_collator
from peft import LoraConfig,TaskType,get_peft_model,PeftModel
from datasets import Dataset
from common import hf_models,ROOT
model_name=hf_models()['generator'];base=AutoModelForCausalLM.from_pretrained(model_name);tok=AutoTokenizer.from_pretrained(model_name);tok.pad_token=tok.eos_token
pairs=[('RAG','retrieval augmented generation'),('embedding','numeric representation of meaning'),('token','unit of text'),('vector store','storage for embeddings'),('LangChain','chain framework'),('LlamaIndex','document indexing framework'),('LangGraph','stateful graph framework'),('CrewAI','multi agent framework'),('LoRA','low rank adapter'),('fine-tuning','additional model training'),('inference','using model to predict'),('retrieval','finding relevant documents'),('context window','token capacity'),('metadata','attributes of a record'),('cosine similarity','direction comparison'),('prompt','model instruction'),('temperature','sampling randomness'),('classifier','model predicting labels'),('NER','named entity recognition'),('checkpoint','saved progress')]
texts=[f'Question: Define {q}. Answer: {a}.' for q,a in pairs]
enc=tok(texts,padding='max_length',truncation=True,max_length=48);enc['labels']=[[x if mask else -100 for x,mask in zip(row,masks)] for row,masks in zip(enc['input_ids'],enc['attention_mask'])]
model=get_peft_model(base,LoraConfig(task_type=TaskType.CAUSAL_LM,r=4,lora_alpha=8,target_modules=['c_attn'],bias='none'))
folder=ROOT/'module-12'/'data';args=TrainingArguments(output_dir=str(folder/'exercise04_train'),max_steps=int(os.getenv('HF_TRAIN_STEPS','5')),per_device_train_batch_size=2,report_to='none',save_strategy='no',disable_tqdm=True,fp16=False)
Trainer(model=model,args=args,train_dataset=Dataset.from_dict(enc),data_collator=default_data_collator).train()
path=folder/'exercise04_adapter';model.save_pretrained(path);tok.save_pretrained(path)
print('Training pairs:',len(pairs),'Saved adapter:',path)
del model,base
inference=PeftModel.from_pretrained(AutoModelForCausalLM.from_pretrained(model_name),str(path)).eval()
for prompt in ('Question: Define RAG. Answer:','Question: Define LoRA. Answer:'):
    with torch.no_grad():generated=inference.generate(**tok(prompt,return_tensors='pt'),max_new_tokens=12,do_sample=False,pad_token_id=tok.eos_token_id)
    print(tok.decode(generated[0],skip_special_tokens=True))
print('Verification: code confirms inference can load the adapter; answer accuracy needs independent evaluation and more training.')
