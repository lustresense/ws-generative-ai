# Module 04 — Exercise 3
import json
import os
from pathlib import Path

MODULE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = MODULE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)


def load_config(path: str, prefix: str = "APP_") -> dict:
    config = json.loads(Path(path).read_text(encoding="utf-8"))
    for key, original_value in list(config.items()):
        env_key = f"{prefix}{key.upper()}"
        if env_key in os.environ:
            raw = os.environ[env_key]
            if isinstance(original_value, bool):
                config[key] = raw.lower() in {"1", "true", "yes", "on"}
            elif isinstance(original_value, int):
                config[key] = int(raw)
            elif isinstance(original_value, float):
                config[key] = float(raw)
            else:
                config[key] = raw
    return config


config_path = DATA_DIR / "config.json"
config_path.write_text(json.dumps({
    "model": "gpt-4o",
    "temperature": 0.7,
    "max_tokens": 1024,
}, indent=2), encoding="utf-8")

os.environ["APP_TEMPERATURE"] = "0.25"
os.environ["APP_MAX_TOKENS"] = "512"

print(load_config(str(config_path)))
