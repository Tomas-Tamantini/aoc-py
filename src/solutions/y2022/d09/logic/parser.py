from typing import Iterator

from src.core.input_reader import InputReader
from src.solutions.shared.parser import DIRECTION_URDL, parse_csv
from src.solutions.y2022.d09.logic.pull_motion import PullMotion


def parse_pull_motions(input_reader: InputReader) -> Iterator[PullMotion]:
    return parse_csv(
        input_reader,
        separator=" ",
        mapper=lambda v: PullMotion(
            direction=DIRECTION_URDL[v[0]], num_steps=int(v[1])
        ),
    )
