from src.solutions.shared.geometry import Direction, Vector2D
from src.solutions.y2019.d11.logic.hull import Hull
from src.solutions.y2019.d11.logic.hull_robot import HullRobot
from src.solutions.y2019.d11.logic.run_hull_program import (
    run_paint_hull_program,
)


def test_hull_painting_program():
    instructions = [3, 100, 4, 100, 4, 100, 104, 1, 99]
    hull = Hull()
    initial_bot = HullRobot(position=Vector2D(0, 0), direction=Direction.UP)
    run_paint_hull_program(instructions, hull, initial_bot)
    assert hull.num_panels_painted_at_least_once == 2
