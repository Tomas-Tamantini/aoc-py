from dataclasses import dataclass
from typing import Iterator

from src.solutions.shared.geometry import Vector2D


@dataclass(frozen=True)
class OxygenSystemArea:
    droid_start_position: Vector2D
    oxygen_system_position: Vector2D
    tiles: set[Vector2D]

    def neighbors(self, position: Vector2D) -> Iterator[Vector2D]:
        for neighbor in position.neighbors():
            if neighbor in self.tiles:
                yield neighbor
