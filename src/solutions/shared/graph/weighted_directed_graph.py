from collections import defaultdict
from typing import Generic, Hashable, Iterator, TypeVar

T = TypeVar("T", bound=Hashable)


class WeightedDirectedGraph(Generic[T]):
    def __init__(self) -> None:
        self._weights: defaultdict[T, dict[T, int]] = defaultdict(dict)

    def add_edge(self, u: T, v: T, weight: int) -> None:
        self._weights[u][v] = weight
        if v not in self._weights:
            self._weights[v] = dict()

    def edge_weight(self, u: T, v: T) -> int:
        return self._weights[u][v]

    def neighbors(self, node: T) -> Iterator[T]:
        return iter(self._weights[node])

    def nodes(self) -> Iterator[T]:
        yield from self._weights.keys()

    def has_edge(self, u: T, v: T) -> bool:
        return v in self._weights[u]
