# Module 01 — 1.2 Numbers
import math

tokens_used = 450
tokens_limit = 1024
remaining = tokens_limit - tokens_used

cost_per_token = 0.000003
total_cost = tokens_used * cost_per_token
print(f"Remaining tokens: {remaining}")
print(f"Cost: ${total_cost:.6f}")

batches = tokens_used // 100
leftover = tokens_used % 100
print(f"Batches: {batches}")
print(f"Leftover: {leftover}")

print(math.log2(512))
print(math.ceil(3.1))
print(1_000_000)
