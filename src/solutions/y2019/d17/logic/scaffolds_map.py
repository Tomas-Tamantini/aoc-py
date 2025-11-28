from dataclasses import dataclass
from typing import Iterator

from src.solutions.shared.geometry import Vector2D
from src.solutions.y2019.d17.logic.vacuum_robot import VacuumRobot


@dataclass(frozen=True)
class ScaffoldsMap:
    tiles: set[Vector2D]
    robot_start: VacuumRobot

    def _num_neighbors(self, tile: Vector2D) -> int:
        return sum(n in self.tiles for n in tile.neighbors())

    def intersections(self) -> Iterator[Vector2D]:
        for tile in self.tiles:
            if self._num_neighbors(tile) > 2:
                yield tile
