from src.solutions.shared.geometry import Vector2D
from src.solutions.y2025.d07.logic.beam_splitter import BeamSplitter

INITIAL_BEAM = Vector2D(7, 15)
SPLITTER = BeamSplitter(
    splitter_positions={
        Vector2D(7, 13),
        Vector2D(6, 11),
        Vector2D(8, 11),
        Vector2D(5, 9),
        Vector2D(7, 9),
        Vector2D(9, 9),
        Vector2D(4, 7),
        Vector2D(6, 7),
        Vector2D(10, 7),
        Vector2D(3, 5),
        Vector2D(5, 5),
        Vector2D(9, 5),
        Vector2D(11, 5),
        Vector2D(2, 3),
        Vector2D(6, 3),
        Vector2D(12, 3),
        Vector2D(1, 1),
        Vector2D(3, 1),
        Vector2D(5, 1),
        Vector2D(7, 1),
        Vector2D(9, 1),
        Vector2D(13, 1),
    }
)


def test_beam_splits_are_counted_once_each():
    assert SPLITTER.num_splits(INITIAL_BEAM) == 21


def test_beam_timelines_are_counted_once_each():
    assert SPLITTER.num_timelines(INITIAL_BEAM) == 40


def test_beam_timelines_are_counted_efficiently():
    initial_beam = Vector2D(15, 30)
    splitter_positions = {
        Vector2D(i, j)
        for i in range(30)
        for j in range(30)
        if (i + j) % 2 == 0
    }

    splitter = BeamSplitter(splitter_positions)
    assert splitter.num_timelines(initial_beam) == 534098305
