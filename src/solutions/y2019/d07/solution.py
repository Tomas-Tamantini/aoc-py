from itertools import permutations

from src.core.io_handler import IOHandler
from src.solutions.y2019.d07.logic.amplified_signal import amplified_signal
from src.solutions.y2019.intcode import parse_instructions


def solve(io_handler: IOHandler) -> None:
    prob_id = 2019, 7
    instructions = parse_instructions(io_handler.input_reader(*prob_id))

    max_linear_signal = max(
        amplified_signal(instructions, phase_settings, include_feedback=False)
        for phase_settings in permutations(range(5))
    )
    io_handler.write_result(*prob_id, part=1, result=max_linear_signal)

    max_feedback_signal = max(
        amplified_signal(instructions, phase_settings, include_feedback=True)
        for phase_settings in permutations(range(5, 10))
    )
    io_handler.write_result(*prob_id, part=2, result=max_feedback_signal)
