from dataclasses import dataclass

from src.solutions.y2015.d21.logic.fighter import Fighter


@dataclass(frozen=True)
class RpgItem:
    name: str
    cost: int
    damage: int
    armor: int


def equip_fighter(hit_points: int, items: list[RpgItem]) -> Fighter:
    total_damage = sum(item.damage for item in items)
    total_armor = sum(item.armor for item in items)

    return Fighter(
        hit_points=hit_points, damage=total_damage, armor=total_armor
    )
