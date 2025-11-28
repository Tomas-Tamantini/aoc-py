from dataclasses import dataclass


@dataclass(frozen=True)
class BossStats:
    hit_points: int
    damage: int
