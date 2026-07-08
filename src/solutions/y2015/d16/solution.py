from src.core.io_handler import IOHandler
from src.solutions.y2015.d16.logic.aunt import (
    Constraint,
    ConstraintType,
    matching_aunt,
)
from src.solutions.y2015.d16.logic.parser import parse_aunts


def _constraints(part: int) -> list[Constraint]:
    if part == 1:
        return [
            Constraint("children", ConstraintType.EQUAL, 3),
            Constraint("cats", ConstraintType.EQUAL, 7),
            Constraint("samoyeds", ConstraintType.EQUAL, 2),
            Constraint("pomeranians", ConstraintType.EQUAL, 3),
            Constraint("akitas", ConstraintType.EQUAL, 0),
            Constraint("vizslas", ConstraintType.EQUAL, 0),
            Constraint("goldfish", ConstraintType.EQUAL, 5),
            Constraint("trees", ConstraintType.EQUAL, 3),
            Constraint("cars", ConstraintType.EQUAL, 2),
            Constraint("perfumes", ConstraintType.EQUAL, 1),
        ]
    else:
        return [
            Constraint("children", ConstraintType.EQUAL, 3),
            Constraint("cats", ConstraintType.GREATER_THAN, 7),
            Constraint("samoyeds", ConstraintType.EQUAL, 2),
            Constraint("pomeranians", ConstraintType.LESS_THAN, 3),
            Constraint("akitas", ConstraintType.EQUAL, 0),
            Constraint("vizslas", ConstraintType.EQUAL, 0),
            Constraint("goldfish", ConstraintType.LESS_THAN, 5),
            Constraint("trees", ConstraintType.GREATER_THAN, 3),
            Constraint("cars", ConstraintType.EQUAL, 2),
            Constraint("perfumes", ConstraintType.EQUAL, 1),
        ]


def solve(io_handler: IOHandler) -> None:
    prob_id = 2015, 16

    aunts = list(parse_aunts(io_handler.input_reader(*prob_id)))

    aunt_p1 = matching_aunt(aunts, _constraints(part=1))
    io_handler.write_result(*prob_id, part=1, result=aunt_p1.id)

    aunt_p2 = matching_aunt(aunts, _constraints(part=2))
    io_handler.write_result(*prob_id, part=2, result=aunt_p2.id)
