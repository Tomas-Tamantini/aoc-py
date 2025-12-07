from functools import cache
from typing import Iterator

from src.solutions.shared.geometry import Direction, Vector2D


class BeamSplitter:
    def __init__(self, splitter_positions: set[Vector2D]) -> None:
        self._splitter_positions = splitter_positions

    def _next_beams(self, beam: Vector2D) -> Iterator[Vector2D]:
        if beam in self._splitter_positions:
            yield beam.move(Direction.LEFT)
            yield beam.move(Direction.RIGHT)
        else:
            yield beam.move(Direction.DOWN)

    def num_splits(self, beam: Vector2D) -> int:
        visited = set()
        remaining_beams = {beam}
        splits = 0
        while remaining_beams:
            current_beam = remaining_beams.pop()
            if current_beam.y <= 0 or current_beam in visited:
                continue
            visited.add(current_beam)
            if current_beam in self._splitter_positions:
                splits += 1
            for next_beam in self._next_beams(current_beam):
                remaining_beams.add(next_beam)

        return splits

    @cache
    def num_timelines(self, beam: Vector2D) -> int:
        if beam.y <= 0:
            return 1
        else:
            return sum(
                self.num_timelines(next_beam)
                for next_beam in self._next_beams(beam)
            )
