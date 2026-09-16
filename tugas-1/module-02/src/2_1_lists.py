# Module 02 — 2.1 Lists
conversation = []
conversation.append({"role": "user", "content": "Hello"})
conversation.append({"role": "assistant", "content": "Hi! How can I help?"})
conversation.append({"role": "user", "content": "Explain RAG."})

print(len(conversation))
print(conversation[0])
print(conversation[-1])
print(conversation[1:3])

scores = [0.91, 0.76, 0.88, 0.65, 0.95]
scores.sort(reverse=True)
print(scores)
print(max(scores), min(scores))

scores.remove(0.76)
popped = scores.pop()
print(popped, scores)
