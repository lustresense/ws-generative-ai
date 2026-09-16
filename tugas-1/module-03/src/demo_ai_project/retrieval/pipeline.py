from .chunker import chunk_text
from .embedder import embed_texts


def run_pipeline(text: str) -> list[list[float]]:
    return embed_texts(chunk_text(text))
