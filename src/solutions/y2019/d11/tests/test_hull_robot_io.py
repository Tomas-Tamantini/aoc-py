from src.solutions.shared.geometry import Direction, Vector2D
from src.solutions.y2019.d11.logic.hull import Hull
from src.solutions.y2019.d11.logic.hull_robot import HullRobot
from src.solutions.y2019.d11.logic.hull_robot_io import HullRobotIO


def _hull(white_panel_at_origin: bool = False) -> Hull:
    hull = Hull()
    if white_panel_at_origin:
        hull.paint_panel(position=Vector2D(0, 0), paint_white=True)
    return hull


def _robot() -> HullRobot:
    return HullRobot(position=Vector2D(0, 0), direction=Direction.UP)


def test_hull_robot_io_reads_zero_if_robot_is_on_black_panel():
    io = HullRobotIO(hull=_hull(), robot=_robot())
    assert io.read_next() == 0


def test_hull_robot_io_reads_one_if_robot_is_on_white_panel():
    io = HullRobotIO(hull=_hull(white_panel_at_origin=True), robot=_robot())
    assert io.read_next() == 1


def test_hull_robot_io_uses_output_to_paint_and_move():
    hull = _hull()
    robot = _robot()
    io = HullRobotIO(hull, robot)
    io.put(1)  # Paint white
    io.put(1)  # Turn right and move
    io.put(0)  # paint black
    io.put(0)  # Turn left and move
    io.put(1)  # Paint white
    assert hull.white_panels == {Vector2D(0, 0), Vector2D(1, 1)}
