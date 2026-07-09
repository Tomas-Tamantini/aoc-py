from src.solutions.y2015.d17.logic.container_combination import (
    container_combinations,
)


def test_container_combinations_yields_all_combinations_that_sum_to_target():
    containers = (20, 15, 10, 5, 5)
    target = 25
    expected_combinations = [
        (5, 5, 15),
        (5, 20),
        (5, 20),
        (10, 15),
    ]
    actual_combinations = sorted(container_combinations(containers, target))
    assert actual_combinations == expected_combinations
