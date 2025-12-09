from itertools import combinations

from src.core.io_handler import IOHandler
from src.solutions.shared.geometry import Vector2D
from src.solutions.shared.parser import parse_csv


def _rectangle_area(corner_a: Vector2D, corner_b: Vector2D) -> int:
    diff = corner_a - corner_b
    return (abs(diff.x) + 1) * (abs(diff.y) + 1)


def solve(io_handler: IOHandler) -> None:
    prob_id = 2025, 9

    positions = list(
        parse_csv(
            io_handler.input_reader(*prob_id),
            mapper=lambda values: Vector2D(*map(int, values)),
        )
    )

    max_area = max(
        _rectangle_area(*corners) for corners in combinations(positions, 2)
    )

    io_handler.write_result(*prob_id, part=1, result=max_area)
    io_handler.write_result(*prob_id, part=2, result="not implemented")
