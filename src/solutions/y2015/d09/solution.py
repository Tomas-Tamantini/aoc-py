from src.core.io_handler import IOHandler
from src.solutions.y2015.d09.logic.hamiltonian import (
    hamiltonian_path_distances,
)
from src.solutions.y2015.d09.logic.parser import parse_distances


def solve(io_handler: IOHandler) -> None:
    prob_id = 2015, 9

    graph = parse_distances(io_handler.input_reader(*prob_id))
    distances = list(hamiltonian_path_distances(graph))

    io_handler.write_result(*prob_id, part=1, result=min(distances))
    io_handler.write_result(*prob_id, part=2, result=max(distances))
