# Module 03 — Exercise 4
from exercise_04_package import ConversationHistory, LLMConfig

history = ConversationHistory(max_turns=2, system_prompt="Be concise.")
history.add("user", "What is RAG?")
history.add("assistant", "RAG combines retrieval and generation.")

config = LLMConfig(model="gpt-4o", temperature=0.3, max_tokens=512)

print(history)
print(f"Messages: {len(history)}")
print(config)
print("Package exports work correctly.")
