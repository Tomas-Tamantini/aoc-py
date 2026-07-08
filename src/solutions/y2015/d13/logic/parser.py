from collections import defaultdict

from src.core.input_reader import InputReader
from src.solutions.shared.graph import (
    WeightedUndirectedGraph,
)


def _parse_happiness_connection(line: str) -> tuple[str, str, int]:
    parts = line.split()
    person_a = parts[0]
    person_b = parts[-1][:-1]
    happiness = int(parts[3])
    if parts[2] == "lose":
        happiness = -happiness
    return person_a, person_b, happiness


def parse_happiness_graph(reader: InputReader) -> WeightedUndirectedGraph[str]:
    weights = defaultdict(int)
    for line in reader.read_stripped_lines():
        person_a, person_b, happiness = _parse_happiness_connection(line)
        weights[frozenset({person_a, person_b})] += happiness

    graph = WeightedUndirectedGraph()
    for nodes, weight in weights.items():
        node_a, node_b = tuple(nodes)
        graph.add_edge(node_a, node_b, weight)
    return graph
