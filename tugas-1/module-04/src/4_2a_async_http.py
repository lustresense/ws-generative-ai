# Module 04 — 4.2 Async/Await with httpx
import asyncio
import httpx


async def fetch_json(client: httpx.AsyncClient, url: str) -> dict:
    response = await client.get(url, timeout=3.0)
    response.raise_for_status()
    return response.json()


async def fetch_multiple(urls: list[str]) -> list[dict]:
    async with httpx.AsyncClient() as client:
        tasks = [fetch_json(client, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)
    return [r for r in results if not isinstance(r, Exception)]


async def main():
    urls = [
        f"https://jsonplaceholder.typicode.com/posts/{i}"
        for i in range(1, 4)
    ]
    posts = await fetch_multiple(urls)

    # Keeps the demo readable when an offline environment blocks the public test API.
    if not posts:
        print("Network unavailable; using local fallback records for demonstration.")
        posts = [
            {"id": 1, "title": "fallback post one"},
            {"id": 2, "title": "fallback post two"},
            {"id": 3, "title": "fallback post three"},
        ]

    for post in posts:
        print(f"Post {post['id']}: {post['title'][:40]}")


asyncio.run(main())
