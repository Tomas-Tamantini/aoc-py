import os
from typing import Iterator, Optional


def _get_available_years() -> list[int]:
    solutions_dir = os.path.join("src", "solutions")
    years: list[int] = []
    for item in os.listdir(solutions_dir):
        if item.startswith("y") and os.path.isdir(
            os.path.join(solutions_dir, item)
        ):
            try:
                year = int(item[1:])
                years.append(year)
            except ValueError:
                continue
    return sorted(years)


def _get_available_days(year: int) -> list[int]:
    year_dir = os.path.join("src", "solutions", f"y{year}")
    if not os.path.exists(year_dir):
        return []

    days: list[int] = []
    for item in os.listdir(year_dir):
        if item.startswith("d") and os.path.isdir(
            os.path.join(year_dir, item)
        ):
            try:
                day = int(item[1:])
                days.append(day)
            except ValueError:
                continue
    return sorted(days)


def parse_problem_ids(
    year: Optional[int], day: Optional[int]
) -> Iterator[tuple[int, int]]:
    if year is not None and day is not None:
        yield (year, day)
    elif year is not None:
        for d in _get_available_days(year):
            yield (year, d)
    elif day is not None:
        for y in _get_available_years():
            yield (y, day)
    else:
        for y in _get_available_years():
            for d in _get_available_days(y):
                yield (y, d)
