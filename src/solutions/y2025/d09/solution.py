from src.core.io_handler import IOHandler
from src.solutions.shared.geometry import Vector2D
from src.solutions.shared.parser import parse_csv
from src.solutions.y2025.d09.logic.rectangle_finder import RectangleFinder


def solve(io_handler: IOHandler) -> None:
    prob_id = 2025, 9

    vertices = list(
        parse_csv(
            io_handler.input_reader(*prob_id),
            mapper=lambda values: Vector2D(*map(int, values)),
        )
    )
    rectangle_finder = RectangleFinder(vertices)

    max_area_p1 = rectangle_finder.largest_rectangle_area()
    io_handler.write_result(*prob_id, part=1, result=max_area_p1)

    io_handler.write_result(*prob_id, part=2, result="not implemented")
