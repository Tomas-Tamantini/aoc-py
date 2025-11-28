from typing import Iterator, Optional

from src.solutions.shared.geometry import Turn, Vector2D
from src.solutions.y2019.d17.logic.scaffolds_map import ScaffoldsMap
from src.solutions.y2019.d17.logic.vacuum_robot import VacuumRobot


def _num_tiles_in_front(robot: VacuumRobot, tiles: set[Vector2D]) -> int:
    num_steps = 0
    current_tile = robot.position
    while True:
        current_tile = current_tile.move(robot.direction)
        if current_tile in tiles:
            num_steps += 1
        else:
            return num_steps


def _next_turn_direction(
    robot: VacuumRobot, tiles: set[Vector2D]
) -> Optional[Turn]:
    for turn in (Turn.RIGHT, Turn.LEFT):
        next_tile = robot.adjacent_tile(turn)
        if next_tile in tiles:
            return turn


def scaffold_movement_instructions(scaffolds: ScaffoldsMap) -> Iterator[str]:
    current_robot = scaffolds.robot_start
    while True:
        if num_steps_forward := _num_tiles_in_front(
            current_robot, scaffolds.tiles
        ):
            yield str(num_steps_forward)
            current_robot = current_robot.move_forward(num_steps_forward)
        elif turn_direction := _next_turn_direction(
            current_robot, scaffolds.tiles
        ):
            yield "R" if turn_direction == Turn.RIGHT else "L"
            current_robot = current_robot.turn(turn_direction)
        else:
            break
