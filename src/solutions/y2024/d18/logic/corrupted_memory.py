from functools import partial
from typing import Iterator

from src.solutions.shared.geometry import Vector2D
from src.solutions.shared.graph import min_path_length_with_bfs


class CorruptedMemory:
    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height
        self._end_position = Vector2D(self._width - 1, self._height - 1)

    def _is_within_bounds(self, cell: Vector2D) -> bool:
        return 0 <= cell.x < self._width and 0 <= cell.y < self._height

    def _neighbors(
        self, node: Vector2D, corrupted_positions: set[Vector2D]
    ) -> Iterator[Vector2D]:
        for n in node.neighbors():
            if self._is_within_bounds(n) and n not in corrupted_positions:
                yield n

    def shortest_path_length(self, corrupted_positions: set[Vector2D]) -> int:
        return min_path_length_with_bfs(
            start_node=Vector2D(0, 0),
            is_final_state=lambda p: p == self._end_position,
            neighbors=partial(
                self._neighbors, corrupted_positions=corrupted_positions
            ),
        )

    def _path_exists(self, corrupted_positions: set[Vector2D]) -> bool:
        try:
            _ = self.shortest_path_length(corrupted_positions)
            return True
        except ValueError:
            return False

    def idx_of_first_blocking_byte(
        self, corrupted_positions: list[Vector2D]
    ) -> int:
        lb = 0
        ub = len(corrupted_positions)
        while lb < ub:
            mid = (lb + ub) // 2
            positions = set(corrupted_positions[:mid])
            if self._path_exists(positions):
                lb = mid + 1
            else:
                ub = mid
        return lb - 1
