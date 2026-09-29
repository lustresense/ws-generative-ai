from dataclasses import dataclass, asdict
from string import Formatter
from pathlib import Path
import json

@dataclass
class PromptTemplate:
    name: str
    system: str
    user: str
    version: str = "1.0"

class PromptLibrary:
    def __init__(self):
        self.templates: dict[str, PromptTemplate] = {}
        self.last_eval_version: dict[str, str] = {}

    def add(self, template: PromptTemplate):
        self.templates[template.name] = template

    def mark_evaluated(self, name: str):
        self.last_eval_version[name] = self.templates[name].version

    def save(self, path: str):
        payload = {
            "templates": {k: asdict(v) for k, v in self.templates.items()},
            "last_eval_version": self.last_eval_version,
        }
        Path(path).write_text(json.dumps(payload, indent=2), encoding="utf-8")

    @classmethod
    def load(cls, path: str):
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        lib = cls()
        lib.templates = {k: PromptTemplate(**v) for k, v in data["templates"].items()}
        lib.last_eval_version = data.get("last_eval_version", {})
        return lib

print("=" * 60)
print("7.8 EXERCISE 02 - PROMPT LIBRARY")
print("=" * 60)
lib = PromptLibrary()
lib.add(PromptTemplate("qa", "You are a {domain} expert.", "Question: {question}", "1.2"))
lib.add(PromptTemplate("summary", "You summarize technical text.", "Summarize: {document}", "1.0"))
lib.mark_evaluated("qa")
out = Path(__file__).resolve().parents[1] / "data" / "prompt_library.json"
lib.save(str(out))
loaded = PromptLibrary.load(str(out))
print("Saved:", out)
print("Templates:", sorted(loaded.templates))
print("Last evaluated versions:", loaded.last_eval_version)
