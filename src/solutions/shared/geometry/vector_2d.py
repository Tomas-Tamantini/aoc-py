from dataclasses import dataclass
from typing import Iterator

from src.solutions.shared.geometry.direction import Direction


@dataclass(frozen=True, order=True)
class Vector2D:
    x: int
    y: int

    def __sub__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x - other.x, self.y - other.y)

    def __add__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x + other.x, self.y + other.y)

    def __floordiv__(self, scalar: int) -> "Vector2D":
        return Vector2D(self.x // scalar, self.y // scalar)

    def manhattan_size(self) -> int:
        return abs(self.x) + abs(self.y)

    def manhattan_distance(self, other: "Vector2D") -> int:
        return (self - other).manhattan_size()

    def neighbors(
        self, include_diagonals: bool = False
    ) -> Iterator["Vector2D"]:
        for direction in Direction:
            yield self.move(direction)
        if include_diagonals:
            for dx in (-1, 1):
                for dy in (-1, 1):
                    yield Vector2D(self.x + dx, self.y + dy)

    def move(self, direction: Direction, num_steps: int = 1) -> "Vector2D":
        if direction == Direction.RIGHT:
            return Vector2D(self.x + num_steps, self.y)
        elif direction == Direction.LEFT:
            return Vector2D(self.x - num_steps, self.y)
        elif direction == Direction.UP:
            return Vector2D(self.x, self.y + num_steps)
        else:
            return Vector2D(self.x, self.y - num_steps)

    def normalized(self) -> "Vector2D":
        if self.x != 0:
            if self.y != 0:
                raise ValueError("Cannot normalize a diagonal vector")
            else:
                return Vector2D(self.x // abs(self.x), 0)
        elif self.y != 0:
            return Vector2D(0, self.y // abs(self.y))
        else:
            raise ValueError("Cannot normalize a zero vector")
