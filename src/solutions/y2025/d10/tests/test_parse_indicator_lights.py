from src.solutions.y2025.d10.logic.parser import (
    IndicatorLightsDiagram,
    parse_indicator_lights_diagrams,
)


def test_parse_indicator_light_diagrams(input_reader):
    reader = input_reader(
        """
        [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
        [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
        """
    )
    diagrams = list(parse_indicator_lights_diagrams(reader))
    assert diagrams == [
        IndicatorLightsDiagram(
            target_configuration=0b0110,
            buttons={0b0001, 0b0101, 0b0010, 0b0011, 0b1010, 0b1100},
        ),
        IndicatorLightsDiagram(
            target_configuration=0b00010,
            buttons={0b10111, 0b00110, 0b10001, 0b11100, 0b01111},
        ),
    ]
