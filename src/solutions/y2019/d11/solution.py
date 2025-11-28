from src.core.io_handler import IOHandler
from src.solutions.shared.geometry import Direction, Vector2D
from src.solutions.y2019.d11.logic.hull import Hull
from src.solutions.y2019.d11.logic.hull_robot import HullRobot
from src.solutions.y2019.d11.logic.render_hull import render_hull
from src.solutions.y2019.d11.logic.run_hull_program import (
    run_paint_hull_program,
)
from src.solutions.y2019.intcode import parse_instructions


def solve(io_handler: IOHandler) -> None:
    prob_id = 2019, 11
    instructions = parse_instructions(io_handler.input_reader(*prob_id))
    inital_bot = HullRobot(position=Vector2D(0, 0), direction=Direction.UP)

    hull = Hull()
    run_paint_hull_program(instructions, hull, inital_bot)
    io_handler.write_result(
        *prob_id, part=1, result=hull.num_panels_painted_at_least_once
    )

    hull = Hull()
    hull.paint_panel(position=inital_bot.position, paint_white=True)
    run_paint_hull_program(instructions, hull, inital_bot)
    io_handler.write_result(*prob_id, part=2, result=render_hull(hull))
