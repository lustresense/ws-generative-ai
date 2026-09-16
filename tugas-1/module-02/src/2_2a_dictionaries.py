# Module 02 — 2.2 Dictionaries
payload = {
    "model": "claude-sonnet-4-5",
    "max_tokens": 1024,
    "temperature": 0.7,
    "messages": [
        {"role": "user", "content": "What is attention in transformers?"}
    ],
}

print(payload["model"])
print(payload.get("top_p", 1.0))

payload["temperature"] = 0.3
payload.update({"stream": True, "top_k": 40})

for key, value in payload.items():
    if not isinstance(value, list):
        print(f"{key}: {value}")

print("stream" in payload)
print("top_p" in payload)
