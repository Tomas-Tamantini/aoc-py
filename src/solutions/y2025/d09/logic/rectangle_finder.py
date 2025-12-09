from dataclasses import dataclass
from itertools import combinations

from src.solutions.shared.geometry import Vector2D


@dataclass(frozen=True)
class _Rectangle:
    corner_a: Vector2D
    corner_b: Vector2D

    @property
    def area(self) -> int:
        diff = self.corner_a - self.corner_b
        return (abs(diff.x) + 1) * (abs(diff.y) + 1)


class RectangleFinder:
    def __init__(self, polygon_vertices: list[Vector2D]):
        self._vertices = polygon_vertices

    def largest_rectangle_area(self) -> int:
        rectangles = (
            _Rectangle(*corners) for corners in combinations(self._vertices, 2)
        )
        return max(r.area for r in rectangles)
