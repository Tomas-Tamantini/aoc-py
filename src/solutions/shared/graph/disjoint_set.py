from typing import Generic, Hashable, TypeVar

T = TypeVar("T", bound=Hashable)


class DisjointSet(Generic[T]):
    def __init__(self):
        self._parents = dict()
        self._rank = dict()

    def make_set(self, element: T) -> None:
        self._parents[element] = element
        self._rank[element] = 0

    def find(self, element: T) -> T:
        if self._parents[element] != element:
            self._parents[element] = self.find(self._parents[element])
        return self._parents[element]

    def union(self, element_a: T, element_b: T) -> None:
        root_a = self.find(element_a)
        root_b = self.find(element_b)
        if root_a == root_b:
            return
        if self._rank[root_b] > self._rank[root_a]:
            root_a, root_b = root_b, root_a
        self._parents[root_b] = root_a
        if self._rank[root_a] == self._rank[root_b]:
            self._rank[root_a] += 1
