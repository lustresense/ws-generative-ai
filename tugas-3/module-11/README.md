# Module 11 - Source Index

Source count: 8

**Run default:** ChromaDB lokal dan exercise. `11_3_pinecone_optional.py` hanya jika pengguna ingin Pinecone free tier. `11_4_weaviate_optional.py` tetap sebagai referensi materi, tetapi **tidak perlu diinstal, diuji, atau dijalankan**. Tidak butuh Docker.

- `11_2a_chroma_persistent.py` | api | PDF pages 125-127 | ChromaDB persistent client with explicitly generated Gemini embeddings.
- `11_2b_chroma_filter_update_delete.py` | api | PDF pages 127-128 | Chroma metadata filtering and explicit embedding update/delete.
- `11_3_pinecone_optional.py` | cloud | PDF pages 128-130 | Pinecone external serverless index + upsert + query. Requires opt-in/API key.
- `11_4_weaviate_optional.py` | cloud | PDF pages 130-133 | Weaviate local/docker collection with explicit vectors and hybrid search.
- `11_6_exercise_01.py` | offline | PDF pages 133-134 | Exercise 1: 1,000 mock vectors, 100 Chroma queries, latency p95/throughput.
- `11_6_exercise_02.py` | offline | PDF pages 134 | Exercise 2: MultiCollectionSearch merges Chroma scores across collections.
- `11_6_exercise_03.py` | offline | PDF pages 134 | Exercise 3: tenant-isolated Chroma collections with safe stable tenant IDs.
- `11_6_exercise_04.py` | offline | PDF pages 134 | Exercise 4: export and import Chroma collection with vectors to JSON.

Screenshot output should use same stem as source file with `.png` extension.