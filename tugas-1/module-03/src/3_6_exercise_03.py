# Module 03 — Exercise 3
import functools
import time


def retry(max_attempts: int = 3, delay: float = 0.1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(1, max_attempts + 1):
                try:
                    print(f"Attempt {attempt}")
                    return func(*args, **kwargs)
                except Exception as error:
                    last_error = error
                    if attempt < max_attempts:
                        time.sleep(delay)
            raise last_error
        return wrapper
    return decorator


state = {"count": 0}


@retry(max_attempts=3, delay=0.1)
def test_function():
    state["count"] += 1
    if state["count"] <= 2:
        raise RuntimeError("Fails on the first two calls")
    return "Succeeded on attempt 3"


print(test_function())
