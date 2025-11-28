from typing import Iterator

from src.core.input_reader import InputReader
from src.core.io_handler import IOHandler
from src.solutions.shared.geometry.hexagonal import HexagonalCoordinates
from src.solutions.y2020.d24.logic.direction_parser import (
    parse_hexagonal_directions,
)
from src.solutions.y2020.d24.logic.hexagonal_automaton import (
    HexagonalAutomaton,
)


def _input_tiles(input_reader: InputReader) -> Iterator[HexagonalCoordinates]:
    for directions in parse_hexagonal_directions(input_reader):
        tile = HexagonalCoordinates(0, 0)
        for direction in directions:
            tile = tile.move(direction)
        yield tile


def solve(io_handler: IOHandler) -> None:
    prob_id = 2020, 24

    black_tiles: set[HexagonalCoordinates] = set()
    for tile in _input_tiles(io_handler.input_reader(*prob_id)):
        if tile in black_tiles:
            black_tiles.remove(tile)
        else:
            black_tiles.add(tile)

    io_handler.write_result(*prob_id, part=1, result=len(black_tiles))

    progress_monitor = io_handler.progress_monitor(*prob_id, part=2)
    automaton = HexagonalAutomaton(alive_cells=black_tiles)
    num_iterations = 100
    for i in range(num_iterations):
        progress_monitor.update_progress_bar(i, num_iterations)
        automaton = automaton.next_iteration()
    io_handler.write_result(
        *prob_id, part=2, result=automaton.num_black_tiles()
    )
