from src.solutions.shared.geometry import Direction, Vector2D


class BeamSplitter:
    def __init__(self, splitter_positions: set[Vector2D]) -> None:
        self._splitter_positions = splitter_positions

    def num_splits(self, initial_beam_position: Vector2D) -> int:
        visited = set()
        remaining_beams = {initial_beam_position}
        splits = 0
        while remaining_beams:
            beam = remaining_beams.pop()
            if beam.y <= 0 or beam in visited:
                continue
            visited.add(beam)
            if beam in self._splitter_positions:
                splits += 1
                remaining_beams.add(beam.move(Direction.LEFT))
                remaining_beams.add(beam.move(Direction.RIGHT))
            else:
                remaining_beams.add(beam.move(Direction.DOWN))

        return splits
