from typing import Iterator

from src.solutions.shared.cellular_automata.binary_automaton import (
    BinaryCellularAutomaton,
)
from src.solutions.shared.geometry import HexagonalCoordinates


class HexagonalAutomaton(BinaryCellularAutomaton[HexagonalCoordinates]):
    def num_black_tiles(self) -> int:
        return len(self.alive_cells())

    def _neighbors(  # noqa: PLR6301
        self, cell: HexagonalCoordinates
    ) -> Iterator[HexagonalCoordinates]:
        yield from cell.neighbors()

    def _cell_is_alive_on_next_iteration(  # noqa: PLR6301
        self, current_cell_is_alive: bool, num_alive_neighbors: int
    ) -> bool:
        if current_cell_is_alive:
            return 1 <= num_alive_neighbors <= 2
        else:
            return num_alive_neighbors == 2

    def next_iteration(self) -> "HexagonalAutomaton":
        return HexagonalAutomaton(
            alive_cells=self._alive_cells_next_iteration()
        )
