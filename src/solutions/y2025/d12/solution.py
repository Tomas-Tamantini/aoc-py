from src.core.io_handler import IOHandler
from src.solutions.y2025.d12.logic.parser import (
    parse_packing_regions,
    parse_shapes,
)


def solve(io_handler: IOHandler) -> None:
    prob_id = 2025, 12

    reader = io_handler.input_reader(*prob_id)

    shapes = {s.id: s for s in parse_shapes(reader)}
    regions = list(parse_packing_regions(reader))

    num_regions = sum(r.can_be_packed(shapes) for r in regions)

    io_handler.write_result(*prob_id, part=1, result=num_regions)
