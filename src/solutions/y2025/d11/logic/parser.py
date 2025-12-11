from src.core.input_reader import InputReader


def parse_adjacency_list(input_reader: InputReader) -> dict[str, tuple[str]]:
    adjacencies = dict()
    for line in input_reader.read_stripped_lines():
        parts = line.split(":")
        adjacencies[parts[0].strip()] = tuple(parts[1].split())
    return adjacencies
