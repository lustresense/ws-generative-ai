class AnthropicClient:
    def __init__(self, model: str):
        self.model = model

    def __repr__(self) -> str:
        return f"AnthropicClient(model={self.model!r})"
