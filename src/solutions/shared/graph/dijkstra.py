from dataclasses import dataclass, field
from queue import PriorityQueue
from typing import Callable, Generic, Hashable, Iterator, TypeVar

T = TypeVar("T", bound=Hashable)


@dataclass(frozen=True, order=True)
class _PriorityQueueItem(Generic[T]):
    priority: int
    item: T = field(compare=False)


def min_path_length_with_dijkstra(
    start_node: T,
    is_final_state: Callable[[T], bool],
    weighted_neighbors: Callable[[T], Iterator[tuple[T, int]]],
) -> int:
    distances: dict[T, int] = dict()
    queue = PriorityQueue()
    queue.put(_PriorityQueueItem(priority=0, item=start_node))
    while not queue.empty():
        current = queue.get()
        if current.item in distances:
            continue
        elif is_final_state(current.item):
            return current.priority
        else:
            distances[current.item] = current.priority
            for neighbor, weight in weighted_neighbors(current.item):
                if neighbor not in distances:
                    queue.put(
                        _PriorityQueueItem(
                            priority=current.priority + weight, item=neighbor
                        )
                    )

    raise ValueError("No path found")
