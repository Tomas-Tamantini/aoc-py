from typing import Iterator

from src.solutions.shared.geometry import Direction, Vector2D


class ParabolicDish:
    def __init__(
        self,
        width: int,
        height: int,
        cube_rock_positions: set[Vector2D],
        rounded_rock_positions: set[Vector2D],
    ) -> None:
        self._width = width
        self._height = height
        self._cube_rock_positions = cube_rock_positions
        self._rounded_rock_positions = rounded_rock_positions

    @property
    def rounded_rock_positions(self) -> set[Vector2D]:
        return self._rounded_rock_positions

    def _roll_inside_slice(
        self, start_pos: Vector2D, end_pos: Vector2D
    ) -> Iterator[Vector2D]:
        free_pos = start_pos
        offset = (end_pos - start_pos).normalized()
        pos = start_pos
        while pos != end_pos + offset:
            if pos in self._rounded_rock_positions:
                yield free_pos
                free_pos += offset
            elif pos in self._cube_rock_positions:
                free_pos = pos + offset
            pos += offset

    def _roll_rounded_rocks_in_row(
        self, row: int, direction: Direction
    ) -> Iterator[Vector2D]:
        start_col, end_col = (
            (0, self._width - 1)
            if direction == Direction.LEFT
            else (self._width - 1, 0)
        )
        yield from self._roll_inside_slice(
            start_pos=Vector2D(start_col, row), end_pos=Vector2D(end_col, row)
        )

    def _roll_rounded_rocks_in_column(
        self, col: int, direction: Direction
    ) -> Iterator[Vector2D]:
        start_row, end_row = (
            (0, self._height - 1)
            if direction == Direction.DOWN
            else (self._height - 1, 0)
        )
        yield from self._roll_inside_slice(
            start_pos=Vector2D(col, start_row), end_pos=Vector2D(col, end_row)
        )

    def _roll_rounded_rocks(self, direction: Direction) -> Iterator[Vector2D]:
        if direction.is_horizontal:
            for row in range(self._height):
                yield from self._roll_rounded_rocks_in_row(row, direction)
        else:
            for col in range(self._width):
                yield from self._roll_rounded_rocks_in_column(col, direction)

    def tilt(self, direction: Direction) -> "ParabolicDish":
        return ParabolicDish(
            width=self._width,
            height=self._height,
            cube_rock_positions=self._cube_rock_positions,
            rounded_rock_positions=set(self._roll_rounded_rocks(direction)),
        )

    def __hash__(self) -> int:
        return hash(frozenset(self._rounded_rock_positions))

    def __eq__(self, other: object) -> bool:
        return self._rounded_rock_positions == other._rounded_rock_positions  # type: ignore
