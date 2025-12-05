import argparse
import importlib
from typing import Callable

from src.cli.io_handler import CLIIOHandler
from src.cli.parse_problem_ids import parse_problem_ids
from src.core.io_handler import IOHandler


def _solver(year: int, day: int) -> Callable[[IOHandler], None]:
    module_path = f"src.solutions.y{year}.d{day:02d}.solution"
    solution_module = importlib.import_module(module_path)
    return solution_module.solve


def _solve(io_handler: IOHandler, year: int, day: int):
    try:
        run_solution = _solver(year, day)
        run_solution(io_handler)
    except ModuleNotFoundError:
        print(f"Solution for year {year}, day {day} not found.")
    except Exception as e:
        print(f"{year}/{day} ERROR: {e}")


def main():
    parser = argparse.ArgumentParser(description="Advent of Code Solutions")
    parser.add_argument(
        "--year", "-y", type=int, help="Year to solve (e.g., 2017, 2022)"
    )
    parser.add_argument("--day", "-d", type=int, help="Day to solve (1-25)")
    parser.add_argument(
        "--animate",
        "-a",
        action="store_true",
        help="Play cool animations for some solutions",
    )
    parser.add_argument(
        "--interactive",
        "-i",
        action="store_true",
        help="Play some solutions as interactive games",
    )
    parser.add_argument(
        "--profile",
        "-p",
        type=str,
        help="Profile name to use for data folder "
        "(e.g., 'tom' will use 'data/tom/' instead of 'data/')",
    )

    args = parser.parse_args()

    io_handler = CLIIOHandler(
        play_animations=args.animate,
        play_games=args.interactive,
        profile=args.profile,
    )

    for year, day in parse_problem_ids(args.year, args.day):
        _solve(io_handler, year, day)


if __name__ == "__main__":
    main()
