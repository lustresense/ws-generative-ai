import anthropic
import json
from dataclasses import dataclass

from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv

ENV_FILE = find_dotenv(filename=".env", usecwd=True)
if not ENV_FILE:
    raise RuntimeError(".env tidak ditemukan. Copy .env.example menjadi .env di folder tugas-2.")
load_dotenv(ENV_FILE)


client = anthropic.Anthropic(api_key=os.environ["NINEROUTER_API_KEY"], base_url=os.environ["NINEROUTER_BASE_URL"].rstrip("/"))
model = os.getenv("ANTHROPIC_MODEL", "ag/claude-sonnet-4-6")

@dataclass
class EvalCase:
    input_text: str
    expected_keywords: list[str]
    must_be_json: bool = False

def evaluate_prompt(system: str, cases: list[EvalCase]) -> dict:
    results = []
    for case in cases:
        resp = client.messages.create(model=model, max_tokens=256, system=system, messages=[{"role": "user", "content": case.input_text}])
        text = resp.content[0].text.strip()
        keyword_hit = any(kw.lower() in text.lower() for kw in case.expected_keywords)
        json_valid = True
        if case.must_be_json:
            try: json.loads(text)
            except json.JSONDecodeError: json_valid = False
        passed = keyword_hit and json_valid
        results.append({"input": case.input_text[:60], "passed": passed, "response_preview": text[:80]})
    pass_rate = sum(r["passed"] for r in results) / len(results)
    return {"pass_rate": pass_rate, "results": results}

CLASSIFY_SYSTEM = """Classify the AI task as one of: CLASSIFICATION, GENERATION, RETRIEVAL, EMBEDDING.
Return ONLY the category word."""
test_cases = [
    EvalCase("Predict whether an email is spam.", ["CLASSIFICATION"]),
    EvalCase("Write a product description for headphones.", ["GENERATION"]),
    EvalCase("Find the most relevant documents for a query.", ["RETRIEVAL"]),
    EvalCase("Convert this sentence to a vector.", ["EMBEDDING"]),
    EvalCase("Label customer reviews as positive or negative.", ["CLASSIFICATION"]),
]

print("=" * 60)
print("7.7 - PROMPT EVALUATION")
print("=" * 60)
report = evaluate_prompt(CLASSIFY_SYSTEM, test_cases)
print(f"Pass rate: {report['pass_rate']:.0%}")
for r in report["results"]:
    status = "PASS" if r["passed"] else "FAIL"
    print(f" [{status}] {r['input']!r} -> {r['response_preview']!r}")
