from typing import Optional

from src.core.animation_renderer import AnimationRenderer
from src.solutions.shared.geometry import Vector2D
from src.solutions.y2019.d13.logic.arcade_screen import ArcadeScreen
from src.solutions.y2019.d13.logic.tile_type import TileType


class ArcadeIO:
    def __init__(
        self,
        screen: ArcadeScreen,
        animation_renderer: Optional[AnimationRenderer] = None,
    ) -> None:
        self._screen = screen
        self._animation_renderer = animation_renderer
        self._output_buffer: list[int] = []

    def _process_output_triplet(self) -> None:
        if self._output_buffer[:2] == [-1, 0]:
            self._screen.set_score(self._output_buffer[-1])
        else:
            position = Vector2D(*self._output_buffer[:2])
            tile_type = TileType(self._output_buffer[-1])
            self._screen.set_tile(position, tile_type)
        if self._animation_renderer:
            frame = self._screen.render()
            self._animation_renderer.render_frame(frame, fps=240)

    def put(self, value: int) -> None:
        self._output_buffer.append(value)
        if len(self._output_buffer) == 3:
            self._process_output_triplet()
            self._output_buffer = []

    def read_next(self) -> int:
        ball_pos = self._screen.ball_position()
        paddle_pos = self._screen.paddle_position()
        dx = ball_pos.x - paddle_pos.x
        return 1 if dx > 0 else (0 if dx == 0 else -1)
