# Module 04 — Exercise 4
import csv
import threading
from datetime import datetime, timezone
from pathlib import Path

MODULE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = MODULE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)


class CSVLogWriter:
    fieldnames = [
        "timestamp", "model", "input_tokens", "output_tokens", "latency_ms"
    ]

    def __init__(self, path: str):
        self.path = Path(path)
        self.lock = threading.Lock()

    def append(self, model: str, input_tokens: int, output_tokens: int, latency_ms: float) -> None:
        with self.lock:
            new_file = not self.path.exists() or self.path.stat().st_size == 0
            with self.path.open("a", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                if new_file:
                    writer.writeheader()
                writer.writerow({
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "model": model,
                    "input_tokens": input_tokens,
                    "output_tokens": output_tokens,
                    "latency_ms": round(latency_ms, 2),
                })


log_path = DATA_DIR / "llm_calls.csv"
if log_path.exists():
    log_path.unlink()
logger = CSVLogWriter(str(log_path))

rows = [
    ("gpt-4o", 120, 70, 410.4),
    ("claude-sonnet-4-5", 140, 80, 380.2),
    ("gemini-1.5-pro", 100, 65, 450.8),
]
threads = [threading.Thread(target=logger.append, args=row) for row in rows]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print(log_path.read_text(encoding="utf-8"))
