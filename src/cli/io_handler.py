from typing import Optional

from src.cli.animation_renderer import CLIAnimationRenderer
from src.cli.game_interface import CLIGameInterface
from src.cli.input_reader import TextFileInputReader
from src.cli.output_writer import CLIOutputWriter
from src.cli.progress_monitor import CLIProgressMonitor
from src.cli.result_checker import JsonResultChecker
from src.core.animation_renderer import AnimationRenderer
from src.core.game_interface import GameInterface
from src.core.input_reader import InputReader
from src.core.progress_monitor import ProgressMonitor


class CLIIOHandler:
    def __init__(
        self,
        play_animations: bool,
        play_games: bool,
        profile: Optional[str] = None,
    ):
        self._result_checker = JsonResultChecker(profile)
        self._output_writer = CLIOutputWriter()
        self._play_animations = play_animations
        self._play_games = play_games
        self._profile = profile

    def input_reader(
        self, year: int, day: int, file_name: Optional[str] = None
    ) -> InputReader:
        return TextFileInputReader(year, day, file_name, self._profile)

    def write_result(  # noqa: PLR0913, PLR0917
        self,
        year: int,
        day: int,
        part: int,
        result: int | str,
        supports_animation: bool = False,
        supports_play: bool = False,
    ) -> None:
        report = self._result_checker.check_result(
            year, day, part, str(result)
        )
        suggest_animation = supports_animation and not self._play_animations
        suggest_play = supports_play and not self._play_games
        self._output_writer.write_result_report(
            report, suggest_animation, suggest_play
        )

    @staticmethod
    def progress_monitor(year: int, day: int, part: int) -> ProgressMonitor:
        return CLIProgressMonitor(year, day, part)

    def animation_renderer(
        self, year: int, day: int, part: int
    ) -> Optional[AnimationRenderer]:
        if self._play_animations:
            return CLIAnimationRenderer(year, day, part)

    def game_interface(
        self, year: int, day: int, part: int
    ) -> Optional[GameInterface]:
        if self._play_games:
            return CLIGameInterface(year, day, part)
