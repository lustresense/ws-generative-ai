# Module 04 — Exercise 1
import json
from pathlib import Path

MODULE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = MODULE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)


def save_conversation(history: list[dict], path: str) -> None:
    Path(path).write_text(json.dumps(history, indent=2), encoding="utf-8")


def load_conversation(path: str) -> list[dict]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


history = [
    {"role": "user", "content": "What is RAG?"},
    {"role": "assistant", "content": "RAG combines retrieval and generation."},
]
path = DATA_DIR / "conversation.json"
save_conversation(history, str(path))
loaded = load_conversation(str(path))

print(f"Saved {len(history)} messages to {path.name}")
print("Loaded:", loaded)
