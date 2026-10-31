"""Exercise 1: 1,000 mock vectors, 100 Chroma queries, latency p95/throughput.
Reference: Python for Gen AI Complete Guide, Module 11, pages 133-134.
Execution: offline.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import time,numpy as np,chromadb
from common import mock_embed
client=chromadb.EphemeralClient();name='m11_benchmark';collection=client.get_or_create_collection(name)
texts=[f'Document number {i}, topic {i%7}' for i in range(1000)];ids=[f'id{i}' for i in range(1000)]
for start in range(0,1000,100):collection.upsert(ids=ids[start:start+100],documents=texts[start:start+100],embeddings=mock_embed(texts[start:start+100]))
lat=[];begin=time.perf_counter()
for i in range(100):
    q=f'topic {i%7}';t=time.perf_counter();collection.query(query_embeddings=mock_embed([q]),n_results=5);lat.append((time.perf_counter()-t)*1000)
elapsed=time.perf_counter()-begin
print({'documents':collection.count(),'queries':len(lat),'avg_ms':round(float(np.mean(lat)),3),'p95_ms':round(float(np.percentile(lat,95)),3),'qps':round(len(lat)/elapsed,2)})
print('NOTE: mock vectors are deterministic testing inputs, NOT semantic embeddings.')
