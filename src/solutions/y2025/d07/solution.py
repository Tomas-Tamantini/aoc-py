from src.core.io_handler import IOHandler
from src.solutions.shared.parser.grid_parser import parse_grid
from src.solutions.y2025.d07.logic.beam_splitter import BeamSplitter


def solve(io_handler: IOHandler) -> None:
    prob_id = 2025, 7

    grid = parse_grid(io_handler.input_reader(*prob_id), y_grows_down=False)

    initial_beam_position = grid.positions("S").pop()
    splitter_positions = grid.positions("^")
    beam_splitter = BeamSplitter(splitter_positions)

    num_splits = beam_splitter.num_splits(initial_beam_position)
    io_handler.write_result(*prob_id, part=1, result=num_splits)

    num_timelines = beam_splitter.num_timelines(initial_beam_position)
    io_handler.write_result(*prob_id, part=2, result=num_timelines)
