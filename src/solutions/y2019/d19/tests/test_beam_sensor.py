import pytest

from src.solutions.shared.geometry import Vector2D
from src.solutions.y2019.d19.logic.beam_sensor import BeamSensor


@pytest.fixture
def sensor() -> BeamSensor:
    instructions = [
        3,  # x = input()
        1000,
        3,  # y = input()
        1001,
        2,  # is_inside_beam = x * y
        1000,
        1001,
        1002,
        4,  # output(is_inside_beam)
        1002,
        99,
    ]
    return BeamSensor(instructions)


def test_beam_sensor_uses_intcode_program_to_check_if_inside_beam(sensor):
    assert not sensor.is_inside_beam(Vector2D(1, 0))
    assert sensor.is_inside_beam(Vector2D(1, 1))


def test_beam_sensor_runs_repeated_query_efficiently(sensor):
    for _ in range(10_000):
        sensor.is_inside_beam(Vector2D(1, 1))
