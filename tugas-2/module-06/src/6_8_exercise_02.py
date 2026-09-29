class BudgetExceeded(RuntimeError):
    pass

class TokenBudgetManager:
    def __init__(self, limit: int):
        self.limit = limit
        self.used = 0

    @property
    def remaining(self) -> int:
        return max(0, self.limit - self.used)

    def record(self, input_tokens: int, output_tokens: int) -> None:
        new_total = self.used + input_tokens + output_tokens
        if new_total > self.limit:
            raise BudgetExceeded(
                f"Budget {self.limit} tokens exceeded: attempted cumulative usage {new_total}."
            )
        self.used = new_total

print("=" * 60)
print("6.8 EXERCISE 02 - TOKEN BUDGET MANAGER")
print("=" * 60)
manager = TokenBudgetManager(limit=1000)
for i, usage in enumerate([(200, 100), (250, 150), (120, 80)], start=1):
    manager.record(*usage)
    print(f"Call {i}: used={manager.used}, remaining={manager.remaining}")
try:
    manager.record(200, 100)
except BudgetExceeded as exc:
    print("BudgetExceeded:", exc)
