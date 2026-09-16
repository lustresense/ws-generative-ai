# Module 01 — 1.2 Variables and Data Types
model_name: str = "claude-sonnet-4-5"
temperature: float = 0.7
max_tokens: int = 1024
is_streaming: bool = True

print(type(model_name))
print(type(temperature))
print(type(max_tokens))
print(type(is_streaming))

response = None
print(response is None)
