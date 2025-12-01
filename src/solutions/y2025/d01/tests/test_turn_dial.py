from src.solutions.y2025.d01.logic.turn_dial import (
    TurnDial,
    num_times_clicked_zero,
    num_times_landed_in_zero,
)

DIAL = TurnDial(size=100, start_position=50)
OFFSETS = [-50, -10, 1000, -90]


def test_turn_dial_keeps_track_of_times_it_landed_on_zero():
    assert num_times_landed_in_zero(DIAL, OFFSETS) == 2


def test_turn_dial_keeps_track_of_times_it_clicked_zero():
    assert num_times_clicked_zero(DIAL, OFFSETS) == 12
