from typing import Optional, Protocol

from src.core.animation_renderer import AnimationRenderer
from src.core.game_interface import GameInterface
from src.core.input_reader import InputReader
from src.core.progress_monitor import ProgressMonitor


class IOHandler(Protocol):
    def input_reader(
        self, year: int, day: int, file_name: Optional[str] = None
    ) -> InputReader: ...

    # TODO: Improve function definition to avoid so many args
    def write_result(  # noqa: PLR0913, PLR0917
        self,
        year: int,
        day: int,
        part: int,
        result: int | str,
        supports_animation: bool = False,
        supports_play: bool = False,
    ) -> None: ...

    def progress_monitor(
        self, year: int, day: int, part: int
    ) -> ProgressMonitor: ...

    def animation_renderer(
        self, year: int, day: int, part: int
    ) -> Optional[AnimationRenderer]: ...

    def game_interface(
        self, year: int, day: int, part: int
    ) -> Optional[GameInterface]: ...
