from itertools import permutations

from src.solutions.shared.graph import WeightedUndirectedGraph


def _happiness_offset(
    route: tuple[str, ...], graph: WeightedUndirectedGraph[str]
) -> int:
    return sum(
        graph.edge_weight(route[i], route[i + 1])
        for i in range(len(route) - 1)
    ) + graph.edge_weight(route[-1], route[0])


def max_happiness_offset(graph: WeightedUndirectedGraph) -> int:
    return max(
        _happiness_offset(route, graph)
        for route in permutations(graph.nodes())
    )
