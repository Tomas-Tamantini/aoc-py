from typing import Iterable, Iterator

from src.core.io_handler import IOHandler
from src.solutions.shared.geometry import Direction, Vector2D


def _parse_instructions(input_reader) -> Iterator[Direction]:
    directions = {
        "^": Direction.UP,
        "v": Direction.DOWN,
        "<": Direction.LEFT,
        ">": Direction.RIGHT,
    }
    for c in input_reader.read_input():
        yield directions[c]


def _visited_houses(instructions: Iterable[Direction]) -> Iterator[Vector2D]:
    position = Vector2D(0, 0)
    yield position
    for direction in instructions:
        position = position.move(direction)
        yield position


def solve(io_handler: IOHandler) -> None:
    prob_id = 2015, 3

    instructions = list(_parse_instructions(io_handler.input_reader(*prob_id)))

    visited_p1 = set(_visited_houses(instructions))
    io_handler.write_result(*prob_id, part=1, result=len(visited_p1))

    instructions_santa = instructions[::2]
    instructions_robo = instructions[1::2]
    visited_santa = set(_visited_houses(instructions_santa))
    visited_robo = set(_visited_houses(instructions_robo))
    visited_p2 = visited_santa.union(visited_robo)
    io_handler.write_result(*prob_id, part=2, result=len(visited_p2))
