from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class ResultReport:
    year: int
    day: int
    part: int
    received: str
    expected: str

    @property
    def result_is_correct(self) -> bool:
        if not self.expected:
            return False
        return self.received == self.expected


class ResultChecker(Protocol):
    def check_result(
        self, year: int, day: int, part: int, result: str
    ) -> ResultReport: ...
