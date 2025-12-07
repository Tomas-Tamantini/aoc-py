from src.solutions.shared.geometry import Vector2D
from src.solutions.y2025.d07.logic.beam_splitter import BeamSplitter


def test_beam_is_not_split_if_no_splitters():
    splitter = BeamSplitter(splitter_positions=set())
    beam_pos = Vector2D(5, 5)
    assert splitter.num_splits(beam_pos) == 0


def test_beam_is_split_once_if_single_splitter():
    splitter = BeamSplitter(splitter_positions={Vector2D(5, 3)})
    beam_pos = Vector2D(5, 5)
    assert splitter.num_splits(beam_pos) == 1


def test_beam_is_not_split_by_splitter_not_in_path():
    splitter = BeamSplitter(splitter_positions={Vector2D(4, 3)})
    beam_pos = Vector2D(5, 5)
    assert splitter.num_splits(beam_pos) == 0


def test_beam_splits_are_counted_only_once():
    splitter = BeamSplitter(
        splitter_positions={
            Vector2D(3, 5),
            Vector2D(2, 3),
            Vector2D(4, 3),
            Vector2D(3, 1),
        }
    )
    beam_pos = Vector2D(3, 7)
    assert splitter.num_splits(beam_pos) == 4
