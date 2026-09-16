# Module 01 — Exercise 4
text = "128000 tokens, 0.005 USD per 1K"

parts = text.split(", ")
token_count = int(parts[0].split()[0])
cost = float(parts[1].split()[0])

print(f"Original: {text}")
print(f"Token count: {token_count} ({type(token_count).__name__})")
print(f"Cost per 1K: {cost} ({type(cost).__name__})")
