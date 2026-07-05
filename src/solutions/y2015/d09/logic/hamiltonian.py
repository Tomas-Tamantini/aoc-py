from itertools import permutations
from typing import Iterator

from src.solutions.shared.graph import WeightedUndirectedGraph


def _route_distance(
    route: tuple[str, ...], graph: WeightedUndirectedGraph[str]
) -> int:
    return sum(
        graph.edge_weight(route[i], route[i + 1])
        for i in range(len(route) - 1)
    )


def hamiltonian_path_distances(
    graph: WeightedUndirectedGraph[str],
) -> Iterator[int]:
    for perm in permutations(graph.nodes()):
        yield _route_distance(perm, graph)
