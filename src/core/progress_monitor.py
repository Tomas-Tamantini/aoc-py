from typing import Iterable, Iterator, Protocol, TypeVar

T = TypeVar("T")


class ProgressMonitor(Protocol):
    def estimate_remaining_time(self, estimation: str) -> None: ...

    def track(self, steps: Iterable[T]) -> Iterator[T]: ...
