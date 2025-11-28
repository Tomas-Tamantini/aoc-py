from src.solutions.shared.geometry import Direction, Turn, Vector2D
from src.solutions.y2019.d11.logic.hull_robot import HullRobot


def test_robot_turns_and_moves_one_step():
    robot = HullRobot(position=Vector2D(10, 20), direction=Direction.DOWN)
    new_bot = robot.turn_and_move(Turn.RIGHT)
    assert new_bot.direction == Direction.LEFT
    assert new_bot.position == Vector2D(9, 20)
