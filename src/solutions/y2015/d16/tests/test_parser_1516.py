from src.solutions.y2015.d16.logic.aunt import Aunt
from src.solutions.y2015.d16.logic.parser import parse_aunts


def test_parse_aunts(input_reader):
    example = """
              Sue 1: goldfish: 9, cars: 0, samoyeds: 9
              Sue 2: perfumes: 5, trees: 8, goldfish: 8
              """
    aunties = list(parse_aunts(input_reader(example)))
    assert aunties == [
        Aunt(id=1, attributes={"goldfish": 9, "cars": 0, "samoyeds": 9}),
        Aunt(id=2, attributes={"perfumes": 5, "trees": 8, "goldfish": 8}),
    ]
