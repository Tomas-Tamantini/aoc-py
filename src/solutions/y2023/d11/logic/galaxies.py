from dataclasses import dataclass
from enum import Enum
from functools import cache
from typing import Iterator

from src.solutions.shared.geometry import Vector2D


class _Direction(Enum):
    HORIZONTAL = 1
    VERTICAL = 2


@dataclass(frozen=True)
class _Displacement:
    occupied_steps: int
    empty_steps: int

    def distance(self, expansion_rate: int) -> int:
        return self.occupied_steps + expansion_rate * self.empty_steps

    def __add__(self, other: "_Displacement") -> "_Displacement":
        return _Displacement(
            occupied_steps=self.occupied_steps + other.occupied_steps,
            empty_steps=self.empty_steps + other.empty_steps,
        )

    def __sub__(self, other: "_Displacement") -> "_Displacement":
        return _Displacement(
            occupied_steps=self.occupied_steps - other.occupied_steps,
            empty_steps=self.empty_steps - other.empty_steps,
        )


class Galaxies:
    def __init__(self, positions: set[Vector2D]):
        self._positions = positions
        self._occupied_columns = {p.x for p in positions}
        self._occupied_rows = {p.y for p in positions}

    def positions(self) -> Iterator[Vector2D]:
        yield from self._positions

    def _is_occupied(self, coord: int, direction: _Direction) -> bool:
        if direction == _Direction.HORIZONTAL:
            return coord in self._occupied_columns
        else:
            return coord in self._occupied_rows

    @cache
    def _displacement_until(self, coord: int, direction: _Direction):
        if coord == 0:
            return _Displacement(0, 0)
        elif self._is_occupied(coord, direction):
            return _Displacement(1, 0) + self._displacement_until(
                coord - 1, direction
            )
        else:
            return _Displacement(0, 1) + self._displacement_until(
                coord - 1, direction
            )

    def _linear_displacement(
        self, coord_a: int, coord_b: int, direction: _Direction
    ) -> _Displacement:
        coord_start, coord_end = min(coord_a, coord_b), max(coord_a, coord_b)
        to_start = self._displacement_until(coord_start, direction)
        to_end = self._displacement_until(coord_end, direction)
        return to_end - to_start

    def _displacement(self, pos_a: Vector2D, pos_b: Vector2D) -> _Displacement:
        dx = self._linear_displacement(pos_a.x, pos_b.x, _Direction.HORIZONTAL)
        dy = self._linear_displacement(pos_a.y, pos_b.y, _Direction.VERTICAL)
        return dx + dy

    def distance(
        self, pos_a: Vector2D, pos_b: Vector2D, expansion_rate: int
    ) -> int:
        displacement = self._displacement(pos_a, pos_b)
        return displacement.distance(expansion_rate)
