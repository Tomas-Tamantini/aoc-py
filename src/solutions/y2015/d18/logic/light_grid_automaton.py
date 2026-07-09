from src.solutions.shared.cellular_automata.game_of_life import GameOfLife
from src.solutions.shared.geometry import Vector2D


class LightGridAutomaton(GameOfLife):
    def __init__(
        self,
        width: int,
        height: int,
        alive_cells: set[Vector2D],
        corner_lights_always_on: bool = False,
    ) -> None:
        if corner_lights_always_on:
            alive_cells.update(self._corners(width, height))
        super().__init__(alive_cells=alive_cells)
        self._width = width
        self._height = height
        self._corner_lights_always_on = corner_lights_always_on

    @staticmethod
    def _corners(width: int, height: int) -> set[Vector2D]:
        return {
            Vector2D(0, 0),
            Vector2D(0, height - 1),
            Vector2D(width - 1, 0),
            Vector2D(width - 1, height - 1),
        }

    def _is_out_of_bounds(self, cell: Vector2D) -> bool:
        return not (0 <= cell.x < self._width and 0 <= cell.y < self._height)

    def _alive_cells_next_iteration(self) -> set[Vector2D]:
        next_alive_cells = super()._alive_cells_next_iteration()
        bounded = {
            c for c in next_alive_cells if not self._is_out_of_bounds(c)
        }
        if self._corner_lights_always_on:
            bounded.update(self._corners(self._width, self._height))
        return bounded

    def next_iteration(self) -> "LightGridAutomaton":
        return LightGridAutomaton(
            width=self._width,
            height=self._height,
            alive_cells=self._alive_cells_next_iteration(),
            corner_lights_always_on=self._corner_lights_always_on,
        )
