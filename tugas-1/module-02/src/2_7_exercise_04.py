# Module 02 — Exercise 4
fast_models = ["gpt-4o-mini", "gemini-flash", "claude-haiku", "llama-3"]
cheap_models = ["gemini-flash", "claude-haiku", "mistral-small", "gpt-4o-mini"]

both_fast_and_cheap = set(fast_models) & set(cheap_models)
print("Fast models:", fast_models)
print("Cheap models:", cheap_models)
print("Both fast and cheap:", sorted(both_fast_and_cheap))
