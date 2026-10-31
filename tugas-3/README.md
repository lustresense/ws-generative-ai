# Tugas 3 - Agentic AI & RAG Systems

Folder ini berisi pengumpulan Tugas 3 dari Workshop Python Gen AI, berdasarkan materi Phase 3 - Agentic AI & RAG Systems.

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
| Module 09 | LangChain Expression Language (LCEL) |
| Module 10 | LlamaIndex RAG |
| Module 11 | Vector Databases |
| Module 12 | Fine-Tuning & PEFT |
| Module 13 | LangGraph Agents |
| Module 14 | CrewAI Multi-Agent Systems |

Tugas ini mencakup **59 source Python runnable** dan **24 exercise**. File exercise ditandai dengan pola `_exercise_` pada namanya.

## Struktur Folder

```text
tugas-3/
|- README.md
|- module-09/
|  |- src/
|  |- data/
|  `- output/
|- module-10/
|  |- src/
|  |- data/
|  `- output/
|- module-11/
|  |- src/
|  |- data/
|  `- output/
|- module-12/
|  |- src/
|  |- data/
|  `- output/
|- module-13/
|  |- src/
|  |- data/
|  `- output/
`- module-14/
   |- src/
   |- data/
   `- output/
```

Setiap folder `src/` berisi source code materi dan exercise. Folder `output/` berisi screenshot hasil eksekusi terminal. Module 10-12 dan 14 juga memakai folder `data/` untuk vector store, model adapter, dan dataset latihan.

## Provider & Model

- **LLM**: 9Router OpenAI-compatible endpoint → `ag/gemini-3.8-flash-low`
- **Embeddings**: OpenAI-compatible `gemini-embedding-2` via 9Router
- **Vector DB**: ChromaDB (local), Pinecone/Weaviate (optional)
- **Frameworks**: LangChain, LlamaIndex, LangGraph, CrewAI

*Semua output di folder `output/` adalah screenshot terminal asli dari eksekusi source di VS Code.*