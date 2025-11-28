from src.core.io_handler import IOHandler
from src.solutions.y2019.d15.logic.explore_area import (
    explore_oxygem_system_area,
)
from src.solutions.y2019.d15.logic.oxygen_distances import calculate_distances
from src.solutions.y2019.d15.logic.repair_droid_io import RepairDroidIO
from src.solutions.y2019.intcode import parse_instructions


def solve(io_handler: IOHandler) -> None:
    prob_id = 2019, 15

    instructions = parse_instructions(io_handler.input_reader(*prob_id))
    droid_io = RepairDroidIO(instructions)

    animation_renderer = io_handler.animation_renderer(*prob_id, part=1)
    area = explore_oxygem_system_area(droid_io, animation_renderer)
    distances = calculate_distances(area)

    io_handler.write_result(
        *prob_id,
        part=1,
        result=distances.start_to_oxygen,
        supports_animation=True,
    )
    io_handler.write_result(
        *prob_id, part=2, result=distances.furthest_from_oxygen
    )
