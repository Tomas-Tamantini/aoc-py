from dataclasses import dataclass


@dataclass(frozen=True)
class Interval:
    min_inclusive: int
    max_inclusive: int

    def contains(self, number: int) -> bool:
        return self.min_inclusive <= number <= self.max_inclusive
