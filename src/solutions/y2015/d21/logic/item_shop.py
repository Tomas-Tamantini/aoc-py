from dataclasses import dataclass
from itertools import combinations, product
from typing import Iterator

from src.solutions.y2015.d21.logic.rpg_item import RpgItem


@dataclass(frozen=True)
class ItemClass:
    items: list[RpgItem]
    min_num_items: int
    max_num_items: int

    def combinations(self) -> Iterator[list[RpgItem]]:
        for num_items in range(self.min_num_items, self.max_num_items + 1):
            for combo in combinations(self.items, num_items):
                yield list(combo)


class ItemShop:
    def __init__(self, *item_classes: ItemClass):
        self._item_classes = item_classes

    def item_combinations(self) -> Iterator[list[RpgItem]]:
        for item_class_combos in product(
            *[item_class.combinations() for item_class in self._item_classes]
        ):
            yield [item for combo in item_class_combos for item in combo]


def default_item_shop() -> ItemShop:
    weapons = ItemClass(
        items=[
            RpgItem(name="Dagger", cost=8, damage=4, armor=0),
            RpgItem(name="Shortsword", cost=10, damage=5, armor=0),
            RpgItem(name="Warhammer", cost=25, damage=6, armor=0),
            RpgItem(name="Longsword", cost=40, damage=7, armor=0),
            RpgItem(name="Greataxe", cost=74, damage=8, armor=0),
        ],
        min_num_items=1,
        max_num_items=1,
    )

    armors = ItemClass(
        items=[
            RpgItem(name="Leather", cost=13, damage=0, armor=1),
            RpgItem(name="Chainmail", cost=31, damage=0, armor=2),
            RpgItem(name="Splintmail", cost=53, damage=0, armor=3),
            RpgItem(name="Bandedmail", cost=75, damage=0, armor=4),
            RpgItem(name="Platemail", cost=102, damage=0, armor=5),
        ],
        min_num_items=0,
        max_num_items=1,
    )

    rings = ItemClass(
        items=[
            RpgItem(name="Damage +1", cost=25, damage=1, armor=0),
            RpgItem(name="Damage +2", cost=50, damage=2, armor=0),
            RpgItem(name="Damage +3", cost=100, damage=3, armor=0),
            RpgItem(name="Defense +1", cost=20, damage=0, armor=1),
            RpgItem(name="Defense +2", cost=40, damage=0, armor=2),
            RpgItem(name="Defense +3", cost=80, damage=0, armor=3),
        ],
        min_num_items=0,
        max_num_items=2,
    )

    return ItemShop(weapons, armors, rings)
