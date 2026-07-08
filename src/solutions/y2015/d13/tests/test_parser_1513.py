from typing import Callable

from src.core.input_reader import InputReader
from src.solutions.y2015.d13.logic.parser import parse_happiness_graph


def test_parse_happiness_yields_undirected_weighted_graph(
    input_reader: Callable[[str], InputReader],
) -> None:
    example = """
              Alice would gain 54 happiness units by sitting next to Bob.
              Alice would lose 79 happiness units by sitting next to Carol.
              Bob would gain 83 happiness units by sitting next to Alice.
              Bob would lose 7 happiness units by sitting next to Carol.
              Carol would lose 62 happiness units by sitting next to Alice.
              Carol would gain 60 happiness units by sitting next to Bob.
              """
    graph = parse_happiness_graph(input_reader(example))
    assert set(graph.nodes()) == {"Alice", "Bob", "Carol"}
    assert graph.edge_weight("Alice", "Bob") == 137  # 54 + 83
    assert graph.edge_weight("Alice", "Carol") == -141  # -79 + -62
    assert graph.edge_weight("Bob", "Carol") == 53  # -7 + 60
