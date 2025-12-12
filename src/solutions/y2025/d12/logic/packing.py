from dataclasses import dataclass

from src.solutions.shared.geometry import Vector2D


@dataclass(frozen=True)
class Shape:
    id: int
    cells: set[Vector2D]


@dataclass(frozen=True)
class Region:
    width: int
    height: int
    shape_requirements: dict[int, int]
