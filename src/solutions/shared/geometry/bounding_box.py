from typing import Iterable

from src.solutions.shared.geometry.vector_2d import Vector2D


class BoundingBox:
    def __init__(self, points: Iterable[Vector2D]) -> None:
        self._min_x = self._max_x = self._min_y = self._max_y = 0
        for i, point in enumerate(points):
            if i == 0:
                self._max_x = self._min_x = point.x
                self._max_y = self._min_y = point.y
            else:
                self._max_x = max(self._max_x, point.x)
                self._min_x = min(self._min_x, point.x)
                self._max_y = max(self._max_y, point.y)
                self._min_y = min(self._min_y, point.y)

    @property
    def min_x(self) -> int:
        return self._min_x

    @property
    def max_x(self) -> int:
        return self._max_x

    @property
    def min_y(self) -> int:
        return self._min_y

    @property
    def max_y(self) -> int:
        return self._max_y

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BoundingBox):
            return NotImplemented
        return (
            self._min_x == other._min_x
            and self._max_x == other._max_x
            and self._min_y == other._min_y
            and self._max_y == other._max_y
        )

    def __hash__(self) -> int:
        return hash((self._min_x, self._max_x, self._min_y, self._max_y))
