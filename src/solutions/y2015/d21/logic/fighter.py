from dataclasses import dataclass


@dataclass(frozen=True)
class Fighter:
    hit_points: int
    damage: int
    armor: int
