from src.core.io_handler import IOHandler
from src.solutions.y2015.d19.logic.molecule_parser import (
    parse_medicine_molecule,
    parse_molecule_replacements,
)
from src.solutions.y2015.d19.logic.molecule_replacement import (
    neighboring_molecules,
)


def solve(io_handler: IOHandler) -> None:
    prob_id = 2015, 19
    input_reader = io_handler.input_reader(*prob_id)

    replacements = list(parse_molecule_replacements(input_reader))
    medicine_molecule = parse_medicine_molecule(input_reader)

    neighbors = set(neighboring_molecules(medicine_molecule, replacements))
    io_handler.write_result(*prob_id, part=1, result=len(neighbors))

    # BFS is way too slow
    # min_length = min_path_length_with_bfs(
    #     start_node="e",
    #     is_final_state=lambda molecule: molecule == medicine_molecule,
    #     neighbors=partial(neighboring_molecules, replacements=replacements),
    # )
    io_handler.write_result(*prob_id, part=2, result="not implemented")
