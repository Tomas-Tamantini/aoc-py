class CLIProgressMonitor:
    def __init__(self, year: int, day: int, part: int) -> None:
        self._year = year
        self._day = day
        self._part = part
        self._last_step = 0

    def _problem_id(self) -> str:
        return f"AOC {self._year}/{self._day:02d} - Part {self._part}"

    def estimate_remaining_time(self, estimation: str) -> None:
        msg = (
            f"{self._problem_id()}: Be patient, "
            f"it takes about {estimation} to run"
        )
        print(msg, end="\r")

    def update_progress_bar(
        self, current_step: int, total_steps: int, step_granularity: int = 1
    ) -> None:
        if abs(current_step - self._last_step) < step_granularity:
            return
        self._last_step = current_step
        progress = (current_step / total_steps) * 100
        bar_length = 40
        filled_length = int(bar_length * progress // 100)
        bar = "█" * filled_length + "-" * (bar_length - filled_length)
        msg = (
            f"{self._problem_id()}: [{bar}] {progress:.2f}% "
            f"({current_step}/{total_steps})"
        )
        print(msg, end="\r")
