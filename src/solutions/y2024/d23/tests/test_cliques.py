from src.solutions.shared.graph import UndirectedGraph
from src.solutions.y2024.d23.logic.cliques import cliques


def test_cliques_iterates_through_all_cliques():
    graph = UndirectedGraph[str]()
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "C")
    graph.add_edge("D", "E")
    graph.add_edge("E", "F")

    all_cliques = list(cliques(graph))
    cliques_as_str = set("".join(sorted(c)) for c in all_cliques)
    assert cliques_as_str == {
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "AB",
        "AC",
        "BC",
        "DE",
        "EF",
        "ABC",
    }
