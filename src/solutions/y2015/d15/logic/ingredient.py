from dataclasses import dataclass


@dataclass(frozen=True)
class Ingredient:
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int
