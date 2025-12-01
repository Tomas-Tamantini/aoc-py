from src.core.io_handler import IOHandler
from src.solutions.y2025.d01.logic.parser import parse_dial_instructions
from src.solutions.y2025.d01.logic.turn_dial import TurnDial, dial_positions


def solve(io_handler: IOHandler) -> None:
    prob_id = 2025, 1

    dial = TurnDial(num_positions=100, start_position=50)
    instructions = list(
        parse_dial_instructions(io_handler.input_reader(*prob_id))
    )

    positions = list(dial_positions(dial, instructions))

    num_zeros = positions.count(0)

    io_handler.write_result(*prob_id, part=1, result=num_zeros)
    io_handler.write_result(*prob_id, part=2, result="not implemented")
