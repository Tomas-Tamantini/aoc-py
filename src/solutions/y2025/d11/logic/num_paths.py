from math import prod
from typing import Hashable, Iterable


def _num_paths_recursive(
    current: Hashable,
    destination: Hashable,
    adjacencies: dict[Hashable, Iterable[Hashable]],
    memoized: dict[Hashable, int],
) -> int:
    if current == destination:
        return 1
    if current not in memoized:
        memoized[current] = sum(
            _num_paths_recursive(neighbor, destination, adjacencies, memoized)
            for neighbor in adjacencies.get(current, tuple())
        )
    return memoized[current]


def num_paths(
    *nodes: Hashable,
    adjacencies: dict[Hashable, Iterable[Hashable]],
) -> int:
    return prod(
        _num_paths_recursive(
            nodes[i], nodes[i + 1], adjacencies, memoized=dict()
        )
        for i in range(len(nodes) - 1)
    )
