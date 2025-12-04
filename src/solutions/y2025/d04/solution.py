from src.core.io_handler import IOHandler
from src.solutions.shared.parser.grid_parser import parse_grid
from src.solutions.y2025.d04.logic.paper_roll import (
    removable_rolls,
    roll_is_reachable,
)


def solve(io_handler: IOHandler) -> None:
    prob_id = 2025, 4

    grid = parse_grid(io_handler.input_reader(*prob_id))
    roll_positions = grid.positions("@")

    num_reachable_rolls = sum(
        roll_is_reachable(p, roll_positions) for p in roll_positions
    )
    io_handler.write_result(*prob_id, part=1, result=num_reachable_rolls)

    removed = len(removable_rolls(roll_positions))
    io_handler.write_result(*prob_id, part=2, result=removed)
