from collections import defaultdict
from typing import Iterator

import pytest

from src.solutions.shared.graph import (
    UndirectedGraph,
    bfs,
    dfs,
    min_path_length_with_bfs,
    min_path_length_with_dijkstra,
)


@pytest.fixture
def simple_undirected_graph():
    graph = UndirectedGraph[str]()
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("D", "E")
    return graph


def test_undirected_graph_keeps_track_of_nodes(simple_undirected_graph):
    nodes = set(simple_undirected_graph.nodes())
    assert nodes == {"A", "B", "C", "D", "E"}


def test_undirected_graph_keeps_track_of_neighbors(simple_undirected_graph):
    assert set(simple_undirected_graph.neighbors("A")) == {"B", "C"}
    assert set(simple_undirected_graph.neighbors("E")) == {"D"}
    assert set(simple_undirected_graph.neighbors("F")) == set()
    assert simple_undirected_graph.are_neighbors("A", "B")
    assert not simple_undirected_graph.are_neighbors("A", "D")
    assert not simple_undirected_graph.are_neighbors("A", "A")


def test_dfs_visits_all_nodes_once(simple_undirected_graph) -> None:
    visited_nodes = "".join(dfs("A", simple_undirected_graph.neighbors))
    assert visited_nodes in {"ABDEC", "ACBDE"}


def test_bfs_visits_all_nodes_once(simple_undirected_graph) -> None:
    visited_nodes = "".join(
        map(lambda c: c.node, bfs("A", simple_undirected_graph.neighbors))
    )
    assert visited_nodes in {"ABCDE", "ACBDE"}


def test_bfs_cannot_find_optinal_path_if_no_path_exists():
    graph = UndirectedGraph[str]()
    with pytest.raises(ValueError, match="No path found"):
        _ = min_path_length_with_bfs(
            start_node="A",
            is_final_state=lambda n: n == "B",
            neighbors=graph.neighbors,
        )


@pytest.fixture
def undirected_graph():
    graph = UndirectedGraph[str]()
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "E")
    graph.add_edge("C", "F")
    graph.add_edge("D", "F")
    graph.add_edge("E", "F")
    graph.add_edge("F", "G")
    return graph


def test_optimal_path_with_bfs(undirected_graph) -> None:
    assert 2 == min_path_length_with_bfs(
        start_node="A",
        is_final_state=lambda n: n in "FG",
        neighbors=undirected_graph.neighbors,
    )


class _WeightedGraph:
    def __init__(self):
        self._adjacencies: dict[str, dict[str, int]] = defaultdict(dict)

    def weighted_neighbors(self, node: str) -> Iterator[tuple[str, int]]:
        yield from self._adjacencies[node].items()

    def add_edge(self, node_a: str, node_b: str, weight: int) -> None:
        self._adjacencies[node_a][node_b] = weight
        self._adjacencies[node_b][node_a] = weight


def test_dijkstra_cannot_find_optimal_path_if_no_path_exists():
    graph = _WeightedGraph()
    with pytest.raises(ValueError, match="No path found"):
        _ = min_path_length_with_dijkstra(
            start_node="A",
            is_final_state=lambda n: n == "B",
            weighted_neighbors=graph.weighted_neighbors,
        )


def test_optimal_path_with_dijkstra():
    graph = _WeightedGraph()
    graph.add_edge("A", "B", weight=3)
    graph.add_edge("A", "D", weight=8)
    graph.add_edge("B", "D", weight=5)
    graph.add_edge("B", "E", weight=6)
    graph.add_edge("D", "E", weight=3)
    graph.add_edge("D", "F", weight=2)
    graph.add_edge("E", "F", weight=1)
    graph.add_edge("E", "C", weight=9)
    graph.add_edge("F", "C", weight=3)
    path_length = min_path_length_with_dijkstra(
        start_node="A",
        is_final_state=lambda n: n == "C",
        weighted_neighbors=graph.weighted_neighbors,
    )
    assert path_length == 13
