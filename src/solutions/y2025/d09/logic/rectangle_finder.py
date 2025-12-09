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

    def _horizontal_segment_passes_inside(
        self, x_start: int, x_end: int, y: int
    ) -> bool:
        return (
            self._min_y < y < self._max_y
            and x_end > self._min_x
            and x_start < self._max_x
        )

    def _vertical_segment_passes_inside(
        self, y_start: int, y_end: int, x: int
    ) -> bool:
        return (
            self._min_x < x < self._max_x
            and y_end > self._min_y
            and y_start < self._max_y
        )

    def segment_passes_inside(
        self, segment: tuple[Vector2D, Vector2D]
    ) -> bool:
        diff = segment[0] - segment[1]
        if diff.y == 0:
            return self._horizontal_segment_passes_inside(
                x_start=min(segment[0].x, segment[1].x),
                x_end=max(segment[0].x, segment[1].x),
                y=segment[0].y,
            )
        else:
            return self._vertical_segment_passes_inside(
                y_start=min(segment[0].y, segment[1].y),
                y_end=max(segment[0].y, segment[1].y),
                x=segment[0].x,
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
        num_rectangles = len(sorted_rectangles)
        step_granularity = 500
        for i, r in enumerate(sorted_rectangles):
            if self._is_inscribed(r):
                return r.area
            if progress_monitor:
                progress_monitor.update_progress_bar(
                    i, num_rectangles, step_granularity
                )
        raise ValueError("Could not find inscribed rectangle")
