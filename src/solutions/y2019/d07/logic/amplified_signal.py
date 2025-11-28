from typing import Iterator

from src.solutions.y2019.d07.logic.amplifier import Amplifier
from src.solutions.y2019.d07.logic.amplifier_io import AmplifierIO
from src.solutions.y2019.intcode import IntcodeProgram


def _io_queues(
    phase_settings: tuple[int, ...], include_feedback: bool
) -> Iterator[AmplifierIO]:
    first_queue = None
    for i, phase_setting in enumerate(phase_settings):
        io_queue = AmplifierIO()
        io_queue.put(phase_setting)
        if i == 0:
            io_queue.put(0)
            first_queue = io_queue
        yield io_queue
    if include_feedback and first_queue:
        yield first_queue
    else:
        yield AmplifierIO()


def amplified_signal(
    instructions: list[int],
    phase_settings: tuple[int, ...],
    include_feedback: bool,
) -> int:
    io_queues = list(_io_queues(phase_settings, include_feedback))
    num_amplifiers = len(phase_settings)
    amplifiers = [
        Amplifier(
            program=IntcodeProgram(instructions),
            input_queue=io_queues[i],
            output_queue=io_queues[i + 1],
        )
        for i in range(num_amplifiers)
    ]
    while not all(a.halted for a in amplifiers):
        for amplifier in amplifiers:
            amplifier.resume_execution()
    return io_queues[-1].last_output
