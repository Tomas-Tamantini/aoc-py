from dataclasses import dataclass
from enum import Enum
from typing import Iterator


class HexagonalDirection(Enum):
    EAST = 0
    NORTHEAST = 2
    NORTHWEST = 3
    WEST = 4
    SOUTHWEST = 5
    SOUTHEAST = 6


@dataclass(frozen=True)
class HexagonalCoordinates:
    east: int
    northeast: int

    def move(self, direction: HexagonalDirection) -> "HexagonalCoordinates":
        offset = {
            HexagonalDirection.EAST: (1, 0),
            HexagonalDirection.NORTHEAST: (0, 1),
            HexagonalDirection.NORTHWEST: (-1, 1),
            HexagonalDirection.WEST: (-1, 0),
            HexagonalDirection.SOUTHWEST: (0, -1),
            HexagonalDirection.SOUTHEAST: (1, -1),
        }[direction]
        return HexagonalCoordinates(
            east=self.east + offset[0], northeast=self.northeast + offset[1]
        )

    def neighbors(self) -> Iterator["HexagonalCoordinates"]:
        for direction in HexagonalDirection:
            yield self.move(direction)
