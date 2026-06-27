from typing import Iterable, Iterator, Optional, TypeVar

T = TypeVar("T")


class CLIProgressMonitor:
    def __init__(self, year: int, day: int, part: int) -> None:
        self._year = year
        self._day = day
        self._part = part

    def _problem_id(self) -> str:
        return f"AOC {self._year}/{self._day:02d} - Part {self._part}"

    def estimate_remaining_time(self, estimation: str) -> None:
        msg = (
            f"{self._problem_id()}: Be patient, "
            f"it takes about {estimation} to run"
        )
        print(msg, end="\r")

    @staticmethod
    def _progress_bar(current_step: int, total_steps: Optional[int]) -> str:
        if not total_steps:
            return f"({current_step}/?)"
        progress = (current_step / total_steps) * 100
        bar_length = 40
        filled_length = int(bar_length * progress // 100)
        bar = "█" * filled_length + "-" * (bar_length - filled_length)
        return f"[{bar}] {progress:.2f}% ({current_step}/{total_steps})"

    def track(self, steps: Iterable[T]) -> Iterator[T]:
        total_steps = len(steps) if hasattr(steps, "__len__") else None  # type: ignore
        resolution = 1 if total_steps is None else max(1, total_steps // 100)
        for i, step in enumerate(steps):
            if i % resolution == 0:
                bar = self._progress_bar(i, total_steps)
                print(f"{self._problem_id()}: {bar}", end="\r")
            yield step
