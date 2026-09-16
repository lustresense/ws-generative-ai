# Module 04 — Exercise 2
import asyncio
import time
import httpx


async def fetch_status(client: httpx.AsyncClient, url: str) -> tuple[str, int, float]:
    start = time.perf_counter()
    try:
        response = await client.get(url, timeout=3.0)
        status = response.status_code
    except Exception:
        status = -1
    elapsed_ms = (time.perf_counter() - start) * 1000
    return url, status, elapsed_ms


async def compare_endpoints(urls: list[str]) -> list[tuple[str, int, float]]:
    async with httpx.AsyncClient() as client:
        return list(await asyncio.gather(*(fetch_status(client, url) for url in urls)))


urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
]

for url, status_code, response_time_ms in asyncio.run(compare_endpoints(urls)):
    label = status_code if status_code != -1 else "network unavailable"
    print(f"{url} | status={label} | {response_time_ms:.1f} ms")
