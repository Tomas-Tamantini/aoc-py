from typing import Iterable, Iterator

from src.solutions.shared.geometry import Direction, Vector2D
from src.solutions.y2019.d17.logic.scaffolds_map import ScaffoldsMap
from src.solutions.y2019.d17.logic.vacuum_robot import VacuumRobot
from src.solutions.y2019.intcode import (
    IntcodeProgram,
    SimpleSerialOutput,
    run_intcode_program,
)


def _parse_direction(output_chr: str) -> Direction | None:
    return {
        "^": Direction.UP,
        "v": Direction.DOWN,
        ">": Direction.RIGHT,
        "<": Direction.LEFT,
    }.get(output_chr)


def _iterate_positions(
    output_values: Iterable[int],
) -> Iterator[tuple[Vector2D, str]]:
    x = y = 0
    for output_value in output_values:
        if output_value == ord("\n"):
            x = 0
            y -= 1
        else:
            yield (Vector2D(x, y), chr(output_value))
            x += 1


def _parse_output(output_values: list[int]) -> ScaffoldsMap:
    tiles: set[Vector2D] = set()
    robot_pos: Vector2D | None = None
    robot_direction: Direction | None = None
    for pos, output_chr in _iterate_positions(output_values):
        if output_chr != ".":
            tiles.add(pos)
        if dir := _parse_direction(output_chr):
            robot_pos = pos
            robot_direction = dir

    if not robot_pos or not robot_direction:
        raise ValueError("Could not find robot position")
    return ScaffoldsMap(
        tiles=tiles, robot_start=VacuumRobot(robot_pos, robot_direction)
    )


def generate_scaffolds_map(instructions: list[int]) -> ScaffoldsMap:
    program = IntcodeProgram(instructions)
    serial_output = SimpleSerialOutput()
    run_intcode_program(program, serial_output=serial_output)
    return _parse_output(serial_output.output_values)
