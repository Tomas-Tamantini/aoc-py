from typing import Hashable, Iterable


def num_paths(
    origin: Hashable,
    destination: Hashable,
    adjacencies: dict[Hashable, Iterable[Hashable]],
) -> int:
    if origin == destination:
        return 1
    else:
        return sum(
            num_paths(neighbor, destination, adjacencies)
            for neighbor in adjacencies[origin]
        )
