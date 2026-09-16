def embed_texts(texts: list[str]) -> list[list[float]]:
    return [[float(len(text)), float(len(text.split()))] for text in texts]
