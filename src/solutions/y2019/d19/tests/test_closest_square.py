from src.solutions.shared.geometry import Vector2D
from src.solutions.y2019.d19.logic.closest_square import closest_square


class _MockBeamSensor:
    @staticmethod
    def is_inside_beam(position: Vector2D) -> bool:
        return position.y * 6 <= position.x * 7 <= position.y * 14


def test_closest_square_which_fits_inside_beam():
    square_size = 10
    beam_sensor = _MockBeamSensor()
    square_pos = closest_square(square_size, beam_sensor)
    assert square_pos == Vector2D(21, 15)
