from collections import deque
from dataclasses import dataclass
from typing import Callable, Generic, Hashable, Iterator, TypeVar

T = TypeVar("T", bound=Hashable)


@dataclass(frozen=True)
class ExploredNode(Generic[T]):
    node: T
    distance_to_start: int


def bfs(
    start_node: T, neighbors: Callable[[T], Iterator[T]]
) -> Iterator[ExploredNode[T]]:
    visited: set[T] = set()
    start = ExploredNode(start_node, 0)
    queue = deque([start])

    while queue:
        current = queue.popleft()
        if current.node in visited:
            continue
        visited.add(current.node)
        yield current
        for neighbor in neighbors(current.node):
            if neighbor not in visited:
                queue.append(
                    ExploredNode(neighbor, current.distance_to_start + 1)
                )


def min_path_length_with_bfs(
    start_node: T,
    is_final_state: Callable[[T], bool],
    neighbors: Callable[[T], Iterator[T]],
) -> int:
    for explored in bfs(start_node, neighbors):
        if is_final_state(explored.node):
            return explored.distance_to_start
    raise ValueError("No path found")
