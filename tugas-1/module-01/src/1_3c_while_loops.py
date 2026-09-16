# Module 01 — 1.3 while loops
import time

MAX_RETRIES = 3
attempt = 0

while attempt < MAX_RETRIES:
    attempt += 1
    print(f"Attempt {attempt}")
    if attempt == 2:
        print("Success!")
        break
    time.sleep(0.1)
else:
    print("All retries failed")
