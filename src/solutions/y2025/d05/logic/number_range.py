from dataclasses import dataclass


@dataclass(frozen=True)
class NumberRange:
    min_inclusive: int
    max_inclusive: int

    def contains(self, n: int):
        return self.min_inclusive <= n <= self.max_inclusive
