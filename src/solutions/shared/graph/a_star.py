from dataclasses import dataclass, field
from queue import PriorityQueue
from typing import Callable, Generic, Hashable, Iterator, TypeVar

T = TypeVar("T", bound=Hashable)


@dataclass(frozen=True, order=True)
class _PriorityQueueItem(Generic[T]):
    f_score: int
    g_score: int
    item: T = field(compare=False)


def min_path_length_with_a_star(
    start_node: T,
    is_final_state: Callable[[T], bool],
    weighted_neighbors: Callable[[T], Iterator[tuple[T, int]]],
    heuristic: Callable[[T], int],
) -> int:
    best_g_score: dict[T, int] = {start_node: 0}
    queue = PriorityQueue()
    queue.put(
        _PriorityQueueItem(
            f_score=heuristic(start_node),
            g_score=0,
            item=start_node,
        )
    )

    while not queue.empty():
        current = queue.get()
        if current.g_score > best_g_score.get(current.item, float("inf")):
            continue
        if is_final_state(current.item):
            return current.g_score

        for neighbor, weight in weighted_neighbors(current.item):
            tentative_g_score = current.g_score + weight
            if tentative_g_score >= best_g_score.get(neighbor, float("inf")):
                continue

            best_g_score[neighbor] = tentative_g_score
            queue.put(
                _PriorityQueueItem(
                    f_score=tentative_g_score + heuristic(neighbor),
                    g_score=tentative_g_score,
                    item=neighbor,
                )
            )

    raise ValueError("No path found")
