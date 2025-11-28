from src.solutions.shared.geometry import Vector2D
from src.solutions.y2022.d09.logic.rope import Rope


class RopeAnimation:
    def __init__(self, num_frames: int) -> None:
        self._width = 50
        self._height = 15
        self._padding = 3
        self._camera_offset = Vector2D(-self._width, -self._height) // 2
        self._current_step = 0
        self._total_steps = num_frames
        self._visited_by_tail: set[Vector2D] = set()

    @staticmethod
    def _is_landscape_marker(pos: Vector2D) -> bool:
        # 'Random' landscape markers spread about
        return (pos.x + pos.y * pos.y) % 31 == (pos.x * pos.y) % 19

    @staticmethod
    def _constrain_number(
        original_number: int, min_value: int, max_value: int
    ) -> int:
        return min(max(original_number, min_value), max_value)

    def _reposition_camera(self, head_pos: Vector2D) -> None:
        next_x = self._constrain_number(
            self._camera_offset.x,
            min_value=head_pos.x + self._padding + 1 - self._width,
            max_value=head_pos.x - self._padding,
        )
        next_y = self._constrain_number(
            self._camera_offset.y,
            min_value=head_pos.y + self._padding + 1 - self._height,
            max_value=head_pos.y - self._padding,
        )
        self._camera_offset = Vector2D(next_x, next_y)

    def _pixel_value(self, pos: Vector2D, rope: Rope) -> str:
        if pos == rope.head:
            return "X"
        elif pos in rope.knots_head_to_tail:
            return "O"
        elif pos in self._visited_by_tail:
            return "~"
        elif self._is_landscape_marker(pos):
            return "*"
        else:
            return "."

    def build_frame(self, rope: Rope) -> str:
        frame = []
        self._reposition_camera(rope.head)
        for y in range(
            self._camera_offset.y, self._camera_offset.y + self._height
        ):
            row = []
            for x in range(
                self._camera_offset.x, self._camera_offset.x + self._width
            ):
                row.append(self._pixel_value(pos=Vector2D(x, y), rope=rope))
            frame.append("".join(row))
        frame.append("")
        frame.append(self._footer())
        self._current_step += 1
        self._visited_by_tail.add(rope.tail)
        return "\n".join(frame)

    def _footer(self) -> str:
        labels = [
            "Head (X)",
            "Body (O)",
            f"Visited by Tail (~): {len(self._visited_by_tail)}",
            f"Iteration: {self._current_step}/{self._total_steps}",
        ]
        return ", ".join(labels)
