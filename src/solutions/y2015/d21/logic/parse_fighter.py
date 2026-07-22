from src.core.io_handler import InputReader
from src.solutions.shared.parser.csv_parser import parse_csv
from src.solutions.y2015.d21.logic.fighter import Fighter


def parse_fighter(reader: InputReader) -> Fighter:
    attributes = parse_csv(reader, separator=":")
    kwargs = {
        key.strip().lower().replace(" ", "_"): int(value)
        for key, value in attributes
    }
    return Fighter(**kwargs)
