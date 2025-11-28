from dataclasses import dataclass
from enum import Enum


class Character(Enum):
    PLAYER = 1
    BOSS = 2


@dataclass(frozen=True)
class CharacterState:
    id: Character
    hit_points: int
    mana_points: int = 0
