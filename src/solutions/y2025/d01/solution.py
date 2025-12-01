from src.core.io_handler import IOHandler
from src.solutions.y2025.d01.logic.parser import parse_dial_offsets
from src.solutions.y2025.d01.logic.turn_dial import (
    TurnDial,
    num_times_clicked_zero,
    num_times_landed_in_zero,
)


def solve(io_handler: IOHandler) -> None:
    prob_id = 2025, 1

    offsets = list(parse_dial_offsets(io_handler.input_reader(*prob_id)))

    dial = TurnDial(size=100, start_position=50)

    num_zeros_p1 = num_times_landed_in_zero(dial, offsets)
    io_handler.write_result(*prob_id, part=1, result=num_zeros_p1)

    num_zeros_p2 = num_times_clicked_zero(dial, offsets)
    io_handler.write_result(*prob_id, part=2, result=num_zeros_p2)
