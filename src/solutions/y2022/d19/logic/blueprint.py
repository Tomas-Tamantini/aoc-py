from dataclasses import dataclass

from src.solutions.y2022.d19.logic.resource import ResourceType


@dataclass(frozen=True)
class Blueprint:
    id: int
    costs: dict[ResourceType, dict[ResourceType, int]]
