# Module 01 — 1.3 if / elif / else
def classify_response_length(token_count: int) -> str:
    if token_count < 100:
        return "short"
    elif token_count < 500:
        return "medium"
    elif token_count < 2000:
        return "long"
    else:
        return "very long"

print(classify_response_length(80))
print(classify_response_length(350))
print(classify_response_length(3000))
