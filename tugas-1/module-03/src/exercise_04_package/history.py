class ConversationHistory:
    def __init__(self, max_turns: int = 10, system_prompt: str = ""):
        self.max_turns = max_turns
        self.system_prompt = system_prompt
        self._messages: list[dict] = []

    def add(self, role: str, content: str) -> None:
        if role not in ("user", "assistant"):
            raise ValueError(f"Invalid role: {role}")
        self._messages.append({"role": role, "content": content})
        self._messages = self._messages[-self.max_turns * 2:]

    def __len__(self) -> int:
        return len(self._messages)

    def __repr__(self) -> str:
        return f"ConversationHistory(messages={len(self._messages)})"
