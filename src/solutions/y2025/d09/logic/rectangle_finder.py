from functools import cache
from itertools import combinations

from src.solutions.shared.geometry import Vector2D


class _Rectangle:
    def __init__(self, corner_a: Vector2D, corner_b: Vector2D):
        self._corner_a = corner_a
        self._corner_b = corner_b
        self._max_x = max(self._corner_a.x, self._corner_b.x)
        self._min_x = min(self._corner_a.x, self._corner_b.x)
        self._max_y = max(self._corner_a.y, self._corner_b.y)
        self._min_y = min(self._corner_a.y, self._corner_b.y)

    @property
    def area(self) -> int:
        diff = self._corner_a - self._corner_b
        return (abs(diff.x) + 1) * (abs(diff.y) + 1)

    def intersects(self, other: "_Rectangle") -> bool:
        return (
            other._max_x > self._min_x
            and other._min_x < self._max_x
            and other._max_y > self._min_y
            and other._min_y < self._max_y
        )


class RectangleFinder:
    def __init__(self, polygon_vertices: list[Vector2D]):
        self._vertices = polygon_vertices

    @cache
    def _sorted_rectangles(self) -> list[_Rectangle]:
        rectangles = [
            _Rectangle(*corners) for corners in combinations(self._vertices, 2)
        ]
        return sorted(rectangles, key=lambda r: -r.area)

    @cache
    def _edges(self) -> list[_Rectangle]:
        edges = []
        for i in range(len(self._vertices)):
            v1 = self._vertices[i]
            v2 = self._vertices[(i + 1) % len(self._vertices)]
            edges.append(_Rectangle(v1, v2))
        return edges

    def largest_rectangle_area(self) -> int:
        return self._sorted_rectangles()[0].area

    def _is_inscribed(self, rectangle: _Rectangle) -> bool:
        return not any(rectangle.intersects(edge) for edge in self._edges())

    def largest_inscribed_rectangle_area(self) -> int:
        for r in self._sorted_rectangles():
            if self._is_inscribed(r):
                return r.area
        raise ValueError("Could not find inscribed rectangle")
