# Workshop Python Gen-AI — Tugas 1

Repository ini berisi implementasi source code dan exercises dari **Module 01–05 (Phase 1 — Python Core for AI)** pada modul *Python for Gen AI Complete Guide*.

## Identitas

| Data | Keterangan |
|---|---|
| Nama | FARCHAN DEANO MUHAMMAD |
| NRP | 5323600012 |
| Program Studi | Teknologi Rekayasa Multimedia |
| Institusi | Politeknik Elektronika Negeri Surabaya (PENS) |

## Cakupan Tugas

| Modul | Materi | Halaman modul |
|---|---|---:|
| Module 01 | Python Foundations | 10–18 |
| Module 02 | Data Structures & Comprehensions | 18–25 |
| Module 03 | OOP & Modules | 26–33 |
| Module 04 | File I/O & APIs | 34–40 |
| Module 05 | Python for Data | 40–48 |

Semua contoh source code runnable pada rentang tersebut dibuat sebagai file `.py`. Bagian exercise tetap dikerjakan dan diberi penanda `_exercise_` pada nama file.

Total yang disiapkan:

- **59 runnable source files / percobaan**.
- **20 exercise files** di dalam 59 source tersebut.
- **59 screenshot output**, satu untuk setiap runnable source.

## Struktur Repository

```text
workshop-python-genai/
├── README.md
├── SETUP_GUIDE.md
├── requirements.txt
├── .gitignore
├── .env.example
└── tugas-1/
    ├── module-01/
    │   ├── src/
    │   └── output/
    ├── module-02/
    │   ├── src/
    │   └── output/
    ├── module-03/
    │   ├── src/
    │   └── output/
    ├── module-04/
    │   ├── src/
    │   ├── data/
    │   └── output/
    └── module-05/
        ├── src/
        ├── data/
        └── output/
```

Module 03 juga memiliki beberapa package helper di dalam `src/` untuk mempraktikkan bagian **Modules and Packages** dan exercise package structure.

## Aturan Penamaan

Source materi:

```text
src/4_2b_simulated_llm_calls.py
output/4_2b_simulated_llm_calls.png
```

Exercise:

```text
src/4_4_exercise_03.py
output/4_4_exercise_03.png
```

Dengan pola ini, source dan screenshot output dapat dicocokkan langsung dari nama file.

## Menjalankan Project

Lihat panduan lengkap di [`SETUP_GUIDE.md`](./SETUP_GUIDE.md).

Versi singkat:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Contoh menjalankan source:

```powershell
python ./tugas-1/module-01/src/1_2a_variables_data_types.py
```

## Catatan Keamanan

File `.env` sudah masuk `.gitignore`. Jangan memasukkan API key asli ke source code atau repository GitHub. Gunakan `.env.example` sebagai template jika diperlukan.
