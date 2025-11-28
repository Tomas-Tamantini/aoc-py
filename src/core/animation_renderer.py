from typing import Protocol


class AnimationRenderer(Protocol):
    def render_frame(self, frame: str, fps: int = 20) -> None: ...
