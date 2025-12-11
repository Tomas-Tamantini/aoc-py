from src.core.io_handler import IOHandler
from src.solutions.y2025.d11.logic.num_paths import num_paths
from src.solutions.y2025.d11.logic.parser import parse_adjacency_list


def solve(io_handler: IOHandler) -> None:
    prob_id = 2025, 11

    adjacencies = parse_adjacency_list(io_handler.input_reader(*prob_id))

    n = num_paths(origin="you", destination="out", adjacencies=adjacencies)

    io_handler.write_result(*prob_id, part=1, result=n)
    io_handler.write_result(*prob_id, part=2, result="not implemented")
