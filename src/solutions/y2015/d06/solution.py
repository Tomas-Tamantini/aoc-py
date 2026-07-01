from src.core.io_handler import IOHandler
from src.solutions.y2015.d06.logic.light_grid import LightGrid
from src.solutions.y2015.d06.logic.parse_light_grid_instructions import (
    parse_light_grid_instructions,
)

_GRID_SIZE = 1000


def solve(io_handler: IOHandler) -> None:
    prob_id = 2015, 6

    grid_p1 = LightGrid(_GRID_SIZE, _GRID_SIZE)
    for instruction in parse_light_grid_instructions(
        io_handler.input_reader(*prob_id)
    ):
        instruction.apply(grid_p1)
    io_handler.write_result(
        *prob_id, part=1, result=grid_p1.total_brightness()
    )

    grid_p2 = LightGrid(_GRID_SIZE, _GRID_SIZE)
    for instruction in parse_light_grid_instructions(
        io_handler.input_reader(*prob_id), translate_instructions=True
    ):
        instruction.apply(grid_p2)
    io_handler.write_result(
        *prob_id, part=2, result=grid_p2.total_brightness()
    )
