from src.solutions.shared.geometry import Direction
from src.solutions.y2022.d09.logic.parser import parse_pull_motions
from src.solutions.y2022.d09.logic.pull_motion import PullMotion


def test_parse_pull_motions(input_reader):
    reader = input_reader("""R 5
                             U 8
                             L 8
                             D 3""")
    motions = list(parse_pull_motions(reader))
    assert motions == [
        PullMotion(Direction.RIGHT, num_steps=5),
        PullMotion(Direction.UP, num_steps=8),
        PullMotion(Direction.LEFT, num_steps=8),
        PullMotion(Direction.DOWN, num_steps=3),
    ]
