# Module 02 — Exercise 2
def conversation_stats(messages: list[dict]) -> dict:
    total_messages = len(messages)
    user_turns = sum(1 for m in messages if m.get("role") == "user")
    assistant_turns = sum(1 for m in messages if m.get("role") == "assistant")
    total_words = sum(len(m.get("content", "").split()) for m in messages)
    avg_words = total_words / total_messages if total_messages else 0.0

    return {
        "total_messages": total_messages,
        "user_turns": user_turns,
        "assistant_turns": assistant_turns,
        "avg_words_per_message": round(avg_words, 2),
    }


messages = [
    {"role": "user", "content": "What is RAG?"},
    {"role": "assistant", "content": "RAG combines retrieval and generation."},
    {"role": "user", "content": "Give me one example."},
    {"role": "assistant", "content": "A chatbot can retrieve company documents before answering."},
]

print(conversation_stats(messages))
