from dataclasses import dataclass


@dataclass(frozen=True)
class RectangularBox:
    length: int
    width: int
    height: int

    def required_wrapping_paper(self) -> int:
        areas = [
            self.length * self.width,
            self.width * self.height,
            self.height * self.length,
        ]
        return 2 * sum(areas) + min(areas)

    def required_ribbon_length(self) -> int:
        perimeters = [
            2 * (self.length + self.width),
            2 * (self.width + self.height),
            2 * (self.height + self.length),
        ]
        volume = self.length * self.width * self.height
        return min(perimeters) + volume
