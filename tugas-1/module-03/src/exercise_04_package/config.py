from dataclasses import dataclass, field
from typing import Optional


@dataclass
class LLMConfig:
    model: str
    temperature: float = 0.7
    max_tokens: int = 1024
    stop_sequences: list[str] = field(default_factory=list)
    system_prompt: Optional[str] = None

    def __post_init__(self):
        if not 0.0 <= self.temperature <= 2.0:
            raise ValueError("temperature must be between 0 and 2")
        if self.max_tokens < 1:
            raise ValueError("max_tokens must be >= 1")
