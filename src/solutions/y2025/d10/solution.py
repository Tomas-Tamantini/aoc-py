from src.core.io_handler import IOHandler
from src.solutions.y2025.d10.logic.optimize_presses import (
    min_presses_to_turn_lights_on,
)
from src.solutions.y2025.d10.logic.parser import (
    parse_indicator_lights_diagrams,
)


def solve(io_handler: IOHandler) -> None:
    prob_id = 2025, 10

    diagrams = parse_indicator_lights_diagrams(
        io_handler.input_reader(*prob_id)
    )

    total = sum(min_presses_to_turn_lights_on(d) for d in diagrams)

    io_handler.write_result(*prob_id, part=1, result=total)
    io_handler.write_result(*prob_id, part=2, result="not implemented")
