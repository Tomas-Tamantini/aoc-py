from typing import Iterator

from src.core.input_reader import InputReader
from src.solutions.y2015.d15.logic.ingredient import Ingredient


def _parse_ingredient(line: str) -> Ingredient:
    _, properties_str = line.split(": ")
    properties = {}
    for property_str in properties_str.split(", "):
        property_name, property_value = property_str.split(" ")
        properties[property_name] = int(property_value)
    return Ingredient(**properties)


def parse_ingredients(reader: InputReader) -> Iterator[Ingredient]:
    for line in reader.read_stripped_lines():
        yield _parse_ingredient(line)
