# Module 04 — 4.1 Text Files with pathlib
import pathlib

MODULE_DIR = pathlib.Path(__file__).resolve().parents[1]
data_dir = MODULE_DIR / "data"
data_dir.mkdir(exist_ok=True)

template = """You are a {role}.
Answer the following question concisely.
Question: {question}"""

template_file = data_dir / "qa_prompt.txt"
template_file.write_text(template, encoding="utf-8")

loaded = template_file.read_text(encoding="utf-8")
filled = loaded.format(role="Python tutor", question="What is a generator?")
print(filled)

for f in data_dir.glob("*.txt"):
    print(f.name, f.stat().st_size, "bytes")
