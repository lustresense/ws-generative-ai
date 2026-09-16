# Module 05 — Exercise 3
from pathlib import Path
import re
import pandas as pd

MODULE_DIR = Path(__file__).resolve().parents[1]
TEXT_DIR = MODULE_DIR / "data" / "text_corpus"
TEXT_DIR.mkdir(parents=True, exist_ok=True)

samples = {
    "rag.txt": "RAG retrieves relevant documents. It then gives the context to a language model.",
    "embeddings.txt": "Embeddings represent text as vectors. Similar meanings can be close in vector space. Cosine similarity compares them.",
    "python.txt": "Python is widely used for AI because its ecosystem is large.",
    "agents.txt": "Agents can reason, call tools, observe results, and continue toward a goal.",
}
for filename, text in samples.items():
    (TEXT_DIR / filename).write_text(text, encoding="utf-8")


def analyse_text_folder(folder: str) -> pd.DataFrame:
    rows = []
    for path in Path(folder).glob("*.txt"):
        text = path.read_text(encoding="utf-8")
        sentences = [s for s in re.split(r"[.!?]+", text) if s.strip()]
        rows.append({
            "filename": path.name,
            "char_count": len(text),
            "word_count": len(text.split()),
            "sentence_count": len(sentences),
        })
    return pd.DataFrame(rows).sort_values("word_count", ascending=False).reset_index(drop=True)


print(analyse_text_folder(str(TEXT_DIR)).to_string(index=False))
