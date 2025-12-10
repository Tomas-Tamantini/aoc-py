from src.core.io_handler import IOHandler
from src.solutions.y2025.d10.logic.optimize_presses import (
    min_presses_to_reach_joltage,
    min_presses_to_turn_lights_on,
)
from src.solutions.y2025.d10.logic.parser import parse_machines


def solve(io_handler: IOHandler) -> None:
    prob_id = 2025, 10

    machines = list(parse_machines(io_handler.input_reader(*prob_id)))

    total_p1 = sum(min_presses_to_turn_lights_on(m) for m in machines)
    io_handler.write_result(*prob_id, part=1, result=total_p1)

    total_p2 = sum(min_presses_to_reach_joltage(m) for m in machines)
    io_handler.write_result(*prob_id, part=2, result=total_p2)
