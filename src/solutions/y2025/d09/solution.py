from itertools import combinations

from src.core.io_handler import IOHandler
from src.solutions.shared.geometry import Vector2D
from src.solutions.shared.parser import parse_csv
from src.solutions.y2025.d09.logic.rectangle import Rectangle


def solve(io_handler: IOHandler) -> None:
    prob_id = 2025, 9

    positions = list(
        parse_csv(
            io_handler.input_reader(*prob_id),
            mapper=lambda values: Vector2D(*map(int, values)),
        )
    )

    rectangles = sorted(
        [Rectangle(*corners) for corners in combinations(positions, 2)],
        key=lambda r: -r.area,
    )

    max_area = rectangles[0].area

    io_handler.write_result(*prob_id, part=1, result=max_area)
    io_handler.write_result(*prob_id, part=2, result="not implemented")
