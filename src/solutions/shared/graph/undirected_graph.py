from collections import defaultdict
from typing import Generic, Hashable, Iterator, TypeVar

T = TypeVar("T", bound=Hashable)


class UndirectedGraph(Generic[T]):
    def __init__(self) -> None:
        self._adjacencies: defaultdict[T, set[T]] = defaultdict(set)

    def add_edge(self, u: T, v: T) -> None:
        self._adjacencies[u].add(v)
        self._adjacencies[v].add(u)

    def neighbors(self, node: T) -> Iterator[T]:
        return iter(self._adjacencies[node])

    def nodes(self) -> Iterator[T]:
        yield from self._adjacencies.keys()

    def are_neighbors(self, node_a: T, node_b: T) -> bool:
        return node_b in self._adjacencies[node_a]
