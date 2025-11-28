from src.core.io_handler import IOHandler
from src.solutions.y2019.d17.logic.generate_scaffolds_map import (
    generate_scaffolds_map,
)
from src.solutions.y2019.d17.logic.memory_specs import VacuumRobotMemorySpecs
from src.solutions.y2019.d17.logic.robot_routine import vacuum_robot_routine
from src.solutions.y2019.d17.logic.scaffolds_map import ScaffoldsMap
from src.solutions.y2019.intcode import (
    IntcodeProgram,
    SimpleSerialInput,
    SimpleSerialOutput,
    parse_instructions,
    run_intcode_program,
)


def _run_vacuum_robot_program(
    instructions: list[int], scaffolds: ScaffoldsMap, see_video_feed: bool
) -> int:
    memory_specs = VacuumRobotMemorySpecs(num_subroutines=3, max_characters=20)
    program = IntcodeProgram(instructions)
    serial_output = SimpleSerialOutput()
    routine = vacuum_robot_routine(
        scaffolds=scaffolds,
        see_video_feed=see_video_feed,
        memory_specs=memory_specs,
    )
    input_values = [ord(c) for c in routine]
    serial_input = SimpleSerialInput(input_values)
    run_intcode_program(
        program, serial_input=serial_input, serial_output=serial_output
    )
    return serial_output.last_output


def solve(io_handler: IOHandler) -> None:
    prob_id = 2019, 17

    instructions = parse_instructions(io_handler.input_reader(*prob_id))
    scaffolds = generate_scaffolds_map(instructions)

    alignment = sum(abs(i.x * i.y) for i in scaffolds.intersections())
    io_handler.write_result(*prob_id, part=1, result=alignment)

    modified_instructions = instructions[:]
    modified_instructions[0] = 2
    see_video_feed = False
    dust = _run_vacuum_robot_program(
        modified_instructions, scaffolds, see_video_feed
    )
    io_handler.write_result(*prob_id, part=2, result=dust)
