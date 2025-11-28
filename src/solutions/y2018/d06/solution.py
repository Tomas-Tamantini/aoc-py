from src.core.io_handler import IOHandler
from src.solutions.shared.geometry import Vector2D
from src.solutions.shared.parser import parse_csv
from src.solutions.y2018.d06.logic.voronoi import Voronoi


def solve(io_handler: IOHandler) -> None:
    prob_id = 2018, 6
    seeds = set(
        parse_csv(
            io_handler.input_reader(*prob_id),
            mapper=lambda v: Vector2D(*map(int, v)),
        )
    )
    voronoi = Voronoi(seeds)

    max_area = max(cell.area for cell in voronoi.finite_cells())
    io_handler.write_result(*prob_id, part=1, result=int(max_area))

    io_handler.progress_monitor(*prob_id, part=2).estimate_remaining_time(
        estimation="5s"
    )

    safe_area = voronoi.safe_area(sum_dist_less_than=10_000)
    io_handler.write_result(*prob_id, part=2, result=safe_area)
