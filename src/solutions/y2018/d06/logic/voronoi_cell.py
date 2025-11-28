from dataclasses import dataclass

from src.solutions.shared.geometry import Vector2D


@dataclass(frozen=True)
class VoronoiCell:
    seed: Vector2D
    area: int
