# Module 02 — 2.3 Sets
retrieved_doc_ids = ["doc_3", "doc_1", "doc_3", "doc_7", "doc_1"]
unique_ids = set(retrieved_doc_ids)
print("Unique IDs:", sorted(unique_ids))

gpt4_topics = {"coding", "math", "reasoning", "vision"}
claude_topics = {"coding", "writing", "reasoning", "safety"}

both = gpt4_topics & claude_topics
either = gpt4_topics | claude_topics
gpt_only = gpt4_topics - claude_topics

print("Both:    ", sorted(both))
print("Either:  ", sorted(either))
print("GPT only:", sorted(gpt_only))
