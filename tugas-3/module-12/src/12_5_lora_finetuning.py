"""Lightweight CPU LoRA training on DistilGPT2, save/reload adapter. Training is optional/heavy.
Reference: Python for Gen AI Complete Guide, Module 12, pages 140-143.
Execution: heavy.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import os,torch
from transformers import AutoTokenizer,AutoModelForCausalLM,Trainer,TrainingArguments,default_data_collator
from peft import LoraConfig,TaskType,get_peft_model,PeftModel
from datasets import Dataset
from common import hf_models,ROOT
name=hf_models()['generator'];folder=ROOT/'module-12'/'data';folder.mkdir(exist_ok=True)
tok=AutoTokenizer.from_pretrained(name);tok.pad_token=tok.eos_token
base=AutoModelForCausalLM.from_pretrained(name)
config=LoraConfig(task_type=TaskType.CAUSAL_LM,r=4,lora_alpha=8,target_modules=['c_attn'],lora_dropout=0.05,bias='none')
model=get_peft_model(base,config);model.print_trainable_parameters()
examples=['Question: What is RAG? Answer: Retrieval augmented generation finds useful documents.','Question: What is an embedding? Answer: An embedding is a numeric vector for meaning.','Question: What is fine tuning? Answer: Fine tuning updates model weights.','Question: What is a vector database? Answer: A vector database indexes numeric vectors.']
encoded=tok(examples,padding='max_length',truncation=True,max_length=64)
labels=[]
for row,mask in zip(encoded['input_ids'],encoded['attention_mask']):labels.append([x if m else -100 for x,m in zip(row,mask)])
encoded['labels']=labels;data=Dataset.from_dict(encoded)
args=TrainingArguments(output_dir=str(folder/'lora_train'),max_steps=int(os.getenv('HF_TRAIN_STEPS','5')),per_device_train_batch_size=1,
    gradient_accumulation_steps=1,learning_rate=2e-4,logging_steps=1,save_strategy='no',report_to='none',fp16=False,disable_tqdm=True,dataloader_num_workers=0)
trainer=Trainer(model=model,args=args,train_dataset=data,data_collator=default_data_collator)
trainer.train();path=folder/'lora_adapter';model.save_pretrained(path);tok.save_pretrained(path)
print('LoRA adapter saved:',path)
del model,trainer,base
loaded=PeftModel.from_pretrained(AutoModelForCausalLM.from_pretrained(name),str(path)).eval()
inputs=tok('Question: What is RAG? Answer:',return_tensors='pt')
with torch.no_grad():output=loaded.generate(**inputs,max_new_tokens=15,do_sample=False,pad_token_id=tok.eos_token_id)
print('Inference:',tok.decode(output[0],skip_special_tokens=True))
print('NOTE: 5 steps with 4 examples does NOT guarantee factual learning, this validates training+adapter mechanism.')
