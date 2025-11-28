from dataclasses import dataclass

from src.solutions.shared.graph import bfs
from src.solutions.y2019.d15.logic.oxygen_system_area import OxygenSystemArea


@dataclass(frozen=True)
class OxygenDistances:
    start_to_oxygen: int
    furthest_from_oxygen: int


def calculate_distances(area: OxygenSystemArea) -> OxygenDistances:
    start_to_oxygen = furthest_from_oxygen = 0
    for explored in bfs(
        start_node=area.oxygen_system_position, neighbors=area.neighbors
    ):
        if explored.node == area.droid_start_position:
            start_to_oxygen = explored.distance_to_start
        furthest_from_oxygen = max(
            furthest_from_oxygen, explored.distance_to_start
        )
    return OxygenDistances(start_to_oxygen, furthest_from_oxygen)
