from abc import ABC, abstractmethod
from collections import defaultdict
from typing import Generic, Hashable, Iterator, TypeVar

T_Cell = TypeVar("T_Cell", bound=Hashable)
T_CellState = TypeVar("T_CellState")


class CellularAutomaton(ABC, Generic[T_Cell, T_CellState]):
    def __init__(
        self, cells: dict[T_Cell, T_CellState], default_state: T_CellState
    ) -> None:
        self._cells = cells
        self._default_state = default_state

    @abstractmethod
    def _neighbors(self, cell: T_Cell) -> Iterator[T_Cell]: ...

    @abstractmethod
    def _next_state(
        self, cell_state: T_CellState, neighbor_count: dict[T_CellState, int]
    ) -> T_CellState: ...

    def _get_state(self, cell: T_Cell) -> T_CellState:
        return self._cells.get(cell, self._default_state)

    def __neighbor_count(self) -> dict[T_Cell, dict[T_CellState, int]]:
        neighbor_count = dict()
        for cell, cell_state in self._cells.items():
            if cell_state == self._default_state:
                continue
            if cell not in neighbor_count:
                neighbor_count[cell] = defaultdict(int)
            for neighbor in self._neighbors(cell):
                if neighbor not in neighbor_count:
                    neighbor_count[neighbor] = defaultdict(int)
                neighbor_count[neighbor][cell_state] += 1
        return neighbor_count

    def _cells_next_iteration(self) -> Iterator[tuple[T_Cell, T_CellState]]:
        neighbor_count = self.__neighbor_count()
        for cell, count in neighbor_count.items():
            next_state = self._next_state(self._get_state(cell), count)
            if next_state != self._default_state:
                yield cell, next_state
