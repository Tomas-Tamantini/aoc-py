from itertools import combinations

from src.core.io_handler import IOHandler
from src.solutions.shared.parser import parse_grid
from src.solutions.y2023.d11.logic.galaxies import Galaxies


def solve(io_handler: IOHandler) -> None:
    prob_id = 2023, 11

    reader = io_handler.input_reader(*prob_id)

    positions = parse_grid(reader).positions(symbol="#")
    galaxies = Galaxies(positions)

    total_p1 = sum(
        galaxies.distance(*pair, expansion_rate=2)
        for pair in combinations(galaxies.positions(), 2)
    )
    io_handler.write_result(*prob_id, part=1, result=total_p1)

    total_p2 = sum(
        galaxies.distance(*pair, expansion_rate=1_000_000)
        for pair in combinations(galaxies.positions(), 2)
    )
    io_handler.write_result(*prob_id, part=2, result=total_p2)
