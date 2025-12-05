from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True, order=True)
class Interval:
    min_inclusive: int
    max_inclusive: int

    @property
    def size(self) -> int:
        return self.max_inclusive - self.min_inclusive + 1

    def contains(self, number: int) -> bool:
        return self.min_inclusive <= number <= self.max_inclusive

    def union(self, other: "Interval") -> Optional["Interval"]:
        if (
            other.min_inclusive > self.max_inclusive + 1
            or self.min_inclusive > other.max_inclusive + 1
        ):
            return None
        else:
            return Interval(
                min(self.min_inclusive, other.min_inclusive),
                max(self.max_inclusive, other.max_inclusive),
            )
