import argparse
import anthropic

from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv

ENV_FILE = find_dotenv(filename=".env", usecwd=True)
if not ENV_FILE:
    raise RuntimeError(".env tidak ditemukan. Copy .env.example menjadi .env di folder tugas-2.")
load_dotenv(ENV_FILE)


client = anthropic.Anthropic(
    api_key=os.environ["NINEROUTER_API_KEY"],
    base_url=os.environ["NINEROUTER_BASE_URL"].rstrip("/"),
)
model = os.getenv("ANTHROPIC_MODEL", "ag/claude-sonnet-4-6")

def ask(history, system, user_input):
    history.append({"role": "user", "content": user_input})
    response = client.messages.create(
        model=model, max_tokens=1024, system=system, messages=history
    )
    assistant_text = response.content[0].text
    history.append({"role": "assistant", "content": assistant_text})
    return assistant_text

def chat(system: str) -> None:
    history = []
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("exit", "quit"):
            break
        print(f"Claude: {ask(history, system, user_input)}\n")

def demo(system: str) -> None:
    history = []
    prompts = [
        "What is a Python list comprehension?",
        "Give me one short example based on your previous explanation.",
    ]
    for prompt in prompts:
        print(f"You: {prompt}")
        print(f"Claude: {ask(history, system, prompt)}\n")
    print(f"Conversation messages stored: {len(history)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    print("=" * 60)
    print("6.2C - ANTHROPIC MULTI-TURN CONVERSATION")
    print("=" * 60)
    system = "You are a helpful Python tutor. Be concise."
    demo(system) if args.demo else chat(system)
