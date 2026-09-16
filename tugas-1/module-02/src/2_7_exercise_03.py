# Module 02 — Exercise 3
from collections.abc import Iterable, Iterator
from typing import TypeVar

T = TypeVar("T")


def batch_items(items: Iterable[T], batch_size: int) -> Iterator[list[T]]:
    if batch_size <= 0:
        raise ValueError("batch_size must be greater than 0")

    batch: list[T] = []
    for item in items:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch


for batch in batch_items(range(1, 11), 4):
    print(batch)
