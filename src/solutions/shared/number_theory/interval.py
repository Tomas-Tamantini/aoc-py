from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Interval:
    min_inclusive: int
    max_inclusive: int

    def contains(self, number: int) -> bool:
        return self.min_inclusive <= number <= self.max_inclusive

    def intersects(self, other: "Interval") -> bool:
        return max(self.min_inclusive, other.min_inclusive) <= min(
            self.max_inclusive, other.max_inclusive
        )
