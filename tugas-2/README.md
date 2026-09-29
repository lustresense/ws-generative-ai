# Tugas 2 - LLM APIs & Prompting

Folder ini berisi pengumpulan Tugas 2 dari Workshop Python Gen AI, berdasarkan materi Phase 2 - LLM APIs & Prompting pada [Modul Python Gen AI.pdf](../Modul%20Python%20Gen%20AI.pdf).

## Identitas

| Data | Keterangan |
|---|---|
| Nama | FARCHAN DEANO MUHAMMAD |
| NRP | 5323600012 |
| Program Studi | Teknologi Rekayasa Multimedia |
| Institusi | Politeknik Elektronika Negeri Surabaya (PENS) |

## Cakupan Tugas

| Modul | Materi |
|---|---|
| Module 06 | OpenAI & Anthropic APIs |
| Module 07 | Prompt Engineering |
| Module 08 | Embeddings & Semantic Search |

Tugas ini mencakup 39 source Python runnable dan 12 exercise. File exercise ditandai dengan pola `_exercise_` pada namanya.

Implementasi provider dan model:
- OpenAI Python SDK → 9Router OpenAI-compatible API (`cx/gpt-5.6-luna` / `ag/gemini-3.8-flash-high`)
- Anthropic Python SDK → 9Router Anthropic-compatible API (`ag/claude-sonnet-4-6`)
- OpenAI Python SDK → Gemini OpenAI-compatible embeddings (`gemini-embedding-2`)
- Voyage AI SDK → Voyage embeddings (`voyage-4-lite`)

## Struktur Folder

```text
tugas-2/
|- README.md
|- requirements.txt
|- .env.example
|- preflight.py
|- RUN_TUGAS_2.bat
|- RUN_ONE_BY_ONE.bat
|- RUN_ONE_BY_ONE.md
|- run_tugas_2.py
|- run_one_by_one.py
|- auto_run_capture.py
|- module-06/
|  |- src/
|  `- output/
|- module-07/
|  |- src/
|  |- data/
|  `- output/
`- module-08/
   |- src/
   |- data/
   `- output/
```

Setiap folder `src/` berisi source code materi dan exercise. Folder `output/` berisi screenshot hasil eksekusi terminal. Module 07 dan Module 08 juga memakai folder `data/` untuk prompt library, cache SQLite, dan file evaluasi.

## Menjalankan Source

Jalankan dari root repository:

```powershell
python ./tugas-2/module-06/src/6_1_print_env_config.py
```

Atau masuk ke folder source module terkait lalu jalankan file Python-nya:

```powershell
cd ./tugas-2/module-06/src
python .\6_2a_anthropic_basic_message.py
```

Atau jalankan runner otomatis / one-by-one:

```powershell
.\tugas-2\RUN_TUGAS_2.bat
# atau
.\tugas-2\RUN_ONE_BY_ONE.bat
```
