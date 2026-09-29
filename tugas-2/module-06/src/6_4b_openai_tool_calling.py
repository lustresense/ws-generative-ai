from openai import OpenAI
import json

from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv

ENV_FILE = find_dotenv(filename=".env", usecwd=True)
if not ENV_FILE:
    raise RuntimeError(".env tidak ditemukan. Copy .env.example menjadi .env di folder tugas-2.")
load_dotenv(ENV_FILE)


client = OpenAI(
    api_key=os.environ["NINEROUTER_API_KEY"],
    base_url=os.environ["NINEROUTER_BASE_URL"].rstrip("/") + "/v1",
)
model = os.getenv("OPENAI_MODEL", "cx/gpt-5.6-luna")

tools = [{
    "type": "function",
    "function": {
        "name": "get_model_info",
        "description": "Returns context window and example module pricing for a given LLM.",
        "parameters": {
            "type": "object",
            "properties": {"model_name": {"type": "string", "description": "Model identifier."}},
            "required": ["model_name"],
        },
    },
}]

def get_model_info(model_name: str) -> dict:
    db = {
        "gpt-4o": {"context_k": 128, "cost_input": 2.50},
        "claude-sonnet-4-5": {"context_k": 200, "cost_input": 3.00},
    }
    return db.get(model_name, {"error": "unknown model"})

messages = [{"role": "user", "content": "What is gpt-4o's context window?"}]
print("=" * 60)
print("6.4B - OPENAI TOOL CALLING")
print("=" * 60)
response = client.chat.completions.create(model=model, tools=tools, messages=messages)
choice = response.choices[0]
if choice.finish_reason == "tool_calls" and choice.message.tool_calls:
    tool_call = choice.message.tool_calls[0]
    args = json.loads(tool_call.function.arguments)
    result = get_model_info(**args)
    print(f"Tool called: {tool_call.function.name}({args})")
    print(f"Tool result: {result}")
    messages.append(choice.message)
    messages.append({"role": "tool", "tool_call_id": tool_call.id, "content": json.dumps(result)})
    final = client.chat.completions.create(model=model, messages=messages)
    print("\nFinal answer:")
    print(final.choices[0].message.content)
else:
    print("Model answered without requesting the tool:")
    print(choice.message.content)
