from typing import Callable, Hashable, Iterator, TypeVar

T = TypeVar("T", bound=Hashable)


def dfs(start_node: T, neighbors: Callable[[T], Iterator[T]]) -> Iterator[T]:
    visited: set[T] = set()
    stack: list[T] = [start_node]

    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        yield current
        for neighbor in neighbors(current):
            if neighbor not in visited:
                stack.append(neighbor)
