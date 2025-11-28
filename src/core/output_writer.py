from typing import Protocol

from src.core.result_checker import ResultReport


class OutputWriter(Protocol):
    def write_result_report(
        self, report: ResultReport, suggest_animation: bool, suggest_play: bool
    ) -> None: ...
