from abc import abstractmethod
from typing import Hashable, TypeVar

from src.solutions.shared.cellular_automata.cellular_automaton import (
    CellularAutomaton,
)

T_Cell = TypeVar("T_Cell", bound=Hashable)


class BinaryCellularAutomaton(CellularAutomaton[T_Cell, bool]):
    def __init__(self, alive_cells: set[T_Cell]) -> None:
        cells = {c: True for c in alive_cells}
        super().__init__(cells, default_state=False)

    def alive_cells(self) -> set[T_Cell]:
        return {c for c, is_alive in self._cells.items() if is_alive}

    @abstractmethod
    def _cell_is_alive_on_next_iteration(
        self, current_cell_is_alive: bool, num_alive_neighbors: int
    ) -> bool: ...

    def _next_state(
        self, cell_state: bool, neighbor_count: dict[bool, int]
    ) -> bool:
        return self._cell_is_alive_on_next_iteration(
            current_cell_is_alive=cell_state,
            num_alive_neighbors=neighbor_count.get(True, 0),
        )

    def _is_alive(self, cell: T_Cell) -> bool:
        return self._get_state(cell)

    def _alive_cells_next_iteration(self) -> set[T_Cell]:
        return {c for c, is_alive in self._cells_next_iteration() if is_alive}
