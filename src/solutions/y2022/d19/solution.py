from math import prod

from src.core.io_handler import IOHandler
from src.solutions.y2022.d19.logic.parser import parse_blueprints
from src.solutions.y2022.d19.logic.resource import ResourceType
from src.solutions.y2022.d19.logic.resource_optimization import (
    maximize_resource,
)


def solve(io_handler: IOHandler) -> None:
    prob_id = 2022, 19
    blueprints = list(parse_blueprints(io_handler.input_reader(*prob_id)))
    initial_fleet = {ResourceType.ORE: 1}

    progress_p1 = io_handler.progress_monitor(*prob_id, part=1)
    quality_sum = 0
    for bp in progress_p1.track(blueprints):
        quality_sum += bp.id * maximize_resource(
            resource_to_maximize=ResourceType.GEODE,
            time_limit=24,
            blueprint=bp,
            initial_fleet=initial_fleet,
        )
    io_handler.write_result(*prob_id, part=1, result=quality_sum)

    candidates = blueprints[:3]
    progress_p2 = io_handler.progress_monitor(*prob_id, part=2)
    geodes = []
    for bp in progress_p2.track(candidates):
        geodes.append(
            maximize_resource(
                resource_to_maximize=ResourceType.GEODE,
                time_limit=32,
                blueprint=bp,
                initial_fleet=initial_fleet,
            )
        )
    io_handler.write_result(*prob_id, part=2, result=prod(geodes))
