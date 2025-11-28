from json import load
from os.path import join

from src.core.result_checker import ResultReport


class JsonResultChecker:
    def __init__(self) -> None:
        self._expected_results: dict[tuple[int, ...], str] = dict()

    def _load_solution(self, year: int, day: int) -> None:
        file_path = join(
            "src",
            "solutions",
            f"y{year}",
            f"d{day:02d}",
            "data",
            "results.json",
        )
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = load(file)
                for part in (1, 2):
                    if (result := data.get(f"part{part}")) is not None:
                        self._expected_results[(year, day, part)] = str(result)
        except (FileNotFoundError, ValueError):
            pass

    def _expected_result(self, year: int, day: int, part: int) -> str:
        lookup_key = year, day, part
        if lookup_key not in self._expected_results:
            self._load_solution(year, day)
        return str(
            self._expected_results.get(
                lookup_key, "<Could not load expected value>"
            )
        )

    def check_result(
        self, year: int, day: int, part: int, result: str
    ) -> ResultReport:
        expected = self._expected_result(year, day, part)
        return ResultReport(year, day, part, result, expected)
