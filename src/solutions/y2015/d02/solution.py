from src.core.io_handler import IOHandler
from src.solutions.y2015.d02.logic.parser import parse_rectangular_boxes


def solve(io_handler: IOHandler) -> None:
    prob_id = 2015, 2

    boxes = list(parse_rectangular_boxes(io_handler.input_reader(*prob_id)))

    wrapping_paper = sum(box.required_wrapping_paper() for box in boxes)
    io_handler.write_result(*prob_id, part=1, result=wrapping_paper)

    ribbon_length = sum(box.required_ribbon_length() for box in boxes)
    io_handler.write_result(*prob_id, part=2, result=ribbon_length)
