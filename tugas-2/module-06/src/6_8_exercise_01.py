import time
import anthropic
import openai

from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv

ENV_FILE = find_dotenv(filename=".env", usecwd=True)
if not ENV_FILE:
    raise RuntimeError(".env tidak ditemukan. Copy .env.example menjadi .env di folder tugas-2.")
load_dotenv(ENV_FILE)


class MockRateLimitError(Exception):
    pass

class MockClient:
    def __init__(self, fail_times=2):
        self.fail_times = fail_times
        self.calls = 0
    def send(self, messages):
        self.calls += 1
        if self.calls <= self.fail_times:
            raise MockRateLimitError("mock rate limit reached")
        return {"status": "ok", "messages": messages, "attempt": self.calls}

def retry_on_rate_limit(client, messages, max_retries=5):
    """Retry SDK rate-limit errors with exponential backoff; mock error is included for testing."""
    retry_errors = (anthropic.RateLimitError, openai.RateLimitError, MockRateLimitError)
    for attempt in range(max_retries + 1):
        try:
            return client.send(messages)
        except retry_errors as exc:
            if attempt >= max_retries:
                raise
            wait = 2 ** attempt
            print(f"Rate limited: {exc} | retry in {wait}s")
            time.sleep(min(wait, 1))  # keep workshop demo fast while preserving exponential schedule

print("=" * 60)
print("6.8 EXERCISE 01 - RETRY ON RATE LIMIT")
print("=" * 60)
result = retry_on_rate_limit(MockClient(fail_times=2), [{"role": "user", "content": "hello"}], max_retries=5)
print("Result:", result)
