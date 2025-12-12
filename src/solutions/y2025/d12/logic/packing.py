from dataclasses import dataclass

from src.solutions.shared.geometry import Vector2D


@dataclass(frozen=True)
class Shape:
    id: int
    cells: set[Vector2D]

    @property
    def num_cells(self) -> int:
        return len(self.cells)


@dataclass(frozen=True)
class Region:
    width: int
    height: int
    shape_requirements: dict[int, int]

    def can_be_packed(self, shapes: dict[int, Shape]) -> int:
        area_available = self.width * self.height
        area_required = sum(
            amount * shapes[id].num_cells
            for id, amount in self.shape_requirements.items()
        )
        return area_available >= area_required
