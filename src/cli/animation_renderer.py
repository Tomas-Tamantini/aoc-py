import time


class CLIAnimationRenderer:
    def __init__(self, year: int, day: int, part: int) -> None:
        self._year = year
        self._day = day
        self._part = part

    @staticmethod
    def render_frame(frame: str, fps: int = 20) -> None:
        num_lines = frame.count("\n")
        print(frame)
        LINE_UP = "\033[1A"
        LINE_CLEAR = "\x1b[2K"
        time.sleep(1.0 / fps)
        for _ in range(num_lines + 1):
            print(LINE_UP, end=LINE_CLEAR)
