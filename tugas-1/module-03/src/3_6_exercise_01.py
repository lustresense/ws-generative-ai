# Module 03 — Exercise 1
import time
from collections import deque


class RateLimiter:
    def __init__(self, max_calls_per_minute: int, period_seconds: float = 60.0):
        if max_calls_per_minute <= 0:
            raise ValueError("max_calls_per_minute must be > 0")
        self.max_calls = max_calls_per_minute
        self.period_seconds = period_seconds
        self.calls = deque()

    def check_and_wait(self) -> None:
        now = time.monotonic()
        while self.calls and now - self.calls[0] >= self.period_seconds:
            self.calls.popleft()

        if len(self.calls) >= self.max_calls:
            wait = self.period_seconds - (now - self.calls[0])
            print(f"Rate limit reached. Waiting {wait:.2f}s")
            time.sleep(max(wait, 0))
            now = time.monotonic()
            while self.calls and now - self.calls[0] >= self.period_seconds:
                self.calls.popleft()

        self.calls.append(time.monotonic())


# Short test window keeps the demonstration quick while using the same algorithm.
limiter = RateLimiter(max_calls_per_minute=3, period_seconds=0.30)
for i in range(5):
    limiter.check_and_wait()
    print(f"Call {i + 1} allowed")
