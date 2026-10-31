# Module 12 - Source Index

Source count: 11

- `12_2a_text_classification.py` | local | PDF pages 134-135 | Hugging Face pipeline sentiment classification using a small DistilBERT model.
- `12_2b_named_entity_recognition.py` | local | PDF pages 135 | Hugging Face pipeline NER using smaller DistilBERT, PERSON/ORG/LOC.
- `12_2c_text_generation.py` | local | PDF pages 136 | Hugging Face local text-generation pipeline (DistilGPT2, CPU).
- `12_2d_summarization.py` | local | PDF pages 136-137 | Hugging Face local summarization pipeline using small Flan-T5 instead of BART-large.
- `12_3_tokenizer.py` | local | PDF pages 137-138 | AutoTokenizer encode/decode, token strings, batch padding and token budget.
- `12_4_auto_model_direct.py` | local | PDF pages 139 | AutoModelForCausalLM direct generation with torch.no_grad.
- `12_5_lora_finetuning.py` | heavy | PDF pages 140-143 | Lightweight CPU LoRA training on DistilGPT2, save/reload adapter. Training is optional/heavy.
- `12_6_exercise_01.py` | heavy | PDF pages 143 | Exercise 1: compare ten prompts using two Hugging Face text generation pipelines.
- `12_6_exercise_02.py` | local | PDF pages 143 | Exercise 2: TokenBudgetChecker filters texts exceeding a token limit.
- `12_6_exercise_03.py` | local | PDF pages 143 | Exercise 3: NER pipeline extracts unique PERSON/ORG/LOC lists from corpus.
- `12_6_exercise_04.py` | heavy | PDF pages 143 | Exercise 4: custom 20 Q&A dataset, complete LoRA loop and after-training inference.

Screenshot output should use same stem as source file with `.png` extension.