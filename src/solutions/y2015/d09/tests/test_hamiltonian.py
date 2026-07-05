from src.solutions.shared.graph import WeightedUndirectedGraph
from src.solutions.y2015.d09.logic.hamiltonian import (
    hamiltonian_path_distances,
)


def test_all_hamiltonian_path_distances_are_yielded() -> None:
    graph: WeightedUndirectedGraph[str] = WeightedUndirectedGraph()
    graph.add_edge("London", "Dublin", 464)
    graph.add_edge("London", "Belfast", 518)
    graph.add_edge("Dublin", "Belfast", 141)
    distances = list(hamiltonian_path_distances(graph))
    assert set(distances) == {605, 659, 982}
