from dataclasses import dataclass
from itertools import combinations
from typing import Iterator, Optional

from src.core.progress_monitor import ProgressMonitor
from src.solutions.shared.geometry import Vector2D


@dataclass(frozen=True)
class _Rectangle:
    corner_a: Vector2D
    corner_b: Vector2D

    @property
    def area(self) -> int:
        diff = self.corner_a - self.corner_b
        return (abs(diff.x) + 1) * (abs(diff.y) + 1)

    @property
    def _max_x(self) -> int:
        return max(self.corner_a.x, self.corner_b.x)

    @property
    def _min_x(self) -> int:
        return min(self.corner_a.x, self.corner_b.x)

    @property
    def _max_y(self) -> int:
        return max(self.corner_a.y, self.corner_b.y)

    @property
    def _min_y(self) -> int:
        return min(self.corner_a.y, self.corner_b.y)

    def segment_passes_inside(
        self, segment: tuple[Vector2D, Vector2D]
    ) -> bool:
        other = _Rectangle(*segment)
        return (
            other._max_x > self._min_x
            and other._min_x < self._max_x
            and other._max_y > self._min_y
            and other._min_y < self._max_y
        )


class RectangleFinder:
    def __init__(self, polygon_vertices: list[Vector2D]):
        self._vertices = polygon_vertices

    def _rectangles(self) -> Iterator[_Rectangle]:
        for corners in combinations(self._vertices, 2):
            yield _Rectangle(*corners)

    def _edges(self) -> Iterator[tuple[Vector2D, Vector2D]]:
        for i in range(len(self._vertices)):
            v1 = self._vertices[i]
            v2 = self._vertices[(i + 1) % len(self._vertices)]
            yield v1, v2

    def largest_rectangle_area(self) -> int:
        return max(r.area for r in self._rectangles())

    def _is_inscribed(self, rectangle: _Rectangle) -> bool:
        return not any(
            rectangle.segment_passes_inside(edge) for edge in self._edges()
        )

    def largest_inscribed_rectangle_area(
        self, progress_monitor: Optional[ProgressMonitor] = None
    ) -> int:
        sorted_rectangles = sorted(self._rectangles(), key=lambda r: -r.area)
        for i, r in enumerate(sorted_rectangles):
            if self._is_inscribed(r):
                return r.area
            if progress_monitor:
                progress_monitor.update_progress_bar(
                    i, len(sorted_rectangles), step_granularity=500
                )
        raise ValueError("Could not find inscribed rectangle")
