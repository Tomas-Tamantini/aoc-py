from typing import Protocol


class ProgressMonitor(Protocol):
    def estimate_remaining_time(self, estimation: str) -> None: ...

    def update_progress_bar(
        self, current_step: int, total_steps: int, step_granularity: int = 1
    ) -> None: ...
