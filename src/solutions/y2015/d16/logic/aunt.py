from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class Aunt:
    id: int
    attributes: dict[str, int]


class ConstraintType(Enum):
    EQUAL = 1
    GREATER_THAN = 2
    LESS_THAN = 3


@dataclass(frozen=True)
class Constraint:
    element: str
    constraint_type: ConstraintType
    value: int

    def is_satisfied(self, aunt: Aunt) -> bool:
        if self.element not in aunt.attributes:
            return True

        attribute_value = aunt.attributes[self.element]
        if self.constraint_type == ConstraintType.EQUAL:
            return attribute_value == self.value
        elif self.constraint_type == ConstraintType.GREATER_THAN:
            return attribute_value > self.value
        else:
            return attribute_value < self.value


def matching_aunt(aunts: list[Aunt], constraints: list[Constraint]) -> Aunt:
    return next(
        aunt
        for aunt in aunts
        if all(constraint.is_satisfied(aunt) for constraint in constraints)
    )
