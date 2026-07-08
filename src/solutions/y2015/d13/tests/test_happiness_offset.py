from src.solutions.shared.graph import WeightedUndirectedGraph
from src.solutions.y2015.d13.logic.happiness_offset import max_happiness_offset


def test_maximum_happiness_offset_is_found_for_graph() -> None:
    graph: WeightedUndirectedGraph[str] = WeightedUndirectedGraph()
    graph.add_edge("Alice", "Bob", 137)
    graph.add_edge("Alice", "Carol", -141)
    graph.add_edge("Alice", "David", 44)
    graph.add_edge("Bob", "Carol", 53)
    graph.add_edge("Bob", "David", 56)
    graph.add_edge("Carol", "David", 96)
    offset = max_happiness_offset(graph)
    assert offset == 330
