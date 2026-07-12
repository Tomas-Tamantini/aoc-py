from typing import Iterator

import pytest

from src.solutions.shared.graph import (
    DisjointSet,
    UndirectedGraph,
    WeightedDirectedGraph,
    WeightedUndirectedGraph,
    bfs,
    dfs,
    min_path_length_with_a_star,
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


def test_dfs_visits_all_nodes_once(simple_undirected_graph):
    visited_nodes = "".join(dfs("A", simple_undirected_graph.neighbors))
    assert visited_nodes in {"ABDEC", "ACBDE"}


def test_bfs_visits_all_nodes_once(simple_undirected_graph):
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


def test_optimal_path_with_bfs(undirected_graph):
    assert 2 == min_path_length_with_bfs(
        start_node="A",
        is_final_state=lambda n: n in "FG",
        neighbors=undirected_graph.neighbors,
    )


@pytest.fixture
def simple_weighted_graph() -> WeightedUndirectedGraph[str]:
    graph: WeightedUndirectedGraph[str] = WeightedUndirectedGraph()
    graph.add_edge("A", "B", 3)
    graph.add_edge("A", "C", 7)
    graph.add_edge("B", "C", 1)
    return graph


def test_weighted_graph_keeps_track_of_nodes(simple_weighted_graph):
    assert set(simple_weighted_graph.nodes()) == {"A", "B", "C"}


def test_weighted_graph_keeps_track_of_edge_weight(simple_weighted_graph):
    assert simple_weighted_graph.edge_weight("A", "B") == 3
    assert simple_weighted_graph.edge_weight("A", "C") == 7
    assert simple_weighted_graph.edge_weight("B", "C") == 1


def test_weighted_graph_is_symmetric(simple_weighted_graph):
    assert simple_weighted_graph.edge_weight("B", "A") == 3
    assert simple_weighted_graph.edge_weight("C", "B") == 1


def test_weighted_graph_indicates_whether_are_neighbors(simple_weighted_graph):
    assert simple_weighted_graph.are_neighbors("A", "B")
    assert not simple_weighted_graph.are_neighbors("A", "A")


def test_weighted_graph_keeps_track_of_neighbors(simple_weighted_graph):
    assert set(simple_weighted_graph.neighbors("A")) == {"B", "C"}


class _WeightedGraph(WeightedUndirectedGraph[str]):
    def weighted_neighbors(self, node: str) -> Iterator[tuple[str, int]]:
        yield from self._weights[node].items()


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


def test_a_star_cannot_find_optimal_path_if_no_path_exists():
    graph = _WeightedGraph()
    with pytest.raises(ValueError, match="No path found"):
        _ = min_path_length_with_a_star(
            start_node="A",
            is_final_state=lambda n: n == "B",
            weighted_neighbors=graph.weighted_neighbors,
            heuristic=lambda _n: 0,
        )


def test_optimal_path_with_a_star():
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

    heuristic = {
        "A": 11,
        "B": 8,
        "C": 0,
        "D": 7,
        "E": 4,
        "F": 3,
    }.__getitem__

    path_length = min_path_length_with_a_star(
        start_node="A",
        is_final_state=lambda n: n == "C",
        weighted_neighbors=graph.weighted_neighbors,
        heuristic=heuristic,
    )
    assert path_length == 13


@pytest.fixture
def simple_weighted_directed_graph() -> WeightedDirectedGraph[str]:
    graph: WeightedDirectedGraph[str] = WeightedDirectedGraph()
    graph.add_edge("A", "B", 3)
    graph.add_edge("B", "A", 2)
    graph.add_edge("A", "C", 7)
    graph.add_edge("B", "C", 1)
    graph.add_edge("D", "A", 5)
    return graph


def test_weighted_directed_graph_keeps_track_of_nodes(
    simple_weighted_directed_graph: WeightedDirectedGraph[str],
):
    assert set(simple_weighted_directed_graph.nodes()) == {"A", "B", "C", "D"}


def test_weighted_directed_graph_keeps_track_of_edge_weight(
    simple_weighted_directed_graph: WeightedDirectedGraph[str],
):
    assert simple_weighted_directed_graph.edge_weight("A", "B") == 3
    assert simple_weighted_directed_graph.edge_weight("B", "A") == 2
    assert simple_weighted_directed_graph.edge_weight("A", "C") == 7
    assert simple_weighted_directed_graph.edge_weight("B", "C") == 1
    assert simple_weighted_directed_graph.edge_weight("D", "A") == 5


def test_weighted_directed_graph_has_edge(
    simple_weighted_directed_graph: WeightedDirectedGraph[str],
):
    assert simple_weighted_directed_graph.has_edge("A", "C")
    assert not simple_weighted_directed_graph.has_edge("C", "A")
    assert not simple_weighted_directed_graph.has_edge("A", "A")


def test_weighted_directed_graph_keeps_track_of_neighbors(
    simple_weighted_directed_graph: WeightedDirectedGraph[str],
):
    assert set(simple_weighted_directed_graph.neighbors("A")) == {"B", "C"}
    assert set(simple_weighted_directed_graph.neighbors("B")) == {"A", "C"}
    assert set(simple_weighted_directed_graph.neighbors("C")) == set()
    assert set(simple_weighted_directed_graph.neighbors("D")) == {"A"}


def test_disjoint_set_starts_empty():
    ds = DisjointSet()
    with pytest.raises(KeyError):
        ds.find("a")


def test_disjoint_set_merges_elements():
    ds = DisjointSet()
    for element in ("a", "b", "c"):
        ds.make_set(element)
    assert ds.find("a") != ds.find("b")
    assert ds.find("a") != ds.find("c")
    ds.union("a", "b")
    assert ds.find("a") == ds.find("b")
    ds.union("b", "c")
    assert ds.find("a") == ds.find("c")
