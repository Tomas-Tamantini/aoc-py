from src.solutions.y2019.d11.logic.hull import Hull
from src.solutions.y2019.d11.logic.hull_robot import HullRobot
from src.solutions.y2019.d11.logic.hull_robot_io import HullRobotIO
from src.solutions.y2019.intcode import IntcodeProgram, run_intcode_program


def run_paint_hull_program(
    instructions: list[int], hull: Hull, robot: HullRobot
) -> None:
    io = HullRobotIO(hull=hull, robot=robot)
    program = IntcodeProgram(instructions)
    run_intcode_program(program, serial_output=io, serial_input=io)
