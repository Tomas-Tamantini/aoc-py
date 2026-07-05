from typing import Callable

from src.core.input_reader import InputReader
from src.solutions.y2015.d09.logic.parser import parse_distances


def test_parse_distances_yields_weighted_graph(
    input_reader: Callable[[str], InputReader],
) -> None:
    example = """
              London to Dublin = 464
              London to Belfast = 518
              Dublin to Belfast = 141
              """
    graph = parse_distances(input_reader(example))
    assert set(graph.nodes()) == {"London", "Dublin", "Belfast"}
    assert graph.edge_weight("London", "Dublin") == 464
    assert graph.edge_weight("London", "Belfast") == 518
    assert graph.edge_weight("Dublin", "Belfast") == 141
