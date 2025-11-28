from enum import Enum
from typing import Iterator

from src.solutions.shared.cellular_automata.cellular_automaton import (
    CellularAutomaton,
)
from src.solutions.shared.geometry import Vector2D


class WireWorldState(Enum):
    EMPTY = 0
    ELECTRON_HEAD = 1
    ELECTRON_TAIL = 2
    CONDUCTOR = 3


class WireWorld(CellularAutomaton[Vector2D, WireWorldState]):
    def __init__(self, cells: dict[Vector2D, WireWorldState]):
        super().__init__(cells, default_state=WireWorldState.EMPTY)

    @property
    def cells(self) -> dict[Vector2D, WireWorldState]:
        return self._cells

    def _neighbors(self, cell: Vector2D) -> Iterator[Vector2D]:  # noqa: PLR6301
        yield from cell.neighbors(include_diagonals=True)

    def _num_electron_head_neighbors(self, cell: Vector2D) -> int:
        return sum(
            self._get_state(n) == WireWorldState.ELECTRON_HEAD
            for n in self._neighbors(cell)
        )

    def _next_state(  # noqa: PLR6301
        self,
        cell_state: WireWorldState,
        neighbor_count: dict[WireWorldState, int],
    ) -> WireWorldState:
        if cell_state == WireWorldState.EMPTY:
            return WireWorldState.EMPTY
        elif cell_state == WireWorldState.ELECTRON_HEAD:
            return WireWorldState.ELECTRON_TAIL
        elif cell_state == WireWorldState.ELECTRON_TAIL:
            return WireWorldState.CONDUCTOR
        elif 1 <= neighbor_count.get(WireWorldState.ELECTRON_HEAD, 0) <= 2:
            return WireWorldState.ELECTRON_HEAD
        else:
            return WireWorldState.CONDUCTOR

    def next_iteration(self) -> "WireWorld":
        return WireWorld(cells=dict(self._cells_next_iteration()))
