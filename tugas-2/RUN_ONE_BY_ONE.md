# Run One-by-One Tugas 2 (VS Code Terminal)

Panduan ini untuk dijalankan langsung di terminal VS Code agar tampilan prompt `(.venv) PS ...>` dan output running terlihat alami seperti pengerjaan manual (bisa langsung di-screenshot per kelompok script dengan `Win + Shift + S`).

---

## 0. Persiapan di Terminal VS Code

Pastikan terminal berada di root project dan `.venv` aktif:

```powershell
cd 'E:\College\Sem 7 - Gen AI'
.\.venv\Scripts\Activate.ps1
```

---

## MODULE 06 — OpenAI & Anthropic APIs

### Bagian 1: Basic & Streaming (6.1 – 6.3)
Masuk ke folder `module-06/src` lalu copy-paste blok ini:

```powershell
cd 'E:\College\Sem 7 - Gen AI\tugas-2\module-06\src'

python .\6_1_print_env_config.py
python .\6_2a_anthropic_basic_message.py
python .\6_2b_anthropic_system_prompt.py
python .\6_2c_anthropic_multiturn.py --demo
python .\6_2d_anthropic_streaming.py
python .\6_3a_openai_basic_message.py
python .\6_3b_openai_streaming.py
```
> *(Setelah selesai running, crop terminal dengan `Win + Shift + S`)*

---

### Bagian 2: Tool Calling, Vision & Client Abstraction (6.4 – 6.7)
Copy-paste blok ini:

```powershell
python .\6_4a_anthropic_tool_calling.py
python .\6_4b_openai_tool_calling.py
python .\6_5_vision_inputs.py
python .\6_6_token_management.py
python .\6_7_provider_agnostic_client.py
```
> *(Setelah selesai running, crop terminal dengan `Win + Shift + S`)*

---

### Bagian 3: Exercises (6.8 Exercise 01 – 04)
Copy-paste blok ini:

```powershell
python .\6_8_exercise_01.py
python .\6_8_exercise_02.py
python .\6_8_exercise_03.py
python .\6_8_exercise_04.py
```
> *(Setelah selesai running, crop terminal dengan `Win + Shift + S`)*

---

## MODULE 07 — Prompt Engineering

### Bagian 1: Techniques & Formatting (7.2 – 7.5)
Masuk ke folder `module-07/src` lalu copy-paste blok ini:

```powershell
cd 'E:\College\Sem 7 - Gen AI\tugas-2\module-07\src'

python .\7_2_system_prompts.py
python .\7_3_few_shot_prompting.py
python .\7_4a_chain_of_thought.py
python .\7_4b_structured_cot_xml.py
python .\7_5a_prompt_enforced_json.py
python .\7_5b_openai_json_mode.py
```
> *(Setelah selesai running, crop terminal dengan `Win + Shift + S`)*

---

### Bagian 2: Templates & Evaluation (7.6 – 7.7)
Copy-paste blok ini:

```powershell
python .\7_6_prompt_template.py
python .\7_7_prompt_evaluation.py
```
> *(Setelah selesai running, crop terminal dengan `Win + Shift + S`)*

---

### Bagian 3: Exercises (7.8 Exercise 01 – 04)
Copy-paste blok ini:

```powershell
python .\7_8_exercise_01.py
python .\7_8_exercise_02.py
python .\7_8_exercise_03.py
python .\7_8_exercise_04.py
```
> *(Setelah selesai running, crop terminal dengan `Win + Shift + S`)*

---

## MODULE 08 — Embeddings & Semantic Search

### Bagian 1: Embeddings & Similarity (8.2 – 8.4)
Masuk ke folder `module-08/src` lalu copy-paste blok ini:

```powershell
cd 'E:\College\Sem 7 - Gen AI\tugas-2\module-08\src'

python .\8_2a_openai_embeddings.py
python .\8_2b_voyage_embeddings.py
python .\8_3_cosine_similarity.py
python .\8_4_semantic_search_vector_store.py
```
> *(Setelah selesai running, crop terminal dengan `Win + Shift + S`)*

---

### Bagian 2: Chunking, Evaluation & Filtering (8.5 – 8.7)
Copy-paste blok ini:

```powershell
python .\8_5_sentence_chunking.py
python .\8_6_retrieval_evaluation.py
python .\8_7_metadata_filtering.py
```
> *(Setelah selesai running, crop terminal dengan `Win + Shift + S`)*

---

### Bagian 3: Exercises (8.8 Exercise 01 – 04)
Copy-paste blok ini:

```powershell
python .\8_8_exercise_01.py
python .\8_8_exercise_02.py
python .\8_8_exercise_03.py
python .\8_8_exercise_04.py
```
> *(Setelah selesai running, crop terminal dengan `Win + Shift + S`)*
