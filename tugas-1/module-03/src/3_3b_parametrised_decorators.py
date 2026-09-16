# Module 03 — 3.3 Parametrised Decorators
import functools
import random
import time


def retry(max_attempts: int = 3, delay: float = 0.1):
    """Parametrised retry decorator."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(1, max_attempts + 1):
                try:
                    print(f"Attempt {attempt}")
                    return func(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    print(f"Failed: {e}")
                    if attempt < max_attempts:
                        time.sleep(delay)
            raise last_error
        return wrapper
    return decorator


random.seed(3)


@retry(max_attempts=3, delay=0.05)
def flaky_api_call(prompt: str) -> str:
    if random.random() < 0.6:
        raise ConnectionError("Simulated network error")
    return f"Response to: {prompt}"


try:
    print(flaky_api_call("What is RAG?"))
except ConnectionError as error:
    print(f"Final failure: {error}")
