from dataclasses import dataclass

from src.solutions.shared.geometry import Vector2D


@dataclass(frozen=True)
class Rectangle:
    corner_a: Vector2D
    corner_b: Vector2D

    @property
    def area(self) -> int:
        diff = self.corner_a - self.corner_b
        return (abs(diff.x) + 1) * (abs(diff.y) + 1)
