from dataclasses import dataclass

import numpy as np

from src.solutions.shared.geometry import BoundingBox


class LightGrid:
    def __init__(self, width: int, height: int):
        self._lights = np.zeros((width, height), dtype=int)

    def total_brightness(self) -> int:
        return np.sum(self._lights)

    def _sub_region(self, region: BoundingBox) -> np.ndarray:
        return self._lights[
            region.min_x : region.max_x + 1, region.min_y : region.max_y + 1
        ]

    def turn_on(self, region: BoundingBox) -> None:
        self._sub_region(region)[:] = 1

    def turn_off(self, region: BoundingBox) -> None:
        self._sub_region(region)[:] = 0

    def toggle(self, region: BoundingBox) -> None:
        self._sub_region(region)[:] ^= 1

    def increase_brightness(
        self, region: BoundingBox, increase_amount: int
    ) -> None:
        self._sub_region(region)[:] += increase_amount

    def decrease_brightness(self, region: BoundingBox) -> None:
        sub = self._sub_region(region)
        sub -= 1
        sub[sub < 0] = 0


@dataclass(frozen=True)
class LightGridInstruction:
    region: BoundingBox

    def apply(self, grid: LightGrid) -> None:
        raise NotImplementedError(
            "This method should be implemented by subclasses."
        )


@dataclass(frozen=True)
class TurnOnInstruction(LightGridInstruction):
    def apply(self, grid: LightGrid) -> None:
        grid.turn_on(self.region)


@dataclass(frozen=True)
class TurnOffInstruction(LightGridInstruction):
    def apply(self, grid: LightGrid) -> None:
        grid.turn_off(self.region)


@dataclass(frozen=True)
class ToggleInstruction(LightGridInstruction):
    def apply(self, grid: LightGrid) -> None:
        grid.toggle(self.region)


@dataclass(frozen=True)
class IncreaseBrightnessInstruction(LightGridInstruction):
    increase_amount: int

    def apply(self, grid: LightGrid) -> None:
        grid.increase_brightness(self.region, self.increase_amount)


@dataclass(frozen=True)
class DecreaseBrightnessInstruction(LightGridInstruction):
    def apply(self, grid: LightGrid) -> None:
        grid.decrease_brightness(self.region)
