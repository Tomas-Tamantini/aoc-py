from typing import Iterator

from src.solutions.shared.geometry import Direction, Vector2D
from src.solutions.y2019.d17.logic.scaffolds_map import ScaffoldsMap
from src.solutions.y2019.d17.logic.vacuum_robot import VacuumRobot


def _tiles() -> Iterator[Vector2D]:
    """
     0123
    0.#..
    1.#..
    2####
    3.#.#
    4.###
    5...#
    """
    for y in range(5):
        yield Vector2D(1, y)
    for x in range(4):
        yield Vector2D(x, 2)
    for y in range(2, 6):
        yield Vector2D(3, y)
    yield Vector2D(2, 4)


def test_scaffolds_map_yields_intersection_positions():
    scaffolds = ScaffoldsMap(
        tiles=set(_tiles()),
        robot_start=VacuumRobot(
            position=Vector2D(0, 0), direction=Direction.UP
        ),
    )
    intersections = list(scaffolds.intersections())
    assert len(intersections) == 2
    assert set(intersections) == {Vector2D(1, 2), Vector2D(3, 4)}
