from src.core.io_handler import IOHandler
from src.solutions.y2019.d25.logic.droid_controller import (
    AutomaticDroidController,
    ManualDroidController,
)
from src.solutions.y2019.d25.logic.droid_input import DroidInput
from src.solutions.y2019.d25.logic.droid_output import DroidOutput
from src.solutions.y2019.intcode import (
    IntcodeProgram,
    parse_instructions,
    run_intcode_program,
)


def _droid_io(io_handler: IOHandler) -> tuple[DroidInput, DroidOutput]:
    prob_id = 2019, 25
    game_interface = io_handler.game_interface(*prob_id, part=1)
    if game_interface:
        controller = ManualDroidController(game_interface)
    else:
        commands = list(
            io_handler.input_reader(
                *prob_id, file_name="solution_part_1.txt"
            ).read_stripped_lines()
        )
        controller = AutomaticDroidController(commands)
    return DroidInput(controller), DroidOutput(game_interface)


def solve(io_handler: IOHandler) -> None:
    prob_id = 2019, 25

    instructions = parse_instructions(
        input_reader=io_handler.input_reader(*prob_id)
    )

    program = IntcodeProgram(instructions)
    droid_input, droid_output = _droid_io(io_handler)
    run_intcode_program(program, droid_input, droid_output)

    io_handler.write_result(
        *prob_id, part=1, result=droid_output.password, supports_play=True
    )
