from src.solutions.y2015.d24.logic.arrangements import (
    find_ideal_arrangement_qe,
)


def test_find_ideal_arrangement_qe_part1():
    packages = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
    assert find_ideal_arrangement_qe(packages, 3) == 99


def test_find_ideal_arrangement_qe_part2():
    packages = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
    assert find_ideal_arrangement_qe(packages, 4) == 44
