from src.core.result_checker import ResultReport


class CLIOutputWriter:
    @staticmethod
    def clear_line() -> None:
        print("\033[K", end="\r")

    @staticmethod
    def write_result_report(
        report: ResultReport, suggest_animation: bool, suggest_play: bool
    ) -> None:
        msg = (
            f"AOC {report.year}/{report.day:02d} - Part {report.part}: "
            f"{report.received}"
        )
        if not report.result_is_correct:
            if report.expected:
                msg += f" (ERROR: Expected {report.expected})"
            else:
                msg += " (ERROR: No expected result found)"
        if suggest_animation:
            msg += " (SET FLAG --animate TO SEE COOL ANIMATION)"
        if suggest_play:
            msg += " (SET FLAG --play TO PLAY AS INTERACTIVE GAME)"
        CLIOutputWriter.clear_line()
        print(msg)
