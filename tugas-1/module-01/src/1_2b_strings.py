# Module 01 — 1.2 Strings
user_input = "Explain transformers in simple terms"
system_prompt = "You are a helpful AI tutor."

full_prompt = f"System: {system_prompt}\nUser: {user_input}"
print(full_prompt)

print(user_input.upper())
print(user_input.split())
print(user_input.replace("simple", "plain"))
print(len(user_input))

prompt = """
You are an expert data scientist.
Answer concisely in bullet points.
"""
print(prompt.strip())
