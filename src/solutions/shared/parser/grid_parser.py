from src.core.input_reader import InputReader
from src.solutions.shared.geometry import Vector2D
from src.solutions.shared.parser.character_grid import CharacterGrid


def parse_grid(
    input_reader: InputReader, y_grows_down: bool = True
) -> CharacterGrid:
    lines = list(input_reader.read_stripped_lines())
    height = len(lines)
    pos_to_symbol: dict[Vector2D, str] = {}
    for y, line in enumerate(input_reader.read_stripped_lines()):
        for x, c in enumerate(line):
            y_coord = y if y_grows_down else height - 1 - y
            pos_to_symbol[Vector2D(x, y_coord)] = c
    return CharacterGrid(pos_to_symbol)
