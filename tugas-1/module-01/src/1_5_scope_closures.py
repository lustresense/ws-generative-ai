# Module 01 — 1.5 Scope and Closures
API_KEY = "sk-test-xxx"


def get_client():
    base_url = "https://api.anthropic.com"
    return f"Client({base_url}, key={API_KEY[:6]}...)"

print(get_client())


def make_counter(start: int = 0):
    count = [start]

    def increment():
        count[0] += 1
        return count[0]

    return increment


token_counter = make_counter()
print(token_counter())
print(token_counter())
print(token_counter())
