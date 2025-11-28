from src.solutions.shared.geometry import Vector2D


class Hull:
    def __init__(self) -> None:
        self._panels_painted_at_least_once: set[Vector2D] = set()
        self._white_panels: set[Vector2D] = set()

    @property
    def num_panels_painted_at_least_once(self) -> int:
        return len(self._panels_painted_at_least_once)

    @property
    def white_panels(self) -> set[Vector2D]:
        return self._white_panels

    def paint_panel(self, position: Vector2D, paint_white: bool) -> None:
        self._panels_painted_at_least_once.add(position)
        if paint_white:
            self._white_panels.add(position)
        else:
            self._white_panels.discard(position)
