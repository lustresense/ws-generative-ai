class OpenAIClient:
    def __init__(self, model: str):
        self.model = model

    def __repr__(self) -> str:
        return f"OpenAIClient(model={self.model!r})"
