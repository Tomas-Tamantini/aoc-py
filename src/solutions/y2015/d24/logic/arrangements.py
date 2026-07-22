from itertools import combinations
from math import prod


def find_ideal_arrangement_qe(packages: list[int], num_groups: int) -> int:
    """
    Finds the quantum entanglement of the first group of packages in the ideal
    arrangement.
    """
    target_weight = sum(packages) // num_groups

    for i in range(1, len(packages) + 1):
        min_qe = float("inf")
        found_in_size = False
        for combo in combinations(packages, i):
            if sum(combo) == target_weight:
                # For this problem, it's stated that if a valid group is found,
                # a partition of the rest of the packages is always possible.
                # So we don't need to check the other groups.
                min_qe = min(min_qe, prod(combo))
                found_in_size = True
        if found_in_size:
            return min_qe  # type: ignore
    return -1
