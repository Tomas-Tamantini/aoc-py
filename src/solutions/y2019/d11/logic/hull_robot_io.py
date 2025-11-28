from src.solutions.shared.geometry.direction import Turn
from src.solutions.y2019.d11.logic.hull import Hull
from src.solutions.y2019.d11.logic.hull_robot import HullRobot


class HullRobotIO:
    def __init__(self, hull: Hull, robot: HullRobot) -> None:
        self._hull = hull
        self._robot = robot
        self._is_paint_instruction = True

    def read_next(self) -> int:
        return int(self._robot.position in self._hull.white_panels)

    def put(self, value: int) -> None:
        if self._is_paint_instruction:
            paint_white = value == 1
            self._hull.paint_panel(self._robot.position, paint_white)
        else:
            turn = Turn.RIGHT if value else Turn.LEFT
            self._robot = self._robot.turn_and_move(turn)
        self._is_paint_instruction = not self._is_paint_instruction
