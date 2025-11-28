from typing import Iterator, TypeVar

from src.solutions.shared.graph import UndirectedGraph

T = TypeVar("T")


def _next_clique_members(
    graph: UndirectedGraph[T], clique: frozenset[T]
) -> Iterator[T]:
    neighbors = set(graph.neighbors(next(iter(clique))))
    for n in neighbors:
        if n not in clique and all(graph.are_neighbors(n, c) for c in clique):
            yield n


def cliques(graph: UndirectedGraph[T]) -> Iterator[frozenset[T]]:
    visited: set[frozenset[T]] = set()
    stack = {frozenset([node]) for node in graph.nodes()}
    while stack:
        current_clique = stack.pop()
        if current_clique in visited:
            continue
        visited.add(current_clique)
        yield current_clique
        for next_member in _next_clique_members(graph, current_clique):
            super_clique = current_clique | {next_member}
            if super_clique not in visited:
                stack.add(super_clique)
