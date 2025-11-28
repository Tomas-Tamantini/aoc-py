from src.core.input_reader import InputReader
from src.solutions.shared.parser.csv_parser import parse_csv
from src.solutions.y2015.d22.logic.parser.boss_stats import BossStats


def _parse_arg_name(arg_name: str) -> str:
    return arg_name.strip().lower().replace(" ", "_")


def parse_boss_stats(input_reader: InputReader) -> BossStats:
    kwargs_reader = parse_csv(
        input_reader,
        separator=":",
        mapper=lambda v: (_parse_arg_name(v[0]), int(v[1])),
    )
    kwargs = {key: value for key, value in kwargs_reader}
    return BossStats(**kwargs)
