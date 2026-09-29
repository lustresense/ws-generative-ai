from abc import ABC, abstractmethod
from dataclasses import dataclass
import anthropic
from openai import OpenAI

from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv

ENV_FILE = find_dotenv(filename=".env", usecwd=True)
if not ENV_FILE:
    raise RuntimeError(".env tidak ditemukan. Copy .env.example menjadi .env di folder tugas-2.")
load_dotenv(ENV_FILE)


@dataclass
class ChatMessage:
    role: str
    content: str

@dataclass
class ChatResponse:
    text: str
    input_tokens: int
    output_tokens: int
    model: str

class BaseLLMClient(ABC):
    @abstractmethod
    def chat(self, messages: list[ChatMessage], system: str = "", max_tokens: int = 1024, temperature: float = 0.7) -> ChatResponse:
        raise NotImplementedError

class AnthropicClient(BaseLLMClient):
    def __init__(self, model: str | None = None):
        self.model = model or os.getenv("ANTHROPIC_MODEL", "ag/claude-sonnet-4-6")
        self._client = anthropic.Anthropic(
            api_key=os.environ["NINEROUTER_API_KEY"],
            base_url=os.environ["NINEROUTER_BASE_URL"].rstrip("/"),
        )

    def chat(self, messages, system="", max_tokens=1024, temperature=0.7) -> ChatResponse:
        kwargs = dict(
            model=self.model,
            max_tokens=max_tokens,
            messages=[{"role": m.role, "content": m.content} for m in messages],
            # temperature removed because modern anthropic sdk / 9router handles defaults
        )
        if system:
            kwargs["system"] = system
        resp = self._client.messages.create(**kwargs)
        return ChatResponse(resp.content[0].text, resp.usage.input_tokens, resp.usage.output_tokens, self.model)

class OpenAIClient(BaseLLMClient):
    def __init__(self, model: str | None = None):
        self.model = model or os.getenv("OPENAI_MODEL", "cx/gpt-5.6-luna")
        self._client = OpenAI(
            api_key=os.environ["NINEROUTER_API_KEY"],
            base_url=os.environ["NINEROUTER_BASE_URL"].rstrip("/") + "/v1",
        )

    def chat(self, messages, system="", max_tokens=1024, temperature=0.7) -> ChatResponse:
        api_messages = []
        if system:
            api_messages.append({"role": "system", "content": system})
        api_messages += [{"role": m.role, "content": m.content} for m in messages]
        resp = self._client.chat.completions.create(
            model=self.model,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=api_messages,
        )
        usage = resp.usage
        return ChatResponse(
            resp.choices[0].message.content or "",
            usage.prompt_tokens if usage else 0,
            usage.completion_tokens if usage else 0,
            self.model,
        )

print("=" * 60)
print("6.7 - PROVIDER-AGNOSTIC CLIENT")
print("=" * 60)
msgs = [ChatMessage(role="user", content="What is a vector database? Answer in one paragraph.")]
for name, client in [("Anthropic SDK", AnthropicClient()), ("OpenAI SDK", OpenAIClient())]:
    result = client.chat(msgs, system="Be concise.", max_tokens=300)
    print(f"\n[{name} | {result.model}]")
    print(result.text)
    print(f"Tokens: {result.input_tokens} in / {result.output_tokens} out")
