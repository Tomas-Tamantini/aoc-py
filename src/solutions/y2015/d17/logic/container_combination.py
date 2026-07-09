from typing import Iterator


def container_combinations(
    containers: tuple[int, ...], target: int
) -> Iterator[tuple[int, ...]]:
    sorted_containers = tuple(sorted(containers))
    if target == 0:
        yield ()
    elif sorted_containers and target >= sorted_containers[0]:
        for combination in container_combinations(
            sorted_containers[1:], target - sorted_containers[0]
        ):
            yield (sorted_containers[0],) + combination
        yield from container_combinations(sorted_containers[1:], target)
