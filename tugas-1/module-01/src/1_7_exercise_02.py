# Module 01 — Exercise 2
import functools
import time


def retry(n: int = 3, sleep_seconds: float = 0.1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(1, n + 1):
                try:
                    print(f"Attempt {attempt}")
                    return func(*args, **kwargs)
                except Exception as error:
                    last_error = error
                    print(f"Failed: {error}")
                    if attempt < n:
                        time.sleep(sleep_seconds)
            raise last_error
        return wrapper
    return decorator


state = {"calls": 0}


@retry(n=4, sleep_seconds=0.05)
def unstable_function() -> str:
    state["calls"] += 1
    if state["calls"] <= 2:
        raise RuntimeError("Simulated failure")
    return "Success on third call"


print(unstable_function())
