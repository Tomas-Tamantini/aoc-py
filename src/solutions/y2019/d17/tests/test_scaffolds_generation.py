from typing import Iterator

from src.solutions.shared.geometry import Direction, Vector2D
from src.solutions.y2019.d17.logic.generate_scaffolds_map import (
    generate_scaffolds_map,
)


def _instructions() -> Iterator[int]:
    expected_map = "..#\n.##\n.^."
    for c in expected_map:
        yield 104
        yield ord(c)
    yield 99


def test_scaffolds_map_is_built_from_intcode_instructions():
    scaffolds_map = generate_scaffolds_map(list(_instructions()))
    assert scaffolds_map.tiles == {
        Vector2D(2, 0),
        Vector2D(1, -1),
        Vector2D(2, -1),
        Vector2D(1, -2),
    }
    assert scaffolds_map.robot_start.position == Vector2D(1, -2)
    assert scaffolds_map.robot_start.direction == Direction.UP
