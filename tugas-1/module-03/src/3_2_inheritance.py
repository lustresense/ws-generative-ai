# Module 03 — 3.2 Inheritance
from abc import ABC, abstractmethod


class BaseLLMClient(ABC):
    """Abstract base class for LLM provider clients."""

    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model

    @abstractmethod
    def complete(self, messages: list[dict], **kwargs) -> str:
        """Send messages and return the assistant's reply."""

    def count_words(self, text: str) -> int:
        return len(text.split())


class MockAnthropicClient(BaseLLMClient):
    def complete(self, messages: list[dict], **kwargs) -> str:
        last_user = next(
            m["content"] for m in reversed(messages) if m["role"] == "user"
        )
        return f"[Mock Anthropic] Echo: {last_user}"


class MockOpenAIClient(BaseLLMClient):
    def complete(self, messages: list[dict], **kwargs) -> str:
        return f"[Mock OpenAI] Received {len(messages)} messages."


clients: list[BaseLLMClient] = [
    MockAnthropicClient("key-ant", "claude-sonnet-4-5"),
    MockOpenAIClient("key-oai", "gpt-4o"),
]
msgs = [{"role": "user", "content": "Hello!"}]
for client in clients:
    print(client.complete(msgs))
