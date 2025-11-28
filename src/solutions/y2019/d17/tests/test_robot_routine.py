from typing import Iterator

import pytest

from src.solutions.shared.geometry import Direction, Vector2D
from src.solutions.y2019.d17.logic.memory_specs import VacuumRobotMemorySpecs
from src.solutions.y2019.d17.logic.robot_routine import vacuum_robot_routine
from src.solutions.y2019.d17.logic.scaffolds_map import ScaffoldsMap
from src.solutions.y2019.d17.logic.vacuum_robot import VacuumRobot


@pytest.fixture(scope="module")
def scaffolds() -> ScaffoldsMap:
    feed = """
           #######...#####
           #.....#...#...#
           #.....#...#...#
           ......#...#...#
           ......#...###.#
           ......#.....#.#
           ^########...#.#
           ......#.#...#.#
           ......#########
           ........#...#..
           ....#########..
           ....#...#......
           ....#...#......
           ....#...#......
           ....#####......
           """
    tiles = set()
    robot_pos = Vector2D(0, 0)
    y = 1
    for line in feed.splitlines():
        if stripped_line := line.strip():
            y -= 1
            for x, c in enumerate(stripped_line):
                pos = Vector2D(x, y)
                if c == "#":
                    tiles.add(pos)
                elif c == "^":
                    tiles.add(pos)
                    robot_pos = pos
    return ScaffoldsMap(
        tiles, robot_start=VacuumRobot(robot_pos, Direction.UP)
    )


def _expected_routine() -> Iterator[str]:
    yield "A,B,C,B,A,C"
    yield "R,8,R,8"
    yield "R,4,R,4"
    yield "R,8,L,6,L,2"


def _memory_specs() -> VacuumRobotMemorySpecs:
    return VacuumRobotMemorySpecs(num_subroutines=3, max_characters=11)


@pytest.mark.parametrize(
    ("see_video_feed", "expected_char"), [(False, "n"), (True, "y")]
)
def test_robot_routine_indicates_whether_will_see_video_feed(
    scaffolds, see_video_feed, expected_char
):
    routine = vacuum_robot_routine(scaffolds, _memory_specs(), see_video_feed)
    assert routine[-2] == expected_char


def test_robot_routine_does_not_exceed_character_limit(scaffolds):
    routine = vacuum_robot_routine(
        scaffolds, _memory_specs(), see_video_feed=True
    )
    expected_routine = "\n".join(_expected_routine()) + "\ny\n"
    assert routine == expected_routine
