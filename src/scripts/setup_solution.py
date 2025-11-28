import argparse
import os


def _solution_file_content(year: int, day: int) -> str:
    return (
        "from src.core.io_handler import IOHandler\n\n\n"
        "def solve(io_handler: IOHandler) -> None:\n"
        f"    prob_id = {year}, {day}\n\n"
        "    io_handler.write_result(*prob_id, part=1,"
        ' result="not implemented")\n'
        "    io_handler.write_result(*prob_id, part=2,"
        ' result="not implemented")\n'
    )


def _expected_results_file_content() -> str:
    return '{\n    "part1": 0,\n    "part2": 0\n}'


def _create_file(path: str, content: str = "") -> None:
    if not os.path.exists(path):
        with open(path, "w", encoding="UTF-8") as f:
            f.write(content)


def _create_solution(year: int, day: int) -> None:
    solution_folder_path = ["src", "solutions", f"y{year}", f"d{day:02d}"]
    os.makedirs(os.path.join(*solution_folder_path), exist_ok=True)

    solution_file_path = os.path.join(*solution_folder_path, "solution.py")
    _create_file(solution_file_path, _solution_file_content(year, day))

    data_folder_path = solution_folder_path + ["data"]
    os.makedirs(os.path.join(*data_folder_path), exist_ok=True)

    input_file_path = os.path.join(*data_folder_path, "input.txt")
    _create_file(input_file_path)

    expected_results_file_path = os.path.join(
        *data_folder_path, "results.json"
    )
    _create_file(expected_results_file_path, _expected_results_file_content())

    print(f"Module created at {'/'.join(solution_folder_path)}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--year",
        "-y",
        type=int,
        help="Problem year (e.g., 2017, 2022)",
        required=True,
    )
    parser.add_argument(
        "--day", "-d", type=int, help="Problem day (1-25)", required=True
    )

    args = parser.parse_args()

    _create_solution(args.year, args.day)


if __name__ == "__main__":
    main()
