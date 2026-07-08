from src.solutions.y2015.d16.logic.aunt import (
    Aunt,
    Constraint,
    ConstraintType,
    matching_aunt,
)

_AUNT_1 = Aunt(id=1, attributes={"cats": 7, "trees": 3})
_AUNT_2 = Aunt(id=2, attributes={"trees": 4, "children": 2})


def test_constraint_is_satisfied_by_missing_attribute():
    constraint = Constraint("cats", ConstraintType.EQUAL, 7)
    assert constraint.is_satisfied(_AUNT_2)


def test_equality_constraint_checks_for_exact_match():
    constraint = Constraint("trees", ConstraintType.EQUAL, 3)
    assert constraint.is_satisfied(_AUNT_1)
    assert not constraint.is_satisfied(_AUNT_2)


def test_greater_than_constraint_checks_for_greater_value():
    constraint = Constraint("trees", ConstraintType.GREATER_THAN, 3)
    assert constraint.is_satisfied(_AUNT_2)
    assert not constraint.is_satisfied(_AUNT_1)


def test_less_than_constraint_checks_for_smaller_value():
    constraint = Constraint("trees", ConstraintType.LESS_THAN, 4)
    assert constraint.is_satisfied(_AUNT_1)
    assert not constraint.is_satisfied(_AUNT_2)


def test_matching_aunt_returns_the_first_aunt_that_satisfies_all_constraints():
    constraints = [
        Constraint("cats", ConstraintType.EQUAL, 7),
        Constraint("trees", ConstraintType.GREATER_THAN, 3),
    ]
    matching = matching_aunt([_AUNT_1, _AUNT_2], constraints)
    assert matching == _AUNT_2
