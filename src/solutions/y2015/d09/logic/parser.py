from src.core.input_reader import InputReader
from src.solutions.shared.graph import WeightedUndirectedGraph


def _parse_distance(line: str) -> tuple[str, str, int]:
    parts = line.split()
    return parts[0], parts[2], int(parts[4])


def parse_distances(reader: InputReader) -> WeightedUndirectedGraph[str]:
    graph = WeightedUndirectedGraph()

    for line in reader.read_stripped_lines():
        city_a, city_b, dist = _parse_distance(line)
        graph.add_edge(city_a, city_b, dist)

    return graph
