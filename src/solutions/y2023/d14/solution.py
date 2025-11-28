from src.core.io_handler import IOHandler
from src.solutions.shared.geometry import Direction
from src.solutions.shared.parser import parse_grid
from src.solutions.y2023.d14.logic.parabolic_dish import ParabolicDish
from src.solutions.y2023.d14.logic.run_cycle import run_cycle


def _calculate_load(dish: ParabolicDish) -> int:
    return sum(r.y + 1 for r in dish.rounded_rock_positions)


def solve(io_handler: IOHandler) -> None:
    prob_id = 2023, 14

    grid = parse_grid(io_handler.input_reader(*prob_id), y_grows_down=False)

    dish = ParabolicDish(
        width=grid.width,
        height=grid.height,
        cube_rock_positions=grid.positions("#"),
        rounded_rock_positions=grid.positions("O"),
    )

    load_p1 = _calculate_load(dish.tilt(Direction.UP))
    io_handler.write_result(*prob_id, part=1, result=load_p1)

    io_handler.progress_monitor(*prob_id, part=2).estimate_remaining_time(
        estimation="30s"
    )
    load_p2 = _calculate_load(
        run_cycle(
            dish,
            cycle=(
                Direction.UP,
                Direction.LEFT,
                Direction.DOWN,
                Direction.RIGHT,
            ),
            num_cycles=1_000_000_000,
        )
    )
    io_handler.write_result(*prob_id, part=2, result=load_p2)
