from copy import deepcopy

from src.core.io_handler import IOHandler
from src.solutions.y2015.d13.logic.happiness_offset import max_happiness_offset
from src.solutions.y2015.d13.logic.parser import parse_happiness_graph


def solve(io_handler: IOHandler) -> None:
    prob_id = 2015, 13

    graph = parse_happiness_graph(io_handler.input_reader(*prob_id))
    happiness_1 = max_happiness_offset(graph)
    io_handler.write_result(*prob_id, part=1, result=happiness_1)

    new_graph = deepcopy(graph)
    for person in graph.nodes():
        new_graph.add_edge("Me", person, 0)
    happiness_2 = max_happiness_offset(new_graph)
    io_handler.write_result(*prob_id, part=2, result=happiness_2)
