from src.solutions.y2025.d10.logic.machine import Machine
from src.solutions.y2025.d10.logic.parser import parse_machines


def test_parse_indicator_light_diagrams(input_reader):
    reader = input_reader(
        """
        [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
        [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
        """
    )
    diagrams = list(parse_machines(reader))
    assert diagrams == [
        Machine(
            target_indicator_lights=(False, True, True, False),
            button_wirings=((3,), (1, 3), (2,), (2, 3), (0, 2), (0, 1)),
            target_joltage=(3, 5, 4, 7),
        ),
        Machine(
            target_indicator_lights=(False, False, False, True, False),
            button_wirings=(
                (0, 2, 3, 4),
                (2, 3),
                (0, 4),
                (0, 1, 2),
                (1, 2, 3, 4),
            ),
            target_joltage=(7, 5, 12, 7, 2),
        ),
    ]
