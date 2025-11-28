from typing import Iterator

from src.solutions.shared.cellular_automata.binary_automaton import (
    BinaryCellularAutomaton,
)
from src.solutions.shared.geometry import Vector2D


class GameOfLife(BinaryCellularAutomaton[Vector2D]):
    def _neighbors(self, cell: Vector2D) -> Iterator[Vector2D]:  # noqa: PLR6301
        yield from cell.neighbors(include_diagonals=True)

    def _cell_is_alive_on_next_iteration(  # noqa: PLR6301
        self, current_cell_is_alive: bool, num_alive_neighbors: int
    ) -> bool:
        if current_cell_is_alive:
            return 2 <= num_alive_neighbors <= 3
        else:
            return num_alive_neighbors == 3

    def next_iteration(self) -> "GameOfLife":
        return GameOfLife(alive_cells=self._alive_cells_next_iteration())
