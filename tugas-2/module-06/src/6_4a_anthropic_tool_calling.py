import anthropic
import json

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

tools = [{
    "name": "get_model_info",
    "description": "Returns context window size and example module pricing for a given LLM.",
    "input_schema": {
        "type": "object",
        "properties": {"model_name": {"type": "string", "description": "Model identifier."}},
        "required": ["model_name"],
    },
}]

def get_model_info(model_name: str) -> dict:
    # Example data from the module; not current provider billing data.
    db = {
        "claude-sonnet-4-5": {"context_k": 200, "cost_input": 3.00, "cost_output": 15.00},
        "gpt-4o": {"context_k": 128, "cost_input": 2.50, "cost_output": 10.00},
        "gemini-1.5-pro": {"context_k": 1000, "cost_input": 1.25, "cost_output": 5.00},
    }
    return db.get(model_name, {"error": f"Unknown model: {model_name}"})

question = "How large is the context window of claude-sonnet-4-5?"
print("=" * 60)
print("6.4A - ANTHROPIC TOOL CALLING")
print("=" * 60)
response = client.messages.create(
    model=model,
    max_tokens=1024,
    tools=tools,
    messages=[{"role": "user", "content": question}],
)

if response.stop_reason == "tool_use":
    tool_block = next(b for b in response.content if b.type == "tool_use")
    result = get_model_info(**tool_block.input)
    print(f"Tool called: {tool_block.name}({tool_block.input})")
    print(f"Tool result: {result}")
    final = client.messages.create(
        model=model,
        max_tokens=1024,
        tools=tools,
        messages=[
            {"role": "user", "content": question},
            {"role": "assistant", "content": response.content},
            {"role": "user", "content": [{"type": "tool_result", "tool_use_id": tool_block.id, "content": json.dumps(result)}]},
        ],
    )
    print("\nFinal answer:")
    print(final.content[0].text)
else:
    print("Model answered without requesting the tool:")
    print("".join(getattr(b, "text", "") for b in response.content))
